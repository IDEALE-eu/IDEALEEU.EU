# CONFIGURATION_BASE

Aircraft systems configuration baseline organized by ATA chapter structure.

## Overview

The CONFIGURATION_BASE directory contains the baseline configuration for all aircraft systems organized according to the ATA (Air Transport Association) iSpec 2200 standard chapter structure. Each ATA chapter represents a specific aircraft system or subsystem and contains comprehensive configuration data including parameters, baselines, hardware configurations, software baselines, interface control documents, verification artifacts, and change logs.

## Purpose

This structure serves as the single source of truth for:
- System parameter definitions and limits
- Hardware configuration baselines
- Software release baselines
- Interface control documents (ICDs)
- Verification and validation artifacts
- Change history and traceability

## Structure

```
CONFIGURATION_BASE/
├─ 00-README.md                            # This file
├─ 00-COMMON/                              # Shared resources across all ATA chapters
│  ├─ RULES.md                             # Configuration rules and guidelines
│  ├─ SCHEMAS/                             # JSON/XML schemas for BASELINE, PARAMS, etc.
│  ├─ UTCS_INDEX/                          # Unified Type Certificate Specs index
│  │  ├─ index.json
│  │  └─ utcs-schemas/
│  ├─ TEMPLATES/                           # Standard templates
│  │  ├─ PARAMS.csv
│  │  ├─ PARTITION_MAP.csv
│  │  └─ IMA_CONFIG.xml
│  └─ GLOBAL_CHANGE_LOG.csv                # Master change log
├─ ATA-[XX]_[SYSTEM_NAME]/                 # Individual ATA chapters
│  ├─ PARAMS/                              # System parameters and limits
│  ├─ BASELINE/                            # Configuration baselines
│  ├─ HW_CONFIG/                           # Hardware configuration
│  ├─ SW_BASELINE/                         # Software baselines
│  ├─ ICD/                                 # Interface control documents
│  ├─ VERIFICATION/                        # V&V artifacts
│  └─ CHANGE_LOG/                          # Chapter-specific change log
└─ ATA-92_EWIS/                            # Electrical Wiring Interconnection System
   └─ (All wiring configurations per rules)
```

## ATA Chapter Organization

### ATA 05-12: General/Operational

- **ATA-05** TIME_LIMITS_MAINT_CHECKS - Time limits and maintenance checks
- **ATA-06** DIMENSIONS_AREAS - Dimensions and areas
- **ATA-08** LEVELING_WEIGHING - Leveling and weighing
- **ATA-11** PLACARDS_MARKINGS - Placards and markings
- **ATA-12** SERVICING - Servicing

### ATA 20-50: Systems

- **ATA-20** STANDARD_PRACTICES - Standard practices
- **ATA-21** AIR_CONDITIONING - Air conditioning
- **ATA-22** AUTO_FLIGHT - Auto flight
- **ATA-23** COMMUNICATIONS - Communications
- **ATA-24** ELECTRICAL_POWER - Electrical power
- **ATA-25** EQUIPMENT_FURNISHINGS - Equipment and furnishings
- **ATA-26** FIRE_PROTECTION - Fire protection
- **ATA-27** FLIGHT_CONTROLS - Flight controls
- **ATA-28** FUEL - Fuel (includes H2 storage systems)
- **ATA-29** HYDRAULIC_POWER - Hydraulic power
- **ATA-30** ICE_RAIN_PROTECTION - Ice and rain protection
- **ATA-31** INDICATING_RECORDING - Indicating and recording systems
- **ATA-32** LANDING_GEAR - Landing gear
- **ATA-33** LIGHTS - Lights
- **ATA-34** NAVIGATION - Navigation
- **ATA-35** OXYGEN - Oxygen
- **ATA-36** PNEUMATIC - Pneumatic
- **ATA-38** WATER_WASTE - Water and waste
- **ATA-42** INTEGRATED_MODULAR_AVIONICS - IMA (ARINC 653 platform)
- **ATA-44** CABIN_SYSTEMS - Cabin systems
- **ATA-45** CENTRAL_MAINTENANCE - Central maintenance system
- **ATA-46** INFORMATION_SYSTEMS - Information systems
- **ATA-47** INERT_GAS - Inert gas (optional)
- **ATA-49** APU - Auxiliary power unit
- **ATA-50** CARGO_LOAD_SYSTEMS - Cargo and load systems (optional)

### ATA 51-57: Structures

- **ATA-51** STRUCTURES_GENERAL - Structures (general)
- **ATA-52** DOORS - Doors
- **ATA-53** FUSELAGE - Fuselage
- **ATA-54** NACELLES_PYLONS - Nacelles and pylons
- **ATA-55** STABILIZERS - Stabilizers
- **ATA-56** WINDOWS - Windows
- **ATA-57** WINGS - Wings

### ATA 70-80: Powerplant

- **ATA-70** POWERPLANT_PRACTICES - Powerplant standard practices
- **ATA-71** POWERPLANT - Powerplant (general)
- **ATA-72** ENGINE - Engine
- **ATA-73** ENGINE_FUEL_CONTROL - Engine fuel and control
- **ATA-74** IGNITION - Ignition
- **ATA-75** BLEED_AIR - Engine bleed air
- **ATA-76** ENGINE_CONTROLS - Engine controls
- **ATA-77** ENGINE_INDICATING - Engine indicating
- **ATA-78** EXHAUST - Exhaust
- **ATA-79** OIL - Oil
- **ATA-80** STARTING - Starting

### ATA 92: Wiring

- **ATA-92** EWIS - Electrical Wiring Interconnection System
  - Contains ALL aircraft wiring configurations per EWIS rules
  - Harnesses, connectors, shielding, and zone specifications

## Standard Subdirectories

Each ATA chapter contains the following standard subdirectories:

### PARAMS/
Parameter definitions, limits, and thresholds for the system. Examples:
- Operating ranges and limits
- Performance thresholds
- Configuration parameters
- Tolerance specifications

### BASELINE/
Baseline configuration data including:
- Component lists and configurations
- System architecture definitions
- Baseline snapshots at major gates

### HW_CONFIG/
Hardware configuration data:
- LRU (Line Replaceable Unit) configurations
- Physical connections and interfaces
- Installation specifications
- Part numbers and variants

### SW_BASELINE/
Software baseline information:
- Software part numbers and versions
- Load configurations
- Partition assignments (for IMA systems)
- Release packages

### ICD/
Interface Control Documents:
- System interfaces
- Data bus definitions (ARINC 429, ARINC 664, etc.)
- Protocol specifications
- Signal definitions

### VERIFICATION/
Verification and validation artifacts:
- Test plans and procedures
- Test results and reports
- Compliance evidence
- Certification artifacts

### CHANGE_LOG/
Chapter-specific change history:
- Configuration changes
- ECR/ECO references
- Baseline updates
- Version history

## Configuration Rules

Key rules governing this structure (see 00-COMMON/RULES.md for details):

1. **LRU Placement**: Line Replaceable Units (LRUs) reside in their primary ATA chapter
2. **Software Placement**: Software resides with its host LRU
3. **EWIS Rule**: ALL wiring configurations reside ONLY in ATA-92_EWIS
4. **Change Control**: All changes require ECR/ECO through CCB process
5. **Baseline Integrity**: Baseline directories are immutable; changes create new baselines
6. **Traceability**: All items must be traceable to requirements and ICDs

## Integration with CM Process

This configuration baseline integrates with the program-level Configuration Management:

- **Item Master**: Links to [00-PROGRAM/CONFIG_MGMT/08-ITEM_MASTER/](../../00-PROGRAM/CONFIG_MGMT/08-ITEM_MASTER/)
- **Baselines**: Gate baselines in [00-PROGRAM/CONFIG_MGMT/04-BASELINES/](../../00-PROGRAM/CONFIG_MGMT/04-BASELINES/)
- **Changes**: ECR/ECO process in [00-PROGRAM/CONFIG_MGMT/06-CHANGES/](../../00-PROGRAM/CONFIG_MGMT/06-CHANGES/)
- **Interfaces**: ICD management in [00-PROGRAM/CONFIG_MGMT/09-INTERFACES/](../../00-PROGRAM/CONFIG_MGMT/09-INTERFACES/)
- **Traceability**: Requirements links in [00-PROGRAM/CONFIG_MGMT/10-TRACEABILITY/](../../00-PROGRAM/CONFIG_MGMT/10-TRACEABILITY/)

## Usage Guidelines

### Adding New Configuration Items

1. Identify the appropriate ATA chapter
2. Place hardware in primary system chapter
3. Place software with host LRU
4. Place all wiring in ATA-92_EWIS
5. Document in PARAMS/ and update BASELINE/
6. Create/update ICDs in ICD/
7. Log change in CHANGE_LOG/

### Updating Configurations

1. Submit ECR through CCB process
2. Upon approval, update configuration files
3. Update baselines at appropriate gates
4. Document in CHANGE_LOG/
5. Update traceability links
6. Verify through VERIFICATION/

### Establishing Baselines

1. Freeze configuration at gate
2. Create baseline snapshot in BASELINE/
3. Update gate baseline in CONFIG_MGMT/04-BASELINES/
4. Generate MANIFEST.json with SHA-256 hashes
5. Obtain CCB approval
6. Tag in version control

## Special Considerations

### ATA-28 FUEL (H2 Systems)
Contains hydrogen storage and distribution systems:
- H2 tank configurations
- Cryogenic system parameters
- Pressure and temperature limits
- Safety parameters

### ATA-42 IMA (Integrated Modular Avionics)
Contains ARINC 653 platform configuration:
- Partition definitions and mappings
- CPU and memory allocations
- Module configurations
- Hosted application bindings

### ATA-92 EWIS (Wiring)
Centralized location for ALL wiring per EWIS rules:
- Wire specifications and routing
- Harness configurations
- Connector and splice definitions
- Zone wire lists
- Shielding and grounding

## References

- **ATA iSpec 2200**: Industry standard for aircraft systems organization
- **Configuration Management Plan**: [00-PROGRAM/CONFIG_MGMT/01-CM_PLAN.md](../../00-PROGRAM/CONFIG_MGMT/01-CM_PLAN.md)
- **Part Numbering**: [00-PROGRAM/CONFIG_MGMT/02-PART_NUMBERING.md](../../00-PROGRAM/CONFIG_MGMT/02-PART_NUMBERING.md)
- **Change Process**: [00-PROGRAM/CONFIG_MGMT/06-CHANGES/](../../00-PROGRAM/CONFIG_MGMT/06-CHANGES/)
- **Baseline Process**: [00-PROGRAM/CONFIG_MGMT/04-BASELINES/00-README.md](../../00-PROGRAM/CONFIG_MGMT/04-BASELINES/00-README.md)

## Compliance

This structure complies with:
- ATA iSpec 2200 specification
- Configuration Management standards
- Systems engineering best practices
- EWIS requirements (FAA/EASA)
- ARINC 653 standards (for IMA)
- DO-178C/DO-254 (for software/hardware)

## Maintenance

- **Owner**: Configuration Management Team
- **Review**: Quarterly and at each program gate
- **Updates**: Via ECR/ECO process only
- **Audit**: Annual configuration audit

---

**Document Control**
- **Version**: 1.0
- **Date**: 2024
- **Status**: Initial Release
- **Classification**: Internal Use
