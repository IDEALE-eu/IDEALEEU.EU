# CHECKS — Quality Assurance and Validation

## Purpose

This directory contains quality assurance records, validation reports, and verification results for IGES exports to ensure geometry accuracy and quality.

## Content

Store files related to:
- **Import verification**: Test import results in various CAD systems
- **Geometry validation**: Checks for completeness and accuracy
- **Dimension verification**: Critical dimension measurements
- **Comparison reports**: Before/after export comparisons
- **Issue logs**: Documented problems and resolutions
- **Quality metrics**: Export quality statistics and trends

## File Types

Common files in this directory:
- **Test reports**: IGES import test results (PDF, DOCX)
- **Screenshots**: Visual verification screenshots (PNG, JPG)
- **Comparison files**: Geometry comparison results
- **Checklists**: Completed validation checklists (PDF)
- **Issue logs**: Problem tracking logs (XLSX, CSV)
- **Metrics**: Quality metrics and dashboards (XLSX, PDF)

## File Naming Convention

```
QA_<check-type>_<file-description>_<date>.<ext>
```

**Examples:**
- `QA_IMPORT-TEST_CATIA-V5_20250110.pdf`
- `QA_DIMENSION-CHECK_FRAME-F01_20250110.xlsx`
- `QA_COMPARISON_EXPORT-vs-SOURCE_20250110.pdf`

## Validation Checklist

Standard validation checks for IGES exports:

### Import Verification
- [ ] File opens without errors in target CAD system
- [ ] All geometry imported correctly
- [ ] No missing surfaces or solids
- [ ] No invalid entities or warnings
- [ ] File size reasonable

### Geometry Validation
- [ ] All surfaces present and closed (if applicable)
- [ ] Surface normals oriented correctly
- [ ] No gaps, overlaps, or discontinuities
- [ ] Trim boundaries correct
- [ ] Wireframe complete

### Dimension Verification
- [ ] Critical dimensions measured and verified
- [ ] Hole locations accurate
- [ ] Overall envelope correct
- [ ] Interface dimensions match ICD
- [ ] Tolerances within specification

### Metadata Verification
- [ ] Units correct (mm or inches)
- [ ] Scale 1:1 (no unintended scaling)
- [ ] Coordinate system correct
- [ ] File naming convention followed
- [ ] Revision designation correct

## Quality Assurance Process

1. **Pre-export**: Validate source CAD model
2. **Export**: Use standardized export settings
3. **Visual check**: Quick visual inspection
4. **Import test**: Test import in target system(s)
5. **Dimension check**: Verify critical dimensions
6. **Comparison**: Compare exported vs. source geometry
7. **Documentation**: Record results
8. **Issue resolution**: Fix any problems found
9. **Re-validation**: Re-check after corrections
10. **Approval**: Sign off on quality

## Test Matrix

Maintain test matrix for IGES exports:

| CAD System | Version | Import Test | Pass/Fail | Issues | Notes |
|------------|---------|-------------|-----------|--------|-------|
| CATIA V5 | R28 | ✓ | Pass | None | Import successful |
| CATIA V6 | R2020x | ✓ | Pass | None | Import successful |
| Siemens NX | NX 12 | ✓ | Pass | Minor | Surface trim issues |
| SolidWorks | 2021 | ✓ | Pass | None | Import successful |
| Creo | 7.0 | ✓ | Pass | None | Import successful |

## Related Directories

- **Parent**: [`../`](../) — Root IGES directory
- **Released**: [`../REVISIONS/RELEASED/`](../REVISIONS/RELEASED/) — Released files being validated
- **Draft**: [`../REVISIONS/DRAFT/`](../REVISIONS/DRAFT/) — Draft files for early validation
- **Source**: [`../../MODELS/`](../../MODELS/) — Source CAD models for comparison

## Common Issues

Track and document common issues:

### Import Errors
- **Issue**: File won't open in CAD system
- **Cause**: Unsupported IGES entities or version
- **Solution**: Re-export with compatible settings

### Missing Geometry
- **Issue**: Parts or surfaces missing after import
- **Cause**: Export filter settings or layer visibility
- **Solution**: Verify all layers visible before export

### Scale Problems
- **Issue**: Geometry imported at wrong scale
- **Cause**: Unit mismatch (mm vs. inches)
- **Solution**: Verify unit setting in IGES global section

### Surface Quality
- **Issue**: Surfaces have gaps or poor quality
- **Cause**: Tight tolerance or complex geometry
- **Solution**: Adjust export tolerance or simplify geometry

## Quality Metrics

Track quality metrics:
- **First-pass success rate**: % files passing validation first time
- **Issue frequency**: Number of issues per file
- **CAD system compatibility**: Pass rate by CAD system
- **Resolution time**: Average time to fix issues
- **Critical dimension accuracy**: Dimensional verification results

## Tools and Software

Quality assurance tools used:
- **CAD viewers**: FreeCAD, eDrawings, IDA-STEP
- **Comparison tools**: Spatial Analyzer, GOM Inspect
- **Dimension tools**: CAD measuring functions
- **Validation scripts**: Custom validation scripts (if any)

## Best Practices

- Test import in multiple CAD systems
- Verify critical dimensions always
- Document all issues and resolutions
- Maintain test matrix for compatibility
- Use standardized checklists
- Archive validation records
- Track quality trends
- Continuous improvement based on metrics

## Validation Report Template

Standard validation report should include:
- File identification (name, revision, date)
- Test date and tester name
- CAD systems tested
- Checklist results
- Issues found (if any)
- Dimensional verification results
- Screenshots or evidence
- Pass/fail determination
- Approver signature

## Continuous Improvement

Use QA data to:
- Identify recurring issues
- Improve export procedures
- Update export settings
- Train personnel
- Enhance validation process
- Reduce errors
- Improve first-pass success rate
