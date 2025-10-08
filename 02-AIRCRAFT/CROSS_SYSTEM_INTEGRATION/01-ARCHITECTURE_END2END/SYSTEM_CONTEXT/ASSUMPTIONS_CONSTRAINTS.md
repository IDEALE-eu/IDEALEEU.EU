# System Assumptions and Constraints

## Overview

This document captures the key assumptions and constraints that guide the aircraft cross-system integration design.

## Design Assumptions

### Environmental Assumptions
- **Operating Altitude**: Sea level to 45,000 ft (13,700 m)
- **Operating Temperature**: -55°C to +55°C ambient
- **Operating Pressure**: 1013 hPa to 187 hPa
- **Humidity**: 0% to 100% RH, condensing
- **Lightning Environment**: Per DO-160G Category A
- **HIRF Environment**: Per DO-160G Category T

### Operational Assumptions
- **Flight Duration**: Maximum 12 hours continuous operation
- **Dispatch Reliability**: Target 99.5% dispatch rate
- **Mean Time Between Failures (MTBF)**: System-specific, documented in domain integration folders
- **Maintenance Intervals**: Aligned with MSG-3 analysis
- **Crew Complement**: 2 pilots minimum (single pilot ops not assumed)
- **Passenger Capacity**: Per aircraft variant specification

### System Assumptions
- **Power Availability**: Dual-redundant electrical power available during normal operations
- **Network Reliability**: Redundant network paths per AFDX standard
- **Time Reference**: GNSS available for precision time synchronization
- **Data Storage**: Non-volatile storage survives power loss
- **Software Updates**: Ground-based only, no in-flight software updates

## Design Constraints

### Regulatory Constraints
- **Certification Basis**: CS-25 / FAR Part 25 for large aircraft
- **Software**: DO-178C up to DAL A for critical functions
- **Hardware**: DO-254 up to Design Assurance Level A for critical hardware
- **Systems**: ARP4754A development process
- **Security**: DO-326A airworthiness security requirements
- **Environmental**: DO-160G environmental qualification
- **EMC**: DO-160G Section 25 (EMI), Section 21 (emissions)

### Physical Constraints
- **Weight Budget**: Aircraft-level weight constraint per configuration
- **Volume**: Equipment bay volume allocations per zone
- **Cooling**: Air-cooled equipment, no liquid cooling in pressurized zones
- **Mounting**: Standard ARINC mounting (MCU, MCDU, etc.)
- **Connectors**: Industry-standard connectors (D38999, ARINC 600, etc.)

### Electrical Constraints
- **Supply Voltage**: 28 VDC ±4V nominal, 115 VAC 400Hz 3-phase
- **Power Budget**: System-level power budget per [04-POWER_THERMAL_CROSSLOAD/POWER_BUDGET.csv](../../04-POWER_THERMAL_CROSSLOAD/POWER_BUDGET.csv)
- **Inrush Current**: Maximum 3x steady-state, <100ms duration
- **Brownout Tolerance**: Systems must tolerate 18 VDC for 50ms
- **EMI/EMC**: Per DO-160G Section 21/25 limits

### Network Constraints
- **AFDX Bandwidth**: 100 Mbps per port, VL allocation per [02-NETWORKS_DATA_BUS/LOGICAL/AFDX_VL_MAP.csv](../../02-NETWORKS_DATA_BUS/LOGICAL/AFDX_VL_MAP.csv)
- **ARINC 429 Rate**: High-speed (100 kbps) or low-speed (12.5 kbps)
- **CAN Bus**: 1 Mbps maximum, identifier allocation per [02-NETWORKS_DATA_BUS/LOGICAL/CAN_IDS.csv](../../02-NETWORKS_DATA_BUS/LOGICAL/CAN_IDS.csv)
- **Latency**: End-to-end latency budgets per functional chain
- **Jitter**: Network jitter limits per [02-NETWORKS_DATA_BUS/QOS_TIMING/](../../02-NETWORKS_DATA_BUS/QOS_TIMING/)

### Timing Constraints
- **Time Synchronization**: ±1 μs across critical systems (PTP IEEE 1588)
- **Determinism**: Time-Triggered Ethernet (TTE) for critical control loops
- **Update Rates**: Per functional chain requirements
- **Latency Budgets**: Documented in [01-ARCHITECTURE_END2END/FUNCTIONAL_CHAINS/LATENCY_BUDGETS.csv](../FUNCTIONAL_CHAINS/LATENCY_BUDGETS.csv)

### Software Constraints
- **ARINC 653**: Partitioned operating system for IMA
- **Partition Isolation**: Time and space partitioning per ARINC 653
- **Memory**: Static allocation, no dynamic memory in critical partitions
- **Scheduling**: Rate-monotonic or fixed-priority scheduling
- **Inter-Partition Comms**: Queuing and sampling ports only, no shared memory

### Thermal Constraints
- **Operating Temperature**: Equipment internal temperature <85°C
- **Storage Temperature**: -55°C to +85°C non-operating
- **Thermal Dissipation**: Per equipment, tracked in [04-POWER_THERMAL_CROSSLOAD/THERMAL_BUDGET.csv](../../04-POWER_THERMAL_CROSSLOAD/THERMAL_BUDGET.csv)
- **Cooling Airflow**: Minimum 200 LFM (linear feet per minute) for air-cooled LRUs

### Safety Constraints
- **DAL Allocation**: Per ARP4754A, documented in [01-ARCHITECTURE_END2END/FUNCTIONAL_CHAINS/DAL_ALLOCATION.csv](../FUNCTIONAL_CHAINS/DAL_ALLOCATION.csv)
- **Common Cause Analysis**: Independence requirements per DO-178C/DO-254
- **Fault Tolerance**: Fail-safe or fail-operational per system criticality
- **FDIR**: Automatic fault detection, isolation, and recovery for critical functions
- **Reversibility**: Critical functions must be reversible/overrideable by crew

### Security Constraints
- **Cyber Boundaries**: Zones and conduits per [02-NETWORKS_DATA_BUS/CYBER_BOUNDARIES.md](../../02-NETWORKS_DATA_BUS/CYBER_BOUNDARIES.md)
- **Cryptographic Anchors**: Hardware roots of trust for critical systems
- **Data Protection**: Encryption for sensitive data at rest and in transit
- **Access Control**: Role-based access for maintenance and configuration
- **Audit Logging**: Security-relevant events logged and protected

## Derived Requirements

These assumptions and constraints drive derived requirements documented in:
- **Functional Requirements** - [00-PROGRAM/DIGITAL_THREAD/04-MBSE/REQUIREMENTS_ALLOCATION.csv](../../../../00-PROGRAM/DIGITAL_THREAD/04-MBSE/REQUIREMENTS_ALLOCATION.csv)
- **Interface Requirements** - [01-ARCHITECTURE_END2END/INTERFACE_MATRIX/INTERFACE_MATRIX.csv](../INTERFACE_MATRIX/INTERFACE_MATRIX.csv)
- **Verification Requirements** - [07-INTEGRATION_TEST/TEST_SPECIFICATIONS/](../../07-INTEGRATION_TEST/TEST_SPECIFICATIONS/)

## Change Control

Changes to assumptions or constraints require:
1. **ECR Submission** - Via [00-PROGRAM/CONFIG_MGMT/06-CHANGES/](../../../../00-PROGRAM/CONFIG_MGMT/06-CHANGES/)
2. **Impact Analysis** - Assess ripple effects on design
3. **CCB Approval** - Configuration Control Board review
4. **Baseline Update** - Update configuration baseline

## References
- **ARP4754A** - Section 4.2, Design Constraints
- **DO-178C** - Appendix A, Design Considerations
- **DO-160G** - Environmental test procedures
- **CS-25** - Certification specifications

## Revision History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2024-10-08 | Systems Architecture Team | Initial assumptions and constraints |
