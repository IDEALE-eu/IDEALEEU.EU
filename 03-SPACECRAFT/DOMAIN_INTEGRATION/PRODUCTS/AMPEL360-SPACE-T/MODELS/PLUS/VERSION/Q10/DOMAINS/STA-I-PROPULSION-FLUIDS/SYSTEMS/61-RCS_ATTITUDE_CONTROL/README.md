# System 61: RCS_ATTITUDE_CONTROL

## Description

Reaction Control System (RCS) for attitude control including thruster modules, feed routing, and safety/isolation systems.

## Quick Links

- [Integration View](./INTEGRATION_VIEW.md) - System overview and subsystem list
- [Interface Matrix](./INTERFACE_MATRIX/) - System-to-system interfaces
- [Subsystems Directory](./SUBSYSTEMS/) - All subsystems for this system

## Subsystems

- [61-10_THRUSTER_MODULES](./SUBSYSTEMS/61-10_THRUSTER_MODULES/) - RCS thruster modules and assemblies.
- [61-30_FEED_ROUTING](./SUBSYSTEMS/61-30_FEED_ROUTING/) - Propellant feed routing and distribution to RCS thrusters.
- [61-90_SAFETY_ISOLATION](./SUBSYSTEMS/61-90_SAFETY_ISOLATION/) - Safety valves and isolation systems for RCS.

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
