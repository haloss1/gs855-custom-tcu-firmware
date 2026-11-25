"""Port remaining Alpina changes to the GS8.55 by exact context matching.

For each changed run (GS8.60.2 stock QJ10 -> Alpina TU02, runs merged with gap <= 4):
  window = stock[s-ctx : e+1+ctx]; it must occur exactly ONCE in the GS8.55 calibration
  (0x8000-0xFFCD), byte for byte (context AND the stock bytes inside the run).
  Then the Alpina bytes are copied to the matching GS8.55 location.
Tries ctx = 16, 12, 8 (largest unique wins). Runs in excluded areas are skipped.
Input: GS855_ALPINA_PORT_v2_lockup.bin (v1 + lockup); output: GS855_ALPINA_PORT_v2b.bin + report."""
import json

st = open("nfs_A7505275.bin", "rb").read()
al = open("alpina_A7505275.bin", "rb").read()
base = open("GS855_ALPINA_PORT_v2_lockup.bin", "rb").read()      # v1 + lockup, before padding
orig = open("GS855_B22P0_24_1423159_full.bin", "rb").read()
img = bytearray(base)
LO, HI = 0x8000, 0xFFCE

EXCLUDE = [  # GS8.60.2 source ranges already handled or not to be ported
    (0x833A, 0x8350, "driving-style limits/thresholds (ported as config)"),
    (0x83EB, 0x8434, "gate default + manual-mode program table (ported / GS8.60.2-specific)"),
    (0x8A5E, 0x8A6A, "data ident"),
    (0x8B4B, 0x8B4D, "function-enable bits (ported)"),
    (0x9000, 0x97C0, "shift maps (ported by content)"),
    (0x97C0, 0x98C0, "lockup table (ported in v2)"),
    (0xFFC0, 0x10000, "ident/checksum area"),
]
# GS8.55 bytes that must not be overwritten (already ported or structural)
PROTECT = [(0x82A2, 0x82B8), (0x8600, 0x8608), (0x8DDC, 0x9400), (0x94F0, 0x95EB), (0xFFCC, 0x10000)]

runs, cur = [], None
for i in range(LO, 0xFFC0):
    if st[i] != al[i]:
        if cur and i - cur[1] <= 4:
            cur[1] = i
        else:
            if cur: runs.append(cur)
            cur = [i, i]
runs.append(cur)

def excluded(s, e):
    for a, b, why in EXCLUDE:
        if s < b and e >= a:
            return why
    return None

def find_all(hay, needle, lo, hi):
    out, k = [], hay.find(needle, lo, hi)
    while k >= 0:
        out.append(k)
        k = hay.find(needle, k + 1, hi)
    return out

report = {"ported": [], "skipped": []}
for s, e in runs:
    why = excluded(s, e)
    if why:
        report["skipped"].append((s, e, why)); continue
    done = False
    for ctx in (16, 12, 8):
        ws, we = s - ctx, e + 1 + ctx
        hits = find_all(orig, st[ws:we], LO, HI)
        if len(hits) == 1:
            t = hits[0] + ctx                      # GS8.55 address of run start
            te = t + (e - s + 1)
            if any(t < pb and te > pa for pa, pb in PROTECT):
                report["skipped"].append((s, e, f"target {t:05X} in protected area")); done = True; break
            img[t:te] = al[s:e + 1]
            report["ported"].append((s, e, t, ctx))
            done = True
            break
        if len(hits) > 1 and ctx == 8:
            report["skipped"].append((s, e, f"ambiguous ({len(hits)} matches)")); done = True
    if not done:
        report["skipped"].append((s, e, "stock bytes/context not found on GS8.55"))

open("GS855_ALPINA_PORT_v2b.bin", "wb").write(img)
pb = sum(e - s + 1 for s, e, t, c in report["ported"])
tot = sum(e - s + 1 for s, e in runs)
print(f"runs: {len(runs)}  ported {len(report['ported'])} runs / {pb} bytes of {tot}")
from collections import Counter
print("skip reasons:", Counter(r[2].split(' (')[0] if 'protected' not in r[2] else 'protected' for r in report["skipped"]))
blocks = Counter()
for s, e, t, c in report["ported"]:
    blocks[f"{s >> 12:X}000"] += e - s + 1
print("ported bytes by GS8.60.2 block:", dict(sorted(blocks.items())))
offs = Counter((t - s) for s, e, t, c in report["ported"])
print("most common address offsets (GS8.55 - GS8.60.2):", offs.most_common(8))
json.dump({k: [[hex(x) if isinstance(x, int) else x for x in r] for r in v] for k, v in report.items()},
          open("port_context_report.json", "w"), indent=0)
d = [i for i in range(len(img)) if img[i] != base[i]]
print(f"bytes changed vs v2-lockup: {len(d)}; outside 0x8000-0xFFCD: {[hex(i) for i in d if not LO <= i < HI]}")

