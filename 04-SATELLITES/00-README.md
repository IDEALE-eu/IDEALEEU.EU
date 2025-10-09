# 04-SATELLITES

Satellite design, systems engineering, and mission definition following ECSS standards.

## Overview

This section contains all satellite-related design, systems engineering, and mission planning work, organized according to ECSS practices and SPACE-T (STA) architecture.

## Contents

- **00-README.md** - This file
- **[DOMAIN_INTEGRATION/](DOMAIN_INTEGRATION/)** - Domain integration products, models, and systems following STA structure
  - See [DOMAIN_INTEGRATION/README.md](DOMAIN_INTEGRATION/README.md) for complete documentation
  - Use `scripts/create-satellite-domains.sh` to generate new mission structures
- **CONFIGURATION_BASE/** - Baseline configuration and change management
- **MISSION_DEFINITION/** - Mission objectives, requirements, and CONOPS

## Quick Start

### Creating a New Satellite Mission Structure

To generate a complete STA-aligned satellite structure for a new mission:

```bash
./scripts/create-satellite-domains.sh <MISSION> <CONF> <TAG>
```

**Example:**
```bash
./scripts/create-satellite-domains.sh EARTH-OBS-1 BASELINE V1.0
```

This creates the complete structure under:
```
04-SATELLITES/DOMAIN_INTEGRATION/PRODUCTS/EARTH-OBS-1/MODELS/BASELINE/VERSION/V1.0/
```

See [DOMAIN_INTEGRATION/README.md](DOMAIN_INTEGRATION/README.md) for detailed documentation.

## STA Structure

Satellites follow the SPACE-T architecture with STA chapter sets (A-M) as defined in the main README:
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

Satellite design follows European Cooperation for Space Standardization (ECSS) standards:
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

### Systems Engineering
- System budgets (mass, power, data, thermal)
- Interface Control Documents (ICDs)
- Requirements management
- Verification and validation planning

### Power & Thermal
- Power generation (solar arrays)
- Power storage (batteries)
- Power distribution and regulation
- Thermal control systems (active and passive)

### Communications
- Communication systems (uplink/downlink)
- Telemetry and command handling
- Data management

### Structures
- Primary structure design
- Mechanisms and deployables
- Structural analysis and testing

## Product Architecture

Satellites use the standard SPACE-T product structure:
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

**Key Conventions:**
- **PLM/CAx only in SUBSYSTEMS** - All engineering artifacts at subsystem level
- **STA-97 for harness** - Electrical harness uses STA-97 (not ATA-92 which is for aircraft EWIS)
- **Integration focus** - Each system has INTEGRATION_VIEW.md and INTERFACE_MATRIX/
- **ECSS compliance** - Following ECSS-E/M/Q/S standards for space systems
