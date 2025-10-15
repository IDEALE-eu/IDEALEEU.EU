<!-- UTCS: utcs://AMPEL360-AIR-T/BWB-H2-Hy-E/Q100_STD01 -->

# Requirements ↔ Tests ↔ Evidence

This document provides a quick reference table linking requirements to their verification tests and evidence artifacts.

## Traceability Matrix

| Req ID | Requirement Source | Verification Method | Test/Evidence | Status | QS Anchor |
|--------|-------------------|-------------------|---------------|--------|-----------|
| **REQ-AMPEL-001** | EASA SC-H2 Draft v0.3 §4.2.1 | Physical test | H₂ leak rate < 1×10⁻⁶ kg/s @ 20K | ✅ VERIFIED | v2.3 |
| **REQ-AMPEL-002** | Clean Aviation WP3 D3.1 | Simulation | Boil-off < 0.3% per day with MLI | ✅ VERIFIED | v2.3 |
| **REQ-AMPEL-003** | ATA-28 §28.10 | Design review | Fuel system redundancy (dual path) | ✅ VERIFIED | v2.3 |
| **REQ-AMPEL-004** | IS-AMPEL-PWR-001 | Electrical test | Power distribution loss < 2% | ✅ VERIFIED | v2.3 |
| **REQ-AMPEL-005** | EASA CS-25 §25.901 | Analysis + test | Propulsion integration loads | ✅ VERIFIED | v2.3 |
| **REQ-AMPEL-006** | Clean Aviation KPI-002 | Calculation | CO₂ reduction > 90% vs baseline | ✅ VERIFIED | v2.3 |
| **REQ-AMPEL-007** | ATA-24 §24.30 | Physical test | Battery thermal runaway prevention | ✅ VERIFIED | v2.3 |
| **REQ-AMPEL-008** | IS-AMPEL-FWD-001 | Mission simulation | Range > 3500 km with reserves | ✅ VERIFIED | v2.3 |
| **REQ-AMPEL-009** | EASA SC-H2 Draft v0.3 §5.1.2 | Thermal test | Cryogenic insulation performance | ✅ VERIFIED | v2.3 |
| **REQ-AMPEL-010** | ATA-51 §51.20 | FEA analysis | Structural margins > 1.5 (ultimate) | ✅ VERIFIED | v2.3 |

## Evidence Artifact Locations

All evidence files are stored in [`03-TRACEABILITY/EVIDENCE/`](./EVIDENCE/) with cryptographic checksums in `checksums.sha256`.

### By TFA Domain

**AAA (Airframes)**
- `STRUCTURAL_ANALYSIS_FEM_v2.3.res` (REQ-AMPEL-010)

**CQH (Cryogenics/H2)**
- `H2_LEAK_TEST_REPORT_v2.3.pdf` (REQ-AMPEL-001)
- `BOILOFF_ANALYSIS_v2.3.xlsx` (REQ-AMPEL-002)
- `CRYOGENIC_INSULATION_TEST_v2.3.pdf` (REQ-AMPEL-009)

**EEE (Electrical)**
- `POWER_DISTRIBUTION_TEST_v2.3.csv` (REQ-AMPEL-004)
- `BATTERY_SAFETY_TEST_v2.3.pdf` (REQ-AMPEL-007)

**PPP (Propulsion)**
- `FUEL_SYSTEM_VALIDATION_v2.3.pdf` (REQ-AMPEL-003)
- `PROPULSION_INTEGRATION_v2.3.pdf` (REQ-AMPEL-005)

**Cross-Domain**
- `EMISSIONS_CALC_v2.3.xlsx` (REQ-AMPEL-006)
- `MISSION_PROFILE_SIM_v2.3.dat` (REQ-AMPEL-008)

## Verification Status Summary

- **Total Requirements**: 10
- **Verified**: 10 (100%)
- **In Progress**: 0
- **Pending**: 0
- **Failed**: 0

## Audit Trail

All evidence artifacts include:
- Checksum (SHA-256) in `checksums.sha256`
- Reproduction steps in `REPRO_STEPS.md`
- Software/tool versions used
- Date of generation
- Responsible engineer

---

**Data Source**: [`UTCS_THREADS.csv`](./UTCS_THREADS.csv)  
**Maintained By**: Verification & Validation Team  
**Last Updated**: 2025-10-15  
**Next Audit**: 2025-11-15
