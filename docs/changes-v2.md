# GS8.55 Alpina port v2: every change vs stock (G1423170 / RD43)

1328 bytes in 552 runs. Addresses are GS8.55 flash addresses.

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
| 0x09519-0x09521 | 9 | v2: converter lockup table (Alpina values, GS8.60.2 0x97C0) | raw data / 16-bit table | 00 00 00 1f 22 5a 2d 30 5a | 1f 22 22 29 2c 2c 29 2c 2c |
| 0x0952B-0x0952D | 3 | v2: converter lockup table (Alpina values, GS8.60.2 0x97C0) | raw data / 16-bit table | 2d 30 5a | 27 2a 2a |
| 0x09531-0x0953F | 15 | v2: converter lockup table (Alpina values, GS8.60.2 0x97C0) | raw data / 16-bit table | 00 00 00 37 3a 5a 00 00 00 1f 22 5a 2d 30 5a | 2f 32 32 2d 30 30 16 19 19 27 2a 2a 29 2c 2c |
| 0x09549-0x0954B | 3 | v2: converter lockup table (Alpina values, GS8.60.2 0x97C0) | raw data / 16-bit table | 2d 30 5a | 1e 21 21 |
| 0x0954F-0x0955D | 15 | v2: converter lockup table (Alpina values, GS8.60.2 0x97C0) | raw data / 16-bit table | 00 00 00 37 3a 5a 00 00 00 1f 22 5a 2d 30 5a | 2f 32 32 2d 30 30 16 19 19 27 2a 2a 29 2c 2c |
| 0x09567-0x09569 | 3 | v2: converter lockup table (Alpina values, GS8.60.2 0x97C0) | raw data / 16-bit table | 2d 30 5a | 1e 21 21 |
| 0x0956D-0x0957B | 15 | v2: converter lockup table (Alpina values, GS8.60.2 0x97C0) | raw data / 16-bit table | 00 00 00 37 3a 5a 00 00 00 1f 27 5a 2d 34 5a | 2f 32 32 2d 30 30 16 19 19 27 2a 2a 29 2c 2c |
| 0x09585-0x09587 | 3 | v2: converter lockup table (Alpina values, GS8.60.2 0x97C0) | raw data / 16-bit table | 2d 30 5a | 1e 21 21 |
| 0x0958B-0x09599 | 15 | v2: converter lockup table (Alpina values, GS8.60.2 0x97C0) | raw data / 16-bit table | 00 00 00 37 3a 5a 00 00 00 25 2d 5a 32 39 5a | 2f 32 32 2d 30 30 16 18 19 27 29 2a 29 2b 2c |
| 0x095A3-0x095A5 | 3 | v2: converter lockup table (Alpina values, GS8.60.2 0x97C0) | raw data / 16-bit table | 2d 30 5a | 1e 20 21 |
| 0x095A9-0x095B7 | 15 | v2: converter lockup table (Alpina values, GS8.60.2 0x97C0) | raw data / 16-bit table | 00 00 00 37 3a 5a 00 00 00 2b 59 5a 38 59 5a | 2f 31 32 2d 2f 30 16 18 19 27 29 2a 29 2b 2c |
| 0x095C1-0x095C3 | 3 | v2: converter lockup table (Alpina values, GS8.60.2 0x97C0) | raw data / 16-bit table | 2d 59 5a | 1e 20 21 |
| 0x095C7-0x095D5 | 15 | v2: converter lockup table (Alpina values, GS8.60.2 0x97C0) | raw data / 16-bit table | 00 00 00 37 59 5a 00 00 00 56 59 5a 56 59 5a | 2f 31 32 2d 2f 30 16 18 19 27 29 2a 29 2b 2c |
| 0x095DF-0x095E1 | 3 | v2: converter lockup table (Alpina values, GS8.60.2 0x97C0) | raw data / 16-bit table | 56 59 5a | 1e 20 21 |
| 0x095E5-0x095EA | 6 | v2: converter lockup table (Alpina values, GS8.60.2 0x97C0) | raw data / 16-bit table | 00 00 00 56 59 5a | 2f 31 32 2d 2f 30 |
| 0x0C2E7-0x0C2E7 | 1 | v2: exact-context port from GS8.60.2 0x0C107 | raw data / 16-bit table | 9c | 38 |
| 0x0C2E9-0x0C2E9 | 1 | v2: exact-context port from GS8.60.2 0x0C107 | raw data / 16-bit table | 28 | 3c |
| 0x0C2EB-0x0C2EB | 1 | v2: exact-context port from GS8.60.2 0x0C107 | raw data / 16-bit table | 28 | 3c |
| 0x0C2ED-0x0C2ED | 1 | v2: exact-context port from GS8.60.2 0x0C107 | raw data / 16-bit table | d6 | cc |
| 0x0C2EF-0x0C2EF | 1 | v2: exact-context port from GS8.60.2 0x0C107 | raw data / 16-bit table | 5e | 68 |
| 0x0C2F1-0x0C2F1 | 1 | v2: exact-context port from GS8.60.2 0x0C107 | raw data / 16-bit table | c4 | 88 |
| 0x0C2F3-0x0C2F3 | 1 | v2: exact-context port from GS8.60.2 0x0C107 | raw data / 16-bit table | 5a | 8c |
| 0x0C2F5-0x0C2F5 | 1 | v2: exact-context port from GS8.60.2 0x0C107 | raw data / 16-bit table | 2c | 54 |
| 0x0C2F7-0x0C2F7 | 1 | v2: exact-context port from GS8.60.2 0x0C107 | raw data / 16-bit table | 2a | 48 |
| 0x0C2FA-0x0C2FF | 6 | v2: exact-context port from GS8.60.2 0x0C107 | raw data / 16-bit table | 18 9c 0f 28 0f 28 | 17 d4 0e d8 0e d8 |
| 0x0C301-0x0C301 | 1 | v2: exact-context port from GS8.60.2 0x0C107 | raw data / 16-bit table | d6 | 68 |
| 0x0C303-0x0C303 | 1 | v2: exact-context port from GS8.60.2 0x0C107 | raw data / 16-bit table | 5e | 04 |
| 0x0C305-0x0C305 | 1 | v2: exact-context port from GS8.60.2 0x0C107 | raw data / 16-bit table | c4 | 24 |
| 0x0C307-0x0C30B | 5 | v2: exact-context port from GS8.60.2 0x0C107 | raw data / 16-bit table | 5a 0b 2c 0d 2a | 28 0a f0 0c e4 |
| 0x0C4C8-0x0C4CB | 4 | v2: exact-context port from GS8.60.2 0x0C340 | raw data / 16-bit table | ff 42 ff c1 | 00 00 00 14 |
| 0x0C4CD-0x0C4CD | 1 | v2: exact-context port from GS8.60.2 0x0C340 | raw data / 16-bit table | 3f | 32 |
| 0x0C4CF-0x0C4D1 | 3 | v2: exact-context port from GS8.60.2 0x0C340 | raw data / 16-bit table | be ff d8 | 5a 00 28 |
| 0x0C4D3-0x0C4D3 | 1 | v2: exact-context port from GS8.60.2 0x0C340 | raw data / 16-bit table | 17 | 32 |
| 0x0C4D5-0x0C4D5 | 1 | v2: exact-context port from GS8.60.2 0x0C340 | raw data / 16-bit table | 57 | 50 |
| 0x0C4D7-0x0C4D7 | 1 | v2: exact-context port from GS8.60.2 0x0C340 | raw data / 16-bit table | 96 | 82 |
| 0x0C4D9-0x0C4D9 | 1 | v2: exact-context port from GS8.60.2 0x0C340 | raw data / 16-bit table | 00 | 02 |
| 0x0C4DB-0x0C4DB | 1 | v2: exact-context port from GS8.60.2 0x0C340 | raw data / 16-bit table | 00 | 05 |
| 0x0C4DD-0x0C4DD | 1 | v2: exact-context port from GS8.60.2 0x0C340 | raw data / 16-bit table | 00 | 0a |
| 0x0C4DF-0x0C4DF | 1 | v2: exact-context port from GS8.60.2 0x0C340 | raw data / 16-bit table | 00 | 0a |
| 0x0C4E1-0x0C4E1 | 1 | v2: exact-context port from GS8.60.2 0x0C340 | raw data / 16-bit table | 00 | 02 |
| 0x0C4E3-0x0C4E3 | 1 | v2: exact-context port from GS8.60.2 0x0C340 | raw data / 16-bit table | 00 | 05 |
| 0x0C4E5-0x0C4E5 | 1 | v2: exact-context port from GS8.60.2 0x0C340 | raw data / 16-bit table | 00 | 0a |
| 0x0C4E7-0x0C4E7 | 1 | v2: exact-context port from GS8.60.2 0x0C340 | raw data / 16-bit table | 00 | 0a |
| 0x0C4E9-0x0C4E9 | 1 | v2: exact-context port from GS8.60.2 0x0C340 | raw data / 16-bit table | 00 | 02 |
| 0x0C4EB-0x0C4EB | 1 | v2: exact-context port from GS8.60.2 0x0C340 | raw data / 16-bit table | 00 | 05 |
| 0x0C4ED-0x0C4ED | 1 | v2: exact-context port from GS8.60.2 0x0C340 | raw data / 16-bit table | 00 | 0a |
| 0x0C4EF-0x0C4EF | 1 | v2: exact-context port from GS8.60.2 0x0C340 | raw data / 16-bit table | 00 | 0a |
| 0x0C4F3-0x0C4F3 | 1 | v2: exact-context port from GS8.60.2 0x0C340 | raw data / 16-bit table | 00 | 04 |
| 0x0C4F5-0x0C4F5 | 1 | v2: exact-context port from GS8.60.2 0x0C340 | raw data / 16-bit table | 00 | 0a |
| 0x0C4F7-0x0C4F7 | 1 | v2: exact-context port from GS8.60.2 0x0C340 | raw data / 16-bit table | 00 | 0a |
| 0x0C5A7-0x0C5A8 | 2 | v2: exact-context port from GS8.60.2 0x0C437 | curve 3x1 @0x0C5A2 (values) | 16 16 | 14 14 |
| 0x0C5C7-0x0C5C8 | 2 | v2: exact-context port from GS8.60.2 0x0C45F | curve 3x1 @0x0C5C2 (values) | 06 0a | 08 08 |
| 0x0C5CF-0x0C5D0 | 2 | v2: exact-context port from GS8.60.2 0x0C467 | curve 3x1 @0x0C5CA (values) | 10 10 | 0c 0c |
| 0x0C5EF-0x0C5F0 | 2 | v2: exact-context port from GS8.60.2 0x0C48F | curve 3x1 @0x0C5EA (values) | 0a 0a | 0c 0c |
| 0x0C5FB-0x0C5FB | 1 | v2: exact-context port from GS8.60.2 0x0C49B | curve 7x1 @0x0C5F2 (values) | a6 | a2 |
| 0x0C5FE-0x0C5FE | 1 | v2: exact-context port from GS8.60.2 0x0C49B | curve 7x1 @0x0C5F2 (values) | 88 | 84 |
| 0x0C60B-0x0C60B | 1 | v2: exact-context port from GS8.60.2 0x0C4AB | curve 7x1 @0x0C602 (values) | a6 | a2 |
| 0x0C62B-0x0C62B | 1 | v2: exact-context port from GS8.60.2 0x0C4DB | curve 7x1 @0x0C622 (values) | a4 | a2 |
| 0x0C63B-0x0C63B | 1 | v2: exact-context port from GS8.60.2 0x0C4EB | curve 7x1 @0x0C632 (values) | 94 | 8a |
| 0x0C677-0x0C677 | 1 | v2: exact-context port from GS8.60.2 0x0C535 | curve 6x1 @0x0C66C (values) | 96 | 94 |
| 0x0C6D4-0x0C6D4 | 1 | v2: exact-context port from GS8.60.2 0x0C5A2 | curve 7x1 @0x0C6C8 (values) | 80 | 7c |
| 0x0C6F3-0x0C6F3 | 1 | v2: exact-context port from GS8.60.2 0x0C5C1 | curve 6x1 @0x0C6E6 (values) | c6 | f8 |
| 0x0C70B-0x0C70F | 5 | v2: close-curve delta (Alpina change on GS8.55 values) | curve 6x1 @0x0C702 (values) | 84 88 9c b0 f8 | 7e 7c 8a c2 ff |
| 0x0C72E-0x0C72F | 2 | v2: exact-context port from GS8.60.2 0x0C61A | curve 6x1 @0x0C72C (axis/header) | 00 14 | 0a 19 |
| 0x0C731-0x0C731 | 1 | v2: exact-context port from GS8.60.2 0x0C61A | curve 6x1 @0x0C72C (axis/header) | 3c | 32 |
| 0x0C733-0x0C733 | 1 | v2: exact-context port from GS8.60.2 0x0C61A | curve 6x1 @0x0C72C (axis/header) | 64 | 82 |
| 0x0C758-0x0C759 | 2 | v2: exact-context port from GS8.60.2 0x0C652 | curve 6x1 @0x0C756 (axis/header) | 00 14 | 0a 19 |
| 0x0C75B-0x0C75B | 1 | v2: exact-context port from GS8.60.2 0x0C652 | curve 6x1 @0x0C756 (axis/header) | 3c | 32 |
| 0x0C75D-0x0C75D | 1 | v2: exact-context port from GS8.60.2 0x0C652 | curve 6x1 @0x0C756 (axis/header) | 64 | 82 |
| 0x0C7D1-0x0C7D1 | 1 | v2: exact-context port from GS8.60.2 0x0C6D9 | raw data / 16-bit table | 0a | 1e |
| 0x0C7ED-0x0C7ED | 1 | v2: exact-context port from GS8.60.2 0x0C6F5 | raw data / 16-bit table | 0a | 1e |
| 0x0C7F3-0x0C7F3 | 1 | v2: exact-context port from GS8.60.2 0x0C6FB | raw data / 16-bit table | c8 | f0 |
| 0x0C7FB-0x0C7FB | 1 | v2: exact-context port from GS8.60.2 0x0C703 | raw data / 16-bit table | 0a | 1e |
| 0x0C80F-0x0C80F | 1 | v2: exact-context port from GS8.60.2 0x0C725 | raw data / 16-bit table | b4 | f0 |
| 0x0C817-0x0C817 | 1 | v2: exact-context port from GS8.60.2 0x0C72D | raw data / 16-bit table | 0a | 1e |
| 0x0C81D-0x0C81D | 1 | v2: exact-context port from GS8.60.2 0x0C733 | raw data / 16-bit table | c8 | f0 |
| 0x0C82F-0x0C82F | 1 | v2: exact-context port from GS8.60.2 0x0C745 | curve 7x1 @0x0C822 (values) | 80 | 83 |
| 0x0C86B-0x0C86E | 4 | v2: exact-context port from GS8.60.2 0x0C791 | curve 7x1 @0x0C862 (values) | 9b 8f 88 81 | 96 8a 83 80 |
| 0x0C87A-0x0C87B | 2 | v2: exact-context port from GS8.60.2 0x0C7A0 | curve 6x1 @0x0C872 (values) | 02 03 | 04 05 |
| 0x0C943-0x0C943 | 1 | v2: exact-context port from GS8.60.2 0x0C8A5 | raw data / 16-bit table | 28 | 2d |
| 0x0C945-0x0C945 | 1 | v2: exact-context port from GS8.60.2 0x0C8A5 | raw data / 16-bit table | 1e | 28 |
| 0x0C951-0x0C951 | 1 | v2: exact-context port from GS8.60.2 0x0C8B3 | raw data / 16-bit table | 28 | 23 |
| 0x0C953-0x0C953 | 1 | v2: exact-context port from GS8.60.2 0x0C8B3 | raw data / 16-bit table | 1e | 19 |
| 0x0C955-0x0C955 | 1 | v2: exact-context port from GS8.60.2 0x0C8B3 | raw data / 16-bit table | 1e | 19 |
| 0x0C961-0x0C961 | 1 | v2: exact-context port from GS8.60.2 0x0C8C3 | raw data / 16-bit table | 1e | 28 |
| 0x0C963-0x0C963 | 1 | v2: exact-context port from GS8.60.2 0x0C8C3 | raw data / 16-bit table | 1e | 23 |
| 0x0CF01-0x0CF01 | 1 | v2: exact-context port from GS8.60.2 0x0CEBD | raw data / 16-bit table | 20 | e8 |
| 0x0CF73-0x0CF73 | 1 | v2: exact-context port from GS8.60.2 0x0CF33 | raw data / 16-bit table | 32 | 28 |
| 0x0CF75-0x0CF75 | 1 | v2: exact-context port from GS8.60.2 0x0CF33 | raw data / 16-bit table | 1e | 28 |
| 0x0CF77-0x0CF77 | 1 | v2: exact-context port from GS8.60.2 0x0CF33 | raw data / 16-bit table | 1e | 28 |
| 0x0CF79-0x0CF79 | 1 | v2: exact-context port from GS8.60.2 0x0CF33 | raw data / 16-bit table | 1e | 28 |
| 0x0CF7B-0x0CF7B | 1 | v2: exact-context port from GS8.60.2 0x0CF33 | raw data / 16-bit table | 1e | 28 |
| 0x0CF7D-0x0CF7D | 1 | v2: exact-context port from GS8.60.2 0x0CF33 | raw data / 16-bit table | 1e | 28 |
| 0x0CF7F-0x0CF7F | 1 | v2: exact-context port from GS8.60.2 0x0CF33 | raw data / 16-bit table | 1e | 28 |
| 0x0CF81-0x0CF81 | 1 | v2: exact-context port from GS8.60.2 0x0CF33 | raw data / 16-bit table | 1e | 28 |
| 0x0CF83-0x0CF83 | 1 | v2: exact-context port from GS8.60.2 0x0CF33 | raw data / 16-bit table | 1e | 28 |
| 0x0CF85-0x0CF85 | 1 | v2: exact-context port from GS8.60.2 0x0CF33 | raw data / 16-bit table | 1e | 28 |
| 0x0CF87-0x0CF87 | 1 | v2: exact-context port from GS8.60.2 0x0CF33 | raw data / 16-bit table | 1e | 28 |
| 0x0CF89-0x0CF89 | 1 | v2: exact-context port from GS8.60.2 0x0CF33 | raw data / 16-bit table | 1e | 28 |
| 0x0CF8B-0x0CF8B | 1 | v2: exact-context port from GS8.60.2 0x0CF33 | raw data / 16-bit table | 1e | 28 |
| 0x0CF8D-0x0CF8D | 1 | v2: exact-context port from GS8.60.2 0x0CF33 | raw data / 16-bit table | 1e | 28 |
| 0x0CF8F-0x0CF8F | 1 | v2: exact-context port from GS8.60.2 0x0CF33 | raw data / 16-bit table | 1e | 28 |
| 0x0CF91-0x0CF91 | 1 | v2: exact-context port from GS8.60.2 0x0CF33 | raw data / 16-bit table | 1e | 28 |
| 0x0CF95-0x0CF95 | 1 | v2: exact-context port from GS8.60.2 0x0CF33 | raw data / 16-bit table | 1e | 28 |
| 0x0CF97-0x0CF97 | 1 | v2: exact-context port from GS8.60.2 0x0CF33 | raw data / 16-bit table | 1e | 28 |
| 0x0CF99-0x0CF99 | 1 | v2: exact-context port from GS8.60.2 0x0CF33 | raw data / 16-bit table | 1e | 28 |
| 0x0CF9B-0x0CF9B | 1 | v2: exact-context port from GS8.60.2 0x0CF33 | raw data / 16-bit table | 1e | 28 |
| 0x0CF9D-0x0CF9D | 1 | v2: exact-context port from GS8.60.2 0x0CF33 | raw data / 16-bit table | 1e | 28 |
| 0x0CF9F-0x0CF9F | 1 | v2: exact-context port from GS8.60.2 0x0CF33 | raw data / 16-bit table | 1e | 28 |
| 0x0CFA1-0x0CFA1 | 1 | v2: exact-context port from GS8.60.2 0x0CF33 | raw data / 16-bit table | 1e | 28 |
| 0x0CFA3-0x0CFA3 | 1 | v2: exact-context port from GS8.60.2 0x0CF33 | raw data / 16-bit table | 1e | 28 |
| 0x0CFA5-0x0CFA5 | 1 | v2: exact-context port from GS8.60.2 0x0CF33 | raw data / 16-bit table | 1e | 28 |
| 0x0CFA7-0x0CFA7 | 1 | v2: exact-context port from GS8.60.2 0x0CF33 | raw data / 16-bit table | 1e | 28 |
| 0x0CFA9-0x0CFA9 | 1 | v2: exact-context port from GS8.60.2 0x0CF33 | raw data / 16-bit table | 1e | 28 |
| 0x0CFAB-0x0CFAB | 1 | v2: exact-context port from GS8.60.2 0x0CF33 | raw data / 16-bit table | 1e | 28 |
| 0x0CFAD-0x0CFAD | 1 | v2: exact-context port from GS8.60.2 0x0CF33 | raw data / 16-bit table | 1e | 28 |
| 0x0CFAF-0x0CFAF | 1 | v2: exact-context port from GS8.60.2 0x0CF33 | raw data / 16-bit table | 1e | 28 |
| 0x0CFB1-0x0CFB1 | 1 | v2: exact-context port from GS8.60.2 0x0CF33 | raw data / 16-bit table | 1e | 28 |
| 0x0CFB3-0x0CFB3 | 1 | v2: exact-context port from GS8.60.2 0x0CF33 | raw data / 16-bit table | 1e | 28 |
| 0x0CFB7-0x0CFB7 | 1 | v2: exact-context port from GS8.60.2 0x0CF33 | raw data / 16-bit table | 0c | 0a |
| 0x0CFB9-0x0CFB9 | 1 | v2: exact-context port from GS8.60.2 0x0CF33 | raw data / 16-bit table | 0c | 0a |
| 0x0CFBD-0x0CFBD | 1 | v2: exact-context port from GS8.60.2 0x0CF33 | raw data / 16-bit table | 28 | 0f |
| 0x0CFBF-0x0CFBF | 1 | v2: exact-context port from GS8.60.2 0x0CF33 | raw data / 16-bit table | 1e | 19 |
| 0x0CFC1-0x0CFC1 | 1 | v2: exact-context port from GS8.60.2 0x0CF33 | raw data / 16-bit table | 22 | 19 |
| 0x0CFC3-0x0CFC3 | 1 | v2: exact-context port from GS8.60.2 0x0CF33 | raw data / 16-bit table | 5a | 46 |
| 0x0CFC5-0x0CFC5 | 1 | v2: exact-context port from GS8.60.2 0x0CF33 | raw data / 16-bit table | 0e | 00 |
| 0x0CFC7-0x0CFC7 | 1 | v2: exact-context port from GS8.60.2 0x0CF33 | raw data / 16-bit table | 11 | 00 |
| 0x0CFC9-0x0CFC9 | 1 | v2: exact-context port from GS8.60.2 0x0CF33 | raw data / 16-bit table | 09 | 00 |
| 0x0CFCB-0x0CFCB | 1 | v2: exact-context port from GS8.60.2 0x0CF33 | raw data / 16-bit table | 0a | 02 |
| 0x0CFEB-0x0CFEB | 1 | v2: exact-context port from GS8.60.2 0x0CFAD | raw data / 16-bit table | 06 | 01 |
| 0x0CFED-0x0CFED | 1 | v2: exact-context port from GS8.60.2 0x0CFAD | raw data / 16-bit table | 05 | 01 |
| 0x0CFEF-0x0CFEF | 1 | v2: exact-context port from GS8.60.2 0x0CFAD | raw data / 16-bit table | 03 | 01 |
| 0x0CFF1-0x0CFF1 | 1 | v2: exact-context port from GS8.60.2 0x0CFAD | raw data / 16-bit table | 02 | 01 |
| 0x0CFF3-0x0CFF3 | 1 | v2: exact-context port from GS8.60.2 0x0CFAD | raw data / 16-bit table | 02 | 01 |
| 0x0CFF5-0x0CFF5 | 1 | v2: exact-context port from GS8.60.2 0x0CFAD | raw data / 16-bit table | 03 | 01 |
| 0x0CFF7-0x0CFF7 | 1 | v2: exact-context port from GS8.60.2 0x0CFAD | raw data / 16-bit table | 03 | 01 |
| 0x0CFF9-0x0CFF9 | 1 | v2: exact-context port from GS8.60.2 0x0CFAD | raw data / 16-bit table | 03 | 01 |
| 0x0CFFB-0x0CFFB | 1 | v2: exact-context port from GS8.60.2 0x0CFAD | raw data / 16-bit table | 03 | 01 |
| 0x0CFFD-0x0CFFD | 1 | v2: exact-context port from GS8.60.2 0x0CFAD | raw data / 16-bit table | 03 | 01 |
| 0x0D009-0x0D009 | 1 | v2: exact-context port from GS8.60.2 0x0CFCB | raw data / 16-bit table | 02 | 01 |
| 0x0D00B-0x0D00B | 1 | v2: exact-context port from GS8.60.2 0x0CFCB | raw data / 16-bit table | 02 | 01 |
| 0x0D00D-0x0D00D | 1 | v2: exact-context port from GS8.60.2 0x0CFCB | raw data / 16-bit table | 02 | 01 |
| 0x0D00F-0x0D00F | 1 | v2: exact-context port from GS8.60.2 0x0CFCB | raw data / 16-bit table | 02 | 01 |
| 0x0D011-0x0D013 | 3 | v2: exact-context port from GS8.60.2 0x0CFCB | raw data / 16-bit table | 02 ff fe | 01 00 00 |
| 0x0D015-0x0D015 | 1 | v2: exact-context port from GS8.60.2 0x0CFCB | raw data / 16-bit table | fc | fe |
| 0x0D017-0x0D017 | 1 | v2: exact-context port from GS8.60.2 0x0CFCB | raw data / 16-bit table | fa | fe |
| 0x0D019-0x0D019 | 1 | v2: exact-context port from GS8.60.2 0x0CFCB | raw data / 16-bit table | fa | fc |
| 0x0D01B-0x0D01F | 5 | v2: exact-context port from GS8.60.2 0x0CFCB | raw data / 16-bit table | fa ff fc ff fa | fc 00 00 00 00 |
| 0x0D021-0x0D021 | 1 | v2: exact-context port from GS8.60.2 0x0CFCB | raw data / 16-bit table | f8 | fe |
| 0x0D023-0x0D023 | 1 | v2: exact-context port from GS8.60.2 0x0CFCB | raw data / 16-bit table | f6 | fc |
| 0x0D025-0x0D027 | 3 | v2: exact-context port from GS8.60.2 0x0CFCB | raw data / 16-bit table | f4 ff ff | fa 00 00 |
| 0x0D02B-0x0D02B | 1 | v2: exact-context port from GS8.60.2 0x0CFCB | raw data / 16-bit table | fd | fe |
| 0x0D02F-0x0D02F | 1 | v2: exact-context port from GS8.60.2 0x0CFCB | raw data / 16-bit table | fa | fc |
| 0x0D031-0x0D03D | 13 | v2: exact-context port from GS8.60.2 0x0CFCB | raw data / 16-bit table | 00 ff fe ff fe ff fc ff fc ff fc ff fa | 01 00 00 00 00 00 00 00 00 00 00 00 00 |
| 0x0D03F-0x0D03F | 1 | v2: exact-context port from GS8.60.2 0x0CFCB | raw data / 16-bit table | f8 | fc |
| 0x0D041-0x0D041 | 1 | v2: exact-context port from GS8.60.2 0x0CFCB | raw data / 16-bit table | f6 | fa |
| 0x0D043-0x0D047 | 5 | v2: exact-context port from GS8.60.2 0x0CFCB | raw data / 16-bit table | f4 ff fe ff fc | f8 00 00 00 00 |
| 0x0D049-0x0D049 | 1 | v2: exact-context port from GS8.60.2 0x0CFCB | raw data / 16-bit table | fa | fe |
| 0x0D04B-0x0D04B | 1 | v2: exact-context port from GS8.60.2 0x0CFCB | raw data / 16-bit table | f8 | fc |
| 0x0D04D-0x0D04D | 1 | v2: exact-context port from GS8.60.2 0x0CFCB | raw data / 16-bit table | f6 | fa |
| 0x0D051-0x0D051 | 1 | v2: exact-context port from GS8.60.2 0x0CFCB | raw data / 16-bit table | fa | fc |
| 0x0D053-0x0D053 | 1 | v2: exact-context port from GS8.60.2 0x0CFCB | raw data / 16-bit table | f8 | fa |
| 0x0D055-0x0D055 | 1 | v2: exact-context port from GS8.60.2 0x0CFCB | raw data / 16-bit table | f6 | f8 |
| 0x0D057-0x0D057 | 1 | v2: exact-context port from GS8.60.2 0x0CFCB | raw data / 16-bit table | f2 | f6 |
| 0x0D05A-0x0D05D | 4 | v2: exact-context port from GS8.60.2 0x0CFCB | raw data / 16-bit table | 00 00 00 00 | ff fe ff fe |
| 0x0D05F-0x0D05F | 1 | v2: exact-context port from GS8.60.2 0x0CFCB | raw data / 16-bit table | ff | fe |
| 0x0D061-0x0D061 | 1 | v2: exact-context port from GS8.60.2 0x0CFCB | raw data / 16-bit table | ff | fe |
| 0x0D063-0x0D063 | 1 | v2: exact-context port from GS8.60.2 0x0CFCB | raw data / 16-bit table | ff | fe |
| 0x0D065-0x0D065 | 1 | v2: exact-context port from GS8.60.2 0x0CFCB | raw data / 16-bit table | fa | fe |
| 0x0D067-0x0D067 | 1 | v2: exact-context port from GS8.60.2 0x0CFCB | raw data / 16-bit table | fa | fe |
| 0x0D069-0x0D069 | 1 | v2: exact-context port from GS8.60.2 0x0CFCB | raw data / 16-bit table | fa | fe |
| 0x0D06B-0x0D06B | 1 | v2: exact-context port from GS8.60.2 0x0CFCB | raw data / 16-bit table | fa | fe |
| 0x0D06D-0x0D06D | 1 | v2: exact-context port from GS8.60.2 0x0CFCB | raw data / 16-bit table | fa | fe |
| 0x0D079-0x0D079 | 1 | v2: exact-context port from GS8.60.2 0x0D03B | raw data / 16-bit table | ff | fe |
| 0x0D07B-0x0D07B | 1 | v2: exact-context port from GS8.60.2 0x0D03B | raw data / 16-bit table | ff | fe |
| 0x0D07D-0x0D07D | 1 | v2: exact-context port from GS8.60.2 0x0D03B | raw data / 16-bit table | ff | fe |
| 0x0D07F-0x0D07F | 1 | v2: exact-context port from GS8.60.2 0x0D03B | raw data / 16-bit table | ff | fe |
| 0x0D081-0x0D081 | 1 | v2: exact-context port from GS8.60.2 0x0D03B | raw data / 16-bit table | ff | fe |
| 0x0D083-0x0D083 | 1 | v2: exact-context port from GS8.60.2 0x0D03B | raw data / 16-bit table | fa | fe |
| 0x0D085-0x0D085 | 1 | v2: exact-context port from GS8.60.2 0x0D03B | raw data / 16-bit table | f8 | fc |
| 0x0D087-0x0D087 | 1 | v2: exact-context port from GS8.60.2 0x0D03B | raw data / 16-bit table | f6 | fc |
| 0x0D089-0x0D089 | 1 | v2: exact-context port from GS8.60.2 0x0D03B | raw data / 16-bit table | f6 | fa |
| 0x0D08B-0x0D08B | 1 | v2: exact-context port from GS8.60.2 0x0D03B | raw data / 16-bit table | f6 | fa |
| 0x0D08D-0x0D08D | 1 | v2: exact-context port from GS8.60.2 0x0D03B | raw data / 16-bit table | f8 | fe |
| 0x0D08F-0x0D08F | 1 | v2: exact-context port from GS8.60.2 0x0D03B | raw data / 16-bit table | f6 | fe |
| 0x0D091-0x0D091 | 1 | v2: exact-context port from GS8.60.2 0x0D03B | raw data / 16-bit table | f4 | fc |
| 0x0D093-0x0D093 | 1 | v2: exact-context port from GS8.60.2 0x0D03B | raw data / 16-bit table | f2 | fa |
| 0x0D095-0x0D095 | 1 | v2: exact-context port from GS8.60.2 0x0D03B | raw data / 16-bit table | f0 | f8 |
| 0x0D097-0x0D097 | 1 | v2: exact-context port from GS8.60.2 0x0D03B | raw data / 16-bit table | fb | fe |
| 0x0D099-0x0D099 | 1 | v2: exact-context port from GS8.60.2 0x0D03B | raw data / 16-bit table | fa | fc |
| 0x0D09B-0x0D09B | 1 | v2: exact-context port from GS8.60.2 0x0D03B | raw data / 16-bit table | f9 | fc |
| 0x0D09D-0x0D09D | 1 | v2: exact-context port from GS8.60.2 0x0D03B | raw data / 16-bit table | f8 | fa |
| 0x0D09F-0x0D09F | 1 | v2: exact-context port from GS8.60.2 0x0D03B | raw data / 16-bit table | f6 | fa |
| 0x0D0A1-0x0D0A1 | 1 | v2: exact-context port from GS8.60.2 0x0D03B | raw data / 16-bit table | fc | ff |
| 0x0D0A3-0x0D0A3 | 1 | v2: exact-context port from GS8.60.2 0x0D03B | raw data / 16-bit table | fa | fe |
| 0x0D0A5-0x0D0A5 | 1 | v2: exact-context port from GS8.60.2 0x0D03B | raw data / 16-bit table | f9 | fe |
| 0x0D0A7-0x0D0A7 | 1 | v2: exact-context port from GS8.60.2 0x0D03B | raw data / 16-bit table | f8 | fe |
| 0x0D0A9-0x0D0A9 | 1 | v2: exact-context port from GS8.60.2 0x0D03B | raw data / 16-bit table | f8 | fe |
| 0x0D0AB-0x0D0AB | 1 | v2: exact-context port from GS8.60.2 0x0D03B | raw data / 16-bit table | f8 | fe |
| 0x0D0AD-0x0D0AD | 1 | v2: exact-context port from GS8.60.2 0x0D03B | raw data / 16-bit table | f6 | fe |
| 0x0D0AF-0x0D0AF | 1 | v2: exact-context port from GS8.60.2 0x0D03B | raw data / 16-bit table | f4 | fa |
| 0x0D0B1-0x0D0B1 | 1 | v2: exact-context port from GS8.60.2 0x0D03B | raw data / 16-bit table | f2 | f8 |
| 0x0D0B3-0x0D0B3 | 1 | v2: exact-context port from GS8.60.2 0x0D03B | raw data / 16-bit table | f0 | f6 |
| 0x0D0B5-0x0D0B5 | 1 | v2: exact-context port from GS8.60.2 0x0D03B | raw data / 16-bit table | fa | fe |
| 0x0D0B7-0x0D0B7 | 1 | v2: exact-context port from GS8.60.2 0x0D03B | raw data / 16-bit table | f8 | fe |
| 0x0D0B9-0x0D0B9 | 1 | v2: exact-context port from GS8.60.2 0x0D03B | raw data / 16-bit table | f6 | fc |
| 0x0D0BB-0x0D0BB | 1 | v2: exact-context port from GS8.60.2 0x0D03B | raw data / 16-bit table | f4 | fa |
| 0x0D0BD-0x0D0BD | 1 | v2: exact-context port from GS8.60.2 0x0D03B | raw data / 16-bit table | f2 | f8 |
| 0x0D0BF-0x0D0BF | 1 | v2: exact-context port from GS8.60.2 0x0D03B | raw data / 16-bit table | f8 | fa |
| 0x0D0C1-0x0D0C1 | 1 | v2: exact-context port from GS8.60.2 0x0D03B | raw data / 16-bit table | f6 | fa |
| 0x0D0C3-0x0D0C3 | 1 | v2: exact-context port from GS8.60.2 0x0D03B | raw data / 16-bit table | f4 | f8 |
| 0x0D0C5-0x0D0C5 | 1 | v2: exact-context port from GS8.60.2 0x0D03B | raw data / 16-bit table | f2 | f6 |
| 0x0D0C7-0x0D0C7 | 1 | v2: exact-context port from GS8.60.2 0x0D03B | raw data / 16-bit table | ee | f4 |
| 0x0DB3C-0x0DB3F | 4 | v2: exact-context port from GS8.60.2 0x0DC7C | raw data / 16-bit table | 09 60 07 d0 | 05 dc 05 78 |
| 0x0DB42-0x0DB42 | 1 | v2: exact-context port from GS8.60.2 0x0DC7C | raw data / 16-bit table | 07 | 03 |
| 0x0DB44-0x0DB4A | 7 | v2: exact-context port from GS8.60.2 0x0DC7C | raw data / 16-bit table | 0b c0 0f a0 13 80 17 | 07 e0 0b c0 0f a0 13 |
| 0x0DB4C-0x0DB55 | 10 | v2: exact-context port from GS8.60.2 0x0DC7C | raw data / 16-bit table | 03 e8 04 4c 04 b0 05 14 05 78 | 02 58 03 84 03 e8 04 1a 04 1a |
| 0x0DB58-0x0DB58 | 1 | v2: exact-context port from GS8.60.2 0x0DC7C | raw data / 16-bit table | 07 | 03 |
| 0x0DB5A-0x0DB60 | 7 | v2: exact-context port from GS8.60.2 0x0DC7C | raw data / 16-bit table | 0b c0 0f a0 13 80 17 | 07 e0 0b c0 0f a0 13 |
| 0x0DB62-0x0DB69 | 8 | v2: exact-context port from GS8.60.2 0x0DC7C | raw data / 16-bit table | 02 58 02 bc 03 20 03 84 | 01 90 01 f4 02 58 02 bc |
| 0x0DB6B-0x0DB6B | 1 | v2: exact-context port from GS8.60.2 0x0DC7C | raw data / 16-bit table | e8 | 20 |
| 0x0DB6E-0x0DB6F | 2 | v2: exact-context port from GS8.60.2 0x0DC7C | curve 3x1 @0x0DB6C (axis/header) | 19 28 | 00 50 |
| 0x0DB71-0x0DB71 | 1 | v2: exact-context port from GS8.60.2 0x0DC7C | curve 3x1 @0x0DB6C (values) | 3c | 32 |
| 0x0DB7E-0x0DB80 | 3 | v2: exact-context port from GS8.60.2 0x0DCBE | curve 3x1 @0x0DB7C (axis/header) | 14 41 50 | 0a 14 1e |
| 0x0DB83-0x0DB83 | 1 | v2: exact-context port from GS8.60.2 0x0DCBE | curve 3x1 @0x0DB7C (values) | ff | 00 |
| 0x0DB86-0x0DB88 | 3 | v2: exact-context port from GS8.60.2 0x0DCBE | curve 3x1 @0x0DB84 (axis/header) | 14 41 50 | 0a 14 1e |
| 0x0DB8B-0x0DB8B | 1 | v2: exact-context port from GS8.60.2 0x0DCBE | curve 3x1 @0x0DB84 (values) | ff | 00 |
| 0x0DBAF-0x0DBB0 | 2 | v2: exact-context port from GS8.60.2 0x0DCEF | curve 3x1 @0x0DBAC (axis/header) | 28 37 | 37 46 |
| 0x0DBB2-0x0DBB3 | 2 | v2: exact-context port from GS8.60.2 0x0DCEF | curve 3x1 @0x0DBAC (values) | 26 66 | 00 00 |
| 0x0DBC7-0x0DBC8 | 2 | v2: exact-context port from GS8.60.2 0x0DD07 | curve 3x1 @0x0DBC4 (axis/header) | 3c 64 | 19 32 |
| 0x0DBCB-0x0DBCB | 1 | v2: exact-context port from GS8.60.2 0x0DD07 | curve 3x1 @0x0DBC4 (values) | 66 | 00 |
| 0x0DBCF-0x0DBCF | 1 | v2: exact-context port from GS8.60.2 0x0DD07 | curve 3x1 @0x0DBCC (axis/header) | 05 | 14 |
| 0x0DBDF-0x0DBDF | 1 | v2: exact-context port from GS8.60.2 0x0DD1F | curve 2x1 @0x0DBDC (axis/header) | 0a | 08 |
| 0x0DBE5-0x0DBE5 | 1 | v2: exact-context port from GS8.60.2 0x0DD25 | curve 2x1 @0x0DBE2 (axis/header) | 0a | 08 |
| 0x0DBEB-0x0DBEB | 1 | v2: exact-context port from GS8.60.2 0x0DD2B | curve 2x1 @0x0DBE8 (axis/header) | 12 | 16 |
| 0x0DBF1-0x0DBF1 | 1 | v2: exact-context port from GS8.60.2 0x0DD31 | curve 2x1 @0x0DBEE (axis/header) | 07 | 08 |
| 0x0DC09-0x0DC09 | 1 | v2: exact-context port from GS8.60.2 0x0DD49 | curve 2x1 @0x0DC06 (axis/header) | 18 | 19 |
| 0x0DC0F-0x0DC0F | 1 | v2: exact-context port from GS8.60.2 0x0DD4F | curve 2x1 @0x0DC0C (axis/header) | 0f | 0e |
| 0x0DC2C-0x0DC30 | 5 | v2: exact-context port from GS8.60.2 0x0DD6C | curve 6x1 @0x0DC24 (values) | 66 69 6f 7b 99 | 80 80 80 80 80 |
| 0x0DC3A-0x0DC3E | 5 | v2: exact-context port from GS8.60.2 0x0DD7A | curve 6x1 @0x0DC32 (values) | 66 69 6f 7b 99 | 80 80 80 80 80 |
| 0x0DCC7-0x0DCCA | 4 | v2: exact-context port from GS8.60.2 0x0DE07 | curve 6x1 @0x0DCBE (values) | 8c 99 bf d9 | 80 80 88 99 |
| 0x0DCE9-0x0DCE9 | 1 | v2: exact-context port from GS8.60.2 0x0DE29 | raw data / 16-bit table | 32 | 14 |
| 0x0DCEB-0x0DCEB | 1 | v2: exact-context port from GS8.60.2 0x0DE29 | raw data / 16-bit table | 32 | 14 |
| 0x0DCED-0x0DCED | 1 | v2: exact-context port from GS8.60.2 0x0DE29 | raw data / 16-bit table | 32 | 14 |
| 0x0DCEF-0x0DCEF | 1 | v2: exact-context port from GS8.60.2 0x0DE29 | raw data / 16-bit table | 32 | 14 |
| 0x0DCF1-0x0DCF1 | 1 | v2: exact-context port from GS8.60.2 0x0DE29 | raw data / 16-bit table | 32 | 28 |
| 0x0DCF3-0x0DCF3 | 1 | v2: exact-context port from GS8.60.2 0x0DE29 | raw data / 16-bit table | 32 | 50 |
| 0x0DD37-0x0DD37 | 1 | v2: exact-context port from GS8.60.2 0x0DE77 | raw data / 16-bit table | 82 | 64 |
| 0x0DD39-0x0DD39 | 1 | v2: exact-context port from GS8.60.2 0x0DE77 | raw data / 16-bit table | 82 | 78 |
| 0x0DD3B-0x0DD3B | 1 | v2: exact-context port from GS8.60.2 0x0DE77 | raw data / 16-bit table | 82 | c8 |
| 0x0DD3D-0x0DD41 | 5 | v2: exact-context port from GS8.60.2 0x0DE77 | raw data / 16-bit table | 82 00 82 00 82 | f0 01 18 01 2c |
| 0x0DE14-0x0DE1F | 12 | v2: exact-context port from GS8.60.2 0x0DF9A | raw data / 16-bit table | 05 dc 07 d0 09 c4 0b b8 0d ac 0f a0 | 03 e0 05 e0 07 e0 09 c0 0b c0 0d c0 |
| 0x0DE21-0x0DE21 | 1 | v2: exact-context port from GS8.60.2 0x0DF9A | raw data / 16-bit table | 50 | 1e |
| 0x0DE23-0x0DE23 | 1 | v2: exact-context port from GS8.60.2 0x0DF9A | raw data / 16-bit table | 40 | 1e |
| 0x0DE25-0x0DE25 | 1 | v2: exact-context port from GS8.60.2 0x0DF9A | raw data / 16-bit table | 40 | 28 |
| 0x0DE27-0x0DE27 | 1 | v2: exact-context port from GS8.60.2 0x0DF9A | raw data / 16-bit table | 40 | 32 |
| 0x0DE29-0x0DE29 | 1 | v2: exact-context port from GS8.60.2 0x0DF9A | raw data / 16-bit table | 40 | 46 |
| 0x0DE2B-0x0DE2B | 1 | v2: exact-context port from GS8.60.2 0x0DF9A | raw data / 16-bit table | 40 | 5a |
| 0x0DEA5-0x0DEA5 | 1 | v2: exact-context port from GS8.60.2 0x0E02B | raw data / 16-bit table | 7d | 8c |
| 0x0DEA7-0x0DEAB | 5 | v2: exact-context port from GS8.60.2 0x0E02B | raw data / 16-bit table | b4 00 dc 00 f0 | dc 01 2c 01 7c |
| 0x0DEAD-0x0DEAD | 1 | v2: exact-context port from GS8.60.2 0x0E02B | raw data / 16-bit table | 0e | cc |
| 0x0DEBD-0x0DEBD | 1 | v2: exact-context port from GS8.60.2 0x0E043 | raw data / 16-bit table | 64 | b4 |
| 0x0DEBF-0x0DEBF | 1 | v2: exact-context port from GS8.60.2 0x0E043 | raw data / 16-bit table | 78 | c8 |
| 0x0DEC1-0x0DEC7 | 7 | v2: exact-context port from GS8.60.2 0x0E043 | raw data / 16-bit table | 8c 00 aa 00 c8 00 dc | e6 01 18 01 4a 01 7c |
| 0x0DF22-0x0DF23 | 2 | v2: exact-context port from GS8.60.2 0x0E0A8 | raw data / 16-bit table | 0d ac | 0b c0 |
| 0x0DF25-0x0DF25 | 1 | v2: exact-context port from GS8.60.2 0x0E0A8 | raw data / 16-bit table | 8c | 64 |
| 0x0DF27-0x0DF29 | 3 | v2: exact-context port from GS8.60.2 0x0E0A8 | raw data / 16-bit table | aa 00 dc | c8 01 40 |
| 0x0DF2B-0x0DF2F | 5 | v2: exact-context port from GS8.60.2 0x0E0A8 | raw data / 16-bit table | 22 01 40 01 c2 | cc 02 4e 02 e4 |
| 0x0DF84-0x0DF87 | 4 | v2: exact-context port from GS8.60.2 0x0E10A | curve 4x1 @0x0DF7E (values) | 32 28 28 28 | 3c 36 32 32 |
| 0x0DF8B-0x0DF8E | 4 | v2: exact-context port from GS8.60.2 0x0E10A | curve 3x1 @0x0DF88 (axis/header) | 05 0a 18 18 | 0a 0f 16 17 |
| 0x0DF9D-0x0DF9F | 3 | v2: close-curve delta (Alpina change on GS8.55 values) | curve 3x1 @0x0DF98 (values) | 1e 20 20 | 1d 1f 1f |
| 0x0DFAD-0x0DFAF | 3 | v2: close-curve delta (Alpina change on GS8.55 values) | curve 3x1 @0x0DFA8 (values) | 1e 20 20 | 1d 1f 1f |
| 0x0DFD5-0x0DFD7 | 3 | v2: close-curve delta (Alpina change on GS8.55 values) | curve 3x1 @0x0DFD0 (values) | 17 17 18 | 18 19 1c |
| 0x0DFDD-0x0DFDF | 3 | v2: close-curve delta (Alpina change on GS8.55 values) | curve 3x1 @0x0DFD8 (values) | 19 24 50 | 1b 20 3a |
| 0x0DFE5-0x0DFE7 | 3 | v2: close-curve delta (Alpina change on GS8.55 values) | curve 3x1 @0x0DFE0 (values) | 25 26 27 | 16 17 19 |
| 0x0DFFD-0x0DFFF | 3 | v2: close-curve delta (Alpina change on GS8.55 values) | curve 3x1 @0x0DFF8 (values) | 13 13 14 | 17 17 17 |
| 0x0E006-0x0E007 | 2 | v2: close-curve delta (Alpina change on GS8.55 values) | curve 3x1 @0x0E000 (values) | 17 18 | 18 1a |
| 0x0E015-0x0E015 | 1 | v2: exact-context port from GS8.60.2 0x0E19B | curve 3x1 @0x0E010 (values) | 15 | 16 |
| 0x0E025-0x0E027 | 3 | v2: close-curve delta (Alpina change on GS8.55 values) | curve 3x1 @0x0E020 (values) | 32 32 32 | 28 29 2a |
| 0x0E02D-0x0E02F | 3 | v2: close-curve delta (Alpina change on GS8.55 values) | curve 3x1 @0x0E028 (values) | 0c 0c 0c | 0e 0e 0e |
| 0x0E041-0x0E041 | 1 | v2: exact-context port from GS8.60.2 0x0E1C7 | curve 2x1 @0x0E03E (axis/header) | 08 | 0c |
| 0x0E043-0x0E043 | 1 | v2: exact-context port from GS8.60.2 0x0E1C7 | curve 2x1 @0x0E03E (values) | 64 | 3c |
| 0x0E048-0x0E049 | 2 | v2: exact-context port from GS8.60.2 0x0E1CE | curve 2x1 @0x0E044 (values) | 78 50 | 6e 5a |
| 0x0E060-0x0E061 | 2 | v2: exact-context port from GS8.60.2 0x0E1E6 | curve 2x1 @0x0E05C (values) | 2c 28 | 40 2c |
| 0x0E0CA-0x0E0CB | 2 | v2: close-curve delta (Alpina change on GS8.55 values) | curve 7x1 @0x0E0BC (values) | 0a 0a | 08 08 |
| 0x0E0D9-0x0E0DB | 3 | v2: exact-context port from GS8.60.2 0x0E25F | curve 7x1 @0x0E0CC (values) | 12 12 12 | 10 10 10 |
| 0x0E0E5-0x0E0E5 | 1 | v2: exact-context port from GS8.60.2 0x0E26B | curve 7x1 @0x0E0DC (values) | 8e | 88 |
| 0x0E0E7-0x0E0E8 | 2 | v2: exact-context port from GS8.60.2 0x0E26B | curve 7x1 @0x0E0DC (values) | 82 81 | 86 82 |
| 0x0E0F5-0x0E0F5 | 1 | v2: exact-context port from GS8.60.2 0x0E27B | curve 7x1 @0x0E0EC (values) | 8e | 88 |
| 0x0E0F7-0x0E0F8 | 2 | v2: exact-context port from GS8.60.2 0x0E27B | curve 7x1 @0x0E0EC (values) | 82 81 | 86 82 |
| 0x0E105-0x0E108 | 4 | v2: exact-context port from GS8.60.2 0x0E28B | curve 7x1 @0x0E0FC (values) | 8a 84 83 80 | 88 88 86 82 |
| 0x0E115-0x0E115 | 1 | v2: close-curve delta (Alpina change on GS8.55 values) | curve 7x1 @0x0E10C (values) | 8a | 86 |
| 0x0E117-0x0E11B | 5 | v2: close-curve delta (Alpina change on GS8.55 values) | curve 7x1 @0x0E10C (values) | 84 84 86 8e 90 | 86 89 8a 8a 8a |
| 0x0E145-0x0E147 | 3 | v2: exact-context port from GS8.60.2 0x0E2CB | curve 7x1 @0x0E13C (values) | 90 84 80 | 78 78 7a |
| 0x0E149-0x0E149 | 1 | v2: exact-context port from GS8.60.2 0x0E2CB | curve 7x1 @0x0E13C (values) | 7d | 7e |
| 0x0E155-0x0E157 | 3 | v2: exact-context port from GS8.60.2 0x0E2DB | curve 7x1 @0x0E14C (values) | 90 84 80 | 78 78 7a |
| 0x0E159-0x0E159 | 1 | v2: exact-context port from GS8.60.2 0x0E2DB | curve 7x1 @0x0E14C (values) | 7d | 7e |
| 0x0E167-0x0E168 | 2 | v2: exact-context port from GS8.60.2 0x0E2ED | curve 7x1 @0x0E15C (values) | 85 82 | 88 86 |
| 0x0E17B-0x0E17B | 1 | v2: exact-context port from GS8.60.2 0x0E301 | curve 7x1 @0x0E16C (values) | 80 | 82 |
| 0x0E185-0x0E187 | 3 | v2: close-curve delta (Alpina change on GS8.55 values) | curve 7x1 @0x0E17C (values) | 8e 82 80 | 90 86 81 |
| 0x0E189-0x0E189 | 1 | v2: close-curve delta (Alpina change on GS8.55 values) | curve 7x1 @0x0E17C (values) | 80 | 7e |
| 0x0E18B-0x0E18B | 1 | v2: close-curve delta (Alpina change on GS8.55 values) | curve 7x1 @0x0E17C (values) | 80 | 82 |
| 0x0E1A2-0x0E1A3 | 2 | v2: exact-context port from GS8.60.2 0x0E328 | curve 7x1 @0x0E19C (axis/header) | 64 78 | 50 82 |
| 0x0E1A6-0x0E1A7 | 2 | v2: exact-context port from GS8.60.2 0x0E328 | curve 7x1 @0x0E19C (values) | 90 84 | 8c 81 |
| 0x0E1B5-0x0E1B9 | 5 | v2: exact-context port from GS8.60.2 0x0E33B | curve 7x1 @0x0E1AC (values) | 68 74 7c 80 80 | 64 70 75 78 7d |
| 0x0E1BB-0x0E1BB | 1 | v2: exact-context port from GS8.60.2 0x0E33B | curve 7x1 @0x0E1AC (values) | 80 | 82 |
| 0x0E1C5-0x0E1C6 | 2 | v2: close-curve delta (Alpina change on GS8.55 values) | curve 7x1 @0x0E1BC (values) | a6 9a | b2 a0 |
| 0x0E1C8-0x0E1C9 | 2 | v2: close-curve delta (Alpina change on GS8.55 values) | curve 7x1 @0x0E1BC (values) | 88 82 | 83 7c |
| 0x0E1CB-0x0E1CB | 1 | v2: close-curve delta (Alpina change on GS8.55 values) | curve 7x1 @0x0E1BC (values) | 80 | 82 |
| 0x0E1E8-0x0E1E9 | 2 | v2: exact-context port from GS8.60.2 0x0E36E | curve 7x1 @0x0E1DC (values) | 7c 80 | 78 7c |
| 0x0E1EB-0x0E1EB | 1 | v2: exact-context port from GS8.60.2 0x0E36E | curve 7x1 @0x0E1DC (values) | 80 | 84 |
| 0x0E1F5-0x0E1F9 | 5 | v2: exact-context port from GS8.60.2 0x0E37B | curve 7x1 @0x0E1EC (values) | 92 8a 86 84 82 | 90 8c 84 80 80 |
| 0x0E205-0x0E205 | 1 | v2: exact-context port from GS8.60.2 0x0E38B | curve 7x1 @0x0E1FC (values) | 60 | 58 |
| 0x0E208-0x0E209 | 2 | v2: exact-context port from GS8.60.2 0x0E38B | curve 7x1 @0x0E1FC (values) | 7c 80 | 79 7c |
| 0x0E215-0x0E217 | 3 | v2: exact-context port from GS8.60.2 0x0E39B | curve 7x1 @0x0E20C (values) | a4 98 90 | a8 9a 92 |
| 0x0E219-0x0E219 | 1 | v2: exact-context port from GS8.60.2 0x0E39B | curve 7x1 @0x0E20C (values) | 82 | 80 |
| 0x0E235-0x0E236 | 2 | v2: close-curve delta (Alpina change on GS8.55 values) | curve 7x1 @0x0E22C (values) | 6b 70 | 55 66 |
| 0x0E238-0x0E239 | 2 | v2: close-curve delta (Alpina change on GS8.55 values) | curve 7x1 @0x0E22C (values) | 7e 80 | 80 82 |
| 0x0E23B-0x0E23B | 1 | v2: close-curve delta (Alpina change on GS8.55 values) | curve 7x1 @0x0E22C (values) | 80 | 7e |
| 0x0E246-0x0E247 | 2 | v2: exact-context port from GS8.60.2 0x0E3CC | curve 7x1 @0x0E23C (values) | 89 84 | 8a 86 |
| 0x0E255-0x0E255 | 1 | v2: exact-context port from GS8.60.2 0x0E3DB | curve 7x1 @0x0E24C (values) | 6c | 6a |
| 0x0E275-0x0E279 | 5 | v2: exact-context port from GS8.60.2 0x0E3FB | curve 7x1 @0x0E26C (values) | 70 74 78 7a 7f | 72 77 7b 7c 7d |
| 0x0E286-0x0E286 | 1 | v2: exact-context port from GS8.60.2 0x0E40C | curve 7x1 @0x0E27C (values) | 72 | 74 |
| 0x0E288-0x0E288 | 1 | v2: exact-context port from GS8.60.2 0x0E40C | curve 7x1 @0x0E27C (values) | 7c | 7a |
| 0x0E28B-0x0E28B | 1 | v2: exact-context port from GS8.60.2 0x0E40C | curve 7x1 @0x0E27C (values) | 82 | 80 |
| 0x0E2B6-0x0E2B8 | 3 | v2: close-curve delta (Alpina change on GS8.55 values) | curve 7x1 @0x0E2AC (values) | 84 80 7c | 8e 84 7e |
| 0x0E2D6-0x0E2D8 | 3 | v2: close-curve delta (Alpina change on GS8.55 values) | curve 7x1 @0x0E2CC (values) | 84 80 7c | 8e 84 7e |
| 0x0E2E4-0x0E2E4 | 1 | v2: exact-context port from GS8.60.2 0x0E46A | curve 7x1 @0x0E2DC (axis/header) | aa | 96 |
| 0x0E2F5-0x0E2F6 | 2 | v2: exact-context port from GS8.60.2 0x0E47B | curve 7x1 @0x0E2EC (values) | 86 81 | 84 82 |
| 0x0E306-0x0E309 | 4 | v2: exact-context port from GS8.60.2 0x0E48C | curve 7x1 @0x0E2FC (values) | 86 81 7d 80 | 88 84 83 82 |
| 0x0E315-0x0E318 | 4 | v2: exact-context port from GS8.60.2 0x0E49B | curve 7x1 @0x0E30C (values) | 8d 85 81 81 | 90 88 84 82 |
| 0x0E336-0x0E338 | 3 | v2: exact-context port from GS8.60.2 0x0E4BC | curve 7x1 @0x0E32C (values) | 8a 88 86 | 86 83 82 |
| 0x0E345-0x0E349 | 5 | v2: close-curve delta (Alpina change on GS8.55 values) | curve 7x1 @0x0E33C (values) | 98 92 86 82 80 | a4 98 8e 86 84 |
| 0x0E34B-0x0E34B | 1 | v2: close-curve delta (Alpina change on GS8.55 values) | curve 7x1 @0x0E33C (values) | 80 | 84 |
| 0x0E36B-0x0E36B | 1 | v2: exact-context port from GS8.60.2 0x0E4F1 | curve 7x1 @0x0E35C (values) | 80 | 82 |
| 0x0E376-0x0E378 | 3 | v2: exact-context port from GS8.60.2 0x0E4FC | curve 7x1 @0x0E36C (values) | 8c 86 84 | 90 84 81 |
| 0x0E395-0x0E397 | 3 | v2: exact-context port from GS8.60.2 0x0E51B | curve 7x1 @0x0E38C (values) | 88 86 84 | 90 8c 86 |
| 0x0E3D5-0x0E3D7 | 3 | v2: exact-context port from GS8.60.2 0x0E55B | curve 7x1 @0x0E3CC (values) | 80 80 80 | 78 78 7d |
| 0x0E4A3-0x0E4A3 | 1 | v2: exact-context port from GS8.60.2 0x0E699 | curve 3x1 @0x0E49C (values) | 9f | 9e |
| 0x0E4BA-0x0E4BB | 2 | v2: close-curve delta (Alpina change on GS8.55 values) | curve 3x1 @0x0E4B4 (values) | 80 7e | 82 80 |
| 0x0E4D2-0x0E4D3 | 2 | v2: close-curve delta (Alpina change on GS8.55 values) | curve 3x1 @0x0E4CC (values) | 7c 79 | 86 85 |
| 0x0E4E0-0x0E4E0 | 1 | v2: exact-context port from GS8.60.2 0x0E6D6 | curve 3x1 @0x0E4DC (axis/header) | 28 | 1e |
| 0x0E4E3-0x0E4E3 | 1 | v2: exact-context port from GS8.60.2 0x0E6D6 | curve 3x1 @0x0E4DC (values) | 7a | 80 |
| 0x0E4EB-0x0E4EB | 1 | v2: exact-context port from GS8.60.2 0x0E6E1 | curve 3x1 @0x0E4E4 (values) | fa | ff |
| 0x0E4EF-0x0E4F0 | 2 | v2: exact-context port from GS8.60.2 0x0E6E1 | curve 3x1 @0x0E4EC (axis/header) | 05 0a | 0a 0f |
| 0x0E4FA-0x0E4FA | 1 | v2: close-curve delta (Alpina change on GS8.55 values) | curve 3x1 @0x0E4F4 (values) | 14 | 20 |
| 0x0E50A-0x0E50A | 1 | v2: close-curve delta (Alpina change on GS8.55 values) | curve 3x1 @0x0E504 (values) | 14 | 20 |
| 0x0E543-0x0E543 | 1 | v2: exact-context port from GS8.60.2 0x0E739 | curve 3x1 @0x0E53C (values) | fa | ff |
| 0x0E547-0x0E548 | 2 | v2: exact-context port from GS8.60.2 0x0E739 | curve 3x1 @0x0E544 (axis/header) | 0a 0f | 0f 19 |
| 0x0E54A-0x0E54B | 2 | v2: exact-context port from GS8.60.2 0x0E739 | curve 3x1 @0x0E544 (values) | 1e fa | 04 ff |
| 0x0E54F-0x0E550 | 2 | v2: exact-context port from GS8.60.2 0x0E739 | curve 3x1 @0x0E54C (axis/header) | 05 0a | 0a 0f |
| 0x0E562-0x0E563 | 2 | v2: exact-context port from GS8.60.2 0x0E758 | curve 3x1 @0x0E55C (values) | 1e fa | 0a ff |
| 0x0E567-0x0E568 | 2 | v2: exact-context port from GS8.60.2 0x0E758 | curve 3x1 @0x0E564 (axis/header) | 0f 14 | 0a 0f |
| 0x0E56A-0x0E56A | 1 | v2: exact-context port from GS8.60.2 0x0E758 | curve 3x1 @0x0E564 (values) | 02 | 14 |
| 0x0E575-0x0E579 | 5 | v2: exact-context port from GS8.60.2 0x0E76B | curve 7x1 @0x0E56C (values) | 50 50 50 50 50 | 86 78 64 58 52 |
| 0x0E585-0x0E589 | 5 | v2: exact-context port from GS8.60.2 0x0E77B | curve 7x1 @0x0E57C (values) | 78 70 68 62 5d | 7c 7a 72 6c 60 |
| 0x0E595-0x0E596 | 2 | v2: exact-context port from GS8.60.2 0x0E78B | curve 7x1 @0x0E58C (values) | 78 78 | 7c 7a |
| 0x0E599-0x0E59B | 3 | v2: exact-context port from GS8.60.2 0x0E78B | curve 7x1 @0x0E58C (values) | 5e 5e 5e | 60 5a 5a |
| 0x0E5A5-0x0E5A9 | 5 | v2: exact-context port from GS8.60.2 0x0E79B | curve 7x1 @0x0E59C (values) | 78 70 68 62 5d | 7c 7a 72 6c 60 |
| 0x0E5B5-0x0E5B6 | 2 | v2: exact-context port from GS8.60.2 0x0E7AB | curve 7x1 @0x0E5AC (values) | 78 78 | 7c 7a |
| 0x0E5B9-0x0E5BB | 3 | v2: exact-context port from GS8.60.2 0x0E7AB | curve 7x1 @0x0E5AC (values) | 5e 5e 5e | 60 5a 5a |
| 0x0E5C4-0x0E5C5 | 2 | v2: exact-context port from GS8.60.2 0x0E7BA | curve 7x1 @0x0E5BC (axis/header) | aa 8c | 96 86 |
| 0x0E5D5-0x0E5D5 | 1 | v2: exact-context port from GS8.60.2 0x0E7CB | curve 7x1 @0x0E5CC (values) | 64 | 6e |
| 0x0E5D7-0x0E5D8 | 2 | v2: exact-context port from GS8.60.2 0x0E7CB | curve 7x1 @0x0E5CC (values) | 64 5a | 5c 54 |
| 0x0E5DA-0x0E5DB | 2 | v2: exact-context port from GS8.60.2 0x0E7CB | curve 7x1 @0x0E5CC (values) | 4c 4c | 50 50 |
| 0x0E5E5-0x0E5E6 | 2 | v2: exact-context port from GS8.60.2 0x0E7DB | curve 7x1 @0x0E5DC (values) | 64 64 | 96 6e |
| 0x0E5EA-0x0E5EB | 2 | v2: exact-context port from GS8.60.2 0x0E7DB | curve 7x1 @0x0E5DC (values) | 4e 4e | 4a 4a |
| 0x0E5F9-0x0E5FB | 3 | v2: exact-context port from GS8.60.2 0x0E7EF | curve 7x1 @0x0E5EC (values) | 5d 2e 2e | 50 2c 2c |
| 0x0E605-0x0E606 | 2 | v2: close-curve delta (Alpina change on GS8.55 values) | curve 7x1 @0x0E5FC (values) | 6c 6a | 78 70 |
| 0x0E608-0x0E60B | 4 | v2: close-curve delta (Alpina change on GS8.55 values) | curve 7x1 @0x0E5FC (values) | 62 5d 5a 5a | 60 56 52 52 |
| 0x0E625-0x0E626 | 2 | v2: exact-context port from GS8.60.2 0x0E81B | curve 7x1 @0x0E61C (values) | 78 72 | 70 70 |
| 0x0E635-0x0E63B | 7 | v2: exact-context port from GS8.60.2 0x0E82B | curve 7x1 @0x0E62C (values) | 50 50 50 50 50 50 50 | 78 70 68 62 5d 5c 5c |
| 0x0E645-0x0E64B | 7 | v2: exact-context port from GS8.60.2 0x0E83B | curve 7x1 @0x0E63C (values) | 6e 6a 64 64 60 5a 5a | 78 70 68 62 5d 5c 5c |
| 0x0E675-0x0E67B | 7 | v2: exact-context port from GS8.60.2 0x0E86B | curve 7x1 @0x0E66C (values) | 58 54 50 50 50 50 50 | 3c 3c 3c 3c 3c 3c 3c |
| 0x0E695-0x0E69B | 7 | v2: exact-context port from GS8.60.2 0x0E88B | curve 7x1 @0x0E68C (values) | 78 6e 60 5c 58 54 54 | 50 50 50 50 50 50 50 |
| 0x0E6A5-0x0E6A5 | 1 | v2: close-curve delta (Alpina change on GS8.55 values) | curve 7x1 @0x0E69C (values) | 80 | 84 |
| 0x0E6A9-0x0E6AB | 3 | v2: close-curve delta (Alpina change on GS8.55 values) | curve 7x1 @0x0E69C (values) | 58 54 54 | 44 40 40 |
| 0x0E6B9-0x0E6BB | 3 | v2: close-curve delta (Alpina change on GS8.55 values) | curve 7x1 @0x0E6AC (values) | 3c 3c 3c | 3e 40 40 |
| 0x0E6C5-0x0E6CB | 7 | v2: exact-context port from GS8.60.2 0x0E8BB | curve 7x1 @0x0E6BC (values) | a8 9c 82 64 58 54 54 | 78 74 68 60 44 40 40 |
| 0x0E6D2-0x0E6D5 | 4 | v2: exact-context port from GS8.60.2 0x0E8C8 | curve 4x1 @0x0E6CC (values) | 0f 0c 0c 0c | 0a 0a 0a 0a |
| 0x0E6E9-0x0E6E9 | 1 | v2: exact-context port from GS8.60.2 0x0E8DF | raw data / 16-bit table | e6 | a4 |
| 0x0E6F3-0x0E6F3 | 1 | v2: exact-context port from GS8.60.2 0x0E8E9 | raw data / 16-bit table | a4 | b4 |
| 0x0E6FD-0x0E6FD | 1 | v2: exact-context port from GS8.60.2 0x0E8F3 | raw data / 16-bit table | c8 | a4 |
| 0x0E707-0x0E707 | 1 | v2: exact-context port from GS8.60.2 0x0E8FD | raw data / 16-bit table | a4 | b4 |
| 0x0E71B-0x0E71B | 1 | v2: exact-context port from GS8.60.2 0x0E911 | raw data / 16-bit table | c8 | fa |
| 0x0E72F-0x0E72F | 1 | v2: exact-context port from GS8.60.2 0x0E925 | raw data / 16-bit table | c8 | a4 |
| 0x0E739-0x0E739 | 1 | v2: exact-context port from GS8.60.2 0x0E92F | raw data / 16-bit table | be | a4 |
| 0x0E743-0x0E743 | 1 | v2: exact-context port from GS8.60.2 0x0E939 | raw data / 16-bit table | 78 | 97 |
| 0x0E757-0x0E757 | 1 | v2: exact-context port from GS8.60.2 0x0E94D | raw data / 16-bit table | b4 | be |
| 0x0E761-0x0E761 | 1 | v2: exact-context port from GS8.60.2 0x0E957 | raw data / 16-bit table | aa | 97 |
| 0x0E76B-0x0E76B | 1 | v2: exact-context port from GS8.60.2 0x0E961 | raw data / 16-bit table | c8 | a4 |
| 0x0E775-0x0E775 | 1 | v2: exact-context port from GS8.60.2 0x0E96B | raw data / 16-bit table | aa | be |
| 0x0E7A7-0x0E7A7 | 1 | v2: exact-context port from GS8.60.2 0x0E99D | raw data / 16-bit table | dc | d2 |
| 0x0E7B1-0x0E7B1 | 1 | v2: exact-context port from GS8.60.2 0x0E9A7 | raw data / 16-bit table | e6 | d2 |
| 0x0E7E3-0x0E7E5 | 3 | v2: exact-context port from GS8.60.2 0x0E9D9 | curve 7x1 @0x0E7DA (values) | 91 8c 81 | 86 84 82 |
| 0x0E7F3-0x0E7F5 | 3 | v2: exact-context port from GS8.60.2 0x0E9E9 | curve 7x1 @0x0E7EA (values) | 91 8c 81 | 86 84 82 |
| 0x0E803-0x0E803 | 1 | v2: exact-context port from GS8.60.2 0x0E9F9 | curve 7x1 @0x0E7FA (values) | 8a | 83 |
| 0x0E807-0x0E807 | 1 | v2: exact-context port from GS8.60.2 0x0E9F9 | curve 7x1 @0x0E7FA (values) | 80 | 81 |
| 0x0E81E-0x0E820 | 3 | v2: exact-context port from GS8.60.2 0x0EA14 | curve 6x1 @0x0E81A (axis/header) | 66 99 cc | 80 b3 e6 |
| 0x0E825-0x0E827 | 3 | v2: exact-context port from GS8.60.2 0x0EA1B | curve 6x1 @0x0E81A (values) | 84 82 82 | 85 85 85 |
| 0x0E8F6-0x0E8F9 | 4 | v2: close-curve delta (Alpina change on GS8.55 values) | curve 6x1 @0x0E8EC (values) | 80 80 80 80 | 7f 7e 7e 7e |
| 0x0E90A-0x0E90F | 6 | v2: exact-context port from GS8.60.2 0x0EB00 | curve 6x1 @0x0E908 (axis/header) | 2f 3f 5e 7d 9c bc | 10 1f 2f 3f 4e 9c |
| 0x0E913-0x0E915 | 3 | v2: exact-context port from GS8.60.2 0x0EB00 | curve 6x1 @0x0E908 (values) | 81 82 83 | 80 80 80 |
| 0x0E926-0x0E92B | 6 | v2: exact-context port from GS8.60.2 0x0EB1C | curve 6x1 @0x0E924 (axis/header) | 10 1f 2f 3f 4e 9c | 1f 2f 3f 4e 5e 7d |
| 0x0E959-0x0E95B | 3 | v2: close-curve delta (Alpina change on GS8.55 values) | curve 6x1 @0x0E94E (values) | 83 84 84 | 82 82 82 |
| 0x0EA02-0x0EA02 | 1 | v2: close-curve delta (Alpina change on GS8.55 values) | curve 2x1 @0x0E9FE (values) | 0c | 08 |
| 0x0EA26-0x0EA27 | 2 | v2: exact-context port from GS8.60.2 0x0EC76 | curve 2x1 @0x0EA22 (values) | 10 10 | 0c 0c |
| 0x0EA62-0x0EA65 | 4 | v2: exact-context port from GS8.60.2 0x0ECB2 | curve 4x1 @0x0EA5C (values) | 13 17 1b 1e | 0c 0c 0f 12 |
| 0x0EA70-0x0EA75 | 6 | v2: exact-context port from GS8.60.2 0x0ECC0 | curve 7x1 @0x0EA66 (values) | 23 1d 1c 1c 1c 1c | 24 1e 1b 1a 1a 1a |
| 0x0EA7F-0x0EA85 | 7 | v2: exact-context port from GS8.60.2 0x0ECCF | curve 7x1 @0x0EA76 (values) | 80 2c 19 10 10 0f 0f | 79 1f 11 0f 0e 0e 0e |
| 0x0EA8F-0x0EA95 | 7 | v2: close-curve delta (Alpina change on GS8.55 values) | curve 7x1 @0x0EA86 (values) | 35 24 15 0f 0e 10 11 | 79 1f 11 0d 0b 0d 0e |
| 0x0EA9F-0x0EAA5 | 7 | v2: exact-context port from GS8.60.2 0x0ECEF | curve 7x1 @0x0EA96 (values) | 35 2c 19 10 10 0f 0f | 79 1f 11 0f 0e 0e 0e |
| 0x0EAAF-0x0EAB5 | 7 | v2: close-curve delta (Alpina change on GS8.55 values) | curve 7x1 @0x0EAA6 (values) | 35 24 15 0f 0e 10 11 | 79 1f 11 0d 0b 0d 0e |
| 0x0EABE-0x0EABE | 1 | v2: exact-context port from GS8.60.2 0x0ED0E | curve 7x1 @0x0EAB6 (axis/header) | aa | 96 |
| 0x0EAC3-0x0EAC5 | 3 | v2: exact-context port from GS8.60.2 0x0ED13 | curve 7x1 @0x0EAB6 (values) | 1e 1e 1e | 1c 1a 1a |
| 0x0EAD0-0x0EAD2 | 3 | v2: exact-context port from GS8.60.2 0x0ED20 | curve 7x1 @0x0EAC6 (values) | 11 0f 0e | 13 0d 0c |
| 0x0EADF-0x0EAE0 | 2 | v2: close-curve delta (Alpina change on GS8.55 values) | curve 7x1 @0x0EAD6 (values) | 1e 11 | 1d 10 |
| 0x0EAE2-0x0EAE5 | 4 | v2: close-curve delta (Alpina change on GS8.55 values) | curve 7x1 @0x0EAD6 (values) | 0d 0c 0a 0b | 0e 0e 0c 0d |
| 0x0EAEF-0x0EAF1 | 3 | v2: close-curve delta (Alpina change on GS8.55 values) | curve 7x1 @0x0EAE6 (values) | 13 12 0d | 2a 16 0e |
| 0x0EAF3-0x0EAF3 | 1 | v2: close-curve delta (Alpina change on GS8.55 values) | curve 7x1 @0x0EAE6 (values) | 0b | 09 |
| 0x0EAFF-0x0EB00 | 2 | v2: close-curve delta (Alpina change on GS8.55 values) | curve 7x1 @0x0EAF6 (values) | 23 1c | 33 1b |
| 0x0EB04-0x0EB05 | 2 | v2: close-curve delta (Alpina change on GS8.55 values) | curve 7x1 @0x0EAF6 (values) | 09 09 | 0a 0a |
| 0x0EB0F-0x0EB15 | 7 | v2: exact-context port from GS8.60.2 0x0ED5F | curve 7x1 @0x0EB06 (values) | 27 1e 14 10 0f 0b 0c | 28 1b 13 0f 0a 08 08 |
| 0x0EB1F-0x0EB25 | 7 | v2: close-curve delta (Alpina change on GS8.55 values) | curve 7x1 @0x0EB16 (values) | 28 1c 16 12 0e 0b 0c | 46 27 19 10 0b 0a 0a |
| 0x0EB2F-0x0EB31 | 3 | v2: exact-context port from GS8.60.2 0x0ED7F | curve 7x1 @0x0EB26 (values) | 32 23 15 | 1c 17 12 |
| 0x0EB33-0x0EB33 | 1 | v2: exact-context port from GS8.60.2 0x0ED7F | curve 7x1 @0x0EB26 (values) | 0e | 0d |
| 0x0EB3F-0x0EB45 | 7 | v2: exact-context port from GS8.60.2 0x0ED8F | curve 7x1 @0x0EB36 (values) | 4b 28 13 0d 09 09 09 | 4a 1e 10 0e 0e 0e 0e |
| 0x0EB4F-0x0EB51 | 3 | v2: exact-context port from GS8.60.2 0x0ED9F | curve 7x1 @0x0EB46 (values) | 28 1e 16 | 20 1a 15 |
| 0x0EB5F-0x0EB60 | 2 | v2: close-curve delta (Alpina change on GS8.55 values) | curve 7x1 @0x0EB56 (values) | 28 1b | 1d 17 |
| 0x0EB62-0x0EB65 | 4 | v2: close-curve delta (Alpina change on GS8.55 values) | curve 7x1 @0x0EB56 (values) | 10 0e 0e 0d | 0f 0c 0c 0b |
| 0x0EB6F-0x0EB72 | 4 | v2: exact-context port from GS8.60.2 0x0EDBF | curve 7x1 @0x0EB66 (values) | 2e 23 16 11 | 39 22 17 12 |
| 0x0EB74-0x0EB75 | 2 | v2: exact-context port from GS8.60.2 0x0EDBF | curve 7x1 @0x0EB66 (values) | 0f 0f | 10 10 |
| 0x0EB7F-0x0EB7F | 1 | v2: exact-context port from GS8.60.2 0x0EDCF | curve 7x1 @0x0EB76 (values) | 2c | 39 |
| 0x0EB81-0x0EB85 | 5 | v2: exact-context port from GS8.60.2 0x0EDCF | curve 7x1 @0x0EB76 (values) | 1b 16 12 11 11 | 17 12 0f 0f 10 |
| 0x0EB8F-0x0EB90 | 2 | v2: exact-context port from GS8.60.2 0x0EDDF | curve 7x1 @0x0EB86 (values) | 32 1e | 1c 16 |
| 0x0EB92-0x0EB95 | 4 | v2: exact-context port from GS8.60.2 0x0EDDF | curve 7x1 @0x0EB86 (values) | 0f 0d 0c 0c | 13 10 0f 0f |
| 0x0EB9F-0x0EBA5 | 7 | v2: close-curve delta (Alpina change on GS8.55 values) | curve 7x1 @0x0EB96 (values) | 23 21 1a 15 13 11 11 | 2b 26 1f 1f 1d 19 19 |
| 0x0EBAF-0x0EBB1 | 3 | v2: close-curve delta (Alpina change on GS8.55 values) | curve 7x1 @0x0EBA6 (values) | 1a 0d 0b | 09 09 09 |
| 0x0EBB4-0x0EBB5 | 2 | v2: close-curve delta (Alpina change on GS8.55 values) | curve 7x1 @0x0EBA6 (values) | 08 08 | 09 07 |
| 0x0EBBF-0x0EBC5 | 7 | v2: close-curve delta (Alpina change on GS8.55 values) | curve 7x1 @0x0EBB6 (values) | 1a 11 0e 0c 09 07 07 | 18 15 11 0d 0b 09 09 |
| 0x0EC0F-0x0EC0F | 1 | v2: exact-context port from GS8.60.2 0x0EE5F | raw data / 16-bit table | 3c | 32 |
| 0x0EC11-0x0EC11 | 1 | v2: exact-context port from GS8.60.2 0x0EE5F | raw data / 16-bit table | 46 | 50 |
| 0x0EC71-0x0EC71 | 1 | v2: exact-context port from GS8.60.2 0x0EEC1 | raw data / 16-bit table | 3c | 32 |
| 0x0EC73-0x0EC73 | 1 | v2: exact-context port from GS8.60.2 0x0EEC1 | raw data / 16-bit table | 46 | 50 |
| 0x0EC7F-0x0EC7F | 1 | v2: exact-context port from GS8.60.2 0x0EECF | raw data / 16-bit table | 3c | 32 |
| 0x0EC81-0x0EC81 | 1 | v2: exact-context port from GS8.60.2 0x0EECF | raw data / 16-bit table | 46 | 50 |
| 0x0EC8D-0x0EC8D | 1 | v2: exact-context port from GS8.60.2 0x0EEDD | raw data / 16-bit table | 3c | 32 |
| 0x0EC8F-0x0EC8F | 1 | v2: exact-context port from GS8.60.2 0x0EEDD | raw data / 16-bit table | 46 | 50 |
| 0x0ECB7-0x0ECB7 | 1 | v2: exact-context port from GS8.60.2 0x0EF07 | raw data / 16-bit table | 3c | 32 |
| 0x0ECB9-0x0ECB9 | 1 | v2: exact-context port from GS8.60.2 0x0EF07 | raw data / 16-bit table | 46 | 50 |
| 0x0ECC5-0x0ECC5 | 1 | v2: exact-context port from GS8.60.2 0x0EF15 | raw data / 16-bit table | 3c | 32 |
| 0x0ECC7-0x0ECC7 | 1 | v2: exact-context port from GS8.60.2 0x0EF15 | raw data / 16-bit table | 46 | 50 |
| 0x0ECCB-0x0ECCB | 1 | v2: exact-context port from GS8.60.2 0x0EF15 | raw data / 16-bit table | 5a | d2 |
| 0x0ECD3-0x0ECD3 | 1 | v2: exact-context port from GS8.60.2 0x0EF23 | raw data / 16-bit table | 28 | 32 |
| 0x0ECD5-0x0ECD5 | 1 | v2: exact-context port from GS8.60.2 0x0EF23 | raw data / 16-bit table | 46 | 50 |
| 0x0ECD9-0x0ECD9 | 1 | v2: exact-context port from GS8.60.2 0x0EF23 | raw data / 16-bit table | 78 | 5a |
| 0x0ECE1-0x0ECE1 | 1 | v2: exact-context port from GS8.60.2 0x0EF31 | raw data / 16-bit table | 3c | 32 |
| 0x0ECE3-0x0ECE3 | 1 | v2: exact-context port from GS8.60.2 0x0EF31 | raw data / 16-bit table | 46 | 50 |
| 0x0ECEF-0x0ECEF | 1 | v2: exact-context port from GS8.60.2 0x0EF3F | raw data / 16-bit table | 3c | 32 |
| 0x0ECF1-0x0ECF1 | 1 | v2: exact-context port from GS8.60.2 0x0EF3F | raw data / 16-bit table | 46 | 50 |
| 0x0ECFD-0x0ECFD | 1 | v2: exact-context port from GS8.60.2 0x0EF4D | raw data / 16-bit table | 3c | 32 |
| 0x0ECFF-0x0ECFF | 1 | v2: exact-context port from GS8.60.2 0x0EF4D | raw data / 16-bit table | 46 | 50 |
| 0x0ED0B-0x0ED0B | 1 | v2: exact-context port from GS8.60.2 0x0EF5B | raw data / 16-bit table | 28 | 32 |
| 0x0ED0D-0x0ED0D | 1 | v2: exact-context port from GS8.60.2 0x0EF5B | raw data / 16-bit table | 46 | 50 |
| 0x0ED11-0x0ED11 | 1 | v2: exact-context port from GS8.60.2 0x0EF5B | raw data / 16-bit table | 78 | 5a |
| 0x0ED19-0x0ED19 | 1 | v2: exact-context port from GS8.60.2 0x0EF69 | raw data / 16-bit table | 3c | 32 |
| 0x0ED1B-0x0ED1B | 1 | v2: exact-context port from GS8.60.2 0x0EF69 | raw data / 16-bit table | 46 | 50 |
| 0x0ED27-0x0ED27 | 1 | v2: exact-context port from GS8.60.2 0x0EF77 | raw data / 16-bit table | 3c | 32 |
| 0x0ED29-0x0ED29 | 1 | v2: exact-context port from GS8.60.2 0x0EF77 | raw data / 16-bit table | 46 | 50 |
| 0x0ED35-0x0ED35 | 1 | v2: exact-context port from GS8.60.2 0x0EF85 | raw data / 16-bit table | 3c | 32 |
| 0x0ED37-0x0ED37 | 1 | v2: exact-context port from GS8.60.2 0x0EF85 | raw data / 16-bit table | 46 | 50 |
| 0x0ED89-0x0ED89 | 1 | v2: exact-context port from GS8.60.2 0x0EFD9 | raw data / 16-bit table | 3c | 32 |
| 0x0ED8B-0x0ED8B | 1 | v2: exact-context port from GS8.60.2 0x0EFD9 | raw data / 16-bit table | 46 | 50 |
| 0x0EDAD-0x0EDAD | 1 | v2: exact-context port from GS8.60.2 0x0EFFD | raw data / 16-bit table | 14 | 0f |
| 0x0EDAF-0x0EDAF | 1 | v2: exact-context port from GS8.60.2 0x0EFFD | raw data / 16-bit table | 14 | 0f |
| 0x0EDB3-0x0EDB3 | 1 | v2: exact-context port from GS8.60.2 0x0EFFD | raw data / 16-bit table | 3c | 32 |
| 0x0EDB5-0x0EDB5 | 1 | v2: exact-context port from GS8.60.2 0x0EFFD | raw data / 16-bit table | 46 | 50 |
| 0x0EDBB-0x0EDBB | 1 | v2: exact-context port from GS8.60.2 0x0F00B | raw data / 16-bit table | 0f | 01 |
| 0x0EDBD-0x0EDBD | 1 | v2: exact-context port from GS8.60.2 0x0F00B | raw data / 16-bit table | 0f | 01 |
| 0x0EDC1-0x0EDC1 | 1 | v2: exact-context port from GS8.60.2 0x0F00B | raw data / 16-bit table | 3c | 32 |
| 0x0EDC3-0x0EDC3 | 1 | v2: exact-context port from GS8.60.2 0x0F00B | raw data / 16-bit table | 46 | 50 |
| 0x0EE0F-0x0EE0F | 1 | v2: exact-context port from GS8.60.2 0x0F05F | raw data / 16-bit table | 0f | 01 |
| 0x0EE11-0x0EE11 | 1 | v2: exact-context port from GS8.60.2 0x0F05F | raw data / 16-bit table | 0f | 01 |
| 0x0EE15-0x0EE15 | 1 | v2: exact-context port from GS8.60.2 0x0F05F | raw data / 16-bit table | 3c | 32 |
| 0x0EE17-0x0EE17 | 1 | v2: exact-context port from GS8.60.2 0x0F05F | raw data / 16-bit table | 46 | 50 |
| 0x0EEDE-0x0EEE3 | 6 | v2: exact-context port from GS8.60.2 0x0F12E | curve 6x1 @0x0EED6 (values) | 1b 1d 1e 20 24 25 | 1e 13 0d 0a 09 09 |
| 0x0EF95-0x0EF95 | 1 | v2: exact-context port from GS8.60.2 0x0F1E5 | raw data / 16-bit table | 23 | 28 |
| 0x0EF97-0x0EF97 | 1 | v2: exact-context port from GS8.60.2 0x0F1E5 | raw data / 16-bit table | 23 | 28 |
| 0x0EF99-0x0EF99 | 1 | v2: exact-context port from GS8.60.2 0x0F1E5 | raw data / 16-bit table | 23 | 28 |
| 0x0F059-0x0F059 | 1 | v2: exact-context port from GS8.60.2 0x0F2A9 | raw data / 16-bit table | 28 | 1e |
| 0x0F05B-0x0F05B | 1 | v2: exact-context port from GS8.60.2 0x0F2A9 | raw data / 16-bit table | 2d | 23 |
| 0x0F05D-0x0F05D | 1 | v2: exact-context port from GS8.60.2 0x0F2A9 | raw data / 16-bit table | 32 | 28 |
| 0x0F067-0x0F067 | 1 | v2: exact-context port from GS8.60.2 0x0F2B7 | raw data / 16-bit table | 28 | 14 |
| 0x0F069-0x0F069 | 1 | v2: exact-context port from GS8.60.2 0x0F2B7 | raw data / 16-bit table | 2d | 1e |
| 0x0F06B-0x0F06B | 1 | v2: exact-context port from GS8.60.2 0x0F2B7 | raw data / 16-bit table | 32 | 28 |
| 0x0F06F-0x0F071 | 3 | v2: exact-context port from GS8.60.2 0x0F2B7 | curve 2x1 @0x0F06C (axis/header) | b9 3c 64 | 7d 28 78 |
| 0x0F0EB-0x0F0EB | 1 | v2: exact-context port from GS8.60.2 0x0F311 | raw data / 16-bit table | 28 | 14 |
| 0x0F0ED-0x0F0ED | 1 | v2: exact-context port from GS8.60.2 0x0F311 | raw data / 16-bit table | 28 | 14 |
| 0x0F0FD-0x0F0FD | 1 | v2: exact-context port from GS8.60.2 0x0F323 | raw data / 16-bit table | 14 | c8 |
| 0x0F123-0x0F123 | 1 | v2: exact-context port from GS8.60.2 0x0F349 | raw data / 16-bit table | 14 | c8 |
| 0x0F13B-0x0F13B | 1 | v2: exact-context port from GS8.60.2 0x0F361 | raw data / 16-bit table | 1e | 3c |
| 0x0F144-0x0F145 | 2 | v2: exact-context port from GS8.60.2 0x0F36A | raw data / 16-bit table | 01 e0 | 02 26 |
| 0x0F147-0x0F147 | 1 | v2: exact-context port from GS8.60.2 0x0F36A | raw data / 16-bit table | f4 | b8 |
| 0x0F149-0x0F14B | 3 | v2: exact-context port from GS8.60.2 0x0F36A | raw data / 16-bit table | f4 01 b8 | b8 02 26 |
| 0x0F151-0x0F151 | 1 | v2: exact-context port from GS8.60.2 0x0F377 | raw data / 16-bit table | c2 | b8 |
| 0x0F156-0x0F159 | 4 | v2: exact-context port from GS8.60.2 0x0F37C | raw data / 16-bit table | 01 f4 01 e0 | 02 26 02 26 |
| 0x0F224-0x0F224 | 1 | v2: exact-context port from GS8.60.2 0x0F45E | raw data / 16-bit table | 14 | 1e |
| 0x0F22C-0x0F22C | 1 | v2: exact-context port from GS8.60.2 0x0F466 | raw data / 16-bit table | 1e | 01 |
| 0x0F230-0x0F230 | 1 | v2: exact-context port from GS8.60.2 0x0F466 | raw data / 16-bit table | 14 | 18 |
| 0x0F31B-0x0F31B | 1 | v2: exact-context port from GS8.60.2 0x0F563 | raw data / 16-bit table | 00 | 0d |
| 0x0F321-0x0F322 | 2 | v2: exact-context port from GS8.60.2 0x0F569 | raw data / 16-bit table | 11 04 | 08 00 |
| 0x0F35C-0x0F35C | 1 | v2: exact-context port from GS8.60.2 0x0F5A4 | raw data / 16-bit table | 64 | 78 |
| 0x0F3CD-0x0F3CD | 1 | v2: exact-context port from GS8.60.2 0x0F618 | raw data / 16-bit table | 0a | 0e |
| 0x0F3D1-0x0F3D1 | 1 | v2: exact-context port from GS8.60.2 0x0F618 | raw data / 16-bit table | 0a | 00 |
| 0x0F3F6-0x0F3F6 | 1 | v2: exact-context port from GS8.60.2 0x0F641 | raw data / 16-bit table | 05 | 00 |
| 0x0F3FC-0x0F3FC | 1 | v2: exact-context port from GS8.60.2 0x0F647 | raw data / 16-bit table | 05 | 03 |
| 0x0F403-0x0F405 | 3 | v2: exact-context port from GS8.60.2 0x0F64E | raw data / 16-bit table | 01 08 08 | 00 0c 0a |
| 0x0F409-0x0F409 | 1 | v2: exact-context port from GS8.60.2 0x0F64E | raw data / 16-bit table | 00 | 08 |
| 0x0F40F-0x0F40F | 1 | v2: exact-context port from GS8.60.2 0x0F65A | raw data / 16-bit table | 04 | 00 |
| 0x0F554-0x0F555 | 2 | v2: exact-context port from GS8.60.2 0x0F864 | raw data / 16-bit table | 1a 2c | 1d b0 |
| 0x0F5B2-0x0F5B3 | 2 | v2: exact-context port from GS8.60.2 0x0F8C2 | curve 6x1 @0x0F5AA (values) | 8d 88 | 80 80 |
| 0x0FFCC-0x0FFCD | 2 | padding (sets WinKFP file checksum) | raw data / 16-bit table | ff ff | 00 07 |
| 0x0FFFE-0x0FFFF | 2 | calibration CRC | raw data / 16-bit table | 87 a8 | 3c 6d |
