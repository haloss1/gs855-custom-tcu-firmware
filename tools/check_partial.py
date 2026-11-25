"""Flag GS8.60.2 tables whose Alpina changes were only partly ported to the GS8.55 (v2)."""
import json, os
os.environ["CAL_LO"] = "0x8000"
import gs86_maps as g

st = open("nfs_A7505275.bin", "rb").read()
al = open("alpina_A7505275.bin", "rb").read()
pp = open("prog_1423416D.bin", "rb").read()
ported = set()
for s, e, t, c in json.load(open("port_context_report.json"))["ported"]:
    ported.update(range(int(s, 16), int(e, 16) + 1))
close_src = set()
for ln in open("port_close.out", encoding="utf-8", errors="replace") if os.path.exists("port_close.out") else []:
    pass
tables = [m for m in g.extract(st, pp) if m["type"] in ("map", "curve")]
partial = []
for m in tables:
    a0, a1 = m["addr"], m["addr"] + m["size"]
    ch = [i for i in range(a0, a1) if st[i] != al[i]]
    if not ch:
        continue
    hdr_axes = [i for i in ch if i < a1 - len(m["z"])]
    vals = [i for i in ch if i >= a1 - len(m["z"])]
    p_axes = sum(1 for i in hdr_axes if i in ported)
    p_vals = sum(1 for i in vals if i in ported)
    if hdr_axes and (p_axes != len(hdr_axes) or (p_axes and p_vals != len(vals))):
        partial.append((a0, len(hdr_axes), p_axes, len(vals), p_vals))
print("tables where Alpina changed axes:", sum(1 for m in tables if any(st[i] != al[i] for i in range(m['addr'], m['addr'] + m['size'] - len(m['z'])))))
print("partially ported tables with axis changes (addr, axis bytes changed, ported, value bytes changed, ported):")
for p in partial:
    print("  %05X  axes %d/%d  values %d/%d" % (p[0], p[2], p[1], p[4], p[3]))
