# ATA-54 NACELLES AND PYLONS - Domain Integration View

## Overview

This directory contains the domain integration view for ATA-54 Nacelles and Pylons, covering engine installation structures.

## Scope

ATA-54 encompasses:
- **54-10**: Nacelle Structure
- **54-20**: Pylon Structure
- **54-30**: Inlet Cowl Structure
- **54-40**: Thrust Reverser Structure

## Integration View Contents

### INTEGRATION_VIEW/
- **MASTER_ASSEMBLY/**: Nacelle and pylon assembly models
- **LAYOUTS/**: Installation and arrangement layouts
- **NEUTRAL_EXPORTS/**: STEP AP242, JT, and QIF format exports
- **REPORTS/**: Nacelle/pylon integration analysis

### SUBSYSTEMS/
Contains PLM_CAX data for each subsystem, organized by ATA sub-chapter.

### INTERFACE_MATRIX.md
Defines interfaces between nacelle/pylon subsystems and other aircraft systems.

## Key Interfaces

ATA-54 interfaces with:
- **ATA-53/57**: Pylon attachment to wing/fuselage
- **ATA-70 through ATA-80**: Powerplant installation
- **ATA-30**: Nacelle anti-ice systems
- **ATA-78**: Engine exhaust system

## Related Configuration Data

See also:
- [Configuration Base ATA-54](../../../../CONFIGURATION_BASE/ATA-54_NACELLES_PYLONS/)
- [Cross-System Integration](../../../../CROSS_SYSTEM_INTEGRATION/)

## Standards and Specifications

- **Load Cases**: FAR 25.361, CS 25.361
- **Fire Protection**: FAR 25.1191 through 25.1203
- **Thrust Reverser**: FAR 25.933
- **Bird Strike**: FAR 25.571(e)

## Contacts

- **System Owner**: Structures Engineering - Nacelles/Pylons
- **Integration Lead**: Propulsion Integration Team

---

**Last Updated**: 2024-01-15  
**Chapter**: ATA-54
