"""Verify a staged GD855 .0DA: record checksums, data vs image, header lines."""
import sys
L = open(sys.argv[1], "rb").read().split(b"\r\n")
img = bytearray(b"\xff" * 0x10000)
bad = 0
for ln in L:
    if not ln.startswith(b":"):
        continue
    r = bytes.fromhex(ln[1:].decode())
    if sum(r) & 0xFF:
        bad += 1
    n, a, t = r[0], r[1] << 8 | r[2], r[3]
    if t in (0, 0x10):
        img[a:a + n] = r[4:4 + n]
p = open("GS855_B22P0_24_1423159_ALPINA_PORT_final.bin", "rb").read()
o = open("GS855_B22P0_24_1423159_full.bin", "rb").read()
print("record checksum errors:", bad)
print("file data == final port image 0x8000-0xFFFF:", bytes(img[0x8000:0x10000]) == p[0x8000:0x10000])
d = [i for i in range(len(p)) if p[i] != o[i]]
print(f"final port vs your read: {len(d)} bytes differ, range {min(d):05X}-{max(d):05X}")
print([l.decode() for l in L if l.startswith(b"$")])
