# CHECKS — Quality Check Reports

## Purpose
Quality assurance check reports, validation results, and verification documentation for DXF files.

## Contents
- Export validation reports
- Geometry verification results
- Dimensional inspection reports
- Manufacturing feasibility assessments
- Pre-release check records
- Non-conformance reports (NCR)

## Check Types

### Export Validation
Verify file integrity:
- File opens without errors in target software
- All layers exported correctly
- Geometry complete and accurate
- Dimensions and text readable
- Proper scaling and units
- No corruption or missing data

### Geometry Verification
Compare to source model:
- Critical dimensions match source
- Geometry not distorted
- Features correctly represented
- Closed contours where required
- No duplicate geometry
- Proper orientation

### Manufacturing Feasibility
Assess manufacturability:
- Features can be produced
- Tolerances are achievable
- Process requirements clear
- Material specifications adequate
- Tooling requirements understood
- Cost-effective to manufacture

### Documentation Completeness
Verify supporting information:
- Part number and revision correct
- Material callouts present
- Process notes included
- Tolerance specifications clear
- Special requirements documented
- Contact information provided

## Check Report Template

### Header Information
- **Check date**: YYYY-MM-DD
- **Checker name**: Name and role
- **Part number**: Full part number
- **Revision**: Current revision
- **File name**: DXF file name
- **Check type**: Export, geometry, manufacturing, etc.

### Checklist Items
For each item:
- [ ] **Item description**
- **Status**: Pass / Fail / N/A
- **Notes**: Comments and observations
- **Action required**: If fail, what action needed

### Results Summary
- **Overall status**: Pass / Fail / Conditional
- **Critical issues**: List any critical problems
- **Minor issues**: List non-critical items
- **Recommendations**: Improvement suggestions

### Approval
- **Checker signature**: Checked by
- **Date**: Check date
- **Reviewer signature**: Reviewed by (if required)
- **Date**: Review date

## File Naming
```
QA-CHECK_<part-number>_<check-type>_<date>.pdf
```

Examples:
- `QA-CHECK_53-10-FRM01_EXPORT_20250110.pdf`
- `QA-CHECK_53-10-SKIN10_GEOMETRY_20250112.pdf`
- `QA-CHECK_BATCH-NEST-001_VALIDATION_20250115.pdf`

## Quality Standards

### Critical Checks (Must Pass)
- File opens without errors
- Critical dimensions within tolerance
- Geometry complete (no missing elements)
- Manufacturing process feasible
- Safety-critical features correct

### Important Checks (Should Pass)
- All layers organized properly
- Text and annotations clear
- Minor dimensions within tolerance
- Documentation complete
- Naming conventions followed

### Nice-to-Have (May Pass)
- Optimized for file size
- Best practice layer structure
- Comprehensive annotations
- Efficient geometry representation

## Non-Conformance Handling

### When Check Fails
1. Document the non-conformance clearly
2. Assess severity: Critical, Major, Minor
3. Identify root cause
4. Determine corrective action
5. Assign responsibility for correction
6. Set target completion date
7. Re-check after correction

### NCR Documentation
For significant issues:
- NCR number and date
- Description of non-conformance
- Impact assessment
- Root cause analysis
- Corrective action
- Preventive action
- Verification of correction
- Closure sign-off

## Batch Checking
For multiple similar parts:
- Sample-based approach acceptable
- Document sampling plan
- Check representative samples
- Extrapolate to batch
- Full check if issues found

## Related Directories
- **[../../PARTS/](../../PARTS/)** — Parts being checked
- **[../../REVISIONS/RELEASED/](../../REVISIONS/RELEASED/)** — Released files
- **[../../SUPPLIERS/PACKAGES/](../../SUPPLIERS/PACKAGES/)** — Supplier packages

## Check Frequency

### Mandatory Checks
- Before first release (Rev A)
- After significant design changes
- Before supplier package release
- After CAD system changes/upgrades
- For critical/safety parts (every revision)

### Recommended Checks
- Periodic audit of released files
- Sample checks of routine exports
- After process changes
- Training verification

## Continuous Improvement
Track and analyze:
- Common failure modes
- Process improvement opportunities
- Training needs
- Tool or process updates needed
- Best practices to document

## Archive and Retention
- Keep check reports with released files
- Minimum retention: Product lifetime + 10 years
- Link to configuration management
- Support audits and investigations
- Maintain traceability

## Best Practices
- Use standard checklists
- Independent checking when possible
- Document all findings clearly
- Timely resolution of issues
- Learn from failures
- Regular process audits
- Feedback to designers
