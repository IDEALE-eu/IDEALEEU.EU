# QA — Quality Assurance

## Purpose

This directory contains quality assurance validation results and checks for JT files.

## What to Store

- File validation results
- Quality check reports
- Compliance verification
- Automated test results
- Manual inspection reports

## Subdirectories

- [`CHECKS/`](./CHECKS/) — Validation checks and test results

## Quality Checks

### File Integrity
- File opens without errors
- No corruption or data loss
- Proper file format version
- Complete data structure

### Content Validation
- Geometry displays correctly
- Assembly structure preserved
- PMI visible and complete
- Metadata present and accurate
- Proper units and scale

### Standards Compliance
- Naming convention adherence
- Required properties present
- LOD appropriateness
- Export settings validation

### Visual Quality
- Tessellation quality adequate
- No visual artifacts
- Colors and materials correct
- Annotations readable

## Validation Process

1. **Automated checks**: Run validation scripts
2. **Manual review**: Visual inspection in JT2Go
3. **Metadata verification**: Check properties
4. **Documentation**: Record results
5. **Approval**: Sign-off on quality

## Related Directories

- [`../REVISIONS/RELEASED/`](../REVISIONS/RELEASED/) — Approved files
- [`../SUPPLIERS/PACKAGES/`](../SUPPLIERS/PACKAGES/) — Supplier deliverables
- [`../INDEX/`](../INDEX/) — File catalogs
- [`../README.md`](../README.md) — JT format overview

## Best Practices

- Validate before release
- Document all checks
- Maintain validation scripts
- Track quality metrics
- Address issues promptly
- Archive validation results
