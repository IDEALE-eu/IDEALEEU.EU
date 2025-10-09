# Configuration to Requirements Mapping

## Purpose

This document establishes traceability between Q100 configuration items and their source requirements.

## Traceability Matrix

### Configuration Sets

| Config ID | Requirement Source | Requirement IDs | Notes |
|-----------|-------------------|-----------------|-------|
| CFG-BASELINE-Q100 | Top-Level Aircraft Requirements (TLAR) | TLAR-001, TLAR-015, TLAR-023 | Standard production config |
| CFG-PAX-Q100 | Customer Requirements | CUST-REQ-005, CUST-REQ-012 | Dual-class layout |

### System Requirements

#### ATA 24 — Electrical Power
- **Config Item:** Fuel cell power system (1.2-1.5 MW)
- **Requirements:**
  - SYS-REQ-024-010: Primary power generation
  - SYS-REQ-024-020: Battery backup minimum 150 kWh
  - CERT-REQ-024-005: CS-25.1351 (Electrical system requirements)
- **Verification:** See [10-TRACEABILITY](../../../../../../../00-PROGRAM/CONFIG_MGMT/10-TRACEABILITY/)

#### ATA 28 — Fuel (H₂)
- **Config Item:** LH₂ tank system (4500-5500 kg)
- **Requirements:**
  - SYS-REQ-028-015: LH₂ storage capacity
  - SYS-REQ-028-025: Boil-off management
  - CERT-REQ-028-010: CS-25.863 (Fuel system safety)
  - CERT-REQ-028-020: ISO 19880-8 (H₂ fuel system)
- **Verification:** See [10-TRACEABILITY](../../../../../../../00-PROGRAM/CONFIG_MGMT/10-TRACEABILITY/)

#### ATA 32 — Landing Gear
- **Config Item:** Dual-wheel bogie configuration
- **Requirements:**
  - SYS-REQ-032-010: Main gear load capacity
  - SYS-REQ-032-030: MTOW support (72-76t)
  - CERT-REQ-032-005: CS-25.721 (Landing gear structural)
- **Verification:** See [10-TRACEABILITY](../../../../../../../00-PROGRAM/CONFIG_MGMT/10-TRACEABILITY/)

#### ATA 34 — Navigation
- **Config Item:** Dual AHRS/IRS with GNSS
- **Requirements:**
  - SYS-REQ-034-015: Navigation accuracy (RNP ≤ 0.3)
  - SYS-REQ-034-025: Redundant navigation systems
  - CERT-REQ-034-010: CS-25.1301 (Navigation equipment)
- **Verification:** See [10-TRACEABILITY](../../../../../../../00-PROGRAM/CONFIG_MGMT/10-TRACEABILITY/)

#### ATA 51-57 — Structures
- **Config Item:** BWB composite primary structure
- **Requirements:**
  - SYS-REQ-051-010: Structural design criteria
  - SYS-REQ-051-025: Pressurization (8.6 psi differential)
  - CERT-REQ-051-005: CS-25.305 (Strength and deformation)
  - CERT-REQ-051-015: CS-25.613 (Material strength)
- **Verification:** See [10-TRACEABILITY](../../../../../../../00-PROGRAM/CONFIG_MGMT/10-TRACEABILITY/)

#### ATA 71 — Power Plant
- **Config Item:** Fuel cell + electric motor propulsion
- **Requirements:**
  - SYS-REQ-071-010: Propulsion power (1.2-1.5 MW total)
  - SYS-REQ-071-020: Electric motor configuration (2×600-750 kW)
  - CERT-REQ-071-005: CS-E (Electric propulsion special condition)
- **Verification:** See [10-TRACEABILITY](../../../../../../../00-PROGRAM/CONFIG_MGMT/10-TRACEABILITY/)

## Modification Traceability

### MOD-BASE
- **Source:** Production baseline requirements
- **Requirements:** SYS-REQ-001 through SYS-REQ-099 (all systems)
- **Certification:** CS-25 Type Certificate

### MOD-M1
- **Source:** Customer enhancement requirements
- **Requirements:**
  - CUST-REQ-015: Premium cabin experience
  - CUST-REQ-027: Enhanced avionics suite
  - CUST-REQ-033: Predictive maintenance
- **Certification:** STC or Type Certificate Amendment

## Effectivity Traceability

### Serial Block BLK-2026A
- **Production Requirements:** PROD-REQ-2026-Q1
- **Quality Gates:** QA-GATE-001 through QA-GATE-005
- **First Article Inspection:** FAI-001 (MSN 001)

### Serial Block BLK-2026B
- **Production Requirements:** PROD-REQ-2026-Q3
- **Quality Gates:** QA-GATE-001 through QA-GATE-006 (enhanced)
- **Production Rate:** 3 aircraft/month

## Certification Requirements

| Certification Basis | Requirement | Status | Evidence |
|---------------------|-------------|--------|----------|
| CS-25 Amendment 27 | Complete | ✅ Compliant | Type Certificate package |
| FAR Part 25 Amend 150 | Complete | ✅ Compliant | Type Certificate package |
| ARP4754A | Guidelines | ✅ Compliant | Development assurance docs |
| ARP4761 | Safety assessment | ✅ Compliant | Safety assessment reports |
| DO-178C Level B | Software (avionics) | ✅ Compliant | Software verification docs |
| ISO 19880-8 | H₂ fuel system | ✅ Compliant | H₂ system certification |

## Compliance Matrix

All configurations must demonstrate compliance with:

1. **Performance Requirements**
   - Range: 3,200-3,800 nm ✅
   - Cruise speed: Mach 0.78-0.82 ✅
   - Service ceiling: 41,000-43,000 ft ✅

2. **Capacity Requirements**
   - Passengers: 96-110 (Q100 class) ✅
   - Cargo: 22-28 m³ ✅

3. **Safety Requirements**
   - CS-25 structural safety factors ✅
   - Redundant systems per CS-25.1309 ✅
   - H₂ safety per ISO 19880-8 ✅

4. **Environmental Requirements**
   - ICAO Annex 16 Vol II (CO₂/NOx) ✅
   - Zero direct emissions (H₂/electric) ✅

## Change Control

All requirement changes must:
1. Be approved by CCB (Configuration Control Board)
2. Update this traceability document
3. Impact assessment on affected configurations
4. Verification/validation evidence updated

## References

- **Requirements Database:** [10-TRACEABILITY](../../../../../../../00-PROGRAM/CONFIG_MGMT/10-TRACEABILITY/)
- **Verification Matrix:** [VERIFICATION_MATRIX.md](../../../../../../../00-PROGRAM/CONFIG_MGMT/10-TRACEABILITY/VERIFICATION_MATRIX.md)
- **Certification Basis:** [CERTIFICATION.md](../../../../../../../00-PROGRAM/CONFIG_MGMT/07-RELEASES/01-POLICY/CERTIFICATION.md)

## Document Control

- **Version:** 1.0.0
- **Last Updated:** 2025-03-31
- **Owner:** Configuration Management Office
- **Review Cycle:** Quarterly or with each baseline release

---

For detailed requirements, see the Configuration Management traceability database at:
[10-TRACEABILITY](../../../../../../../00-PROGRAM/CONFIG_MGMT/10-TRACEABILITY/)
