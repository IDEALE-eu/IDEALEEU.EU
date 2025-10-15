---
area: "00-PROGRAM/COMPLIANCE/01-STANDARDS"
owner: "Standards & Compliance Manager"
status: "Active"
utcs_anchor: "utcs://PROGRAM/COMPLIANCE/STANDARDS"
confidentiality: "Internal"
---

# 01-STANDARDS

Controlled copies of applicable standards and applicability matrices for the IDEALEEU.EU program.

## Purpose

Maintain current, controlled versions of all standards applicable to aircraft and spacecraft development, ensuring traceability and proper application across the program.

## Contents

### Controlled Standards Repository
- **Aviation Standards**: DO-178C, DO-254, DO-160, ARP4754A, ARP4761, EASA CS-25, Part 21/145
- **Space Standards**: ECSS-E (Engineering), ECSS-M (Management), ECSS-Q (Quality), ECSS-S (Space systems)
- **Quality Standards**: AS9100, ISO 9001, ISO 10007 (Configuration Management)
- **Security Standards**: ISO 27001, DO-326A/355A/356A (Cybersecurity)
- **Safety Standards**: ISO 14971, ARP4761, MIL-STD-882E

### Applicability Matrix
Document which standards apply to which:
- Aircraft models and variants
- Spacecraft configurations
- Subsystems and components
- Development phases
- Certification authorities

### Standard Version Control
- Active versions (current baseline)
- Superseded versions (historical reference)
- Change notices and amendments
- Transition plans for standard updates

## Key Documents

### STANDARDS_REGISTER.csv
Master register of all applicable standards:
- Standard ID, Title, Version, Effective Date
- Issuing body (EASA, FAA, ECSS, ISO, SAE)
- Applicability scope (aircraft/spacecraft/systems)
- Supersedes/Superseded by relationships
- Procurement source and access method

### APPLICABILITY_MATRIX.xlsx
Maps standards to program elements:
- Product lines (aircraft models, spacecraft missions)
- System/subsystem breakdown
- Development phases (A, B, C, D, E, F)
- Certification basis
- Tailoring decisions

### STANDARDS_LIBRARY/
Controlled copies organized by:
- `AVIATION/` - DO-178C, DO-254, ARP4754A, etc.
- `SPACE/` - ECSS family
- `QUALITY/` - AS9100, ISO standards
- `SAFETY/` - Safety and risk standards
- `SECURITY/` - Cybersecurity and data protection

## Standard Access Control

Standards are controlled documents:
- Read access: All engineering staff
- Write access: Standards Manager only
- Distribution: Internal use only (copyright restrictions)
- External sharing: Requires approval per licensing terms

## Standard Updates

When a new version is released:
1. Standards Manager procures and reviews new version
2. Gap analysis conducted (delta review)
3. Impact assessment on program artifacts
4. Transition plan created if needed
5. CCB approval for baseline update
6. Old version archived, new version activated
7. Affected documents updated

## Tailoring Process

Standards may be tailored with justification:
1. Document tailoring rationale
2. Perform impact assessment
3. Obtain customer/authority approval
4. Record in applicability matrix
5. Track in `../05-REGISTERS/DEVIATIONS_WAIVERS.csv`

## Integration Points

- **Requirements**: Standards drive system requirements (see `../05-REGISTERS/COMPLIANCE_MATRIX.csv`)
- **Procedures**: Standards inform internal processes (see `../02-POLICIES/`)
- **Evidence**: Compliance shown through objective evidence (see `../06-EVIDENCE/`)
- **Audits**: Standards form basis of audit criteria (see `../04-AUDITS/`)

## Related Documents

- Compliance Matrix: [`../05-REGISTERS/COMPLIANCE_MATRIX.csv`](../05-REGISTERS/COMPLIANCE_MATRIX.csv)
- Standards Mapping: [`../../STANDARDS/05-MAPPINGS/`](../../STANDARDS/05-MAPPINGS/)
- Certification Plans: [`../03-CERTIFICATION/`](../03-CERTIFICATION/)

## Metrics

- Standards currency (% up-to-date)
- Tailoring requests (count, approval rate)
- Gap closure (open gaps vs. closed)
- Standard update cycle time

---

**Owner**: Standards & Compliance Manager  
**Review**: Quarterly or upon standard update  
**Approval**: Chief Engineer, Quality Manager
