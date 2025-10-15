<!-- UTCS: utcs://AMPEL360-AIR-T/BWB-H2-Hy-E/Q100_STD01 -->
<!-- TFA-DOMAINS: AAA, CQH, EEE, PPP, LIB, IIS -->

# UTCS Index - Q100_STD01 Configuration Flow

This document provides a visual mapping of the **QS → FWD → UE → FE → CB → QB** workflow, showing how each phase intersects with TFA domains and physical file locations.

## Workflow Phase × TFA Domain Matrix

| Phase | AAA (Airframes) | CQH (Cryogenics/H2) | EEE (Electrical) | PPP (Propulsion) | LIB (Logistics) | IIS (Information) |
|-------|----------------|-------------------|-----------------|-----------------|----------------|------------------|
| **QS** | Superposition states | H₂ tank configs | Power topologies | Propulsion variants | BOM alternatives | Data schemas |
| **FWD** | Aero predictions | Boil-off models | Energy forecasts | Thrust profiles | Supply scenarios | Analytics models |
| **UE** | Mass/geometry | Tank elements | Battery cells | Motor units | Part catalog | Data nodes |
| **FE** | Fleet aero feedback | H₂ consumption data | Power usage patterns | Engine telemetry | Supplier performance | Fleet analytics |
| **CB** | Baseline geometry | Crystallized tank design | Final power distribution | Production propulsion | Approved BOM | Operational schema |
| **QB** | Structural optimization | Cryogenic efficiency | Energy routing | Thrust optimization | Logistics optimization | Data flow optimization |

## Physical Path Mappings

### QS Phase
- **Location**: `00-CONFIG/QS_STATE.yaml`
- **Domains**: All (AAA, CQH, EEE, PPP, LIB, IIS)

### FWD Phase
- **Location**: `performance/mission_profile.yaml`
- **Domains**: AAA, CQH, PPP
- **Artifacts**: Energy models, range predictions, thermal analysis

### UE Phase
- **Locations**:
  - `geometry/` (AAA)
  - `propulsion/` (CQH, PPP)
  - `weights/` (AAA, EEE)
- **Domains**: AAA, CQH, EEE, PPP

### FE Phase
- **Location**: `../../../01-FLEET/FEDERATED_LEARNING/JOBS/Q100_STD01.job.yaml`
- **Domains**: All (fleet feedback integration)

### CB Phase
- **Location**: `../../../00-PROGRAM/CONFIG_MGMT/04-BASELINES/Q100_STD01_v2.3.yaml`
- **Domains**: All (crystallized baseline)

### QB Phase
- **Location**: `tools/qb_optimize_mass.py`, `tools/qb_optimize_routing.py`
- **Domains**: AAA, EEE, PPP (quantum optimization)

## UTCS Thread References

Full traceability threads available at: [`03-TRACEABILITY/UTCS_THREADS.csv`](./03-TRACEABILITY/UTCS_THREADS.csv)

## Domain Integration Paths

| TFA Domain | Integration Path |
|-----------|-----------------|
| AAA | `02-AIRCRAFT/DOMAIN_INTEGRATION/PRODUCTS/AMPEL360-AIR-T/MODELS/BWB-H2-Hy-E/VERSION/Q100/AAA/` |
| CQH | `02-AIRCRAFT/DOMAIN_INTEGRATION/PRODUCTS/AMPEL360-AIR-T/MODELS/BWB-H2-Hy-E/VERSION/Q100/CQH/` |
| EEE | `02-AIRCRAFT/DOMAIN_INTEGRATION/PRODUCTS/AMPEL360-AIR-T/MODELS/BWB-H2-Hy-E/VERSION/Q100/EEE/` |
| PPP | `02-AIRCRAFT/DOMAIN_INTEGRATION/PRODUCTS/AMPEL360-AIR-T/MODELS/BWB-H2-Hy-E/VERSION/Q100/PPP/` |
| LIB | `02-AIRCRAFT/DOMAIN_INTEGRATION/PRODUCTS/AMPEL360-AIR-T/MODELS/BWB-H2-Hy-E/VERSION/Q100/LIB/` |
| IIS | `02-AIRCRAFT/DOMAIN_INTEGRATION/PRODUCTS/AMPEL360-AIR-T/MODELS/BWB-H2-Hy-E/VERSION/Q100/IIS/` |

---

**Maintained by**: Configuration Management Team  
**Last Updated**: 2025-10-15  
**UTCS Version**: v2.3
