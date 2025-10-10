# AMPEL360-SPACE-T SYSTEMS Architecture

## Overview

This directory contains the flat SYSTEMS tree for the AMPEL360-SPACE-T spacecraft product. The structure follows the unified architecture with 10 primary systems containing 99 total leaf subsystems, each with complete PLM/CAx engineering artifacts.

## Quick Navigation

### Systems Overview

| System ID | System Name | Subsystems | Interface Matrix |
|-----------|-------------|------------|------------------|
| **06** | [DIMENSIONS_ALIGNMENTS](./06_DIMENSIONS_ALIGNMENTS/) | 10 | [CSV](./06_DIMENSIONS_ALIGNMENTS/INTERFACE_MATRIX/06↔51_53_55_57_66_94.csv) |
| **50** | [PAYLOAD_STRUCTURES](./50_PAYLOAD_STRUCTURES/) | 10 | [CSV](./50_PAYLOAD_STRUCTURES/INTERFACE_MATRIX/50↔06_51_53_57_66_94.csv) |
| **51** | [PRIMARY_STRUCTURE](./51_PRIMARY_STRUCTURE/) | 9 | [CSV](./51_PRIMARY_STRUCTURE/INTERFACE_MATRIX/51↔06_50_53_57_66_94.csv) |
| **52** | [DOORS_HATCHES](./52_DOORS_HATCHES/) | 10 | [CSV](./52_DOORS_HATCHES/INTERFACE_MATRIX/52↔50_53_66_94.csv) |
| **53** | [STRUCTURAL_BODY](./53_STRUCTURAL_BODY/) | 10 | [CSV](./53_STRUCTURAL_BODY/INTERFACE_MATRIX/53↔06_50_52_55_57_66_94.csv) |
| **55** | [ADCS_STRUCTURES](./55_ADCS_STRUCTURES/) | 10 | [CSV](./55_ADCS_STRUCTURES/INTERFACE_MATRIX/55↔06_53_57_66_94.csv) |
| **56** | [WINDOWS](./56_WINDOWS/) | 10 | [CSV](./56_WINDOWS/INTERFACE_MATRIX/56↔50_53_55_66_94.csv) |
| **57** | [SOLAR_ARRAYS](./57_SOLAR_ARRAYS/) | 10 | [CSV](./57_SOLAR_ARRAYS/INTERFACE_MATRIX/57↔51_53_55_66_94.csv) |
| **66** | [MECHANISMS](./66_MECHANISMS/) | 10 | [CSV](./66_MECHANISMS/INTERFACE_MATRIX/66↔50_52_53_55_57_94.csv) |
| **94** | [QUALIFICATION_ACCEPTANCE](./94_QUALIFICATION_ACCEPTANCE/) | 10 | [CSV](./94_QUALIFICATION_ACCEPTANCE/INTERFACE_MATRIX/94↔06_50_51_52_53_55_56_57_66.csv) |

### By Discipline

#### Structural Systems
- [06 - Dimensions & Alignments](./06_DIMENSIONS_ALIGNMENTS/)
- [50 - Payload Structures](./50_PAYLOAD_STRUCTURES/)
- [51 - Primary Structure](./51_PRIMARY_STRUCTURE/)
- [52 - Doors & Hatches](./52_DOORS_HATCHES/)
- [53 - Structural Body](./53_STRUCTURAL_BODY/)

#### ADCS & Mechanisms
- [55 - ADCS Structures](./55_ADCS_STRUCTURES/)
- [66 - Mechanisms](./66_MECHANISMS/)

#### Power & Optics
- [56 - Windows](./56_WINDOWS/)
- [57 - Solar Arrays](./57_SOLAR_ARRAYS/)

#### Qualification
- [94 - Qualification & Acceptance](./94_QUALIFICATION_ACCEPTANCE/)

## Directory Structure

```
SYSTEMS/
├─ README.md (this file)
└─ {SYSTEM_ID}_{SYSTEM_NAME}/
   ├─ README.md
   ├─ INTEGRATION_VIEW.md
   ├─ INTERFACE_MATRIX/
   │  └─ {ID}↔{OTHERS}.csv
   └─ SUBSYSTEMS/
      └─ {SYSTEM_ID}_{SUB_ID}_{SUBSYSTEM_NAME}/
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
               ├─ CAS/  (Computer-Aided Simulation)
               └─ CMP/  (Composite Materials Processing)
```

## Architecture Rules

### Naming Conventions
- **Systems**: Use underscores only (no hyphens): `XX_SYSTEM_NAME`
- **Subsystems**: Format `XX_YY_SUBSYSTEM_NAME` where:
  - `XX` = System ID (06, 50, 51, etc.)
  - `YY` = Subsystem ID (00, 10, 20, etc.)
  - Increments of 10 for future expansion

### PLM Structure (Leaf Rule)
Every leaf subsystem **must** contain:
- `PLM/EBOM_LINKS.md` - Engineering BOM references
- `PLM/CAx/` directory with all 8 subdirectories:
  - CAD, CAE, CAO, CAM, CAI, CAV, CAS, CMP

### Interface Management
- Each system has an `INTERFACE_MATRIX` directory
- CSV files define system-to-system interfaces
- Format: `XX↔YY_ZZ_...csv` showing all interfacing systems

## Working with This Structure

### For System Engineers
1. Navigate to your system directory (e.g., `06_DIMENSIONS_ALIGNMENTS/`)
2. Review the `INTEGRATION_VIEW.md` for system overview
3. Check `INTERFACE_MATRIX/` for system interfaces
4. Access subsystems in `SUBSYSTEMS/` directory

### For Subsystem Engineers
1. Navigate to your subsystem (e.g., `06_DIMENSIONS_ALIGNMENTS/SUBSYSTEMS/06_10_REFERENCE_FRAMES/`)
2. Review the subsystem `README.md` for scope and requirements
3. Access engineering artifacts in `PLM/CAx/` subdirectories
4. Update `PLM/EBOM_LINKS.md` for BOM references

### For PLM/Configuration Management
1. All engineering artifacts reside in subsystem-level `PLM/CAx/` directories
2. BOM links tracked in `PLM/EBOM_LINKS.md`
3. Interface definitions in system-level `INTERFACE_MATRIX/` CSVs
4. No PLM artifacts at system or domain level (validation enforced)

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

- **Total Systems**: 10
- **Total Subsystems**: 99
- **Total CAx Directories**: 792 (99 × 8)
- **Interface Matrices**: 10
- **EBOM Link Files**: 99

## References

- [Spacecraft Product README](../../README.md) (if exists)
- [Domain Integration README](../../../../../00-README.md)
- Configuration Management: `00-PROGRAM/CONFIG_MGMT/`
- Validation Scripts: `scripts/`

## Status

**Current Version**: Q10  
**Status**: Structure scaffolded - Ready for engineering artifact population  
**Last Updated**: 2025-10-10

---

For questions or issues with this structure, contact the spacecraft systems integration team or refer to the validation scripts for compliance requirements.
