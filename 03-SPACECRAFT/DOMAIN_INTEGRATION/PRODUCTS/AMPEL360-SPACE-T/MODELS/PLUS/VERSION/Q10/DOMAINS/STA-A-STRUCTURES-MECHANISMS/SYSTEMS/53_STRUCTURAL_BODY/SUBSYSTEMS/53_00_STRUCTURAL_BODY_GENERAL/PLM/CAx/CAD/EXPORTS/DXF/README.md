# DXF — Drawing Exchange Format Exports

## Purpose

This directory contains DXF format exports for 2D drawings and profiles used in manufacturing processes.

## Format Details

### DXF (Drawing Exchange Format)
- **Full name**: AutoCAD Drawing Exchange Format
- **Primary use**: 2D geometry for manufacturing
- **Use cases**:
  - CNC programming
  - Laser/waterjet cutting
  - Sheet metal flat patterns
  - Inspection overlays

## Export Settings

### Recommended Settings
- **Version**: DXF 2013 or later
- **Units**: Millimeters (or as specified)
- **Layers**: Organize by feature type
- **2D geometry**: Profiles, dimensions, annotations

## Naming Convention

```
53_00_<component>_<part-number>_<type>_<revision>_<date>.dxf
```

Examples:
- `53_00_SKIN-PANEL_PN-12346_FLAT-PATTERN_RevA_20250110.dxf`
- `53_00_BRACKET_PN-12347_PROFILE_RevB_20250110.dxf`

## Content Types

### Flat Patterns
- Sheet metal flat patterns
- Bend lines and annotations
- Material specifications

### Profiles
- 2D cross-sections
- Extrusion profiles
- Cutting templates

### Inspection
- Inspection overlays
- Dimensional verification templates
- Quality control gauges

## Validation

Before committing DXF files:
- [ ] File opens in AutoCAD/DraftSight
- [ ] Geometry accurate to source
- [ ] Units correct
- [ ] Layers properly organized
- [ ] Annotations readable

## Related Directories

- **Source drawings**: [`../../DRAWINGS/`](../../DRAWINGS/)
- **3D geometry**: [`../STEP/`](../STEP/)
- **Manufacturing**: [`../../../CAM/`](../../../CAM/)
