# DO-178C Overview

Primary standard for planning, developing, verifying, and certifying airborne software.

## Software Levels
| Level | Effect | Typical Objectives | Rigor |
|------|--------|---------------------|-------|
| **A** | Catastrophic | ~71 | Highest |
| **B** | Hazardous/Severe-Major | Fewer than A | High |
| **C** | Major | Fewer than B | Moderate |
| **D** | Minor | Reviews only | Low |
| **E** | No safety effect | None | Minimal |

## Lifecycle Data (what to store here)
- **Planning:** [PSAC](./LEVEL_A/planning/PSAC.md), [SDP](./LEVEL_A/planning/SDP.md), [SVP](./LEVEL_A/planning/SVP.md), [SQAP](./LEVEL_A/planning/SQAP.md), [SCMP](./LEVEL_A/planning/SCMP.md)
- **Development:** SRS/HLR, LLR/SDD, source code, interfaces
- **Verification:** procedures, results, anomalies, structural coverage
- **Configuration Management:** baselines, CCB minutes, change logs
- **Quality Assurance:** audits, NCRs, readiness reviews
- **Certification:** SAS, Configuration Index, SOI records

## Verification Independence & Coverage
| Level | Independence | Structural Coverage |
|------|--------------|---------------------|
| **A** | Full (dev vs. verification/QA) | Statement + Decision + **MC/DC** |
| **B** | Significant | Statement + Decision (often MC/DC by policy) |
| **C** | Limited | Decision |
| **D/E** | Minimal/None | Reviews only (no structural coverage) |

## Supplements
- **DO-330** Tool Qualification  
- **DO-331** Model-Based Development  
- **DO-332** Object-Oriented Technology  
- **DO-333** Formal Methods  

## Folder Index
- [LEVEL_A/](./LEVEL_A/) — Level A compliance set  
  - [planning/](./LEVEL_A/planning/) — plans and approvals  
  - [requirements/](./LEVEL_A/requirements/) — HLR/LLR and trace  
  - [design/](./LEVEL_A/design/)  
  - [source/](./LEVEL_A/source/)  
  - [verification/](./LEVEL_A/verification/)  
  - [cm/](./LEVEL_A/cm/)  
  - [qa/](./LEVEL_A/qa/)  
  - [certification/](./LEVEL_A/certification/)

> Keep links relative. Baseline signed PDFs alongside editable sources.
