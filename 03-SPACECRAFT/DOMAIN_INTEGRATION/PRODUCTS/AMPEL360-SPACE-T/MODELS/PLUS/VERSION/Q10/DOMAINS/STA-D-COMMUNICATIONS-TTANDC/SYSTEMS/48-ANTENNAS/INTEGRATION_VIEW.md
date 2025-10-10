# 48-ANTENNAS — Integration View
**AMPEL360-SPACE-T · Q10 Baseline**

> **📌 Purpose**: Define antenna subsystem for RF communications, tracking, and ranging.  
> **✅ Boundary**: 48 owns **antenna radiating elements**, **RF feeds**, **mechanical interfaces**, and **antenna patterns**.  
> **❌ Not owned**: RF transceivers (23), Power (24), Harness/EWIS (97), Structure (51).

---

## System Overview

System 48 provides the antenna subsystem for spacecraft communications, including:
- Antenna radiating elements and arrays
- RF feed networks and distribution
- Polarization control and switching
- Antenna pointing and deployment mechanisms (if applicable)
- RF performance (gain, patterns, VSWR)

---

## Key Interfaces

> 📄 **Full Matrix**: `INTERFACE_MATRIX/48↔06_21_23_24_51_93_97.csv`

| System | ID | Interface Type | Key Exchange |
|--------|----|----------------|--------------|
| Dimensions/Stations | 06 | Mechanical | Antenna envelopes, mounting datums, alignment references |
| Thermal Control | 21 | Thermal | Antenna thermal environment, survival temperatures |
| RF Communications | 23 | RF/Mechanical | Waveguide/coax interface, VSWR < 1.5:1, polarization |
| Electrical Power | 24 | Power | Deployment/pointing mechanism power (if applicable) |
| Primary Structure | 51 | Structural | Mounting interface, load paths, deployment kinematics |
| Databus | 93 | Data | Control/telemetry for mechanisms (if applicable) |
| Harness/EWIS | 97 | Electrical | RF coax routing, mechanism control harness |

---

## Operational Modes

| Mode | Description | Key Parameters |
|------|-------------|----------------|
| **Stowed** | Launch configuration | Antenna locked, deployment mechanisms inhibited |
| **Deployed** | On-orbit nominal | Antenna deployed, nominal RF performance |
| **Pointing** | Active pointing (if applicable) | Gimbal control, pointing accuracy |
| **Safe** | Fault recovery | Fixed pointing or safe position |

---

## Controls & States

### Commands (via 93, if applicable)
- `DEPLOY`, `POINT_AZ`, `POINT_EL`, `STOW`, `BIT_START`

### Telemetry
- `DEPLOY_STATUS`, `VSWR`, `TEMP_ARRAY`, `POINTING_AZ/EL`, `MECHANISM_POSITION`

### Safing Logic
- **Deployment inhibited** during launch and early mission phases
- **Safe pointing** activated on mechanism failure

---

## Budgets (To Be Closed at CDR)

| Domain | Parameter | Target |
|--------|----------|--------|
| **RF** | Gain | TBD dBi |
| | VSWR | < 1.5:1 |
| | Beamwidth | TBD degrees |
| | Polarization | TBD (LHCP/RHCP/Linear) |
| **Power** | Deployment | TBD W |
| | Pointing (if applicable) | TBD W |
| **Mass** | Antenna assembly | TBD kg |
| **Thermal** | Operating range | TBD °C |
| | Survival range | TBD °C |

---

## Verification Strategy

| Method | Scope | Evidence Location |
|--------|------|-------------------|
| **RF Patterns** | Antenna pattern measurements, gain, beamwidth | `PLM/CAx/CMP/pattern_meas__r01__REL.pdf` |
| **VSWR** | Input impedance, return loss | `PLM/CAx/CMP/vswr_test__r01__REL.xlsx` |
| **Deployment** | Mechanism function, deployment dynamics | `PLM/CAx/CAV/deploy_test__r01__REL.pdf` |
| **Environmental** | TVAC, vibe/shock per 51 | `PLM/CAx/CMP/tvac_report__r01__REL.pdf` |
| **OTA Testing** | On-air performance with 23 | `PLM/CAx/CMP/ota_test__r01__REL.pdf` |

---

## Compliance

- **Standards**:  
  - ECSS-E-ST-50-05C (RF Communications)  
  - ECSS-E-ST-20-07C (EMC)
- **Configuration**:  
  - Baseline: **Q10**  
  - UTCS Context: `utcs://AMPEL360/48/Q10`

---

## Ownership & Boundaries — Clarified

- ✅ **48 owns**: Antenna radiating elements, RF feeds, mechanical interfaces, antenna patterns, EBOM and ICDs for antennas.
- ❌ **48 does NOT own**:  
  - RF transceivers/amplifiers → **23-COMMUNICATIONS_RF_LINKS**  
  - Structure/mounting → **51-STRUCTURES** (48 owns interface)
  - Mechanism control software → **42-AVIONICS** or **40-FLIGHT_SOFTWARE**

---
