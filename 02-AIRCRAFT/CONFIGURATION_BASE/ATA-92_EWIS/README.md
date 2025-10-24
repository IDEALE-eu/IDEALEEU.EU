# ATA-92 EWIS

Electrical Wiring Interconnection System - Centralized repository for ALL aircraft wiring configurations.

## Overview

Per configuration rules, ATA-92 contains ALL electrical wiring configurations for the entire aircraft. No wiring information is stored in other ATA chapters.

## Purpose

This chapter serves as the single source of truth for:
- Wire specifications and routing
- Harness assemblies and configurations
- Connector and splice definitions
- Zone wire lists
- Shielding and grounding specifications
- Wire protection and installation standards

## Regulatory Context

EWIS is subject to specific FAA/EASA regulatory requirements:
- FAA SFAR 88 (Special Federal Aviation Regulation)
- EASA CS-25 Amendment 15
- Enhanced inspection and maintenance
- Enhanced training requirements
- Aging aircraft considerations

## Directory Contents

### PARAMS/
Wire specifications and parameters:
- `WIRE_GAUGE_SPECS.csv` - Wire gauge specifications (AWG/mm²)
- `SHIELDING_SPECS.csv` - Shielding requirements by circuit type
- `ZONE_DEFINITIONS.csv` - Aircraft zone definitions for wire routing
- `WIRE_DERATING.csv` - Current derating factors
- `ENVIRONMENTAL_RATINGS.csv` - Temperature and environmental ratings
- `GROUNDING_SPECS.csv` - Grounding and bonding requirements

### BASELINE/
Wiring baseline configurations:
- `HARNESS_ASSEMBLIES.xml` - Complete harness definitions
- `BACKSHELL_CONFIGS.csv` - Backshell and connector accessories
- `WIRE_LISTS_BY_ZONE.csv` - Wire lists organized by aircraft zone
- `ROUTING_PATHS.csv` - Approved wire routing paths
- Baseline snapshots at major gates

### HW_CONFIG/
Hardware components:
- `CONNECTORS.csv` - Connector part numbers and specifications
- `SPLICES.csv` - Splice specifications and locations
- `TERMINATIONS.csv` - Termination methods and hardware
- `WIRE_TIES_CLAMPS.csv` - Wire support hardware
- `CONDUIT_SPECS.csv` - Conduit and protection specifications
- `BREAKOUTS.csv` - Breakout locations and configurations

### SW_BASELINE/
Software baselines (rare, typically none):
- Wire harness design tools configuration
- Automated test equipment software
- Wire identification database

### ICD/
Interface control documents and standards:
- `ICD_ARINC622.pdf` - ARINC 622 (Wire Marking)
- `ICD_ARINC615.pdf` - ARINC 615 (Software Data Loader - for wire ID systems)
- `ICD_ZONE_SPECS.pdf` - Zone interface specifications
- `ICD_CONNECTOR_PIN_ASSIGNMENTS.pdf` - Connector pinout standards
- Electrical interface specifications for all systems

### VERIFICATION/
Verification and validation:
- `CONTINUITY_TEST_PROCEDURES.pdf` - Continuity test procedures
- `CONTINUITY_TEST_RESULTS.csv` - Test results by harness
- `IR_TEST_PROCEDURES.pdf` - Insulation resistance test procedures
- `IR_TEST_RESULTS.csv` - IR test results
- `ARC_FAULT_TESTS.pdf` - Arc fault circuit breaker tests
- `HIPOT_TEST_RESULTS.csv` - High-potential test results
- `INSTALLATION_VERIFICATION.pdf` - Installation inspection results
- Certification compliance evidence

### CHANGE_LOG/
Wiring-specific change history:
- All wire routing changes
- Harness modifications
- Connector changes
- Installation changes

## Organization Principles

### By Aircraft Zone
Wiring organized by aircraft zone:
- Zone 100-199: Fuselage sections
- Zone 200-299: Wings
- Zone 300-399: Empennage
- Zone 400-499: Powerplant
- Zone 500-599: Landing gear
- Zone 600-699: Doors
- Zone 700-799: Auxiliary systems

### By System Connection
Cross-reference to system ATA chapters:
- Each wire/harness tagged with connected system
- Example: "FCC-001-HARNESS → Connects ATA-27 (Flight Controls)"
- System chapters reference ATA-92 for wiring details

### By Harness Assembly
Complete harness assemblies with:
- Harness part number
- Bill of materials (wires, connectors, splices)
- Installation drawing reference
- Zone routing
- Connected systems

## Configuration Rules

### Rule: ALL Wiring in ATA-92

**Stored in ATA-92**:
- ✓ Wire specifications and routing
- ✓ Harness assemblies
- ✓ Connector pinout definitions
- ✓ Splice locations
- ✓ Shielding configurations
- ✓ Grounding points

**NOT stored in system chapters** (e.g., ATA-27):
- ❌ Wire routing
- ❌ Harness configurations
- ❌ Connector pinouts
- ❌ Wire gauge selections

**Allowed in system chapters**:
- ✓ LRU connector type/part number (without pinouts)
- ✓ Reference to ATA-92 for wiring details
- ✓ Electrical interface requirements (signal type, voltage, current)

## Key Interfaces

### All Systems
ATA-92 provides wiring to ALL aircraft systems:
- ATA-21 through ATA-80: System power and signal wiring
- ATA-24: Main electrical power distribution
- ATA-26: Fire detection and suppression wiring
- ATA-27: Flight control signal wiring
- ATA-28: Fuel system sensor wiring
- ATA-42: IMA module interconnections
- And all other systems...

### Special Considerations

**High-Power Wiring** (ATA-24):
- Main generator feeders
- Bus tie cables
- Heavy loads
- Circuit protection coordination

**Shielded Signal Wiring**:
- Avionics data buses (ARINC 429, ARINC 664)
- Sensor signals
- Communication RF cables
- Navigation signals

**Critical Wiring**:
- Flight control wiring (redundant paths)
- Engine control (FADEC)
- Fire detection loops
- Emergency systems

## Wire Identification Standards

### Wire Marking (ARINC 622)
- System code
- Wire number
- Segment identifier
- Gauge designation

Example: `27-1234-A-20` (ATA-27, wire 1234, segment A, 20 AWG)

### Harness Marking
- Harness part number
- Installation location
- Maintenance level
- Critical path designation

## Testing and Verification

### Pre-Installation Testing
- Continuity verification
- Insulation resistance (IR)
- High-potential (Hi-Pot) testing
- Shield continuity

### Post-Installation Testing
- Point-to-point continuity
- IR testing per zone
- Functional testing
- Arc fault circuit breaker verification

### Periodic Inspection
- Visual inspection per maintenance schedule
- Chafe and wear inspection
- Connector inspection
- Compliance with aging aircraft programs

## Safety and Certification

### Safety Considerations
- Wire separation requirements (power vs. signal)
- Redundant path protection
- Fire zone wiring protection
- Moisture and fluid protection
- Electromagnetic interference (EMI) control

### Certification Evidence
- DO-160 environmental testing
- Installation compliance
- Maintenance program approval
- Training program documentation

## Related Documents

- [Configuration Rules](../ATA-00_GENERAL/RULES.md) - Rule 3: EWIS Centralization
- [Global Change Log](../ATA-00_GENERAL/GLOBAL_CHANGE_LOG.csv)
- System ICD directories in respective ATA chapters (for signal definitions)

## Standards References

- **ARINC 622**: Design Guidance for Wire Marking
- **ARINC 615**: Software Data Loader
- **MIL-W-5088**: Military wire specifications
- **SAE AS50881**: Wiring Aerospace Vehicle
- **FAA AC 43.13-1B**: Acceptable Methods, Techniques, and Practices
- **DO-160**: Environmental Conditions and Test Procedures

## Contacts

- **System Owner**: Electrical Systems Engineering
- **Configuration Owner**: Configuration Management
- **EWIS Specialist**: EWIS Engineering Team
- **Certification**: Certification Engineering

---

**Last Updated**: 2024-01-15

**Important**: All personnel must be trained on EWIS requirements before working with wire configurations.
