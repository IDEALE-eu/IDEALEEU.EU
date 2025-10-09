# DOMAIN_INTEGRATION - Spacecraft Systems Integration

## Overview

This directory implements the **ATA-aligned Domain Integration** pattern for spacecraft systems, following the same `/SYSTEMS/ → SUBSYSTEMS/ → PLM/CAx` structure used in aircraft integration.

## Purpose

The Domain Integration structure provides:
- **Consistent organization** across all spacecraft systems using ATA chapter numbering
- **PLM artifact management** with CAx tool integration (CAD, CAE, CAM)
- **Interface management** through INTEGRATION_VIEW.md and INTERFACE_MATRIX CSV files
- **Traceability** from system-level to subsystem components
- **Configuration control** through product/model/version hierarchy

## Directory Structure

```
DOMAIN_INTEGRATION/
└── PRODUCTS/<MISSION>/
    └── MODELS/<CONFIGURATION>/
        └── VERSION/<TAG>/
            └── SYSTEMS/
                └── ATA-XX_NAME/
                    ├── INTEGRATION_VIEW.md
                    ├── INTERFACE_MATRIX/
                    │   └── XX_INTERFACES.csv
                    └── SUBSYSTEMS/
                        └── ATA-XX-YY_NAME/
                            └── PLM/
                                ├── EBOM_LINKS.md
                                └── CAx/
                                    ├── CAD/
                                    ├── CAE/
                                    ├── CAM/
                                    └── ANALYSIS/
```

## Key Rules

### 1. System Organization
- **Always** use `/SYSTEMS/ATA-XX_NAME/` pattern
- Each SYSTEM has `INTEGRATION_VIEW.md` describing modes, dependencies, budgets
- Each SYSTEM has `INTERFACE_MATRIX/*.csv` for cross-chapter interface tracking

### 2. Software Placement
- **Software resides with its host LRU** in the functional chapter
- Flight software documented in functional system (e.g., ATA-42 for IMA)
- Software-to-hardware binding documented in SUBSYSTEMS

### 3. EWIS (Electrical Wiring Interconnect System)
- **Physical EWIS only in ATA-92** (analogous to aircraft rule)
- Other chapters reference ATA-92 for wiring/harness
- Connector specifications in interface matrices

### 4. PLM Integration
- **PLM artifacts only under** `SUBSYSTEMS/*/PLM/CAx/`
- CAx subdirectories: CAD, CAE, CAM, ANALYSIS
- EBOM_LINKS.md provides traceability to PLM system

## Spacecraft System Sets (A-M)

### Set A: Structures & Mechanisms (10 systems)
- ATA-06, 50, 51, 52, 53, 55, 56, 57, 66, 94
- Primary structure, doors, panels, deployables, compartments

### Set B: Thermal & TPS (2 systems)
- ATA-21, 30
- Thermal control, radiators, MLI, TPS (Thermal Protection System)

### Set C: Power / EPS / Harness (4 systems)
- ATA-24, 39, 49, 97
- Electrical Power System, panels, APU, wiring administration

### Set D: Communications & TT&C (3 systems)
- ATA-23, 33, 48
- RF communications, optical comms, telemetry/telecommand

### Set E: Navigation, Time & Data Handling (3 systems)
- ATA-31, 34, 41
- Sensors, timing, C&DH (Command & Data Handling)

### Set F: Avionics, Flight SW & Databus (3 systems)
- ATA-40, 42, 93
- IMA, flight computers, networks, databus

### Set G: Control, Autonomy, FDIR & Health (3 systems)
- ATA-22, 44, 45
- GNC, attitude control, FDIR, health management

### Set H: ECLSS, Crew & Payload Accommodation (5 systems)
- ATA-25, 35, 36, 37, 38
- Life support, oxygen, pneumatic, vacuum, water/waste

### Set I: Propulsion & Fluids (19 systems)
- ATA-28, 29, 47, 60-61, 70-84
- Main propulsion, RCS, fuel/propellant, engines, electric propulsion

### Set J: Docking, Sampling & Robotics (2 systems)
- ATA-58, 59
- Docking mechanisms, robotic arms, sample acquisition

### Set K: Environment, Safety & Space Traffic (5 systems)
- ATA-15, 26, 86, 87, 90
- Acoustic/vibration, ordnance, planetary protection, radiation, debris

### Set L: Ground, Integration & Mission Ops (6 systems)
- ATA-07, 10, 16, 32, 46, 92
- MGSE, EGSE, integration, landing ops, ground segment, calibration

### Set M: Program, Compliance & Records (13 systems)
- ATA-01, 04, 05, 11-14, 17-20, 98-99
- Program management, standards, compliance, records

## Interface Management

### INTEGRATION_VIEW.md
Each system's INTEGRATION_VIEW.md contains:
- **Operational modes** with power/thermal/data profiles
- **Dependencies** (input/output interfaces)
- **Resource budgets** (mass, power, thermal, data)
- **Cross-system interfaces** references
- **Verification approach** (analysis, test, reviews)
- **Configuration items** listing

### INTERFACE_MATRIX CSV Files
Interface matrices track:
- Interface IDs and descriptions
- Source and destination systems
- Interface types (electrical, mechanical, thermal, data)
- Signal types and connector specifications
- ICD references (links to `00-PROGRAM/CONFIG_MGMT/09-INTERFACES/`)
- Status tracking

### ICD Integration
All detailed Interface Control Documents (ICDs) are managed in:
```
00-PROGRAM/CONFIG_MGMT/09-INTERFACES/
├── ICD_INDEX.md
└── ICD-*.md
```

Interface matrices provide local summaries and point to formal ICDs for detailed specifications.

## Verification & Validation

### HIL/SIL Integration
Hardware-in-the-Loop (HIL) and Software-in-the-Loop (SIL) test items are documented in:
- **Set F** (Avionics, ATA-42) for flight computer simulation
- **Set E** (Data Handling, ATA-41) for C&DH simulation
- **Set G** (Control, ATA-22) for GNC simulation
- **Set L** (EGSE, ATA-16) for ground test equipment

Links maintained to physical test facilities in `03-SPACECRAFT/AIT/`.

### Integration Testing
System-level integration testing documented in:
- `03-SPACECRAFT/AIT/` - Assembly, Integration, Test procedures
- Cross-reference to INTEGRATION_VIEW.md verification sections

## Configuration Management

### Product/Model/Version Hierarchy
- **PRODUCTS:** Mission-specific (e.g., EXAMPLE_MISSION, MARS_ORBITER)
- **MODELS:** Configuration variants (CONFIG_A, CONFIG_B)
- **VERSION:** Release versions (V1.0, V2.0)
- **TAG:** Build tags or release candidates

### Baseline Control
- System baselines controlled through `00-PROGRAM/CONFIG_MGMT/07-RELEASES/`
- Changes managed via ECR/ECO process
- Version tags aligned with program milestones (PDR, CDR, SAR)

## Tags and Metadata

BEZ tag decks (A/B/C/D/E/F/G/I/J/R) can be used as:
- **Front-matter** in `SUBSYSTEMS/*/README.md`
- **TAGS.yaml** files in each subsystem directory
- **References** in DEL (Data Exchange Layer) documentation

## Standards Compliance

### ECSS Standards
- **ECSS-E-ST-10C** - System engineering general requirements
- **ECSS-E-ST-40C** - Software engineering
- **ECSS-M-ST-10C** - Project planning and implementation
- **ECSS-Q-ST-10C** - Product assurance management

### ATA Standards
- ATA iSpec 2200 (adapted for spacecraft)
- Consistent chapter numbering with aircraft domain

## CI/CD Integration

Validation scripts check:
- [ ] `SYSTEMS/` directory present
- [ ] Each system has `INTEGRATION_VIEW.md`
- [ ] Each system has `INTERFACE_MATRIX/*.csv`
- [ ] **PLM only under** `SUBSYSTEMS/*/PLM/CAx/`
- [ ] Software/EWIS placement rules followed

See: `scripts/validate-structure.sh` (to be updated)

## Related Documentation

### Program-Level
- [00-PROGRAM/CONFIG_MGMT/09-INTERFACES/](../../00-PROGRAM/CONFIG_MGMT/09-INTERFACES/) - Interface Control Documents
- [00-PROGRAM/DIGITAL_THREAD/04-MBSE/](../../00-PROGRAM/DIGITAL_THREAD/04-MBSE/) - MBSE integration
- [00-PROGRAM/INDUSTRIALISATION/16-IT_INTEGRATION/PLM_LINKS/](../../00-PROGRAM/INDUSTRIALISATION/16-IT_INTEGRATION/PLM_LINKS/) - PLM system links

### Spacecraft-Level
- [03-SPACECRAFT/SYSTEMS_ENGINEERING/](../SYSTEMS_ENGINEERING/) - Requirements, budgets, ICDs
- [03-SPACECRAFT/AIT/](../AIT/) - Integration and test procedures
- [03-SPACECRAFT/CONFIGURATION_BASE/](../CONFIGURATION_BASE/) - Legacy ATA configuration baseline

### Aircraft Comparison
- [02-AIRCRAFT/DOMAIN_INTEGRATION/](../../02-AIRCRAFT/DOMAIN_INTEGRATION/) - Aircraft integration pattern
- [02-AIRCRAFT/CROSS_SYSTEM_INTEGRATION/](../../02-AIRCRAFT/CROSS_SYSTEM_INTEGRATION/) - Cross-system architecture

## Example Usage

### Adding a New Subsystem
1. Create directory: `SYSTEMS/ATA-XX_NAME/SUBSYSTEMS/ATA-XX-YY_SUBSYSTEM/`
2. Add PLM structure: `PLM/CAx/{CAD,CAE,CAM,ANALYSIS}/`
3. Create `PLM/README.md` and `PLM/EBOM_LINKS.md`
4. Update parent system's `INTEGRATION_VIEW.md`
5. Add interface entries to `INTERFACE_MATRIX/*.csv`

### Documenting an Interface
1. Identify source and destination systems
2. Add entry to both systems' interface matrices
3. Create or reference ICD in `00-PROGRAM/CONFIG_MGMT/09-INTERFACES/`
4. Update `INTEGRATION_VIEW.md` cross-system interfaces section

### Linking PLM Artifacts
1. Store CAD models in `PLM/CAx/CAD/`
2. Document part numbers in `PLM/EBOM_LINKS.md`
3. Reference PLM workspace URL
4. Maintain revision control per `00-PROGRAM/CONFIG_MGMT/01-VERSIONING/`

## Revision History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2024-10-09 | Systems Engineering | Initial spacecraft domain integration structure |

## References

- **ARP4754A** - Guidelines for Development of Civil Aircraft and Systems
- **ECSS-E-ST-10C** - System engineering general requirements
- **ATA iSpec 2200** - Information Standards for Aviation Maintenance
- Problem Statement: Drop-in spacecraft integration using `/SYSTEMS/ → SUBSYSTEMS/ → PLM/CAx` pattern
