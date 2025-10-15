# 100-GENERAL — Integration View

## System Overview

**Description:** 100-GENERAL system for standards, templates, and best practices.

**System ID:** 100  
**Interface Matrix:** See [INTERFACE_MATRIX/](./INTERFACE_MATRIX/) for interface definitions.

## Purpose

This system provides integration and coordination for all 100-GENERAL subsystems within the AMPEL360-AIR-T aircraft.

## System Interfaces

The [Interface Matrix](./INTERFACE_MATRIX/) directory contains CSV files defining interfaces with other systems.

## Documentation Structure

```
100-GENERAL/
├─ INTEGRATION_VIEW.md          # This file - integration overview
├─ INTERFACE_MATRIX/            # System interface definitions
│  └─ *.csv                     # Interface requirement CSVs
└─ SUBSYSTEMS/                  # All subsystems for this system
   └─ {SUBSYSTEM}/
      └─ PLM/                   # Engineering artifacts
         ├─ EBOM_LINKS.md       # BOM references
         └─ CAx/                # CAx artifacts by discipline
            ├─ CAD/
            ├─ CAE/
            ├─ CAM/
            ├─ CAI/
            ├─ CAV/
            ├─ CAP/
            ├─ CAS/
            ├─ CAO/
            └─ CMP/
```

## Compliance

- **Standards:** Follow ATA iSpec 2200 and project-specific guidelines
- **ICDs:** see `00-PROGRAM/CONFIG_MGMT/09-INTERFACES/`
- **Baselines & Changes:** `00-PROGRAM/CONFIG_MGMT/04-BASELINES/`

---

**Last Updated:** 2025-10-11
