# SYSTEM: 88-RESERVED_TEMPLATES

**Architecture:** AIR-T (ATA) • **Domain:** OOO-OS-ONTOLOGIES-OFFICE

## Purpose

Integration anchor for **88-RESERVED_TEMPLATES** with interface map and views.

## Quick Links

- **Interface Matrix:** `INTERFACE_MATRIX/*.csv`
- **Integration View:** `INTEGRATION_VIEW.md`
- **Sub-Systems:** `SUBSYSTEMS/*/`

## UiX Workflow

1. Define scope & boundaries in `INTEGRATION_VIEW.md`
2. Add / extend `INTERFACE_MATRIX/*.csv` header below
3. Implement sub-systems in `SUBSYSTEMS/*/`

> PLM & CAx **inside each subsystem** only

### CSV Use Everywhere :

```csv
from_ata,to_ata,interface,signal_or_medium,protocol/spec,notes
```

## Compliance

- **ICDs:** see `00-PROGRAM/CONFIG_MGMT/09-INTERFACES/`
- **Baselines & Changes:** `00-PROGRAM/CONFIG_MGMT/04-BASELINES/`
