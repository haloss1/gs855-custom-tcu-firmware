"""Read-only RAM monitor for the GS8.55 over DS2 (memory type 0x04 = RAM_EXTERN).
Logs every byte that changes, with elapsed seconds.
usage: python ram_monitor.py COM1 SECONDS [START END]   (hex, 24-bit, default FFF480 FFF780)"""
import sys, time
from ds2 import DS2

port = sys.argv[1]
dur = float(sys.argv[2])
start = int(sys.argv[3], 16) if len(sys.argv) > 3 else 0xFFF480
end = int(sys.argv[4], 16) if len(sys.argv) > 4 else 0xFFF780
d = DS2(port)


def snap():
    out = bytearray()
    a = start
    while a < end:
        n = min(0xF8, end - a)
        st, data = d.request(0x32, [0x06, 0x04, a >> 16, (a >> 8) & 0xFF, a & 0xFF, n])
        if st != 0xA0 or len(data) != n:
            raise RuntimeError(f"read {a:06X} status {st:02X}")
        out += data
        a += n
    return bytes(out)


t0 = time.time()
prev = snap()
print(f"[{0:6.1f}s] baseline {start:06X}-{end:06X} ({len(prev)} bytes)", flush=True)
with open("ram_baseline.bin", "wb") as f:
    f.write(prev)
passes = 0
while time.time() - t0 < dur:
    try:
        cur = snap()
    except Exception as e:
        print(f"[{time.time()-t0:6.1f}s] read error: {e}; reopening {port}", flush=True)
        try:
            d.close()
        except Exception:
            pass
        time.sleep(1.0)
        try:
            d = DS2(port)
        except Exception as e2:
            print(f"[{time.time()-t0:6.1f}s] reopen failed: {e2}", flush=True)
        continue
    passes += 1
    ch = [i for i in range(len(cur)) if cur[i] != prev[i]]
    if ch:
        print(f"[{time.time()-t0:6.1f}s] " + "  ".join(f"{start+i:06X}:{prev[i]:02X}->{cur[i]:02X}" for i in ch), flush=True)
    prev = cur
print(f"[{time.time()-t0:6.1f}s] done, {passes} passes", flush=True)
d.close()
