"""Parse a WinKFP .0DA/.0PA (Intel HEX with ';' header) into a binary + range list."""
import sys, re

path = sys.argv[1]
out = sys.argv[2] if len(sys.argv) > 2 else None
mem = {}
base = 0
seg = 0
hdr = []
for ln in open(path, "r", encoding="latin-1"):
    ln = ln.strip()
    if ln.startswith(";"):
        if ln.strip(";=").strip():
            hdr.append(ln)
        continue
    if not ln.startswith(":"):
        continue
    raw = bytes.fromhex(ln[1:])
    n, addr, typ = raw[0], raw[1] << 8 | raw[2], raw[3]
    data = raw[4:4 + n]
    if (sum(raw) & 0xFF) != 0:
        print("checksum error:", ln)
    if typ == 0:
        a = base + seg + addr
        for i, b in enumerate(data):
            mem[a + i] = b
    elif typ == 2:
        seg = (data[0] << 8 | data[1]) << 4
    elif typ == 4:
        base = (data[0] << 8 | data[1]) << 16
    elif typ == 1:
        break

print("\n".join(hdr))
addrs = sorted(mem)
ranges = []
for a in addrs:
    if ranges and a == ranges[-1][1] + 1:
        ranges[-1][1] = a
    else:
        ranges.append([a, a])
print(f"\n{len(mem)} bytes in {len(ranges)} ranges:")
for s, e in ranges:
    print(f"  {s:06X}-{e:06X} ({e-s+1} B)")
if out:
    lo, hi = addrs[0], addrs[-1]
    img = bytearray(b"\xff" * (hi + 1))
    for a, b in mem.items():
        img[a] = b
    open(out, "wb").write(img)
    print("wrote", out, len(img), "bytes (FF-filled from 0)")
    for m in re.finditer(rb"[\x20-\x7e]{8,}", img):
        print(f"  str {m.start():06X} {m.group().decode()[:80]}")
