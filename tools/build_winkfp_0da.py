"""Build a WinKFP data file for the GS8.55 by re-filling BMW's own G1423170.0DA.

1. Self-test: refill G1423170.0DA with the car's STOCK read -> must equal BMW's file byte for byte.
2. Port: refill with the Alpina-port image. The unused padding bytes 0xFFCC/0xFFCD (FF in BMW's
   file and in the car) are searched so that the file's $CHECKSUMME (CRC-16/ARC) lands on a value
   whose check character is known from BMW's own files. The TCU's own CRC at 0xFFFE
   (CRC-16 table 0x10C68 over 0x8000-0xFFCD) is recomputed for every candidate.
Everything else (header, $REFERENZ line and its check char, record layout) stays BMW's."""
import json, os, sys
import gs855_crc

BMW = "G1423170_bmw_original.0DA"   # BMW's data file for ZB 1423169, from your own ISTA/P
STOCK = "GS855_B22P0_24_1423159_full.bin"
PORT = sys.argv[1] if len(sys.argv) > 1 else "GS855_B22P0_24_1423159_ALPINA_PORT.bin"
OUT = sys.argv[2] if len(sys.argv) > 2 else "G1423170.0DA"
FINAL = sys.argv[3] if len(sys.argv) > 3 else "GS855_B22P0_24_1423159_ALPINA_PORT_final.bin"
table = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data", "checksumme_check_chars.json")))["cs"]   # value(hex) -> check char

raw = open(BMW, "rb").read()
lines = raw.split(b"\r\n")


def arc_step(c, b):
    c ^= b
    for _ in range(8):
        c = (c >> 1) ^ 0xA001 if c & 1 else c >> 1
    return c


def records(img):
    """Yield (line index, address, type, data) for data records, using img for the bytes."""
    seg = 0
    for i, ln in enumerate(lines):
        if not ln.startswith(b":"):
            continue
        r = bytes.fromhex(ln[1:].decode())
        n, addr, typ = r[0], r[1] << 8 | r[2], r[3]
        if typ == 4:
            seg = (r[4] << 8 | r[5]) << 16
        if typ in (0, 0x10) and n:
            yield i, seg + addr, typ, n


def refill(img, cs_char=None):
    out = list(lines)
    crc = 0
    for i, a, typ, n in records(img):
        data = img[a:a + n]
        body = bytes([n, a >> 8 & 0xFF, a & 0xFF, typ]) + data
        out[i] = (":" + (body + bytes([(-sum(body)) & 0xFF])).hex().upper()).encode()
        for b in data:
            crc = arc_step(crc, b)
    for i, ln in enumerate(out):
        if ln.startswith(b"$CHECKSUMME"):
            ch = cs_char if cs_char else ln.split()[2].decode()
            out[i] = f"$CHECKSUMME {crc:04X} {ch}".encode()
    return b"\r\n".join(out), crc


# 1) self-test
stock = open(STOCK, "rb").read()
again, crc = refill(stock)
if again != raw:
    sys.exit("SELF-TEST FAILED: rebuilt stock file differs from BMW's G1423170.0DA")
print(f"self-test OK: stock read rebuilds BMW's G1423170.0DA byte-identically ($CHECKSUMME {crc:04X})")

# 2) port with padding search
port = bytearray(open(PORT, "rb").read())
if port[0xFFCC:0xFFCE] != b"\xff\xff":
    sys.exit("padding not FF in port image")
recs = list(records(port))
order = [a + k for _, a, _, n in recs for k in range(n)]      # file order of data addresses
cut = order.index(0xFFCC)
pre = 0
for a in order[:cut]:
    pre = arc_step(pre, port[a])
tab = [int.from_bytes(port[0x10C68 + 2 * i:0x10C6A + 2 * i], "big") for i in range(256)]
tcu_pre = 0
for b in port[0x8000:0xFFCC]:
    tcu_pre = ((tcu_pre << 8) & 0xFFFF) ^ tab[((tcu_pre >> 8) ^ b) & 0xFF]
rest = order[cut:]
found = None
for x in range(256):
    for y in range(256):
        t = tcu_pre
        for b in (x, y):
            t = ((t << 8) & 0xFFFF) ^ tab[((t >> 8) ^ b) & 0xFF]
        c = pre
        for a in rest:
            if a == 0xFFCC: b = x
            elif a == 0xFFCD: b = y
            elif a == 0xFFFE: b = t >> 8
            elif a == 0xFFFF: b = t & 0xFF
            else: b = port[a]
            c = arc_step(c, b)
        if f"{c:04X}" in table:
            found = (x, y, t, c)
            break
    if found:
        break
if not found:
    sys.exit("no padding value gives a known checksum")
x, y, t, c = found
port[0xFFCC], port[0xFFCD] = x, y
port[0xFFFE:0x10000] = t.to_bytes(2, "big")
for name, s, e, at, calc, stored in gs855_crc.check(port):
    if calc != stored:
        sys.exit(f"{name} CRC wrong after padding")
data, crc = refill(port, table[f"{c:04X}"])
assert crc == c
open(OUT, "wb").write(data)
open(FINAL, "wb").write(port)
print(f"padding 0xFFCC/0xFFCD = {x:02X} {y:02X}; TCU CRC 0xFFFE = {t:04X}; "
      f"$CHECKSUMME {c:04X} {table[f'{c:04X}']} (check char from BMW's own files)")
print("wrote", OUT, "and", FINAL)
