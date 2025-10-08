# 05-MAPPINGS

Standards-to-requirements mappings, compliance matrices, and stage gate checklists.

## Overview

This directory provides traceability between standards and program artifacts, including requirements, processes, compliance matrices, and review checklists for stage gates.

## Contents

- **00-README.md** - This file
- **STANDARD_TO_REQUIREMENT.csv** - Maps standards clauses to system requirements
- **STANDARD_TO_PROCESS.md** - Maps standards to internal procedures and processes
- **COMPLIANCE_MATRIX_TEMPLATES/** - Templates for compliance matrices by standard
- **CHECKLISTS/** - Stage gate checklists (PDR, CDR, PRR, etc.)

## Purpose

The mappings in this directory serve multiple purposes:
1. **Traceability**: Link standards to requirements, design, verification
2. **Compliance Demonstration**: Show how each standard requirement is met
3. **Stage Gate Evidence**: Checklists ensure readiness for reviews
4. **Audit Support**: Provide evidence for certification authorities and auditors
5. **Gap Analysis**: Identify missing compliance elements

## STANDARD_TO_REQUIREMENT.csv

### Structure
Maps individual standard clauses to system requirements:
- **standard_id**: Reference to uid in 01-REGISTER/STANDARDS_REGISTER.csv
- **clause**: Specific clause/section of standard (e.g., "5.2.1", "Table A-1 Objective 5")
- **requirement_id**: System requirement identifier (e.g., "SYS-REQ-001")
- **coverage_type**: How requirement addresses standard (FULL, PARTIAL, INDIRECT)
- **verification_method**: How compliance is verified (TEST, ANALYSIS, INSPECTION, REVIEW)

### Example
```csv
standard_id,clause,requirement_id,coverage_type,verification_method
STD-001,5.1.2,SYS-REQ-123,FULL,REVIEW
STD-001,5.2.1,SYS-REQ-124,FULL,ANALYSIS
STD-003,6.3.1a,SW-REQ-045,FULL,TEST
```

### Usage
- Systems engineers allocate standard requirements to system requirements
- During design reviews, verify coverage is complete
- During audits, demonstrate traceability
- Identify gaps (standard clauses not covered)

## STANDARD_TO_PROCESS.md

### Structure
Maps standards to internal procedures and processes:
- **Standard**: Which standard (e.g., DO-178C, ARP4754A)
- **Internal Process/Procedure**: Document or procedure that implements standard
- **Notes**: Additional context

### Example
- **DO-178C** → PRO-012 Software Development Procedure
- **DO-254** → PRO-015 Hardware Design Assurance Procedure
- **ARP4761** → PRO-003 Safety Assessment Process
- **ISO 10007** → PRO-001 Configuration Management Plan

### Usage
- New team members understand where standards are implemented
- Auditors see mapping between standards and procedures
- Updates to standards trigger review of procedures

## COMPLIANCE_MATRIX_TEMPLATES/

### Purpose
Provide templates for detailed compliance matrices per standard. These are "objective-by-objective" or "clause-by-clause" mappings.

### Templates Provided
- **ARP4754A_CM.csv** - Systems engineering compliance matrix
- **DO178C_CM.csv** - Software compliance matrix
- **ECSS_CM.csv** - Spacecraft engineering compliance matrix

### Template Structure
Typically includes:
- **Objective/Clause**: Standard requirement
- **Applicability**: FULL, PARTIAL, N/A
- **Rationale**: Why applicable or not applicable
- **Compliance Method**: How met (document, test, review, analysis)
- **Compliance Evidence**: Reference to artifact (document ID, test report)
- **Status**: COMPLIANT, IN-PROGRESS, NOT-STARTED, N/A

### Usage
- Project teams fill out templates during development
- Reviewed at stage gates (PDR, CDR, TRR)
- Submitted to certification authorities as compliance evidence
- Audited by quality assurance and authorities

## CHECKLISTS/

### Purpose
Provide stage gate checklists ensuring standards compliance evidence is ready for reviews.

### Checklists Provided
- **PDR_CHECKLIST.md** - Preliminary Design Review checklist
- **CDR_CHECKLIST.md** - Critical Design Review checklist (certification basis freeze)
- **PRR_CHECKLIST.md** - Production Readiness Review checklist

### Checklist Structure
Organized by topic:
- **Standards Compliance**: Required documents and evidence
- **Requirements**: Traceability, completeness
- **Design**: Architecture, interfaces, analysis
- **Verification**: Test plans, procedures
- **Configuration Management**: Baselines, change control
- **Safety**: Hazard analysis, safety case
- **Quality**: Quality plans, audits
- **Schedule**: Completion status, open items

### Usage
- Program teams prepare for stage gates
- Review board uses checklist to assess readiness
- Missing items are identified and tracked
- No-go if critical items not complete

## Traceability Flow

```
Standards (ARP4754A, DO-178C, etc.)
    ↓ (allocated to)
System Requirements (SYS-REQ-xxx)
    ↓ (refined to)
Subsystem Requirements (SW-REQ-xxx, HW-REQ-xxx)
    ↓ (implemented in)
Design (architecture, detailed design)
    ↓ (verified by)
Verification (test cases, analyses, reviews)
```

Mappings in this directory support each step of traceability.

## Key Deliverables

1. **Populated STANDARD_TO_REQUIREMENT.csv** - Complete mapping
2. **STANDARD_TO_PROCESS.md** - Updated with current procedures
3. **Compliance Matrices** - Filled-in templates (ARP4754A, DO-178C, ECSS)
4. **Stage Gate Checklists** - Completed checklists for each review
5. **Traceability Report** - Requirements-to-verification traceability

## Compliance Requirements

- All applicable standard requirements shall be traced to system requirements
- Compliance matrices shall be maintained and updated
- Stage gate checklists shall be completed before reviews
- Gaps identified shall be tracked and resolved
- Traceability shall be auditable

## Integration with Other Standards

- **ARP4754A**: Traceability is core systems engineering activity
- **DO-178C/DO-254**: Software/hardware requirements traced to standards
- **ECSS-E-ST-10C**: Verification Control Document (VCD) similar concept
- **ISO 10007 / EIA-649C**: Configuration management of baselines

## Tools

- **Requirements Management**: DOORS, Jama, Polarion, Jira
- **Spreadsheets**: Excel, Google Sheets for matrices
- **PLM/PDM**: Teamcenter, 3DEXPERIENCE for traceability
- **Custom Tools**: In-house traceability databases

## Best Practices

- Establish mappings early (Phase A/B)
- Update continuously (not just before audits)
- Automate traceability where possible (tools, scripts)
- Review mappings at stage gates
- Engage certification authorities early (agree on approach)

## Common Pitfalls

- Mappings created late (scramble before audit)
- Incomplete coverage (gaps not identified)
- Mappings not maintained (become stale)
- Too high-level (not detailed enough for audit)
- Too detailed (overwhelms auditors, hard to maintain)

## References

- 01-REGISTER/STANDARDS_REGISTER.csv - List of applicable standards
- 02-AIRCRAFT/, 03-SPACECRAFT/ - Standard requirements by domain
- 00-PROGRAM/CONFIG_MGMT/ - Configuration management of mappings
- Certification authority guidance on compliance demonstration

---

**Status**: Configuration-controlled per 00-PROGRAM/CONFIG_MGMT/
