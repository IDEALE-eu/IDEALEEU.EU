# CURVES — Wireframe and Curve IGES Exports

## Purpose

This directory contains IGES exports of wireframe geometry, curves, and construction elements used for reference and definition.

## Content

Store IGES files (`.igs` or `.iges`) for:
- **Wireframe geometry**: Lines, arcs, splines
- **Reference curves**: Guide curves, section profiles
- **Boundary curves**: Trim boundaries, edge definitions
- **Construction geometry**: Datum curves, construction lines
- **Intersection curves**: Surface intersection definitions
- **2D profiles**: Cross-sections, frame definitions

## File Naming Convention

```
<subsystem>_<component>_<part-number>_<revision>_<date>.igs
```

**Examples:**
- `53-10_FRAME-PROFILE_PN-78901_RevA_20250110.igs`
- `53-10_INTERSECTION_PN-78902_RevA_20250110.igs`
- `53-10_REFERENCE-CURVES_PN-78903_RevB_20250110.igs`

## Export Requirements

When exporting curves to IGES:
- ✅ Use IGES version 5.3
- ✅ Export curve entities (lines, arcs, splines)
- ✅ Include all control points for splines
- ✅ Use millimeters for units
- ✅ Set curve tolerance to 0.001 mm

## Curve Entity Types

IGES supports various curve types:
- **Line** (Entity 110): Straight line segments
- **Circular Arc** (Entity 100): Arc segments
- **Composite Curve** (Entity 102): Connected curve segments
- **Conic Arc** (Entity 104): Ellipse, parabola, hyperbola
- **Rational B-Spline Curve** (Entity 126): General parametric curves

## Use Cases

### Reference Geometry
- Frame station lines
- Waterlines and buttock lines
- Reference axes and datums
- Construction geometry for modeling

### Manufacturing
- CNC toolpath definitions
- Wire EDM paths
- Laser cutting profiles
- Inspection paths

### Analysis
- Section cut locations
- Measurement reference lines
- Coordinate system definitions

## Validation Checklist

Before committing IGES curve files:
- [ ] All curves imported correctly
- [ ] Curve continuity preserved
- [ ] Control points accurate
- [ ] Curve direction correct
- [ ] Units verified
- [ ] No missing segments

## Related Directories

- **Parent**: [`../`](../) — All PARTS exports
- **Alternatives**: [`../SURFACES/`](../SURFACES/) — Surface geometry
- **Alternatives**: [`../SOLIDS/`](../SOLIDS/) — Solid geometry
- **Source**: [`../../../MODELS/`](../../../MODELS/) — Native CAD models

## Best Practices

- Export curves in logical groups
- Maintain curve connectivity where needed
- Document curve purpose and usage
- Include construction curves if needed for downstream work
- Verify curve direction and orientation

## Integration Notes

Wireframe curves are often used in combination with:
- Surface modeling (trim boundaries, guide curves)
- Assembly definitions (reference geometry)
- Inspection and measurement (datum curves)
- Manufacturing (toolpath references)

Export curves separately when:
- They serve as reference for multiple parts
- Surface models need boundary definitions
- Manufacturing requires standalone profiles
- Inspection requires measurement references
