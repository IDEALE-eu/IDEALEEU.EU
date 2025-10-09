# Interface Control Document (ICD) — 54-70 System Interfaces

**ICD Number:** ICD-54-70-001  
**Title:** Nacelles-Pylons Multi-System Integration Interfaces  
**Version:** 1.0  
**Date:** 2024-01-15  
**Status:** Active

## Document Control

| Field | Value |
|---|------|
| Document Number | ICD-54-70-001 |
| Version | 1.0 |
| Status | Active |
| Release Date | 2024-01-15 |
| Next Review Date | 2024-07-15 |
| Configuration Baseline | [CDR](../../../../../../../../../00-PROGRAM/CONFIG_MGMT/04-BASELINES/CDR/) |

## Approvals

| Role | Name | Signature | Date |
|---|---|---|---|
| Systems Engineering Lead | [Name] | [Signature] | YYYY-MM-DD |
| Propulsion Integration Lead | [Name] | [Signature] | YYYY-MM-DD |
| Electrical Systems Lead | [Name] | [Signature] | YYYY-MM-DD |
| Configuration Manager | [Name] | [Signature] | YYYY-MM-DD |

## Revision History

| Version | Date | Author | Description of Changes |
|---|---|---|---|
| 1.0 | 2024-01-15 | Systems Engineering | Initial release for BWB-H2-Hy-E Q100 |

## 1. Introduction

### 1.1 Purpose
This Interface Control Document (ICD) defines and controls all mechanical, electrical, fluid, and data interfaces between the 54-NACELLES-PYLONS system and interfacing aircraft systems for the BWB-H2-Hy-E hybrid-electric aircraft configuration.

### 1.2 Scope
This ICD covers the following interface categories:
- High-voltage electrical power distribution interfaces
- Hydrogen fuel system cryogenic interfaces
- Flight control and engine management data interfaces
- Emergency and safety system interfaces
- Thermal management and cooling system interfaces

### 1.3 Interface Parties

**Party A: 54-NACELLES-PYLONS**  
- Organization: AAA-AIRFRAMES-AERODYNAMICS-AIRWORTHINESS  
- Point of Contact: Propulsion Integration Lead

**Party B: Interfacing Systems**
- **24-ELECTRICAL**: Electrical Power System
- **28-FUEL**: Hydrogen Fuel System
- **31-INSTRUMENTS**: Instrumentation and Sensors
- **71-POWERPLANT**: Propulsion System
- **22-AUTO-FLIGHT**: Flight Control System
- **26-FIRE-PROTECTION**: Fire Detection and Suppression
- **21-AIR-CONDITIONING**: Thermal Management and Cooling

### 1.4 Applicable Documents

| Document Number | Title | Version |
|---|---|---|
| AMPEL360-SPEC-001 | BWB-H2-Hy-E System Requirements | 2.1 |
| AMPEL360-ICD-024 | Electrical Power Distribution | 1.3 |
| AMPEL360-ICD-028 | Hydrogen Fuel System | 1.2 |
| AMPEL360-ICD-071 | Propulsion System Integration | 2.0 |
| MIL-STD-1760 | Aircraft/Store Electrical Interconnection System | Rev E |
| ARINC 429 | Mark 33 Digital Information Transfer System | Rev 18 |
| ARINC 664 | Aircraft Data Network | Part 7 |

## 2. Interface Overview

### 2.1 Interface Summary

This ICD manages the following primary interfaces:

1. **Electrical Power Interfaces (24↔54)**
   - High-voltage DC power distribution (800V DC)
   - Electric motor power feeds
   - Electromagnetic grounding and bonding

2. **Hydrogen Fuel Interfaces (28↔54)**
   - Cryogenic fuel supply lines (-253°C)
   - Fuel management and distribution
   - Leak detection and safety isolation

3. **Data and Control Interfaces (22/31/71↔54)**
   - ARINC 429 communication buses
   - ARINC 664 (AFDX) network
   - Discrete signals for safety-critical functions

4. **Safety and Emergency Interfaces (26↔54)**
   - Fire detection sensor integration
   - Fire suppression system activation
   - Emergency shutdown signals

5. **Thermal Management Interfaces (21↔54)**
   - Electric motor cooling air supply
   - Heat exchanger integration
   - Thermal monitoring sensors

### 2.2 Interface Locations

All interface locations are referenced to the aircraft coordinate system:
- Origin: Fuselage nose reference point
- X-axis: Positive aft
- Y-axis: Positive right wing
- Z-axis: Positive up

Interface locations documented in `INTERFACE_LOCATIONS.csv`

## 3. Mechanical Interfaces

### 3.1 Structural Attachment Interfaces

**Interface ID:** MECH-54-51-001  
**Description:** Primary pylon-to-wing structural attachment

| Parameter | Specification |
|---|---|
| Attachment Points | 6 locations per pylon |
| Bolt Size | M24 Class 12.9 |
| Torque | 450 Nm ± 10 Nm |
| Material | Ti-6Al-4V |
| Load Capacity | Ultimate: 250 kN per fastener |
| Inspection | Torque check every 500 flight hours |

### 3.2 Fuel Line Interfaces

**Interface ID:** MECH-54-28-001  
**Description:** Cryogenic hydrogen fuel line connections

| Parameter | Specification |
|---|---|
| Connection Type | Quick-disconnect cryogenic coupling |
| Line Size | 50 mm inner diameter |
| Operating Pressure | 5 bar nominal, 10 bar maximum |
| Operating Temperature | -253°C (liquid H₂) |
| Material | Stainless steel 316L with internal insulation |
| Leak Rate | < 1 × 10⁻⁶ mbar·L/s |
| Thermal Expansion | Bellows section accommodates ±25 mm |

### 3.3 Dimensional Tolerances

All mechanical interface dimensions shall be maintained within ±0.5 mm unless otherwise specified. Critical alignment interfaces (engine mounts, pylon attachments) shall be maintained within ±0.1 mm.

## 4. Electrical Interfaces

### 4.1 High-Voltage Power Distribution

**Interface ID:** ELEC-54-24-001  
**Description:** High-voltage DC power feed to electric motors

| Parameter | Specification |
|---|---|
| Voltage | 800V DC nominal (700-850V range) |
| Current Capacity | 500A continuous, 750A peak (5 sec) |
| Connector Type | Amphenol EPIC H-BE Series |
| Cable Type | Shielded high-voltage cable, 95 mm² |
| EMI Shielding | 360° shield termination, >80 dB attenuation |
| Insulation | Rated for 3000V DC test voltage |
| Grounding | Dedicated safety ground, <0.1 Ω resistance |

**Pin Assignment:**

| Pin | Signal | Wire Gauge | Notes |
|---|---|---|---|
| 1 | +800V DC Power | 95 mm² | Red cable |
| 2 | Power Return | 95 mm² | Black cable |
| 3 | Safety Ground | 50 mm² | Green/Yellow |
| 4 | Shield Ground | - | Drain wire |

### 4.2 Control and Monitoring Signals

**Interface ID:** ELEC-54-71-001  
**Description:** Engine control and monitoring interface

| Parameter | Specification |
|---|---|
| Connector Type | Deutsch D38999/24 Series III |
| Contact Type | Size 20 pins |
| Cable Type | Shielded twisted pair, MIL-C-27500 |
| Signal Voltage | 28V DC logic levels |
| Current per Pin | 5A maximum |

**Discrete Signals:**

| Signal Name | Pin | Direction | Type | Function |
|---|---|---|---|---|
| MOTOR_START | A1 | 54←71 | Discrete | Motor start command |
| MOTOR_RUNNING | A2 | 54→71 | Discrete | Motor running status |
| OVER_TEMP | A3 | 54→71 | Discrete | Over-temperature warning |
| EMERGENCY_STOP | A4 | 54←71 | Discrete | Emergency shutdown |
| FAULT_INDICATOR | A5 | 54→71 | Discrete | General fault status |

### 4.3 Electromagnetic Compatibility

All electrical interfaces shall comply with:
- DO-160G Section 20: Radio Frequency Susceptibility
- DO-160G Section 21: Emission of Radio Frequency Energy
- MIL-STD-461G: EMI/EMC Requirements

Measured EMI levels shall not exceed Category M limits per DO-160G.

## 5. Fluid Interfaces

### 5.1 Hydrogen Fuel Supply

**Interface ID:** FLUID-54-28-001  
**Description:** Liquid hydrogen fuel supply to propulsion system

| Parameter | Specification |
|---|---|
| Fluid | Liquid hydrogen (LH₂), 99.99% purity |
| Temperature | -253°C ± 2°C |
| Pressure | 5 bar nominal (3-7 bar operating range) |
| Flow Rate | 0-50 kg/min per engine |
| Connection | Bayonet-type cryogenic coupling |
| Insulation | Multi-layer vacuum insulation (MLI) |
| Vent System | Boil-off venting to atmosphere via 25 mm vent line |

### 5.2 Cooling Air Supply

**Interface ID:** FLUID-54-21-001  
**Description:** Cooling air for electric motor thermal management

| Parameter | Specification |
|---|---|
| Fluid | Ram air from inlet system |
| Temperature | -40°C to +50°C ambient |
| Pressure | 1.1 bar (ram pressure) |
| Flow Rate | 2.5 kg/s per motor (continuous) |
| Duct Size | 150 mm diameter |
| Filtration | 100 micron particle filter |

### 5.3 Fire Suppression

**Interface ID:** FLUID-54-26-001  
**Description:** Fire suppression agent distribution

| Parameter | Specification |
|---|---|
| Agent | Halon alternative (HFC-125 or equivalent) |
| Pressure | 25 bar stored, 5 bar discharge |
| Discharge Time | Complete discharge in <1 second |
| Nozzle Type | Multi-port spray nozzle |
| Coverage | Complete nacelle internal volume |

## 6. Data Interfaces

### 6.1 ARINC 429 Communication

**Interface ID:** DATA-54-71-001  
**Description:** Engine monitoring and control data bus

| Parameter | Specification |
|---|---|
| Protocol | ARINC 429 Mark 33 DITS |
| Bit Rate | 100 kbps (high speed) |
| Word Format | 32-bit data word |
| Bus Type | Point-to-point, unidirectional |
| Connector | D38999 connector (twisted shielded pair) |
| Update Rate | 10 Hz typical, 50 Hz maximum |

**Key Data Labels:**

| Label (Octal) | Parameter | Units | Range | Resolution |
|---|---|---|---|---|
| 015 | Motor Speed | RPM | 0-15000 | 1 RPM |
| 016 | Motor Torque | Nm | 0-5000 | 0.1 Nm |
| 017 | Motor Temperature | °C | -50-250 | 0.1°C |
| 020 | Motor Current | A | 0-750 | 0.1 A |
| 021 | Motor Voltage | V | 0-900 | 0.1 V |
| 030 | Fuel Flow | kg/min | 0-50 | 0.01 kg/min |
| 031 | H₂ Temperature | K | 20-300 | 0.1 K |
| 032 | H₂ Pressure | bar | 0-10 | 0.01 bar |

### 6.2 ARINC 664 Network (AFDX)

**Interface ID:** DATA-54-ALL-001  
**Description:** High-speed data network for system integration

| Parameter | Specification |
|---|---|
| Protocol | ARINC 664 Part 7 (AFDX) |
| Data Rate | 100 Mbps (switched Ethernet) |
| Topology | Redundant dual network (A and B) |
| Connector | RJ-45 or D38999 with Ethernet contacts |
| Cable Type | CAT-6 shielded twisted pair |
| Virtual Links | Dedicated VLs per system interface |

**Virtual Link Allocation:**

| VL ID | Source | Destination | BAG (ms) | Max Frame (bytes) |
|---|---|---|---|---|
| 1001 | 54-NACELLES | 71-POWERPLANT | 20 | 1518 |
| 1002 | 71-POWERPLANT | 54-NACELLES | 20 | 1518 |
| 1003 | 54-NACELLES | 22-AUTO-FLIGHT | 50 | 512 |
| 1004 | 54-NACELLES | 31-INSTRUMENTS | 100 | 256 |

### 6.3 Message Formats

All AFDX messages shall use standardized formats per `DATA_DICTIONARY.csv`:
- Header: 8 bytes (timestamp, sequence, source ID)
- Payload: Variable length, defined per message type
- CRC: 4 bytes (CRC-32)

## 7. Thermal Interfaces

### 7.1 Thermal Management Requirements

**Interface ID:** THRM-54-21-001  
**Description:** Electric motor cooling heat rejection

| Parameter | Specification |
|---|---|
| Heat Load | 150 kW per motor (continuous) |
| Peak Heat Load | 225 kW per motor (5 min) |
| Cooling Method | Forced air cooling with heat exchanger |
| Coolant | Air (primary), glycol/water (secondary HX) |
| Inlet Temperature | Ambient ±10°C |
| Outlet Temperature | Max 150°C |
| Temperature Sensors | Type K thermocouple, ±1°C accuracy |

### 7.2 Cryogenic Thermal Management

**Interface ID:** THRM-54-28-001  
**Description:** Liquid hydrogen thermal management

| Parameter | Specification |
|---|---|
| Insulation | Multi-layer vacuum insulation (10-20 layers) |
| Heat Leak | <5 W per meter of fuel line |
| Boil-off Rate | <0.5% per hour at ground idle |
| Thermal Monitoring | Cryogenic RTD sensors, ±0.1 K |
| Vent Temperature | <-100°C at vent outlet |

## 8. Safety and Hazards

### 8.1 Hazard Analysis

The following hazards have been identified and mitigated:

**HAZ-54-001: Hydrogen Leak**
- **Severity:** Catastrophic
- **Mitigation:** Redundant leak detection, automatic isolation valves, ventilation system
- **Detection:** Hydrogen sensors at 1% LEL threshold
- **Response Time:** <100 ms for valve closure

**HAZ-54-002: High-Voltage Electric Shock**
- **Severity:** Catastrophic
- **Mitigation:** Insulation rated for 3× operating voltage, interlocked access panels, automatic discharge
- **Detection:** Ground fault detection <1 Ω
- **Response Time:** <10 ms for system isolation

**HAZ-54-003: Electromagnetic Interference**
- **Severity:** Major
- **Mitigation:** 360° shielding, filtered connectors, segregated routing
- **Verification:** EMI testing per DO-160G

**HAZ-54-004: Fire in Nacelle**
- **Severity:** Catastrophic
- **Mitigation:** Fire detection system, automatic suppression, hydrogen isolation
- **Detection:** Dual-channel optical/thermal detectors
- **Response Time:** <1 s for suppression activation

### 8.2 Safety-Critical Functions

The following functions are classified as DAL A (Design Assurance Level A):
- Emergency engine shutdown
- Hydrogen fuel isolation
- Fire detection and suppression
- High-voltage system isolation

## 9. Testing and Verification

### 9.1 Interface Verification Requirements

All interfaces shall be verified through the following test methods:

**Mechanical Interfaces:**
- Dimensional inspection (CMM measurement)
- Fit check assembly
- Ultimate load testing
- Thermal cycling (-55°C to +85°C)

**Electrical Interfaces:**
- Continuity and resistance testing
- Insulation resistance (1000V Megger)
- EMI/EMC testing per DO-160G
- High-potential (HiPot) testing at 2× voltage + 1000V

**Fluid Interfaces:**
- Leak testing (helium mass spectrometry)
- Pressure testing at 1.5× maximum operating pressure
- Flow testing across operating range
- Cryogenic thermal performance testing

**Data Interfaces:**
- Protocol compliance testing
- Bit error rate testing (BER < 10⁻⁹)
- Latency measurement
- Message content validation

### 9.2 Interface Integration Testing

System-level integration testing shall include:
- Iron Bird testing (complete system integration)
- Ground run testing (propulsion system operation)
- Electromagnetic compatibility testing
- Safety system functional testing
- Emergency scenario testing

### 9.3 Test Evidence

All test results shall be documented in:
- `54-90_QUALIFICATION_TESTS/TEST_EVIDENCE/`
- Traceability maintained in `TRACE/REQ2TEST.csv`

## 10. Configuration Management

### 10.1 Interface Change Control

All interface changes require:
1. Engineering Change Request (ECR) submission
2. Impact analysis on interfacing systems
3. Configuration Control Board (CCB) approval
4. Updated ICD release with revision history
5. Regression testing of affected interfaces

### 10.2 Interface Baselines

Interface configurations are controlled at the following baselines:
- **SRR**: Preliminary interface definitions
- **PDR**: Interface requirements and specifications
- **CDR**: Detailed interface designs and ICDs (current)
- **TRR**: Interface test procedures and plans
- **PRR**: Interface verification evidence

### 10.3 Version Control

This ICD is maintained under configuration control:
- Repository: `02-AIRCRAFT/DOMAIN_INTEGRATION/.../54-NACELLES-PYLONS/SUBSYSTEMS/54-70_SYSTEM_INTERFACES/`
- Version control: Git
- Change tracking: ECR/ECO system
- Approval: CCB

## 11. Points of Contact

### 11.1 Technical Contacts

| System | Contact | Email | Phone |
|---|---|---|---|
| 54-NACELLES-PYLONS | Propulsion Integration Lead | [email] | [phone] |
| 24-ELECTRICAL | Electrical Systems Lead | [email] | [phone] |
| 28-FUEL | Fuel Systems Lead | [email] | [phone] |
| 71-POWERPLANT | Propulsion Systems Lead | [email] | [phone] |

### 11.2 Configuration Management

| Role | Contact | Email |
|---|---|---|
| Configuration Manager | [Name] | [email] |
| CCB Chairperson | [Name] | [email] |

## 12. Appendices

### Appendix A: Interface Location Drawings
Reference: `PLM/CAx/CAD/interface_locations.dwg`

### Appendix B: Connector Pin-Out Details
Reference: `ELECTRICAL_INTERFACES.md`

### Appendix C: Data Message Catalog
Reference: `DATA_INTERFACES.md`

### Appendix D: Test Procedures
Reference: `54-90_QUALIFICATION_TESTS/`

---

**Document Control**
- **Classification:** Internal Use
- **Export Control:** ITAR Controlled (if applicable)
- **Distribution:** Controlled distribution per project access list

**Next Review Date:** 2024-07-15

---

**End of ICD-54-70-001**
