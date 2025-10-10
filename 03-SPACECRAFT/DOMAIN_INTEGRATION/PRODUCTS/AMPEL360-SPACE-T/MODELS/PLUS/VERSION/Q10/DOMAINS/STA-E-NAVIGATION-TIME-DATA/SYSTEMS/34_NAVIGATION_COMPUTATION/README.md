# System 34: NAVIGATION_COMPUTATION

## Description

Navigation computation systems including Kalman filters, state propagation, reference frames, and fault detection for accurate position and attitude determination.

## Quick Links

- [Integration View](./INTEGRATION_VIEW.md) - System overview and subsystem list
- [Interface Matrix](./INTERFACE_MATRIX/) - System-to-system interfaces
- [Subsystems Directory](./SUBSYSTEMS/) - All subsystems for this system

## Subsystems

- [34-10_FILTERS_KALMAN_NAV](./SUBSYSTEMS/34-10_FILTERS_KALMAN_NAV/) - Kalman filters and navigation filters for state estimation and data fusion.
- [34-20_STATE_PROPAGATION_EPHEMERIDES](./SUBSYSTEMS/34-20_STATE_PROPAGATION_EPHEMERIDES/) - State propagation models and ephemerides computation for orbit and trajectory.
- [34-30_REFERENCE_FRAMES_TIME_MODELS](./SUBSYSTEMS/34-30_REFERENCE_FRAMES_TIME_MODELS/) - Reference frame transformations and time system models for navigation.
- [34-40_FDI_FDE_FAULT_HANDLING](./SUBSYSTEMS/34-40_FDI_FDE_FAULT_HANDLING/) - Fault detection, isolation, and exclusion for navigation system integrity.
- [34-60_ALGORITHMS_NAV](./SUBSYSTEMS/34-60_ALGORITHMS_NAV/) - Navigation algorithms for position, velocity, and attitude computation.
- [34-80_TESTING_VALIDATION](./SUBSYSTEMS/34-80_TESTING_VALIDATION/) - Testing procedures and validation methods for navigation computation.

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
- [📋 Main SYSTEMS README](../README.md)

---

**Status**: Structure scaffolded - Ready for engineering artifact population
