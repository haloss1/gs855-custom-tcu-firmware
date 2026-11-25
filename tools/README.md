# Tools

Python 3.11. `pip install pyserial capstone`. Run scripts from a working folder that holds the input
files below. Scripts that import other tools (`ds2`, `gs86_maps`, `gs855_crc`) must run from this
folder or with it on `PYTHONPATH`.

## Inputs you provide (not included)

| File name | What |
|---|---|
| `GS855_B22P0_24_1423159_full.bin` | Full 256 KB read of a stock B22P0_24 unit (`gs855tool.py read --region all --verify`) |
| `nfs_A7505275.bin` | BMW GS8.60.2 data `A7505275.0DA` converted with `parse_0da.py` |
| `alpina_A7505275.bin` | Alpina GS8.60.2 data (`TU02`) converted with `parse_0da.py` |
| `prog_1423416D.bin` | BMW GS8.60.2 program `1423416D.0PA` converted with `parse_0da.py` |
| `G1423170_bmw_original.0DA` | BMW GS8.55 data file for ZB 1423169 (from ISTA/P) |
| `gs86_compare.json` | Output of `compare_all.py` (needs the NFS GD8602 folder) |

## Reading and diagnostics

| Script | Purpose |
|---|---|
| `ds2.py` | DS2 transport (K-line, echo handling, checksum) |
| `gs855tool.py` | `ident`, `read` (full/partial, `--verify`), `verify` against a file |
| `ediabas_read.py` | Read-only EDIABAS jobs via api64.dll |
| `ediabas_clear.py` | `FS_LOESCHEN` + `RESET_ADAPTION` only |
| `ram_monitor.py`, `ram_focus.py`, `ram_states.py` | Live RAM monitoring and analysis |

## Analysis

| Script | Purpose |
|---|---|
| `parse_0da.py` | NFS `.0DA/.0PA` -> binary (type 00 records) |
| `gs86_maps.py` | Table extraction (pointer lists + program references) |
| `compare_all.py` | Align tables across many data sets -> `gs86_compare.json` |
| `m68dis.py`, `ramxref.py`, `bittrace.py`, `fingerprint.py` | 68k disassembly and cross-references (capstone) |
| `alpina_inventory.py` | Inventory of Alpina changes and GS8.55 matches |
| `collect_cs.py`, `nfs_check_all.py` | Collect/verify `$CHECKSUMME` data from NFS/ISTA files |

## Building

| Order | Script | Output |
|---|---|---|
| 1 | `build_alpina_port.py` | v1 image (logic bytes + shift maps + CRC) |
| 2 | `build_v2_lockup.py` | + lockup table |
| 3 | `port_context.py` | + exact-context runs |
| 4 | `port_close.py` | + close curves |
| 5 | `check_partial.py` | consistency check |
| 6 | `build_winkfp_0da.py <image> <out.0DA> <final.bin>` | padding, CRCs, WinKFP file |
| - | `gs855_crc.py`, `verify_0da.py`, `list_changes.py` | checks and change lists |
