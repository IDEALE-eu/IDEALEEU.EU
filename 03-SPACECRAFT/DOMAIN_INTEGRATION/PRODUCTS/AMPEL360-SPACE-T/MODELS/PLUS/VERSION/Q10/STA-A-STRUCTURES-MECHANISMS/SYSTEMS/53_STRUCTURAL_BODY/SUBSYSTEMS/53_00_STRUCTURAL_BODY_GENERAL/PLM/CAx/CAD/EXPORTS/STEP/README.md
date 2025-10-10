# STEP — ISO 10303 STEP Format Exports

## Purpose

This directory contains STEP (ISO 10303) format exports of CAD models. STEP AP242 is the primary neutral format for aerospace 3D data exchange.

## Format Details

### STEP AP242 (ISO 10303-242)
- **Full name**: Product model data for process planning using machining features
- **Primary use**: 3D geometry with PMI (Product Manufacturing Information)
- **Advantages**:
  - Preserves assembly structure
  - Includes GD&T and annotations
  - Industry standard for aerospace
  - Long-term archival stability

## Export Settings

### Recommended Settings
- **Protocol**: AP242
- **Include**: Geometry, assembly structure, attributes, PMI
- **Units**: Millimeters (or as specified)
- **Validation**: Visual exterior surfaces
- **Assembly structure**: Maintain hierarchy

## Naming Convention

```
53_00_<component>_<part-number>_<revision>_<date>.step
```

Examples:
- `53_00_FRAME-F01_PN-12345_RevB_20250110.step`
- `53_00_ASM_STRUCTURAL-BODY_PN-10000_RevA_20250110.step`

## File Organization

Organize files by:
- **Component type**: Parts, assemblies
- **Configuration**: Flight, test, analysis variants
- **Release status**: Draft, released, archived

## Validation

Before committing STEP files:
- [ ] File opens without errors in STEP viewer
- [ ] Geometry matches source CAD model
- [ ] Assembly structure preserved
- [ ] Units correct (millimeters)
- [ ] PMI transferred (if applicable)
- [ ] File size reasonable

## Related Directories

- **Source CAD models**: [`../../MODELS/`](../../MODELS/) and [`../../ASSEMBLIES/`](../../ASSEMBLIES/)
- **Other formats**: [`../IGES/`](../IGES/), [`../JT/`](../JT/), [`../DXF/`](../DXF/)

## Standards

- **ISO 10303-242**: STEP AP242 specification
- **ECSS-E-ST-10C**: Space engineering standards
- **AS9100**: Quality management for aerospace
