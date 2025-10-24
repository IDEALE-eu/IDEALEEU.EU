# ATA-42 INTEGRATED MODULAR AVIONICS

Integrated Modular Avionics (IMA) platform configuration following ARINC 653 standards.

## Overview

This chapter contains the complete configuration for the aircraft IMA platform, including module configurations, partition definitions, hosted applications, and resource allocations.

## System Description

The IMA system provides:
- Shared computing platform for multiple avionics functions
- ARINC 653 partitioned operating environment
- Time and space partitioning for application isolation
- Standardized interfaces and communication
- Resource management and monitoring

## Directory Contents

### PARAMS/
System parameters and allocations:
- `PARTITION_MAP.csv` - Partition definitions and resource allocations
- `CPU_ALLOCATIONS.csv` - CPU percentage allocations per partition
- `MEMORY_ALLOCATIONS.csv` - Memory allocations per partition
- `TIMING_BUDGETS.csv` - Timing windows and periods
- `THRESHOLD_LIMITS.csv` - Monitoring thresholds

### BASELINE/
Platform baseline configurations:
- `IMA_PLATFORM_CONFIG.xml` - ARINC 653 configuration (primary)
- `MODULE_MAP.csv` - Physical module locations and IDs
- `PARTITION_BINDINGS.csv` - Application-to-partition bindings
- System architecture baseline

### HW_CONFIG/
Hardware configuration:
- IMA chassis specifications
- Module cards and slots
- Processor configurations
- Memory modules
- Cooling systems
- Power distribution
- Backplane and interconnect

### SW_BASELINE/
Software baselines:
- ARINC 653 operating system version
- Hosted application binaries and versions
- Partition executable load files
- Health monitoring software
- Configuration management tools

### ICD/
Interface control documents:
- `ICD_ARINC653_API.pdf` - ARINC 653 API specification
- `ICD_INTER_PARTITION_COMM.pdf` - Inter-partition communication
- `ICD_MODULE_INTERFACES.pdf` - Module-level interfaces
- ARINC 664 (AFDX) network interface specifications
- ARINC 429 interface specifications

### VERIFICATION/
Verification and validation:
- Partition isolation test results
- Boot sequence verification
- Failover and fault tolerance tests
- Timing analysis results
- DO-178C/DO-254 compliance evidence
- Integration test results

### CHANGE_LOG/
Chapter-specific change history

## ARINC 653 Configuration

### Partition Management
Each partition is defined with:
- Unique partition ID
- Memory allocation (isolated address space)
- CPU time allocation (cyclic scheduling)
- Period and duration
- Criticality level (DAL-A through DAL-E)
- Entry point and initialization

### Module Configuration
Each IMA module includes:
- Module ID and name
- Processor cores and architecture
- Total memory capacity
- Operating system version
- Hosted partitions list
- Network interfaces

### Inter-Partition Communication
Communication between partitions via:
- Sampling ports (periodic data)
- Queuing ports (event-driven messages)
- Channels with defined refresh rates
- Message size limits
- Buffer configurations

## Hosted Applications

Applications hosted on IMA platform include functions from:
- **ATA-22**: Auto flight control applications
- **ATA-23**: Communication management
- **ATA-27**: Flight control laws
- **ATA-31**: Display management
- **ATA-34**: Navigation processing
- **ATA-45**: Central maintenance computing

Each application documented in its functional ATA chapter with:
- Functional requirements → System chapter (e.g., ATA-27)
- Software binary and partition binding → ATA-42/SW_BASELINE/
- Interface requirements → System chapter ICD/ directory

## Key Interfaces

- **All Avionics Systems**: IMA provides computing platform
- **ATA-24**: Electrical power (28V DC, 115V AC)
- **ATA-21**: Cooling air supply
- **ATA-92**: EWIS (all wiring to/from IMA modules)

## Configuration Rules

Per [Configuration Rules](../ATA-00_GENERAL/RULES.md):

1. **IMA modules and chassis** → ATA-42/HW_CONFIG/
2. **Partition definitions** → ATA-42/PARAMS/
3. **Hosted application binaries** → ATA-42/SW_BASELINE/
4. **Application functional requirements** → Host system chapter (e.g., ATA-27)
5. **Application-to-partition binding** → Documented in BASELINE/PARTITION_BINDINGS.csv

## Special Considerations

### Safety and Criticality
- Mixed-criticality hosting (DAL-A through DAL-E)
- Partition isolation enforcement
- Independent verification of isolation
- Fail-safe and fault tolerance

### Resource Management
- CPU allocation not to exceed 100% per core
- Memory allocations with margins for overhead
- Timing budgets with analysis margins
- Deterministic scheduling verification

### Certification
- DO-178C for software (by DAL level)
- DO-254 for hardware
- DO-297 for IMA platform integration
- ARINC 653 compliance

## Related Documents

- [Configuration Rules](../ATA-00_GENERAL/RULES.md)
- [IMA Config Template](../ATA-00_GENERAL/TEMPLATES/IMA_CONFIG.xml)
- [Partition Map Template](../ATA-00_GENERAL/TEMPLATES/PARTITION_MAP.csv)
- [Global Change Log](../ATA-00_GENERAL/GLOBAL_CHANGE_LOG.csv)

## Standards References

- **ARINC 653**: Avionics Application Software Standard Interface
- **ARINC 664**: Aircraft Data Network (AFDX)
- **ARINC 429**: Digital Information Transfer System
- **DO-297**: Integrated Modular Avionics Development Guidance
- **DO-178C**: Software Considerations in Airborne Systems
- **DO-254**: Design Assurance Guidance for Airborne Electronic Hardware

## Contacts

- **System Owner**: Avionics Systems Engineering
- **Configuration Owner**: Configuration Management
- **Software Configuration**: Software Engineering

---

**Last Updated**: 2024-01-15
