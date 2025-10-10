# System 66: MECHANISMS

## Description

Release devices, hinges, bearings, deployable mechanisms, and associated actuation systems.

## Quick Links

- [Integration View](./INTEGRATION_VIEW.md) - System overview and subsystem list
- [Interface Matrix](./INTERFACE_MATRIX/) - System-to-system interfaces
- [Subsystems Directory](./SUBSYSTEMS/) - All subsystems for this system

## Subsystems

- [66_00_MECHANISMS_GENERAL](./SUBSYSTEMS/66_00_MECHANISMS_GENERAL/) - General requirements and standards for mechanism systems.
- [66_10_RELEASE_DEVICES_HDRM](./SUBSYSTEMS/66_10_RELEASE_DEVICES_HDRM/) - Release devices including HDRM and separation mechanisms.
- [66_20_HINGES_BEARINGS_GUIDES](./SUBSYSTEMS/66_20_HINGES_BEARINGS_GUIDES/) - Hinges, bearings, and guide systems for articulation.
- [66_30_COVERS_SHROUDS](./SUBSYSTEMS/66_30_COVERS_SHROUDS/) - Covers and shrouds for mechanism protection.
- [66_40_LINKAGES_ACTUATION](./SUBSYSTEMS/66_40_LINKAGES_ACTUATION/) - Linkages and actuation systems for mechanism operation.
- [66_50_DEPLOYABLES_MASTS_BOOMS](./SUBSYSTEMS/66_50_DEPLOYABLES_MASTS_BOOMS/) - Deployable structures including masts and booms.
- [66_60_ALIGNMENT_FUNCTIONAL](./SUBSYSTEMS/66_60_ALIGNMENT_FUNCTIONAL/) - Alignment verification and functional positioning.
- [66_70_MATERIALS_LUBRICATION_TRIBOLOGY](./SUBSYSTEMS/66_70_MATERIALS_LUBRICATION_TRIBOLOGY/) - Materials, lubrication, and tribology for mechanisms.
- [66_80_NDI_FUNCTIONAL_INSPECTION](./SUBSYSTEMS/66_80_NDI_FUNCTIONAL_INSPECTION/) - NDI and functional inspection of mechanism assemblies.
- [66_90_QUALIFICATION_ACCEPTANCE](./SUBSYSTEMS/66_90_QUALIFICATION_ACCEPTANCE/) - Qualification testing and acceptance for mechanisms.

## Directory Structure

```
{SYSTEM}/
├─ README.md (this file)
├─ INTEGRATION_VIEW.md
├─ INTERFACE_MATRIX/
│  └─ *.csv
└─ SUBSYSTEMS/
   └─ {SUBSYSTEM}/
      ├─ README.md
      └─ PLM/
         ├─ EBOM_LINKS.md
         └─ CAx/
            ├─ CAD/
            ├─ CAE/
            ├─ CAO/
            ├─ CAM/
            ├─ CAI/
            ├─ CAV/
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
- [📋 Main SYSTEMS README](../README.md)

---

**Status**: Structure scaffolded - Ready for engineering artifact population
