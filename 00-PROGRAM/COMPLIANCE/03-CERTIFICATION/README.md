---
area: "00-PROGRAM/COMPLIANCE/03-CERTIFICATION"
owner: "Certification Manager"
status: "Active"
utcs_anchor: "utcs://PROGRAM/COMPLIANCE/CERTIFICATION"
confidentiality: "Internal"
---

# 03-CERTIFICATION

Certification plans, compliance checklists, and statements of compliance (SoC) for aircraft and spacecraft certification.

## Purpose

Manage the certification strategy and artifacts required to demonstrate compliance with applicable airworthiness and space mission assurance standards to certification authorities.

## Contents

### Certification Plans

#### Aviation Certification
- **PSAC** (Plan for Software Aspects of Certification) - DO-178C
- **PHAC** (Plan for Hardware Aspects of Certification) - DO-254
- **CMP** (Certification Maintenance Plan)
- **Certification Basis** document defining applicable regulations
- **Type Certification** strategy (TC, STC, ATC)

#### Space Certification
- **Mission Assurance Plan** - ECSS-Q-ST-80
- **Safety Case** documentation
- **Launch Approval** package
- **Mission Readiness Review** (MRR) materials

### Compliance Checklists

Objective-by-objective verification:
- **DO-178C Checklist** (by software level A-E)
- **DO-254 Checklist** (by hardware level A-E)
- **ARP4754A Checklist** (systems engineering objectives)
- **ARP4761 Checklist** (safety assessment)
- **ECSS Checklists** (by applicable ECSS standards)
- **ISO 27001 Checklist** (information security controls)

### Statements of Compliance (SoC)

Formal compliance declarations:
- Requirements compliance statement
- Test compliance statement
- Analysis compliance statement
- Process compliance statement
- Tool qualification statement

### Certification Authority Interaction

- **Questions and Responses** log
- **Finding Reports** and closure evidence
- **Issue Papers** for complex compliance topics
- **Meeting Minutes** with certification authority
- **Compliance Notifications** and updates

## Certification Process Flow

```
Phase A-B: Define Certification Basis
    ↓
Phase C: Develop Certification Plans (PSAC, PHAC, etc.)
    ↓
Phase D: Execute per Plans, Collect Evidence
    ↓
Phase E: Compliance Reviews, Authority Audits
    ↓
Phase F: Final Certification Package Submission
    ↓
Type Certificate / Mission Approval Issued
```

## Certification Artifacts by Phase

### Phase B (Preliminary Design)
- Draft certification basis
- Certification approach (means of compliance)
- Authority engagement plan

### Phase C (Detailed Design)
- Approved certification plans (PSAC, PHAC, etc.)
- Initial compliance checklists
- Tool qualification plans

### Phase D (Development)
- Evidence collection per compliance matrix
- Regular compliance status reviews
- Preliminary SoC drafts

### Phase E (Verification & Validation)
- Completed compliance checklists
- Final statements of compliance
- Authority audit preparation

### Phase F (Production & Delivery)
- Type Certificate Data Sheet (TCDS)
- Certification Maintenance Requirements
- Instructions for Continued Airworthiness (ICA)

## Compliance Demonstration Methods

- **Test**: Physical testing with recorded results
- **Analysis**: Engineering analysis and simulation
- **Review**: Design review and documentation review
- **Inspection**: Physical inspection of hardware
- **Similarity**: Comparison to previously certified items

## Tool Qualification

Software/hardware tools used in certification:
- Tool Qualification Plan (TQP)
- Tool Operational Requirements (TOR)
- Tool Qualification Data (TQD)
- Tool Qualification Summary (TQS)

Tracked in `TOOL_QUALIFICATION_LOG.csv`

## Certification Milestones

Key reviews with certification authority:
- **Certification Basis Review** (Phase B exit)
- **Plan Review** (Phase C exit)
- **Compliance Demonstration Review** (Phase D-E)
- **Certification Audit** (Phase E)
- **Final Certification Board** (Phase F)

## Compliance Matrix Integration

This directory works closely with `../05-REGISTERS/COMPLIANCE_MATRIX.csv`:
- Certification plans define *how* compliance will be shown
- Compliance matrix tracks *what* needs to be complied with
- Evidence index (`../06-EVIDENCE/`) shows *where* evidence is located

## Key Artifacts

### PLAN_FOR_SOCC.md
Master Plan for Statement of Compliance and Conformity:
- Certification strategy overview
- Compliance demonstration approach
- Schedule and milestones
- Roles and responsibilities
- References to detailed plans (PSAC, PHAC, etc.)

### COMPLIANCE_CHECKLISTS/
Directory containing:
- DO-178C objectives checklist (by DAL A-E)
- DO-254 objectives checklist (by DAL A-E)
- ARP4754A development assurance checklist
- ARP4761 safety assessment checklist
- ECSS requirements checklists

### CERTIFICATION_PACKAGES/
Organized by certification event:
- `PDR_COMPLIANCE/` - Preliminary Design Review compliance
- `CDR_COMPLIANCE/` - Critical Design Review compliance
- `TRR_COMPLIANCE/` - Test Readiness Review compliance
- `PRR_COMPLIANCE/` - Production Readiness Review compliance
- `FINAL_CERT/` - Final certification submission package

### AUTHORITY_CORRESPONDENCE/
- Questions received and responses provided
- Finding reports and corrective actions
- Issue papers for complex topics
- Meeting minutes and action items

## Certification Authority Relationships

### EASA (European Union Aviation Safety Agency)
- Primary authority for EU operations
- Type certification (TC) for new aircraft
- Supplemental Type Certification (STC) for modifications

### FAA (Federal Aviation Administration)
- Authority for US operations
- Bilateral agreements with EASA
- Import/export certificates

### ESA (European Space Agency)
- Space mission reviews (for ESA-funded missions)
- Launch approval coordination

### National Space Agencies
- Mission-specific requirements
- Launch site approvals

## Non-Compliance Management

When non-compliance identified:
1. Document in `COMPLIANCE_ISSUES_LOG.csv`
2. Assess impact on certification
3. Develop corrective action plan
4. Notify certification authority if required
5. Track to closure
6. Update compliance checklist

## Related Documents

- Compliance Matrix: [`../05-REGISTERS/COMPLIANCE_MATRIX.csv`](../05-REGISTERS/COMPLIANCE_MATRIX.csv)
- Evidence Index: [`../06-EVIDENCE/EVIDENCE_INDEX.csv`](../06-EVIDENCE/EVIDENCE_INDEX.csv)
- Standards Library: [`../01-STANDARDS/`](../01-STANDARDS/)
- Audit Reports: [`../04-AUDITS/`](../04-AUDITS/)
- V&V Plans: [`../../CONFIG_MGMT/08-VERIFICATION_VALIDATION/`](../../CONFIG_MGMT/08-VERIFICATION_VALIDATION/)

## Metrics

- Compliance checklist completion (% complete)
- Open findings from authority (count, age)
- Certification milestones (on-time %)
- Evidence gaps (count, closure trend)

---

**Owner**: Certification Manager with Systems Engineering support  
**Review**: Continuous during development, frozen at Type Certificate  
**Approval**: Chief Engineer, Certification Review Board
