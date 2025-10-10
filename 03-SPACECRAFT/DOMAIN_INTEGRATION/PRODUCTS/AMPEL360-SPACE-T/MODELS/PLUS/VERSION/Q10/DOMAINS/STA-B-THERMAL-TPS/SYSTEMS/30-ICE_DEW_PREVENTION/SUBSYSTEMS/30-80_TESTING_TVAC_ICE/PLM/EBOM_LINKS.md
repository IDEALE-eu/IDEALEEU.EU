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

TVAC-CHAMBER-L | Large Thermal-Vacuum Chamber (1.5m diameter) | PLM://plm.ampel.space/parts/TVAC-CHAMBER-L | Rev C | Supplier: Applied Test Systems
CRYO-SHROUD-LN2 | LN2 Cryogenic Shroud Panel Kit | PLM://plm.ampel.space/parts/CRYO-SHROUD-LN2 | Rev B | Supplier: Advanced Energy
PUMP-TURBO-300L | Turbomolecular Vacuum Pump (300 L/s) | PLM://plm.ampel.space/parts/PUMP-TURBO-300L | Rev D | Supplier: Agilent
SOLAR-SIM-1000W | Solar Simulator (1000W, AM0 spectrum) | PLM://plm.ampel.space/parts/SOLAR-SIM-1000W | Rev A | Supplier: Newport Oriel
DAQ-HIOKI-32CH | Data Acquisition System (32-channel, high-speed) | PLM://plm.ampel.space/parts/DAQ-HIOKI-32CH | Rev C | Supplier: Hioki
THERMO-TC-ARRAY | Thermocouple Array (Type K, 24-point) | PLM://plm.ampel.space/parts/THERMO-TC-ARRAY | Rev B | Standard Part
GAUGE-PRESSURE-VAC | Vacuum Pressure Gauge (10^-7 to 10^3 Torr) | PLM://plm.ampel.space/parts/GAUGE-PRESSURE-VAC | Rev A | Supplier: MKS Instruments
FIXTURE-MOUNT-TVAC | Custom TVAC Mounting Fixture (aluminum) | PLM://plm.ampel.space/parts/FIXTURE-MOUNT-TVAC | Rev B | Custom Fabrication
ICE-GEN-SPRAY | Ice Generation System (spray nozzle array) | PLM://plm.ampel.space/parts/ICE-GEN-SPRAY | Rev A | Custom Assembly
CTRL-PLC-TVAC | PLC Controller for TVAC Automation | PLM://plm.ampel.space/parts/CTRL-PLC-TVAC | Rev D | Supplier: Siemens

---

**Note**: This file serves as a bridge between this repository structure and the authoritative PLM/ERP system of record.

