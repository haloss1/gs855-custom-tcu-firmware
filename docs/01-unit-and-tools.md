# 01: Unit identification and tools

## The unit

| Item | Value |
|---|---|
| TCU | Bosch GS8.55 (EGS), 0 260 002 502, DS2 address 0x32 |
| BMW part number / hardware | 1423159 / 2A (built week 11/1997 on the reference unit) |
| HW reference / ZIF | B22 P0_24, program 42C0, data RD43 |
| AIF (last programming) | ZB 1423169, SW 1423170 (BMW data file `G1423170.0DA`) |
| CPU / flash | Motorola 68332-class, 256 KB AMD/Fujitsu AM29F200-type flash |

Other GS8.55 hardware: 1423044 (`B22P0_22`, e.g. the Discord community dumps) and 1423204. Their boot
and program code differ from P0_24; do not mix images.

MS4x Flasher does not support this unit ("Hardware ID B22P0_24 not supported").

## Connection

K+DCAN (FTDI) cable in K-line mode, DS2 protocol at 9600 baud 8E1, DTR off. The cable echoes each
request; strip the echo before parsing the answer.

DS2 telegram: `[addr] [len] [data...] [xor of all previous bytes]`. Answer status `A0` = OK,
`B0` = parameter error.

## Reading memory over DS2 (read-only)

`32 09 06 <type> <A2> <A1> <A0> <count> <xor>`

| Type | Reads | Notes |
|---|---|---|
| 0x00 / 0x02 | Flash 0x000000-0x03FFFF | max count 251; beyond 0x40000 -> B0 |
| 0x03 | another memory (EEPROM-like) | |
| 0x04 | RAM at 24-bit 0xFFFxxx (= 0xFFFFFxxx) | used for live monitoring |
| 0x01 | rejected (B0) | |

A full 256 KB read takes about 6 minutes at 251-byte blocks. `tools/gs855tool.py read --verify` reads
twice and compares.

## EDIABAS from Python

`C:\EDIABAS\Bin\api64.dll` exports the handle-based API (`__apiInit(&handle)`, `__apiJob(handle, ...)`,
etc.). `tools/ediabas_read.py` runs read-only jobs (it refuses anything that writes);
`tools/ediabas_clear.py` runs only `GS855.FS_LOESCHEN` and `GS855.RESET_ADAPTION`.

Useful read-only jobs of the flash SGBD `10GD855`: `INFO`, `IDENT`, `HW_REFERENZ`, `DATEN_REFERENZ`,
`ZIF`, `ZIF_BACKUP`, `AIF_LESEN`, `STATUS_LESEN`, `UPROG_LESEN`, `BLOCKLAENGE_MAX` (246).
`STATUS_CODIER_CHECKSUMME` is rejected outside programming mode.

## Live monitoring

`tools/ram_monitor.py` (whole range, ~1 pass / 3 s) and `tools/ram_focus.py` (focused ranges, ~2
passes / s). Manual mode only engages with the engine running. Heavy polling made the instrument
cluster glitch on the test car; poll gently.
