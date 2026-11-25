"""From a ram_monitor log, list 'state-like' bytes: outside the stack, changing rarely,
with few distinct values. Prints each one's value timeline."""
import re, sys, collections

log = sys.argv[1]
base = open("ram_baseline.bin", "rb").read()
START = int(sys.argv[2], 16) if len(sys.argv) > 2 else 0xFFF000
L = open(log, encoding="utf-8", errors="replace").read().splitlines()
ev = collections.defaultdict(list)
passes = 0
for ln in L:
    m = re.match(r"\[\s*([\d.]+)s\] (.*)", ln)
    if not m or "baseline" in ln or "done" in ln or "error" in ln:
        continue
    passes += 1
    t = float(m.group(1))
    for a, o, n in re.findall(r"([0-9A-F]{6}):([0-9A-F]{2})->([0-9A-F]{2})", m.group(2)):
        ev[int(a, 16)].append((t, int(o, 16), int(n, 16)))

rows = []
for a, e in ev.items():
    if a < 0xFFF290:          # CPU stack area (SSP = FFFFF28E)
        continue
    vals = {e[0][1]} | {x[2] for x in e}
    if len(e) <= 16 and len(vals) <= 6:
        rows.append((e[0][0], a, e, vals))
rows.sort()
print(f"{passes} change-lines; {len(rows)} state-like bytes")
for t0, a, e, vals in rows:
    tl = f"{e[0][1]:02X}" + "".join(f" -({t:.0f}s)-> {n:02X}" for t, o, n in e)
    print(f"{a:06X}: {tl}")
