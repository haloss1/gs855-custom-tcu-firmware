"""Run READ-ONLY jobs of an SGBD through EDIABAS (api64.dll) and print all results.
usage: python ediabas_read.py SGBD JOB [JOB ...]
Refuses any job whose name suggests writing, erasing, unlocking or mode changes."""
import ctypes, sys, time

FORBIDDEN = ("SCHREIB", "LOESCH", "SEED", "KEY", "UPROG_EIN", "UPROG_AUS", "SCHALTE", "UMSTELL",
             "RESET", "SET_", "PROGRAMM", "STEUERN", "ENDE")
_dll = ctypes.WinDLL(r"C:\EDIABAS\Bin\api64.dll")
_h = ctypes.c_uint(0)


class _Api:
    """Wrap the handle-based __api* exports so calls look like the classic API."""
    def __getattr__(self, name):
        f = getattr(_dll, "__" + name)
        if name == "apiInit":
            return lambda: f(ctypes.byref(_h))
        if name in ("apiState", "apiErrorCode"):
            f.restype = ctypes.c_int
        if name == "apiErrorText":
            f.restype = ctypes.c_char_p
        return lambda *a: f(_h, *a)


api = _Api()
APIBUSY, APIREADY, APIBREAK, APIERROR = 0, 1, 2, 3
FMT = {0: "char", 1: "byte", 2: "int", 3: "word", 4: "long", 5: "dword", 6: "text", 7: "binary", 8: "real"}



def run(sgbd, job, para=""):
    api.apiJob(sgbd.encode(), job.encode(), para.encode(), b"")
    t0 = time.time()
    while api.apiState() == APIBUSY:
        time.sleep(0.05)
        if time.time() - t0 > 30:
            api.apiBreak()
            return None, "timeout"
    st = api.apiState()
    if st == APIERROR:
        return None, f"EDIABAS error {api.apiErrorCode()}: {api.apiErrorText().decode(errors='replace')}"
    sets = ctypes.c_ushort()
    api.apiResultSets(ctypes.byref(sets))
    out = []
    for s in range(0, sets.value + 1):
        n = ctypes.c_ushort()
        if not api.apiResultNumber(ctypes.byref(n), s):
            continue
        for i in range(1, n.value + 1):
            name = ctypes.create_string_buffer(64)
            api.apiResultName(name, i, s)
            fmt = ctypes.c_int()
            api.apiResultFormat(ctypes.byref(fmt), name.value, s)
            if fmt.value == 7:
                buf = ctypes.create_string_buffer(1100)
                ln = ctypes.c_ushort()
                api.apiResultBinary(buf, ctypes.byref(ln), name.value, s)
                val = buf.raw[:ln.value].hex(" ")
            else:
                buf = ctypes.create_string_buffer(1100)
                api.apiResultText(buf, name.value, s, b"")
                val = buf.value.decode("latin-1")
            out.append((s, name.value.decode(), FMT.get(fmt.value, fmt.value), val))
    return out, None


sgbd, jobs = sys.argv[1], sys.argv[2:]
if not api.apiInit():
    sys.exit(f"apiInit failed: {api.apiErrorText().decode(errors='replace')}")
try:
    for job in jobs:
        if any(f in job.upper() for f in FORBIDDEN):
            print(f"== {job}: SKIPPED (not read-only)")
            continue
        res, err = run(sgbd, job)
        print(f"== {sgbd}.{job}")
        if err:
            print("   ", err)
            continue
        for s, name, fmt, val in res:
            if s == 0 and name in ("VARIANTE", "OBJECT", "SAETZE", "JOBNAME", "JOBSTATUS", "UBATTCURRENT",
                                    "UBATTHISTORY", "IGNITIONCURRENT", "IGNITIONHISTORY"):
                continue
            print(f"   [{s}] {name:32} {val}")
finally:
    api.apiEnd()

