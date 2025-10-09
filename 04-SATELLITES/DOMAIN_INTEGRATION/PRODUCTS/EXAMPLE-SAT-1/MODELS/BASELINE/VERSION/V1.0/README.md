# EXAMPLE-SAT-1 - BASELINE (V1.0)

STA-aligned satellite system structure following ECSS standards.

## Mission Overview
Mission: **EXAMPLE-SAT-1**
Configuration: **BASELINE**
Version: **V1.0**

## Structure
This directory contains all systems for the satellite organized according to SPACE-T (STA) architecture:

```
SYSTEMS/
├─ 01-INTRO/                     # Mission overview and CONOPS
├─ 06-DIMENSIONS_ALIGNMENTS/     # Reference frames and alignments
├─ 15-ENVIRONMENT_VIBRATION/     # Environmental specifications
├─ 21-THERMAL_CONTROL/           # Thermal management
├─ 23-COMMS_TT&C_RF_OPTICAL/     # Communications
├─ 24-ELECTRICAL_POWER_EPS/      # Power generation and distribution
├─ 28-PROPELLANT_SYSTEMS/        # Propellant storage and feed
├─ 29-PRESSURIZATION_PURGE/      # Pressurization systems
├─ 31-DATA_HANDLING_CDH/         # Command and data handling
├─ 34-NAVIGATION_ATTITUDE/       # GNC systems
├─ 40-DATABUS_NETWORKS/          # Internal data networks
├─ 42-AVIONICS_COMPUTE_FSW/      # Flight software and computers
├─ 45-HEALTH_MONITORING_FDIR/    # Health monitoring
├─ 50-MECHANISMS_DEPLOYABLES/    # Deployment mechanisms
├─ 51-PRIMARY_STRUCTURE/         # Structural elements
├─ 57-INSTRUMENT_BAYS/           # Payload accommodation
├─ 61-RCS_ATTITUDE_CONTROL/      # Reaction control system
├─ 70-OPTICAL_SUBSYSTEMS/        # Optical payloads (if applicable)
├─ 71-PAYLOADS/                  # Science/mission payloads
├─ 72-PROPULSION_MAIN/           # Main propulsion (if applicable)
├─ 84-ELECTRIC_PROPULSION/       # Electric propulsion (if applicable)
├─ 87-RADIATION/                 # Radiation analysis
├─ 90-SPACE_TRAFFIC_CONJUNCTION/ # Collision avoidance
├─ 97-ELECTRICAL_HARNESS/        # Electrical harness (STA-97)
└─ 99-MISSION_OPERATIONS/        # Operations concept
```

## Key Principles
1. **PLM/CAx only in SUBSYSTEMS** - All engineering artifacts at subsystem level
2. **Integration focus** - Each system has INTEGRATION_VIEW.md and INTERFACE_MATRIX/
3. **STA-97 for harness** - All physical harness in dedicated chapter (not ATA-92)
4. **ECSS compliance** - Following ECSS-E/M/Q/S standards

## System Interfaces
Interface control documents are maintained in INTERFACE_MATRIX/ folders within each system.
Cross-system interfaces are documented using CSV format: `XX↔YY.csv`

## Configuration Management
This configuration is baselined and controlled through:
- 00-PROGRAM/CONFIG_MGMT/04-BASELINES/
- Change control via CCB process
- Version control in Git

## References
- **ECSS Standards**: [ECSS website](https://ecss.nl/)
- **STA Structure**: [04-SATELLITES/00-README.md](../../../../00-README.md)
- **Interface Definitions**: [00-PROGRAM/DIGITAL_THREAD/04-MBSE/INTERFACE_DEFINITIONS/](../../../../../../../00-PROGRAM/DIGITAL_THREAD/04-MBSE/INTERFACE_DEFINITIONS/)
