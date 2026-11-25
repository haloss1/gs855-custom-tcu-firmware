"""GS8.55 (E39 M62, B22P0_xx) flash reader over DS2/K-line with a K+DCAN cable.

Reading uses the EGS diagnostic service 0x06 (SPEICHER_LESEN) with memory type 0x00,
which returns the external flash at 0x000000-0x03FFFF. No bootloader or security
access is needed. Writing is NOT implemented: it needs the 10GD855 programming
protocol (seed/key + K2 flash mode), which is not available yet.

Usage:
  python gs855tool.py ident  [--port COM1]
  python gs855tool.py read   [--port COM1] [--region all|boot|cal|prog] [--out file.bin]
  python gs855tool.py read   --start 0x4000 --end 0x10000 [--out cal.bin]
  python gs855tool.py read   --region cal --into full.bin      (patch range into a 256 KB image)
  python gs855tool.py verify file.bin [--start 0x0]             (compare file with the unit)
"""
import argparse, datetime, hashlib, os, re, sys, time
from ds2 import DS2, DS2Error

EGS = 0x32
FLASH_SIZE = 0x40000
MAX_BLOCK = 0xFB  # 251 bytes: largest that fits a DS2 frame
REGIONS = {  # from bench dumps of B22P0_22 and reads of B22P0_24
    "all":  (0x00000, 0x40000),
    "boot": (0x00000, 0x04000),
    "cal":  (0x04000, 0x10000),
    "prog": (0x10000, 0x40000),
}


def num(s):
    return int(s, 0)


def read_mem(d, addr, n, mtype=0x00):
    st, data = d.request(EGS, [0x06, mtype, addr >> 16 & 0xFF, addr >> 8 & 0xFF, addr & 0xFF, n])
    if st != 0xA0:
        raise DS2Error(f"read {addr:06X}+{n} rejected, status {st:02X}")
    if len(data) != n:
        raise DS2Error(f"read {addr:06X}: got {len(data)} of {n} bytes")
    return data


def read_range(d, start, end, block, progress=True):
    out = bytearray()
    addr = start
    t0 = time.time()
    while addr < end:
        n = min(block, end - addr)
        for attempt in range(5):
            try:
                chunk = read_mem(d, addr, n)
                break
            except DS2Error as e:
                if attempt == 4:
                    raise
                print(f"\n  retry {addr:06X}: {e}", file=sys.stderr)
                time.sleep(0.5)
        out += chunk
        addr += n
        if progress:
            done = addr - start
            rate = done / max(time.time() - t0, 1e-6)
            eta = (end - addr) / rate if rate else 0
            print(f"\r  {addr:06X}  {100*done/(end-start):5.1f}%  {rate:5.0f} B/s  ETA {eta:4.0f}s",
                  end="", flush=True)
    if progress:
        print()
    return bytes(out)


def ident(d):
    st, data = d.request(EGS, [0x00])
    if st != 0xA0:
        raise DS2Error(f"ident rejected, status {st:02X}")
    a = data.decode("ascii", "replace")
    info = {"bmw_nr": a[0:7], "hw_nr": a[7:9], "coding_idx": a[9:11], "diag_idx": a[11:13],
            "bus_idx": a[13:15], "date_week": a[15:17], "date_year": a[17:19], "raw": a}
    blk = read_mem(d, 0x03F796, 64)
    m = re.match(rb"(B\d\dP\d_\d\d)", blk)
    info["hw_id"] = m.group(1).decode() if m else "?"
    info["flash_ident"] = blk.decode("ascii", "replace").rstrip("\xff")
    return info


def open_ds2(a):
    return DS2(a.port)


def cmd_ident(a):
    d = open_ds2(a)
    try:
        for k, v in ident(d).items():
            print(f"{k:12} {v}")
    finally:
        d.close()


def resolve_range(a):
    if a.start is not None or a.end is not None:
        start = a.start or 0
        end = a.end if a.end is not None else FLASH_SIZE
    else:
        start, end = REGIONS[a.region]
    if not (0 <= start < end <= FLASH_SIZE):
        sys.exit(f"bad range {start:#x}-{end:#x} (flash is 0x0-{FLASH_SIZE:#x})")
    return start, end


def cmd_read(a):
    start, end = resolve_range(a)
    d = open_ds2(a)
    try:
        info = ident(d)
        print(f"EGS {info['bmw_nr']}  {info['hw_id']}  reading {start:06X}-{end:06X} ({end-start} bytes)")
        data = read_range(d, start, end, a.block)
        if a.verify:
            print("verifying (second pass)...")
            again = read_range(d, start, end, a.block)
            if again != data:
                bad = next(i for i in range(len(data)) if data[i] != again[i])
                sys.exit(f"VERIFY FAILED: first mismatch at {start+bad:06X}; nothing saved")
    finally:
        d.close()

    if a.into:
        img = bytearray(open(a.into, "rb").read()) if os.path.exists(a.into) else bytearray(b"\xff" * FLASH_SIZE)
        if len(img) != FLASH_SIZE:
            sys.exit(f"{a.into} is {len(img)} bytes, expected {FLASH_SIZE}")
        img[start:end] = data
        out, blob = a.into, bytes(img)
    else:
        if a.out:
            out = a.out
        else:
            ts = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            tag = a.region if a.start is None and a.end is None else f"{start:06X}-{end:06X}"
            out = f"GS855_{info['hw_id']}_{info['bmw_nr']}_{tag}_{ts}.bin"
        blob = data
    with open(out, "wb") as f:
        f.write(blob)
    print(f"saved {out}  ({len(blob)} bytes, md5 {hashlib.md5(blob).hexdigest()})")


def cmd_verify(a):
    blob = open(a.file, "rb").read()
    start = a.start or 0
    end = start + len(blob)
    if end > FLASH_SIZE:
        sys.exit("file does not fit in flash at that start address")
    d = open_ds2(a)
    try:
        live = read_range(d, start, end, a.block)
    finally:
        d.close()
    diffs = [i for i in range(len(blob)) if blob[i] != live[i]]
    if not diffs:
        print("identical")
        return
    print(f"{len(diffs)} bytes differ; first at {start+diffs[0]:06X}")
    sys.exit(1)


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--port", default="COM1")
    p.add_argument("--block", type=num, default=0x80, help="bytes per request (1-251, default 128)")
    sub = p.add_subparsers(dest="cmd", required=True)
    sub.add_parser("ident")
    r = sub.add_parser("read")
    r.add_argument("--region", choices=REGIONS, default="all")
    r.add_argument("--start", type=num)
    r.add_argument("--end", type=num, help="exclusive")
    r.add_argument("--out")
    r.add_argument("--into", help="patch the range into this 256 KB image (created FF-filled if missing)")
    r.add_argument("--verify", action="store_true", help="read twice and compare before saving")
    v = sub.add_parser("verify")
    v.add_argument("file")
    v.add_argument("--start", type=num)
    a = p.parse_args()
    if not 1 <= a.block <= MAX_BLOCK:
        sys.exit("--block must be 1-251")
    {"ident": cmd_ident, "read": cmd_read, "verify": cmd_verify}[a.cmd](a)


if __name__ == "__main__":
    main()
