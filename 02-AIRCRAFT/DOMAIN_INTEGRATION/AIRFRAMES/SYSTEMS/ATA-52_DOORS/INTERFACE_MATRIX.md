# ATA-52 DOORS - Interface Matrix

## Overview

This interface matrix defines the relationships and interfaces between ATA-52 door subsystems and other aircraft systems.

## Internal Interfaces (Within ATA-52)

| From Subsystem | To Subsystem | Interface Type | Description |
|----------------|--------------|----------------|-------------|
| 52-10 Passenger Doors | 52-50 Warning System | Status Monitoring | Door open/close status |
| 52-20 Service Doors | 52-50 Warning System | Status Monitoring | Service door status |
| 52-30 Cargo Doors | 52-50 Warning System | Status Monitoring | Cargo door position |
| 52-40 Emergency Exits | 52-50 Warning System | Status Monitoring | Exit door status |

## External Interfaces (ATA-52 to Other Systems)

| ATA-52 Subsystem | External System | Interface Type | Description | ICD Reference |
|------------------|-----------------|----------------|-------------|---------------|
| All Door Types | ATA-53 Fuselage | Structural | Door frame attachment and sealing | ICD-STRUCT-010 |
| All Door Types | ATA-32 Landing Gear | Functional | Door interlock with gear position | ICD-GEAR-001 |
| 52-50 Warning | ATA-31 Indicating | Display | Door status to cockpit displays | ICD-DISP-005 |
| 52-50 Warning | ATA-24 Electrical | Power | Warning system power supply | ICD-ELEC-012 |
| All Door Types | ATA-92 EWIS | Electrical | Wiring for sensors and indicators | ICD-EWIS-010 |
| 52-10/40 Exit Doors | ATA-25 Equipment | Evacuation | Emergency slide interface | ICD-EQUIP-003 |

## Interface Control

- **Primary ICD Repository**: `00-PROGRAM/CONFIG_MGMT/09-INTERFACES/`
- **Interface Change Control**: Configuration Control Board (CCB)
- **Traceability**: Requirements linked in Digital Thread

## Critical Interfaces

### Safety-Critical (DAL A)
- Door open/close sensing and indication
- Door-to-fuselage pressure seal
- Emergency exit operation
- Door/gear interlock system

### Performance-Critical
- Door operating mechanisms
- Sealing effectiveness (pressurization)
- Emergency evacuation time

## Data Exchange Formats

- **CAD Models**: STEP AP242, JT
- **Kinematic Analysis**: Adams, RecurDyn formats
- **Sealing Analysis**: CFD data formats
- **Sensor Data**: ARINC 429, ARINC 664

---

**Last Updated**: 2024-01-15  
**Owner**: Door Systems Integration Team
