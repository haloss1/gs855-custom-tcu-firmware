"""Extract maps/curves from Bosch GS8.6x calibration images (0x8000-0xFFFF).

Discovery: the calibration contains pointer directories (big-endian longwords
into 0x8000-0xFFFF). Every pointer target is tried as
  map   : 00 NX 00 NY  X[NX] Y[NY]  Z[NX*NY]   (bytes, axes strictly increasing)
  curve : 00 NX        X[NX] Z[NX]
Anything else is kept as a raw 'value' (first 2 bytes).

Usage:
  python gs86_maps.py extract cal.bin [--csv out.csv]
  python gs86_maps.py compare a.bin b.bin [c.bin ...]   (same program layout)
"""
import struct, sys, csv, argparse

import os
LO = int(os.environ.get("CAL_LO", "0x8000"), 0)  # GS8.55: CAL_LO=0x4000
HI = 0xFFC0


def pointer_targets(d):
    t = set()
    for i in range(LO, min(len(d), HI) - 4, 2):
        v = struct.unpack(">I", d[i:i + 4])[0]
        if LO <= v < HI:
            # require being part of a run of >=3 pointers (a directory, not random data)
            nb = sum(1 for k in (-8, -4, 4, 8) if LO <= i + k < HI - 4 and
                     LO <= struct.unpack(">I", d[i + k:i + k + 4])[0] < HI)
            if nb >= 2:
                t.add(v)
    return sorted(t)


def inc(a):
    return all(a[i] < a[i + 1] for i in range(len(a) - 1))


def parse_at(d, a):
    if a + 4 <= len(d) and d[a] == 0 and d[a + 2] == 0 and 2 <= d[a + 1] <= 20 and 2 <= d[a + 3] <= 20:
        nx, ny = d[a + 1], d[a + 3]
        x = list(d[a + 4:a + 4 + nx]); y = list(d[a + 4 + nx:a + 4 + nx + ny])
        if inc(x) and inc(y):
            z0 = a + 4 + nx + ny
            z = list(d[z0:z0 + nx * ny])
            return {"addr": a, "type": "map", "nx": nx, "ny": ny, "x": x, "y": y, "z": z,
                    "size": 4 + nx + ny + nx * ny}
    if a + 2 <= len(d) and d[a] == 0 and 2 <= d[a + 1] <= 32:
        n = d[a + 1]
        x = list(d[a + 2:a + 2 + n])
        if inc(x):
            z = list(d[a + 2 + n:a + 2 + 2 * n])
            return {"addr": a, "type": "curve", "nx": n, "ny": 1, "x": x, "y": [], "z": z, "size": 2 + 2 * n}
    return {"addr": a, "type": "value", "nx": 1, "ny": 1, "x": [], "y": [], "z": list(d[a:a + 2]), "size": 2}


def program_refs(p, start=0x10000):
    """abs.L operands in program code that point into the calibration."""
    t = set()
    for i in range(start, len(p) - 4, 2):
        v = struct.unpack(">I", p[i:i + 4])[0]
        if LO <= v < HI:
            t.add(v)
    return t


def extract(d, prog=None):
    """prog: bytes of the matching program image (code at 0x10000+), or None.
    For a full-flash image (GS8.55) pass the image itself."""
    targets = set(pointer_targets(d))
    if prog is not None:
        targets |= program_refs(prog)
    items = [parse_at(d, a) for a in sorted(targets)]
    # drop items that start inside a previously parsed map/curve (axis/data pointers)
    out, end = [], 0
    for m in items:
        if m["addr"] < end and m["type"] == "value":
            continue
        if m["addr"] < end and m["type"] != "value":
            continue
        out.append(m)
        if m["type"] != "value":
            end = m["addr"] + m["size"]
    return out


def fmt_map(m, z=None):
    z = z if z is not None else m["z"]
    if m["type"] == "map":
        rows = ["        " + " ".join(f"{v:4d}" for v in m["x"])]
        for j, yv in enumerate(m["y"]):
            rows.append(f"  {yv:4d} |" + " ".join(f"{z[j * m['nx'] + i]:4d}" for i in range(m["nx"])))
        return "\n".join(rows)
    if m["type"] == "curve":
        return "   x " + " ".join(f"{v:4d}" for v in m["x"]) + "\n   y " + " ".join(f"{v:4d}" for v in z)
    return "   " + " ".join(f"{v:4d}" for v in z)


def main():
    ap = argparse.ArgumentParser()
    sp = ap.add_subparsers(dest="cmd", required=True)
    e = sp.add_parser("extract"); e.add_argument("file"); e.add_argument("--csv")
    c = sp.add_parser("compare"); c.add_argument("files", nargs="+"); c.add_argument("--all", action="store_true")
    a = ap.parse_args()
    if a.cmd == "extract":
        d = open(a.file, "rb").read()
        ms = extract(d)
        n = {t: sum(1 for m in ms if m["type"] == t) for t in ("map", "curve", "value")}
        print(f"{len(ms)} items: {n}")
        if a.csv:
            with open(a.csv, "w", newline="") as f:
                w = csv.writer(f)
                w.writerow(["addr", "type", "nx", "ny", "x", "y", "z"])
                for m in ms:
                    w.writerow([f"{m['addr']:05X}", m["type"], m["nx"], m["ny"],
                                " ".join(map(str, m["x"])), " ".join(map(str, m["y"])), " ".join(map(str, m["z"]))])
            print("wrote", a.csv)
    else:
        ds = [open(f, "rb").read() for f in a.files]
        base = extract(ds[0])
        print("files:", *[f"[{i}] {f}" for i, f in enumerate(a.files)], sep="\n  ")
        for m in base:
            vals = [parse_at(d, m["addr"]) for d in ds]
            if any(v["type"] != m["type"] or v["x"] != m["x"] or v["y"] != m["y"] for v in vals):
                print(f"\n{m['addr']:05X} {m['type']}: axes/shape differ between files")
                continue
            if not a.all and all(v["z"] == m["z"] for v in vals):
                continue
            print(f"\n=== {m['addr']:05X} {m['type']} {m['nx']}x{m['ny']}")
            for i, v in enumerate(vals):
                print(f"[{i}]" + ("" if i == 0 else "  (diff)" if v["z"] != m["z"] else "  (same)"))
                print(fmt_map(m, v["z"]))


if __name__ == "__main__":
    main()
