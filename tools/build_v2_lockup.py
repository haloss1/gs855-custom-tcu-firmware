"""v2 = v1 port + Alpina torque-converter lockup table.
GS8.60.2 table 0x97C0 (00 1E 00 07: 30 x-points, 7 y-points, 210 values) -> GS8.55 0x94F0 (same layout).
Applies Alpina's change relative to stock GS8.60.2 onto the GS8.55 values, clamped to 0..255.
The padding/CRC/file checksum are redone by build_winkfp_0da.py afterwards."""
import sys

st = open("nfs_A7505275.bin", "rb").read()
al = open("alpina_A7505275.bin", "rb").read()
v1 = bytearray(open("GS855_B22P0_24_1423159_ALPINA_PORT.bin", "rb").read())   # v1 before padding
orig = open("GS855_B22P0_24_1423159_full.bin", "rb").read()

SRC, DST = 0x97C0, 0x94F0
for name, img, a in (("GS8.60.2 stock", st, SRC), ("GS8.60.2 Alpina", al, SRC), ("GS8.55", v1, DST)):
    if img[a:a + 4] != b"\x00\x1e\x00\x07" or list(img[a + 4:a + 34]) != list(range(30)):
        sys.exit(f"STOP: {name} table header/x-axis not as expected at {a:05X}")
ys, ya, ym = st[SRC + 34:SRC + 41], al[SRC + 34:SRC + 41], v1[DST + 34:DST + 41]
print("y axis  stock", list(ys), " alpina", list(ya), " GS8.55", list(ym))
if ys != ya:
    sys.exit("STOP: Alpina changed the y axis; delta method not valid")
z_s, z_a, z_m = SRC + 41, SRC + 41, DST + 41
# Stock tables differ in only 9 of 210 cells (one group, by <=3), and Alpina's triples follow a
# pattern (fully-closed = engage) that a delta would break, so Alpina's values are copied as they are.
changed = sum(1 for k in range(210) if v1[z_m + k] != al[z_a + k])
v1[z_m:z_m + 210] = al[z_a:z_a + 210]
print(f"lockup table: Alpina values copied, {changed} of 210 values changed")
print("row-by-row (GS8.55 before -> after), 10 groups of 3 per row:")
for r in range(7):
    b = orig[z_m + 30 * r:z_m + 30 * r + 30]; a = v1[z_m + 30 * r:z_m + 30 * r + 30]
    print(f" y={ym[r]:3}  before " + " ".join(f"{b[i]:3}" for i in range(30)))
    print(f"        after  " + " ".join(f"{a[i]:3}" for i in range(30)))
open("GS855_ALPINA_PORT_v2_lockup.bin", "wb").write(v1)
print("wrote GS855_ALPINA_PORT_v2_lockup.bin (CRC/padding not yet fixed)")
