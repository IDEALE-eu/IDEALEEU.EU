# AVIONICS_INTERFACES

Avionics interface and data bus standards.

## Overview

This directory contains standards for avionics interfaces and data buses, including ARINC specifications for various communication protocols.

## Applicable Standards

### ARINC 429 - Mark 33 Digital Information Transfer System (DITS)
- **Type**: Serial data bus
- **Characteristics**: Unidirectional, point-to-point, self-clocking
- **Speed**: 12.5 or 100 kbps
- **Usage**: Widely used for avionics equipment communication
- **Data Format**: 32-bit words (label, SDI, data, SSM, parity)

### ARINC 629 - Multi-Transmitter Data Bus
- **Type**: Serial data bus
- **Characteristics**: Bidirectional, multi-drop
- **Speed**: 2 Mbps
- **Usage**: Boeing 777, 747-400 (less common now)
- **Topology**: Linear bus with stubs

### ARINC 653 - Avionics Application Software Standard Interface
- **Type**: Software partitioning API
- **Purpose**: Define standard API for IMA applications
- **Services**: Process management, time management, partition communication, health monitoring
- **Versions**: Part 1 (Required Services), Part 2-4 (Extended Services)
- **See also**: 02-AIRCRAFT/IMA/ for DO-297 IMA standards

### ARINC 661 - Cockpit Display System Interfaces to User Systems
- **Purpose**: Define interface between display system and user applications
- **Benefits**: Portable cockpit applications, vendor independence
- **Protocol**: Server (CDS) and clients (User Applications)

### ARINC 664 - Aircraft Data Network (ADN)
- **Also known as**: AFDX (Avionics Full-Duplex Switched Ethernet)
- **Type**: Deterministic Ethernet network
- **Speed**: 10/100 Mbps full-duplex
- **Characteristics**:
  - Switched Ethernet with deterministic behavior
  - Virtual Links (VLs) for guaranteed bandwidth
  - BAG (Bandwidth Allocation Gap) timing
  - Redundant networks (A and B)
- **Usage**: Modern aircraft (A380, A350, 787)

## AFDX (ARINC 664) Details

### Architecture
- **End Systems (ES)**: Avionics equipment connected to network
- **Switches**: Central switches route traffic
- **Virtual Links (VL)**: Unidirectional logical connections
- **Redundancy**: Dual network (A and B) for fault tolerance

### Configuration
- Static configuration of VLs
- Bandwidth allocation per VL (BAG)
- Priority assignment
- Network schedule deterministic

### Verification
- Network timing analysis
- Bandwidth utilization
- Latency analysis
- Redundancy verification

## Interface Design Considerations

### Data Integrity
- Parity checking (ARINC 429)
- CRC (ARINC 664)
- Protocol validation
- Message authentication

### Timing
- Update rates appropriate to function
- Latency budgets
- Jitter tolerance
- Synchronization requirements

### Redundancy
- Dual channels (ARINC 429)
- Dual networks (ARINC 664)
- Voting logic
- Failure detection and annunciation

### EMI/EMC
- Shielded cables
- Proper grounding
- DO-160 Section 20/21 compliance
- Separation from sensitive systems

## Key Deliverables

1. **Interface Control Document (ICD)** - Define all interfaces between systems
2. **Network Architecture** - Topology, VL definitions, bandwidth allocation
3. **Message Dictionary** - All messages, parameters, encoding
4. **Interface Verification Plan** - Test procedures for interface compliance
5. **Interface Verification Results** - Test results, compliance statement

## Compliance Requirements

- Interfaces shall comply with applicable ARINC specifications
- Interface verification per ICD requirements
- Network timing analysis for AFDX
- EMI/EMC compliance per DO-160

## Integration with Other Standards

- **ARP4754A** - Interface requirements defined at system level
- **DO-178C** - Software implements protocol stacks
- **DO-254** - Hardware implements PHY and MAC layers
- **DO-160** - Environmental qualification including EMI/EMC

## Design Tools

- AFDX network configuration and analysis tools
- Protocol analyzers and monitors
- Test equipment for interface verification
- Simulation tools for early verification

## Common Issues

- Incorrect ARINC 429 label assignments
- AFDX bandwidth over-subscription
- Inadequate redundancy management
- EMI/EMC problems due to poor installation

## Tools and Templates

- ICD templates
- AFDX VL configuration templates
- Message dictionary templates
- Interface verification procedures

## References

- ARINC specifications (purchase required from Airlines Electronic Engineering Committee)
- 01-REGISTER/STANDARDS_REGISTER.csv - Applicable ARINC standards
- 06-INTERPRETATIONS/FAQ.md - Interface design questions

---

**Status**: Configuration-controlled per 00-PROGRAM/CONFIG_MGMT/
