# 23-COMMUNICATIONS_RF_LINKS — Integration View  
**AMPEL360-SPACE-T · Q10 Baseline**

> **📌 Purpose**: Define the integrated RF link chain for TT&C and payload downlink/uplink.  
> **✅ Boundary**: 23 owns **RF hardware**, **link budgets**, **frequency plan**, and **RF signal conditioning**.  
> **❌ Not owned**: Antennas (48), Power (24), Harness/EWIS (97), Flight Software (40/42), Ground Ops (STA-L).

---

## Functional Architecture

| Block | Function | Hosted In |
|------|--------|----------|
| **Baseband/IF Interface** | CCSDS frames in (TX), telemetry/status out (RX) | Logical ICD to **42-AVIONICS** / **93-DATABUS** |
| **Frequency Conversion** | Synthesizers, up/downconverters, LO distribution | 23-LRUs (e.g., 23-20_CONVERTERS) |
| **RF Conditioning** | AGC/attenuation, filtering, diplexing, switch matrix | 23-LRUs |
| **Front-End** | LNA/LNB (RX), SSPA/TWTA (TX) | 23-LRUs |
| **Antenna Interface** | Waveguide/coax feeds, OMTs, polarization control | Mechanical/RF I/F to **48-ANTENNAS** |
| **Timing Reference** | 10 MHz + 1 PPS disciplined reference | From **41-TIME_NAV** |

---

## Key Interfaces

> 📄 **Full Matrix**: `INTERFACE_MATRIX/23↔06_15_21_24_41_42_48_51_93_97.csv`

| System | ID | Interface Type | Key Exchange |
|--------|----|----------------|--------------|
| Dimensions/Stations | 06 | Mechanical | RF equipment envelopes, waveguide keep-outs, EMI clearance zones |
| Data Handling | 31 | Logical | CCSDS frame structure (ICD only; no hardware) |
| Thermal Control | 21 | Thermal | PA/converter waste heat (W), cold-plate interface, survival limits |
| Electrical Power | 24 | Power | 28V ±10%, inrush current, brownout recovery behavior |
| Time/Navigation | 41 | Timing | Disciplined 10 MHz, 1 PPS (jitter < 10 ns) |
| Avionics/FSW | 42 | Command/Telemetry | Endpoints hosted in **42-10_OBC_MAIN_BACKUP** |
| Antennas | 48 | RF/Mechanical | Waveguide/coax type, VSWR < 1.5:1, polarization alignment |
| Primary Structure | 51 | Structural | Mounting stiffness, grounding/bonding points (impedance < 2.5 mΩ) |
| Databus | 93 | Data | 1553/SpW/CAN/ETH control & TM (routed via 42) |
| Harness/EWIS | 97 | Electrical | Coax type (e.g., RG402), connectors (SMA/2.92), EMC shielding |

---

## Operational Modes

| Mode | Description | Key Parameters |
|------|-------------|----------------|
| **RF-SAFE** | Safe configuration | TX inhibited, RX enabled, max attenuation |
| **LEOP/Acquisition** | Launch & early orbit | Low-rate beacon, high EIRP, open-loop AGC |
| **Nominal TT&C** | Routine operations | Scheduled duplex, closed-loop AGC/PWR |
| **Payload Downlink** | Science data return | High-rate modulation (e.g., 256-QAM), PA at high-power setpoint |
| **Emergency Low-Rate** | Fault recovery | Robust coding (e.g., LDPC), RX-only fallback |
| **Test/BIT** | Built-in test | Loopback, tone gen, BER/Eb/N0 measurement |

---

## Controls & States

### Commands (via 42/93)
- `TX_EN`, `PA_LEVEL`, `RX_PATH_SEL`, `ATTEN_SET[dB]`, `LO_SEL`, `SW_MATRIX_CFG[id]`, `MUTE`, `BIT_START`

### Telemetry
- `PA_V/I/T`, `LNA_T`, `RF_PWR_FWD/REV`, `RSSI`, `AGC_LEVEL`, `LO_LOCK`, `BER/FER`, `MER/Eb/N0`, `WG_TEMP`, `VSWR`

### Safing Logic
- **TX inhibited** on: door-open, proximity sensor trigger, or thermal/electrical limit violation  
- **RX-only mode** activated  
- **PA crowbar trip** reported to 42 for FDIR

---

## Budgets (To Be Closed at CDR)

| Domain | Parameter | Target |
|--------|----------|--------|
| **Link** | EIRP | TBD dBW |
| | G/T | TBD dB/K |
| | Eb/N0 margin | ≥ 3 dB |
| | Implementation loss | ≤ 1.5 dB |
| **Power** | TX peak | TBD W |
| | RX avg | TBD W |
| | Standby | TBD W |
| **Mass** | Unit masses | TBD kg |
| | RF harness delta | TBD kg |
| **Thermal** | PA waste heat | TBD W |
| | Cold-case survival | ≥ -40°C |

---

## Verification Strategy

| Method | Scope | Evidence Location |
|--------|------|-------------------|
| **Link Analysis** | End-to-end (CCSDS), Doppler, rain fade (X/Ka) | `PLM/CAx/CAE/link_analysis__r01__REL.pdf` |
| **Environmental** | TVAC with RF load, vibe/shock per 51 | `PLM/CAx/CMP/tvac_report__r01__REL.pdf` |
| **RF Performance** | IP3, ACPR, phase noise, NF, VSWR | `PLM/CAx/CMP/rf_test__r02__REL.xlsx` |
| **Data Integrity** | BER/Eb/N0, AGC dynamics, switch transients | `PLM/CAx/CAV/hil_ber__r01__REL.zip` |
| **EMC** | CE/RE/CS/RS with coax/waveguide | `PLM/CAx/CMP/emc_cert__r01__REL.pdf` |
| **OTA** | Chamber patterns (with 48), on-air pass | `PLM/CAx/CMP/ota_test__r01__REL.pdf` |

> 📁 **Flight SW Evidence**:  
> `.../STA-F-AVIONICS-FSW-DATABUS/SYSTEMS/40-FLIGHT_SOFTWARE/PLM/CAx/CMP/`

---

## Compliance

- **Standards**:  
  - CCSDS 130.0-G-3 (RF)  
  - ECSS-E-ST-50-05C (RF Communications)  
  - ECSS-E-ST-20-07C (EMC)  
  - ECSS-Q-ST-20-06C (EEE Parts)  
- **Regulatory**: ITU filings (payload bands), S-band TT&C allocations (per national authority)  
- **Configuration**:  
  - Baseline: **Q10**  
  - UTCS Context: `utcs://AMPEL360/23/Q10`  
  - IEF Manifests: `PLM/.ief/23-rf.evidence.ief.json`

---

## Ownership & Boundaries — Clarified

- ✅ **23 owns**: RF hardware units, link budgets, frequency plan, RF ICDs.  
- ❌ **23 does NOT own**:  
  - Any software/firmware → lives in **42-AVIONICS** or **40-FLIGHT_SOFTWARE**  
  - Antenna radiating elements → **48-ANTENNAS**  
  - RF switch matrix **mechanical housing** → if part of antenna farm, owned by 48; otherwise, 23 owns RF function, 51 owns structure.  
- 🔗 **Parameters** (e.g., PA setpoints) are defined by 23 but stored in **40/42 configuration evidence**.

---
