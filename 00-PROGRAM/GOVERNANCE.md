# Program Governance · Supply Chain Integration

## Overview
Defines gate readiness, roles, and evidence for Supply Chain within IDEALE EU. Aligns with CONFIG_MGMT, DIGITAL_THREAD, QUALITY_QMS, and SUPPLY_CHAIN.

## Stage Gates & Supply Chain Deliverables

| Gate | Full Name | Key Supply Chain Inputs & Approvals |
|---|---|---|
| **SRR** | System Requirements Review | Approved **Category Strategy** (`SUPPLY_CHAIN/01-STRATEGY/`); initial **Make/Buy** (`01-STRATEGY/MAKE_BUY.md`); preliminary **AML/AVL** (`13-DATA_MODELS/`). |
| **MCR** | Mission Concept Review | **Localization & Resilience Plan** (`01-STRATEGY/LOCALIZATION_RESILIENCE.md`); high-level **Single-Source Risk Register** (`08-RISK/SINGLE_SOURCE_LIST.csv`). |
| **PDR** | Preliminary Design Review | **AML finalized**; **RFI/RFQ completed** for long-lead items (`03-SUPPLIER_LIFECYCLE/SOURCING/`); **Tooling strategy** approved (`12-TOOLING_PROPERTY/`). |
| **CDR** | Critical Design Review | **AVL locked** (`13-DATA_MODELS/AVL_APPROVED_VENDOR_LIST.csv`); **PPAP/FAI plans** in place (`06-SUPPLIER_QUALITY/`); **Compliance screening** complete (ITAR, REACH, Conflict Minerals) (`07-COMPLIANCE/`). |
| **TRR** | Test Readiness Review | **SCARs closed** for test-critical suppliers (`06-SUPPLIER_QUALITY/SCAR/`); **Calibration & tooling** verified (`12-TOOLING_PROPERTY/`); **EEE radiation data** ready (`17-SPACECRAFT_PARTS/`). |
| **PRR** | Production Readiness Review | **Supplier scorecards** ≥ target (`14-METRICS/`); **VMI/consignment** active (`04-PROCUREMENT/VMI_CONSIGNMENT/`); **Business continuity** validated (`08-RISK/BUSINESS_CONTINUITY.md`). |
| **ORR/EIS** | Operational Readiness / Entry Into Service (Aircraft) | **Spare parts AVL** confirmed; **Logistics & customs** readiness (`10-LOGISTICS/`); **Sustainability/ESG** verified (`02-POLICIES/SUSTAINABILITY_ESG.md`). |
| **FRR** | Flight Readiness Review (Spacecraft) | **EEE lot screening reports** (`17-SPACECRAFT_PARTS/EEE_COMPONENTS/LOT_SCREENING.md`); **Final SCAR closure**; **Export licenses** confirmed (`07-COMPLIANCE/EXPORT_CLASSIFICATION/`). |

## V&V — Supply Chain Contributions

| Activity | Supply Chain Role |
|---|---|
| **RTM** | Link supplier deliverables to system reqs via `SUPPLY_CHAIN/15-DIGITAL_THREAD_HOOKS/`. |
| **HARA/SSA** | Provide PPM and SCAR trends (`14-METRICS/PPM_DEFECTS.csv`), supplier failure history. |
| **FTA/FMEA** | Feed process risks and mitigations (`08-RISK/`). |
| **Flight/Ground Tests** | Source test articles from AVL; track FAI status (`06-SUPPLIER_QUALITY/`). |
| **Conformity** | Evidence for REACH/ROHS (`07-COMPLIANCE/`), AS9100 supplier audits (`06-SUPPLIER_QUALITY/AUDITS/`). |

## Roles
- **Supply Chain Program Manager** — gate readiness sign-off.
- **Supplier Quality Engineer (SQE)** — quality deliverables at PDR/CDR/TRR/FRR.
- **Compliance Officer** — regulatory checks at CDR/FRR.
- **Logistics Lead** — ORR/EIS operational readiness.

## Gate Readiness Checklist (template)
```md
Gate: <SRR|MCR|PDR|CDR|TRR|PRR|ORR/EIS|FRR>
Date: YYYY-MM-DD

- [ ] Required artifacts present in SUPPLY_CHAIN tree
- [ ] Cross-links to CONFIG_MGMT baseline (ID: <baseline_id>)
- [ ] Risks updated in 08-RISK/
- [ ] Metrics meet threshold (14-METRICS/)
- [ ] Approvals recorded (signatures below)

Approvals: SC PM | SQE | Compliance | Logistics
````

## Evidence Manifest (YAML)

```yaml
gate: CDR
date: 2025-11-15
baseline_ref: CONFIG_MGMT/04-BASELINES/CDR/MANIFEST.json
artifacts:
  - path: SUPPLY_CHAIN/13-DATA_MODELS/AVL_APPROVED_VENDOR_LIST.csv
    type: dataset
    hash: "<sha256>"
  - path: SUPPLY_CHAIN/06-SUPPLIER_QUALITY/PPAP/
    type: folder
  - path: SUPPLY_CHAIN/07-COMPLIANCE/REACH_ROHS/
    type: folder
owners:
  sc_pm: "<name>"
  sqe: "<name>"
  compliance: "<name>"
signoff: APPROVED
```

## Documentation Control

* Version tag format: `vX.Y_YYYY-MM-DD`.
* Store in Program Data Vault (`SUPPLY_CHAIN/19-LINKS/`).
* Expose trace via `SUPPLY_CHAIN/15-DIGITAL_THREAD_HOOKS/API_BINDINGS.md`.

```
```
