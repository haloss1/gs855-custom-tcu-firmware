"""Minimal BMW DS2 (K-line, 9600 8E1) transport for K+DCAN / FTDI cables."""
import time
import serial


class DS2Error(Exception):
    pass


def xor(data):
    c = 0
    for b in data:
        c ^= b
    return c


class DS2:
    def __init__(self, port, baud=9600, timeout=1.0, dtr=False, rts=False, echo=True):
        self.s = serial.Serial(port, baud, bytesize=8, parity=serial.PARITY_EVEN,
                               stopbits=1, timeout=timeout)
        self.s.dtr = dtr
        self.s.rts = rts
        self.echo = echo
        time.sleep(0.2)
        self.s.reset_input_buffer()

    def close(self):
        self.s.close()

    def _read(self, n):
        b = self.s.read(n)
        if len(b) != n:
            raise DS2Error(f"timeout: wanted {n} bytes, got {len(b)} ({b.hex(' ')})")
        return b

    def request(self, addr, payload, retries=3):
        """Send [addr][len][payload...][xor]; return (status, data) of the answer."""
        tel = bytes([addr, len(payload) + 3]) + bytes(payload)
        tel += bytes([xor(tel)])
        last = None
        for _ in range(retries):
            try:
                self.s.reset_input_buffer()
                self.s.write(tel)
                if self.echo:
                    e = self._read(len(tel))
                    if e != tel:
                        raise DS2Error(f"bad echo {e.hex(' ')}")
                hdr = self._read(2)
                if hdr[0] != addr:
                    raise DS2Error(f"unexpected address in answer {hdr.hex(' ')}")
                rest = self._read(hdr[1] - 2)
                ans = hdr + rest
                if xor(ans[:-1]) != ans[-1]:
                    raise DS2Error(f"checksum error {ans.hex(' ')}")
                return ans[2], ans[3:-1]
            except DS2Error as e:
                last = e
                time.sleep(0.3)
                self.s.reset_input_buffer()
        raise last
