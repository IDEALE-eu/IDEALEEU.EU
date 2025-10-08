# IDEALEEU.EU
https://www.idealeeu.eu

> **Mission:** Design, certify, manufacture, and industrialise next-gen aircraft and spacecraft with a closed-loop digital thread from concept to fleet operations.

---

## Program Overview

This repository is the single source of truth for IDEALE EU’s engineering, certification, industrialisation, and fleet operations. It integrates **ATA-aligned configuration baselines**, **IMA-centric integration**, and **fleet learning** under rigorous configuration management.

### Program Charter

**Goals**
- Flight-ready prototypes
- Type certification / flight-worthiness (aircraft) & FRR (spacecraft)
- Serial production ramp ≥ target rate
- Cost, safety, and reliability KPIs within targets

**Standards Baseline**
- Aircraft: ARP4754A / ARP4761, DO-178C / DO-254 / DO-160, AS9100, CS-23 / CS-25  
- Spacecraft: ECSS (E/Q/M series)

**Stage Gates**
SRR → MCR → PDR → CDR → TRR → PRR → ORR/EIS (aircraft) / FRR (spacecraft)  
**V&V:** Requirements trace, HARA/SSA, FTA/FMEA, ground/flight test, conformity

---

## Repository Map

```

IDEALEEU.EU/
├─ 00-PROGRAM/          # Program governance, CM, QMS, standards, supply chain
├─ 01-FLEET/            # Operational data hub, MRO strategy, federated learning
├─ 02-AIRCRAFT/         # ATA-aligned CONFIGURATION_BASE, cross-system integration
├─ 03-SPACECRAFT/       # Spacecraft systems, AIT, mission definition
└─ 04-BUSINESS/         # Market, partnerships, finance

```

**Quick links**
- Program Governance: [`00-PROGRAM/GOVERNANCE.md`](./00-PROGRAM/GOVERNANCE.md)
- Standards Register: [`00-PROGRAM/STANDARDS/`](./00-PROGRAM/STANDARDS/)
- Configuration Management (CM): [`00-PROGRAM/CONFIG_MGMT/`](./00-PROGRAM/CONFIG_MGMT/)
- Quality QMS: [`00-PROGRAM/QUALITY_QMS/`](./00-PROGRAM/QUALITY_QMS/)
- Digital Thread: [`00-PROGRAM/DIGITAL_THREAD/`](./00-PROGRAM/DIGITAL_THREAD/)
- Supply Chain: [`00-PROGRAM/SUPPLY_CHAIN/`](./00-PROGRAM/SUPPLY_CHAIN/)
- Aircraft ATA Baselines: [`02-AIRCRAFT/CONFIGURATION_BASE/`](./02-AIRCRAFT/CONFIGURATION_BASE/)
- Cross-System Integration: [`02-AIRCRAFT/CROSS_SYSTEM_INTEGRATION/`](./02-AIRCRAFT/CROSS_SYSTEM_INTEGRATION/)
- Fleet Ops Hub: [`01-FLEET/OPERATIONAL_DATA_HUB/`](./01-FLEET/OPERATIONAL_DATA_HUB/)
- MRO Strategy: [`01-FLEET/MRO_STRATEGY/`](./01-FLEET/MRO_STRATEGY/)
- Federated Learning: [`01-FLEET/FEDERATED_LEARNING/`](./01-FLEET/FEDERATED_LEARNING/)

---

## Ways of Working

- **Baselines & Releases:** See [`00-PROGRAM/CONFIG_MGMT/04-BASELINES/`](./00-PROGRAM/CONFIG_MGMT/04-BASELINES/) and [`07-RELEASES/`](./00-PROGRAM/CONFIG_MGMT/07-RELEASES/).  
- **Changes:** All changes use ECR/ECO per [`06-CHANGES/`](./00-PROGRAM/CONFIG_MGMT/06-CHANGES/) with CCB oversight ([`05-CCB/`](./00-PROGRAM/CONFIG_MGMT/05-CCB/)).  
- **Traceability:** Requirements↔Design↔Test↔Evidence in [`10-TRACEABILITY/`](./00-PROGRAM/CONFIG_MGMT/10-TRACEABILITY/).  
- **ICDs:** Managed under [`09-INTERFACES/`](./00-PROGRAM/CONFIG_MGMT/09-INTERFACES/) with an [ICD Index](./00-PROGRAM/CONFIG_MGMT/09-INTERFACES/ICD_INDEX.md).  
- **ATA Alignment (Aircraft):** Full baseline under [`02-AIRCRAFT/CONFIGURATION_BASE/`](./02-AIRCRAFT/CONFIGURATION_BASE/). IMA in `ATA-42`, EWIS in `ATA-92`.  
- **Digital Thread:** End-to-end automation hooks in [`00-PROGRAM/DIGITAL_THREAD/`](./00-PROGRAM/DIGITAL_THREAD/).

---

## Key Interfaces

- **Aircraft ↔ Spacecraft shared tech:** materials, thermal, avionics/IMA, propulsion test assets.  
- **Fleet feedback loop:** Operational data and MRO outcomes feed design via [`01-FLEET/OPERATIONAL_DATA_HUB/`](./01-FLEET/OPERATIONAL_DATA_HUB/) and trigger changes in [`CONFIG_MGMT/06-CHANGES/`](./00-PROGRAM/CONFIG_MGMT/06-CHANGES/).

---

## Compliance & Security

- **QMS:** [`00-PROGRAM/QUALITY_QMS/`](./00-PROGRAM/QUALITY_QMS/)  
- **Standards:** [`00-PROGRAM/STANDARDS/`](./00-PROGRAM/STANDARDS/) (register, mappings, checklists)  
- **Data Classification & Access:** See [`DIGITAL_THREAD/06-DATA_MANAGEMENT/METADATA_REGISTRY/`](./00-PROGRAM/DIGITAL_THREAD/06-DATA_MANAGEMENT/METADATA_REGISTRY/) and QMS policies.  
- **ITAR/EAR & GDPR:** Handling rules in [`QUALITY_QMS/11-COMPLIANCE_LINKS/REGULATORY/`](./00-PROGRAM/QUALITY_QMS/11-COMPLIANCE_LINKS/REGULATORY/) and [`OPERATIONAL_DATA_HUB/04-DATA_SECURITY_COMPLIANCE/`](./01-FLEET/OPERATIONAL_DATA_HUB/04-DATA_SECURITY_COMPLIANCE/).

---

## Metrics (Program-level)

- Requirements coverage ≥ **99%**  
- Defect escape rate ≤ **target**  
- Weight/mass budgets within **allocated margins**  
- Schedule variance ≤ **target**  
- Unit cost ≤ **target**  
- Dispatch reliability / mission success ≥ **target**

**Dashboard specs:** [`00-PROGRAM/DIGITAL_THREAD/10-METRICS/`](./00-PROGRAM/DIGITAL_THREAD/10-METRICS/) and [`01-FLEET/.../DASHBOARD_SPECS/`](./01-FLEET/ANALYTICS_AND_AI/DASHBOARD_SPECS/)

---

## Get Started

1. Read the **Governance**: [`00-PROGRAM/GOVERNANCE.md`](./00-PROGRAM/GOVERNANCE.md)  
2. Review **CM Plan**: [`00-PROGRAM/CONFIG_MGMT/01-CM_PLAN.md`](./00-PROGRAM/CONFIG_MGMT/01-CM_PLAN.md)  
3. Use the **ICD template**: [`00-PROGRAM/CONFIG_MGMT/09-INTERFACES/ICD-XXXX.md`](./00-PROGRAM/CONFIG_MGMT/09-INTERFACES/ICD-XXXX.md)  
4. File changes via **ECR**: [`06-CHANGES/05-ECR/`](./00-PROGRAM/CONFIG_MGMT/06-CHANGES/05-ECR/)

---

**Program site:** https://www.idealeeu.eu  
**Ownership:** Program Management & Configuration Management (see [`00-PROGRAM/CONFIG_MGMT/05-CCB/`](./00-PROGRAM/CONFIG_MGMT/05-CCB/))
```

