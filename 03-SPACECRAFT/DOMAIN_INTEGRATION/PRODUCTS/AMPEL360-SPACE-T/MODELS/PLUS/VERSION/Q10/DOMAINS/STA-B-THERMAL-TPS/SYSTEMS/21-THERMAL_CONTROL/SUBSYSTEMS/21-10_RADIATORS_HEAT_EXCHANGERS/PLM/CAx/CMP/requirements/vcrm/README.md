# VCRM — Verification Cross-Reference Matrix

## Purpose

The Verification Cross-Reference Matrix (VCRM) maps requirements to specific verification activities and test procedures, ensuring comprehensive verification coverage and traceability to test results.

## Contents

This directory contains VCRM files that cross-reference:
- Requirements to test procedures
- Test procedures to test reports
- Test reports to acceptance criteria
- Test results to requirement closure

## VCRM Structure

### Required Columns

| Column | Description | Example |
|--------|-------------|---------|
| Requirement ID | Subsystem requirement | 21-10-THM-RAD-005 |
| Verification Method | Primary method | Test (T) |
| Test Procedure | Procedure reference | TP-21-10-TVAC-001 |
| Test Report | Results reference | TR-21-10-TVAC-001-r02 |
| Test Date | When performed | 2025-03-15 |
| Acceptance Criteria | Pass/fail criteria | Tmin ≥ -20°C, Tmax ≤ 80°C |
| Result | Pass/Fail/Conditional | Pass |
| Notes | Additional information | Minor deviation per NCR-21-10-007 |

## File Naming

```
21-10-CMP-VCRM_<scope>__r<NN>__<STATUS>.xlsx
```

Examples:
- `21-10-CMP-VCRM_master__r02__REL.xlsx` - Complete VCRM
- `21-10-CMP-VCRM_TVAC__r01__RVW.xlsx` - TVAC test only
- `21-10-CMP-VCRM_vibration__r01__WIP.xlsx` - Vibration tests

## Verification Methods Mapping

### Analysis (A)
- Links to CAE analysis reports in `../../analyses/`
- References thermal models, FEA, or other simulations

### Test (T)
- Links to CAV test procedures and reports
- References actual test data in `../../test_evidence/`

### Inspection (I)
- Links to CAI inspection records
- References dimensional checks, visual inspection, NDT

### Demonstration (D)
- Links to functional demonstrations
- References operational verification procedures

## Cross-Reference Requirements

1. **Complete Coverage**: Every requirement must appear in VCRM
2. **Traceability**: Each entry must link to verification artifact
3. **Results Documentation**: Test results must be recorded with pass/fail
4. **Deviation Handling**: Failures must reference NCR or waiver

## Review Cycle

1. VCRM drafted during verification planning (DVP/ATP)
2. Updated as verification activities are performed
3. Reviewed after each major test campaign
4. Final approval at acceptance review
5. Configuration controlled after delivery

## Status Tracking

- **Planned**: Verification activity scheduled
- **In-Progress**: Test/analysis underway
- **Complete**: Results available
- **Accepted**: Customer approved

## Tools

- Microsoft Excel or equivalent
- Database integration for test data
- PLM system for configuration control

## Standards

- **ECSS-E-ST-10-03C**: Testing
- **ECSS-Q-ST-10C**: Product assurance
- **MIL-STD-1540E**: Test requirements for launch vehicles

## Related Documentation

- Test evidence: [`../../test_evidence/`](../../test_evidence/)
- RTM: [`../rtm/`](../rtm/)
- Verification matrix: [`../verification_matrix/`](../verification_matrix/)
