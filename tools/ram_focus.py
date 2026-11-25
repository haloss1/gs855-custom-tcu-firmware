"""Read-only fast RAM monitor for the GS8.55 (DS2 0x06, type 0x04).
Each pass: the focus ranges, plus one rotating 248-byte slice of FFF290-FFF800.
Logs changes with elapsed time.  usage: python ram_focus.py COM1 SECONDS"""
import sys, time
from ds2 import DS2

port, dur = sys.argv[1], float(sys.argv[2])
FOCUS = [(0xFFF2F0, 0x10), (0xFFF350, 0x10), (0xFFF490, 0x20), (0xFFF560, 0x10),
         (0xFFF6A0, 0x10), (0xFFF730, 0x30)]
SWEEP_LO, SWEEP_HI, STEP = 0xFFF290, 0xFFF800, 0xF8
d = DS2(port)
mem = {}


def rd(a, n):
    st, data = d.request(0x32, [0x06, 0x04, a >> 16, (a >> 8) & 0xFF, a & 0xFF, n])
    if st != 0xA0 or len(data) != n:
        raise RuntimeError(f"read {a:06X} status {st:02X}")
    return data


def take(a, data, t, log):
    ch = []
    for i, b in enumerate(data):
        k = a + i
        if k in mem and mem[k] != b:
            ch.append(f"{k:06X}:{mem[k]:02X}->{b:02X}")
        mem[k] = b
    if ch:
        log(f"[{t:6.1f}s] " + "  ".join(ch))


log = lambda s: print(s, flush=True)
t0 = time.time()
sw = SWEEP_LO
# baseline
for a, n in FOCUS:
    take(a, rd(a, n), 0, log)
a = SWEEP_LO
while a < SWEEP_HI:
    n = min(STEP, SWEEP_HI - a); take(a, rd(a, n), 0, log); a += n
log(f"[{time.time()-t0:6.1f}s] baseline done")
passes = 0
while time.time() - t0 < dur:
    try:
        for a, n in FOCUS:
            take(a, rd(a, n), time.time() - t0, log)
        n = min(STEP, SWEEP_HI - sw)
        take(sw, rd(sw, n), time.time() - t0, log)
        sw = SWEEP_LO if sw + n >= SWEEP_HI else sw + n
        passes += 1
    except Exception as e:
        log(f"[{time.time()-t0:6.1f}s] read error: {e}; reopening")
        try:
            d.close()
        except Exception:
            pass
        time.sleep(1)
        try:
            d = DS2(port)
        except Exception as e2:
            log(f"[{time.time()-t0:6.1f}s] reopen failed: {e2}")
log(f"[{time.time()-t0:6.1f}s] done, {passes} passes ({passes/max(time.time()-t0,1):.1f}/s)")
d.close()
