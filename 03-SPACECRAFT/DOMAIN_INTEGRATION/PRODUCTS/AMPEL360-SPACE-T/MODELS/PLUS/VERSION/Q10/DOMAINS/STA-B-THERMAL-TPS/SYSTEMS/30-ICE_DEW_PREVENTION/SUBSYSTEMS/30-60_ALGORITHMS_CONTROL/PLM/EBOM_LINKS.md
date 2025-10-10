# Engineering BOM Links

This file contains references to authoritative part definitions in the enterprise PLM/ERP system.

## Format

Each entry should reference:
- Part number
- Part name/description
- PLM/ERP system URL or identifier
- Configuration/revision
- Supplier information (if applicable)

## Example Entries

```
PART-12345 | Sensor Assembly | PLM://erp.example.com/parts/12345 | Rev C | Supplier: ACME Corp
PART-67890 | Mounting Bracket | PLM://erp.example.com/parts/67890 | Rev B | Standard Part
```

## BOM Entries

PROC-FPGA-RAD | Radiation-Hardened FPGA (Xilinx Virtex-5QV) | PLM://plm.ampel.space/parts/PROC-FPGA-RAD | Rev C | Supplier: Xilinx
MEM-SRAM-ECC | ECC SRAM Memory Module (4MB, rad-tolerant) | PLM://plm.ampel.space/parts/MEM-SRAM-ECC | Rev B | Supplier: Cobham
ADC-16BIT-SPI | 16-bit ADC with SPI Interface (8-channel) | PLM://plm.ampel.space/parts/ADC-16BIT-SPI | Rev D | Supplier: Texas Instruments
PWR-REG-LDO | Low-Dropout Regulator (3.3V, rad-hard) | PLM://plm.ampel.space/parts/PWR-REG-LDO | Rev A | Supplier: Intersil
OSC-TCXO-10MHZ | Temperature-Compensated Crystal Oscillator (10 MHz) | PLM://plm.ampel.space/parts/OSC-TCXO-10MHZ | Rev B | Supplier: Vectron
PCB-SUBSTRATE-RF | RF-Compatible PCB Substrate (Rogers 4350B) | PLM://plm.ampel.space/parts/PCB-SUBSTRATE-RF | Rev A | Supplier: Rogers Corporation
CONN-MICRO-D38 | 38-pin Micro-D Connector (space-grade) | PLM://plm.ampel.space/parts/CONN-MICRO-D38 | Rev C | Supplier: TE Connectivity
FILTER-EMI-PWR | EMI Filter for Power Lines (28VDC rated) | PLM://plm.ampel.space/parts/FILTER-EMI-PWR | Rev B | Supplier: API Technologies
TEST-JTAG-CABLE | JTAG Programming Cable (radiation-tolerant) | PLM://plm.ampel.space/parts/TEST-JTAG-CABLE | Rev A | Standard Part
ENCL-SHIELD-AL | Aluminum RF Shield Enclosure (custom) | PLM://plm.ampel.space/parts/ENCL-SHIELD-AL | Rev B | Standard Part

---

**Note**: This file serves as a bridge between this repository structure and the authoritative PLM/ERP system of record.

