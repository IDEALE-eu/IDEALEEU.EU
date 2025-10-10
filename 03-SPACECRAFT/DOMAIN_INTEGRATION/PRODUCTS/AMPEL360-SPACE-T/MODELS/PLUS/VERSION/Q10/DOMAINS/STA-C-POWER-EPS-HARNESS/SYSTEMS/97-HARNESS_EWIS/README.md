# System 97: HARNESS_EWIS

## Description

Harness/EWIS (Electrical Wiring Interconnection System) providing all electrical wiring, cables, connectors, and associated hardware for spacecraft electrical connectivity.

## Quick Links

- [Integration View](./INTEGRATION_VIEW.md) - System overview and subsystem list
- [Interface Matrix](./INTERFACE_MATRIX/) - System-to-system interfaces
- [Subsystems Directory](./SUBSYSTEMS/) - All subsystems for this system

## Subsystems

- [97-10_MAIN_HARNESS_BACKBONE](./SUBSYSTEMS/97-10_MAIN_HARNESS_BACKBONE/) - Primary cable runs and trunk lines
- [97-20_BRANCH_LOOMS_SUBHARNESSES](./SUBSYSTEMS/97-20_BRANCH_LOOMS_SUBHARNESSES/) - Secondary distribution and branch circuits
- [97-30_CONNECTORS_TERMINALS_CONTACTS](./SUBSYSTEMS/97-30_CONNECTORS_TERMINALS_CONTACTS/) - All electrical connectors and terminations
- [97-40_EMI_EMC_SHIELDING_BONDING](./SUBSYSTEMS/97-40_EMI_EMC_SHIELDING_BONDING/) - Electromagnetic interference protection
- [97-50_CLAMPS_BRACKETS_STRESS_RELIEF](./SUBSYSTEMS/97-50_CLAMPS_BRACKETS_STRESS_RELIEF/) - Cable support and retention hardware
- [97-60_LABELING_MARKING_CONFIGURATION](./SUBSYSTEMS/97-60_LABELING_MARKING_CONFIGURATION/) - Wire identification and configuration management
- [97-70_SCHEMATICS_ROUTING_INSTALLATION](./SUBSYSTEMS/97-70_SCHEMATICS_ROUTING_INSTALLATION/) - Wiring diagrams and installation drawings
- [97-80_TESTING_CONTINUITY_HIPOT](./SUBSYSTEMS/97-80_TESTING_CONTINUITY_HIPOT/) - Electrical testing and qualification procedures

## Directory Structure

```
97-HARNESS_EWIS/
├─ README.md (this file)
├─ INTEGRATION_VIEW.md
├─ INTERFACE_MATRIX/
│  └─ 97↔06_15_24_31_39_42_51_57.csv
└─ SUBSYSTEMS/
   └─ 97-XX_SUBSYSTEM/
      └─ PLM/
         ├─ EBOM_LINKS.md
         └─ CAx/
            ├─ README.md
            ├─ CAD/
            ├─ CAE/
            ├─ CAM/
            ├─ CAI/
            ├─ CAV/
            ├─ CAP/
            ├─ CAS/
            └─ CMP/
```

## Working with This System

### System Engineers
1. Review [INTEGRATION_VIEW.md](./INTEGRATION_VIEW.md) for system scope
2. Check [INTERFACE_MATRIX/](./INTERFACE_MATRIX/) for interfaces with other systems
3. Navigate to specific subsystems in [SUBSYSTEMS/](./SUBSYSTEMS/)

### Subsystem Engineers
1. Access your subsystem directory under `SUBSYSTEMS/`
2. Review subsystem README for specific requirements
3. Place engineering artifacts in `PLM/CAx/` subdirectories
4. Update `PLM/EBOM_LINKS.md` for BOM references

### Configuration Management
- Interface definitions in `INTERFACE_MATRIX/*.csv`
- Engineering BOMs in `SUBSYSTEMS/*/PLM/EBOM_LINKS.md`
- CAx artifacts in `SUBSYSTEMS/*/PLM/CAx/*`

## Navigation

- [⬆️ Back to SYSTEMS](../)
- [📋 Domain README](../../README.md)

---

**Status**: Structure scaffolded - Ready for engineering artifact population
