# Interface Control Document (ICD) Index

## Overview

Human-friendly index of all ICDs relevant to cross-system integration.

## Critical ICDs (DAL A)

### Flight Control
- **[ICD-0003](../../../../00-PROGRAM/CONFIG_MGMT/09-INTERFACES/ICD-0003.md)**: Avionics ↔ Flight Control (AFDX)
- **[ICD-0015](../../../../00-PROGRAM/CONFIG_MGMT/09-INTERFACES/ICD-0015.md)**: Flight Control ↔ Actuator Control (AFDX)

### Propulsion
- **[ICD-0001](../../../../00-PROGRAM/CONFIG_MGMT/09-INTERFACES/ICD-0001.md)**: Airframe ↔ Propulsion System
- **[ICD-0006](../../../../00-PROGRAM/CONFIG_MGMT/09-INTERFACES/ICD-0006.md)**: Engine ECU ↔ FADEC (CAN)
- **[ICD-0031](../../../../00-PROGRAM/CONFIG_MGMT/09-INTERFACES/ICD-0031.md)**: Throttle ↔ FADEC
- **[ICD-0032](../../../../00-PROGRAM/CONFIG_MGMT/09-INTERFACES/ICD-0032.md)**: FADEC ↔ Engine ECU (CAN)

### Power
- **[ICD-0004](../../../../00-PROGRAM/CONFIG_MGMT/09-INTERFACES/ICD-0004.md)**: Power Generation ↔ Distribution

### Fire Detection
- **[ICD-0011](../../../../00-PROGRAM/CONFIG_MGMT/09-INTERFACES/ICD-0011.md)**: Fire Detection ↔ Suppression

### Braking
- **[ICD-0018](../../../../00-PROGRAM/CONFIG_MGMT/09-INTERFACES/ICD-0018.md)**: Brake Control ↔ Actuators

### Air Data
- **[ICD-0023](../../../../00-PROGRAM/CONFIG_MGMT/09-INTERFACES/ICD-0023.md)**: Air Data ↔ Avionics (ARINC 429)

## Essential ICDs (DAL B)

### Navigation
- **[ICD-0005](../../../../00-PROGRAM/CONFIG_MGMT/09-INTERFACES/ICD-0005.md)**: Navigation ↔ FMS (ARINC 429)
- **[ICD-0021](../../../../00-PROGRAM/CONFIG_MGMT/09-INTERFACES/ICD-0021.md)**: GPS ↔ FMS (ARINC 429)
- **[ICD-0022](../../../../00-PROGRAM/CONFIG_MGMT/09-INTERFACES/ICD-0022.md)**: IRS ↔ FMS (AFDX)

### Display
- **[ICD-0008](../../../../00-PROGRAM/CONFIG_MGMT/09-INTERFACES/ICD-0008.md)**: Display ↔ Avionics (AFDX)

## Non-Critical ICDs (DAL C/D)

### Hydraulics
- **[ICD-0007](../../../../00-PROGRAM/CONFIG_MGMT/09-INTERFACES/ICD-0007.md)**: Hydraulic System Interface
- **[ICD-0041](../../../../00-PROGRAM/CONFIG_MGMT/09-INTERFACES/ICD-0041.md)**: Hydraulic Sensor Interface

### Communications
- **[ICD-0013](../../../../00-PROGRAM/CONFIG_MGMT/09-INTERFACES/ICD-0013.md)**: Communications Radio ↔ Avionics

### Weather Radar
- **[ICD-0014](../../../../00-PROGRAM/CONFIG_MGMT/09-INTERFACES/ICD-0014.md)**: Weather Radar ↔ Avionics (ARINC 429)

### Fuel
- **[ICD-0012](../../../../00-PROGRAM/CONFIG_MGMT/09-INTERFACES/ICD-0012.md)**: Fuel System Interface

## ICD Status Summary

- **Total ICDs**: 28
- **Approved**: 16 (61%)
- **Draft**: 10 (36%)
- **Superseded**: 0

## References

- **Master ICD Catalog**: [00-PROGRAM/CONFIG_MGMT/09-INTERFACES/ICD_INDEX.md](../../../../00-PROGRAM/CONFIG_MGMT/09-INTERFACES/ICD_INDEX.md)
- **Interface Matrix**: [01-ARCHITECTURE_END2END/INTERFACE_MATRIX/INTERFACE_MATRIX.csv](../../01-ARCHITECTURE_END2END/INTERFACE_MATRIX/INTERFACE_MATRIX.csv)
- **ICD Mapping**: [MAP_TO_CONFIG_MGMT.csv](./MAP_TO_CONFIG_MGMT.csv)
