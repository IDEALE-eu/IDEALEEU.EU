# HW_CONFIG - Hardware Configuration

This directory contains hardware configuration data including LRU (Line Replaceable Unit) configurations, physical connections, installation specifications, and part numbers.

## Purpose

Hardware configuration documentation ensures:
- Correct component selection and installation
- Proper physical interfaces and connections
- Traceability to design requirements
- Support for maintenance and logistics
- Configuration control of hardware items

## Contents

This directory should contain:

### LRU Configurations
- **Component specifications** - Technical data for each LRU
- **Part numbers** - Manufacturer and internal part numbers
- **Variants and options** - Different configurations and alternatives
- **Interchangeability data** - Substitutable components

### Physical Configuration
- **Installation drawings** - Mounting locations and arrangements
- **Connector pinouts** - Electrical and data connections
- **Harness routings** - Cable and wire routing paths
- **Interface definitions** - Physical interface specifications

### Hardware Documentation
- **Datasheets** - Manufacturer specifications
- **Assembly procedures** - Installation instructions
- **Test procedures** - Acceptance and functional tests
- **Maintenance manuals** - Repair and troubleshooting guides

## File Organization

```
HW_CONFIG/
├── LRU_[NAME]/            # Individual LRU configurations
│   ├── SPECIFICATIONS.pdf
│   ├── PART_NUMBERS.csv
│   ├── INSTALLATION.pdf
│   └── TEST_PROCEDURES.pdf
├── CONNECTORS/            # Connector definitions
├── ASSEMBLIES/            # Hardware assemblies
└── BOM/                   # Bills of materials
```

## LRU Placement Rules

Per [Configuration Rules](../../ATA-00_GENERAL/RULES.md):
- LRUs reside in their **primary functional ATA chapter**
- Related hardware stays together with host system
- Cross-reference other chapters when interfaces exist

## Hardware Categories

### Electronic LRUs
- Computers and processors
- Controllers and interfaces
- Sensors and transducers
- Power supplies and converters

### Mechanical LRUs
- Actuators and servos
- Valves and pumps
- Structural components
- Mechanical assemblies

### Electrical LRUs
- Circuit breakers and relays
- Switches and indicators
- Transformers and inductors
- Wiring harnesses (reference ATA-92)

## Configuration Data Requirements

Each hardware item should document:
- **Identification** - Part number, serial number, nomenclature
- **Specifications** - Technical performance characteristics
- **Interfaces** - Physical, electrical, data connections
- **Installation** - Mounting, routing, adjustment procedures
- **Testing** - Acceptance criteria and test methods
- **Maintenance** - Service intervals, repair procedures

## Change Control

Hardware configuration changes require:
- Engineering Change Request (ECR)
- Impact analysis on interfaces and installation
- CCB approval
- Update to related ICDs and wiring (ATA-92)
- Documentation in CHANGE_LOG

## Wiring Note

⚠️ **Important**: All wiring configurations reside in **ATA-92_EWIS** per EWIS rules. Hardware chapters only reference wiring interfaces.

## References

- [Configuration Rules](../../ATA-00_GENERAL/RULES.md)
- [Part Numbering](../../../../00-PROGRAM/CONFIG_MGMT/02-PART_NUMBERING.md)
- [Item Master](../../../../00-PROGRAM/CONFIG_MGMT/08-ITEM_MASTER/)
- [ATA-92 EWIS](../ATA-92_EWIS/) (for wiring)

## Environmental Requirements

Hardware must comply with:
- **DO-160**: Environmental conditions and test procedures
- Temperature ranges and thermal management
- Vibration and shock requirements
- EMI/EMC requirements
- Altitude and pressure requirements

---

**Status**: Active  
**Owner**: Systems Engineering  
**Last Updated**: 2024-01-15
