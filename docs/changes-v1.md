# GS8.55 Alpina port v1: every change vs stock (G1423170 / RD43)

253 bytes in 31 runs. Addresses are GS8.55 flash addresses.

| GS8.55 addr | bytes | origin | table | stock | port |
|---|---|---|---|---|---|
| 0x082A2-0x082A2 | 1 | v1: function mask, evaluators off (0x8B4B) | raw data / 16-bit table | f7 | 11 |
| 0x082A3-0x082A3 | 1 | v1: option byte, evaluator D off (0x8B4C) | raw data / 16-bit table | fa | f8 |
| 0x082AA-0x082AB | 2 | v1: driving-style lower limits (0x8340) | curve 2x1 @0x082A6 (values) | 20 81 | 00 00 |
| 0x082B0-0x082B1 | 2 | v1: driving-style upper limits (0x833C) | curve 2x1 @0x082AC (values) | 80 ff | 00 00 |
| 0x082B4-0x082B7 | 4 | v1: driving-style thresholds (0x834A) | curve 4x1 @0x082B2 (axis/header) | 00 41 81 c1 | ff ff ff ff |
| 0x08606-0x08606 | 1 | v1: gate default -> manual (GS8.60.2 0x83EB) | raw data / 16-bit table | fe | 0b |
| 0x08DF4-0x08DF9 | 6 | v1: shift map (Alpina delta from GS8.60.2 0x9666) | map 8x11 @0x08DDC (values) | 13 1d 30 09 10 19 | 15 1f 37 08 0b 18 |
| 0x08DFC-0x08E01 | 6 | v1: shift map (Alpina delta from GS8.60.2 0x9666) | map 8x11 @0x08DDC (values) | 13 1d 30 09 10 19 | 15 1f 37 08 0b 18 |
| 0x08E04-0x08E09 | 6 | v1: shift map (Alpina delta from GS8.60.2 0x9666) | map 8x11 @0x08DDC (values) | 1a 29 3d 09 10 19 | 1c 2a 3e 08 0b 18 |
| 0x08E0B-0x08E36 | 44 | v1: shift map (Alpina delta from GS8.60.2 0x9666) | map 8x11 @0x08DDC (values) | 13 26 3b 5b 09 10 19 2c 18 2f 48 70 09 10 19 2c 1d 37 53 83 09 10 19 4f ... | 0f 20 35 59 08 0b 18 32 10 26 3e 6c 08 0b 1a 38 12 2b 41 81 08 0e 20 3f ... |
| 0x08E38-0x08E3E | 7 | v1: shift map (Alpina delta from GS8.60.2 0x9666) | map 8x11 @0x08DDC (values) | 27 4e 83 29 4a 6f b4 | 23 51 7d 2c 4c 74 b7 |
| 0x08E40-0x08E4A | 11 | v1: shift map (Alpina delta from GS8.60.2 0x9666) | map 8x11 @0x08DDC (values) | 27 4e 83 2b 4d 73 b8 20 43 6c b0 | 23 51 7d 2c 4b 72 af 1e 40 68 ab |
| 0x09254-0x09259 | 6 | v1: shift map (Alpina delta from GS8.60.2 0x9276) | map 8x11 @0x0923C (values) | 13 1d 30 09 10 19 | 15 1f 37 08 0b 18 |
| 0x0925C-0x09261 | 6 | v1: shift map (Alpina delta from GS8.60.2 0x9276) | map 8x11 @0x0923C (values) | 13 1d 30 09 10 19 | 15 1f 37 08 0b 18 |
| 0x09264-0x09269 | 6 | v1: shift map (Alpina delta from GS8.60.2 0x9276) | map 8x11 @0x0923C (values) | 1a 29 42 09 10 19 | 1c 2a 3f 08 0b 18 |
| 0x0926B-0x09296 | 44 | v1: shift map (Alpina delta from GS8.60.2 0x9276) | map 8x11 @0x0923C (values) | 13 26 3b 97 09 10 19 2c 18 2f 48 a7 09 10 19 3f 1d 37 53 b4 09 10 19 4f ... | 0f 20 35 59 08 0b 18 32 10 26 3e 6f 08 0b 1a 36 12 2b 41 84 08 0e 20 3f ... |
| 0x09298-0x0929E | 7 | v1: shift map (Alpina delta from GS8.60.2 0x9276) | map 8x11 @0x0923C (values) | 27 4e 83 29 4a 6f b4 | 23 51 7d 2c 4c 74 b7 |
| 0x092A0-0x092AA | 11 | v1: shift map (Alpina delta from GS8.60.2 0x9276) | map 8x11 @0x0923C (values) | 27 4e 83 2b 4d 73 b8 20 43 6c b0 | 23 51 7d 2c 4b 72 af 1e 40 68 ab |
| 0x092C3-0x092C6 | 4 | v1: shift map (Alpina delta from GS8.60.2 0x94A6) | map 8x11 @0x092AC (values) | 2b 4d 73 b8 | 30 55 7e c3 |
| 0x092C8-0x092CE | 7 | v1: shift map (Alpina delta from GS8.60.2 0x94A6) | map 8x11 @0x092AC (values) | 00 19 2c 2b 4d 73 b8 | 0e 18 2a 30 55 7e c3 |
| 0x092D0-0x092D6 | 7 | v1: shift map (Alpina delta from GS8.60.2 0x94A6) | map 8x11 @0x092AC (values) | 00 19 2c 2b 4d 73 b8 | 0e 18 2a 30 55 7e c3 |
| 0x092D8-0x092DE | 7 | v1: shift map (Alpina delta from GS8.60.2 0x94A6) | map 8x11 @0x092AC (values) | 00 19 2c 2b 4d 73 b8 | 0e 18 2a 30 55 7e c3 |
| 0x092E0-0x092E6 | 7 | v1: shift map (Alpina delta from GS8.60.2 0x94A6) | map 8x11 @0x092AC (values) | 00 19 2c 2b 4d 73 b8 | 0e 18 2a 30 55 7e c3 |
| 0x092E8-0x092EE | 7 | v1: shift map (Alpina delta from GS8.60.2 0x94A6) | map 8x11 @0x092AC (values) | 00 19 2c 2b 4d 73 b8 | 0e 18 2a 30 55 7e c3 |
| 0x092F0-0x092F6 | 7 | v1: shift map (Alpina delta from GS8.60.2 0x94A6) | map 8x11 @0x092AC (values) | 00 19 2c 2b 4d 73 b8 | 0e 18 2a 30 55 7e c3 |
| 0x092F8-0x092FE | 7 | v1: shift map (Alpina delta from GS8.60.2 0x94A6) | map 8x11 @0x092AC (values) | 00 19 2c 2b 4d 73 b8 | 0e 18 2a 30 55 7e c3 |
| 0x09300-0x09306 | 7 | v1: shift map (Alpina delta from GS8.60.2 0x94A6) | map 8x11 @0x092AC (values) | 00 19 2c 2b 4d 73 b8 | 0e 18 2a 30 55 7e c3 |
| 0x09308-0x0930E | 7 | v1: shift map (Alpina delta from GS8.60.2 0x94A6) | map 8x11 @0x092AC (values) | 00 19 2c 2b 4d 73 b8 | 0e 18 2a 30 55 7e c3 |
| 0x09310-0x0931A | 11 | v1: shift map (Alpina delta from GS8.60.2 0x94A6) | map 8x11 @0x092AC (values) | 00 19 2c 2b 4d 73 b8 20 43 6c b0 | 0e 18 2a 30 55 7e c3 24 4b 75 bf |
| 0x0FFCC-0x0FFCD | 2 | padding (sets WinKFP file checksum) | raw data / 16-bit table | ff ff | 00 2b |
| 0x0FFFE-0x0FFFF | 2 | calibration CRC | raw data / 16-bit table | 87 a8 | 8a ee |
