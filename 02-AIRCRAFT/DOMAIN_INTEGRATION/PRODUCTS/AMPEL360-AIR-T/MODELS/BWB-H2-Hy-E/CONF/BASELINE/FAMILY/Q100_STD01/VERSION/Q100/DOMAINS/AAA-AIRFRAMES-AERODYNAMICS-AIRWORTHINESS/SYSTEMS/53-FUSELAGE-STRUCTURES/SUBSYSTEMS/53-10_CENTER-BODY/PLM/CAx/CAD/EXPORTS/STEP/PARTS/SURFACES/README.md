# SURFACES — Surface Models and Complex Geometry

## Purpose

This directory contains STEP files for **surface-only models** including complex surfaces, lofts, and Class-A surfaces used in aerodynamic design and styling.

## What to Store

- **Class-A surfaces**: High-quality aerodynamic or aesthetic surfaces
- **Lofted surfaces**: Complex surface transitions and blends
- **Wireframe geometry**: Curves and edges for surface construction
- **Trimmed surfaces**: Bounded and trimmed surface patches
- **Reference geometry**: Master surfaces for downstream modeling

## File Naming Convention

Follow the standard naming pattern:
```
<subsystem>_<component>_<part-number>_<revision>_<date>.step
```

Example:
```
53-10_SKIN-OUTER_PN-12346_RevA_20250110.step
```

## Export Guidelines

When exporting surface models to STEP:
- ✅ Export as **NURBS surfaces** (not tessellated)
- ✅ Include trimming curves and boundaries
- ✅ Preserve surface continuity (G0, G1, G2, G3)
- ✅ Include construction curves if needed
- ✅ Verify surface quality and smoothness

## Use Cases

- **Aerodynamic analysis**: Outer mold line (OML) surfaces for CFD
- **Tooling design**: Master surfaces for mold/die creation
- **Class-A styling**: High-quality visible surfaces
- **Interface definitions**: Mating surfaces between components
- **Lofting templates**: Reference geometry for complex shapes

## Related Directories

- [**../SOLIDS/**](../SOLIDS/) — 3D solid part models
- [**../PMI/**](../PMI/) — Product Manufacturing Information
- [**../../TOOLING/**](../../TOOLING/) — Tooling and mold designs using these surfaces
- [**../../SCHEMAS/AP242/**](../../SCHEMAS/AP242/) — AP242 protocol files
- [**../../ZONES/**](../../ZONES/) — Zone-specific surface organization

## Validation

Before committing STEP files:
- [ ] Surfaces are continuous and smooth
- [ ] No gaps or overlaps in surface patches
- [ ] Trimming curves are accurate
- [ ] Surface quality meets requirements (G1, G2, etc.)
- [ ] File opens correctly in target CAD systems

## References

- Parent directory: [**../**](../)
- Main STEP README: [**../../README.md**](../../README.md)
- Surface quality standards: `00-PROGRAM/STANDARDS/04-CROSS_CUTTING/DATA_EXCHANGE/`
