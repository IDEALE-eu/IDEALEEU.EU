# EXPORTS — Neutral Format Exports

## Purpose

This directory contains neutral format exports of the top-level assembly for data exchange with external systems and partners.

## Export Formats

### Available Formats
- **[STEP/](./STEP/)** — ISO 10303 STEP format (primary exchange)
- **[JT/](./JT/)** — Lightweight visualization format
- **[IGES/](./IGES/)** — Legacy exchange format (if required)

## Format Selection

### STEP (Recommended)
- **Use for**: CAD exchange, archival, analysis
- **Advantages**: Complete geometry, PMI support, assembly structure
- **Standard**: ISO 10303-242 (AP242)

### JT
- **Use for**: Visualization, collaboration, reviews
- **Advantages**: Lightweight, fast loading, web-ready
- **Standard**: ISO 14306

### IGES
- **Use for**: Legacy systems only
- **Limitations**: No PMI, limited assembly structure
- **Note**: Use STEP when possible

## Export Quality

### Before Export
- [ ] Model is complete and error-free
- [ ] Units are correct (mm or inches)
- [ ] Assembly structure is valid
- [ ] Reference geometry included
- [ ] Material properties assigned

### After Export
- [ ] File opens without errors
- [ ] Geometry is complete
- [ ] Assembly structure preserved
- [ ] Dimensions are accurate
- [ ] File size is reasonable

## Naming Convention

```
53-10_ASM_CENTER-BODY_<config>_<version>.<ext>
```

Examples:
- `53-10_ASM_CENTER-BODY_COMPLETE_v01.stp`
- `53-10_ASM_CENTER-BODY_SIMPLIFIED_v01.jt`
- `53-10_ASM_CENTER-BODY_LIGHTWEIGHT_v01.igs`

## Export Workflow

1. **Prepare model**: Verify model is ready
2. **Export**: Use CAD system export function
3. **Validate**: Check exported file quality
4. **Document**: Record export parameters
5. **Commit**: Add to version control

## Related Directories

- **Assembly**: [`../ASM/`](../ASM/) — Source assembly files
- **Configurations**: [`../CONFIGURATIONS/`](../CONFIGURATIONS/) — Export configurations
