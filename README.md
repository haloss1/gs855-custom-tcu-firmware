# GS8.55 custom TCU firmware (E39 M62 pre-TU, ZF 5HP24)

Alpina-style calibration for the **Bosch GS8.55** transmission control unit (EGS) used with the
pre-TU M62 V8 and the ZF 5HP24 automatic, plus the reverse-engineering notes and tools behind it.

> **Unofficial.** Not an Alpina, BMW, Bosch or ZF release. Tested on one car (v1). Flashing a TCU
> can leave the gearbox undrivable until it is re-flashed. Use at your own risk.

## What it does

| | v1.0.0 (tested) | v2.0.0-beta (untested) |
|---|---|---|
| S gate goes straight to manual (no S mode) | yes | yes |
| Manual mode holds gears until you shift | yes | yes |
| Adaptive driving-style switching off | yes | yes |
| Alpina shift points (later full-load upshifts) | yes | yes |
| Alpina torque-converter lockup (earlier, fully closed) | no | **yes** |
| Further Alpina calibration values (tables proven identical to the GS8.60.2) | no | **yes** (about 950 bytes) |
| Alpina shift-pressure tables | no | no (different hardware scaling, see docs) |

Downloads are on the [Releases](../../releases) page: one WinKFP data file (`G1423170.0DA`) and
instructions per version. Full byte-level change lists: [v1](docs/changes-v1.md), [v2](docs/changes-v2.md).

## Only for this unit

| Item | Must be |
|---|---|
| TCU | GS8.55, Bosch 0 260 002 502 |
| BMW part / hardware number | 1423159 / HW 2A |
| ZIF (project / program / data) | B22 P0_24 / 42C0 / RD43 |
| Assembly / software (AIF) | ZB 1423169 / SW 1423170 |

Other GS8.55 hardware (1423044, 1423204) or assembly numbers run different data. GS8.60.x units are a
different TCU. Check with WinKFP *Diagnosis → ECU Ident*, INPA or Tool32 (`10GD855` → `ZIF`, `AIF_LESEN`)
before flashing.

## Flashing (short version)

Full procedure: [docs/05-winkfp-flashing.md](docs/05-winkfp-flashing.md).

1. You need BMW's GD855 WinKFP files from your own tools (old ISTA/P has them). None are included here.
2. Keep a copy of BMW's original `G1423170.0DA`, then put the release file in `C:\EC-APPS\NFS\DATA\GD855\`.
3. WinKFP: Bootsectorupdate **NOT ACTIVATED**, Test Checksum ON, Comfort mode, ZUSB **1423169**, Program.
4. Ignition off 30 s, then on. Clear faults and reset adaptations.

## Documentation

| Doc | Contents |
|---|---|
| [01 Unit and tools](docs/01-unit-and-tools.md) | Identification, DS2 memory read, RAM read, EDIABAS from Python |
| [02 Flash layout and checksums](docs/02-flash-layout-and-checksums.md) | Memory map, the three TCU CRCs, boot command table |
| [03 Calibration and mode logic](docs/03-calibration-and-mode-logic.md) | Table format, shift/lockup maps, lever → mode logic, option bits, live RAM addresses |
| [04 Alpina analysis and porting](docs/04-alpina-analysis-and-porting.md) | What Alpina changed, how it was ported, what was left out and why |
| [05 WinKFP flashing](docs/05-winkfp-flashing.md) | NFS data format, `$CHECKSUMME`, procedure, recovery |

Tools (Python) are in [tools/](tools/README.md). They need your own reads and BMW files as input.

## What is not in this repository

No BMW, Bosch, ZF or Alpina files: no SGBDs, flash scripts, NFS/ISTA data, original data or program
files, and no flash dumps. The release `.0DA` files contain the modified calibration only.
