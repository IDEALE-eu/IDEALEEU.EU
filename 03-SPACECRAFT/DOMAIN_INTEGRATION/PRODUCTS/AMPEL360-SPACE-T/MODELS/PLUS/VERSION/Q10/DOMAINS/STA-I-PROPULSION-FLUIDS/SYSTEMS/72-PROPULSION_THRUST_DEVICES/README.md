# System 72: PROPULSION_THRUST_DEVICES

## Description

Main propulsion thrust devices including chemical thrusters, ignition systems, thermal protection, TVC mechanisms, and plume analysis.

## Quick Links

- [Integration View](./INTEGRATION_VIEW.md) - System overview and subsystem list
- [Interface Matrix](./INTERFACE_MATRIX/) - System-to-system interfaces
- [Subsystems Directory](./SUBSYSTEMS/) - All subsystems for this system

## Subsystems

- [72-40_CHEMICAL_THRUSTERS](./SUBSYSTEMS/72-40_CHEMICAL_THRUSTERS/) - Chemical thruster engines and combustion chambers.
- [72-50_IGNITION_SYSTEMS](./SUBSYSTEMS/72-50_IGNITION_SYSTEMS/) - Ignition and startup systems for thrusters.
- [72-60_THERMAL_PROTECTION](./SUBSYSTEMS/72-60_THERMAL_PROTECTION/) - Thermal protection systems for thrust devices.
- [72-70_TVC_MECHANISMS](./SUBSYSTEMS/72-70_TVC_MECHANISMS/) - Thrust Vector Control (TVC) mechanisms and actuators.
- [72-90_PLUME_ANALYSIS](./SUBSYSTEMS/72-90_PLUME_ANALYSIS/) - Exhaust plume analysis and characterization.

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
