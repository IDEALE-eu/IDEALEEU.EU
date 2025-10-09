# ATA-22 AUTO FLIGHT - Integration View

## Overview

Automatic Flight Control System (AFCS) integration covering autopilot, flight director, and autothrust systems.

## System Architecture

### Autopilot (AP)
- Lateral and vertical guidance
- Approach modes (ILS, RNP, etc.)
- Altitude hold, heading select
- Speed control integration

### Flight Director (FD)
- Command bar guidance
- Mode annunciations
- FMS coupled modes

### Autothrust (if separate from ATA-76)
- Speed/thrust control
- Integration with flight envelope protection

## Key Interfaces

### Internal Interfaces
- **22 ↔ 24**: Electrical power supply
- **22 ↔ 31**: Mode displays and annunciations
- **22 ↔ 34**: FMS guidance inputs (LNAV/VNAV)
- **22 ↔ 42**: IMA hosting for AFCS applications
- **22 ↔ 45**: CMC monitoring and BITE
- **22 ↔ 46**: Software loading
- **22 ↔ 92**: EWIS (all wiring in ATA-92)

### Cross-Domain Interfaces
- **22 ↔ 27**: Flight control surface commands
- **22 ↔ 76/77**: Engine thrust commands (autothrust)

### Data Flows
- FMS lateral/vertical guidance → AFCS
- AFCS mode status → Displays (ATA-31)
- Autopilot commands → Flight controls (ATA-27)
- Air data inputs → AFCS algorithms

## Network Integration

### ARINC 429 Buses
- Air data inputs (airspeed, altitude, vertical speed)
- IRS inputs (attitude, position)
- FMS guidance commands
- Flight control surface position feedback

### AFDX Network
- AFCS processing (if IMA-hosted)
- Mode control panel interfaces
- Display system data

## Subsystems

### ATA-22-10: AFCS/Autopilot
- Autopilot computer (may be IMA-hosted per ATA-42)
- Mode control panel (MCP)
- Servo actuators interface (if not in ATA-27)

### ATA-22-20: Flight Director
- Flight director computation
- Command bar generation
- Mode logic and transitions

## IMA Hosting (ATA-42 Integration)

If AFCS is IMA-hosted:
- **Partition**: See ATA-42-90_PARTITION_MAP_APPS
- **Software**: Managed in CONFIGURATION_BASE/ATA-22/SW_BASELINE/
- **Criticality**: Typically DAL B or C depending on function
- **Determinism**: ARINC 653 scheduling for safety-critical functions

## PLM Integration

All hardware and software artifacts link to CONFIGURATION_BASE for authoritative configurations:
- **Hardware**: CONFIGURATION_BASE/ATA-22_AUTO_FLIGHT/HW_CONFIG/
- **Software**: CONFIGURATION_BASE/ATA-22_AUTO_FLIGHT/SW_BASELINE/
- **Interfaces**: CONFIGURATION_BASE/ATA-22_AUTO_FLIGHT/ICD/

PLM folders in this domain contain:
- **EBOM_LINKS.md**: References to engineering BOMs in CONFIGURATION_BASE
- **CAx/**: Integration artifacts (control laws, mode logic diagrams)

## Compliance

### Applicable Standards
- **DO-178C**: Software (AFCS algorithms, DAL B/C)
- **DO-254**: Hardware (autopilot computer)
- **DO-160**: Environmental testing
- **ARINC 653**: IMA partitioning (if IMA-hosted)
- **CS-25/FAR 25**: Autopilot certification requirements
- **AC 25-7**: Flight Test Guide for Certification of Transport Category Airplanes

### Certification Considerations
- AFCS failure modes and effects analysis
- Autopilot engagement and disengagement logic
- Flight director reliability
- Integration with flight envelope protection (if applicable)

## Verification Requirements

### Integration Testing
- Autopilot coupled approaches (ILS, RNP)
- FMS-AFCS mode transitions
- Failure mode behavior
- Go-around and TOGA modes

### Interface Testing
- FMS guidance command validation
- Flight control surface command verification
- Mode annunciation accuracy
- Air data and IRS input validation

### Flight Testing
- Autopilot performance across flight envelope
- Mode capture and tracking accuracy
- Turbulence and wind shear response
- Failure transients

## Known Issues & Risks

### Technical Risks
- FMS-AFCS synchronization issues
- Mode confusion or nuisance disconnects
- Autopilot performance in turbulence
- Integration with newer RNP-AR procedures

### Mitigation Strategies
- Rigorous mode logic verification
- Flight director always available as backup
- Conservative engagement criteria
- Extensive flight test validation

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2024-01-15 | Systems Integration | Initial integration view |

## References

- [Interface Matrix](./INTERFACE_MATRIX/22↔24_31_34_42_45_46_92.csv)
- [CONFIGURATION_BASE/ATA-22](../../../CONFIGURATION_BASE/ATA-22_AUTO_FLIGHT/)
- [CONFIG_MGMT ICDs](../../../../00-PROGRAM/CONFIG_MGMT/09-INTERFACES/)
- [ATA-42 Partition Map](../ATA-42_INTEGRATED_MODULAR_AVIONICS/SUBSYSTEMS/ATA-42-90_PARTITION_MAP_APPS/)
