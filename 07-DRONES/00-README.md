# 07-DRONES

Drone design, systems engineering, and mission definition (space/stratospheric and atmospheric).

## Overview

This section contains all drone-related design, systems engineering, and mission planning work, organized according to applicable standards (ECSS for space/stratospheric, ATA for atmospheric).

## Contents

- **00-README.md** - This file
- **DOMAIN_INTEGRATION/** - Domain integration products, models, and systems
- **CONFIGURATION_BASE/** - Baseline configuration and change management
- **MISSION_DEFINITION/** - Mission objectives, requirements, and CONOPS

## Architecture

Drones follow either:
- **SPACE-T (STA)** architecture for space/stratospheric drones
- **AIR-T (ATA)** architecture for atmospheric drones

### STA Structure (Space/Stratospheric Drones)

Space/stratospheric drones follow the STA chapter sets (A-M) as defined in the main README:
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

## Standards

Drone design follows applicable standards based on operational domain:

### Space/Stratospheric Drones
- ECSS-E: Engineering standards
- ECSS-M: Management standards
- ECSS-Q: Quality assurance standards
- ECSS-S: System standards

### Atmospheric Drones
- ARP4754A / ARP4761 (systems engineering)
- DO-178C (software)
- DO-254 (hardware)
- DO-160 (environmental conditions)

## Key Subsystems

### Mission Definition
- Mission objectives and requirements
- Flight envelope and operational concept
- Autonomy requirements
- Success criteria

### Systems Engineering
- System budgets (mass, power, data, thermal)
- Interface Control Documents (ICDs)
- Requirements management
- Verification and validation planning

### Propulsion
- Propulsion systems (electric, hybrid, chemical)
- Energy storage and management
- Fuel/propellant systems

### Avionics & Control
- Flight control systems
- Navigation systems (GPS, INS)
- Communication systems
- Autopilot and autonomy

### Payload
- Sensor systems
- Data acquisition
- Payload accommodation
- Mission-specific equipment

### Structures & Materials
- Airframe/spacecraft structure
- Materials selection
- Environmental protection
- Deployment mechanisms

## Product Architecture

Drones use the standard SPACE-T or AIR-T product structure depending on operational domain:
```
DOMAIN_INTEGRATION/PRODUCTS/<PRODUCT-ID>/MODELS/<MODEL-ID>/VERSION/<TAG>/
└─ SYSTEMS/
   └─ <ATA|STA>-XX_NAME/
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
