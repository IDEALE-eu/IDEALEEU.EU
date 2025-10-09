# ATA-52 DOORS - Domain Integration View

## Overview

This directory contains the domain integration view for ATA-52 Doors, covering all aircraft doors and exits.

## Scope

ATA-52 encompasses:
- **52-10**: Passenger Doors
- **52-20**: Service Doors
- **52-30**: Cargo Doors
- **52-40**: Emergency Exits
- **52-50**: Door Warning and Indication

## Integration View Contents

### INTEGRATION_VIEW/
- **MASTER_ASSEMBLY/**: Door system integration models
- **LAYOUTS/**: Door arrangement and installation layouts
- **NEUTRAL_EXPORTS/**: STEP AP242, JT, and QIF format exports
- **REPORTS/**: Door system integration analysis

### SUBSYSTEMS/
Contains PLM_CAX data for each subsystem, organized by ATA sub-chapter.

### INTERFACE_MATRIX.md
Defines interfaces between door subsystems and other aircraft systems.

## Key Interfaces

ATA-52 interfaces with:
- **ATA-53**: Fuselage structure and door frames
- **ATA-24/31**: Warning and indication systems
- **ATA-32**: Door actuation and control
- **ATA-92**: EWIS for door systems

## Related Configuration Data

See also:
- [Configuration Base ATA-52](../../../../CONFIGURATION_BASE/ATA-52_DOORS/)
- [Cross-System Integration](../../../../CROSS_SYSTEM_INTEGRATION/)

## Standards and Specifications

- **Safety**: FAR 25.783, CS 25.783 (Door operating requirements)
- **Emergency Exits**: FAR 25.807, FAR 25.809
- **Cargo Doors**: FAR 25.787
- **Door Warnings**: FAR 25.1421

## Contacts

- **System Owner**: Structures Engineering - Doors
- **Integration Lead**: Door Systems Integration Team

---

**Last Updated**: 2024-01-15  
**Chapter**: ATA-52
