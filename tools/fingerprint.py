"""Fingerprint 68k functions: calibration refs, RAM refs, calls, until the first rts (max N insns).
usage: python fingerprint.py image.bin cal_stock.bin cal_alpina.bin FUNC [FUNC...]"""
import sys, re, capstone

img = open(sys.argv[1], "rb").read()
st = open(sys.argv[2], "rb").read(); al = open(sys.argv[3], "rb").read()
md = capstone.Cs(capstone.CS_ARCH_M68K, capstone.CS_MODE_BIG_ENDIAN | capstone.CS_MODE_M68K_040)
md.skipdata = True
for f in sys.argv[4:]:
    a = int(f, 16)
    cal, ram, calls, n = set(), set(), [], 0
    for ins in md.disasm(img[a:a + 0x1400], a):
        n += 1
        for m in re.finditer(r"\$([0-9a-f]{4,8})", ins.op_str):
            v = int(m.group(1), 16)
            if 0x8000 <= v < 0x10000:
                cal.add(v)
            elif v >= 0xFFFF0000:
                ram.add(v & 0xFFFF)
        if ins.mnemonic in ("jsr", "bsr.w", "bsr.b", "bsr"):
            calls.append(ins.op_str)
        if ins.mnemonic in ("rts", "rtd") or n > 600:
            break
    changed = sorted(c for c in cal if st[c:c + 4] != al[c:c + 4])
    print(f"== {a:06X}: {n} insns, {len(cal)} cal refs, {len(ram)} RAM refs, {len(calls)} calls")
    print("   cal:", " ".join(f"{c:04X}" for c in sorted(cal)))
    print("   cal changed by Alpina:", " ".join(f"{c:04X}" for c in changed) or "-")
    print("   RAM:", " ".join(f"{r:04X}" for r in sorted(ram)))
    print("   calls:", " ".join(sorted(set(calls))))
