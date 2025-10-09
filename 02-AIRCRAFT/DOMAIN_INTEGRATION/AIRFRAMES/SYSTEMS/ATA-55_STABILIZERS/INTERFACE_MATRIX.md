# ATA-55 STABILIZERS - Interface Matrix

## Overview

This interface matrix defines the relationships and interfaces between ATA-55 stabilizer subsystems and other aircraft systems.

## Internal Interfaces (Within ATA-55)

| From Subsystem | To Subsystem | Interface Type | Description |
|----------------|--------------|----------------|-------------|
| 55-10 Horizontal Stabilizer | 55-20 Elevator | Structural/Hinge | Elevator attachment and actuation |
| 55-30 Vertical Stabilizer | 55-40 Rudder | Structural/Hinge | Rudder attachment and actuation |
| 55-10 Horizontal | 55-30 Vertical | Structural | Horizontal-to-vertical interface |

## External Interfaces (ATA-55 to Other Systems)

| ATA-55 Subsystem | External System | Interface Type | Description | ICD Reference |
|------------------|-----------------|----------------|-------------|---------------|
| 55-10/30 Stabilizers | ATA-53 Fuselage | Structural | Empennage attachment to fuselage | ICD-STRUCT-040 |
| 55-20 Elevator | ATA-27 Flight Controls | Actuation/Control | Elevator control system | ICD-FCS-001 |
| 55-40 Rudder | ATA-27 Flight Controls | Actuation/Control | Rudder control system | ICD-FCS-002 |
| 55-20/40 Surfaces | ATA-27 Flight Controls | Sensing | Control surface position feedback | ICD-FCS-003 |
| All Subsystems | ATA-30 Ice Protection | Functional | Leading edge ice protection | ICD-ICE-005 |
| All Subsystems | ATA-92 EWIS | Electrical | Wiring for actuators and sensors | ICD-EWIS-040 |

## Interface Control

- **Primary ICD Repository**: `00-PROGRAM/CONFIG_MGMT/09-INTERFACES/`
- **Interface Change Control**: Configuration Control Board (CCB)
- **Traceability**: Requirements linked in Digital Thread

## Critical Interfaces

### Safety-Critical (DAL A)
- Stabilizer attachment to fuselage
- Control surface hinge fittings
- Flight control actuation interfaces
- Control surface position sensing

### Performance-Critical
- Control surface aerodynamic effectiveness
- Stabilizer structural stiffness (flutter)
- Ice protection coverage
- Control surface travel limits

## Data Exchange Formats

- **CAD Models**: STEP AP242, JT
- **Aerodynamic Data**: CFD formats (CGNS)
- **Flutter Analysis**: Nastran, MSC.FlightLoads
- **Control Laws**: MATLAB/Simulink

---

**Last Updated**: 2024-01-15  
**Owner**: Flight Surfaces Integration Team
