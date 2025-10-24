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
├─ ATA-00_GENERAL/                              # Shared resources across all ATA chapters
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

### ATA Chapter Organization

#### ATA 05–12: General/Operational

* [ATA-05_TIME_LIMITS_MAINT_CHECKS](./ATA-05_TIME_LIMITS_MAINT_CHECKS/)
* [ATA-06_DIMENSIONS_AREAS](./ATA-06_DIMENSIONS_AREAS/)
* [ATA-08_LEVELING_WEIGHING](./ATA-08_LEVELING_WEIGHING/)
* [ATA-11_PLACARDS_MARKINGS](./ATA-11_PLACARDS_MARKINGS/)
* [ATA-12_SERVICING](./ATA-12_SERVICING/)

#### ATA 20–50: Systems

* [ATA-20_STANDARD_PRACTICES](./ATA-20_STANDARD_PRACTICES/)
* [ATA-21_AIR_CONDITIONING](./ATA-21_AIR_CONDITIONING/)
* [ATA-22_AUTO_FLIGHT](./ATA-22_AUTO_FLIGHT/)
* [ATA-23_COMMUNICATIONS](./ATA-23_COMMUNICATIONS/)
* [ATA-24_ELECTRICAL_POWER](./ATA-24_ELECTRICAL_POWER/)
* [ATA-25_EQUIPMENT_FURNISHINGS](./ATA-25_EQUIPMENT_FURNISHINGS/)
* [ATA-26_FIRE_PROTECTION](./ATA-26_FIRE_PROTECTION/)
* [ATA-27_FLIGHT_CONTROLS](./ATA-27_FLIGHT_CONTROLS/)
* [ATA-28_FUEL](./ATA-28_FUEL/) — includes H₂ storage systems
* [ATA-29_HYDRAULIC_POWER](./ATA-29_HYDRAULIC_POWER/)
* [ATA-30_ICE_RAIN_PROTECTION](./ATA-30_ICE_RAIN_PROTECTION/)
* [ATA-31_INDICATING_RECORDING](./ATA-31_INDICATING_RECORDING/)
* [ATA-32_LANDING_GEAR](./ATA-32_LANDING_GEAR/)
* [ATA-33_LIGHTS](./ATA-33_LIGHTS/)
* [ATA-34_NAVIGATION](./ATA-34_NAVIGATION/)
* [ATA-35_OXYGEN](./ATA-35_OXYGEN/)
* [ATA-36_PNEUMATIC](./ATA-36_PNEUMATIC/)
* [ATA-38_WATER_WASTE](./ATA-38_WATER_WASTE/)
* [ATA-42_INTEGRATED_MODULAR_AVIONICS](./ATA-42_INTEGRATED_MODULAR_AVIONICS/) — ARINC 653 platform
* [ATA-44_CABIN_SYSTEMS](./ATA-44_CABIN_SYSTEMS/)
* [ATA-45_CENTRAL_MAINTENANCE](./ATA-45_CENTRAL_MAINTENANCE/)
* [ATA-46_INFORMATION_SYSTEMS](./ATA-46_INFORMATION_SYSTEMS/)
* [ATA-47_INERT_GAS](./ATA-47_INERT_GAS/) *(optional)*
* [ATA-49_APU](./ATA-49_APU/)
* [ATA-50_CARGO_LOAD_SYSTEMS](./ATA-50_CARGO_LOAD_SYSTEMS/) *(optional)*

#### ATA 51–57: Structures

* [ATA-51_STRUCTURES_GENERAL](./ATA-51_STRUCTURES_GENERAL/)
* [ATA-52_DOORS](./ATA-52_DOORS/)
* [ATA-53_FUSELAGE](./ATA-53_FUSELAGE/)
* [ATA-54_NACELLES_PYLONS](./ATA-54_NACELLES_PYLONS/)
* [ATA-55_STABILIZERS](./ATA-55_STABILIZERS/)
* [ATA-56_WINDOWS](./ATA-56_WINDOWS/)
* [ATA-57_WINGS](./ATA-57_WINGS/)

#### ATA 70–80: Powerplant

* [ATA-70_POWERPLANT_PRACTICES](./ATA-70_POWERPLANT_PRACTICES/)
* [ATA-71_POWERPLANT](./ATA-71_POWERPLANT/)
* [ATA-72_ENGINE](./ATA-72_ENGINE/)
* [ATA-73_ENGINE_FUEL_CONTROL](./ATA-73_ENGINE_FUEL_CONTROL/)
* [ATA-74_IGNITION](./ATA-74_IGNITION/)
* [ATA-75_BLEED_AIR](./ATA-75_BLEED_AIR/)
* [ATA-76_ENGINE_CONTROLS](./ATA-76_ENGINE_CONTROLS/)
* [ATA-77_ENGINE_INDICATING](./ATA-77_ENGINE_INDICATING/)
* [ATA-78_EXHAUST](./ATA-78_EXHAUST/)
* [ATA-79_OIL](./ATA-79_OIL/)
* [ATA-80_STARTING](./ATA-80_STARTING/)

#### ATA 92: Wiring

* [ATA-92_EWIS](./ATA-92_EWIS/) — **all** aircraft wiring per EWIS rules (harnesses, connectors, shielding, zones)


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

Key rules governing this structure (see ATA-00_GENERAL/RULES.md for details):

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
