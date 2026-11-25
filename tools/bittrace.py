"""Find all bit tests of given calibration option bytes in a 68k image.
usage: python bittrace.py image.bin BYTEADDR [BYTEADDR...]   (hex)
Handles: btst #n,$abs.l ; move.b $abs.l,Dx then btst/and ; movea.l #abs,An then btst #n,d(An).
For each test prints the instruction, the branch after it, and the first jsr reached."""
import sys, struct, re, capstone

img = open(sys.argv[1], "rb").read()
targets = [int(a, 16) for a in sys.argv[2:]]
md = capstone.Cs(capstone.CS_ARCH_M68K, capstone.CS_MODE_BIG_ENDIAN | capstone.CS_MODE_M68K_040)
md.skipdata = True


def insn_at(a):
    return next(md.disasm(img[a:a + 12], a), None)


def follow(a, n=8):
    out, cur = [], a
    for _ in range(n):
        i = insn_at(cur)
        if not i:
            break
        out.append(f"{i.address:06X} {i.mnemonic} {i.op_str}")
        cur += i.size
    return out


def find_starts(op_addr, base=None):
    best = None
    for back in (2, 4, 6, 8):
        i = insn_at(op_addr - back)
        if i and i.address + i.size > op_addr:
            if base is not None and f"${base:x}" in i.op_str:
                return i
            best = best or i
    return best


results = []
lo, hi = min(targets) - 4, max(targets) + 4
for base in range(lo, hi):
    pat = struct.pack(">I", base)
    k = img.find(pat, 0x10000)
    while k >= 0:
        ins = find_starts(k, base)
        k2 = k
        k = img.find(pat, k + 1)
        if not ins:
            continue
        # direct btst on abs
        if ins.mnemonic.startswith("btst") and base in targets:
            results.append((base, ins, follow(ins.address + ins.size, 4)))
            continue
        # pointer load: scan forward for btst #n,d(An) / (An)
        m = re.match(r"(?:#\$%x), (a\d)" % base, ins.op_str)
        if ins.mnemonic.startswith(("movea", "lea")) and m:
            reg = m.group(1)
            cur = ins.address + ins.size
            for _ in range(40):
                j = insn_at(cur)
                if not j:
                    break
                mm = re.search(r"(?:\$([0-9a-f]+))?\(%s\)" % reg, j.op_str)
                if mm and j.mnemonic.startswith("btst"):
                    off = int(mm.group(1), 16) if mm.group(1) else 0
                    if base + off in targets:
                        results.append((base + off, j, follow(j.address + j.size, 4)))
                if re.search(r",\s*%s$" % reg, j.op_str) and j.address != ins.address:
                    break   # register overwritten
                if j.mnemonic in ("rts", "rte"):
                    break
                cur += j.size
            continue
        # byte load then and/btst on data reg
        if ins.mnemonic.startswith("move.b") and base in targets:
            dm = re.search(r",\s*(d\d)$", ins.op_str)
            if dm:
                results.append((base, ins, follow(ins.address + ins.size, 5)))

for addr, ins, nxt in sorted(results, key=lambda r: (r[0], r[1].address)):
    bit = re.match(r"#\$?([0-9a-f]+)", ins.op_str)
    b = f"bit {int(bit.group(1), 16)}" if ins.mnemonic.startswith("btst") and bit else "byte"
    print(f"[{addr:05X} {b:6}] {ins.address:06X} {ins.mnemonic} {ins.op_str}")
    for l in nxt:
        print(f"                    {l}")
