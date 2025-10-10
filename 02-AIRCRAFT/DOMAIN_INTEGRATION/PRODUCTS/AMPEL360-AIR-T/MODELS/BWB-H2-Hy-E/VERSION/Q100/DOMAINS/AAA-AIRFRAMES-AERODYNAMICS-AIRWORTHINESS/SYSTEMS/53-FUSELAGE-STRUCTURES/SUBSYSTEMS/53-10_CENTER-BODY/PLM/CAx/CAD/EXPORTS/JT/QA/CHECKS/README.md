# CHECKS — Validation Checks and Results

## Purpose

Storage for validation check results, test reports, and quality verification documentation for JT files.

## What to Store

- Automated validation results
- Manual inspection reports
- Checklist completion records
- Test execution logs
- Issue tracking and resolution

## Validation Categories

### File Format Checks
- ✅ File opens in JT2Go without errors
- ✅ Proper JT version (9.5, 10.x)
- ✅ File not corrupted
- ✅ Complete data structure

### Geometry Checks
- ✅ Geometry displays correctly
- ✅ No missing surfaces
- ✅ Proper tessellation
- ✅ Scale and units correct
- ✅ No visual artifacts

### Assembly Checks
- ✅ Assembly structure preserved
- ✅ Component hierarchy correct
- ✅ Part instances positioned correctly
- ✅ Component count matches BOM

### PMI Checks (if applicable)
- ✅ PMI annotations visible
- ✅ Dimensions readable
- ✅ GD&T complete
- ✅ Manufacturing notes present

### Metadata Checks
- ✅ Part number present
- ✅ Revision correct
- ✅ Material specified
- ✅ Mass properties included
- ✅ Custom attributes populated

### Naming Checks
- ✅ Naming convention followed
- ✅ Proper file extension (.jt)
- ✅ Version/revision in filename

## Check Results Format

```
filename: 53-10_FRAME-F01_PN-12345_RevB_20250110.jt
date: 2025-01-10
inspector: J. Smith
status: PASS
issues: None
notes: All checks passed successfully
```

## Related Directories

- [`../`](../) — QA directory
- [`../../REVISIONS/RELEASED/`](../../REVISIONS/RELEASED/) — Approved files
- [`../../INDEX/`](../../INDEX/) — File catalogs
- [`../../README.md`](../../README.md) — JT format overview

## Best Practices

- Check before releasing
- Document all results
- Address failures immediately
- Maintain check history
- Automate where possible
- Periodic re-validation of released files
