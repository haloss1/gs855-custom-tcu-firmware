# 03: Calibration format and mode logic

## Table format (Bosch GS8.5x/8.6x)

| Kind | Layout |
|---|---|
| Map | `00 NX 00 NY`, X axis (NX bytes), Y axis (NY bytes), NX*NY values (byte) |
| Curve | `00 N`, X axis (N bytes), N values |

Axes are strictly increasing. Many further tables hold 16-bit big-endian values.

The GS8.55 program reaches calibration through block pointers held in RAM (read live:
F53C = 0xA78C, F540 = 0xA8E8, F544 = 0xA9CE, F548 = 0xAA50) and through pointer lists in the
calibration (e.g. 0x95EC: shift maps, lever tables). The GS8.60.2 program mostly uses absolute
addresses. `tools/gs86_maps.py` extracts tables from pointer lists and program references.

## Shift maps

14 maps of 8x11 at 0x8DDC-0x938C. X = shift lines (1->2, 2->3, 3->4, 4->5 up; 2->1, 3->2, 4->3,
5->4 down), Y = pedal 0-255 (255 = kick-down), values approximately output speed / 32 rpm (about
0.83 km/h per unit on a 540i; inferred, not confirmed).

Content match to the GS8.60.2 pre-TU data: 0x9666 -> 0x8DDC, 0x9276 -> 0x923C (0x9196 close),
0x94A6 -> 0x92AC.

## Torque-converter lockup

0x94F0: `00 1E 00 07`, X = 0..29, Y = `00 05 22 31 40 4F 61`, 210 values = 10 groups of three
(release, engage, fully closed) per row. Same table as GS8.60.2 0x97C0 (stock values differ in only
9 cells).

## Lever -> mode

| Item | Address |
|---|---|
| Lever position (live) | RAM 0xFFF734: 7 P, 6 R, 5 N, 4 D (firmware numbering: 1-3 = "2/3/4", 4 = D) |
| Gate switch | RAM 0xFFF2FA bit 6 |
| Tip +/-, brake | RAM 0xFFF2F9 bit 2 / bit 5 / bit 7 |
| Mode variable | RAM 0xFFFFB6D8: 8 = gate, 0x0B / 0x0D = manual |
| Mode as sent to the cluster | RAM 0xFFF356: 0x40 gate, 0x60 manual |
| Manual active | RAM 0xFFF739 (set on the first tip) |
| Gear | 0xFFF354 (with shift codes 09/0A/0B), target 0xFFF562, actual 0xFFF6A4 |
| Lever x sub-state -> mode tables | 0x825A, 0x827E (selected by RAM B676 == 2), looked up at 0x23240 |
| Mode-request priority routine | 0x22FC8 |
| Gate conversion (Steptronic variant) | 0x2314A |

Mode values FF/FE in the lever table are resolved through the driving-style level (RAM B6B4) and a
fixed table in the program area (0x1147A).

**Gate default before the first tip:** the small table at 0x8604 (`00 04 FE 04 05 06`); its first
entry **0x8606** is used before any tip. Stock `FE` = stay on the driving-style program (S-like).
`0B` = manual immediately. This is the equivalent of GS8.60.2 0x83EB, which Alpina changes from FE
to 0B.

## Driving-style (adaptive) logic

| GS8.55 | GS8.60.2 | Meaning | Stock |
|---|---|---|---|
| 0x82AA-0x82AB | 0x8340 | lower limits | 20 81 |
| 0x82B0-0x82B1 | 0x833C | upper limits | 80 FF |
| 0x82B4-0x82B7 | 0x834A | level thresholds | 00 41 81 C1 |

## Option / function-enable bits

0x82A2 / 0x82A3 match GS8.60.2 0x8B4B / 0x8B4C bit for bit:

| Bit | Function |
|---|---|
| 82A2.7 | gate for the evaluators + own routine (GS8.60.2 0x16EC0) |
| 82A2.6 | driving-style evaluator A (0x1F832 / 0x216AE) |
| 82A2.5 | evaluator B, largest, selects shift-program pointers (0x1E548 / 0x20732) |
| 82A2.4, .2 | not tested in either firmware |
| 82A2.3 | GS8.55 only (0x15768), stock off |
| 82A2.1 | evaluator C, event-based bump of the style value (0x224BE / 0x225D4) |
| 82A2.0 | lever x sub-state override tables (0x234B4 / 0x232D2) |
| 82A3.7 | manual variant 0x0D vs 0x0B |
| 82A3.3 | flag at 0x23336 / 0x26486 |
| 82A3.1 | evaluator D (0x17EDC / 0x1D842) |

Every block enabled by 82A2 bits 7/6/5/1 and 82A3 bit 1 reads the level thresholds at 0x82B2.
