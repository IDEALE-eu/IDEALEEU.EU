# MODELS — CAD Model Files

## Purpose

This directory contains native and neutral format CAD model files for the 53_00 Structural Body components.

## What to Store

### Native CAD Models
- **Part files**: Individual component models (`.prt`, `.sldprt`, `.CATPart`, etc.)
- **Master models**: Top-level design files with parameters and features
- **Parametric models**: Fully-featured models with design history
- **Reference geometry**: Construction planes, axes, coordinate systems

### Model Types
- **Structural components**: Primary structure elements (frames, stringers, skin panels)
- **Attachment points**: Interface fittings and mounting provisions
- **Loft surfaces**: Outer mold line (OML) and inner mold line (IML) definitions
- **Detail parts**: Brackets, clips, doublers, and reinforcements

## Naming Convention

Use the following naming pattern:
```
<subsystem>_<component>_<part-number>_<version>.<ext>
```

Examples:
- `53_00_FRAME_F01_FWD_v01.CATPart`
- `53_00_SKIN_PANEL_SP-001_v02.prt`
- `53_00_STRINGER_STR-L01_v01.sldprt`

## Organization

Organize models by:
- **Component type**: Frames, stringers, skins, etc.
- **Zone/station**: Forward, center, aft sections
- **Part family**: Related components with similar design

## File Formats

### Native Formats
- **CATIA V5/V6**: `.CATPart`, `.CATProduct`
- **NX (Siemens)**: `.prt`
- **SolidWorks**: `.sldprt`, `.sldasm`
- **Creo (PTC)**: `.prt`, `.asm`

### Best Practices
- Always export to neutral formats (see [`../EXPORTS/`](../EXPORTS/)) for long-term archival
- Document design parameters in model properties or separate parameter file
- Include material specifications in model metadata
- Link to applicable standards in [`../../PLM/EBOM_LINKS.md`](../../EBOM_LINKS.md)

## Version Control

- Use Git LFS for large binary files (> 10 MB)
- Tag major design milestones with version numbers
- Document design changes in commit messages
- Reference related drawings in [`../DRAWINGS/`](../DRAWINGS/)

## Metadata Requirements

Include the following in model properties or accompanying JSON:
- **Part number**: Unique identifier
- **Revision**: Version/revision letter
- **Material**: Material specification (e.g., Al 2024-T3)
- **Mass**: Calculated mass in kg
- **Author**: Designer name/ID
- **Date**: Creation/modification date
- **Status**: Draft, Released, Obsolete

## Quality Checks

Before committing models:
- [ ] Model opens without errors
- [ ] All features rebuild successfully
- [ ] Material properties defined
- [ ] Mass properties calculated
- [ ] Design parameters documented
- [ ] Neutral format export verified
- [ ] File metadata complete

## References

- **Geometry standards**: ECSS-E-ST-32C
- **Data exchange**: [`../EXPORTS/`](../EXPORTS/)
- **Assembly models**: [`../ASSEMBLIES/`](../ASSEMBLIES/)
- **Engineering drawings**: [`../DRAWINGS/`](../DRAWINGS/)
- **EBOM links**: [`../../EBOM_LINKS.md`](../../EBOM_LINKS.md)
