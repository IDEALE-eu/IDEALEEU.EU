# AVIONICS NETWORKS

Avionics network architecture, protocols, quality of service, and latency management.

## Overview

This document describes the avionics network architecture for the INFO_COMM_AVIONICS domain, including ARINC 429, AFDX (ARINC 664), and other network protocols.

## Network Architecture

### AFDX Network (ARINC 664 Part 7)

#### Network Topology
- **Redundant Networks**: Network A and Network B for fault tolerance
- **End Systems**: Avionics LRUs connected to both networks
- **Switches**: Full-duplex switched Ethernet (100 Mbps per port)
- **Virtual Links (VL)**: Logical connections with guaranteed bandwidth

#### Virtual Link Allocation

| VL ID | Source | Destination(s) | BAG (ms) | S_max (bytes) | Jitter (μs) | Priority | Application |
|-------|--------|----------------|----------|---------------|-------------|----------|-------------|
| VL-001 | FMS | AFCS, Displays | 50 | 1024 | 500 | High | FMS guidance |
| VL-002 | IRS | FMS, AFCS | 20 | 512 | 200 | High | Position/attitude |
| VL-003 | AFCS | Flight Controls | 50 | 256 | 300 | Critical | Control commands |
| VL-004 | CMC | Displays | 1000 | 512 | 1000 | Low | Maintenance messages |
| VL-005 | Displays | IMA | 50 | 2048 | 500 | Medium | Display rendering |
| VL-006 | ACARS | Ground | 1000 | 1500 | 2000 | Low | Data link messages |

**Key Parameters:**
- **BAG (Bandwidth Allocation Gap)**: Minimum time between VL frame transmissions
- **S_max**: Maximum frame size
- **Jitter**: Maximum timing variation

#### QoS Strategy
- **Priority Queuing**: Critical > High > Medium > Low
- **Bandwidth Reservation**: Each VL has guaranteed bandwidth
- **Deterministic Latency**: Maximum end-to-end latency calculated per VL
- **Redundancy Management**: Automatic failover between Network A and B

### ARINC 429 Buses

#### Bus Allocation

| Bus ID | Speed | Source | Destinations | Purpose | Signal Count |
|--------|-------|--------|--------------|---------|--------------|
| A429-01 | 100 kbps | IRS-1 | FMS, AFCS, Displays | Primary IRS data | 8 labels |
| A429-02 | 100 kbps | IRS-2 | FMS, AFCS, Displays | Backup IRS data | 8 labels |
| A429-03 | 12.5 kbps | VOR/ILS | FMS, AFCS | Radio navigation | 12 labels |
| A429-04 | 12.5 kbps | DME | FMS | Distance measuring | 4 labels |
| A429-05 | 100 kbps | FMS | AFCS, Displays | FMS outputs | 20 labels |
| A429-06 | 12.5 kbps | CMC | Displays | Maintenance messages | 6 labels |

#### ARINC 429 Characteristics
- **Unidirectional**: One transmitter, multiple receivers
- **Self-Clocking**: Manchester encoding (bipolar RZ)
- **Data Rate**: 12.5 kbps (low speed) or 100 kbps (high speed)
- **Word Format**: 32-bit words with parity

### Gateway Modules

#### AFDX ↔ ARINC 429 Gateway
- **Purpose**: Bridge legacy ARINC 429 equipment to AFDX network
- **Latency**: Maximum 5 ms conversion delay
- **Throughput**: Up to 100 buses per gateway module
- **Redundancy**: Dual gateways for fault tolerance

#### Protocol Conversion
- ARINC 429 labels mapped to AFDX VLs
- Latency compensation for different data rates
- Error detection and reporting

### Other Networks

#### ARINC 717 (Flight Data Recorder)
- **Data Rate**: 64 or 256 words per second
- **Frame Structure**: Subframe, superframe organization
- **Purpose**: FDR/QAR data recording
- **Latency**: Not time-critical (buffered)

#### ARINC 708 (Weather Radar)
- **Data Rate**: High-bandwidth (1-10 Mbps)
- **Purpose**: Weather radar image transmission
- **Network**: Typically uses AFDX for modern systems

#### ARINC 1553 (Legacy Systems)
- **Data Rate**: 1 Mbps
- **Purpose**: Legacy military/transport avionics
- **Status**: Not used in primary avionics (if present, via gateway)

## Latency Budget

### Critical Paths

#### Sensor to Display (Flight-Critical)
| Segment | Source | Destination | Protocol | Latency Budget | Measured |
|---------|--------|-------------|----------|----------------|----------|
| 1 | IRS | AFDX Switch | AFDX | 1 ms | 0.8 ms |
| 2 | AFDX Switch | Display | AFDX | 2 ms | 1.5 ms |
| 3 | Display Processing | - | Internal | 30 ms | 25 ms |
| **Total** | | | | **33 ms** | **27.3 ms** |

#### FMS to Autopilot (Flight-Critical)
| Segment | Source | Destination | Protocol | Latency Budget | Measured |
|---------|--------|-------------|----------|----------------|----------|
| 1 | FMS | AFDX Switch | AFDX | 2 ms | 1.2 ms |
| 2 | AFDX Switch | AFCS | AFDX | 2 ms | 1.5 ms |
| 3 | AFCS Processing | - | IMA Partition | 10 ms | 8 ms |
| 4 | AFCS | Gateway | AFDX | 2 ms | 1.3 ms |
| 5 | Gateway | Flight Controls | A429 | 5 ms | 3.5 ms |
| **Total** | | | | **21 ms** | **15.5 ms** |

### Latency Margins
- **Critical Paths**: Minimum 20% margin
- **High-Priority Paths**: Minimum 30% margin
- **Low-Priority Paths**: Best effort (no guarantee)

## Network Performance

### Bandwidth Utilization
- **Network A**: 45% average, 68% peak
- **Network B**: 43% average, 65% peak
- **Target**: < 70% average, < 85% peak

### Error Rates
- **AFDX**: < 1E-9 bit error rate
- **ARINC 429**: < 1E-7 bit error rate (self-correcting with parity)

### Availability
- **Dual Redundancy**: 99.999% availability (5 nines)
- **Failover Time**: < 100 ms for AFDX network switchover

## Network Security

### Isolation
- **Flight-Critical Network**: No external connectivity
- **Cabin Network**: Isolated via firewall (ATA-46-30)
- **Maintenance Network**: Controlled access via gateway

### Monitoring
- **Intrusion Detection**: Real-time monitoring of network traffic
- **Anomaly Detection**: Unusual patterns flagged to CMC
- **Logging**: Security events logged for audit

## Timing and Synchronization

### Time Synchronization Strategy
- **Primary**: Precision Time Protocol (PTP) via AFDX
- **Backup**: IRIG-B time code
- **Accuracy**: ±100 μs across all avionics

See [TIME_SYNC.md](./TIME_SYNC.md) for detailed synchronization architecture.

## Testing and Verification

### Network Performance Testing
- Latency measurement for all critical paths
- Bandwidth utilization under maximum load
- Failover and redundancy testing
- Error injection and recovery

### Compliance Testing
- ARINC 664 conformance testing
- ARINC 429 signal validation
- EMI/EMC testing per DO-160

## Known Issues & Risks

### Technical Risks
- Network congestion under high load
- Latency spikes during failover
- Gateway conversion errors
- Timing synchronization drift

### Mitigation Strategies
- Conservative bandwidth allocation (< 70% average)
- Redundant networks with fast failover
- Gateway self-test and monitoring
- Regular time synchronization checks

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2024-01-15 | Systems Integration | Initial avionics network architecture |

## References

- **ARINC 664 Part 7**: Aircraft Data Network, Part 7 - Avionics Full-Duplex Switched Ethernet Network
- **ARINC 429**: Mark 33 Digital Information Transfer System (DITS)
- **ARINC 717**: Flight Data Recorder Systems
- **DO-178C**: Software Considerations in Airborne Systems (for network software)
- [Time Synchronization](./TIME_SYNC.md)
- [Display Data Flows](./DISPLAY_DATA_FLOWS.md)
- [ATA-42 IMA](../01-SYSTEMS/ATA-42_INTEGRATED_MODULAR_AVIONICS/INTEGRATION_VIEW.md)
