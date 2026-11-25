"""Inventory of all Alpina pre-TU changes (A7505275 TU02 vs stock QJ10) and their GS8.55 counterparts.
Uses the aligned table data in gs86_compare.json plus direct byte diffs for anything not inside a table."""
import json

st = open("nfs_A7505275.bin", "rb").read()
al = open("alpina_A7505275.bin", "rb").read()
D = json.load(open("gs86_compare.json"))
V = [v["key"] for v in D["variants"]]
iS, iA, iM = V.index("A7505275"), V.index("ALPINA_A7505275_TU02"), V.index("GS855_B22P0_24_1423159_full")
PORTED = {0x9276, 0x9666, 0x94A6}

# changed byte runs
runs, cur = [], None
for i in range(0x8000, 0xFFC0):
    if st[i] != al[i]:
        if cur and i - cur[1] <= 4:
            cur[1] = i
        else:
            if cur: runs.append(cur)
            cur = [i, i]
runs.append(cur)

# table spans (stock layout)
spans = []
for t in D["tables"]:
    p = t["per"][iS]
    if not p:
        continue
    v = t["versions"][p[0]]
    size = (4 + len(v["x"]) + len(v["y"]) + len(v["z"])) if t["type"] == "map" else (2 + 2 * len(v["x"]))
    spans.append((p[1], p[1] + size, t))

rows, covered = [], set()
for s, e, t in spans:
    nchg = sum(1 for i in range(s, e) if st[i] != al[i])
    if not nchg:
        continue
    covered.update(i for i in range(s, e))
    pm = t["per"][iM]
    vs = t["versions"][t["per"][iS][0]]
    if pm:
        vm = t["versions"][pm[0]]
        same_axes = vm["x"] == vs["x"] and vm["y"] == vs["y"]
        dist = sum(abs(a - b) for a, b in zip(vm["z"], vs["z"])) if len(vm["z"]) == len(vs["z"]) else None
        g = f"{pm[1]:05X} ({ {'a':'addr','s':'struct','h':'shape'}[pm[2]] }, axes {'same' if same_axes else 'DIFF'}, |GS855-stock|={dist})"
    else:
        g = "-- no match"
    rows.append((s, t["type"], f"{t['nx']}x{t['ny']}", nchg, g, "PORTED" if s in PORTED else ""))

loose = [r for r in runs if not any(i in covered for i in range(r[0], r[1] + 1))]
print(f"Alpina changed {sum(1 for i in range(0x8000,0xFFC0) if st[i]!=al[i])} bytes in {len(runs)} runs")
print(f"{len(rows)} tables touched; {len(loose)} runs outside parsed tables\n")
print("addr   type   shape  changed  GS8.55 counterpart")
for r in sorted(rows):
    print(f"{r[0]:05X}  {r[1]:5}  {r[2]:6} {r[3]:5}    {r[4]}  {r[5]}")
print("\nruns outside parsed tables (config bytes / raw tables):")
for s, e in loose:
    print(f"  {s:05X}-{e:05X} ({e-s+1:4} B)  stock {st[s:min(e+1,s+12)].hex(' ')}  alpina {al[s:min(e+1,s+12)].hex(' ')}")
