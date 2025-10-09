# 05-TELESCOPES

Space telescope design, systems engineering, and mission definition following ECSS standards.

## Overview

This section contains all space telescope-related design, systems engineering, and mission planning work, organized according to ECSS practices and SPACE-T (STA) architecture.

## Contents

- **00-README.md** - This file
- **[DOMAIN_INTEGRATION/](./DOMAIN_INTEGRATION/)** - Domain integration products, models, and systems following STA structure
  - **[SPACE-TELESCOPE Product](./DOMAIN_INTEGRATION/PRODUCTS/SPACE-TELESCOPE/MODELS/BASELINE/VERSION/V001/README.md)** - Baseline telescope model documentation
  - **[Quick Reference](./DOMAIN_INTEGRATION/PRODUCTS/SPACE-TELESCOPE/MODELS/BASELINE/VERSION/V001/QUICK_REFERENCE.md)** - Systems quick reference guide
- **CONFIGURATION_BASE/** - Baseline configuration and change management
- **MISSION_DEFINITION/** - Mission objectives, requirements, and CONOPS

## STA Structure

Telescopes follow the SPACE-T architecture with STA chapter sets (A-M) as defined in the main README:
- **A)** Structures & Mechanisms (ch. 06, 50-57, 66, 94)
- **B)** Thermal & TPS (ch. 21, 30)
- **C)** Power / EPS / Harness (ch. 24, 39, 49, 97)
- **D)** Communications (RF/Optical) & TT&C (ch. 23, 33, 48)
- **E)** Navigation, Time & Data Handling (ch. 31, 34, 41)
- **F)** Avionics, FSW & Databus (ch. 40, 42, 93)
- **G)** Control, Autonomy, FDIR & Health (ch. 22, 44, 45)
- **H)** ECLSS, Crew & Payload Accommodation (ch. 25, 35-38)
- **I)** Propulsion & Fluids (ch. 28, 29, 47, 60-85)
- **J)** Docking, Sampling & Robotics (ch. 58, 59)
- **K)** Environment, Safety & Space Traffic (ch. 15, 26, 86, 87, 90)
- **L)** Ground, Integration & Mission Ops (ch. 07, 10, 16, 32, 46, 92)
- **M)** Program, Compliance & Records (ch. 01, 04, 05, 11-14, 17-20, 98-99)

## ECSS Standards

Telescope design follows European Cooperation for Space Standardization (ECSS) standards:
- ECSS-E: Engineering standards
- ECSS-M: Management standards
- ECSS-Q: Quality assurance standards
- ECSS-S: System standards

## Key Subsystems

### Mission Definition
- Mission objectives and requirements
- Orbital mechanics and trajectory design
- Operations concept (CONOPS)
- Success criteria
- Science objectives and instrument requirements

### Optical Systems
- Primary and secondary optics
- Optical bench and support structure
- Alignment and calibration
- Stray light control

### Detector Systems
- Focal plane assemblies
- Detector cooling systems
- Signal processing electronics
- Data acquisition systems

### Systems Engineering
- System budgets (mass, power, data, thermal)
- Interface Control Documents (ICDs)
- Requirements management
- Verification and validation planning

### Power & Thermal
- Power generation (solar arrays)
- Power storage (batteries)
- Power distribution and regulation
- Thermal control systems (cryogenic and passive)

### Communications & Data
- Science data handling and storage
- Communication systems (uplink/downlink)
- Telemetry and command handling
- Ground segment interfaces

### Structures & Pointing
- Primary structure design
- Mechanisms and deployables
- Pointing and stability systems
- Vibration isolation

## Product Architecture

Telescopes use the standard SPACE-T product structure:
```
DOMAIN_INTEGRATION/PRODUCTS/<PRODUCT-ID>/MODELS/<MODEL-ID>/VERSION/<TAG>/
└─ SYSTEMS/
   └─ STA-XX_NAME/
      ├─ INTEGRATION_VIEW.md
      ├─ INTERFACE_MATRIX/
      │  └─ XX↔OTHERS.csv
      └─ SUBSYSTEMS/
         └─ XX-YY_SUBSYS/
            ├─ README.md
            ├─ DELs/
            ├─ PAx/
            ├─ PLM/CAx/
            ├─ SUPPLIERS/
            ├─ policy/
            ├─ tests/
            └─ META.json
```

### Architecture Rules

**Key principles for telescope systems:**

1. **PLM/CAx ONLY in SUBSYSTEMS**: Engineering artifacts (CAD, CAE, CAM, etc.) are maintained only at the subsystem level under `SUBSYSTEMS/*/PLM/CAx/`, never at system or domain level.

2. **Software with Host LRU**: Software resides with its hosting Line Replaceable Unit (e.g., avionics partitions under `42-AVIONICS_CONTROL`).

3. **EWIS ONLY in 92-EWIS_HARNESS**: All electrical wiring interconnection system (harnesses, connectors, routing) is maintained exclusively in system `92-EWIS_HARNESS`.

4. **Interface Matrices at System Level**: Each system has an `INTERFACE_MATRIX/` directory containing CSV files documenting interfaces with other systems.

### Custom Optical Systems Block (70-OPTICAL_SUBSYSTEMS)

System `70-OPTICAL_SUBSYSTEMS` is a custom block specifically for telescope optics, containing:

**Subsystems:**
- [`70-10_PRIMARY_MIRROR`](./DOMAIN_INTEGRATION/PRODUCTS/SPACE-TELESCOPE/MODELS/BASELINE/VERSION/V001/SYSTEMS/70-OPTICAL_SUBSYSTEMS/SUBSYSTEMS/70-10_PRIMARY_MIRROR/) - Primary mirror assembly and coatings
- [`70-20_SECONDARY_MIRROR`](./DOMAIN_INTEGRATION/PRODUCTS/SPACE-TELESCOPE/MODELS/BASELINE/VERSION/V001/SYSTEMS/70-OPTICAL_SUBSYSTEMS/SUBSYSTEMS/70-20_SECONDARY_MIRROR/) - Secondary mirror assembly
- [`70-30_TERTIARY_FLAT`](./DOMAIN_INTEGRATION/PRODUCTS/SPACE-TELESCOPE/MODELS/BASELINE/VERSION/V001/SYSTEMS/70-OPTICAL_SUBSYSTEMS/SUBSYSTEMS/70-30_TERTIARY_FLAT/) - Tertiary flat mirror (if applicable)
- [`70-40_CORRECTORS_LENS`](./DOMAIN_INTEGRATION/PRODUCTS/SPACE-TELESCOPE/MODELS/BASELINE/VERSION/V001/SYSTEMS/70-OPTICAL_SUBSYSTEMS/SUBSYSTEMS/70-40_CORRECTORS_LENS/) - Corrector optics and lenses
- [`70-50_FILTERS_GRISMS`](./DOMAIN_INTEGRATION/PRODUCTS/SPACE-TELESCOPE/MODELS/BASELINE/VERSION/V001/SYSTEMS/70-OPTICAL_SUBSYSTEMS/SUBSYSTEMS/70-50_FILTERS_GRISMS/) - Filters and grism assemblies
- [`70-60_DETECTOR_CRYOSTATS`](./DOMAIN_INTEGRATION/PRODUCTS/SPACE-TELESCOPE/MODELS/BASELINE/VERSION/V001/SYSTEMS/70-OPTICAL_SUBSYSTEMS/SUBSYSTEMS/70-60_DETECTOR_CRYOSTATS/) - Detector assemblies and cryostats
- [`70-70_WAVEFRONT_SENSORS`](./DOMAIN_INTEGRATION/PRODUCTS/SPACE-TELESCOPE/MODELS/BASELINE/VERSION/V001/SYSTEMS/70-OPTICAL_SUBSYSTEMS/SUBSYSTEMS/70-70_WAVEFRONT_SENSORS/) - Wavefront sensing optics
- [`70-80_CALIBRATION_SOURCES`](./DOMAIN_INTEGRATION/PRODUCTS/SPACE-TELESCOPE/MODELS/BASELINE/VERSION/V001/SYSTEMS/70-OPTICAL_SUBSYSTEMS/SUBSYSTEMS/70-80_CALIBRATION_SOURCES/) - Calibration light sources

Each subsystem contains full PLM/CAx engineering artifacts (CAD, CAE, CAM, CAI, CAV, CAP, CAS, CMP).

**See also:**
- [System 70 Integration View](./DOMAIN_INTEGRATION/PRODUCTS/SPACE-TELESCOPE/MODELS/BASELINE/VERSION/V001/SYSTEMS/70-OPTICAL_SUBSYSTEMS/INTEGRATION_VIEW.md)
- [System 70 Interface Matrix](./DOMAIN_INTEGRATION/PRODUCTS/SPACE-TELESCOPE/MODELS/BASELINE/VERSION/V001/SYSTEMS/70-OPTICAL_SUBSYSTEMS/INTERFACE_MATRIX/)
- [Complete Systems Catalog](./DOMAIN_INTEGRATION/PRODUCTS/SPACE-TELESCOPE/MODELS/BASELINE/VERSION/V001/README.md#systems-catalog)

### Interface Matrix CSV Format

All interface matrices use the following header:
```csv
from_system,to_system,interface_type,icd_ref,signals/measures,thermal,mechanical,electrical,data_bus,harness,sw_api,safety_class,owner,status,notes
```

Interface Control Documents (ICDs) are referenced from: [`00-PROGRAM/CONFIG_MGMT/09-INTERFACES/`](../../00-PROGRAM/CONFIG_MGMT/09-INTERFACES/)

## Quick Start

### Documentation Navigation

- **[Product Model README](./DOMAIN_INTEGRATION/PRODUCTS/SPACE-TELESCOPE/MODELS/BASELINE/VERSION/V001/README.md)** - Complete systems catalog and detailed architecture
- **[Quick Reference Guide](./DOMAIN_INTEGRATION/PRODUCTS/SPACE-TELESCOPE/MODELS/BASELINE/VERSION/V001/QUICK_REFERENCE.md)** - Tables, commands, and common tasks
- **[Systems Directory](./DOMAIN_INTEGRATION/PRODUCTS/SPACE-TELESCOPE/MODELS/BASELINE/VERSION/V001/SYSTEMS/)** - All 34 telescope systems

### Scripts

- **[Create Telescope Systems](../../scripts/create-telescope-systems.sh)** - Generate complete structure
- **[Validate Structure](../../scripts/validate-telescope-systems.sh)** - Verify compliance with architecture rules

### Key Systems

- **[70-OPTICAL_SUBSYSTEMS](./DOMAIN_INTEGRATION/PRODUCTS/SPACE-TELESCOPE/MODELS/BASELINE/VERSION/V001/SYSTEMS/70-OPTICAL_SUBSYSTEMS/)** - Custom optics block (8 subsystems)
- **[71-INSTRUMENTS_PAYLOADS](./DOMAIN_INTEGRATION/PRODUCTS/SPACE-TELESCOPE/MODELS/BASELINE/VERSION/V001/SYSTEMS/71-INSTRUMENTS_PAYLOADS/)** - Science instruments (3 subsystems)
- **[92-EWIS_HARNESS](./DOMAIN_INTEGRATION/PRODUCTS/SPACE-TELESCOPE/MODELS/BASELINE/VERSION/V001/SYSTEMS/92-EWIS_HARNESS/)** - Centralized electrical wiring
