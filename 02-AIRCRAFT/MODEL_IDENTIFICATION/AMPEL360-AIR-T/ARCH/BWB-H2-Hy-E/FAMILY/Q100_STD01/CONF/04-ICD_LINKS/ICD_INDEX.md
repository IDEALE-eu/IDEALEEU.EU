<!-- UTCS: utcs://AMPEL360-AIR-T/BWB-H2-Hy-E/Q100_STD01 -->

# Interface Control Documents (ICD) Index

## Purpose

This index catalogs all Interface Control Documents (ICDs) governing interfaces between systems, subsystems, and domains in the Q100_STD01 configuration.

---

## Active ICDs

| ICD_ID | Title | Version | Owner | Verification Method | Status | Last Updated |
|--------|-------|---------|-------|-------------------|--------|--------------|
| **ICD-CQH-001** | LH₂ Tank ↔ Fuel Cell Interface | 2.1 | CQH Domain | Physical integration test | ✅ ACTIVE | 2025-10-01 |
| **ICD-EEE-003** | Battery ↔ Power Distribution Bus | 1.8 | EEE Domain | Electrical bench test | ✅ ACTIVE | 2025-09-25 |
| **ICD-PPP-005** | Fuel Cell ↔ Electric Motor Interface | 2.0 | PPP Domain | System-level test | ✅ ACTIVE | 2025-10-10 |
| **ICD-AAA-007** | Wing Structure ↔ Propulsion Mounts | 1.5 | AAA Domain | FEA + physical test | ✅ ACTIVE | 2025-09-15 |
| **ICD-IIS-012** | Avionics ↔ Data Bus Protocol | 3.2 | IIS Domain | Protocol analyzer | ✅ ACTIVE | 2025-10-05 |
| **ICD-CQH-AAA-002** | H₂ Tank ↔ Airframe Integration | 1.3 | CQH/AAA Joint | Design review + stress test | ✅ ACTIVE | 2025-08-30 |
| **ICD-EEE-IIS-004** | Power System ↔ Flight Control Computer | 2.5 | EEE/IIS Joint | Integration test | ✅ ACTIVE | 2025-09-20 |
| **ICD-PPP-EEE-006** | Motor Controller ↔ Power Electronics | 1.9 | PPP/EEE Joint | Functional test | ✅ ACTIVE | 2025-10-08 |

---

## ICD Details

### ICD-CQH-001: LH₂ Tank ↔ Fuel Cell Interface

**Scope**: Defines mechanical, thermal, and fluid interfaces between the LH₂ storage tank and PEM fuel cell stack.

**Key Parameters**:
- H₂ flow rate: 0–15 kg/h
- Pressure: 5–8 bar
- Temperature: 20–30 K at tank outlet
- Connector: Parker Hannifin cryogenic coupling
- Leak rate: < 1×10⁻⁶ kg/s

**Document Location**: `00-PROGRAM/CONFIG_MGMT/09-INTERFACES/ICD-AMPEL360-AIR-T-CQH-001.md`

**Verification**: Physical integration test at TRL-6 facility (Munich)

---

### ICD-EEE-003: Battery ↔ Power Distribution Bus

**Scope**: Electrical interface between Li-S battery packs and 800 VDC power distribution bus.

**Key Parameters**:
- Voltage range: 600–900 VDC
- Max current: 3,000 A continuous, 4,500 A peak (30s)
- Connector: TE Connectivity HVP320
- Protection: DC circuit breakers, arc fault detection
- Communication: CAN-FD (5 Mbps)

**Document Location**: `00-PROGRAM/CONFIG_MGMT/09-INTERFACES/ICD-AMPEL360-AIR-T-EEE-003.md`

**Verification**: Electrical bench test with full-power cycling

---

### ICD-PPP-005: Fuel Cell ↔ Electric Motor Interface

**Scope**: Power and control interface between PEM fuel cell stack and electric propulsion motors.

**Key Parameters**:
- Power: 400 kW per motor (6 motors total)
- Voltage: 800 VDC ± 50 V
- Control: Torque command via CAN-FD
- Cooling: Liquid glycol loop, 40–60°C
- Redundancy: Dual power paths per motor

**Document Location**: `00-PROGRAM/CONFIG_MGMT/09-INTERFACES/ICD-AMPEL360-AIR-T-PPP-005.md`

**Verification**: System-level test at iron bird rig

---

### ICD-AAA-007: Wing Structure ↔ Propulsion Mounts

**Scope**: Structural interface for mounting ducted fan propulsion units to wing spar.

**Key Parameters**:
- Load capacity: 50 kN ultimate per mount point
- Attachment: Ti-6Al-4V bolted joint (8× M16 bolts)
- Vibration isolation: Elastomeric bushings
- Inspection access: Removable panels
- Fail-safe: Redundant load paths

**Document Location**: `00-PROGRAM/CONFIG_MGMT/09-INTERFACES/ICD-AMPEL360-AIR-T-AAA-007.md`

**Verification**: FEA analysis + physical pull test

---

### ICD-IIS-012: Avionics ↔ Data Bus Protocol

**Scope**: Network protocol and data format for avionics communication.

**Key Parameters**:
- Bus type: AFDX (ARINC 664-P7)
- Bandwidth: 100 Mbps per channel
- Latency: < 10 ms end-to-end
- Redundancy: Dual channels (A/B)
- Message format: ARINC 429 wrapped in AFDX

**Document Location**: `00-PROGRAM/CONFIG_MGMT/09-INTERFACES/ICD-AMPEL360-AIR-T-IIS-012.md`

**Verification**: Protocol analyzer + network load test

---

## Change Control

All ICD changes require:
1. ECR filed by interface owner
2. Impact assessment on both sides of interface
3. CCB approval
4. Re-verification after implementation
5. Version increment in this index

---

## Cross-Domain ICDs

ICDs with joint ownership (e.g., ICD-CQH-AAA-002) require coordination between multiple domain stewards. Change requests must be co-signed by all affected domains.

---

**Maintained By**: Configuration Management  
**Next Review**: 2025-11-15  
**Contact**: `ccb@idealeeu.eu`
