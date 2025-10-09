# ATA-56 WINDOWS - Domain Integration View

## Overview

This directory contains the domain integration view for ATA-56 Windows, covering all aircraft glazing.

## Scope

ATA-56 encompasses:
- **56-10**: Windshield Structure
- **56-20**: Cockpit Side Windows
- **56-30**: Cabin Windows and Frames

## Integration View Contents

### INTEGRATION_VIEW/
- **MASTER_ASSEMBLY/**: Window system integration models
- **LAYOUTS/**: Window arrangement and installation layouts
- **NEUTRAL_EXPORTS/**: STEP AP242, JT, and QIF format exports
- **REPORTS/**: Window system integration analysis

### SUBSYSTEMS/
Contains PLM_CAX data for each subsystem, organized by ATA sub-chapter.

### INTERFACE_MATRIX.md
Defines interfaces between window subsystems and other aircraft systems.

## Key Interfaces

ATA-56 interfaces with:
- **ATA-53**: Fuselage window cutouts and frames
- **ATA-30**: Window heating and anti-ice systems
- **ATA-33**: External lighting near windows
- **ATA-92**: EWIS for window heating

## Related Configuration Data

See also:
- [Configuration Base ATA-56](../../../../CONFIGURATION_BASE/ATA-56_WINDOWS/)
- [Cross-System Integration](../../../../CROSS_SYSTEM_INTEGRATION/)

## Standards and Specifications

- **Windshield**: FAR 25.775, FAR 25.773
- **Bird Strike**: FAR 25.775(b)
- **Emergency Exit Marking**: FAR 25.811
- **Vision**: FAR 25.773 (pilot vision)

## Contacts

- **System Owner**: Structures Engineering - Windows
- **Integration Lead**: Windows/Transparencies Team

---

**Last Updated**: 2024-01-15  
**Chapter**: ATA-56
