"""Align all maps/curves of every variant to a reference layout and export a wide CSV.

Table start addresses come from calibration pointer directories plus the abs.L references
in each file's own program. Files that share the reference program are matched by address;
others by sequence alignment on (type, nx, ny, x-axis, y-axis), with gaps filled using
(type, nx, ny) only.
Output:
  all_maps_wide.csv    : id, ref_addr, type, nx, ny, cell, x, y, <value per variant>, <addr per variant>
  all_maps_summary.txt : per table, groups of variants that share identical values
"""
import os, re, csv, difflib, importlib

NFS = r"C:\EC-APPS\NFS\DATA\GD8602"
DAT = {l.split(",")[4][:7]: l.split(",")[2] + l.split(",")[3]
       for l in open(os.path.join(NFS, "GD8602.DAT"), encoding="latin-1") if re.match(r"\d{7},", l)}
REF = "variants/A7505275.bin"   # stock QJ10, program 1423416D


def prog_for(path):
    if path.startswith("GS855"):
        return path                              # full image: code is inside
    m = re.search(r"A(\d{7})", os.path.basename(path))
    pg = DAT.get(m.group(1)) if m else None
    if not pg:
        return None
    out = f"prog_{pg}.bin"
    if not os.path.exists(out):
        os.system(f'python -I parse_0da.py "{os.path.join(NFS, pg + ".0PA")}" {out} > NUL')
    return out


def load(path, lo):
    os.environ["CAL_LO"] = hex(lo)
    import gs86_maps
    g = importlib.reload(gs86_maps)
    pp = prog_for(path)
    prog = open(pp, "rb").read() if pp else None
    its = [m for m in g.extract(open(path, "rb").read(), prog) if m["type"] in ("map", "curve")]
    return its, pp


strict = lambda m: (m["type"], m["nx"], m["ny"], tuple(m["x"]), tuple(m["y"]))
loose = lambda m: (m["type"], m["nx"], m["ny"])
label = lambda p: os.path.splitext(os.path.basename(p))[0]


def align(ref, its):
    sm = difflib.SequenceMatcher(None, [strict(m) for m in ref], [strict(m) for m in its], autojunk=False)
    mp = {}
    prev_a = prev_b = 0
    for blk in sm.get_matching_blocks():
        # fill the gap before this block with a loose alignment
        ga, gb = ref[prev_a:blk.a], its[prev_b:blk.b]
        if ga and gb:
            s2 = difflib.SequenceMatcher(None, [loose(m) for m in ga], [loose(m) for m in gb], autojunk=False)
            for b2 in s2.get_matching_blocks():
                for k in range(b2.size):
                    mp[prev_a + b2.a + k] = dict(gb[b2.b + k], match="shape")
        for k in range(blk.size):
            mp[blk.a + k] = dict(its[blk.b + k], match="structure")
        prev_a, prev_b = blk.a + blk.size, blk.b + blk.size
    return mp


FILES = [("variants/" + f, 0x8000) for f in sorted(os.listdir("variants"))]
FILES.append(("GS855_B22P0_24_1423159_full.bin", 0x4000))
ref, ref_prog = load(REF, 0x8000)
cols = {}
for path, lo in FILES:
    its, pp = load(path, lo)
    if pp == ref_prog:
        by = {m["addr"]: m for m in its}
        mp = {i: dict(by[m["addr"]], match="address") for i, m in enumerate(ref) if m["addr"] in by}
        how = "by address"
    else:
        mp = align(ref, its)
        how = "by structure"
    cols[label(path)] = mp
    print(f"{label(path):30} prog={os.path.basename(pp or '?'):22} items={len(its):4}  matched={len(mp):4}/{len(ref)} ({how})")

names = list(cols)
with open("all_maps_wide.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["id", "ref_addr", "type", "nx", "ny", "cell", "x", "y"] + names + ["addr:" + n for n in names])
    for i, m in enumerate(ref):
        for c in range(len(m["z"])):
            xi, yi = c % m["nx"], c // m["nx"]
            row = [f"T{i:03d}", f"{m['addr']:05X}", m["type"], m["nx"], m["ny"], c,
                   m["x"][xi], m["y"][yi] if m["y"] else ""]
            row += [cols[n][i]["z"][c] if i in cols[n] and c < len(cols[n][i]["z"]) else "" for n in names]
            row += [f"{cols[n][i]['addr']:05X}" if i in cols[n] else "" for n in names]
            w.writerow(row)

with open("all_maps_summary.txt", "w") as f:
    for i, m in enumerate(ref):
        versions = {}
        for n in names:
            if i in cols[n]:
                o = cols[n][i]
                versions.setdefault((tuple(o["x"]), tuple(o["y"]), tuple(o["z"])), []).append(n)
        if len(versions) > 1:
            f.write(f"T{i:03d} {m['addr']:05X} {m['type']} {m['nx']}x{m['ny']}: {len(versions)} versions\n")
            for k, (_, ns) in enumerate(sorted(versions.items(), key=lambda kv: -len(kv[1]))):
                f.write(f"   v{k}: {', '.join(ns)}\n")
print("wrote all_maps_wide.csv, all_maps_summary.txt")

# ---- JSON for the comparison page -------------------------------------------------
import json


def header_info(key):
    if key.startswith("GS855"):
        return {"desc": "Your car: GS8.55, read over K-line", "ref": "B22P0_24 42C0", "date": "1997",
                "prog": "GS8.55 (own)", "family": "GS8.55"}
    m = re.search(r"A(\d{7})", key)
    path = os.path.join(NFS, f"A{m.group(1)}.0DA")
    if key.startswith("ALPINA_A7505275"):
        path = "A7505275_alpina.0DA"
    if key.startswith("ALPINA_A7509370"):
        path = "A7509370_alpina.0DA"
    t = open(path, encoding="latin-1").read(5000)
    g = lambda k: (re.search(k + r"[:\s]+([^\n]*)", t) or [None, ""])[1].strip()
    desc = [x.strip() for x in re.findall(r";;K_(?:F1|F2|V1|V2)[:\s]+([^\n]*)", t) if x.strip()]
    desc = [d for d in desc if not d.startswith(";;") and d not in ("Datenstand fuer", "Datenstand f. E53")]
    pg = DAT.get(m.group(1), "?")
    ident = open(f"variants/{key}.bin", "rb").read()[0xFFCE:0xFFDE].decode("latin-1")
    fam = {"1423416D": "QH 0307", "1423953A": "0W 0309", "7506450A": "0W 0417",
           "7508972A": "0W 0521", "7512653A": "0W 0624"}.get(pg, pg)
    return {"desc": " Â· ".join(dict.fromkeys(desc))[:120], "ref": ident, "date": g("K_Stand"),
            "prog": pg, "family": fam}


variants = []
for n in names:
    h = header_info(n)
    h["key"] = n
    h["alpina"] = n.startswith("ALPINA") or "ALPINA" in h["desc"].upper()
    variants.append(h)

tables = []
for i, m in enumerate(ref):
    versions, vidx, per = [], {}, []
    for n in names:
        o = cols[n].get(i)
        if o is None:
            per.append(None)
            continue
        k = (tuple(o["x"]), tuple(o["y"]), tuple(o["z"]))
        if k not in vidx:
            vidx[k] = len(versions)
            versions.append({"x": o["x"], "y": o["y"], "z": o["z"]})
        per.append([vidx[k], o["addr"], o["match"][0]])  # version, addr, a/s/s(hape)
    tables.append({"id": f"T{i:03d}", "addr": m["addr"], "type": m["type"], "nx": m["nx"], "ny": m["ny"],
                   "versions": versions, "per": per})

json.dump({"variants": variants, "tables": tables, "base": "A7505275"},
          open("gs86_compare.json", "w"), separators=(",", ":"))
print("wrote gs86_compare.json", os.path.getsize("gs86_compare.json"), "bytes")
