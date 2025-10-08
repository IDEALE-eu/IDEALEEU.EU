# PTP Synchronization Bounds

## Overview

This document defines Precision Time Protocol (IEEE 1588) synchronization error budgets and bounds for the aircraft time distribution network.

## PTP Architecture

### Grandmaster Clock
- **Location**: IMA Core Module 1 (primary), IMA Core Module 2 (backup)
- **Reference**: GNSS disciplined oscillator (GPS/Galileo/GLONASS)
- **Accuracy**: ±50 ns to UTC when GNSS available
- **Holdover**: ±10 μs over 24 hours without GNSS
- **Stratum**: Stratum 1 (direct GNSS reference)

### Boundary Clocks
- **AFDX-SW-1**: Boundary clock, PTP domain 0
- **AFDX-SW-2**: Boundary clock, PTP domain 0
- **Sync Interval**: 125 ms (8 packets/second)
- **Delay Request Interval**: 1 second

### Ordinary Clocks (Slave Devices)
- All LRUs with time-critical functions
- Sync to nearest boundary clock
- Maximum 2 hops from grandmaster

## Synchronization Error Budget

### End-to-End Error Budget

| Error Source | Budget (μs) | Notes |
|-------------|-------------|-------|
| Grandmaster stability | ±0.05 | GNSS-disciplined OCXO |
| Network asymmetry | ±0.3 | AFDX deterministic switching |
| Boundary clock accuracy | ±0.2 | Per boundary clock |
| Slave clock servo | ±0.3 | PI controller settling |
| Oscillator drift | ±0.15 | Between sync packets |
| **Total (RSS)** | **±0.52** | Root-sum-square |
| **Allocated budget** | **±1.0** | Design requirement |
| **Margin** | **48%** | Design margin |

### Critical Systems Requirements

#### Flight Control System (FC-001)
- **Requirement**: ±1 μs synchronization across FCC-1, FCC-2, ACE-1, ACE-2
- **Allocated**: ±0.8 μs
- **Measured**: ±0.6 μs typical
- **Status**: ✓ PASS with 25% margin

#### Engine Control (FC-003)
- **Requirement**: ±5 μs synchronization between FADEC-1, FADEC-2, ENG-ECU-1, ENG-ECU-2
- **Allocated**: ±3 μs
- **Measured**: ±2.1 μs typical
- **Status**: ✓ PASS with 30% margin

#### Navigation System (FC-002)
- **Requirement**: ±10 μs synchronization across GPS-1, IRS-1, FMS-1
- **Allocated**: ±7 μs
- **Measured**: ±4.5 μs typical
- **Status**: ✓ PASS with 36% margin

## Sync Message Rates

### Critical Functions (DAL A)
- **Rate**: 125 ms (8 Hz)
- **Priority**: Highest (DSCP EF)
- **Redundancy**: Dual path
- **Applicable to**: Flight control, engine control, fire detection, brakes

### High-Priority Functions (DAL B)
- **Rate**: 250 ms (4 Hz)
- **Priority**: High (DSCP AF41)
- **Redundancy**: Dual path
- **Applicable to**: Navigation, landing gear, pressurization

### Medium-Priority Functions (DAL C/D)
- **Rate**: 1 second (1 Hz)
- **Priority**: Medium (DSCP AF21)
- **Redundancy**: Single path acceptable
- **Applicable to**: Fuel indication, displays, communications

## Wander and Drift Limits

### Short-Term Stability (Allan Deviation)
- **1 second**: < 1×10⁻⁹ (1 ns)
- **10 seconds**: < 5×10⁻⁹ (5 ns)
- **100 seconds**: < 1×10⁻⁸ (10 ns)

### Long-Term Drift
- **Aging rate**: < ±1 ppm/year (OCXO)
- **Temperature coefficient**: < ±0.1 ppb/°C (OCXO)

### Holdover Performance
- **Immediate loss of GNSS**: < ±1 μs for 10 minutes
- **Extended holdover (no GNSS)**: < ±10 μs for 24 hours
- **Holdover mode entry**: Automatic, crew alert after 5 minutes

## GNSS Failure Modes

### Primary GNSS Loss
- **Action**: Automatic switch to backup GNSS receiver
- **Switchover time**: < 1 second
- **Crew notification**: EICAS caution message

### Total GNSS Loss
- **Action**: Enter holdover mode using OCXO
- **Accuracy degradation**: Gradual per holdover spec
- **Crew notification**: EICAS caution message
- **Flight impact**: Operations continue, time accuracy degrades

### GNSS Jamming/Spoofing
- **Detection**: Multi-constellation cross-check, signal quality monitoring
- **Action**: Reject suspect GNSS data, use last known good time + OCXO
- **Notification**: Crew alert, log security event per DO-326A

## Verification and Monitoring

### Ground Test Requirements
- Verify ±1 μs sync accuracy with test equipment (Calnex Sentinel, Meinberg)
- Inject GNSS loss and verify holdover performance
- Measure asymmetry on all network paths
- Document all measurements in [07-INTEGRATION_TEST/EVIDENCE/](../../07-INTEGRATION_TEST/EVIDENCE/)

### In-Flight Monitoring
- Continuous monitoring of sync error vs. grandmaster
- Log PTP statistics (offset, delay, jitter) at 1 Hz
- Alert crew if sync error exceeds 5 μs
- Record time sync health in flight data recorder

### Maintenance Actions
- Monthly check of PTP sync status
- Annual calibration of grandmaster vs. UTC reference
- Replace OCXO if aging exceeds ±2 ppm

## Compliance

- **IEEE 1588-2008**: PTP version 2
- **ARINC 664 Part 7**: PTP profile for AFDX
- **DO-178C**: Software time service functions (DAL A)
- **DO-254**: Hardware clock implementation (DAL A)

## References

- **IEEE 1588-2008**: Precision Time Protocol standard
- **[03-TIME_SYNCHRONISATION/TIME_SOURCES.md](../../03-TIME_SYNCHRONISATION/TIME_SOURCES.md)** - Time source architecture
- **[03-TIME_SYNCHRONISATION/SYNC_TREE.svg](../../03-TIME_SYNCHRONISATION/SYNC_TREE.svg)** - Synchronization tree diagram
- **[03-TIME_SYNCHRONISATION/REQUIREMENTS.csv](../../03-TIME_SYNCHRONISATION/REQUIREMENTS.csv)** - Detailed timing requirements

## Revision History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2024-10-08 | Timing Architecture Team | Initial PTP sync bounds |
