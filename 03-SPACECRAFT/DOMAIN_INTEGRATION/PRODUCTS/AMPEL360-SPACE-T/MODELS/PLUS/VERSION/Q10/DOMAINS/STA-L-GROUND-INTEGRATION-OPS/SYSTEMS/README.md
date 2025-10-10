# AMPEL360-SPACE-T Ground Integration & Operations SYSTEMS

## Overview

This directory contains the SYSTEMS tree for Ground Integration & Operations (STA-L) of the AMPEL360-SPACE-T spacecraft product. The structure follows the unified architecture with 6 primary systems containing 24 total leaf subsystems, each with complete PLM/CAx engineering artifacts.

## Quick Navigation

### Systems Overview

| System ID | System Name | Subsystems | Interface Matrix |
|-----------|-------------|------------|------------------|
| **07** | [GSE_HANDLING_LIFTING](./07-GSE_HANDLING_LIFTING/) | 4 | [CSV](./07-GSE_HANDLING_LIFTING/INTERFACE_MATRIX/07↔06_15_21_24_26_40_42_51_93_97.csv) |
| **10** | [EGSE_POWER_COMMS](./10-EGSE_POWER_COMMS/) | 4 | [CSV](./10-EGSE_POWER_COMMS/INTERFACE_MATRIX/10↔15_24_33_40_42_93_97.csv) |
| **16** | [INTEGRATION_AND_TEST](./16-INTEGRATION_AND_TEST/) | 4 | [CSV](./16-INTEGRATION_AND_TEST/INTERFACE_MATRIX/16↔06_15_21_24_26_33_40_42_51_58_59_93_97.csv) |
| **32** | [EDL_LANDING_OPERATIONS](./32-EDL_LANDING_OPERATIONS/) | 4 | [CSV](./32-EDL_LANDING_OPERATIONS/INTERFACE_MATRIX/32↔06_15_21_24_26_33_40_41_42_51_58_93_97.csv) |
| **46** | [GROUND_MOC_INTERFACE](./46-GROUND_MOC_INTERFACE/) | 4 | [CSV](./46-GROUND_MOC_INTERFACE/INTERFACE_MATRIX/46↔06_10_15_23_24_33_40_41_42_90_93_97.csv) |
| **92** | [CALIBRATION_DATA_ARCHIVAL](./92-CALIBRATION_DATA_ARCHIVAL/) | 4 | [CSV](./92-CALIBRATION_DATA_ARCHIVAL/INTERFACE_MATRIX/92↔06_10_15_24_33_40_41_42_46_93_97.csv) |

### By Discipline

#### Ground Support Equipment (GSE)
- [07 - GSE Handling & Lifting](./07-GSE_HANDLING_LIFTING/) - Mechanical ground support, lifting, environmental protection
- [10 - EGSE Power & Communications](./10-EGSE_POWER_COMMS/) - Electrical ground support, power conditioning, signal simulation

#### Integration & Testing
- [16 - Integration and Test](./16-INTEGRATION_AND_TEST/) - Clean rooms, test infrastructure, anomaly resolution

#### Mission Operations
- [32 - EDL Landing Operations](./32-EDL_LANDING_OPERATIONS/) - Entry, descent, landing simulators and rehearsals
- [46 - Ground MOC Interface](./46-GROUND_MOC_INTERFACE/) - Mission Operations Center interface and command validation

#### Data Management
- [92 - Calibration Data Archival](./92-CALIBRATION_DATA_ARCHIVAL/) - Calibration database and long-term archival

## Directory Structure

```
SYSTEMS/
├─ README.md (this file)
└─ {SYSTEM_ID}-{SYSTEM_NAME}/
   ├─ README.md
   ├─ INTEGRATION_VIEW.md
   ├─ INTERFACE_MATRIX/
   │  └─ {ID}↔{OTHERS}.csv
   └─ SUBSYSTEMS/
      └─ {SYSTEM_ID}-{SUB_ID}_{SUBSYSTEM_NAME}/
         ├─ README.md
         └─ PLM/
            ├─ EBOM_LINKS.md
            └─ CAx/
               ├─ CAD/  (Computer-Aided Design)
               ├─ CAE/  (Computer-Aided Engineering)
               ├─ CAO/  (Computer-Aided Optimization)
               ├─ CAM/  (Computer-Aided Manufacturing)
               ├─ CAI/  (Computer-Aided Installation)
               ├─ CAV/  (Computer-Aided Validation)
               ├─ CAP/  (Computer-Aided Process Planning)
               ├─ CAS/  (Computer-Aided Simulation)
               └─ CMP/  (Composite Materials Processing)
```

## Architecture Rules

### Naming Conventions
- **Systems**: Use hyphens between ID and name: `XX-SYSTEM_NAME`
- **Subsystems**: Format `XX-YY_SUBSYSTEM_NAME` where:
  - `XX` = System ID (07, 10, 16, 32, 46, 92)
  - `YY` = Subsystem ID (10, 20, 30, 90)
  - Standard pattern: 10-20-30-90 for core-supporting-integration-operations

### PLM Structure (Leaf Rule)
Every leaf subsystem **must** contain:
- `PLM/EBOM_LINKS.md` - Engineering BOM references
- `PLM/CAx/` directory with all 9 subdirectories:
  - CAD, CAE, CAO, CAM, CAI, CAV, CAP, CAS, CMP

### Interface Management
- Each system has an `INTERFACE_MATRIX` directory
- CSV files define system-to-system interfaces
- Format: `XX↔YY_ZZ_...csv` showing all interfacing systems

## Working with This Structure

### For System Engineers
1. Navigate to your system directory (e.g., `07-GSE_HANDLING_LIFTING/`)
2. Review the `INTEGRATION_VIEW.md` for system overview
3. Check `INTERFACE_MATRIX/` for system interfaces
4. Access subsystems in `SUBSYSTEMS/` directory

### For Subsystem Engineers
1. Navigate to your subsystem (e.g., `07-GSE_HANDLING_LIFTING/SUBSYSTEMS/07-10_MGSE_MECHANICAL_HANDLING/`)
2. Review the subsystem `README.md` for scope and requirements
3. Access engineering artifacts in `PLM/CAx/` subdirectories
4. Update `PLM/EBOM_LINKS.md` for BOM references

### For PLM/Configuration Management
1. All engineering artifacts reside in subsystem-level `PLM/CAx/` directories
2. BOM links tracked in `PLM/EBOM_LINKS.md`
3. Interface definitions in system-level `INTERFACE_MATRIX/` CSVs
4. No PLM artifacts at system or domain level (validation enforced)

## Ground Operations Context

The STA-L domain covers:
- **MGSE/EGSE**: Mechanical and Electrical Ground Support Equipment
- **AIT**: Assembly, Integration, and Test infrastructure
- **Mission Ops**: Ground-to-spacecraft operations interfaces
- **Data Management**: Calibration data and long-term archival

These systems support spacecraft operations from integration through launch preparation, mission operations, and data archival.

## Validation

Structure compliance validated by:
- `scripts/validate-spacecraft-systems.sh` - Spacecraft-specific checks
- `00-PROGRAM/CONFIG_MGMT/12-CI/validate-structure.sh` - CI validation

Run validation:
```bash
cd /path/to/repository
bash scripts/validate-spacecraft-systems.sh
```

## Statistics

- **Total Systems**: 6
- **Total Subsystems**: 24 (4 per system)
- **Total CAx Directories**: 216 (24 × 9)
- **Interface Matrices**: 6
- **EBOM Link Files**: 24

## References

- [Domain README](../README.md)
- [Spacecraft Product README](../../README.md) (if exists)
- Configuration Management: `00-PROGRAM/CONFIG_MGMT/`
- Validation Scripts: `scripts/`
- STA-L Chapters: 07, 10, 16, 32, 46, 92

## Related Domains

- **STA-A**: Structures & Mechanisms (spacecraft hardware)
- **STA-B**: Thermal & TPS (thermal systems)
- **STA-C**: Power / EPS / Harness (electrical power)
- **STA-D**: Communications (RF/Optical & TT&C)
- **STA-M**: Program, Compliance & Records (documentation)

## Status

**Current Version**: Q10  
**Status**: Structure scaffolded - Ready for engineering artifact population  
**Last Updated**: 2025-10-10

---

For questions or issues with this structure, contact the ground operations integration team or refer to the validation scripts for compliance requirements.
