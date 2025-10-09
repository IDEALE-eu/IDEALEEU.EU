# Configuration Base Links - CABINS_CARGO_PAX Domain

## Purpose

This document provides pointers to the configuration baseline for each ATA chapter within the CABINS_CARGO_PAX domain. The actual configuration data resides in `CONFIGURATION_BASE/`.

## Principle: Reference, Don't Copy

This domain integration **references** configuration data; it does NOT duplicate it. All baseline configuration, parameters, hardware specs, and software baselines are maintained in the `CONFIGURATION_BASE/` directory.

## ATA-25: Equipment & Furnishings

### Configuration Location
`02-AIRCRAFT/CONFIGURATION_BASE/ATA-25_EQUIPMENT_FURNISHINGS/`

### Contents
- **BASELINE/**: Component lists, system architecture, baseline snapshots
- **HW_CONFIG/**: LRU configurations, installation specs, assemblies
- **SW_BASELINE/**: Software versions, load configurations
- **PARAMS/**: System parameters, operating limits
- **ICD/**: Interface Control Documents
- **VERIFICATION/**: Test plans, procedures, results
- **CHANGE_LOG/**: Configuration change history

### Key Documents
- [ATA-25 README](../../../CONFIGURATION_BASE/ATA-25_EQUIPMENT_FURNISHINGS/README.md)
- [ATA-25 Baseline](../../../CONFIGURATION_BASE/ATA-25_EQUIPMENT_FURNISHINGS/BASELINE/)
- [ATA-25 Parameters](../../../CONFIGURATION_BASE/ATA-25_EQUIPMENT_FURNISHINGS/PARAMS/)

### Subsystems in Config Base
- Seats (ATA-25-10)
- Galleys (ATA-25-20)
- Lavatories (ATA-25-30)
- Trims & Linings (ATA-25-40)
- Overhead Bins (ATA-25-50)
- Floors (ATA-25-60)
- Passenger Service Units (ATA-25-70)
- Emergency Equipment (ATA-25-80)

---

## ATA-44: Cabin Systems

### Configuration Location
`02-AIRCRAFT/CONFIGURATION_BASE/ATA-44_CABIN_SYSTEMS/`

### Contents
- **BASELINE/**: System architecture, component inventory
- **HW_CONFIG/**: Server configs, network equipment, LRUs
- **SW_BASELINE/**: CMS software, IFE software, firmware versions
- **PARAMS/**: Network parameters, system settings
- **ICD/**: Interface specifications
- **VERIFICATION/**: System test results
- **CHANGE_LOG/**: Configuration changes

### Key Documents
- [ATA-44 README](../../../CONFIGURATION_BASE/ATA-44_CABIN_SYSTEMS/README.md)
- [ATA-44 Software Baseline](../../../CONFIGURATION_BASE/ATA-44_CABIN_SYSTEMS/SW_BASELINE/)
- [ATA-44 Hardware Config](../../../CONFIGURATION_BASE/ATA-44_CABIN_SYSTEMS/HW_CONFIG/)

### Subsystems in Config Base
- Cabin Management System (ATA-44-10)
- In-Flight Entertainment (ATA-44-20)
- Cabin Network (ATA-44-30)
- Connectivity (ATA-44-40)
- Passenger Power & USB (ATA-44-50)
- Lighting Control (ATA-44-60)

---

## ATA-50: Cargo & Load Systems

### Configuration Location
`02-AIRCRAFT/CONFIGURATION_BASE/ATA-50_CARGO_LOAD_SYSTEMS/`

### Contents
- **BASELINE/**: Cargo system configuration, ULD specifications
- **HW_CONFIG/**: PDU configs, lock specs, load cell configs
- **SW_BASELINE/**: Control software versions
- **PARAMS/**: Load limits, system parameters
- **ICD/**: Interface definitions
- **VERIFICATION/**: Load testing results
- **CHANGE_LOG/**: System changes

### Key Documents
- [ATA-50 README](../../../CONFIGURATION_BASE/ATA-50_CARGO_LOAD_SYSTEMS/README.md)
- [ATA-50 Baseline](../../../CONFIGURATION_BASE/ATA-50_CARGO_LOAD_SYSTEMS/BASELINE/)
- [ATA-50 Verification](../../../CONFIGURATION_BASE/ATA-50_CARGO_LOAD_SYSTEMS/VERIFICATION/)

### Subsystems in Config Base
- Main Deck Cargo (ATA-50-10)
- Lower Deck Cargo (ATA-50-20)
- ULDs and Locks (ATA-50-30)
- Power Drive Units (ATA-50-40)
- Load Sensing (ATA-50-50)
- Control Electronics (ATA-50-60)

---

## Configuration Management Rules

### What's in CONFIGURATION_BASE
- **Baseline configurations**: Approved, controlled configurations
- **Component specifications**: Part numbers, versions, suppliers
- **Hardware configurations**: LRU settings, installation data
- **Software baselines**: Software versions, load configurations
- **Parameters**: System parameters, limits, settings
- **Verification data**: Test results, certification artifacts

### What's in DOMAIN_INTEGRATION
- **Integration views**: How systems work together
- **Interface matrices**: Cross-system interfaces
- **PLM artifacts**: Design models, CAD/CAE data
- **Domain governance**: RASCI, safety boundaries, change rules
- **Architecture**: Domain context, dependencies, data contracts
- **Metrics**: Domain-level KPIs and performance data

### Change Control
- Changes to configuration baselines: Follow CCB process
- Changes to integration views: Domain owner approval
- Interface changes: Coordinated through ICN process

### Version Control
- Configuration items are version controlled
- Baselines are tagged and immutable
- Changes create new versions/baselines

## Related References

- [Configuration Rules](../../../CONFIGURATION_BASE/00-COMMON/RULES.md)
- [Global Change Log](../../../CONFIGURATION_BASE/00-COMMON/GLOBAL_CHANGE_LOG.csv)
- [Interface Management](../../../../00-PROGRAM/CONFIG_MGMT/09-INTERFACES/)

---

**Last Updated**: 2025-01-15
