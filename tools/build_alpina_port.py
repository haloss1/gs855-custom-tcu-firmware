"""Build an Alpina-style GS8.55 image from the user's full read. Nothing is written to any unit.

Every patch first checks the original bytes; the build stops if any differ.
Shift maps get Alpina's change relative to stock GS8.60.2 (A7505275 -> TU02), added to the
GS8.55 values and clamped to 0..255. The calibration CRC (0x8000-0xFFCD -> 0xFFFE) is recomputed
with the firmware's own algorithm and all three CRCs are verified at the end."""
import os, sys, json
os.environ["CAL_LO"] = "0x4000"
import gs86_maps as g
import gs855_crc as crcmod

SRC = "GS855_B22P0_24_1423159_full.bin"
OUT = "GS855_B22P0_24_1423159_ALPINA_PORT.bin"
img = bytearray(open(SRC, "rb").read())
orig = bytes(img)
log = []

BYTE_PATCHES = [  # (address, expected stock bytes, new bytes, description)
    (0x8606, "FE", "0B", "Gate before first tip goes straight to manual (GS8.60.2 0x83EB FE->0B)"),
    (0x82AA, "20 81", "00 00", "Driving-style lower limits (GS8.60.2 0x8340)"),
    (0x82B0, "80 FF", "00 00", "Driving-style upper limits (GS8.60.2 0x833C)"),
    (0x82B4, "00 41 81 C1", "FF FF FF FF", "Driving-style level thresholds (GS8.60.2 0x834A)"),
    (0x82A2, "F7", "11", "Function mask: evaluators off, bits 7/6/5/2/1 (GS8.60.2 0x8B4B F7->11)"),
    (0x82A3, "FA", "F8", "Option byte: evaluator D off, bit 1 (GS8.60.2 0x8B4C FB->F9)"),
]
for addr, exp, new, desc in BYTE_PATCHES:
    e, n = bytes.fromhex(exp), bytes.fromhex(new)
    if img[addr:addr + len(e)] != e:
        sys.exit(f"STOP: {addr:05X} is {img[addr:addr+len(e)].hex(' ')}, expected {exp}")
    img[addr:addr + len(n)] = n
    log.append(f"{addr:05X}  {exp:<12} -> {new:<12} {desc}")

# shift maps: GS8.60.2 map -> GS8.55 map (content-matched)
os.environ["CAL_LO"] = "0x8000"
import importlib
g8 = importlib.reload(g)
pp = open("prog_1423416D.bin", "rb").read()
st = {m["addr"]: m for m in g8.extract(open("nfs_A7505275.bin", "rb").read(), pp)}
al = {m["addr"]: m for m in g8.extract(open("alpina_A7505275.bin", "rb").read(), pp)}
os.environ["CAL_LO"] = "0x4000"
g5 = importlib.reload(g)
MAPS = [(0x9666, 0x8DDC), (0x9276, 0x923C), (0x94A6, 0x92AC)]
for src, dst in MAPS:
    s, a, m = st[src], al[src], g5.parse_at(orig, dst)
    if not (m["type"] == "map" and m["x"] == s["x"] == a["x"] and m["y"] == s["y"] == a["y"]):
        sys.exit(f"STOP: axes of GS8.55 {dst:04X} and GS8.60.2 {src:04X} differ")
    z0 = dst + 4 + m["nx"] + m["ny"]
    new = [max(0, min(255, mz + (az - sz))) for mz, sz, az in zip(m["z"], s["z"], a["z"])]
    clamped = sum(1 for mz, sz, az in zip(m["z"], s["z"], a["z"]) if not 0 <= mz + az - sz <= 255)
    img[z0:z0 + len(new)] = bytes(new)
    nch = sum(1 for x, y in zip(m["z"], new) if x != y)
    log.append(f"{dst:05X}  shift map 8x11: {nch} cells changed (Alpina delta from GS8.60.2 {src:04X}), {clamped} clamped")

# checksum
calc = crcmod.crc(img, 0x8000, 0xFFCE)
img[0xFFFE:0x10000] = calc.to_bytes(2, "big")
log.append(f"0FFFE  {orig[0xFFFE:0x10000].hex(' ').upper():<12} -> {calc:04X}         Calibration CRC recomputed")
for name, s, e, at, c, stored in crcmod.check(img):
    if c != stored:
        sys.exit(f"STOP: {name} CRC mismatch after build")

open(OUT, "wb").write(img)
diff = [i for i in range(len(img)) if img[i] != orig[i]]
outside = [i for i in diff if not 0x8000 <= i < 0x10000]
print("\n".join(log))
print(f"\nwrote {OUT}: {len(diff)} bytes differ from your read, all inside calibration: {not outside}")
for name, s, e, at, c, stored in crcmod.check(img):
    print(f"  {name:12} CRC {stored:04X} OK")
