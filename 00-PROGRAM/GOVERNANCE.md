# Program Governance · Supply Chain Integration

## Overview
This document defines the governance structure for the IDEALE EU aerospace program, including cross-functional accountability for engineering, quality, compliance, and **supply chain**.

## Stage Gates & Supply Chain Deliverables

The program follows a rigorous stage-gate process. At each gate, **Supply Chain must certify readiness** based on defined criteria:

| Gate | Full Name | Key Supply Chain Inputs & Approvals |
|------|----------|-------------------------------------|
| **SRR** | System Requirements Review | • Approved **Category Strategy** ([SUPPLY_CHAIN/01-STRATEGY/](../SUPPLY_CHAIN/01-STRATEGY/)) <br>• Initial **Make/Buy Decision** ([SUPPLY_CHAIN/01-STRATEGY/MAKE_BUY.md](../SUPPLY_CHAIN/01-STRATEGY/MAKE_BUY.md)) <br>• Preliminary **AML/AVL** ([SUPPLY_CHAIN/13-DATA_MODELS/](../SUPPLY_CHAIN/13-DATA_MODELS/)) |
| **MCR** | Mission Concept Review | • **Localization & Resilience Plan** ([SUPPLY_CHAIN/01-STRATEGY/LOCALIZATION_RESILIENCE.md](../SUPPLY_CHAIN/01-STRATEGY/LOCALIZATION_RESILIENCE.md)) <br>• High-level **Single-Source Risk Register** ([SUPPLY_CHAIN/08-RISK/SINGLE_SOURCE_LIST.csv](../SUPPLY_CHAIN/08-RISK/SINGLE_SOURCE_LIST.csv)) |
| **PDR** | Preliminary Design Review | • **Approved Manufacturer List (AML)** finalized ([SUPPLY_CHAIN/13-DATA_MODELS/AML_APPROVED_MFR_LIST.csv](../SUPPLY_CHAIN/13-DATA_MODELS/AML_APPROVED_MFR_LIST.csv)) <br>• **RFI/RFQ completed** for long-lead items ([SUPPLY_CHAIN/03-SUPPLIER_LIFECYCLE/SOURCING/](../SUPPLY_CHAIN/03-SUPPLIER_LIFECYCLE/SOURCING/)) <br>• **Tooling strategy** approved ([SUPPLY_CHAIN/12-TOOLING_PROPERTY/](../SUPPLY_CHAIN/12-TOOLING_PROPERTY/)) |
| **CDR** | Critical Design Review | • **AVL locked** ([SUPPLY_CHAIN/13-DATA_MODELS/AVL_APPROVED_VENDOR_LIST.csv](../SUPPLY_CHAIN/13-DATA_MODELS/AVL_APPROVED_VENDOR_LIST.csv)) <br>• **PPAP/FAI plans** in place ([SUPPLY_CHAIN/06-SUPPLIER_QUALITY/](../SUPPLY_CHAIN/06-SUPPLIER_QUALITY/)) <br>• **Compliance screening** complete ITAR/REACH/Conflict Minerals ([SUPPLY_CHAIN/07-COMPLIANCE/](../SUPPLY_CHAIN/07-COMPLIANCE/)) |
| **TRR** | Test Readiness Review | • **SCARs closed** for test-critical suppliers ([SUPPLY_CHAIN/06-SUPPLIER_QUALITY/SCAR/](../SUPPLY_CHAIN/06-SUPPLIER_QUALITY/SCAR/)) <br>• **Calibration & tooling status** verified ([SUPPLY_CHAIN/12-TOOLING_PROPERTY/](../SUPPLY_CHAIN/12-TOOLING_PROPERTY/)) <br>• **EEE parts radiation data** available ([SUPPLY_CHAIN/17-SPACECRAFT_PARTS/EEE_COMPONENTS/RADIATION_DATA/](../SUPPLY_CHAIN/17-SPACECRAFT_PARTS/EEE_COMPONENTS/RADIATION_DATA/)) |
| **PRR** | Production Readiness Review | • **Supplier scorecards** ≥ target threshold ([SUPPLY_CHAIN/14-METRICS/](../SUPPLY_CHAIN/14-METRICS/)) <br>• **VMI/consignment agreements** active ([SUPPLY_CHAIN/04-PROCUREMENT/VMI_CONSIGNMENT/](../SUPPLY_CHAIN/04-PROCUREMENT/VMI_CONSIGNMENT/)) <br>• **Business continuity plans** validated ([SUPPLY_CHAIN/08-RISK/BUSINESS_CONTINUITY.md](../SUPPLY_CHAIN/08-RISK/BUSINESS_CONTINUITY.md)) |
| **ORR/EIS** | Operational Readiness Review / Entry Into Service (Aircraft) | • **Spare parts AVL** confirmed ([SUPPLY_CHAIN/13-DATA_MODELS/AVL_APPROVED_VENDOR_LIST.csv](../SUPPLY_CHAIN/13-DATA_MODELS/AVL_APPROVED_VENDOR_LIST.csv)) <br>• **Logistics & customs** readiness ([SUPPLY_CHAIN/10-LOGISTICS/](../SUPPLY_CHAIN/10-LOGISTICS/)) <br>• **Sustainability & ESG compliance** verified ([SUPPLY_CHAIN/02-POLICIES/SUSTAINABILITY_ESG.md](../SUPPLY_CHAIN/02-POLICIES/SUSTAINABILITY_ESG.md)) |
| **FRR** | Flight Readiness Review (Spacecraft) | • **Lot screening reports** for EEE parts ([SUPPLY_CHAIN/17-SPACECRAFT_PARTS/EEE_COMPONENTS/LOT_SCREENING.md](../SUPPLY_CHAIN/17-SPACECRAFT_PARTS/EEE_COMPONENTS/LOT_SCREENING.md)) <br>• **Final SCAR closure** ([SUPPLY_CHAIN/06-SUPPLIER_QUALITY/SCAR/](../SUPPLY_CHAIN/06-SUPPLIER_QUALITY/SCAR/)) <br>• **Export licenses** confirmed ([SUPPLY_CHAIN/07-COMPLIANCE/EXPORT_CLASSIFICATION/](../SUPPLY_CHAIN/07-COMPLIANCE/EXPORT_CLASSIFICATION/)) |

## Verification & Validation – Supply Chain Contributions

| Activity | Supply Chain Role |
|--------|------------------|
| **Requirements Traceability Matrix (RTM)** | Link supplier deliverables to system requirements via **Digital Thread** bindings ([SUPPLY_CHAIN/15-DIGITAL_THREAD_HOOKS/](../SUPPLY_CHAIN/15-DIGITAL_THREAD_HOOKS/)). |
| **HARA / SSA** | Provide supplier failure history, PPM data ([SUPPLY_CHAIN/14-METRICS/PPM_DEFECTS.csv](../SUPPLY_CHAIN/14-METRICS/PPM_DEFECTS.csv)), and SCAR trends ([SUPPLY_CHAIN/06-SUPPLIER_QUALITY/SCAR/](../SUPPLY_CHAIN/06-SUPPLIER_QUALITY/SCAR/)). |
| **FTA / FMEA** | Input supplier process risks, single-point failures, and mitigation plans ([SUPPLY_CHAIN/08-RISK/](../SUPPLY_CHAIN/08-RISK/)). |
| **Flight & Ground Testing** | Ensure test articles sourced from **AVL-approved suppliers** ([SUPPLY_CHAIN/13-DATA_MODELS/AVL_APPROVED_VENDOR_LIST.csv](../SUPPLY_CHAIN/13-DATA_MODELS/AVL_APPROVED_VENDOR_LIST.csv)); track FAI status ([SUPPLY_CHAIN/06-SUPPLIER_QUALITY/](../SUPPLY_CHAIN/06-SUPPLIER_QUALITY/)). |
| **Conformity Assessments** | Demonstrate compliance with program **standards** ([STANDARDS/](../STANDARDS/)); REACH/ROHS evidence ([SUPPLY_CHAIN/07-COMPLIANCE/REACH_ROHS/](../SUPPLY_CHAIN/07-COMPLIANCE/REACH_ROHS/)); AS9100 QMS evidence ([SUPPLY_CHAIN/06-SUPPLIER_QUALITY/AUDITS/](../SUPPLY_CHAIN/06-SUPPLIER_QUALITY/AUDITS/)). |

## Governance Roles

- **Supply Chain Program Manager**: gate readiness sign-off.  
- **Supplier Quality Engineer (SQE)**: validates quality deliverables at PDR, CDR, TRR, FRR.  
- **Compliance Officer**: confirms regulatory adherence at CDR and FRR.  
- **Logistics Lead**: certifies operational support readiness at ORR/EIS.

## Documentation Control

All referenced supply chain artifacts must be:
- Version-controlled, e.g., `v1.2_2025-10-09`.
- Stored in the **Program Data Vault** ([SUPPLY_CHAIN/19-LINKS/](../SUPPLY_CHAIN/19-LINKS/)).
- Traceable via **Digital Thread API** ([SUPPLY_CHAIN/15-DIGITAL_THREAD_HOOKS/API_BINDINGS.md](../SUPPLY_CHAIN/15-DIGITAL_THREAD_HOOKS/API_BINDINGS.md)).
```

```
