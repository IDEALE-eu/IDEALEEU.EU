# DEVIATIONS_WAIVERS — Deviations, Waivers, and Non-Conformances

## Purpose

This directory documents all approved deviations from standards, waivers for non-compliance, and non-conformance reports (NCRs) with associated risk assessments and dispositions.

## Contents

This directory contains:
- Deviation requests and approvals
- Waiver documentation with risk acceptance
- Non-conformance reports (NCRs)
- Material Review Board (MRB) dispositions
- Risk assessments for non-compliances

## Document Types

### Deviation Request (DR)
Planned non-compliance with a standard:
- Identified during design phase
- Technical justification provided
- Alternative compliance method proposed
- Approved before implementation

### Waiver
Approved exception to a requirement:
- Cannot be met as specified
- Risk assessment performed
- Mitigation measures identified
- Authority approval obtained

### Non-Conformance Report (NCR)
Unplanned non-compliance discovered:
- Found during manufacturing or test
- Root cause analysis performed
- Disposition determined (use-as-is, rework, scrap)
- Corrective action implemented

## File Naming

```
21-10-CMP-<TYPE>-<ID>__r<NN>__<STATUS>.pdf
```

Examples:
- `21-10-CMP-DR-001-thermal-margin__r01__REL.pdf`
- `21-10-CMP-WAIVER-002-coating-alpha__r02__REL.pdf`
- `21-10-CMP-NCR-003-weld-porosity__r01__REL.pdf`

## Deviation Request Structure

### Required Sections

1. **Identification**
   - DR number and title
   - Date submitted
   - Originator and organization

2. **Requirement**
   - Standard/requirement being deviated
   - Specific clause or section
   - Original requirement text

3. **Justification**
   - Technical rationale for deviation
   - Why standard approach not feasible
   - Heritage or precedent (if applicable)

4. **Alternative Approach**
   - Proposed compliance method
   - Evidence that alternative meets intent
   - Performance comparison to standard

5. **Risk Assessment**
   - Technical risks identified
   - Probability and consequence
   - Mitigation measures
   - Residual risk

6. **Approval**
   - Signatures: Project manager, chief engineer, quality
   - Customer approval (if required)
   - Date approved

## MRB Dispositions

### Use-As-Is
- Discrepancy has no impact on form, fit, function
- Risk assessment supports acceptance
- Documentation updated to reflect as-built

### Rework
- Discrepancy correctable
- Rework procedure defined
- Re-inspection after rework
- Root cause corrective action

### Repair
- Discrepancy acceptable with repair
- Repair procedure approved
- Re-verification required
- Documentation of repair

### Scrap
- Discrepancy not correctable or acceptable
- Part replaced
- Root cause analysis and corrective action
- Lessons learned documented

## Risk Assessment

### Risk Categories
- **Technical**: Performance impact
- **Schedule**: Delivery impact
- **Cost**: Budget impact
- **Safety**: Mission/crew safety
- **Quality**: Product quality impact

### Risk Levels
- **High**: Significant impact, immediate action
- **Medium**: Moderate impact, managed mitigation
- **Low**: Minor impact, accepted with documentation

## Tracking and Closure

1. Deviation/NCR logged in tracking system
2. Risk assessment performed
3. Disposition determined by MRB
4. Corrective action implemented
5. Verification of closure
6. Documentation archived

## Configuration Control

- All deviations/waivers require CCB approval
- NCRs tracked in quality management system
- Closure verified before delivery
- Audit trail maintained

## Standards

- **ECSS-Q-ST-10C**: Product assurance management
- **AS9100**: Nonconformity and corrective action
- **ISO 9001**: Control of nonconforming product

## Related Documentation

- Standards applicability: [`../applicability_matrix/`](../applicability_matrix/)
- Requirements: [`../../requirements/`](../../requirements/)
- NCR linkage: [`../../ncr_waivers/`](../../ncr_waivers/)
