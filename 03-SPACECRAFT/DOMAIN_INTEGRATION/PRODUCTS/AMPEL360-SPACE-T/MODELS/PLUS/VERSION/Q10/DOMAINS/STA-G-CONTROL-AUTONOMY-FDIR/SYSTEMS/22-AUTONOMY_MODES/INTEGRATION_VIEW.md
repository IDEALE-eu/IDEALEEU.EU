# 22-AUTONOMY_MODES — Integration View

## System Overview

**Description:** AUTONOMY MODES system for spacecraft control, autonomy, and fault protection.

**System ID:** 22  
**Interface Matrix:** [22↔06_15_21_24_31_34_40_41_42_93_97.csv](./INTERFACE_MATRIX/22↔06_15_21_24_31_34_40_41_42_93_97.csv)

## Purpose

This system provides integration and coordination for all AUTONOMY_MODES subsystems within the AMPEL360-SPACE-T spacecraft.

## Quick Navigation

- [📋 System README](./README.md) - Detailed system documentation
- [🔗 Interface Matrix](./INTERFACE_MATRIX/) - System interface definitions
- [📂 Subsystems](./SUBSYSTEMS/) - Access all subsystems
- [🏠 Domain Home](../../README.md) - Return to STA-G-CONTROL-AUTONOMY-FDIR domain

## Subsystems

| ID | Subsystem | Description |
|----|-----------|-------------|
| 10 | [22-10_MODE_ARCHITECTURE_AUTOMATA](./SUBSYSTEMS/22-10_MODE_ARCHITECTURE_AUTOMATA/) | MODE ARCHITECTURE AUTOMATA subsystem. |
| 20 | [22-20_MODE_TRANSITIONS_SAFING](./SUBSYSTEMS/22-20_MODE_TRANSITIONS_SAFING/) | MODE TRANSITIONS SAFING subsystem. |
| 30 | [22-30_COMMAND_ROUTING_TO_ACTUATORS](./SUBSYSTEMS/22-30_COMMAND_ROUTING_TO_ACTUATORS/) | COMMAND ROUTING TO ACTUATORS subsystem. |
| 40 | [22-40_POLICY_RULES_IF_TO_FDIR](./SUBSYSTEMS/22-40_POLICY_RULES_IF_TO_FDIR/) | POLICY RULES IF TO FDIR subsystem. |
| 50 | [22-50_HEALTH_CBM_AUTONOMY_MONITORS](./SUBSYSTEMS/22-50_HEALTH_CBM_AUTONOMY_MONITORS/) | HEALTH CBM AUTONOMY MONITORS subsystem. |
| 60 | [22-60_REDUNDANCY_VOTING_POLICIES](./SUBSYSTEMS/22-60_REDUNDANCY_VOTING_POLICIES/) | REDUNDANCY VOTING POLICIES subsystem. |
| 70 | [22-70_TRENDING_KPIS_AUTONOMY](./SUBSYSTEMS/22-70_TRENDING_KPIS_AUTONOMY/) | TRENDING KPIS AUTONOMY subsystem. |
| 80 | [22-80_CLOSED_LOOP_VV_MISSION_SIM](./SUBSYSTEMS/22-80_CLOSED_LOOP_VV_MISSION_SIM/) | CLOSED LOOP VV MISSION SIM subsystem. |
| 90 | [22-90_OPERATIONS_LIMITS_MODES](./SUBSYSTEMS/22-90_OPERATIONS_LIMITS_MODES/) | OPERATIONS LIMITS MODES subsystem. |

## System Interfaces

The [Interface Matrix](./INTERFACE_MATRIX/) directory contains CSV files defining interfaces with other systems.

## Documentation Structure

```
22-AUTONOMY_MODES/
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
