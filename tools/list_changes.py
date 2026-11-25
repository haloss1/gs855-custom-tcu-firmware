"""List every change in v2 vs the car's stock read: address, table, origin, stock -> v2 bytes.
Writes v2_changes.md and prints a summary."""
import json, os
os.environ["CAL_LO"] = "0x4000"
import gs86_maps as g

stock = open("GS855_B22P0_24_1423159_full.bin", "rb").read()
import sys
v2 = open(sys.argv[1] if len(sys.argv) > 1 else "GS855_ALPINA_PORT_v2_final.bin", "rb").read()
OUTMD = sys.argv[2] if len(sys.argv) > 2 else "v2_changes.md"
TITLE = sys.argv[3] if len(sys.argv) > 3 else "v2"
gs_tables = [m for m in g.extract(stock, stock) if m["type"] in ("map", "curve")]

origin = {}
def mark(a, b, label):
    for i in range(a, b):
        origin.setdefault(i, label)

mark(0x8606, 0x8607, "v1: gate default -> manual (GS8.60.2 0x83EB)")
mark(0x82AA, 0x82AC, "v1: driving-style lower limits (0x8340)")
mark(0x82B0, 0x82B2, "v1: driving-style upper limits (0x833C)")
mark(0x82B4, 0x82B8, "v1: driving-style thresholds (0x834A)")
mark(0x82A2, 0x82A3, "v1: function mask, evaluators off (0x8B4B)")
mark(0x82A3, 0x82A4, "v1: option byte, evaluator D off (0x8B4C)")
for dst, src in ((0x8DDC, 0x9666), (0x923C, 0x9276), (0x92AC, 0x94A6)):
    mark(dst, dst + 0x70, f"v1: shift map (Alpina delta from GS8.60.2 0x{src:04X})")
mark(0x94F0, 0x95EB, "v2: converter lockup table (Alpina values, GS8.60.2 0x97C0)")
for s, e, t, c in json.load(open("port_context_report.json"))["ported"]:
    s, e, t = int(s, 16), int(e, 16), int(t, 16)
    if s <= 0xEAC5 and e >= 0xEAB8:
        continue
    mark(t, t + (e - s + 1), f"v2: exact-context port from GS8.60.2 0x{s:05X}")
mark(0xFFCC, 0xFFCE, "padding (sets WinKFP file checksum)")
mark(0xFFFE, 0x10000, "calibration CRC")

def table_of(a):
    for m in gs_tables:
        if m["addr"] <= a < m["addr"] + m["size"]:
            part = "values" if a >= m["addr"] + m["size"] - len(m["z"]) else "axis/header"
            return f"{m['type']} {m['nx']}x{m['ny']} @0x{m['addr']:05X} ({part})"
    return "raw data / 16-bit table"

runs, cur = [], None
for i in range(len(stock)):
    if stock[i] != v2[i]:
        if cur and i - cur[1] <= 1 and origin.get(i, "v2: close-curve delta") == origin.get(cur[1], "v2: close-curve delta"):
            cur[1] = i
        else:
            if cur: runs.append(cur)
            cur = [i, i]
runs.append(cur)

from collections import Counter, OrderedDict
cat = Counter(); catb = Counter()
lines = [f"# GS8.55 Alpina port {TITLE}: every change vs stock (G1423170 / RD43)", "",
         f"{sum(e - s + 1 for s, e in runs)} bytes in {len(runs)} runs. Addresses are GS8.55 flash addresses.", "",
         "| GS8.55 addr | bytes | origin | table | stock | port |", "|---|---|---|---|---|---|"]
for s, e in runs:
    o = origin.get(s, "v2: close-curve delta (Alpina change on GS8.55 values)")
    key = o.split(" (")[0].split(" from")[0]
    cat[key] += 1; catb[key] += e - s + 1
    sb, vb = stock[s:e + 1], v2[s:e + 1]
    show = lambda b: b[:24].hex(" ") + (" ..." if len(b) > 24 else "")
    lines.append(f"| 0x{s:05X}-0x{e:05X} | {e - s + 1} | {o} | {table_of(s)} | {show(sb)} | {show(vb)} |")
open(OUTMD, "w", encoding="utf-8").write("\n".join(lines) + "\n")
print(f"{sum(e - s + 1 for s, e in runs)} bytes in {len(runs)} runs -> {OUTMD}")
for k in sorted(cat, key=lambda k: -catb[k]):
    print(f"  {catb[k]:5} bytes {cat[k]:4} runs  {k}")
reg = Counter()
for s, e in runs:
    reg[f"0x{s >> 12:X}000"] += e - s + 1
print("by region:", dict(sorted(reg.items())))

