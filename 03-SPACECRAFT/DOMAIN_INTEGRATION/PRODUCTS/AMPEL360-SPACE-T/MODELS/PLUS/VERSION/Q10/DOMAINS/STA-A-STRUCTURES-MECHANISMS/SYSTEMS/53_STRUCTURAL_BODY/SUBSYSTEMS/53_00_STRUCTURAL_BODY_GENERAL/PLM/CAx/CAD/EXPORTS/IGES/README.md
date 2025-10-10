# IGES — Initial Graphics Exchange Specification Exports

## Purpose

This directory contains IGES format exports of CAD models. IGES is a legacy 3D format used for compatibility with older CAD systems and certain CAM applications.

## Format Details

### IGES 5.3
- **Full name**: Initial Graphics Exchange Specification
- **Primary use**: 3D surfaces, wireframe, and solid models
- **Use cases**:
  - Legacy CAD system compatibility
  - CAM system input
  - Supplier requirements (when STEP not supported)

## Export Settings

### Recommended Settings
- **Version**: IGES 5.3
- **Entity types**: Surfaces and solids, trimmed surfaces
- **Units**: Millimeters (or as specified)
- **Validation**: Check for surface gaps

## Naming Convention

```
53_00_<component>_<part-number>_<revision>_<date>.igs
```

Examples:
- `53_00_FRAME-F01_PN-12345_RevB_20250110.igs`
- `53_00_SKIN-PANEL_PN-12346_RevA_20250110.igs`

## Limitations

IGES has limitations compared to STEP:
- No PMI (GD&T) preservation
- Less robust assembly structure
- Potential geometry translation issues
- Not recommended for long-term archival

## When to Use IGES

Use IGES only when:
- Partner/supplier specifically requests it
- CAM system requires IGES input
- Legacy system compatibility needed
- STEP is not supported by recipient

## Validation

Before committing IGES files:
- [ ] File opens without errors
- [ ] Geometry visually matches source
- [ ] No missing surfaces or gaps
- [ ] Units correct
- [ ] File size reasonable

## Related Directories

- **Source CAD models**: [`../../MODELS/`](../../MODELS/)
- **Preferred format**: [`../STEP/`](../STEP/) — Use STEP when possible
