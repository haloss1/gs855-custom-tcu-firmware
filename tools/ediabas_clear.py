"""Run exactly two writing jobs on the GS8.55 via EDIABAS: clear fault memory, reset adaptations.
Nothing else is allowed. Then re-read the fault memory."""
import ctypes, time

ALLOWED = ("FS_LOESCHEN", "RESET_ADAPTION")
_dll = ctypes.WinDLL(r"C:\EDIABAS\Bin\api64.dll")
h = ctypes.c_uint(0)
_dll.__apiState.restype = ctypes.c_int
_dll.__apiErrorText.restype = ctypes.c_char_p


def job(sgbd, name):
    _dll.__apiJob(h, sgbd.encode(), name.encode(), b"", b"")
    t0 = time.time()
    while _dll.__apiState(h) == 0:
        time.sleep(0.05)
        if time.time() - t0 > 30:
            _dll.__apiBreak(h)
            return "timeout"
    if _dll.__apiState(h) == 3:
        return "EDIABAS error: " + _dll.__apiErrorText(h).decode(errors="replace")
    buf = ctypes.create_string_buffer(256)
    sets = ctypes.c_ushort()
    _dll.__apiResultSets(h, ctypes.byref(sets))
    for s in range(1, sets.value + 1):
        if _dll.__apiResultText(h, buf, b"JOB_STATUS", s, b""):
            return buf.value.decode()
    return "?"


if not _dll.__apiInit(ctypes.byref(h)):
    raise SystemExit("apiInit failed")
try:
    for name in ALLOWED:
        print(f"GS855.{name}: {job('GS855', name)}")
    _dll.__apiJob(h, b"GS855", b"FS_LESEN", b"", b"")
    while _dll.__apiState(h) == 0:
        time.sleep(0.05)
    n = ctypes.c_ushort(); sets = ctypes.c_ushort()
    _dll.__apiResultSets(h, ctypes.byref(sets))
    buf = ctypes.create_string_buffer(256)
    _dll.__apiResultText(h, buf, b"F_ANZ_NR", 1, b"")
    print("faults stored after clearing:", buf.value.decode() or "0 (no fault records)")
finally:
    _dll.__apiEnd(h)
