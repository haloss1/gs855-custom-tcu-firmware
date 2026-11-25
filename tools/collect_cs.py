"""Collect ($CHECKSUMME value, check char) and ($REFERENZ text, check char) pairs from the tails
and heads of BMW NFS data files, then test simple functions of the value."""
import os, re, itertools, functools, json

ROOT = r"C:\ProgramData\BMW\ISPI\data\TRIC\ISTA-P\BMW\Services\data\ecudata"
cs, ref = {}, {}
n = 0
for dp, dn, fn in os.walk(ROOT):
    for f in fn:
        if not re.search(r"\.0[dp]a$", f, re.I):
            continue
        p = os.path.join(dp, f)
        try:
            with open(p, "rb") as fh:
                head = fh.read(6000)
                fh.seek(max(0, os.path.getsize(p) - 400))
                tail = fh.read()
        except OSError:
            continue
        n += 1
        m = re.search(rb"\$CHECKSUMME ([0-9A-F]{4}) (\S)", tail)
        if m:
            cs.setdefault(m.group(1).decode(), set()).add(m.group(2).decode())
        m = re.search(rb"\$REFERENZ ([^\r\n]*?) (\S)\r?\n", head)
        if m:
            ref.setdefault(m.group(1).decode("latin-1"), set()).add(m.group(2).decode("latin-1"))
        if n >= 20000:
            break
print(n, "files;", len(cs), "distinct checksum values;", len(ref), "distinct references")
incons = {k: v for k, v in cs.items() if len(v) > 1}
print("checksum values with >1 different char:", len(incons), list(incons.items())[:5])
json.dump({"cs": {k: sorted(v)[0] for k, v in cs.items()}, "ref": {k: sorted(v)[0] for k, v in ref.items()}},
          open("check_samples.json", "w"))

A36 = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
samples = [(k, sorted(v)[0]) for k, v in cs.items() if len(v) == 1]
def digs(s): return [A36.index(c) for c in s]
feats = {
    "value": lambda s: int(s, 16),
    "digsum": lambda s: sum(digs(s)),
    "wdig1": lambda s: sum((i + 1) * d for i, d in enumerate(digs(s))),
    "wdigrev": lambda s: sum((len(s) - i) * d for i, d in enumerate(digs(s))),
    "asciisum": lambda s: sum(map(ord, s)),
    "wascii": lambda s: sum((i + 1) * ord(c) for i, c in enumerate(s)),
    "bytesum": lambda s: (int(s, 16) >> 8) + (int(s, 16) & 0xFF),
    "bytexor": lambda s: (int(s, 16) >> 8) ^ (int(s, 16) & 0xFF),
    "w2": lambda s: sum(d * (2 ** (len(s) - 1 - i)) for i, d in enumerate(digs(s))),
    "w3": lambda s: sum(d * (3 ** (len(s) - 1 - i)) for i, d in enumerate(digs(s))),
}
best = []
for (fn, f) in feats.items():
    for mod in (36, 37, 35, 31, 26, 43, 97):
        for off in range(mod):
            hit = sum(1 for s, c in samples if (f(s) + off) % mod < 36 and A36[(f(s) + off) % mod] == c)
            best.append((hit, fn, mod, off))
best.sort(reverse=True)
print("samples:", len(samples))
for b in best[:6]:
    print(b)
