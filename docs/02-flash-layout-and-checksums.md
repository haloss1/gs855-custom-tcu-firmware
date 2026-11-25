# 02: Flash layout and checksums (B22P0_24)

## Memory map

| Range | Contents |
|---|---|
| 0x00000-0x03FFF | Boot (vectors: SSP 0xFFFFF28E, reset 0x400). Matches the AM29F200B 16 KB boot sector. |
| 0x04000-0x07FFF | Identification blocks, the TCU's own flash log (0x4206 onward), AIF records (0x602E), region-A CRC (0x5FFE) |
| 0x08000-0x0FFFF | Calibration (map programming area; this is what the WinKFP data file covers) |
| 0x10000-0x3F7FF | Program (second vector table at 0x10000, entry 0x15000) |
| 0x3F796-0x3F7FF | Program ident block |

Data idents: 0xFFCE `B22P0_2442C0RD43`, 0x3F796 `B22P0_2442C0...1423159...`.

## TCU checksums

Routine around 0x25810, helper 0x1C13A. CRC-16, MSB-first, initial value 0, lookup table stored in the
image at 0x10C68:

```
crc = ((crc << 8) & 0xFFFF) ^ table[((crc >> 8) ^ byte) & 0xFF]
```

| Region | Range | Stored at (big-endian) |
|---|---|---|
| A | 0x00000-0x041FF | 0x5FFE |
| Program | 0x10000-0x3F795 | 0x3F7FE |
| Calibration | 0x08000-0x0FFCD | 0x0FFFE |

A mismatch sets bits in RAM 0xFFFFB74F. `tools/gs855_crc.py image.bin [--fix out.bin]` checks and fixes
all three. The `_22` community dumps use a different table/layout (their CRCs don't verify with these
parameters).

## Boot code

- Flash programming uses standard AMD commands with word-mode unlock addresses 0xAAAA / 0x5554
  (program ~0x2DE6-0x2E70, erase ~0x2F16-0x2FA0).
- DS2 command table at 0x3CCE, 6 bytes per entry (command byte, `00`, 32-bit handler address):

| Cmd | Handler |
|---|---|
| 00 (ident) | 0x0F5E |
| 06 (read memory) | 0x105C |
| 07 (write) | 0x10EE |
| 0A (erase) | 0x1332 |
| 0D | 0x1500 |
| 90 / 91 / 9E / 9F | 0x156A / 0x16DA / 0x1744 / 0x1764 |

- After a WinKFP flash the unit stays in boot mode until the ignition is cycled: ident and memory read
  work, but application jobs (fault memory, adaptations) answer NACK.
