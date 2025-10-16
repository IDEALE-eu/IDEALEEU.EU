---
area: "00-PROGRAM/COMPLIANCE/03-CERTIFICATION/COMPLIANCE_CHECKLISTS"
owner: "Certification Manager"
status: "Active"
---

# COMPLIANCE_CHECKLISTS

Objective-by-objective verification checklists for applicable standards.

## Purpose

Track compliance status for each objective in applicable certification standards. These checklists provide:
- Detailed objective-by-objective compliance tracking
- Evidence references for each objective
- Compliance method identification (Test, Analysis, Review, Inspection, Similarity)
- Status tracking (Not Started, In Progress, Complete, Verified)
- Authority review status

## Checklist Types

### Aviation Standards
- **DO_178C_CHECKLIST.csv** - Software objectives by Design Assurance Level (A-E)
- **DO_254_CHECKLIST.csv** - Hardware objectives by Design Assurance Level (A-E)
- **ARP4754A_CHECKLIST.csv** - Systems development assurance objectives
- **ARP4761_CHECKLIST.csv** - Safety assessment objectives

### Space Standards
- **ECSS_E_CHECKLIST.csv** - ECSS Engineering standards objectives
- **ECSS_Q_CHECKLIST.csv** - ECSS Quality assurance objectives
- **ECSS_M_CHECKLIST.csv** - ECSS Management standards objectives
- **ECSS_S_CHECKLIST.csv** - ECSS Space sustainability objectives

### Security and Quality
- **ISO_27001_CHECKLIST.csv** - Information security controls checklist
- **AS9100D_CHECKLIST.csv** - Quality management system requirements

## Checklist CSV Format

Standard format for all checklists:
```csv
Objective_ID,Standard,Section,Objective_Description,DAL_Level,Applicability,Compliance_Method,Evidence_Reference,Status,Verified_By,Verified_Date,Authority_Review,Notes
```

### Field Descriptions
- **Objective_ID**: Unique identifier for the objective
- **Standard**: Standard name (e.g., DO-178C, ECSS-Q-ST-80)
- **Section**: Section/clause in the standard
- **Objective_Description**: Full text of the objective
- **DAL_Level**: Design Assurance Level (A-E) if applicable
- **Applicability**: Applicable / Not Applicable / Partial
- **Compliance_Method**: Test / Analysis / Review / Inspection / Similarity
- **Evidence_Reference**: Link to evidence in Evidence Index
- **Status**: Not Started / In Progress / Complete / Verified
- **Verified_By**: Name of verifier
- **Verified_Date**: Date of verification
- **Authority_Review**: Pending / Reviewed / Accepted / Finding
- **Notes**: Additional information or clarifications

## Usage Process

1. **Initialize**: Populate checklist with all objectives from standard
2. **Plan**: Assign compliance methods and responsibility
3. **Execute**: Perform activities and collect evidence
4. **Verify**: Independent verification of compliance
5. **Review**: Authority review of compliance demonstration
6. **Close**: Final acceptance and closure

## Compliance Status Reporting

Checklists feed into:
- Weekly compliance status meetings
- Monthly program reports
- Certification milestone packages
- Authority audit preparation

## Integration Points

- **Evidence Index** (`../../06-EVIDENCE/EVIDENCE_INDEX.csv`): Evidence location
- **Compliance Matrix** (`../../05-REGISTERS/COMPLIANCE_MATRIX.csv`): Requirements traceability
- **Statements of Compliance** (`../STATEMENTS_OF_COMPLIANCE/`): Formal declarations
- **Certification Packages** (`../CERTIFICATION_PACKAGES/`): Milestone deliverables

## Quality Control

- Checklists reviewed quarterly for completeness
- Evidence references verified before milestone reviews
- Authority findings tracked and resolved
- Configuration managed with certification baselines

## Related Documents

- Master Plan: [`../PLAN_FOR_SOCC.md`](../PLAN_FOR_SOCC.md)
- Certification Plans: [`../CERTIFICATION_PLANS/`](../CERTIFICATION_PLANS/)
- Compliance Issues: [`../COMPLIANCE_ISSUES_LOG.csv`](../COMPLIANCE_ISSUES_LOG.csv)
