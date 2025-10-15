# QA — Quality Assurance

## Purpose
Quality assurance documentation and verification files for DXF exports.

## Contents
- **[CHECKS/](CHECKS/)** — Quality check reports and validation results

## Organization
Quality documentation organized by:
- Check type (geometry, dimension, export)
- Part or assembly
- Date and checker
- Pass/fail status

## File Naming Convention
```
QA-CHECK_<part>_<check-type>_<date>.pdf
```

Examples:
- `QA-CHECK_53-10-FRM01_GEOMETRY_20250110.pdf`
- `QA-CHECK_BATCH-001_EXPORT_20250110.pdf`
- `QA-CHECK_NEST-JOB-005_VALIDATION_20250112.pdf`

## Quality Requirements

### DXF Export Validation
Verify before release:
- [ ] File opens without errors
- [ ] All geometry present and correct
- [ ] Dimensions accurate and readable
- [ ] Layers properly organized
- [ ] Units correct (mm or inches)
- [ ] Scale verified (1:1)
- [ ] Text and annotations clear
- [ ] No duplicate or overlapping geometry
- [ ] Closed contours where required
- [ ] Naming convention followed

### Manufacturing Verification
Confirm:
- [ ] Geometry suitable for manufacturing process
- [ ] Features are manufacturable
- [ ] Tolerances achievable
- [ ] Material specifications clear
- [ ] Process requirements defined
- [ ] Inspection requirements specified

### Documentation Completeness
Ensure:
- [ ] Part number and revision correct
- [ ] Material specification included
- [ ] Process notes present
- [ ] Tolerance callouts clear
- [ ] Surface finish specified (if applicable)
- [ ] Contact information provided

## Quality Check Process
1. **Export validation**: Check file integrity
2. **Geometry verification**: Validate against source
3. **Dimension check**: Verify critical dimensions
4. **Manufacturing review**: Confirm feasibility
5. **Documentation review**: Ensure completeness
6. **Sign-off**: Formal approval

## Related Directories
- **[../PARTS/](../PARTS/)** — Part files to be checked
- **[../REVISIONS/RELEASED/](../REVISIONS/RELEASED/)** — Released files
- **[../SUPPLIERS/PACKAGES/](../SUPPLIERS/PACKAGES/)** — Supplier packages

## Guidelines
- Perform QA checks before release
- Document all checks and results
- Address non-conformances before release
- Maintain check records
- Regular audit of QA process
- Continuous improvement

## Best Practices
- Formal QA checklist for all files
- Independent verification when possible
- Test in recipient's software if available
- Document and resolve all issues
- Regular process audits
- Lessons learned documentation
