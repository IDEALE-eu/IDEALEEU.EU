# TIME SYNCHRONIZATION

Time synchronization strategy for avionics systems using PTP, IRIG, and 1PPS.

## Overview

Accurate time synchronization across all avionics systems is critical for:
- Coordinated data sampling
- Event correlation in fault isolation
- Data recorder time stamping
- Navigation system accuracy
- Network scheduling (AFDX VL timing)

## Synchronization Architecture

### Primary: Precision Time Protocol (PTP)

**IEEE 1588 PTP over AFDX Network**
- **Grandmaster Clock**: IRS-1 (primary), IRS-2 (backup)
- **Accuracy**: ±100 μs across all avionics
- **Sync Rate**: 1 sync message per second
- **Protocol**: IEEE 1588-2008 (PTPv2)

**PTP Hierarchy:**
```
Grandmaster (IRS-1)
  └─ Boundary Clocks (IMA modules, AFDX switches)
      └─ Ordinary Clocks (End systems: FMS, AFCS, Displays, etc.)
```

### Backup: IRIG-B Time Code

**IRIG-B (Inter-Range Instrumentation Group Time Code)**
- **Format**: IRIG-B000 (1 kHz modulated)
- **Source**: GPS receiver (ATA-34)
- **Distribution**: Dedicated IRIG-B lines to critical systems
- **Accuracy**: ±1 ms

### External: 1PPS (One Pulse Per Second)

**GPS 1PPS Signal**
- **Source**: GNSS receiver (ATA-34)
- **Purpose**: Absolute time reference for IRS and FDR
- **Accuracy**: ±1 μs (GPS accuracy)

## Time Synchronization Strategy

### Normal Operation
1. IRS-1 acts as PTP Grandmaster (derives time from GPS)
2. All avionics synchronize to IRS-1 via PTP over AFDX
3. IRIG-B provides backup time reference

### Failover Scenarios

#### IRS-1 Failure
1. IRS-2 becomes PTP Grandmaster
2. Automatic failover within 1 second
3. All systems re-synchronize to IRS-2

#### PTP Network Failure
1. Systems fall back to IRIG-B time code
2. Accuracy degrades to ±1 ms
3. CMC alert generated

#### Complete Time Reference Loss
1. Systems use internal clocks (free-running)
2. Time stamping continues but accuracy degrades
3. Flight crew alerted via EICAS/ECAM

## Time Synchronization Performance

### Accuracy Requirements

| System | Accuracy Requirement | Achieved |
|--------|---------------------|----------|
| FMS | ±1 ms | ±50 μs |
| AFCS | ±1 ms | ±80 μs |
| Displays | ±10 ms | ±100 μs |
| FDR | ±100 ms | ±1 ms |
| CMC | ±1 s | ±100 ms |

### Synchronization Latency
- **Initial Sync**: < 5 seconds after power-up
- **Re-sync (after fault)**: < 1 second
- **Drift Correction**: Continuous (every sync message)

## Implementation

### PTP Configuration
```
Domain Number: 0
Sync Interval: 1 second (log interval 0)
Delay Request Interval: 1 second
Announce Interval: 2 seconds
Priority 1: 128 (IRS-1), 129 (IRS-2)
```

### IRIG-B Distribution
- Buffered distribution amplifiers
- Impedance matching (50 Ω)
- Redundant paths for critical systems

## Testing and Verification

### Synchronization Tests
1. **Accuracy Test**: Verify ±100 μs accuracy across all systems
2. **Failover Test**: Verify automatic failover from IRS-1 to IRS-2
3. **IRIG-B Backup Test**: Verify fallback to IRIG-B
4. **Drift Test**: Verify clock drift < 1 ppm

### Compliance
- IEEE 1588-2008 compliance
- DO-178C for PTP software
- ARINC 664 for PTP over AFDX

## Related Documents

- [Avionics Networks](./AVIONICS_NETWORKS.md)
- [ATA-34 Navigation](../01-SYSTEMS/ATA-34_NAVIGATION/INTEGRATION_VIEW.md)
- [ATA-42 IMA](../01-SYSTEMS/ATA-42_INTEGRATED_MODULAR_AVIONICS/INTEGRATION_VIEW.md)

## Revision History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2024-01-15 | Systems Integration | Initial time sync architecture |
