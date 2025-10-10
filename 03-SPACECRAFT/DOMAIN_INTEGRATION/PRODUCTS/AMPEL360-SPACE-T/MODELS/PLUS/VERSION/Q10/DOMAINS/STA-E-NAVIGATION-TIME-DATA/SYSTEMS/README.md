# AMPEL360-SPACE-T SYSTEMS Architecture

**Domain:** STA-E-NAVIGATION-TIME-DATA  
**Product:** AMPEL360-SPACE-T  
**Model:** PLUS  
**Version:** Q10

## Overview

This directory contains the system-level architecture for Navigation, Time, and Data systems organized according to the spacecraft chapter numbering convention.

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
               ├─ CAI/  (Computer-Aided Inspection)
               ├─ CAV/  (Computer-Aided Validation)
               ├─ CAP/  (Computer-Aided Planning)
               ├─ CAS/  (Computer-Aided Simulation)
               └─ CMP/  (Computer-Aided Modeling/Programming)
```

## Architecture Rules

### PLM/CAx Location
- PLM/CAx directories **ONLY** exist at SUBSYSTEM level
- Systems contain INTEGRATION_VIEW and INTERFACE_MATRIX
- Domain level contains configuration and standards

### Interface Management
- Each system has an `INTERFACE_MATRIX` directory
- CSV files define system-to-system interfaces
- Format: `XX↔YY_ZZ_...csv` showing all interfacing systems

### Naming Convention
- Systems: `{ID}_{NAME}` (e.g., `31_NAV_SENSORS`)
- Subsystems: `{SYSTEM_ID}-{SUB_ID}_{NAME}` (e.g., `31-10_IMUS_GYROS_ACCELS`)
- Use underscores for multi-word names
- Use uppercase for consistency

## Quick Navigation

### Systems Overview

| System | Name | Subsystems | Interface Matrix |
|--------|------|------------|------------------|
| **31** | [NAV_SENSORS](./31_NAV_SENSORS/) | 7 | [CSV](./31_NAV_SENSORS/INTERFACE_MATRIX/31↔06_15_21_23_24_42_51_97.csv) |
| **34** | [NAVIGATION_COMPUTATION](./34_NAVIGATION_COMPUTATION/) | 6 | [CSV](./34_NAVIGATION_COMPUTATION/INTERFACE_MATRIX/34↔06_15_21_23_24_31_42_51_97.csv) |
| **41** | [TIME_SYNCHRONIZATION](./41_TIME_SYNCHRONIZATION/) | 6 | [CSV](./41_TIME_SYNCHRONIZATION/INTERFACE_MATRIX/41↔06_15_21_23_24_31_34_42_51_97.csv) |

## Working with Systems

### For System Engineers
1. Navigate to your system directory
2. Review `INTEGRATION_VIEW.md` for system scope and subsystems
3. Check `INTERFACE_MATRIX/*.csv` for interfaces with other systems
4. Coordinate subsystem integration activities

### For Subsystem Engineers
1. Access your subsystem in `{SYSTEM}/SUBSYSTEMS/{SUBSYSTEM}/`
2. Review subsystem README for requirements
3. Place engineering artifacts in `PLM/CAx/` subdirectories
4. Update `PLM/EBOM_LINKS.md` for BOM references

### For Configuration Management
- Interface definitions tracked in `INTERFACE_MATRIX/*.csv`
- Engineering BOMs in `SUBSYSTEMS/*/PLM/EBOM_LINKS.md`
- CAx artifacts organized by discipline in `SUBSYSTEMS/*/PLM/CAx/*`

## Domain Context

This SYSTEMS directory is part of the STA-E-NAVIGATION-TIME-DATA domain which covers:

**Chapters:** 31, 34, 41

**Subsections:**
- 10 Navigation Sensors
- 20 Timing
- 30 C&DH/Recording
- 40 Input/Output
- 50 Processing/Storage
- 60 Telemetry Parameters
- 70 FDIR Hooks
- 80 HIL/SIL
- 90 Security/Hardening

## References

- [Domain README](../README.md) - Domain-level overview and rules
- [Main Program](../../../../../../../../../../00-PROGRAM/) - Program-level documentation
- Validation: `scripts/validate-structure.sh`

---

**Status**: Structure scaffolded - Ready for engineering artifact population  
**Last Updated**: 2025-10-10
