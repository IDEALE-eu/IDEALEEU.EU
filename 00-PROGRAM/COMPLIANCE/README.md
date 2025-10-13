---
area: "00-PROGRAM/COMPLIANCE"
owner: "Compliance Office"
status: "InWork"
utcs_anchor: "utcs://PROGRAM/COMPLIANCE"
tfa_flow: "QS→FWD→UE→FE→CB→QB"
confidentiality: "Internal"
---

# COMPLIANCE

Single source of truth for regulatory compliance, certifications, audits, and evidence.

## Scope
- Aviation: EASA CS-25, Part 21/145, DO-178C, DO-254, DO-160, ARP4754A, ARP4761
- Space: ECSS-E/M/Q/S (as applicable)
- Quality: AS9100/ISO 9001
- Security & Data: GDPR, ISO 27001
- Trade & Export: ITAR/EAR (if in scope)

## Structure
- `01-STANDARDS/` — controlled copies, applicability matrix  
- `02-POLICIES/` — program policies, SOPs, WI links  
- `03-CERTIFICATION/` — plans, compliance checklists, statements of compliance  
- `04-AUDITS/` — plans, reports, CAPA  
- `05-REGISTERS/` — compliance matrix, deviations, waivers, concessions  
- `06-EVIDENCE/` — objective evidence index ↔ UTCS anchors  
- `07-ICD/` — compliance-relevant interfaces  
- `08-TRAINING/` — competency, currency, records  
- `09-RISK_COMPLIANCE/` — risk register, mitigations  
- `10-EXPORT_CONTROL/` — classification, licenses, screening logs  
- `11-DATA_PROTECTION/` — DPIA, RoPA, incidents  
- `98-TOOLS/` — validators, CI checks  
- `99-TEMPLATES/` — forms and CSV/YAML schemas

## Core artifacts
- `05-REGISTERS/COMPLIANCE_MATRIX.csv`  
- `05-REGISTERS/DEVIATIONS_WAIVERS.csv`  
- `04-AUDITS/CAPA_LOG.csv`  
- `03-CERTIFICATION/PLAN_FOR_SOCC.md` (or equivalent)  
- `06-EVIDENCE/EVIDENCE_INDEX.csv` (UTCS, hash, owner, rev)

## Badging
- Micro: `Compliance-Checks-Passed`, `Evidence-Hash-Verified`  
- Macro: `CCB-Compliance-Approved`, `Audit-Closed-NoMajors`

## rewardIT hooks
VerIT = closed audit or certified milestone with evidence.  
merIT = reward units for sustained zero-majors and on-time CAPA closure.

## Related Documents

- Governance: [`../GOVERNANCE/README.md`](../GOVERNANCE/README.md)
- Security: [`../SECURITY/`](../SECURITY/)
- Quality: [`../QUALITY_QMS/`](../QUALITY_QMS/)
- Standards Mapping (legacy): [`./standards-mapping.csv`](./standards-mapping.csv)
