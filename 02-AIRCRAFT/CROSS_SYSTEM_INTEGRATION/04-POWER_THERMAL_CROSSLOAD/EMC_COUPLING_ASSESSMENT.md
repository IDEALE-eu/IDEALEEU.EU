# EMC Coupling Assessment

## Overview

This document assesses electromagnetic compatibility (EMC) coupling between aircraft systems per DO-160G and CS-25 requirements.

## EMC Requirements

### DO-160G Environmental Categories
- **Section 15 - Magnetic Effect**: Category Z (worst case)
- **Section 16 - Power Input**: Category A (normal voltage variation)
- **Section 17 - Voltage Spike**: Category A (standard aircraft)
- **Section 18 - Audio Frequency Conducted Susceptibility**: Category A
- **Section 19 - Induced Signal Susceptibility**: Category A
- **Section 20 - Radio Frequency Susceptibility**: Category T (typical)
- **Section 21 - Emission of RF Energy**: Category M (equipment with intentional RF)
- **Section 22 - Lightning Induced Transient Susceptibility**: Category A
- **Section 25 - Electrostatic Discharge**: Category A

### CS-25 Requirements
- **CS-25.1317**: High-Intensity Radiated Fields (HIRF) protection
- **CS-25.899**: Electrical bonding and protection against lightning
- **CS-25.1353**: Electrical equipment and installations

## Coupling Paths

### Conductive Coupling
**Path**: Via power and ground wiring
**Risk Areas**:
- Shared ground returns between critical and non-critical systems
- Long cable runs acting as antennas
- Power supply ripple/noise injection

**Mitigation**:
- Star-grounding architecture for critical systems
- Dedicated power feeds for DAL A systems
- EMI filters on all power inputs (common-mode and differential-mode)
- Shielded twisted-pair for sensitive signals

### Radiated Coupling
**Path**: Via electromagnetic fields (near-field and far-field)
**Risk Areas**:
- High-power radar (WX-RADAR-1: 200W transmit) near sensitive receivers
- WiFi/cellular transmitters in Zone 4 coupling to avionics
- HIRF from external sources (ground radar, nearby aircraft)

**Mitigation**:
- Physical separation: >1 meter between high-power transmitters and sensitive LRUs
- Shielded enclosures for all avionics (>80 dB shielding effectiveness)
- Low-pass filtering on signal lines entering/exiting enclosures
- HIRF testing per DO-160G Section 20 Category T (200 V/m)

### Substrate/Chassis Coupling
**Path**: Via common mounting structure
**Risk Areas**:
- Ground loops between LRUs mounted on same rack
- High-frequency currents on mounting structure

**Mitigation**:
- Single-point grounding per equipment bay
- Bonding straps: <2.5 mΩ impedance per CS-25.899
- Isolation washers for sensitive equipment where needed

## Critical Coupling Scenarios

### Scenario 1: Weather Radar Near GPS
**Risk**: WX-RADAR-1 (1.5 kW peak, X-band 9.3 GHz) desensing GPS-1 (L1: 1.575 GHz, L5: 1.176 GHz)
**Assessment**: 
- Physical separation: 2.5 meters (adequate per analysis)
- Frequency separation: No harmonics of GPS in radar band
- GPS antenna on top of fuselage, radar in nose (maximum separation)
**Mitigation**: 
- GPS antenna shielding (rear-facing, ground plane)
- Radar antenna steering pattern (null towards GPS antenna)
**Status**: ✓ PASS - No GPS desensitization observed in testing

### Scenario 2: AFDX Switch EMI to Flight Control
**Risk**: High-speed digital switching in AFDX-SW-1/SW-2 (100 MHz clocks) coupling to FCC-1/FCC-2
**Assessment**:
- Worst-case radiated emission: -20 dBm @ 100 MHz
- FCC susceptibility threshold: +10 dBm (30 dB margin)
**Mitigation**:
- Switches in shielded enclosure (>60 dB)
- Spread-spectrum clocking to reduce peak emissions
- Physical separation: >0.5 meters
**Status**: ✓ PASS - No interference observed

### Scenario 3: Lightning Strike to Airframe
**Risk**: Lightning-induced transients coupling to avionics via structure and cabling
**Assessment**: Per DO-160G Section 22 (Lightning Induced Transient Susceptibility)
**Mitigation**:
- All LRUs tested to DO-160G Section 22, Category A
- Transient voltage suppressors (TVS) on all power and signal lines
- Shielded cables for critical functions (flight control, engine control)
- Cable shields bonded at both ends for low-frequency transients, single-point for high-frequency
**Status**: ✓ PASS - All LRUs qualified to DO-160G Section 22

### Scenario 4: Passenger WiFi Coupling to Avionics
**Risk**: WiFi transmitters in Zone 4 (2.4/5 GHz, up to 1W) coupling to safety-critical systems
**Assessment**:
- Physical isolation: Zone 4 completely separate from Zones 1/2/3
- No shared cabling or structure
- Metal bulkhead between passenger cabin and avionics bay (>80 dB shielding)
**Mitigation**:
- Complete network isolation (no routing between zones)
- Physical barriers (metal bulkheads, shielded doors)
- Avionics LRUs tested to DO-160G Section 20 at WiFi frequencies
**Status**: ✓ PASS - No coupling path exists

## EMI/EMC Test Evidence

### DO-160G Testing
All LRUs tested per DO-160G:
- **Section 20 - RF Susceptibility**: 20 V/m (Category T), 200 V/m for HIRF per CS-25.1317
- **Section 21 - RF Emissions**: Conducted and radiated per Category M limits
- **Section 22 - Lightning**: Waveforms 1-5A per Category A

**Test Reports**: See [07-INTEGRATION_TEST/EVIDENCE/REPORTS/EMC_TESTING/](../../07-INTEGRATION_TEST/EVIDENCE/REPORTS/)

### Aircraft-Level HIRF Testing
- Whole-aircraft HIRF testing per CS-25.1317
- Frequency range: 10 kHz to 40 GHz
- Field strength: 200 V/m (critical systems), 100 V/m (essential systems)
- No safety-related anomalies observed

### Lightning Strike Testing
- Indirect effects testing per DO-160G Section 22
- Direct effects testing per CS-25.899 (bonding, structure)
- Acceptable: No loss of critical function, transient anomalies acceptable with recovery

## Bonding and Grounding

### Bonding Requirements
- All LRUs bonded to structure: <2.5 mΩ per CS-25.899
- Cable shields bonded to connectors (360° backshells)
- Equipment bay bonding studs: <1 mΩ to structure

### Grounding Architecture
- **Star Ground**: Critical systems (flight control, engine control) have dedicated ground returns to power source
- **Single-Point Ground**: Avionics racks have single ground connection per bay
- **Multi-Point Ground**: High-frequency systems grounded at both ends (cable shields)

### Lightning Protection
- Composite structures: Embedded copper mesh for conductivity
- Fuel tanks: Bonding and static discharge paths
- Radome: Conductive coating, bonded to structure
- All external antennas: Lightning diverter strips

## Crosstalk Analysis

### Cable Routing
- Critical signal cables (flight control, engine control) routed separately from power cables
- Minimum separation: 6 inches from high-power cables, 3 inches from low-power
- Shielded twisted-pair for all ARINC 429, CAN, and discrete signals

### Crosstalk Budget
- Near-End Crosstalk (NEXT): <-40 dB (acceptable)
- Far-End Crosstalk (FEXT): <-50 dB (acceptable)
- Alien Crosstalk: <-60 dB between cable bundles

## Compliance Evidence

### DO-160G Test Reports
- All LRUs tested and qualified per DO-160G applicable sections
- Test reports archived in [07-INTEGRATION_TEST/EVIDENCE/REPORTS/EMC_TESTING/](../../07-INTEGRATION_TEST/EVIDENCE/REPORTS/)

### CS-25 Compliance
- **CS-25.1317 (HIRF)**: Whole-aircraft HIRF testing completed, compliance demonstrated
- **CS-25.899 (Lightning)**: Bonding and lightning protection design compliant
- **CS-25.1353 (Electrical)**: Electrical system design review approved

### Stage Gate Status
- **CDR**: EMC analysis complete, mitigation plan approved
- **TRR**: EMC testing (LRU-level) complete
- **FRR**: Aircraft-level HIRF and lightning testing complete

## References

- **DO-160G**: Environmental Conditions and Test Procedures for Airborne Equipment
- **CS-25**: Certification Specifications for Large Aeroplanes
- **MIL-STD-464**: Electromagnetic Environmental Effects Requirements for Systems
- **[POWER_BUDGET.csv](./POWER_BUDGET.csv)** - Power system design
- **[02-NETWORKS_DATA_BUS/CYBER_BOUNDARIES.md](../../02-NETWORKS_DATA_BUS/CYBER_BOUNDARIES.md)** - Zone isolation

## Revision History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2024-10-08 | EMC Engineering Team | Initial EMC coupling assessment |
