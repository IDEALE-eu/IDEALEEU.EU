# Inter-Partition Communications

## Overview

This document defines the inter-partition communication channels, protocols, Quality of Service (QoS), and Interface Control Document (ICD) references for software integration.

## Communication Architecture

Inter-partition communication uses ARINC 653 APEX API (sampling and queuing ports) for logical communication, mapped to physical AFDX network for inter-module communication.

```
Partition P001 (IMA-CORE-1) ←→ Partition P002 (IMA-CORE-2)
      ↓ APEX Sampling Port              ↓ APEX Sampling Port
      ↓ (Intra-module: Shared Memory)   ↓ (Inter-module: AFDX)
      ↓                                  ↓
   AFDX-SW-1 ←→ AFDX-SW-2 (Redundant Network)
```

## Communication Channels

### Critical Control Channels (DAL A)

#### Channel: Flight Control Sync
- **From**: P001 (FCC-1) → P002 (FCC-2)
- **Type**: Sampling port (periodic)
- **Rate**: 100 Hz (10 ms period)
- **Message Size**: 32 bytes
- **QoS**: 
  - Latency budget: 2 ms
  - Jitter: <100 μs
  - Redundancy: Dual AFDX paths
- **ICD**: [ICD-0003](../../../../00-PROGRAM/CONFIG_MGMT/09-INTERFACES/ICD-0003.md)

#### Channel: Air Data to Flight Control
- **From**: P008 (ADC-1) → P001 (FCC-1)
- **Type**: Sampling port (periodic)
- **Rate**: 10 Hz (100 ms period)
- **Message Size**: 16 bytes
- **QoS**:
  - Latency budget: 5 ms
  - Jitter: <200 μs
  - Redundancy: Dual AFDX paths
- **ICD**: [ICD-0023](../../../../00-PROGRAM/CONFIG_MGMT/09-INTERFACES/ICD-0023.md)

#### Channel: Engine Monitoring
- **From**: P006 (FADEC-1 Mon) → P007 (FADEC-2 Mon)
- **Type**: Sampling port (periodic)
- **Rate**: 20 Hz (50 ms period)
- **Message Size**: 256 bytes
- **QoS**:
  - Latency budget: 10 ms
  - Jitter: <500 μs
  - Redundancy: Dual AFDX paths
- **ICD**: [ICD-0006](../../../../00-PROGRAM/CONFIG_MGMT/09-INTERFACES/ICD-0006.md)

### Essential Channels (DAL B)

#### Channel: Navigation Data Distribution
- **From**: P003 (FMS-1) → P004 (Display-1), P005 (Display-2)
- **Type**: Sampling port (periodic)
- **Rate**: 1 Hz (1000 ms period)
- **Message Size**: 128 bytes
- **QoS**:
  - Latency budget: 100 ms
  - Jitter: <10 ms
  - Redundancy: Single path acceptable
- **ICD**: [ICD-0005](../../../../00-PROGRAM/CONFIG_MGMT/09-INTERFACES/ICD-0005.md)

#### Channel: Inertial Reference
- **From**: P010 (IRS-1) → P001 (FCC-1), P003 (FMS-1)
- **Type**: Sampling port (periodic)
- **Rate**: 50 Hz (20 ms period)
- **Message Size**: 64 bytes
- **QoS**:
  - Latency budget: 10 ms
  - Jitter: <500 μs
  - Redundancy: Dual AFDX paths
- **ICD**: [ICD-0022](../../../../00-PROGRAM/CONFIG_MGMT/09-INTERFACES/ICD-0022.md)

### Event-Driven Channels (DAL A/B)

#### Channel: Fire Alert
- **From**: P012 (Fire Detection) → P017 (System Health Monitor)
- **Type**: Queuing port (event-driven)
- **Max Queue Depth**: 10 messages
- **Message Size**: 64 bytes
- **QoS**:
  - Latency budget: 50 ms (worst-case: full queue)
  - Priority: Critical
  - Redundancy: Dual AFDX paths
- **ICD**: [ICD-0011](../../../../00-PROGRAM/CONFIG_MGMT/09-INTERFACES/ICD-0011.md)

#### Channel: Health Events
- **From**: P001-P016 (All Partitions) → P017 (System Health Monitor)
- **Type**: Queuing port (event-driven)
- **Max Queue Depth**: 50 messages
- **Message Size**: 256 bytes
- **QoS**:
  - Latency budget: 1 second (worst-case)
  - Priority: Medium
  - Redundancy: Single path acceptable
- **Note**: Aggregates health events from all partitions

### Non-Critical Channels (DAL C/D)

#### Channel: Configuration Commands
- **From**: P018 (Config Manager) → P001-P016 (All Partitions)
- **Type**: Queuing port (event-driven)
- **Max Queue Depth**: 5 messages per partition
- **Message Size**: 128 bytes
- **QoS**:
  - Latency budget: 5 seconds
  - Priority: Low
  - Redundancy: Not required
- **Note**: Configuration updates (ground only)

## QoS Parameters

### Latency Budgets
Per functional chain, see [01-ARCHITECTURE_END2END/FUNCTIONAL_CHAINS/LATENCY_BUDGETS.csv](../../01-ARCHITECTURE_END2END/FUNCTIONAL_CHAINS/LATENCY_BUDGETS.csv)

### Jitter Tolerance
- **DAL A**: <100 μs (critical control loops)
- **DAL B**: <1 ms (navigation, essential functions)
- **DAL C/D**: <10 ms (displays, non-critical)

### Message Loss
- **DAL A**: Zero loss tolerated (dual redundancy required)
- **DAL B**: 1 in 10⁶ messages (redundancy recommended)
- **DAL C/D**: 1 in 10⁴ messages (best effort)

### Priority Levels
1. **Critical (P1)**: Flight control, engine control, fire detection
2. **High (P2)**: Navigation, pressurization, braking
3. **Medium (P3)**: Displays, hydraulics, fuel management
4. **Low (P4)**: Configuration, diagnostics, non-critical

## Protocol Stack

### Layer 1: Physical (AFDX Network)
- 100 Mbps full-duplex Ethernet
- CAT6A shielded twisted-pair cables
- Redundant AFDX switches (AFDX-SW-1, AFDX-SW-2)

### Layer 2: Data Link (AFDX)
- ARINC 664 Part 7 (AFDX)
- Virtual Links (VLs) with Bandwidth Allocation Gap (BAG)
- See [02-NETWORKS_DATA_BUS/LOGICAL/AFDX_VL_MAP.csv](../../02-NETWORKS_DATA_BUS/LOGICAL/AFDX_VL_MAP.csv)

### Layer 3: Application (ARINC 653 APEX)
- Sampling ports for periodic data
- Queuing ports for event-driven messages
- See [05-IMA_INTEGRATION/APEX_API_USAGE.md](../../05-IMA_INTEGRATION/APEX_API_USAGE.md)

## Data Formats

### Message Encoding
- **Binary**: Native C struct packing (no padding, aligned to 4-byte boundaries)
- **Endianness**: Big-endian (network byte order) per ARINC standards
- **CRC**: 16-bit CRC-CCITT for critical messages (DAL A)

### Example Message Structure (Flight Control Command)
```c
typedef struct {
    uint32_t timestamp_us;      // PTP synchronized time (microseconds)
    uint16_t sequence_number;   // Message sequence counter
    int16_t  pitch_cmd;         // Pitch command (0.01 deg units)
    int16_t  roll_cmd;          // Roll command (0.01 deg units)
    int16_t  yaw_cmd;           // Yaw command (0.01 deg units)
    uint8_t  control_mode;      // 0=Manual, 1=Autopilot, 2=Emergency
    uint8_t  status_flags;      // Bit-packed status flags
    uint16_t crc16;             // CRC-CCITT checksum
} __attribute__((packed)) FlightControlCommand;
```

## Interface Control

### ICD References
All inter-partition interfaces controlled by ICDs:
- ICD repository: [00-PROGRAM/CONFIG_MGMT/09-INTERFACES/](../../../../00-PROGRAM/CONFIG_MGMT/09-INTERFACES/)
- ICD index: [10-ICD_LINKS/INDEX.md](../../10-ICD_LINKS/INDEX.md)
- ICD mapping: [01-ARCHITECTURE_END2END/INTERFACE_MATRIX/MAP_TO_ICDS.md](../../01-ARCHITECTURE_END2END/INTERFACE_MATRIX/MAP_TO_ICDS.md)

### Change Control
All ICD changes require:
1. ECR submission with impact analysis
2. CCB approval
3. Software update to both communicating partitions
4. Integration testing to verify compatibility

## Error Handling

### Communication Failures
- **Timeout**: Partition receives no data within expected period
  - DAL A: Switch to backup partition immediately
  - DAL B: Retry 3 times, then alert crew
  - DAL C/D: Log error, continue with stale data

- **Invalid Data**: CRC mismatch or out-of-range values
  - DAL A: Reject message, use previous valid data, alert health monitor
  - DAL B: Reject message, retry request
  - DAL C/D: Log error, may continue with invalid data (non-safety)

- **Sequence Error**: Missing or duplicate sequence numbers
  - DAL A: Alert health monitor, may trigger partition failover
  - DAL B: Log warning, continue
  - DAL C/D: Ignore

### Network Failures
- **Single AFDX Path Failure**: Automatic switch to redundant path
- **Dual AFDX Path Failure**: Partition failover or safe mode entry
- **Switch Failure**: Traffic re-routes via redundant switch

## Testing and Verification

### Communication Testing
- Verify all channels transmit/receive at expected rates
- Measure end-to-end latency per channel
- Inject faults (message loss, corruption, delay) and verify error handling
- Test failover scenarios (partition failure, network failure)
- Document in [07-INTEGRATION_TEST/EVIDENCE/](../../07-INTEGRATION_TEST/EVIDENCE/)

### Acceptance Criteria
- All channels meet QoS requirements (latency, jitter, loss)
- Error handling per DAL requirements
- Traceability to ICDs (100% coverage)
- No communication deadlocks or livelocks

## Compliance

- **ARINC 653**: Inter-partition communication per APEX API
- **ARINC 664**: AFDX network protocol
- **DO-178C**: Software verification of communication stack (DAL A)
- **DO-254**: Hardware network switches (DAL A)

## References

- **[05-IMA_INTEGRATION/APEX_API_USAGE.md](../../05-IMA_INTEGRATION/APEX_API_USAGE.md)** - APEX API details
- **[02-NETWORKS_DATA_BUS/](../../02-NETWORKS_DATA_BUS/)** - Network architecture
- **[01-ARCHITECTURE_END2END/FUNCTIONAL_CHAINS/](../../01-ARCHITECTURE_END2END/FUNCTIONAL_CHAINS/)** - Functional chains

## Revision History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2024-10-08 | SW Integration Team | Initial inter-partition comms document |
