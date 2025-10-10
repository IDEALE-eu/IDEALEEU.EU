# System 24: ELECTRICAL_POWER

## Description

Electrical Power System (EPS) providing generation, conditioning, distribution, storage, and protection of electrical power for the spacecraft.

## Quick Links

- [Integration View](./INTEGRATION_VIEW.md) - System overview and subsystem list
- [Interface Matrix](./INTERFACE_MATRIX/) - System-to-system interfaces
- [Subsystems Directory](./SUBSYSTEMS/) - All subsystems for this system

## Subsystems

- [24-10_POWER_GENERATION](./SUBSYSTEMS/24-10_POWER_GENERATION/) - Solar arrays and primary power generation
- [24-20_POWER_CONDITIONING](./SUBSYSTEMS/24-20_POWER_CONDITIONING/) - Voltage regulation and power conditioning
- [24-30_POWER_DISTRIBUTION](./SUBSYSTEMS/24-30_POWER_DISTRIBUTION/) - Power bus management and distribution
- [24-40_ENERGY_STORAGE](./SUBSYSTEMS/24-40_ENERGY_STORAGE/) - Battery systems and energy storage
- [24-50_PROTECTION_FUSES_BREAKERS](./SUBSYSTEMS/24-50_PROTECTION_FUSES_BREAKERS/) - Overcurrent protection and circuit breakers
- [24-60_CONVERTERS_DCDC_ACDC](./SUBSYSTEMS/24-60_CONVERTERS_DCDC_ACDC/) - DC-DC and AC-DC power converters
- [24-70_ALGORITHMS_CONTROL](./SUBSYSTEMS/24-70_ALGORITHMS_CONTROL/) - Power management algorithms and control software
- [24-80_TESTING_QUALIFICATION](./SUBSYSTEMS/24-80_TESTING_QUALIFICATION/) - EPS testing and qualification procedures

## Directory Structure

```
24-ELECTRICAL_POWER/
├─ README.md (this file)
├─ INTEGRATION_VIEW.md
├─ INTERFACE_MATRIX/
│  └─ 24↔06_15_31_42_51_57_97.csv
└─ SUBSYSTEMS/
   └─ 24-XX_SUBSYSTEM/
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
