"""List instructions that reference given absolute addresses (RAM or calibration) in a 68k image.
usage: python ramxref.py image.bin ADDR [ADDR ...] [--writes]   (hex, e.g. FFFF90DD 8B4B)
Disassembles every function-sized window around each hit and prints the hit instruction."""
import sys, struct, capstone

img = open(sys.argv[1], "rb").read()
targets = [int(a, 16) & 0xFFFFFFFF for a in sys.argv[2:] if not a.startswith("--")]
writes_only = "--writes" in sys.argv
md = capstone.Cs(capstone.CS_ARCH_M68K, capstone.CS_MODE_BIG_ENDIAN | capstone.CS_MODE_M68K_040)
md.skipdata = True

for t in targets:
    pat = struct.pack(">I", t)
    hits, i = [], img.find(pat, 0x10000 if len(img) > 0x10000 else 0)
    while i >= 0:
        hits.append(i)
        i = img.find(pat, i + 1)
    print(f"== {t:08X}: {len(hits)} operand hits")
    for h in hits:
        # try instruction starts 2..8 bytes before the operand
        for back in (2, 4, 6, 8):
            s = h - back
            ins = next(md.disasm(img[s:s + 12], s), None)
            if ins and s <= h < s + ins.size and f"{t:x}" in ins.op_str:
                ops = ins.op_str
                is_write = ops.rstrip().endswith(f"${t:x}.l") and "," in ops or \
                           ins.mnemonic.startswith(("clr", "st", "sf", "addq", "subq", "bset", "bclr", "not", "neg"))
                if ins.mnemonic.startswith("movea"):
                    is_write = None  # pointer load: depends on later use
                if writes_only and is_write is False:
                    break
                tag = {True: "WRITE", False: "read ", None: "ptr  "}[is_write]
                print(f"   {tag} {ins.address:06X}: {ins.mnemonic:<8} {ops}")
                break
