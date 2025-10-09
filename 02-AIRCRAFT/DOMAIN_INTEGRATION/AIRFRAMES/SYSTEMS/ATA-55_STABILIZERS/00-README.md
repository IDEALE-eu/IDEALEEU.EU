# ATA-55 STABILIZERS - Domain Integration View

## Overview

This directory contains the domain integration view for ATA-55 Stabilizers, covering horizontal and vertical stabilizer structures.

## Scope

ATA-55 encompasses:
- **55-10**: Horizontal Stabilizer
- **55-20**: Elevator Structure
- **55-30**: Vertical Stabilizer
- **55-40**: Rudder Structure

## Integration View Contents

### INTEGRATION_VIEW/
- **MASTER_ASSEMBLY/**: Stabilizer assembly models
- **LAYOUTS/**: Stabilizer arrangement and installation layouts
- **NEUTRAL_EXPORTS/**: STEP AP242, JT, and QIF format exports
- **REPORTS/**: Stabilizer integration analysis

### SUBSYSTEMS/
Contains PLM_CAX data for each subsystem, organized by ATA sub-chapter.

### INTERFACE_MATRIX.md
Defines interfaces between stabilizer subsystems and other aircraft systems.

## Key Interfaces

ATA-55 interfaces with:
- **ATA-53**: Stabilizer attachment to fuselage
- **ATA-27**: Flight control systems (elevator/rudder actuation)
- **ATA-30**: Ice protection systems
- **ATA-92**: EWIS for control surface systems

## Related Configuration Data

See also:
- [Configuration Base ATA-55](../../../../CONFIGURATION_BASE/ATA-55_STABILIZERS/)
- [Cross-System Integration](../../../../CROSS_SYSTEM_INTEGRATION/)

## Standards and Specifications

- **Control Surfaces**: FAR 25.391, FAR 25.415
- **Flutter**: FAR 25.629
- **Trim Systems**: FAR 25.677
- **Load Cases**: FAR 25.345 through 25.351

## Contacts

- **System Owner**: Structures Engineering - Empennage
- **Integration Lead**: Flight Surfaces Integration Team

---

**Last Updated**: 2024-01-15  
**Chapter**: ATA-55
