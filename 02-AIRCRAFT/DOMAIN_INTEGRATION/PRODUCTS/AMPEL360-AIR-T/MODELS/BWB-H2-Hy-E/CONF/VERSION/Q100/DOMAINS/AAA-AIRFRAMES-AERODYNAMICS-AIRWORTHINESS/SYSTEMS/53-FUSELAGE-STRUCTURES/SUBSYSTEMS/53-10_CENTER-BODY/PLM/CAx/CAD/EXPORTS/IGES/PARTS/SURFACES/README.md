# SURFACES — NURBS and Trimmed Surface IGES Exports

## Purpose

This directory contains IGES exports of surface geometries, particularly NURBS (Non-Uniform Rational B-Splines) and trimmed parametric surfaces.

## Content

Store IGES files (`.igs` or `.iges`) for:
- **NURBS surfaces**: Complex parametric surfaces
- **Trimmed surfaces**: Surfaces with boundary curves
- **Class-A surfaces**: High-quality exterior surfaces (OML)
- **Lofted surfaces**: Surfaces created by lofting profiles
- **Swept surfaces**: Surfaces from sweep operations
- **Complex curvature**: Surfaces requiring precise definition

## File Naming Convention

```
<subsystem>_<component>_<part-number>_<revision>_<date>.igs
```

**Examples:**
- `53-10_SKIN-PANEL_PN-12346_RevA_20250110.igs`
- `53-10_SURFACE_OML_PN-98765_RevA_20250110.igs`
- `53-10_FAIRING_PN-45678_RevB_20250110.igs`

## Export Requirements

When exporting surfaces to IGES:
- ✅ Use IGES version 5.3
- ✅ Select trimmed surface entity type (typically entity 144)
- ✅ Include trim curves and boundaries
- ✅ Check surface normals (outward-facing)
- ✅ Use millimeters for units
- ✅ Set surface tolerance to 0.001 mm

## CAD System Export Paths

- **CATIA V5/V6**: File → Export → IGES → Select "Trimmed surfaces"
- **Siemens NX**: File → Export → IGES → Type: "Trimmed parametric surfaces"
- **SolidWorks**: File → Save As → IGES → Options: "Trimmed surfaces"
- **Creo (PTC)**: File → Save a Copy → IGES → Entities: "Surfaces"

## Use Cases

### Manufacturing
- Sheet metal flat patterns
- Mold surfaces for composites
- Reference surfaces for CNC programming
- Tooling surface definitions

### Aerodynamics
- Outer Mold Line (OML) surfaces
- Wing and fuselage contours
- Fairing and blending surfaces
- Flow surface definitions

### Class-A Surfacing
- Exterior appearance surfaces
- High-quality aesthetic surfaces
- Surfaces requiring continuity (G2, G3)

## Validation Checklist

Before committing IGES surface files:
- [ ] All surfaces imported correctly
- [ ] Trim boundaries are correct
- [ ] No gaps between adjacent surfaces
- [ ] Surface normals oriented correctly
- [ ] Continuity maintained (if applicable)
- [ ] Units and scale verified

## Related Directories

- **Parent**: [`../`](../) — All PARTS exports
- **Alternatives**: [`../SOLIDS/`](../SOLIDS/) — Solid body geometry
- **Alternatives**: [`../CURVES/`](../CURVES/) — Boundary curves only
- **Source**: [`../../../MODELS/`](../../../MODELS/) — Native CAD models

## Best Practices

- Export high-quality surfaces without simplification
- Include all trim curves and boundaries
- Verify surface continuity at boundaries
- Document surface quality requirements (G1, G2, G3)
- Test with recipient's CAD system if possible

## Surface Quality Notes

**Surface Continuity Levels:**
- **G0**: Position continuity (touching)
- **G1**: Tangent continuity (smooth blend)
- **G2**: Curvature continuity (Class-A)
- **G3**: Acceleration continuity (highest quality)

IGES preserves surface geometry but may not explicitly maintain continuity metadata. Verify after import.
