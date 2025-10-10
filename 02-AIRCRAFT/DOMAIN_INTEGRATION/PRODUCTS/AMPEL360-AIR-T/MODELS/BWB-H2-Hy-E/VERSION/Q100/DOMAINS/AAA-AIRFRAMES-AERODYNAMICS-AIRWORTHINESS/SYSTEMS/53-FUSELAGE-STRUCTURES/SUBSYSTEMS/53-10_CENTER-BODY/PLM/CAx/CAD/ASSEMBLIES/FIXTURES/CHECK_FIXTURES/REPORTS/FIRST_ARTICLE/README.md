# FIRST_ARTICLE — First Article Inspection Reports

## Purpose

This directory contains First Article Inspection (FAI) reports per AS9102 requirements.

## Contents

### FAI Report Components
- **Form 1**: Part number and engineering approval record
- **Form 2**: Product accountability (accountability for all drawings)
- **Form 3**: Characteristic accountability and verification
- **Supporting data**: CMM reports, certificates, test results
- **Assembly FAI**: For assemblies with multiple components

## Naming Convention

Use the following pattern:
```
FAI_<part-id>_<serial>_<date>_<revision>.pdf
```

Examples:
- `FAI_FRAME-F05_S001_2024-01-15_Rev-A.pdf`
- `FAI_WING-INTERFACE_S001_2024-02-20_Rev-B.pdf`
- `FAI_SKIN-PANEL-001_S001_2024-03-10_Rev-A.pdf`

## AS9102 Requirements

### Form 1: Part Number and Engineering Approval Record
- Part number and nomenclature
- Drawing number and revision
- Organization information
- Engineering approval signature
- Quality approval signature

### Form 2: Product Accountability
- List all applicable drawings
- List all specifications
- List all customer requirements
- Document review and approval

### Form 3: Characteristic Accountability
For each characteristic:
- Characteristic number
- Drawing reference
- Specification requirement
- Method of verification (measured, tested, etc.)
- Results (actual measurements)
- Tolerance limits
- Pass/fail status
- Supporting data reference

### Supporting Documentation
- CMM measurement reports
- Material certificates
- Test reports
- Process verification records
- Calibration certificates
- Photographs (as applicable)
- Special process certifications

## FAI Triggers

FAI required for:
- **New part number**: First production unit
- **Design change**: After engineering change
- **Process change**: New manufacturing method
- **Tooling change**: New or modified tooling
- **New supplier**: First article from supplier
- **Production restart**: After 2+ years shutdown
- **Customer request**: As specified in contract

## FAI Process

1. **Plan**: Identify characteristics to verify
2. **Inspect**: Measure per inspection plan
3. **Document**: Complete AS9102 forms
4. **Review**: Engineering and quality review
5. **Approve**: Management approval
6. **Submit**: Customer approval (if required)
7. **File**: Retain records per requirements

## Acceptance Criteria

FAI passes if:
- All characteristics within tolerance
- All supporting documentation complete
- All approvals obtained
- Customer accepts (if applicable)

FAI fails if:
- Any characteristic out of tolerance
- Missing documentation
- Approvals not obtained

## FAI Retention

FAI reports must be:
- Retained indefinitely for critical parts
- Minimum retention: Part lifetime + 10 years
- Readily available for customer review
- Protected and backed up
- Traceable to part serial number

## Related Directories

- **Periodic reports**: [`../PERIODIC/`](../PERIODIC/)
- **CMM reports**: [`../../CMM/REPORTS/`](../../CMM/REPORTS/)
- **Run data**: [`../../RUN_DATA/`](../../RUN_DATA/)
