# DO-178C Level A – Planning README

## Purpose
This directory holds all Level A planning data per DO-178C and ARP4754A linkage.  
It defines the lifecycle framework, independence, and configuration control for the system or software item classified as DAL A (catastrophic failure condition).

## Required Plans
Each plan must reference project identifiers, baselines, and trace matrices.

| File | Description |
|------|--------------|
| **PSAC.md** | Plan for Software Aspects of Certification – links all other plans and defines DAL, system context, and certification approach. |
| **SDP.md** | Software Development Plan – methods, standards, and environment. |
| **SVP.md** | Software Verification Plan – verification strategy, independence matrix, and coverage objectives. |
| **SQAP.md** | Software Quality Assurance Plan – audits, process monitoring, and QA independence. |
| **SCMP.md** | Software Configuration Management Plan – baselines, CCB procedures, and change tracking. |

## Responsibilities
- **Development Lead:** author SDP, maintain consistency with design/code repositories.  
- **Verification Lead (independent):** own SVP, define test independence and MC/DC evidence scope.  
- **QA Lead:** maintain SQAP, record audits, and ensure objective independence.  
- **CM Lead:** maintain SCMP, operate CCB, generate baselines and indices.  
- **Certification Focal:** maintain PSAC and coordinate with authorities.

## Deliverables
1. Signed and baselined plan set (`*_vX.Y_signed.pdf`).
2. Approval evidence (email, minutes, or SOI-1 record).
3. Cross-reference matrix linking DO-178C §11 objectives to plan sections.
4. Version control and hash records for traceability.

## Structure
```

planning/
PSAC.md
SDP.md
SVP.md
SQAP.md
SCMP.md
approvals/
SOI1_minutes.pdf
authority_correspondence/
traceability/
objectives_matrix.xlsx

```

## Quality Gates
- **FCR-1:** all plans approved, environments verified, independence matrix complete.  
- **FCR-2:** plan compliance verified, updates incorporated into SAS.

## Notes
- Keep document headers with: project, DAL, baseline ID, date, author, approver.  
- All edits require version increment and QA review.  
- Use markdown for draft, PDF for signed deliverables.
```

