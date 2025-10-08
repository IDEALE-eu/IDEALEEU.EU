# ROADMAP.md

**Program Roadmap — IDEALE EU**

- **Owner:** Program Manager  
- **Last Updated:** 2025-10-08  
- **Governance:** see **[GOVERNANCE.md](./GOVERNANCE.md)**  
- **Change Control:** via **[CONFIG_MGMT/06-CHANGES/](./CONFIG_MGMT/06-CHANGES/)**

---

## Phases

| Phase | Scope | Planned Start | Planned End | Primary Gates | Key Links |
|---|---|---|---|---|---|
| 1. Concept & Requirements | Mission definition, stakeholder capture, system reqs | YYYY-MM-DD | YYYY-MM-DD | SRR | **[STANDARDS/](./STANDARDS/)** · **[DIGITAL_THREAD/04-MBSE/](./DIGITAL_THREAD/04-MBSE/)** |
| 2. Preliminary Design | Architecture, subsystem design, trades | YYYY-MM-DD | YYYY-MM-DD | MCR, PDR | **[STANDARDS/05-MAPPINGS/CHECKLISTS/PDR_CHECKLIST.md](./STANDARDS/05-MAPPINGS/CHECKLISTS/PDR_CHECKLIST.md)** |
| 3. Detailed Design | Design freeze, mfg & test planning | YYYY-MM-DD | YYYY-MM-DD | CDR | **[CONFIG_MGMT/04-BASELINES/CDR/](./CONFIG_MGMT/04-BASELINES/CDR/)** |
| 4. Manufacturing & Integration | Ramp-up, AIT | YYYY-MM-DD | YYYY-MM-DD | TRR, PRR | **[INDUSTRIALISATION/](./INDUSTRIALISATION/)** · **[QUALITY_QMS/08-CALIBRATION_METROLOGY/](./QUALITY_QMS/08-CALIBRATION_METROLOGY/)** |
| 5. Testing & Certification | Ground, flight, certification | YYYY-MM-DD | YYYY-MM-DD | ORR/EIS or FRR | **[QUALITY_QMS/](./QUALITY_QMS/)** · **[STANDARDS/02-AIRCRAFT/](./STANDARDS/02-AIRCRAFT/)** · **[STANDARDS/03-SPACECRAFT/](./STANDARDS/03-SPACECRAFT/)** |
| 6. Operations & Support | Serial production, fleet ops, MRO | YYYY-MM-DD | YYYY-MM-DD | — | **[SUPPLY_CHAIN/](./SUPPLY_CHAIN/)** · **[DIGITAL_THREAD/05-DIGITAL_TWIN/](./DIGITAL_THREAD/05-DIGITAL_TWIN/)** |

---

## Stage-Gate Milestones

| ID | Milestone | Entry Criteria | Exit Evidence | Owners |
|---|---|---|---|---|
| G1 | **SRR** | ConOps, top-level reqs (**[DIGITAL_THREAD/05-TRACEABILITY/MATRICES/REQ_ITEM.csv](./DIGITAL_THREAD/05-TRACEABILITY/MATRICES/REQ_ITEM.csv)**) | SRR baseline (**[CONFIG_MGMT/04-BASELINES/SRR/](./CONFIG_MGMT/04-BASELINES/SRR/)**) | PM, SE, QMR |
| G2 | **MCR** | Trades, concept selection | MCR record (**[GOVERNANCE.md](./GOVERNANCE.md)**) | PM, TRB |
| G3 | **PDR** | Allocations, ICD drafts (**[DIGITAL_THREAD/04-MBSE/INTERFACE_DEFINITIONS/](./DIGITAL_THREAD/04-MBSE/INTERFACE_DEFINITIONS/)**) | PDR baseline (**[CONFIG_MGMT/04-BASELINES/PDR/](./CONFIG_MGMT/04-BASELINES/PDR/)**) | SE, CCB |
| G4 | **CDR** | Detailed design, test plans, twin def (**[DIGITAL_THREAD/05-DIGITAL_TWIN/TWIN_DEFINITION.md](./DIGITAL_THREAD/05-DIGITAL_TWIN/TWIN_DEFINITION.md)**) | CDR **MANIFEST.json** (**[CONFIG_MGMT/04-BASELINES/CDR/](./CONFIG_MGMT/04-BASELINES/CDR/)**) | SE, CM Lead |
| G5 | **TRR** | Rigs ready, procedures, config lock | TRR report, evidence (**[DIGITAL_THREAD/08-EVIDENCE/TEST/](./DIGITAL_THREAD/08-EVIDENCE/TEST/)**) | TRB, QMR |
| G6 | **PRR** | MBOM/routings, PPAP/FAI (**[INDUSTRIALISATION/04-MBOM_ROUTINGS/](./INDUSTRIALISATION/04-MBOM_ROUTINGS/)** · **[QUALITY_QMS/02-PROCEDURES/PRO-009_APQP_PPAP.md](./QUALITY_QMS/02-PROCEDURES/PRO-009_APQP_PPAP.md)**) | PRR package (**[INDUSTRIALISATION/11-PRR/EVIDENCE/](./INDUSTRIALISATION/11-PRR/EVIDENCE/)**) | Ops, SQE |
| G7 | **ORR/EIS** (Aircraft) | Compliance bundle, ops readiness | Release notes & compliance (**[CONFIG_MGMT/07-RELEASES/AIRCRAFT/](./CONFIG_MGMT/07-RELEASES/AIRCRAFT/)**) | PM, Certification |
| G8 | **FRR** (Spacecraft) | Launch readiness, GSE, hazard controls | Flight config freeze (**[CONFIG_MGMT/07-RELEASES/SPACECRAFT/](./CONFIG_MGMT/07-RELEASES/SPACECRAFT/)**) | PM, Mission |

---

## Cross-Function Dependencies

- **Supply Chain:** AML/AVL, PPAP/SCARs (**[SUPPLY_CHAIN/](./SUPPLY_CHAIN/)**)  
- **Quality:** QMS procedures, audits (**[QUALITY_QMS/02-PROCEDURES/](./QUALITY_QMS/02-PROCEDURES/)**)  
- **Standards:** Compliance matrices (**[STANDARDS/05-MAPPINGS/](./STANDARDS/05-MAPPINGS/)**)  
- **Digital Thread:** CI/CD gates, traceability (**[DIGITAL_THREAD/10-CI_CD/GATES.md](./DIGITAL_THREAD/10-CI_CD/GATES.md)**)

---

## Tracking Artifacts

- **Milestone CSV:** **[ROADMAP_MILESTONES.csv](./ROADMAP_MILESTONES.csv)**  
- **Risk linkage:** **[RISK_REGISTER.md](./RISK_REGISTER.md)**  
- **KPIs:** **[DIGITAL_THREAD/10-METRICS/DT_HEALTH_DASHBOARD.md](./DIGITAL_THREAD/10-METRICS/DT_HEALTH_DASHBOARD.md)**

