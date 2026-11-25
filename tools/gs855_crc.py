"""GS8.55 flash checksums, as implemented by the firmware (routine ~0x25810, helper 0x1C13A):
CRC-16, MSB-first, init 0, table at 0x10C68 in the image itself.
  region A   : 0x00000-0x041FF  -> stored big-endian at 0x05FFE
  program    : 0x10000-0x3F795  -> stored at 0x3F7FE
  calibration: 0x08000-0x0FFCD  -> stored at 0x0FFFE
usage: python gs855_crc.py image.bin [--fix out.bin]"""
import sys

REGIONS = [("regionA", 0x00000, 0x04200, 0x05FFE),
           ("program", 0x10000, 0x3F796, 0x3F7FE),
           ("calibration", 0x08000, 0x0FFCE, 0x0FFFE)]


def crc(img, s, e):
    tab = [int.from_bytes(img[0x10C68 + 2 * i:0x10C6A + 2 * i], "big") for i in range(256)]
    c = 0
    for b in img[s:e]:
        c = ((c << 8) & 0xFFFF) ^ tab[((c >> 8) ^ b) & 0xFF]
    return c


def check(img):
    out = []
    for name, s, e, at in REGIONS:
        calc, stored = crc(img, s, e), int.from_bytes(img[at:at + 2], "big")
        out.append((name, s, e, at, calc, stored))
    return out


if __name__ == "__main__":
    img = bytearray(open(sys.argv[1], "rb").read())
    for name, s, e, at, calc, stored in check(img):
        print(f"{name:12} {s:05X}-{e - 1:05X}  stored {stored:04X} @ {at:05X}  calc {calc:04X}  {'OK' if calc == stored else 'MISMATCH'}")
    if "--fix" in sys.argv:
        for name, s, e, at, calc, stored in check(img):
            img[at:at + 2] = calc.to_bytes(2, "big")
        out = sys.argv[sys.argv.index("--fix") + 1]
        open(out, "wb").write(img)
        print("wrote", out)
