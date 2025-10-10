# 45-FDIR_FAULT_PROTECTION — Integration View

## System Overview

**Description:** FDIR FAULT PROTECTION system for spacecraft control, autonomy, and fault protection.

**System ID:** 45  
**Interface Matrix:** [45↔06_15_21_24_31_33_34_40_41_42_48_93_97.csv](./INTERFACE_MATRIX/45↔06_15_21_24_31_33_34_40_41_42_48_93_97.csv)

## Purpose

This system provides integration and coordination for all FDIR_FAULT_PROTECTION subsystems within the AMPEL360-SPACE-T spacecraft.

## Quick Navigation

- [📋 System README](./README.md) - Detailed system documentation
- [🔗 Interface Matrix](./INTERFACE_MATRIX/) - System interface definitions
- [📂 Subsystems](./SUBSYSTEMS/) - Access all subsystems
- [🏠 Domain Home](../../README.md) - Return to STA-G-CONTROL-AUTONOMY-FDIR domain

## Subsystems

| ID | Subsystem | Description |
|----|-----------|-------------|
| 10 | [45-10_ARCHITECTURE_FDIR_STATES](./SUBSYSTEMS/45-10_ARCHITECTURE_FDIR_STATES/) | ARCHITECTURE FDIR STATES subsystem. |
| 20 | [45-20_DETECTION_ISOLATION_ALGORITHMS](./SUBSYSTEMS/45-20_DETECTION_ISOLATION_ALGORITHMS/) | DETECTION ISOLATION ALGORITHMS subsystem. |
| 30 | [45-30_RECOVERY_RECONFIGURATION_ACTUATION](./SUBSYSTEMS/45-30_RECOVERY_RECONFIGURATION_ACTUATION/) | RECOVERY RECONFIGURATION ACTUATION subsystem. |
| 40 | [45-40_RULES_TABLES_THRESHOLDS](./SUBSYSTEMS/45-40_RULES_TABLES_THRESHOLDS/) | RULES TABLES THRESHOLDS subsystem. |
| 50 | [45-50_HEALTH_CBM_DIAGNOSTICS](./SUBSYSTEMS/45-50_HEALTH_CBM_DIAGNOSTICS/) | HEALTH CBM DIAGNOSTICS subsystem. |
| 60 | [45-60_REDUNDANCY_CROSS_STRAP_LOGIC](./SUBSYSTEMS/45-60_REDUNDANCY_CROSS_STRAP_LOGIC/) | REDUNDANCY CROSS STRAP LOGIC subsystem. |
| 70 | [45-70_TRENDING_FAULT_METRICS](./SUBSYSTEMS/45-70_TRENDING_FAULT_METRICS/) | TRENDING FAULT METRICS subsystem. |
| 80 | [45-80_VERIFICATION_FAULT_INJECTION](./SUBSYSTEMS/45-80_VERIFICATION_FAULT_INJECTION/) | VERIFICATION FAULT INJECTION subsystem. |
| 90 | [45-90_OPERATIONS_LIMITS_INHIBITS](./SUBSYSTEMS/45-90_OPERATIONS_LIMITS_INHIBITS/) | OPERATIONS LIMITS INHIBITS subsystem. |

## System Interfaces

The [Interface Matrix](./INTERFACE_MATRIX/) directory contains CSV files defining interfaces with other systems.

## Documentation Structure

```
45-FDIR_FAULT_PROTECTION/
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
