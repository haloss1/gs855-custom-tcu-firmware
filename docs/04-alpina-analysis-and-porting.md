# 04: Alpina analysis and porting

## Sources

There is no Alpina data set for the GS8.55. The reference is the GS8.60.2 (pre-TU, program
`B22QH_0307C0`) Alpina data set `A7505275.0DA`, ident `TU02`. It is BMW's stock `A7505275` (ident
`QJ10`, E38/E39 M62B44 ECE) with 4,441 bytes changed. A second Alpina set exists for the TU program
(`A7509370`, ident `6212`, base "M62B44 HH JA"); it is much less similar to the GS8.55.

BMW's own NFS also contains official Alpina data for the Roadster V8 (M62B48): `A7834461`, `A7834463`.

## What Alpina changes (GS8.60.2)

- Gate default before the first tip: 0x83EB FE -> 0B (S position = manual).
- Driving-style logic: limits 0x833C/0x8340 -> 00, thresholds 0x834A -> FF, so the adaptive level
  stays fixed.
- Function-enable 0x8B4B F7 -> 11 and 0x8B4C bit 1 off: driving-style evaluators off.
- Manual-mode program table 0x83EE (4x16): rows 0/10 and 11-13 rewritten (GS8.60.2-specific).
- Shift maps 0x9276, 0x9666 (earlier part-throttle upshifts), 0x94A6 (later full-load upshifts).
- Converter lockup table 0x97C0: fully closed = engage, two extra lockup groups, lockup kept under high pedal.
- About 4,000 further bytes in 0xC000-0xFFFF: small curves, 16-bit tables, and 4x4/3x3 maps that look
  like shift pressure.

## How it was ported

1. **Logic bytes** (gate default, limits, thresholds, option bits): equivalent GS8.55 addresses found by
   disassembly (same code structure in both firmwares). See [03](03-calibration-and-mode-logic.md).
2. **Shift maps:** matched by content; Alpina's change (Alpina - stock) added to the GS8.55 values.
   Hysteresis checked (every upshift line above its downshift).
3. **Lockup table:** same table on both units; Alpina's values copied (a delta would break the
   "fully closed = engage" pattern).
4. **Exact-context port** (`tools/port_context.py`): for each changed run, BMW's stock bytes plus 8-16
   bytes of context on each side must occur **exactly once** in the GS8.55 calibration; then Alpina's
   bytes are copied. 182 runs. Address offsets drift smoothly between neighbouring tables.
5. **Close curves** (`tools/port_close.py`): byte curves with identical axes and slightly different
   stock values; per cell, Alpina's value if GS8.55 == stock, else GS8.55 + (Alpina - stock). Offset
   must agree with nearby context matches. 38 curves.
6. **Consistency** (`tools/check_partial.py`): no table may have only part of its Alpina changes. One
   table (GS8.60.2 0xEAB8 = GS8.55 0xE8C4) had only its axis ported and was reverted.

## Left out on purpose

- **Pressure-like tables at 0xD000** (about 1,700 bytes). On the GS8.55 they have different axes
  (e.g. Y `25 50 125 200` vs `38 50 88 125`) and a different value scale, and Alpina changes them in
  both directions. Porting would be guesswork; wrong pressure can slip or burn clutches.
- Runs that are ambiguous (22) or whose stock bytes don't exist on the GS8.55 (about 275).
- The GS8.60.2 manual-mode program table 0x83EE (no GS8.55 equivalent found).

Observation: some Alpina GS8.60.2 tables move towards values the GS8.55 already has (e.g. 0xC198),
so part of that behaviour may already be in the GS8.55 stock data.

## Not known

The function of most tables in the exact-context group is not identified; they are only proven to be
the same tables as on the GS8.60.2. If v2 behaves unexpectedly, that group is the first suspect.
