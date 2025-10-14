---
doc_type: "design_spec"
title: "Air-Conditioning Spec"
artifact_id: "01-air-conditioning-spec"
item_id: "ATA-21-10-01"
version: "v1.0"
date: "2025-10-14"
status: "Draft"
owner: "AirConditioningTeam"
effectivity: "0001-9999"
utcs_anchor: "utcs://AIRCRAFT/AMPEL360-AIR-T/ATA-21-10-01/01-air-conditioning-spec/design_spec_v1.0"
confidentiality: "Internal"
related_icd:
  - "/02-AIRCRAFT/DOMAIN_INTEGRATION/PRODUCTS/AMPEL360-AIR-T/MODELS/BWB-H2-Hy-E/VERSION/Q100/04-ICD_LINKS/ATA21_IF-CABIN_ENV.md"
  - "/02-AIRCRAFT/DOMAIN_INTEGRATION/PRODUCTS/AMPEL360-AIR-T/MODELS/BWB-H2-Hy-E/VERSION/Q100/04-ICD_LINKS/ATA24_IF-ELEC_POWER.md"
  - "/02-AIRCRAFT/DOMAIN_INTEGRATION/PRODUCTS/AMPEL360-AIR-T/MODELS/BWB-H2-Hy-E/VERSION/Q100/04-ICD_LINKS/ATA31_IF-AVIONICS_BUS.md"
related_regs:
  - "CS-25.831 (Ventilation)"
  - "CS-25.832 (Cabin ozone concentration)"
  - "CS-25.841 (Pressurized cabins)"
  - "DO-160G Section 4-8"
  - "DO-178C Level C"
---

# 1. Purpose and scope
Define functional, performance, interfaces, and verification for item **ATA-21-10-01** air-conditioning spec. Applies to effectivity **0001–9999**. This specification covers the electric-driven vapor-cycle air conditioning system for the AMPEL360-AIR-T BWB aircraft, providing cabin temperature control, ventilation, and humidity management for up to **120** passengers and crew.

# 2. References
- Program standards: `../README.md`, MANIFEST, CONFIG.
- Regulations: CS-25.831/832/841, DO-160G, DO-178C Level C, ARP4754A Rev A, ARP4761A.
- ICDs: see `related_icd`.
- Industry standards: SAE ARP217E (Aircraft Cargo Compartment Halon Replacement), MIL-STD-810H.
- Company standards: AMPEL360-STD-001 (Electric System Architecture), AMPEL360-STD-021 (ECS Design).

# 3. Definitions and acronyms
- **PACK**: Vapor-cycle air conditioning pack (electric compressor-based)
- **ECS**: Environmental Control System
- **RAM**: Ram Air Modulating valve
- **COP**: Coefficient of Performance
- **TCAS**: Temperature Control and Sensing
- **HEPA**: High-Efficiency Particulate Air filter
- **FADEC**: Full Authority Digital Engine Control (interface point)
- **BWB**: Blended Wing Body
- **UTCS**: Universal Traceability and Configuration System

# 4. Functional requirements
## 4.1 Temperature control
- **FR-TC-01**: Maintain cabin temperature 18–27°C (adjustable by crew).
- **FR-TC-02**: Temperature uniformity ±3°C across cabin zones.
- **FR-TC-03**: Response time to commanded temperature change ≤10 min at cruise.

## 4.2 Ventilation and air quality
- **FR-VQ-01**: Provide minimum 0.55 lb/min fresh air per occupant (CS-25.831).
- **FR-VQ-02**: HEPA filtration efficiency ≥99.97% at 0.3 μm particles.
- **FR-VQ-03**: Ozone concentration ≤0.1 ppm at any altitude (CS-25.832).
- **FR-VQ-04**: CO₂ concentration ≤5000 ppm under normal operations.

## 4.3 Humidity management
- **FR-HM-01**: Maintain relative humidity 20–60% at cruise altitude.
- **FR-HM-02**: Condensate removal rate ≥5 kg/hr.

## 4.4 System availability
- **FR-AV-01**: System MTBF ≥5000 flight hours.
- **FR-AV-02**: No single point of failure shall cause total loss of cabin conditioning.

# 5. Performance requirements
## 5.1 Cooling capacity
- **PR-CC-01**: Total cooling capacity ≥150 kW at ISA+10°C ground conditions.
- **PR-CC-02**: Cruise cooling capacity ≥80 kW at FL410.
- **PR-CC-03**: COP ≥2.5 at cruise conditions.

## 5.2 Power consumption
- **PR-PC-01**: Maximum electrical power draw ≤60 kW per PACK at full load.
- **PR-PC-02**: Standby power ≤2 kW per PACK.

## 5.3 Weight and volume
- **PR-WV-01**: Total system mass (2 PACKs + distribution) ≤450 kg.
- **PR-WV-02**: PACK envelope fit within allocated BWB underfloor bay (2.5m × 1.2m × 0.8m).

# 6. Interface requirements
## 6.1 Electrical interfaces (ATA-24)
- **IF-EL-01**: 540 VDC primary power bus (ICD: ATA24_IF-ELEC_POWER.md).
- **IF-EL-02**: 28 VDC control power.
- **IF-EL-03**: ARINC 664 Part 7 (AFDX) data bus for control and monitoring.

## 6.2 Cabin interface (ATA-25)
- **IF-CB-01**: Ducting interface to cabin distribution system (ICD: ATA21_IF-CABIN_ENV.md).
- **IF-CB-02**: Return air plenum connection.

## 6.3 Avionics interface (ATA-31)
- **IF-AV-01**: AFDX connection to cabin management system (ICD: ATA31_IF-AVIONICS_BUS.md).
- **IF-AV-02**: Discrete signals for pack status (ON/OFF/FAULT).

## 6.4 External air interface
- **IF-EA-01**: Ram air inlet sizing and pressure drop budget.
- **IF-EA-02**: Exhaust air discharge to ambient.

# 7. Environmental and operational conditions
## 7.1 Temperature extremes
- Operating: -55°C to +50°C ambient.
- Storage: -65°C to +70°C.

## 7.2 Altitude
- Operational ceiling: 45,000 ft.
- Pressurized cabin: 8,000 ft equivalent at FL410.

## 7.3 Vibration and shock
- Per DO-160G Section 8 (Category S, Curve 5).

## 7.4 EMI/EMC
- Per DO-160G Section 4–8, Category M.

# 8. Design constraints
- **DC-01**: Use only non-ozone-depleting refrigerants (e.g., R-1234yf).
- **DC-02**: Minimize acoustic noise: ≤65 dBA in cabin during cruise.
- **DC-03**: Redundancy: dual PACKs, each capable of 60% total load.
- **DC-04**: Maintenance accessibility: major components replaceable in ≤4 man-hours.

# 9. Verification and validation
## 9.1 Analysis
- Thermal load analysis (cruise, climb, descent, ground ops).
- Power consumption modeling and trade studies.
- Weight and CG impact assessment.

## 9.2 Testing
- Component-level environmental testing per DO-160G.
- Integrated system test in iron bird.
- Flight test validation on prototype aircraft.

## 9.3 Simulation
- CFD analysis of airflow distribution.
- Transient thermal modeling for rapid descent scenarios.

## 9.4 Compliance demonstration
- FAA/EASA type certification: CS-25.831/832/841 compliance reports.
- DO-178C Level C software verification for control algorithms.

# 10. Safety and reliability
## 10.1 Failure modes
- FMEA conducted per ARP4761A.
- Critical failure modes identified: compressor seizure, refrigerant leak, electrical short.

## 10.2 Fault detection and isolation
- Built-in test (BIT) for self-diagnostics.
- Fault codes reported via AFDX to cockpit display.

## 10.3 Fire protection
- Over-temperature sensors and automatic shut-off.
- Fire-resistant materials per CS-25.853.

# 11. Maintenance and support
## 11.1 Scheduled maintenance
- Inspection interval: 1000 flight hours or 12 months.
- Major overhaul: 10,000 flight hours.

## 11.2 Line replaceable units (LRUs)
- Compressor module
- Heat exchangers
- Control unit
- Sensors and valves

## 11.3 Ground support equipment
- Refrigerant service cart (R-1234yf).
- Electrical load bank for ground testing.

# 12. Configuration and traceability
- **UTCS Anchor**: `utcs://AIRCRAFT/AMPEL360-AIR-T/ATA-21-10-01/01-air-conditioning-spec/design_spec_v1.0`
- **Version control**: All changes tracked in Git; major revisions require CCB approval.
- **Baseline**: This document establishes the Preliminary Design Review (PDR) baseline.

# 13. Approval and authorization
| Role | Name | Signature | Date |
|------|------|-----------|------|
| System Engineer | TBD | | |
| Chief Engineer | TBD | | |
| Quality Manager | TBD | | |
| Program Manager | TBD | | |

# 14. Revision history
| Version | Date | Author | Description |
|---------|------|--------|-------------|
| v1.0 | 2025-10-14 | AirConditioningTeam | Initial draft for PDR |

---

**Document Owner**: AirConditioningTeam  
**Status**: Draft  
**Effectivity**: 0001–9999  
**Next Review**: 2025-11-14
