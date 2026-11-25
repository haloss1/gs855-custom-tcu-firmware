# 05: WinKFP flashing

## What you need (from your own BMW tools, not included here)

| File | Where it goes | Where to find it |
|---|---|---|
| GD855 data folder (`GD855.DAT/.HIS/.HWH/.ATS`, `1423*A.0PA`, `G*.0DA`) | `C:\EC-APPS\NFS\DATA\GD855\` | old ISTA/P: `...\ISTA-P\BMW\Services\data\ecudata\E38\data\GD855` |
| `10GD855.prg` (P-SGBD) | `C:\EDIABAS\Ecu\` | ISTA/P `ecudata\E38\ecu` |
| `10GD855.ipo` (PABD) | `C:\EC-APPS\NFS\SGDAT\` | ISTA/P `ecudata\E38\sgdat` (also often in `C:\EC-APPS\INPA\SGDAT`) |

A normal SP-Daten install already lists GD855 in `NFS\DATA\GDATEN\KFCONF10.DA2` and `HWNR.DA2`; no
config edits are needed. Many installs lack the data folder itself.

BMW's `GD855.DAT` line for the target unit:
`1423169,1000000,1423159,A,1423170DA,FFFFFFFFFFD,088,1 P`. BMW's `1423159A.0PA` is identical to the
program code in the unit.

## Procedure (tested with WinKFP 5.3.1, K+DCAN on STD:OBD)

1. Battery charger, ignition on, engine off. Laptop on mains, direct USB, nothing else using the port.
2. Save BMW's original `G1423170.0DA` (way back), then copy the release `G1423170.0DA` over it.
3. *Configuration*: Bootsectorupdate **NOT ACTIVATED**; Test Checksum **ON** (the release files have a
   valid `$CHECKSUMME`). With `SCHNELLE_BAUDRATE=OFF` in `NFS\BIN\Winkfpt.ini` it stays at 9600 baud.
4. *Comfort mode* -> *Choose ZUSB* -> GD855 -> 1423169 -> `ECU = 2A, ADDR = 32` -> OK. Enter VIN.
5. Optional: *Diagnosis* -> *ECU Ident* (1423159 / 2A).
6. *Program*. On the test car: "Programming OK" after about 2 minutes.
7. Ignition off 30 s, on. Clear faults and reset adaptations (`GS855` `FS_LOESCHEN`, `RESET_ADAPTION`).

WinKFP also writes the programming record (AIF, 0x602E) and the TCU adds four entries to its flash log
(0x4464). These are outside the checksummed regions.

To go back: put BMW's original `G1423170.0DA` back and repeat.

## NFS data file format (`.0DA`)

```
;... header lines ...
$REFERENZ B22P0_2442C0RD43 U          <- data ident + check char
:020000040000FA                       Intel-HEX extended linear address
:020000020000FC                       extended segment address
:10800000...                          type 00 data records (0x8000-0xFFBF, 0xFFCE-0xFFEF)
:0EFFC010...                          type 10 "write last" records (0xFFC0-0xFFCD, 0xFFF0-0xFFFD,
:02FFFE10....                           and the TCU CRC at 0xFFFE)
:0060001090                           constant marker
$CHECKSUMME E22A F                    <- CRC-16/ARC + check char
:00000001FF
```

- `$CHECKSUMME` = **CRC-16/ARC** (poly 0xA001 reflected, init 0) over the data bytes of all type 00 and
  type 10 records, in file order. Verified on BMW's files.
- The check character after `$CHECKSUMME` depends only on the 16-bit value (verified on 9,644 values
  from 15,404 BMW files) but its formula is unknown. `data/checksumme_check_chars.json` maps known
  values to characters. The build tool tunes two unused padding bytes (0xFFCC/0xFFCD, `FF` in stock and
  not referenced by the firmware) so the checksum lands on a known value, and recomputes the TCU CRC.
- The `$REFERENZ` and `.DAT` line check characters are also of unknown formula; the release files keep
  BMW's `$REFERENZ` unchanged.

`tools/build_winkfp_0da.py` refills BMW's `G1423170.0DA` with an image; its self-test rebuilds BMW's
file byte-identically from a stock read.
