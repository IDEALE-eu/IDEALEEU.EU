# ICD - Interface Control Documents

This directory contains Interface Control Documents (ICDs) that define system interfaces, data bus specifications, protocol definitions, and signal definitions.

## Purpose

ICDs establish formal agreements between interfacing systems, ensuring:
- Compatible interfaces
- Correct data exchange
- Protocol compliance
- Electrical/mechanical compatibility
- Coordinated development

## Contents

This directory should contain:

### Interface Specifications
- **Data bus interfaces** - ARINC 429, ARINC 664 (AFDX), MIL-STD-1553
- **Protocol definitions** - Communication protocols and message formats
- **Signal definitions** - Discrete signals, analog signals
- **Timing requirements** - Message rates, latencies, synchronization

### ICD Documents
- **System-to-system ICDs** - Interfaces between aircraft systems
- **Hardware ICDs** - Physical and electrical interfaces
- **Software ICDs** - API definitions, data structures
- **External ICDs** - Ground support equipment, test equipment

### Data Dictionaries
- **Message catalogs** - Complete list of messages and parameters
- **Parameter definitions** - Data types, ranges, scaling factors
- **Status words** - Bit definitions and meanings
- **Command words** - Control commands and responses

## File Organization

```
ICD/
├── ARINC_429/             # ARINC 429 bus interfaces
│   ├── ICD_[SYSTEM_A]_to_[SYSTEM_B].pdf
│   └── MESSAGE_CATALOG.csv
├── ARINC_664/             # AFDX network interfaces
├── DISCRETES/             # Discrete signal interfaces
├── ANALOG/                # Analog signal interfaces
└── API/                   # Software API definitions
```

## ICD Naming Convention

ICDs should be named to clearly identify the interface:
- `ICD_[SOURCE]_to_[DESTINATION].pdf`
- `ICD_[PROTOCOL]_[SYSTEM].pdf`
- `MESSAGE_CATALOG_[BUS_TYPE].csv`

## Interface Categories

### Data Bus Interfaces
- **ARINC 429**: Point-to-point digital data
- **ARINC 664 (AFDX)**: Switched Ethernet network
- **MIL-STD-1553**: Dual redundant data bus
- **CAN Bus**: Controller Area Network
- **RS-422/485**: Serial data links

### Signal Interfaces
- **Discrete Signals**: On/off, open/close status
- **Analog Signals**: Voltage, current measurements
- **PWM Signals**: Pulse-width modulated control
- **Frequency Signals**: RPM, frequency measurements

### Physical Interfaces
- **Connectors**: Type, pin assignments, mates
- **Power Interfaces**: Voltage, current, grounding
- **Mechanical Interfaces**: Mounting, clearances
- **Optical Interfaces**: Fiber optic connections

## ICD Development Process

1. **Requirements Analysis** - Identify interface needs
2. **Preliminary ICD** - Draft interface definition
3. **Coordination** - Agreement between parties
4. **Formal Release** - Approved ICD baseline
5. **Change Control** - Manage interface changes
6. **Verification** - Test interface compliance

## Interface Management

ICDs must be:
- **Bilaterally approved** - Agreement by both parties
- **Version controlled** - Tracked in configuration management
- **Traceable** - Linked to system requirements
- **Testable** - Verification criteria defined

## Change Control

Interface changes require:
- Interface Change Notice (ICN)
- Impact analysis on both systems
- Coordination between affected parties
- CCB approval
- Update to interface test procedures

## Cross-References

Interfaces typically involve:
- **ATA-42**: IMA platform (hosted applications)
- **ATA-92**: EWIS (all wiring)
- Other system chapters (functional interfaces)

## EWIS Coordination

⚠️ **Important**: Physical wiring for all interfaces is documented in **ATA-92_EWIS**. ICDs define the logical interface; wiring docs define physical implementation.

## References

- [Configuration Rules](../../ATA-00_GENERAL/RULES.md)
- [Interface Management](../../../../00-PROGRAM/CONFIG_MGMT/09-INTERFACES/)
- [ATA-92 EWIS](../ATA-92_EWIS/) (for wiring)

## Standards and Protocols

Common interface standards:
- **ARINC 429**: Digital Information Transfer System
- **ARINC 664**: Aircraft Data Network
- **ARINC 653**: Avionics Application Software Standard Interface
- **ARINC 825**: CAN Aerospace
- **MIL-STD-1553**: Digital Time Division Command/Response Multiplex Data Bus
- **IEEE 1394**: High-speed serial bus

## Verification

Interface verification includes:
- **Requirements traceability** - All interface requirements covered
- **Design verification** - Design meets ICD requirements
- **Integration testing** - Interface functions correctly
- **Compliance testing** - Meets protocol standards

---

**Status**: Active  
**Owner**: Systems Engineering  
**Last Updated**: 2024-01-15
