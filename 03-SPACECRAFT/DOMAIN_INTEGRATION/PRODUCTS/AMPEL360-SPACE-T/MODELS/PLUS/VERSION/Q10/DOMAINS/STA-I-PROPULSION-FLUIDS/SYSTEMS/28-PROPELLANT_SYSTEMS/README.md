# System 28: PROPELLANT_SYSTEMS

## Description

Propellant storage, pressurization, feed systems, thermal management, sequencing, and plume/EMC analysis.

## Quick Links

- [Integration View](./INTEGRATION_VIEW.md) - System overview and subsystem list
- [Interface Matrix](./INTERFACE_MATRIX/) - System-to-system interfaces
- [Subsystems Directory](./SUBSYSTEMS/) - All subsystems for this system

## Subsystems

- [28-10_TANKS_PMD](./SUBSYSTEMS/28-10_TANKS_PMD/) - Propellant tanks and Propellant Management Devices (PMD).
- [28-20_PRESSURIZATION_GAS](./SUBSYSTEMS/28-20_PRESSURIZATION_GAS/) - Pressurization and purge gas systems.
- [28-30_FEED_MANIFOLDS](./SUBSYSTEMS/28-30_FEED_MANIFOLDS/) - Feed lines, manifolds, and distribution systems.
- [28-60_THERMAL_MANAGEMENT](./SUBSYSTEMS/28-60_THERMAL_MANAGEMENT/) - Thermal management for propellant systems.
- [28-80_SEQUENCING_EVIDENCE](./SUBSYSTEMS/28-80_SEQUENCING_EVIDENCE/) - Sequencing control, ICDs, diagrams, and logs (CMP only).
- [28-90_PLUME_SAFETY_EMC](./SUBSYSTEMS/28-90_PLUME_SAFETY_EMC/) - Plume analysis, safety, and EMC considerations.

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
