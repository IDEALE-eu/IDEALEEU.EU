# DISPLAY DATA FLOWS

Data flows from sensors through processing to flight deck displays.

## Overview

This document describes the data flow paths from sensors through the avionics network, processing systems (FMS, AFCS, IMA), and finally to flight deck displays (PFD, ND, EICAS/ECAM).

## Primary Flight Display (PFD) Data Flows

### Attitude Data
```
IRS → AFDX → Display Management Computer (DMC) → Primary Flight Display
```
- **Source**: IRS (ATA-34-10)
- **Data**: Pitch, roll, heading
- **Rate**: 50 Hz
- **Latency**: < 30 ms end-to-end
- **Criticality**: DAL B

### Airspeed/Altitude/Vertical Speed
```
Air Data Computer → ARINC 429 → Gateway → AFDX → DMC → PFD
```
- **Source**: Air Data Computer (ATA-34)
- **Data**: IAS, TAS, altitude, vertical speed
- **Rate**: 50 Hz
- **Latency**: < 35 ms end-to-end
- **Criticality**: DAL B

### Autopilot Mode Annunciations
```
AFCS → AFDX → DMC → PFD
```
- **Source**: AFCS (ATA-22)
- **Data**: AP mode, FD mode, autothrust status
- **Rate**: 10 Hz
- **Latency**: < 100 ms
- **Criticality**: DAL C

## Navigation Display (ND) Data Flows

### Navigation Map
```
FMS → AFDX → DMC → Navigation Display
```
- **Source**: FMS (ATA-34-30)
- **Data**: Flight plan, waypoints, navaids
- **Rate**: 1 Hz
- **Latency**: < 500 ms
- **Criticality**: DAL C

### Aircraft Position
```
IRS/GNSS → AFDX → FMS → AFDX → DMC → ND
```
- **Source**: IRS/GNSS (ATA-34-10)
- **Data**: Latitude, longitude, track, ground speed
- **Rate**: 10 Hz
- **Latency**: < 200 ms
- **Criticality**: DAL C

### Weather Radar
```
Weather Radar → AFDX → DMC → ND
```
- **Source**: Weather Radar (ATA-34)
- **Data**: Radar image, weather returns
- **Rate**: 1-4 Hz
- **Latency**: < 1000 ms
- **Criticality**: DAL D

## EICAS/ECAM Data Flows

### Engine Parameters
```
Engine Control → ARINC 429 → Gateway → AFDX → DMC → EICAS/ECAM
```
- **Source**: Engine Control (ATA-76/77)
- **Data**: N1, N2, EGT, fuel flow
- **Rate**: 10 Hz
- **Latency**: < 500 ms
- **Criticality**: DAL C

### System Status and Alerts
```
All Avionics → AFDX → CMC → AFDX → DMC → EICAS/ECAM
```
- **Source**: All avionics systems
- **Data**: BITE status, warnings, cautions, advisories
- **Rate**: 1 Hz (status), immediate (alerts)
- **Latency**: < 1000 ms (status), < 500 ms (alerts)
- **Criticality**: DAL C

## Display Management Architecture

### Display Units (DU)
- **Type**: High-resolution LCD displays (typically 10-15 inch)
- **Resolution**: 1920x1200 or higher
- **Refresh Rate**: 60 Hz
- **Brightness**: 400-600 cd/m² (sunlight readable)

### Display Management Computer (DMC)
- **Processing**: Symbol generation, rendering, compositing
- **Redundancy**: Dual DMCs for each DU
- **Failover**: Automatic (< 1 second)
- **Hosting**: May be IMA-hosted (ATA-42)

### Display Reversionary Modes

#### Single DMC Failure
- Remaining DMC drives display
- All display formats available

#### Single DU Failure
- Adjacent DU shows combined PFD+ND
- Critical data always displayed

#### Multiple Failures
- Standby instruments provide minimum flight data
- Emergency procedures followed

## Data Flow Latency Budget

### Flight-Critical Displays (PFD)

| Segment | Budget | Measured | Margin |
|---------|--------|----------|--------|
| Sensor sampling | 5 ms | 3 ms | 40% |
| AFDX transmission | 10 ms | 6 ms | 40% |
| DMC processing | 10 ms | 8 ms | 20% |
| Display rendering | 17 ms | 16 ms | 6% |
| **Total** | **42 ms** | **33 ms** | **21%** |

### Navigation Displays (ND)

| Segment | Budget | Measured | Margin |
|---------|--------|----------|--------|
| FMS computation | 100 ms | 70 ms | 30% |
| AFDX transmission | 50 ms | 30 ms | 40% |
| DMC processing | 100 ms | 80 ms | 20% |
| Display rendering | 100 ms | 85 ms | 15% |
| **Total** | **350 ms** | **265 ms** | **24%** |

## Data Integrity

### Error Detection
- CRC checks on all AFDX messages
- Parity on ARINC 429 words
- Sequence numbers for data ordering
- Staleness detection (data age monitoring)

### Redundancy Management
- Dual sensor inputs (e.g., IRS-1, IRS-2)
- Voting algorithms (typically 2-out-of-3)
- Cross-channel monitoring
- Failure detection and annunciation

## Display Formats

### Standard Display Modes
- **PFD**: Primary flight data (attitude, airspeed, altitude)
- **ND**: Navigation data (map, plan, VOR, ILS modes)
- **EICAS/ECAM**: Engine and system synoptics

### Optional Display Modes
- **MFD**: Multi-function display (configurable)
- **Checklist**: Electronic checklists
- **Airport Map**: Airport moving map
- **TCAS**: Traffic display

## Testing and Verification

### Display Data Flow Tests
1. End-to-end latency measurement
2. Data integrity verification
3. Failover and reversionary mode testing
4. Display readability and sunlight testing

### Human Factors Testing
- Display clarity and readability
- Symbology consistency
- Alert prioritization
- Crew workload assessment

## Related Documents

- [ATA-31 Indicating & Recording](../01-SYSTEMS/ATA-31_INDICATING_RECORDING/INTEGRATION_VIEW.md)
- [Avionics Networks](./AVIONICS_NETWORKS.md)
- [ATA-42 IMA](../01-SYSTEMS/ATA-42_INTEGRATED_MODULAR_AVIONICS/INTEGRATION_VIEW.md)

## Revision History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2024-01-15 | Systems Integration | Initial display data flow architecture |
