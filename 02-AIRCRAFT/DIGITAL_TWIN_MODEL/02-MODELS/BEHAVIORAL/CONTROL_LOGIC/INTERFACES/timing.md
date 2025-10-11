# TIMING ANALYSIS AND REQUIREMENTS
# ATA-27 Flight Controls - Control Loop Timing

**System**: Flight Control Computer (FCC)  
**Related**: [signals.yaml](signals.yaml)  
**Version**: 1.0  
**Last Updated**: 2025-01-15

## Overview

This document defines the timing requirements and analysis for the flight control system. Timing is critical for stability, performance, and safety of the control laws.

## Control Loop Timing

### Primary Control Loop

```
Frequency: 50 Hz
Period: 20 ms
```

**Execution Breakdown**:

| Phase | Duration (ms) | Cumulative (ms) | Notes |
|-------|--------------|-----------------|-------|
| Sensor data acquisition | 2.0 | 2.0 | Read ARINC 429/664 inputs |
| Signal validation & filtering | 1.5 | 3.5 | Cross-check, range check |
| Sensor fusion | 2.0 | 5.5 | Kalman filter, state estimation |
| Control law computation | 6.0 | 11.5 | PID, gain scheduling, envelope protection |
| Command limiting & shaping | 1.5 | 13.0 | Rate limits, position limits |
| Redundancy management | 2.0 | 15.0 | Voting, fault detection |
| Output generation | 2.0 | 17.0 | Format ARINC commands |
| BIT and monitoring | 1.0 | 18.0 | Health checks |
| **Total** | **18.0** | **18.0** | **2 ms margin** |

**Margin**: 2.0 ms (10% of cycle time)

### Fast Feedback Loops

Some signals require faster sampling for stability:

| Signal | Rate (Hz) | Purpose |
|--------|-----------|---------|
| Surface position feedback | 100 | Actuator servo loop stability |
| Rate gyros | 100 | Fast attitude control |
| Angle of attack | 50 | Envelope protection |
| Load factor | 50 | Structural load monitoring |

## End-to-End Latency Budget

**Requirement**: Total latency from pilot input to surface movement < 60 ms

| Segment | Duration (ms) | Notes |
|---------|--------------|-------|
| Control column to FCC input | 5 | Sensor + ARINC 429 transmission |
| FCC input buffer | 2 | Wait for next control cycle |
| FCC computation | 18 | See control loop breakdown |
| FCC output buffer | 2 | ARINC 429 transmission |
| Actuator response time | 25 | Hydraulic servo bandwidth |
| **Total** | **52** | **8 ms margin to requirement** |

## Jitter and Synchronization

### Clock Synchronization

- **Master Clock**: GPS-disciplined oscillator on IMA
- **FCC Clock Sync**: ±100 μs to master
- **Cross-channel Sync**: ±50 μs between redundant FCCs

### Jitter Tolerance

- **Control Loop Jitter**: <500 μs (2.5% of period)
- **Input Signal Jitter**: <200 μs for critical signals
- **Impact**: Minimal on control stability per analysis

## Watchdog and Timeout

### FCC Watchdog

```
Timeout: 100 ms (5× control loop period)
Action: Reset FCC, engage backup channel
```

### Signal Freshness

| Signal Type | Timeout (ms) | Action on Timeout |
|-------------|--------------|-------------------|
| Pilot commands | 50 | Use last valid + warning |
| Air data | 100 | Degrade control law mode |
| Autopilot commands | 100 | Disengage autopilot |
| Position feedback | 30 | Flag actuator fault |

## Timing Verification

### Analysis Methods

1. **Worst-Case Execution Time (WCET)**: Static analysis tool + measurements
2. **Schedulability Analysis**: Rate Monotonic Analysis (RMA)
3. **Jitter Analysis**: Monte Carlo simulation
4. **End-to-End Testing**: Hardware-in-the-Loop (HIL) measurements

### Test Results

| Test Case | Requirement | Measured | Margin | Status |
|-----------|-------------|----------|--------|--------|
| Control loop period | 20 ms ±0.5 ms | 20.0 ms ±0.15 ms | Good | PASS |
| End-to-end latency | <60 ms | 52 ms | 8 ms | PASS |
| Watchdog response | <100 ms | 85 ms | 15 ms | PASS |
| Clock sync accuracy | ±100 μs | ±42 μs | Good | PASS |

**Evidence**: See [../EVIDENCE/timing_verification_report.pdf](../EVIDENCE/timing_verification_report.pdf)

## Timing Diagrams

### Normal Operation Sequence

```
Time (ms)    0    5    10   15   20   25   30   35   40   45   50   55   60
             |----|----|----|----|----|----|----|----|----|----|----|----|
Pilot Input  ▼                              
             └─┐
FCC Read        └─┐
                  └─────┐
FCC Compute           └──────┐
                             └─┐
FCC Output                      └─┐
                                  └──────┐
Actuator Move                            └────────────┐
                                                      └─► Surface at position
```

### Degraded Mode (Single Channel Failure)

When one FCC channel fails:

```
Failure Detection: 2 control cycles (40 ms)
Channel Isolation: 1 control cycle (20 ms)
Reconfiguration: 1 control cycle (20 ms)
Total Switchover: <80 ms (within certification requirement of 100 ms)
```

## Safety Considerations

### Timing Hazards

| Hazard | Mitigation | Verification |
|--------|------------|--------------|
| Delayed command | Watchdog timeout | HIL test |
| Clock drift | GPS sync + independent oscillators | Clock accuracy test |
| Computation overrun | WCET margin + overflow detection | Static analysis |
| Missed deadline | Priority scheduling + load monitoring | Schedulability analysis |

### Certification Evidence

- **DO-178C**: Timing requirements traced to software requirements
- **DO-254**: Hardware timing margins verified in FPGA/ASIC design
- **ARP-4754A**: System-level timing analysis

## Related Documents

- [signals.yaml](signals.yaml) - Signal definitions and rates
- [../SPEC/control_modes.md](../SPEC/control_modes.md) - Control law modes
- [../TESTS/VECTORS/timing_test_case.yaml](../TESTS/VECTORS/timing_test_case.yaml) - Timing test vectors
- [../../../../../../00-PROGRAM/CONFIG_MGMT/09-INTERFACES/](../../../../../../00-PROGRAM/CONFIG_MGMT/09-INTERFACES/) - ICD repository

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2025-01-15 | Flight Controls Engineering | Initial timing specification |

---

**Status**: Configuration-controlled per `00-PROGRAM/CONFIG_MGMT/`
