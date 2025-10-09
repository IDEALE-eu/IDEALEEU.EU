# ATA-31 INDICATING & RECORDING - Integration View

## Overview

Indicating and recording systems integration covering flight deck displays, data acquisition units (DAU), flight data recorders (FDR), cockpit voice recorders (CVR), and quick access recorders (QAR).

## System Architecture

### Displays
- **Primary Flight Display (PFD)**: Attitude, airspeed, altitude, vertical speed
- **Navigation Display (ND)**: Navigation map, flight plan, weather
- **Engine Indication and Crew Alerting System (EICAS/ECAM)**: Engine parameters, system synoptics, alerts
- **Multi-Function Display (MFD)**: Configurable display for various functions

### Display Management
- **Display Units (DU)**: Physical display hardware
- **Display Management Computer (DMC)**: Display rendering and data processing

### Data Acquisition and Recording
- **DAU**: Data Acquisition Unit - collects data from aircraft systems
- **FDR**: Flight Data Recorder (crash-protected)
- **CVR**: Cockpit Voice Recorder (crash-protected)
- **QAR**: Quick Access Recorder (for maintenance and operations analysis)

### Data Buses
- **ARINC 429**: Legacy avionics data bus
- **AFDX (ARINC 664)**: Avionics Full-Duplex Switched Ethernet
- **ARINC 717**: Flight data recorder interface

## Key Interfaces

### Internal Interfaces
- **31 ↔ 22**: Autopilot mode displays
- **31 ↔ 23**: Radio tuning and communication status
- **31 ↔ 24**: Electrical system synoptics and warnings
- **31 ↔ 34**: Navigation data, flight plan display
- **31 ↔ 42**: IMA network for display data
- **31 ↔ 45**: CMC alerts and maintenance messages
- **31 ↔ 46**: Display software loading
- **31 ↔ 92**: EWIS (all wiring in ATA-92)

### Cross-Domain Interfaces
- **31 ↔ All Systems**: Data for recording and display

### Data Flows
- Sensor data → DAU → FDR/QAR
- Flight parameters → DMC → Display Units
- Crew audio → CVR
- Alerts/warnings → EICAS/ECAM displays

## Network Integration

### ARINC 429 Buses
- Air data inputs
- IRS inputs
- Engine data
- System discrete signals

### AFDX Network
- Display data from systems
- High-bandwidth data (e.g., weather radar, terrain database)
- QoS for critical data (alerts, flight-critical parameters)

### ARINC 717
- FDR data frame (typically 64 or 256 words/sec)

## Subsystems

### ATA-31-10: DISPLAYS (DU/DMC)
- Display Units (physical displays)
- Display Management Computers
- Cursor control devices
- Display symbology and graphics

### ATA-31-30: RECORDERS (FDR/CVR/QAR)
- Flight Data Recorder (25-hour solid-state)
- Cockpit Voice Recorder (2-hour minimum)
- Quick Access Recorder (for FOQA/FDM)
- Data Acquisition Units

## PLM Integration

All hardware and software artifacts link to CONFIGURATION_BASE for authoritative configurations:
- **Hardware**: CONFIGURATION_BASE/ATA-31_INDICATING_RECORDING/HW_CONFIG/
- **Software**: CONFIGURATION_BASE/ATA-31_INDICATING_RECORDING/SW_BASELINE/
- **Interfaces**: CONFIGURATION_BASE/ATA-31_INDICATING_RECORDING/ICD/

PLM folders in this domain contain:
- **EBOM_LINKS.md**: References to engineering BOMs in CONFIGURATION_BASE
- **CAx/**: Integration artifacts (display formats, data flow diagrams, FDR parameter lists)

## Compliance

### Applicable Standards
- **DO-178C**: Software (display rendering, DAL B/C)
- **DO-254**: Hardware (display units, recorders)
- **DO-160**: Environmental testing
- **ARINC 429**: Data bus standard
- **ARINC 664**: AFDX network standard
- **ARINC 717**: FDR data frame standard
- **CS-25/FAR 25**: Display and recording requirements
- **ED-112A/DO-178C**: Display software considerations
- **EUROCAE ED-155**: FDR crash-protection standards

### Certification Considerations
- FDR parameter list approval
- CVR audio quality and duration
- Display failure modes (reversionary modes)
- Alert prioritization and presentation

## Verification Requirements

### Integration Testing
- Display data integrity from all sources
- FDR parameter recording verification
- CVR audio quality tests
- QAR data extraction and analysis

### Interface Testing
- ARINC 429 signal validation
- AFDX network performance
- Display reversionary modes
- Recorder crash-survivability

### Human Factors Testing
- Display readability and clarity
- Alert prioritization and presentation
- Crew workload assessment
- Symbology consistency

## Known Issues & Risks

### Technical Risks
- Display sunlight readability
- FDR parameter coverage gaps
- CVR audio quality in high-noise environments
- QAR data latency for real-time monitoring

### Mitigation Strategies
- High-brightness displays with anti-reflective coatings
- Comprehensive FDR parameter list review
- Multiple microphones with noise cancellation
- QAR data buffering and compression

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2024-01-15 | Systems Integration | Initial integration view |

## References

- [Interface Matrix](./INTERFACE_MATRIX/31↔22_23_24_34_42_45_46_92.csv)
- [CONFIGURATION_BASE/ATA-31](../../../CONFIGURATION_BASE/ATA-31_INDICATING_RECORDING/)
- [CONFIG_MGMT ICDs](../../../../00-PROGRAM/CONFIG_MGMT/09-INTERFACES/)
- [Display Data Flows](../../03-INTEGRATION_VIEWS/DISPLAY_DATA_FLOWS.md)
