"""Disassemble a range of a GS8.6x/GS8.55 program image (68k, CPU32).
usage: python dis.py image.bin START END [--cal cal.bin]   (hex addresses)
Annotates abs references into 0x8000-0xFFFF with the calibration bytes there."""
import sys, re, capstone

img = open(sys.argv[1], "rb").read()
s, e = int(sys.argv[2], 16), int(sys.argv[3], 16)
cal = open(sys.argv[sys.argv.index("--cal") + 1], "rb").read() if "--cal" in sys.argv else img
md = capstone.Cs(capstone.CS_ARCH_M68K, capstone.CS_MODE_BIG_ENDIAN | capstone.CS_MODE_M68K_040)
md.skipdata = True
for ins in md.disasm(img[s:e], s):
    note = ""
    for m in re.finditer(r"\$([0-9a-f]{4,8})", ins.op_str):
        v = int(m.group(1), 16)
        if 0x4000 <= v < 0x10000 and v < len(cal):
            note += f"  ; [{v:05X}] = {cal[v:v+8].hex(' ')}"
    print(f"{ins.address:06X}: {ins.bytes.hex():<20} {ins.mnemonic:<8} {ins.op_str}{note}")
