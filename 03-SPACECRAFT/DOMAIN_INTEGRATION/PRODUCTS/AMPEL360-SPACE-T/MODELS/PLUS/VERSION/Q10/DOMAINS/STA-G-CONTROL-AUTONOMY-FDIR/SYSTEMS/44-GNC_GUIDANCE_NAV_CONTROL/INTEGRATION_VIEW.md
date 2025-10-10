# 44-GNC_GUIDANCE_NAV_CONTROL — Integration View

## System Overview

**Description:** GNC GUIDANCE NAV CONTROL system for spacecraft control, autonomy, and fault protection.

**System ID:** 44  
**Interface Matrix:** [44↔06_15_21_24_31_33_34_40_41_42_48_93_97.csv](./INTERFACE_MATRIX/44↔06_15_21_24_31_33_34_40_41_42_48_93_97.csv)

## Purpose

This system provides integration and coordination for all GNC_GUIDANCE_NAV_CONTROL subsystems within the AMPEL360-SPACE-T spacecraft.

## Quick Navigation

- [📋 System README](./README.md) - Detailed system documentation
- [🔗 Interface Matrix](./INTERFACE_MATRIX/) - System interface definitions
- [📂 Subsystems](./SUBSYSTEMS/) - Access all subsystems
- [🏠 Domain Home](../../README.md) - Return to STA-G-CONTROL-AUTONOMY-FDIR domain

## Subsystems

| ID | Subsystem | Description |
|----|-----------|-------------|
| 10 | [44-10_FUNCTIONAL_ARCHITECTURE_GNC](./SUBSYSTEMS/44-10_FUNCTIONAL_ARCHITECTURE_GNC/) | FUNCTIONAL ARCHITECTURE GNC subsystem. |
| 20 | [44-20_ESTIMATION_NAV_FILTERS](./SUBSYSTEMS/44-20_ESTIMATION_NAV_FILTERS/) | ESTIMATION NAV FILTERS subsystem. |
| 30 | [44-30_CONTROL_LAWS_ACTUATION_ALLOCATION](./SUBSYSTEMS/44-30_CONTROL_LAWS_ACTUATION_ALLOCATION/) | CONTROL LAWS ACTUATION ALLOCATION subsystem. |
| 40 | [44-40_FDIR_HOOKS_LIMITS](./SUBSYSTEMS/44-40_FDIR_HOOKS_LIMITS/) | FDIR HOOKS LIMITS subsystem. |
| 50 | [44-50_HEALTH_CBM_GNC_PERFORMANCE](./SUBSYSTEMS/44-50_HEALTH_CBM_GNC_PERFORMANCE/) | HEALTH CBM GNC PERFORMANCE subsystem. |
| 60 | [44-60_REDUNDANCY_SENSORS_ACTUATORS](./SUBSYSTEMS/44-60_REDUNDANCY_SENSORS_ACTUATORS/) | REDUNDANCY SENSORS ACTUATORS subsystem. |
| 70 | [44-70_TRENDING_STATES_RESIDUALS](./SUBSYSTEMS/44-70_TRENDING_STATES_RESIDUALS/) | TRENDING STATES RESIDUALS subsystem. |
| 80 | [44-80_CLOSED_LOOP_VERIF_HIL_SIL](./SUBSYSTEMS/44-80_CLOSED_LOOP_VERIF_HIL_SIL/) | CLOSED LOOP VERIF HIL SIL subsystem. |
| 90 | [44-90_OPERATIONS_LIMITS_GNC](./SUBSYSTEMS/44-90_OPERATIONS_LIMITS_GNC/) | OPERATIONS LIMITS GNC subsystem. |

## System Interfaces

The [Interface Matrix](./INTERFACE_MATRIX/) directory contains CSV files defining interfaces with other systems.

## Documentation Structure

```
44-GNC_GUIDANCE_NAV_CONTROL/
├─ INTEGRATION_VIEW.md          # This file - integration overview
├─ INTERFACE_MATRIX/            # System interface definitions
│  └─ *.csv                     # Interface requirement CSVs
└─ SUBSYSTEMS/                  # All subsystems for this system
   └─ {SUBSYSTEM}/
      └─ PLM/                   # Engineering artifacts
         ├─ EBOM_LINKS.md       # BOM references
         └─ CAx/                # CAx artifacts by discipline
            ├─ CAD/
            ├─ CAE/
            ├─ CAM/
            ├─ CAI/
            ├─ CAV/
            ├─ CAP/
            ├─ CAS/
            └─ CMP/
```

## Configuration Management

- All interface changes require CCB approval
- PLM artifacts tracked in ERP/PLM system
- Interface definitions under configuration control

## References

- [Domain README](../../README.md)
- Configuration Management: `00-PROGRAM/CONFIG_MGMT/`

---

**Status**: Structure ready for subsystem population  
**Last Updated**: 2025-10-10
