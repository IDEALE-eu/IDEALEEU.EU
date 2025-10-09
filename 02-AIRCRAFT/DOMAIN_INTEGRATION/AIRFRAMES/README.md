# AIRFRAMES

This directory contains the domain integration view for aircraft airframe systems, organized by ATA chapters 51-57.

## Overview

The AIRFRAMES domain encompasses all structural systems and components that form the aircraft's primary structure, including:

- **ATA-51**: Structures General (materials, joints, damage tolerance, corrosion protection)
- **ATA-52**: Doors (passenger, service, cargo, emergency exits)
- **ATA-53**: Fuselage (nose, center, aft sections, pressure vessel, floor structure)
- **ATA-54**: Nacelles and Pylons (nacelle structure, pylons, inlet cowls, thrust reversers)
- **ATA-55**: Stabilizers (horizontal/vertical stabilizers, elevator/rudder structures)
- **ATA-56**: Windows (windshield, cockpit windows, cabin windows)
- **ATA-57**: Wings (wing box, leading edge, trailing edge, wing tip devices)

## Purpose

This domain integration view provides:

- **Cross-system integration**: Interfaces and integration points between airframe systems
- **PLM/CAx data management**: Centralized location for CAD, CAE, CAM, and other engineering artifacts
- **Master assemblies**: Top-level integration views and layouts
- **Neutral formats**: STEP AP242, JT, and QIF exports for data exchange
- **Interface documentation**: Interface matrices and control documents

## Structure

```
AIRFRAMES/
├── 00-README.md (this file)
└── SYSTEMS/
    ├── ATA-51_STRUCTURES_GENERAL/
    ├── ATA-52_DOORS/
    ├── ATA-53_FUSELAGE/
    ├── ATA-54_NACELLES_PYLONS/
    ├── ATA-55_STABILIZERS/
    ├── ATA-56_WINDOWS/
    └── ATA-57_WINGS/
```

Each system directory contains:

### INTEGRATION_VIEW/
- **MASTER_ASSEMBLY/**: Top-level assembly models and configurations
- **LAYOUTS/**: Installation layouts and arrangement drawings
- **NEUTRAL_EXPORTS/**: 
  - **STEP_AP242/**: ISO 10303 AP242 model-based definition files
  - **JT/**: JT format files for visualization and collaboration
  - **QIF/**: Quality Information Framework files for inspection
- **REPORTS/**: Integration analysis reports and documentation

### SUBSYSTEMS/
Subsystem-specific content organized by ATA sub-chapter, each containing:

- **PLM_CAX/**: Product Lifecycle Management and CAx data
  - **CAD/**: Computer-Aided Design models and drawings
  - **CAE/**: Computer-Aided Engineering (FEA, CFD, etc.)
  - **CAO/**: Computer-Aided Optimization
  - **CAM/**: Computer-Aided Manufacturing
  - **CAI/**: Computer-Aided Inspection
  - **CAV/**: Computer-Aided Verification
  - **CAP/**: Computer-Aided Planning
  - **CAS/**: Computer-Aided Simulation
  - **CMP/**: Configuration Management Package
  - **METADATA/**: Metadata and data management files

### Interface Documentation
- **INTERFACE_MATRIX.md**: Interface relationships within the system
- **00-README.md**: System-specific overview and documentation

## Integration with Configuration Base

This domain integration view complements the configuration management data in:
- `02-AIRCRAFT/CONFIGURATION_BASE/ATA-51_STRUCTURES_GENERAL/` through `ATA-57_WINGS/`

While CONFIGURATION_BASE focuses on:
- Parameters and operating limits
- Hardware/software configuration
- Interface Control Documents (ICDs)
- Verification and validation
- Change logs

DOMAIN_INTEGRATION focuses on:
- Physical integration and assembly
- CAD/CAE/CAM data and models
- Master assemblies and layouts
- Cross-domain interfaces
- Neutral format exports for collaboration

## Key Interfaces

Airframe systems interface with:
- **ATA-20 through ATA-50**: Systems installation and mounting
- **ATA-70 through ATA-80**: Powerplant installation and nacelle integration
- **ATA-92**: EWIS (Electrical Wiring Interconnection System)

## PLM System Integration

The PLM_CAX directories are intended for integration with:
- Siemens Teamcenter
- Dassault Systèmes 3DEXPERIENCE/ENOVIA
- PTC Windchill
- SAP PLM
- Aras Innovator

See: `00-PROGRAM/STANDARDS/04-CROSS_CUTTING/CONFIG_MGMT/00-README.md` for PLM system details.

## Data Exchange Standards

- **STEP AP242**: ISO 10303-242 for 3D model-based definition
- **JT**: ISO 14306 for 3D visualization
- **QIF**: ANSI/DMSC Quality Information Framework for inspection

## Related Documentation

- [Configuration Base README](../../CONFIGURATION_BASE/00-README.md)
- [Cross-System Integration](../../CROSS_SYSTEM_INTEGRATION/)
- [Digital Thread](../../../00-PROGRAM/DIGITAL_THREAD/)
- [Configuration Management Standards](../../../00-PROGRAM/STANDARDS/04-CROSS_CUTTING/CONFIG_MGMT/)

## Contacts

- **Domain Owner**: Structures Engineering
- **Integration Lead**: Systems Integration Team
- **Data Management**: PLM/PDM Team

---

**Last Updated**: 2024-01-15  
**Status**: Active
