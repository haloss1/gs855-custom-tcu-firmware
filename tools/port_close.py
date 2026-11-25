"""Port Alpina changes in byte-valued maps/curves whose axes match but whose stock values differ slightly.
Per cell: GS8.55 == stock -> Alpina value; else GS8.55 + (Alpina - stock), clamped 0..255.
Safety: the table offset (GS8.55 addr - GS8.60.2 addr) must be within 64 bytes of an offset seen
in the context-matched runs nearby (+-0x200), and the target must not overlap already-changed bytes."""
import json

st = open("nfs_A7505275.bin", "rb").read()
al = open("alpina_A7505275.bin", "rb").read()
orig = open("GS855_B22P0_24_1423159_full.bin", "rb").read()
img = bytearray(open("GS855_ALPINA_PORT_v2b.bin", "rb").read())
prev = bytes(img)
D = json.load(open("gs86_compare.json"))
V = [v["key"] for v in D["variants"]]
iS, iA, iM = V.index("A7505275"), V.index("ALPINA_A7505275_TU02"), V.index("GS855_B22P0_24_1423159_full")
ctxp = [(int(s, 16), int(t, 16)) for s, e, t, c in json.load(open("port_context_report.json"))["ported"]]
SKIP_SRC = [(0x833A, 0x8350), (0x9000, 0x98C0)]
PROTECT = [(0x82A2, 0x82B8), (0x8600, 0x8608), (0x8DDC, 0x9400), (0x94F0, 0x95EB), (0xFFCC, 0x10000)]

def z_span(t, v, addr):
    if t["type"] == "map":
        z0 = addr + 4 + len(v["x"]) + len(v["y"])
    else:
        z0 = addr + 2 + len(v["x"])
    return z0, len(v["z"])

done, skipped = [], []
for t in D["tables"]:
    ps, pa, pm = t["per"][iS], t["per"][iA], t["per"][iM]
    if not (ps and pa and pm):
        continue
    vs, va, vm = t["versions"][ps[0]], t["versions"][pa[0]], t["versions"][pm[0]]
    if vs["z"] == va["z"] or vs["z"] == vm["z"]:
        continue                       # not changed by Alpina, or identical stock (handled by context port)
    s_addr, m_addr = ps[1], pm[1]
    if any(a <= s_addr < b for a, b in SKIP_SRC):
        continue
    if not (vs["x"] == va["x"] == vm["x"] and vs["y"] == va["y"] == vm["y"] and len(vs["z"]) == len(vm["z"])):
        skipped.append((s_addr, m_addr, "axes differ")); continue
    off = m_addr - s_addr
    near = [tt - ss for ss, tt in ctxp if abs(ss - s_addr) <= 0x200]
    if not near or min(abs(off - o) for o in near) > 64:
        skipped.append((s_addr, m_addr, f"offset {off:+d} not consistent with nearby {sorted(set(near))[:4]}")); continue
    z0, n = z_span(t, vm, m_addr)
    if any(z0 < pb and z0 + n > pa_ for pa_, pb in PROTECT) or img[z0:z0 + n] != orig[z0:z0 + n]:
        skipped.append((s_addr, m_addr, "target overlaps changed/protected bytes")); continue
    if list(orig[z0:z0 + n]) != vm["z"]:
        skipped.append((s_addr, m_addr, "target bytes do not match parsed table")); continue
    new = []
    for zs, za, zm in zip(vs["z"], va["z"], vm["z"]):
        new.append(za if zm == zs else max(0, min(255, zm + (za - zs))))
    img[z0:z0 + n] = bytes(new)
    done.append((s_addr, m_addr, t["type"], len(vs["z"]), sum(1 for a, b in zip(new, vm["z"]) if a != b)))

open("GS855_ALPINA_PORT_v2c.bin", "wb").write(img)
print(f"close tables ported: {len(done)}, cells changed: {sum(d[4] for d in done)}")
for d in done:
    print(f"  {d[0]:05X} -> {d[1]:05X} {d[2]:5} {d[3]:3} cells, {d[4]} changed")
print(f"skipped: {len(skipped)}")
for s in skipped[:40]:
    print(f"  {s[0]:05X} -> {s[1]:05X}: {s[2]}")
diff = [i for i in range(len(img)) if img[i] != prev[i]]
print("bytes changed vs v2b:", len(diff), " outside cal:", [hex(i) for i in diff if not 0x8000 <= i < 0xFFCE])

