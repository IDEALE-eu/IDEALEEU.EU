# RTM — Requirement Traceability Matrix

## Purpose

The Requirement Traceability Matrix (RTM) provides bidirectional traceability between parent requirements and derived requirements, ensuring complete coverage and traceability throughout the subsystem lifecycle.

## Contents

This directory contains RTM files that trace:
- System-level requirements to subsystem requirements
- Subsystem requirements to design requirements
- Design requirements to verification activities
- Requirements to evidence artifacts

## RTM Structure

### Required Columns

| Column | Description | Example |
|--------|-------------|---------|
| Parent Req ID | System/mission requirement | STA-B-21-THM-001 |
| Requirement ID | Subsystem requirement | 21-10-THM-RAD-001 |
| Requirement Text | Full requirement statement | Radiator shall reject 500W minimum |
| Rationale | Why this requirement exists | Payload thermal load dissipation |
| Verification Method | A, T, I, or D | A+T (Analysis + Test) |
| Evidence Reference | Location of proof | CAE/thermal_analysis_r02.pdf |
| Status | Open, In-Progress, Verified, Accepted | Verified |
| Owner | Responsible engineer | J.Smith |
| NCR/Waiver | Non-conformance reference | NCR-21-10-003 (if applicable) |

## File Naming

```
21-10-CMP-RTM_<scope>__r<NN>__<STATUS>.xlsx
```

Examples:
- `21-10-CMP-RTM_master__r03__REL.xlsx` - Complete RTM
- `21-10-CMP-RTM_thermal__r02__RVW.xlsx` - Thermal requirements only
- `21-10-CMP-RTM_structural__r01__WIP.xlsx` - Structural requirements subset

## Traceability Rules

1. **One-to-Many**: One parent requirement may generate multiple derived requirements
2. **No Orphans**: Every requirement must trace to a parent (except top-level)
3. **Complete Verification**: Every requirement must have at least one verification method
4. **Evidence Required**: Every verified requirement must reference evidence

## Verification Status

- **Open**: Requirement defined, verification pending
- **In-Progress**: Verification activity underway
- **Verified**: Evidence collected, awaiting acceptance
- **Accepted**: Verification complete and approved

## Review Process

1. Draft RTM created during requirements definition
2. Peer review by systems engineering team
3. Approval by chief engineer and customer (if required)
4. Baseline control after PDR/CDR gate
5. Update via ECN process for changes

## Tools

- Microsoft Excel or equivalent
- PLM system integration for version control
- Export to CSV for data interchange

## Standards

- **ECSS-E-ST-10C**: Requirements management
- **NASA-STD-7009**: Standard for models and simulations
- **ISO/IEC/IEEE 29148**: Requirements engineering

## Related Documentation

- Verification matrix: [`../verification_matrix/`](../verification_matrix/)
- VCRM: [`../vcrm/`](../vcrm/)
- Parent README: [`../README.md`](../README.md)
