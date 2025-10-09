# AIRFRAMES DOMAIN INTEGRATION - Directory Structure

This document provides a complete overview of the AIRFRAMES domain integration directory structure.

## Structure Overview

The AIRFRAMES domain integration is organized into 7 major ATA chapters (51-57), each with detailed subsystem breakdowns:

```
02-AIRCRAFT/DOMAIN_INTEGRATION/AIRFRAMES/
├── 00-README.md (this file)
├── README.md (overview)
└── SYSTEMS/
    ├── ATA-51_STRUCTURES_GENERAL/
    ├── ATA-52_DOORS/
    ├── ATA-53_FUSELAGE/
    ├── ATA-54_NACELLES_PYLONS/
    ├── ATA-55_STABILIZERS/
    ├── ATA-56_WINDOWS/
    └── ATA-57_WINGS/
```

## ATA-51: STRUCTURES GENERAL

**Directory**: `SYSTEMS/ATA-51_STRUCTURES_GENERAL/`

### Subsystems (4):
- ATA-51-10: Materials and Processes
- ATA-51-20: Joints and Fasteners
- ATA-51-30: Damage Tolerance and Repairs
- ATA-51-40: Corrosion Prevention and Control

## ATA-52: DOORS

**Directory**: `SYSTEMS/ATA-52_DOORS/`

### Subsystems (5):
- ATA-52-10: Passenger Doors
- ATA-52-20: Service Doors
- ATA-52-30: Cargo Doors
- ATA-52-40: Emergency Exits
- ATA-52-50: Door Warning and Indication

## ATA-53: FUSELAGE

**Directory**: `SYSTEMS/ATA-53_FUSELAGE/`

### Subsystems (5):
- ATA-53-10: Nose Section
- ATA-53-20: Center Fuselage
- ATA-53-30: Aft Fuselage
- ATA-53-40: Pressure Vessel and Sealing
- ATA-53-50: Floor Structure

## ATA-54: NACELLES AND PYLONS

**Directory**: `SYSTEMS/ATA-54_NACELLES_PYLONS/`

### Subsystems (4):
- ATA-54-10: Nacelle Structure
- ATA-54-20: Pylon Structure
- ATA-54-30: Inlet Cowl Structure
- ATA-54-40: Thrust Reverser Structure

## ATA-55: STABILIZERS

**Directory**: `SYSTEMS/ATA-55_STABILIZERS/`

### Subsystems (4):
- ATA-55-10: Horizontal Stabilizer
- ATA-55-20: Elevator Structure
- ATA-55-30: Vertical Stabilizer
- ATA-55-40: Rudder Structure

## ATA-56: WINDOWS

**Directory**: `SYSTEMS/ATA-56_WINDOWS/`

### Subsystems (3):
- ATA-56-10: Windshield Structure
- ATA-56-20: Cockpit Side Windows
- ATA-56-30: Cabin Windows and Frames

## ATA-57: WINGS

**Directory**: `SYSTEMS/ATA-57_WINGS/`

### Subsystems (4):
- ATA-57-10: Wing Box Structure
- ATA-57-20: Leading Edge Structure
- ATA-57-30: Trailing Edge Structure
- ATA-57-40: Wing Tip Devices

## Common Structure for Each System

Every ATA system follows this consistent structure:

```
ATA-XX_SYSTEM_NAME/
├── 00-README.md                    # System overview and documentation
├── INTERFACE_MATRIX.md             # Interface definitions and relationships
├── INTEGRATION_VIEW/
│   ├── MASTER_ASSEMBLY/            # Top-level assembly models
│   ├── LAYOUTS/                    # Installation layouts and arrangements
│   ├── NEUTRAL_EXPORTS/
│   │   ├── STEP_AP242/            # ISO 10303-242 model exports
│   │   ├── JT/                    # JT format visualization files
│   │   └── QIF/                   # Quality Information Framework files
│   └── REPORTS/                   # Integration analysis reports
└── SUBSYSTEMS/
    └── ATA-XX-YY_SUBSYSTEM_NAME/
        └── PLM_CAX/
            ├── CAD/               # Computer-Aided Design
            ├── CAE/               # Computer-Aided Engineering
            ├── CAO/               # Computer-Aided Optimization
            ├── CAM/               # Computer-Aided Manufacturing
            ├── CAI/               # Computer-Aided Inspection
            ├── CAV/               # Computer-Aided Verification
            ├── CAP/               # Computer-Aided Planning
            ├── CAS/               # Computer-Aided Simulation
            ├── CMP/               # Configuration Management Package
            └── METADATA/          # Data management and metadata
```

## Statistics

- **Total ATA Systems**: 7 (ATA-51 through ATA-57)
- **Total Subsystems**: 29
- **Total Directories**: 419
- **Total Files**: 346 (including .gitkeep files)

## Documentation Files

Each system includes:
- **00-README.md**: Comprehensive system overview, scope, interfaces, and standards
- **INTERFACE_MATRIX.md**: Detailed interface definitions with internal and external system interfaces

## PLM/CAx Integration

All subsystems include a complete PLM_CAX structure with 10 subdirectories:

1. **CAD**: Computer-Aided Design models and drawings
2. **CAE**: Finite Element Analysis, CFD, and other engineering analysis
3. **CAO**: Design optimization studies and results
4. **CAM**: Manufacturing planning and toolpath data
5. **CAI**: Inspection programs and measurement data
6. **CAV**: Verification models and validation data
7. **CAP**: Production planning and process planning
8. **CAS**: Simulation models and results
9. **CMP**: Configuration management packages and baselines
10. **METADATA**: Data management, BOM, and metadata files

## Data Exchange Standards

The NEUTRAL_EXPORTS directories support:
- **STEP AP242**: ISO 10303-242 for model-based definition and PMI
- **JT**: ISO 14306 for lightweight 3D visualization
- **QIF**: ANSI/DMSC Quality Information Framework for inspection data

## Integration with Repository

This domain integration structure complements:
- **Configuration Base** (`02-AIRCRAFT/CONFIGURATION_BASE/ATA-51_*` through `ATA-57_*`)
- **Cross-System Integration** (`02-AIRCRAFT/CROSS_SYSTEM_INTEGRATION/`)
- **Digital Thread** (`00-PROGRAM/DIGITAL_THREAD/`)

## Usage Guidelines

1. **CAD Data**: Store native CAD files in PLM_CAX/CAD, export neutral formats to NEUTRAL_EXPORTS
2. **Analysis Data**: Organize by discipline in appropriate CAx directories
3. **Integration Models**: Place top-level assemblies in INTEGRATION_VIEW/MASTER_ASSEMBLY
4. **Interface Control**: Document all interfaces in INTERFACE_MATRIX.md
5. **Version Control**: Use .gitkeep to maintain directory structure, actual PLM data may reside in external systems

## Related Documentation

- [AIRFRAMES Overview](./README.md)
- [Configuration Base](../../CONFIGURATION_BASE/00-README.md)
- [PLM Standards](../../../00-PROGRAM/STANDARDS/04-CROSS_CUTTING/CONFIG_MGMT/)

---

**Created**: 2024-01-15  
**Last Updated**: 2024-01-15  
**Maintained By**: Structures Integration Team
