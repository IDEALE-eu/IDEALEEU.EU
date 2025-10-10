# System 54: PROPULSION_STRUCTURES

## Description

Propulsion-specific structures including thrust device mounts and thermal shields.

**⚠️ Ownership Note:** See [REDIRECT.md](./REDIRECT.md) - System 54 may belong to STA-A (Structures) or STA-I (Propulsion-Fluids) depending on mission configuration.

## Quick Links

- [Integration View](./INTEGRATION_VIEW.md) - System overview and subsystem list
- [Redirect Note](./REDIRECT.md) - System ownership information
- [Interface Matrix](./INTERFACE_MATRIX/) - System-to-system interfaces
- [Subsystems Directory](./SUBSYSTEMS/) - All subsystems for this system

## Subsystems

- [54-40_THRUST_DEVICE_MOUNTS](./SUBSYSTEMS/54-40_THRUST_DEVICE_MOUNTS/) - Mounting structures for thrust devices and engines.
- [54-60_THERMAL_SHIELDS](./SUBSYSTEMS/54-60_THERMAL_SHIELDS/) - Thermal shields and protection for propulsion structures.

## Directory Structure

```
{SYSTEM}/
├─ README.md (this file)
├─ INTEGRATION_VIEW.md
├─ REDIRECT.md
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
2. Check [REDIRECT.md](./REDIRECT.md) for ownership coordination
3. Check [INTERFACE_MATRIX/](./INTERFACE_MATRIX/) for interfaces with other systems
4. Navigate to specific subsystems in [SUBSYSTEMS/](./SUBSYSTEMS/)

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
