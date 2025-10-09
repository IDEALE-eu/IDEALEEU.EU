# ATA-42 INTEGRATED MODULAR AVIONICS - Integration View

## Overview

Integrated Modular Avionics (IMA) platform integration covering IMA chassis, modules, ARINC 653 partitions, and network gateways (AFDX/ARINC 429).

## System Architecture

### IMA Platform
- **Cabinet**: Physical chassis with power supply and backplane
- **Core Processing Modules (CPM)**: Host ARINC 653 partitions
- **I/O Modules (IOM)**: ARINC 429, discrete I/O, analog I/O
- **Network Modules**: AFDX switch cards
- **Gateway Modules**: Bridge between AFDX and ARINC 429

### ARINC 653 Partitioning
- **Spatial Partitioning**: Memory isolation between applications
- **Temporal Partitioning**: Deterministic scheduling (Major Frame/Minor Frame)
- **Resource Partitioning**: CPU, memory, I/O allocation per partition

### Hosted Applications
- FMS (ATA-34)
- AFCS (ATA-22)
- Communication processors (ATA-23)
- Display management (ATA-31)
- Other avionics applications

## Key Interfaces

### Internal Interfaces
- **42 ↔ 22**: AFCS partitions hosted on IMA
- **42 ↔ 23**: Communication application partitions
- **42 ↔ 24**: Electrical power supply
- **42 ↔ 31**: Display management partitions
- **42 ↔ 34**: FMS partitions hosted on IMA
- **42 ↔ 45**: CMC monitoring via health messages
- **42 ↔ 46**: Software loading (partitions and IMA OS)
- **42 ↔ 92**: EWIS (all wiring in ATA-92)

### Network Gateways
- **AFDX ↔ ARINC 429**: Gateway modules for legacy equipment
- **Multiple AFDX VLs**: Virtual Links with QoS and BAG (Bandwidth Allocation Gap)

## Network Integration

### AFDX (ARINC 664 Part 7)
- Full-duplex switched Ethernet
- Virtual Links (VL) with guaranteed bandwidth
- Redundant networks (A and B)
- QoS and deterministic latency

### ARINC 429
- Legacy interfaces for sensors and actuators
- Gateway modules bridge to AFDX
- Multiple buses (typically 10-50+ buses)

## Subsystems

### ATA-42-10: IMA CHASSIS/MODULES
- IMA cabinets with redundancy
- Core Processing Modules (CPM)
- I/O Modules (IOM)
- Power supply modules
- Network switch modules

### ATA-42-90: PARTITION MAP/APPS
- Partition allocation to applications
- Major Frame and Minor Frame schedules
- Memory budgets per partition
- Health monitoring strategy
- See partition map templates in 08-TEMPLATES/

## Partition Map

The partition map is critical for IMA integration. See ATA-42-90 subsystem for:
- Application-to-partition mapping
- Partition scheduling (Major Frame table)
- Resource allocation (CPU %, memory)
- Inter-partition communication (via AFDX VLs or APEX ports)

Example partition allocation:
```
Partition ID | Application      | Module | CPU % | Memory | Schedule
P1          | FMS-Primary      | CPM-1  | 25%   | 64 MB  | 0-25ms
P2          | AFCS-Primary     | CPM-1  | 20%   | 32 MB  | 25-45ms
P3          | COMM-ACARS       | CPM-2  | 15%   | 16 MB  | 0-15ms
P4          | Display-Mgmt     | CPM-2  | 30%   | 128 MB | 15-45ms
...
```

## PLM Integration

All hardware and software artifacts link to CONFIGURATION_BASE for authoritative configurations:
- **Hardware**: CONFIGURATION_BASE/ATA-42_INTEGRATED_MODULAR_AVIONICS/HW_CONFIG/
- **Software**: CONFIGURATION_BASE/ATA-42_INTEGRATED_MODULAR_AVIONICS/SW_BASELINE/ (IMA OS)
  - Hosted application SW in their respective ATA chapters (e.g., FMS in ATA-34/SW_BASELINE/)
- **Interfaces**: CONFIGURATION_BASE/ATA-42_INTEGRATED_MODULAR_AVIONICS/ICD/

PLM folders in this domain contain:
- **EBOM_LINKS.md**: References to engineering BOMs in CONFIGURATION_BASE
- **CAx/**: Integration artifacts (partition schedules, network topology, resource budgets)

## Compliance

### Applicable Standards
- **ARINC 653**: Avionics Application Software Standard Interface (APEX)
- **ARINC 664 Part 7**: AFDX network specification
- **DO-178C**: Software (IMA OS, typically DAL A; hosted apps per their criticality)
- **DO-254**: Hardware (IMA modules)
- **DO-160**: Environmental testing
- **DO-297**: IMA Development and Integration Guidance

### Certification Considerations
- IMA OS certification (typically DAL A)
- Hosted application isolation verification
- Partition scheduling analysis (WCET, jitter)
- Network performance (VL latency, bandwidth)

## Verification Requirements

### Integration Testing
- Partition isolation verification
- Deterministic scheduling validation
- Network performance (VL latency, BAG compliance)
- Gateway functionality (AFDX ↔ ARINC 429)

### Interface Testing
- APEX port communication between partitions
- AFDX VL data integrity
- ARINC 429 gateway validation
- Health monitoring messages

### Timing Analysis
- Worst-Case Execution Time (WCET) analysis
- Major Frame schedule feasibility
- Network latency budgets
- Partition scheduling jitter

## Known Issues & Risks

### Technical Risks
- Partition overruns affecting other applications
- Network congestion causing VL drops
- Gateway latency impacting real-time performance
- IMA module failures requiring partition migration

### Mitigation Strategies
- Conservative CPU and memory budgets (30% margin)
- Rigorous WCET analysis and testing
- Redundant IMA modules with partition replication
- Health monitoring and automatic failover

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2024-01-15 | Systems Integration | Initial integration view |

## References

- [Interface Matrix](./INTERFACE_MATRIX/42↔22_23_24_31_34_45_46_92.csv)
- [Partition Map](./SUBSYSTEMS/ATA-42-90_PARTITION_MAP_APPS/)
- [CONFIGURATION_BASE/ATA-42](../../../CONFIGURATION_BASE/ATA-42_INTEGRATED_MODULAR_AVIONICS/)
- [CONFIG_MGMT ICDs](../../../../00-PROGRAM/CONFIG_MGMT/09-INTERFACES/)
- [Avionics Networks](../../03-INTEGRATION_VIEWS/AVIONICS_NETWORKS.md)
- [Partition Map Template](../../08-TEMPLATES/A653_PARTITION_MAP_TEMPLATE.csv)
