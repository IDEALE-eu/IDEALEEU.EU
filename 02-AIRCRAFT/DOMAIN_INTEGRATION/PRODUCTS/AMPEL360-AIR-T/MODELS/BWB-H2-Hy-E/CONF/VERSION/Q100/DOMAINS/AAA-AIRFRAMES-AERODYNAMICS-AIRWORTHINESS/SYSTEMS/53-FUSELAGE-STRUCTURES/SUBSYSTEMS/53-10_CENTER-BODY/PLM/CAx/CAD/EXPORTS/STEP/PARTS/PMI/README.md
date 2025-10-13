# PMI — Product and Manufacturing Information

## Purpose

This directory contains STEP files with **Product and Manufacturing Information (PMI)** including geometric dimensioning and tolerancing (GD&T), annotations, and manufacturing specifications.

## What to Store

- **GD&T annotations**: Datums, feature control frames, tolerances
- **Dimensions**: Critical dimensions and measurements
- **Surface finish**: Surface texture and roughness specifications
- **Notes and callouts**: Manufacturing and inspection notes
- **Validation models**: Inspection and quality control references

## File Naming Convention

Follow the standard naming pattern:
```
<subsystem>_<component>_<part-number>_<revision>_<date>.step
```

Example:
```
53-10_FRAME-F01_PMI_PN-12345_RevB_20250110.step
```

## PMI Content Types

### Geometric Dimensioning and Tolerancing (GD&T)
- Datum reference frames
- Feature control frames
- Position, profile, parallelism tolerances
- Form and orientation controls

### Annotations
- Critical dimensions with tolerances
- Material specifications
- Surface finish symbols (Ra, Rz values)
- Process notes and manufacturing instructions
- Inspection requirements

### Validation Data
- Measurement points for CMM inspection
- Quality control checkpoints
- First article inspection (FAI) requirements

## Export Guidelines

When exporting PMI to STEP AP242:
- ✅ Use **STEP AP242** (not AP214) for full PMI support
- ✅ Include semantic PMI (not just visual annotations)
- ✅ Verify GD&T exports correctly with datums
- ✅ Include associated geometry references
- ✅ Test import in target inspection software

## Related Directories

- [**../SOLIDS/**](../SOLIDS/) — 3D solid models (may include PMI)
- [**../SURFACES/**](../SURFACES/) — Surface models
- [**../../QA/CHECKS/**](../../QA/CHECKS/) — Quality assurance validation
- [**../../SCHEMAS/AP242/**](../../SCHEMAS/AP242/) — AP242 files with full PMI support
- [**../../TEMPLATES/**](../../TEMPLATES/) — PMI templates and standards

## CAD System Settings

### CATIA V5/V6
- File → Export → STEP AP242
- ✅ Enable "Export PMI"
- ✅ Include functional and annotation sets

### Siemens NX
- File → Export → STEP AP242
- ✅ Enable "Export PMI"
- ✅ Include product structure

### SolidWorks
- File → Save As → STEP AP242
- ✅ Include dimensions and tolerances

## Validation

Before committing PMI files:
- [ ] All GD&T elements export correctly
- [ ] Datums are properly defined
- [ ] Tolerances are readable and accurate
- [ ] Surface finish symbols preserved
- [ ] File imports correctly in inspection software

## References

- Parent directory: [**../**](../)
- Main STEP README: [**../../README.md**](../../README.md)
- GD&T standards: ASME Y14.5, ISO 1101
- PMI best practices: `00-PROGRAM/STANDARDS/04-CROSS_CUTTING/DATA_EXCHANGE/`
