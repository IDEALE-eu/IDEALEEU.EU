# ATA-27 FLIGHT CONTROLS

Flight control system configuration.

## Overview

This chapter contains the complete configuration for the aircraft flight control system, including primary and secondary flight control surfaces, actuators, and control laws.

## System Description

The flight control system includes:
- Primary flight controls (ailerons, elevators, rudder)
- Secondary flight controls (flaps, slats, spoilers)
- Flight control computers (FCC)
- Actuators and servos
- Control laws and algorithms
- Redundancy and voting logic

## Directory Contents

### PARAMS/
- Control surface limits and rates
- Actuator performance specifications
- Control law parameters
- Redundancy thresholds
- Self-test parameters

### BASELINE/
- System architecture baseline
- FCC configurations
- Surface assignments
- Redundancy architecture

### HW_CONFIG/
- Flight Control Computers (FCC) - LRU configurations
- Actuators and servos
- Position sensors and transducers
- Mechanical linkages (if any)
- Interface units

### SW_BASELINE/
- FCC application software versions
- Control law software
- Built-In-Test (BIT) software
- Boot loaders and firmware

### ICD/
- Interface to cockpit controls (ATA-25)
- Interface to air data system (ATA-34)
- Interface to IMA platform (ATA-42) if hosted
- ARINC 429/664 interface specifications
- Actuator command interfaces

### VERIFICATION/
- Control law verification tests
- Actuator performance tests
- Redundancy and failover tests
- DO-178C compliance evidence (DAL-A)
- DO-254 compliance evidence
- Flight test data

### CHANGE_LOG/
Chapter-specific change history

## Key Interfaces

- **ATA-22**: Auto flight (autopilot commands)
- **ATA-25**: Cockpit controls (pilot inputs)
- **ATA-34**: Air data (for flight envelope protection)
- **ATA-42**: IMA platform (if FCC hosted on IMA)
- **ATA-92**: EWIS (all wiring to FCCs and actuators)

## Safety Considerations

Flight controls are **safety-critical** (DAL-A):
- Redundant architectures (typically triple or quadruple)
- Dissimilar redundancy where applicable
- Comprehensive failure detection and isolation
- Fail-safe and fail-operational design
- Extensive verification and validation

## Related Documents

- [Configuration Rules](../ATA-00_GENERAL/RULES.md)
- [Global Change Log](../ATA-00_GENERAL/GLOBAL_CHANGE_LOG.csv)

## Standards References

- **DO-178C**: Software (DAL-A)
- **DO-254**: Hardware (DAL-A)
- **ARP-4754A**: Development of civil aircraft systems
- **DO-160**: Environmental testing

## Contacts

- **System Owner**: Flight Controls Engineering
- **Configuration Owner**: Configuration Management

---

**Last Updated**: 2024-01-15
