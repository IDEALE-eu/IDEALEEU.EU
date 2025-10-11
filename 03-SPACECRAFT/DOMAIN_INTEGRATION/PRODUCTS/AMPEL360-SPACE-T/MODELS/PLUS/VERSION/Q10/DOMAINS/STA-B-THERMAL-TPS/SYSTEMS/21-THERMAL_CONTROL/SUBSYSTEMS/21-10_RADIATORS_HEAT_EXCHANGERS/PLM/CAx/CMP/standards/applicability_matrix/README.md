# APPLICABILITY_MATRIX — Standards Applicability Matrix (SAM)

## Purpose

The Standards Applicability Matrix (SAM) documents which standards apply to the 21-10 RADIATORS_HEAT_EXCHANGERS subsystem, the level of applicability, and how compliance is demonstrated.

## Contents

This directory contains SAM files that document:
- Applicable standards and their versions
- Specific clauses/requirements from each standard
- Level of applicability (Full/Partial/Not Applicable)
- Compliance statement and evidence reference
- Approved deviations or tailoring

## SAM Structure

### Required Columns

| Column | Description | Example |
|--------|-------------|---------|
| Standard | Standard identifier | ECSS-E-ST-31C |
| Version | Standard version | Rev. 1, 2008-07-15 |
| Clause | Specific section | 5.2.3 Radiator design |
| Requirement | Clause text summary | Radiator sizing margins |
| Applicability | Full/Partial/N/A | Full |
| Compliance Method | How met | Analysis + Test |
| Evidence | Reference to proof | CAE/thermal_analysis_r02.pdf |
| Deviation | If tailored | None |
| Notes | Additional info | Heritage from previous mission |

## File Naming

```
21-10-CMP-SAM_<standard>__r<NN>__<STATUS>.xlsx
```

Examples:
- `21-10-CMP-SAM_ECSS-E-ST-31C__r02__REL.xlsx` - Thermal standard
- `21-10-CMP-SAM_NASA-STD-5001__r01__REL.xlsx` - Structural factors
- `21-10-CMP-SAM_master__r03__REL.xlsx` - All standards

## Applicability Levels

### Full Applicability
- Standard fully applicable without modification
- All clauses apply as written
- No tailoring or deviation
- Complete compliance demonstrated

### Partial Applicability
- Some clauses apply, others do not
- Tailoring approved (e.g., reduced test levels)
- Alternative compliance method
- Documented rationale for non-applicable clauses

### Not Applicable
- Standard does not apply to this subsystem
- Documented rationale (e.g., no electrical components)
- Reviewed and approved by systems engineering

## Compliance Statement Guidelines

Each compliance statement should:
1. Clearly state how the requirement is met
2. Reference specific evidence artifacts
3. Identify responsible organization/engineer
4. Note any assumptions or limitations

Examples:
- "Thermal analysis per CAE/thermal_model_r05 demonstrates compliance with margin requirements"
- "TVAC test report CAV/tvac_report_r02 validates thermal performance"
- "Material selection documented in materials_processes/outgassing/"

## Deviation Documentation

When tailoring is required:
1. Document technical justification
2. Assess risk and impact
3. Propose alternative compliance method
4. Obtain DRB approval
5. Link to deviation/waiver in [`../deviations_waivers/`](../deviations_waivers/)

## Review Cycle

1. Initial SAM created during requirements definition
2. Review at PDR for completeness
3. Update at CDR with evidence references
4. Final approval at acceptance review
5. Configuration controlled post-delivery

## Version Control

- Update revision number for substantive changes
- Track changes in revision history section
- Maintain previous versions for audit trail

## Standards

- **ECSS-M-ST-10C**: Project planning
- **ISO 9001**: Quality management documentation

## Related Documentation

- Standards references: [`../refs/`](../refs/)
- Deviations/waivers: [`../deviations_waivers/`](../deviations_waivers/)
- Requirements: [`../../requirements/`](../../requirements/)
