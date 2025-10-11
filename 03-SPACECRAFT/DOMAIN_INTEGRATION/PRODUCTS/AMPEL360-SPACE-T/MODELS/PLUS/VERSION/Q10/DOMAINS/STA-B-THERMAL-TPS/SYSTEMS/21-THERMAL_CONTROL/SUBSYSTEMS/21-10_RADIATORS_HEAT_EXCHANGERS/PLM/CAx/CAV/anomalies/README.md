# ANOMALIES — Non-Conformance Reports and Re-Test Evidence

## Purpose

This directory contains non-conformance reports (NCRs), deviation records, and re-test evidence documenting issues encountered during testing and their resolution.

## Contents

- Non-conformance reports (NCRs)
- Test deviations and waivers
- Failure investigation reports
- Root cause analysis
- Corrective action records
- Re-test data and verification
- Lessons learned documentation

## File Naming Convention

```
NCR_<number>_<serial>_<issue>_<date>.{pdf|docx}
```

Examples:
- `NCR-21-10-001_RAD-SN001_leak_detected_20251011.pdf`
- `NCR-21-10-002_HX-SN005_overtemp_20251012.docx`
- `DEVIATION_tvac_chamber_temp_20251015.pdf`

## Non-Conformance Categories

### Hardware Non-Conformances
- Dimensional out-of-tolerance
- Material defects
- Workmanship issues
- Damage during handling/test
- Performance below specification

### Test Non-Conformances
- Test procedure not followed
- Equipment malfunction
- Environmental conditions out-of-spec
- Data loss or corruption
- Safety incident

### Process Non-Conformances
- Manufacturing process deviation
- Coating application issue
- Weld/braze defect
- Cleaning/contamination issue

## NCR Process

### 1. Identification
- Detect and document non-conformance
- Stop work if safety or quality risk
- Tag hardware "HOLD" if applicable
- Initiate NCR immediately

### 2. Documentation
NCR must include:
- Unique NCR number
- Date and reporter name
- Hardware serial number
- Description of non-conformance
- Photos or data showing issue
- Requirement violated
- Impact assessment

### 3. Investigation
- Root cause analysis
- Contributing factors
- Extent of condition (other units affected?)
- Reference to specifications/drawings

### 4. Disposition
Options:
- **Use-As-Is**: Acceptable despite non-conformance
- **Repair**: Fix and re-inspect
- **Rework**: Redo process correctly
- **Scrap**: Hardware unusable
- **Return to Vendor**: Supplier issue

### 5. Approval
Disposition requires approval from:
- ✅ Engineering (design authority)
- ✅ Quality assurance
- ✅ Manufacturing (if process change)
- ✅ Customer (if contractually required)

### 6. Implementation
- Execute approved disposition
- Document actions taken
- Perform re-inspection or re-test
- Update records

### 7. Verification
- Verify corrective action effective
- Re-test if performance affected
- Document verification results
- Close NCR

## Re-Test Requirements

After repair/rework:
- Perform all affected tests again
- Not just spot-check repair location
- Document re-test with clear traceability to NCR
- Compare to original baseline data
- Obtain approval before proceeding

## Deviation Handling

Test deviations (non-hardware issues):
- Document what was different from procedure
- Assess impact on test results
- Obtain engineering concurrence
- Update procedures if needed
- Note in test report

## Lessons Learned

Capture lessons learned:
- What went wrong and why
- How to prevent in future
- Process improvements identified
- Training needs identified
- Documentation updates needed

## Trend Analysis

Periodically review NCRs for:
- Common issues or patterns
- Systemic problems
- Supplier quality trends
- Process improvements needed
- Training effectiveness

## Traceability

Maintain traceability:
- NCR number to hardware serial
- NCR to test data affected
- NCR to corrective action
- NCR to verification test
- NCR to related NCRs (if applicable)

## Related Directories

- **[../tvac/](../tvac/)** — Test data potentially affected
- **[../leak_proof/](../leak_proof/)** — Leak repairs and re-tests
- **[../fai/](../fai/)** — FAI non-conformances
- **[../reports/](../reports/)** — Test reports noting NCRs
- **[../../CAI/](../../CAI/)** — Inspection findings

---

**Last Updated**: 2025-10-10
