# System 21: THERMAL_CONTROL

## System Overview

**Description:** Thermal management including radiators, MLI, heaters, TPS, and thermal control loops.

**System ID:** 21  
**Total Subsystems:** 8  
**Interface Matrix:** [21↔15_24_31_51_70_72_75_97.csv](./INTERFACE_MATRIX/21↔15_24_31_51_70_72_75_97.csv)

## Purpose

This system provides integration and coordination for all THERMAL_CONTROL subsystems within the AMPEL360-SPACE-T spacecraft. It serves as:

- **Integration Anchor**: Central coordination point for subsystem interfaces
- **Interface Definition**: Manages system-to-system interface requirements
- **Configuration Control**: Ensures subsystem compatibility and integration

## Quick Navigation

- [📋 System README](./README.md) - Detailed system documentation
- [🔗 Interface Matrix](./INTERFACE_MATRIX/) - System interface definitions
- [📂 Subsystems](./SUBSYSTEMS/) - Access all subsystems
- [🏠 Domain Home](../../README.md) - Return to STA-B-THERMAL-TPS domain

## Subsystems

| ID | Subsystem | Description |
|----|-----------|-------------|
| 10 | [21-10_RADIATORS_HEAT_EXCHANGERS](./SUBSYSTEMS/21-10_RADIATORS_HEAT_EXCHANGERS/) | Radiators and heat exchangers for heat rejection |
| 20 | [21-20_MLI](./SUBSYSTEMS/21-20_MLI/) | Multi-layer insulation blankets and thermal barriers |
| 30 | [21-30_HEATERS](./SUBSYSTEMS/21-30_HEATERS/) | Survival heaters and thermostatic controls |
| 40 | [21-40_PIPES_HEAT_STRAPS](./SUBSYSTEMS/21-40_PIPES_HEAT_STRAPS/) | Thermal pipes, heat straps, and fluid loops |
| 50 | [21-50_THERMAL_PROTECTION_SYSTEM](./SUBSYSTEMS/21-50_THERMAL_PROTECTION_SYSTEM/) | TPS for re-entry and high-temperature environments |
| 60 | [21-60_TEMPERATURE_SENSORS](./SUBSYSTEMS/21-60_TEMPERATURE_SENSORS/) | Temperature sensors and monitoring instrumentation |
| 70 | [21-70_THERMAL_ALGORITHMS](./SUBSYSTEMS/21-70_THERMAL_ALGORITHMS/) | Thermal control algorithms and software |
| 80 | [21-80_TVAC_TESTING](./SUBSYSTEMS/21-80_TVAC_TESTING/) | Thermal vacuum testing and validation |

## System Interfaces

The [Interface Matrix](./INTERFACE_MATRIX/) directory contains CSV files defining interfaces with other systems:

- Interface requirements and specifications
- Physical interfaces (mechanical, electrical)
- Functional interfaces (data, commands)
- Verification and validation approach

### Key System Interfaces

- **15 - Environment/Vibration**: Thermal environment characterization
- **24 - Electrical Power**: Heater power supply, sensor power
- **31 - Data Handling**: Temperature data acquisition and processing
- **51 - Structures**: Thermal mounting interfaces, heat paths
- **70 - Thermal Algorithms**: Software control interfaces
- **72 - Avionics Cooling**: Equipment cooling requirements
- **75 - Fluid Systems**: Coolant loops and thermal management
- **97 - Harness**: Sensor wiring and heater power distribution

### Interface Management Process

1. **Define**: Document interface requirements in CSV format
2. **Review**: Coordinate with interfacing system teams
3. **Implement**: Develop interface control documents (ICDs)
4. **Verify**: Validate interfaces during integration testing

## Integration Workflow

### For System Engineers

1. **Planning Phase**
   - Review subsystem requirements
   - Define system-level interfaces
   - Develop thermal integration sequence

2. **Implementation Phase**
   - Coordinate subsystem development
   - Manage interface definitions
   - Track integration readiness

3. **Verification Phase**
   - Verify system-level thermal requirements
   - Validate interface compliance
   - Conduct TVAC testing

### For Subsystem Engineers

1. **Access Your Subsystem**
   - Navigate to `SUBSYSTEMS/{YOUR_SUBSYSTEM}/`
   - Review subsystem README for requirements

2. **Develop Artifacts**
   - Place engineering files in `PLM/CAx/` subdirectories
   - Update `PLM/EBOM_LINKS.md` for BOM references

3. **Interface Coordination**
   - Review interface matrix for your subsystem
   - Coordinate with interfacing subsystems
   - Update ICDs as needed

## Documentation Structure

```
21-THERMAL_CONTROL/
├─ README.md                    # Detailed system documentation
├─ INTEGRATION_VIEW.md          # This file - integration overview
├─ INTERFACE_MATRIX/            # System interface definitions
│  └─ 21↔15_24_31_51_70_72_75_97.csv
└─ SUBSYSTEMS/                  # All subsystems for this system
   └─ {SUBSYSTEM}/
      ├─ README.md              # Subsystem documentation
      └─ PLM/                   # Engineering artifacts
         ├─ EBOM_LINKS.md       # BOM references
         └─ CAx/                # CAx artifacts by discipline
            ├─ CAD/             # (or DATA for non-geometric)
            ├─ CAE/
            ├─ CAM/
            ├─ CAI/
            ├─ CAV/
            ├─ CAP/
            ├─ CAS/
            └─ CMP/
```

## Configuration Management

### Change Control

- All interface changes require CCB approval
- Update interface matrix CSV files for changes
- Coordinate with affected subsystems
- Update ICDs and trace to requirements

### Baseline Management

- System baselines established per program milestones
- Subsystem PLM artifacts tracked in ERP/PLM system
- Interface definitions under configuration control

## References

- [Domain README](../../README.md)
- Configuration Management: `00-PROGRAM/CONFIG_MGMT/`
- Validation: `scripts/validate-spacecraft-systems.sh`
- Interface Requirements: See `INTERFACE_MATRIX/*.csv`

---

**Status**: Structure ready for subsystem population  
**Integration Lead**: TBD  
**Last Updated**: 2025-10-10
