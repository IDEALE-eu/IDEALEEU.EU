# SOLIDS — 3D Solid Part Models

## Purpose

This directory contains STEP files for **3D solid B-rep (boundary representation) models** of individual parts. Solid models represent the complete volume and mass of a component.

## What to Store

- **Solid parts**: Complete 3D parametric parts exported as B-rep solids
- **Machined components**: Parts with defined volumes and material removal
- **Sheet metal parts**: Flat patterns and formed solid bodies
- **Cast/molded parts**: Components with material fill volumes
- **Standard parts**: Fasteners, bearings, bushings as solids

## File Naming Convention

Follow the standard naming pattern:
```
<subsystem>_<component>_<part-number>_<revision>_<date>.step
```

Example:
```
53-10_FRAME-F01_PN-12345_RevB_20250110.step
```

## Export Guidelines

When exporting solid models to STEP:
- ✅ Export as **B-rep solids** (not tessellated)
- ✅ Include all visible solid bodies
- ✅ Verify closed volumes (no gaps or openings)
- ✅ Include material properties and mass
- ✅ Export PMI/GD&T if present (or place in [../PMI/](../PMI/))

## Related Directories

- [**../SURFACES/**](../SURFACES/) — Surface-only models and complex geometry
- [**../PMI/**](../PMI/) — Product Manufacturing Information and GD&T annotations
- [**../../ASSEMBLIES/**](../../ASSEMBLIES/) — Multi-part assemblies
- [**../../SCHEMAS/AP242/**](../../SCHEMAS/AP242/) — AP242 protocol files (recommended)
- [**../../REVISIONS/**](../../REVISIONS/) — Revision state management

## Validation

Before committing STEP files:
- [ ] File opens without errors in neutral viewer
- [ ] Geometry is complete and accurate
- [ ] Units are correct (mm or inches)
- [ ] Mass properties calculated correctly
- [ ] File size reasonable (< 100 MB for individual parts)

## References

- Parent directory: [**../**](../)
- Main STEP README: [**../../README.md**](../../README.md)
- Export standards: `00-PROGRAM/STANDARDS/04-CROSS_CUTTING/DATA_EXCHANGE/`
