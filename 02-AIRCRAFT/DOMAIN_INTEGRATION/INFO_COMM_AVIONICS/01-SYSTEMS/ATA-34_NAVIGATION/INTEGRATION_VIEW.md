# ATA-34 NAVIGATION - Integration View

## Overview

Navigation systems integration covering satellite navigation (GNSS/IRS), radio navigation (VOR/ILS/DME), and Flight Management System (FMS).

## System Architecture

### Satellite Navigation
- **GNSS**: Global Navigation Satellite System (GPS, Galileo, GLONASS, BeiDou)
- **IRS**: Inertial Reference System (position, attitude, velocity)
- **AHRS**: Attitude and Heading Reference System (if separate)

### Radio Navigation
- **VOR**: VHF Omnidirectional Range
- **ILS**: Instrument Landing System
- **DME**: Distance Measuring Equipment
- **ADF**: Automatic Direction Finder (if applicable)

### Flight Management
- **FMS**: Flight Management System
  - Flight planning and optimization
  - Lateral/vertical navigation
  - Performance predictions
  - Database management

## Key Interfaces

### Internal Interfaces
- **34 ↔ 22**: FMS guidance to autopilot/flight director
- **34 ↔ 23**: Position data for ACARS/CPDLC
- **34 ↔ 24**: Electrical power supply
- **34 ↔ 31**: Navigation data to displays
- **34 ↔ 42**: IMA hosting for FMS applications
- **34 ↔ 45**: CMC monitoring and navigation database loading
- **34 ↔ 46**: Navigation database updates (ARINC 424)
- **34 ↔ 92**: EWIS (all wiring in ATA-92)

### Data Flows
- GNSS/IRS position to FMS
- VOR/DME tuning and deviations
- ILS localizer/glideslope signals
- FMS guidance to autopilot
- Navigation data to displays

## Network Integration

### ARINC 429 Buses
- IRS outputs (position, attitude, velocity)
- VOR/ILS/DME receivers
- FMS outputs to autopilot
- Radio tuning commands

### AFDX Network
- FMS processing (if IMA-hosted)
- Navigation database loading
- Multi-sensor position fusion

## Subsystems

### ATA-34-10: SENSORS (GNSS/IRS)
- GNSS receivers with SBAS/GBAS augmentation
- Inertial reference units
- Air data integration for IRS

### ATA-34-20: RADIONAV (VOR/ILS/DME)
- VOR/ILS receivers
- DME interrogators
- Antenna systems

### ATA-34-30: FMS
- FMS computer (may be IMA-hosted per ATA-42)
- Control Display Unit (CDU)
- Navigation database
- Performance database

## IMA Hosting (ATA-42 Integration)

If FMS is IMA-hosted:
- **Partition**: See ATA-42-90_PARTITION_MAP_APPS
- **Software**: Managed in CONFIGURATION_BASE/ATA-34/SW_BASELINE/
- **Determinism**: ARINC 653 scheduling ensures deterministic execution
- **Redundancy**: Dual FMS partitions on separate IMA modules

## PLM Integration

All hardware and software artifacts link to CONFIGURATION_BASE for authoritative configurations:
- **Hardware**: CONFIGURATION_BASE/ATA-34_NAVIGATION/HW_CONFIG/
- **Software**: CONFIGURATION_BASE/ATA-34_NAVIGATION/SW_BASELINE/
- **Interfaces**: CONFIGURATION_BASE/ATA-34_NAVIGATION/ICD/

PLM folders in this domain contain:
- **EBOM_LINKS.md**: References to engineering BOMs in CONFIGURATION_BASE
- **CAx/**: Integration artifacts (navigation performance analysis, sensor fusion diagrams)

## Compliance

### Applicable Standards
- **DO-178C**: Software (FMS, GNSS software)
- **DO-254**: Hardware (IRS, GNSS receivers)
- **DO-160**: Environmental testing
- **DO-229**: GNSS equipment (MOPS)
- **ARINC 424**: Navigation database format
- **ARINC 653**: IMA partitioning (if FMS is IMA-hosted)
- **RTCA DO-236C**: Minimum Aviation System Performance Standards (MASPS) for RNP
- **TSO-C129a**: GPS equipment
- **TSO-C196**: SBAS equipment

### Certification Considerations
- FMS software criticality (typically DAL B or C)
- RNP authorization (RNP-AR, RNP 0.3, etc.)
- GNSS augmentation (SBAS, GBAS)
- Navigation database integrity

## Verification Requirements

### Integration Testing
- Multi-sensor navigation accuracy
- FMS flight plan execution
- Autopilot guidance verification
- Navigation database updates

### Interface Testing
- ARINC 429 signal validation
- IRS alignment and position accuracy
- VOR/ILS/DME signal processing
- FMS-autopilot coupling

### Performance Testing
- RNP navigation accuracy
- FMS prediction accuracy
- Sensor failure detection and isolation

## Known Issues & Risks

### Technical Risks
- GNSS jamming and spoofing
- IRS drift over time
- Navigation database currency
- FMS performance predictions in non-standard conditions

### Mitigation Strategies
- Multi-constellation GNSS for redundancy
- IRS aided by GNSS for drift correction
- Automatic navigation database update alerts
- Conservative FMS performance margins

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2024-01-15 | Systems Integration | Initial integration view |

## References

- [Interface Matrix](./INTERFACE_MATRIX/34↔22_23_24_31_42_45_46_92.csv)
- [CONFIGURATION_BASE/ATA-34](../../../CONFIGURATION_BASE/ATA-34_NAVIGATION/)
- [CONFIG_MGMT ICDs](../../../../00-PROGRAM/CONFIG_MGMT/09-INTERFACES/)
- [ATA-42 Partition Map](../ATA-42_INTEGRATED_MODULAR_AVIONICS/SUBSYSTEMS/ATA-42-90_PARTITION_MAP_APPS/)
