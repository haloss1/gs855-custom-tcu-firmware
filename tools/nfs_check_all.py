"""1) Verify $CHECKSUMME = CRC-16/ARC over type 00/10 data on all NFS data files.
2) Brute-force the trailing check character of $CHECKSUMME / $REFERENZ / .DAT lines."""
import glob, re, zlib, itertools, functools

A36 = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def arc(data, init=0):
    c = init
    for b in data:
        c ^= b
        for _ in range(8):
            c = (c >> 1) ^ 0xA001 if c & 1 else c >> 1
    return c


def ccitt(data, init=0):
    c = init
    for b in data:
        c ^= b << 8
        for _ in range(8):
            c = ((c << 1) ^ 0x1021) & 0xFFFF if c & 0x8000 else (c << 1) & 0xFFFF
    return c


ok = bad = 0
samples = []  # (text before the check char, check char)
for f in glob.glob(r"C:\EC-APPS\NFS\DATA\*\*.0[DP]A") + glob.glob(r"C:\EC-APPS\NFS\DATA\*\*.0[dp]a"):
    try:
        L = [l.rstrip("\r\n") for l in open(f, encoding="latin-1")]
    except Exception:
        continue
    cs = [l for l in L if l.startswith("$CHECKSUMME")]
    if not cs:
        continue
    try:
        recs = [bytes.fromhex(l[1:].strip()) for l in L if l.startswith(":")]
    except ValueError:
        continue
    data = b"".join(r[4:4 + r[0]] for r in recs if len(r) > 4 and r[3] in (0, 0x10))
    parts = cs[0].split()
    if len(parts) >= 3:
        if arc(data) == int(parts[1], 16):
            ok += 1
        else:
            bad += 1
        samples.append(("CS", parts[1], parts[2]))
    for l in L:
        if l.startswith("$REFERENZ"):
            p = l.split()
            if len(p) >= 3 and len(p[-1]) == 1:
                samples.append(("REF", p[1], p[-1]))
print(f"$CHECKSUMME CRC-16/ARC: {ok} match, {bad} mismatch")
for f in glob.glob(r"C:\EC-APPS\NFS\DATA\*\*.DAT"):
    for ln in open(f, encoding="latin-1"):
        m = re.match(r"^(\d{7},.*\S)\s+(\S)$", ln.rstrip("\r\n"))
        if m:
            samples.append(("DAT", m.group(1), m.group(2)))
print(len(samples), "check-char samples:", {k: sum(1 for s in samples if s[0] == k) for k in ("CS", "REF", "DAT")})

funcs = {
    "sum": lambda s: sum(s), "xor": lambda s: functools.reduce(lambda a, b: a ^ b, s, 0),
    "wsum": lambda s: sum((i + 1) * c for i, c in enumerate(s)),
    "wsumrev": lambda s: sum((len(s) - i) * c for i, c in enumerate(s)),
    "arc": arc, "ccitt": ccitt, "ccittFFFF": lambda s: ccitt(s, 0xFFFF), "arcFFFF": lambda s: arc(s, 0xFFFF),
    "crc32": lambda s: zlib.crc32(s), "adler": lambda s: zlib.adler32(s),
}
alphabets = {"A36": A36, "A26": "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "A33": "0123456789ABCDEFGHJKLMNPRSTUVWXYZ"}
for kind in ("CS", "REF", "DAT"):
    S = [(t.encode("latin-1"), c) for k, t, c in samples if k == kind]
    if not S:
        continue
    best = (0,)
    for (fn, f), (an, al) in itertools.product(funcs.items(), alphabets.items()):
        for div in (1, 2, 4, 8, 16, 256):
            vals = [(f(t) // div) for t, c in S]
            for off in range(len(al)):
                hit = sum(1 for v, (t, c) in zip(vals, S) if al[(v + off) % len(al)] == c)
                if hit > best[0]:
                    best = (hit, fn, an, div, off)
    print(f"{kind}: best {best[0]}/{len(S)} with {best[1:]}")
