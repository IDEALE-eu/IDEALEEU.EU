# Time Sources and Synchronization Architecture

## Overview

This document defines the aircraft time sources, synchronization hierarchy, and time distribution architecture.

## Primary Time Sources

### GNSS Time Reference
**Type**: Multi-constellation GNSS receiver with time output
**Constellations**: GPS, Galileo, GLONASS
**Accuracy**: ±50 ns to UTC when satellites available
**Output**: 1PPS (1 Pulse Per Second), IRIG-B, PTP

**Receivers**:
- GPS-1 (primary): Location Zone-C1
- GPS-2 (backup): Location Zone-C2

**Antenna Placement**:
- Top of fuselage for unobstructed sky view
- Dual antennas for redundancy
- Lightning protection per DO-160G

### IRIG Time Code
**Standard**: IRIG-B (amplitude modulated, BCD format)
**Source**: GNSS receivers generate IRIG-B output
**Distribution**: Dedicated IRIG distribution to legacy systems
**Users**: Flight Data Recorder, Maintenance Data Recorder

### 1PPS (1 Pulse Per Second)
**Source**: GNSS receivers
**Purpose**: Hardware time base for critical systems
**Distribution**: Differential pair, <10m cable length
**Users**: IMA Core Modules (Grandmaster clock inputs)

## Grandmaster Clocks

### Primary Grandmaster
**Location**: IMA Core Module 1
**Input**: 1PPS from GPS-1, IRIG-B
**Oscillator**: Oven-Controlled Crystal Oscillator (OCXO)
**Stability**: ±1×10⁻⁹ (Allan deviation at 1 second)
**Holdover**: ±10 μs over 24 hours without GNSS
**Output**: PTP (IEEE 1588) on AFDX network, domain 0

### Backup Grandmaster
**Location**: IMA Core Module 2
**Input**: 1PPS from GPS-2, IRIG-B
**Oscillator**: Oven-Controlled Crystal Oscillator (OCXO)
**Stability**: ±1×10⁻⁹ (Allan deviation at 1 second)
**Holdover**: ±10 μs over 24 hours without GNSS
**Output**: PTP (IEEE 1588) on AFDX network, domain 0

### Grandmaster Selection
**Normal**: Primary Grandmaster active, Backup in hot standby
**Failover**: Automatic switch if Primary loses GNSS or exceeds error threshold
**Criteria**: Best Master Clock Algorithm (BMCA) per IEEE 1588
**Switchover Time**: <1 second

## PTP Distribution Network

### Boundary Clocks
**Devices**: AFDX-SW-1, AFDX-SW-2
**Function**: Regenerate PTP sync messages, reduce error accumulation
**Sync Interval**: 125 ms (8 packets/second)
**Delay Request Interval**: 1 second

### Ordinary Clocks (End Devices)
**All LRUs** requiring time synchronization implement PTP ordinary clock
**Sync to**: Nearest boundary clock (AFDX switch)
**Max Hops**: 2 from grandmaster (Grandmaster → Boundary → Ordinary)
**Servo**: PI controller for phase lock

## Time Distribution Tree

See [SYNC_TREE.svg](./SYNC_TREE.svg) for visual representation.

```
GNSS Satellites (GPS, Galileo, GLONASS)
    ↓ 1PPS + IRIG-B
GPS-1 (Zone-C1)                    GPS-2 (Zone-C2)
    ↓                                   ↓
IMA Core 1 (Grandmaster)          IMA Core 2 (Backup Grandmaster)
    ↓                                   ↓
[BMCA - Best Master Clock Selection]
    ↓
┌───────────────┴───────────────┐
↓                               ↓
AFDX-SW-1 (Boundary Clock)      AFDX-SW-2 (Boundary Clock)
↓                               ↓
[Ordinary Clocks - All LRUs on respective networks]
FCC-1, FMS-1, ACE-1, ...        FCC-2, GPS-1, IRS-1, ...
```

## Synchronization Requirements

See [REQUIREMENTS.csv](./REQUIREMENTS.csv) for detailed requirements table.

### Critical Systems (DAL A)
- **Flight Control**: ±1 μs across FCC-1, FCC-2, ACE-1, ACE-2
- **Engine Control**: ±5 μs across FADEC-1, FADEC-2, ENG-ECU-1, ENG-ECU-2
- **Fire Detection**: ±10 μs across fire detection and suppression systems

### High-Priority Systems (DAL B)
- **Navigation**: ±10 μs across GPS, IRS, FMS
- **Landing Gear**: ±20 μs across landing gear control and sensors

### Medium-Priority Systems (DAL C/D)
- **Displays**: ±100 μs for display synchronization
- **Fuel Management**: ±1 ms for fuel indication

## Failure Modes and Recovery

### GNSS Signal Loss
**Detection**: Loss of 1PPS, degraded satellite count, poor signal quality
**Action**: 
1. Grandmaster enters holdover mode using OCXO
2. Crew alerted via EICAS caution message
3. Time accuracy degrades per holdover spec (±10 μs/24hr)
4. Flight operations continue normally

**Recovery**: Automatic when GNSS signal restored

### Grandmaster Failure
**Detection**: Loss of PTP sync messages, health monitoring failure
**Action**:
1. Automatic failover to backup grandmaster via BMCA
2. Crew alerted via EICAS caution message
3. Synchronization maintained with backup
4. Maintenance action required before next flight

**Recovery**: Replace failed grandmaster module

### Network Asymmetry
**Detection**: Excessive delay variation between sync and delay_req paths
**Action**:
1. Log asymmetry warning
2. If exceeds threshold, use alternate network path
3. Maintenance diagnostic check during next service

## Testing and Verification

### Ground Tests
- Verify ±1 μs sync accuracy with Calnex Sentinel or Meinberg test equipment
- Inject GNSS loss and verify holdover performance
- Measure network asymmetry on all paths
- Test failover from primary to backup grandmaster
- Document in [07-INTEGRATION_TEST/EVIDENCE/REPORTS/](../../07-INTEGRATION_TEST/EVIDENCE/REPORTS/)

### In-Flight Monitoring
- Continuous sync error monitoring vs. grandmaster
- Log PTP statistics at 1 Hz
- Alert crew if sync error exceeds 5 μs
- Record time sync health in flight data recorder

### Acceptance Criteria
- Sync accuracy ±1 μs in normal operation
- Holdover ±10 μs over 24 hours
- Failover <1 second
- No intermittent time steps >1 μs

## Compliance

- **IEEE 1588-2008**: Precision Time Protocol v2
- **ARINC 664 Part 7**: PTP profile for AFDX
- **DO-178C**: Software for time distribution (DAL A)
- **DO-254**: Hardware grandmaster clocks (DAL A)
- **DO-160G**: Environmental qualification of GNSS receivers

## References

- **[02-NETWORKS_DATA_BUS/QOS_TIMING/PTP_SYNC_BOUNDS.md](../../02-NETWORKS_DATA_BUS/QOS_TIMING/PTP_SYNC_BOUNDS.md)** - Detailed sync error budgets
- **[SYNC_TREE.svg](./SYNC_TREE.svg)** - Synchronization tree diagram
- **[REQUIREMENTS.csv](./REQUIREMENTS.csv)** - Timing requirements by system

## Revision History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2024-10-08 | Timing Architecture Team | Initial time sources document |
