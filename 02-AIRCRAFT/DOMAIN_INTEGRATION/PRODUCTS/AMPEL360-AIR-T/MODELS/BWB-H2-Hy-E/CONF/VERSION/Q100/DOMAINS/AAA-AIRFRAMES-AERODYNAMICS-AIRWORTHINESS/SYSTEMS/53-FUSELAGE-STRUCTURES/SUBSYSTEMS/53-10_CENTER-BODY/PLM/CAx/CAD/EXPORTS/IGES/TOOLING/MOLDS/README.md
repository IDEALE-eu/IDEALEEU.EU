# MOLDS — Mold and Cavity Geometry IGES Exports

## Purpose

This directory contains IGES exports of mold geometries, cavity surfaces, and tooling definitions for composite layup and manufacturing processes.

## Content

Store IGES files (`.igs` or `.iges`) for:
- **Composite molds**: Layup mold surfaces
- **Cavity tooling**: Mold cavities and cores
- **Female molds**: Negative surface molds
- **Male molds**: Positive surface mandrels
- **Forming tools**: Sheet metal forming dies
- **Tool surfaces**: Reference surfaces for tool design

## File Naming Convention

```
<subsystem>_MOLD_<component>_<tool-number>_<revision>_<date>.igs
```

**Examples:**
- `53-10_MOLD_SKIN-PANEL-01_TL-5001_RevA_20250110.igs`
- `53-10_MOLD_FRAME-F01_TL-5002_RevB_20250110.igs`
- `53-10_MOLD_FAIRING_TL-5003_RevA_20250110.igs`

## Export Requirements

When exporting mold geometry to IGES:
- ✅ Use IGES version 5.3
- ✅ Export high-quality surface geometry
- ✅ Include all mold surfaces and cavities
- ✅ Verify surface normals (typically inward for cavities)
- ✅ Use millimeters for units
- ✅ Set tight tolerance: 0.001 mm or better

## Mold Surface Types

### Composite Molds
- **Layup surfaces**: Surface for composite part layup
- **Tool reference**: Datum surfaces for tool positioning
- **Trim edges**: Perimeter trim definitions
- **Core surfaces**: Internal mandrel surfaces

### Metal Forming Molds
- **Die surfaces**: Forming die cavity surfaces
- **Punch surfaces**: Punch geometry
- **Draw dies**: Sheet metal drawing dies
- **Blank holders**: Blank holder surfaces

## Quality Requirements

Mold surfaces require high accuracy:
- ✅ Class-A surface quality (G2 or G3 continuity)
- ✅ Smooth transitions (no sharp edges unless intentional)
- ✅ Accurate dimensions (critical for part fit)
- ✅ Proper surface orientation
- ✅ Clean surface boundaries

## Validation Checklist

Before committing mold IGES files:
- [ ] Surface quality verified (no gaps, overlaps)
- [ ] Surface normals correct
- [ ] Dimensions accurate
- [ ] Parting lines defined
- [ ] Draft angles verified (if applicable)
- [ ] Scale confirmed (1:1)
- [ ] File opens in CAM system

## Related Directories

- **Parent**: [`../`](../) — All TOOLING
- **Fixtures**: [`../FIXTURES/`](../FIXTURES/) — Fixturing tooling
- **Jigs**: [`../JIGS/`](../JIGS/) — Assembly jigs
- **Parts**: [`../../PARTS/`](../../PARTS/) — Part geometry (for reference)
- **Source**: [`../../../MODELS/`](../../../MODELS/) — Native CAD tooling models

## Best Practices

- Export mold surfaces with sufficient quality for manufacturing
- Include trim edges and parting lines
- Document mold orientation and setup
- Verify surface continuity at boundaries
- Test import in recipient's CAM or tooling system
- Provide both surface and solid representations when possible

## Manufacturing Notes

When providing mold IGES files:
- **Include**: Mold surface, parting line, trim edges
- **Document**: Material removal direction, draft angles
- **Specify**: Surface finish requirements
- **Reference**: Part geometry for fit verification
- **Coordinate**: With tooling design and manufacturing teams

## CAM Integration

Mold IGES files are typically used for:
- CNC milling of mold cavities
- EDM electrode design
- Surface finishing operations
- Mold inspection and validation
- Tool path generation

Ensure exported geometry is compatible with downstream CAM systems.
