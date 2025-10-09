# Interface Control Documents (ICDs) - Links

## Overview

This document provides links to Interface Control Documents (ICDs) stored in the program-level interface repository.

## ICD Repository Location

All formal ICDs are stored in: `00-PROGRAM/CONFIG_MGMT/09-INTERFACES/`

## Domain Interface Categories

### Power Interfaces
- **Electrical Power Distribution**
  - ICD Location: `09-INTERFACES/ELECTRICAL/`
  - Primary ICDs: AC bus specifications, DC bus specifications
  - Related ATAs: 24, all power consumers

### Data Bus Interfaces
- **ARINC 429 Interfaces**
  - ICD Location: `09-INTERFACES/DATA_BUS/ARINC_429/`
  - Message catalogs for all systems
  - Related ATAs: 24, 42, 45, 46, 73, 76, 77

- **ARINC 664 (AFDX) Interfaces**
  - ICD Location: `09-INTERFACES/DATA_BUS/ARINC_664/`
  - Network topology and virtual links
  - Related ATAs: 24, 42, 46, 73, 76, 77

### Mechanical Interfaces
- **Engine Mounting**
  - ICD Location: `09-INTERFACES/MECHANICAL/ENGINE_MOUNTS/`
  - Related ATAs: 71, 72

- **Actuation Interfaces**
  - ICD Location: `09-INTERFACES/MECHANICAL/ACTUATION/`
  - Related ATAs: 72, 73, 76

### Fluid Interfaces
- **Fuel System**
  - ICD Location: `09-INTERFACES/FLUID/FUEL/`
  - Related ATAs: 28, 49, 72, 73

- **Oil System**
  - ICD Location: `09-INTERFACES/FLUID/OIL/`
  - Related ATAs: 72, 79

### Pneumatic Interfaces
- **Bleed Air**
  - ICD Location: `09-INTERFACES/PNEUMATIC/BLEED_AIR/`
  - Related ATAs: 21, 29, 36, 49, 72, 75

- **Engine Starting Air**
  - ICD Location: `09-INTERFACES/PNEUMATIC/START_AIR/`
  - Related ATAs: 36, 49, 72, 80

### Thermal Interfaces
- **Heat Exchangers**
  - ICD Location: `09-INTERFACES/THERMAL/HEAT_EXCHANGERS/`
  - Related ATAs: 21, 78, 79

### EWIS Interfaces
- **Physical Wiring**
  - ICD Location: `09-INTERFACES/EWIS/` and `02-AIRCRAFT/CONFIGURATION_BASE/ATA-92_EWIS/`
  - All electrical wiring documented per EWIS standards
  - Related ATAs: All systems (physical wiring only)

## ICD Naming Convention

ICDs follow the naming pattern:
- `ICD-{SOURCE_ATA}-{DEST_ATA}-{INTERFACE_TYPE}-{VERSION}.pdf`

Examples:
- `ICD-24-42-POWER-v2.1.pdf` - Electrical power to avionics
- `ICD-72-73-FADEC-v1.3.pdf` - Engine to FADEC interface
- `ICD-75-21-BLEED_AIR-v1.0.pdf` - Bleed air to ECS

## ICD Change Control

All ICD changes must:
1. Be approved by Configuration Control Board (CCB)
2. Update compatibility matrix in `00-PROGRAM/CONFIG_MGMT/06-CHANGES/12-INTERFACE_CHANGES/`
3. Notify affected system owners
4. Update interface matrices in this domain

## Interface Coordination

### Cross-References
- System-level interface matrices in each ATA directory (`01-SYSTEMS/ATA-XX/INTERFACE_MATRIX/`)
- Domain-level interface matrix (`02-INTERFACES/INTERFACE_MATRIX.csv`)
- Program-level ICD repository (`00-PROGRAM/CONFIG_MGMT/09-INTERFACES/`)

### EWIS Coordination
Physical wiring for all interfaces is documented in:
- `02-AIRCRAFT/CONFIGURATION_BASE/ATA-92_EWIS/`

This domain documents logical/functional interfaces only.

## Related Documents

- [Configuration Management](../../../../00-PROGRAM/CONFIG_MGMT/)
- [Interface Change Management](../../../../00-PROGRAM/CONFIG_MGMT/06-CHANGES/12-INTERFACE_CHANGES/)
- [ATA-92 EWIS](../../../CONFIGURATION_BASE/ATA-92_EWIS/)

---

**Last Updated**: 2024-01-15
