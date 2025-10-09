# PART — Individual Component Drawings

## Purpose

This directory contains part drawings for individual components of the 53-10 Center Body subsystem.

## What to Store

### Part Drawing Types
- **Detail part drawings**: Individual structural components (frames, stringers, clips)
- **Machined parts**: CNC machined fittings, brackets, and attachments
- **Sheet metal parts**: Formed skin panels, brackets, doublers
- **Composite parts**: Composite layup drawings with ply schedules
- **Fabricated parts**: Welded or brazed assemblies treated as parts

## Content Requirements

### Mandatory Information
- **Geometric dimensions**: All manufacturing dimensions with tolerances
- **Material specification**: Material grade, form, and condition
- **Surface finish**: Roughness values (Ra, Rz) and coating specifications
- **Heat treatment**: Process specifications and acceptance criteria
- **GD&T**: Geometric dimensioning and tolerancing per ASME Y14.5
- **Datums**: Reference datum system (A, B, C)
- **Notes**: Manufacturing notes, inspection requirements, special processes

## Naming Convention

```
53-10_DWG_PART_<component-name>_<drawing-number>_<sheet>_<revision>.<ext>
```

### Examples
- `53-10_DWG_PART_FRAME-F01_D0001_SH1_RevA.pdf`
- `53-10_DWG_PART_STRINGER-STR-L01_D0015_SH1_RevB.pdf`
- `53-10_DWG_PART_SKIN-PANEL-SP-001_D0025_SH1-3_RevA.pdf`
- `53-10_DWG_PART_BRACKET-BRK-045_D0100_SH1_RevA.pdf`

## Organization

Organize part drawings by:
- **Component type**: Frames, stringers, skins, brackets, fittings
- **Zone**: Reference to zone (FWD, CTR, AFT) in drawing number or notes
- **Part family**: Group related parts (e.g., all frame clips together)

## Related Directories

- **CAD models**: [`../../MODELS/`](../../MODELS/)
- **Assemblies**: [`../ASSEMBLY/`](../ASSEMBLY/) - for assembly drawings
- **Details**: [`../DETAIL/`](../DETAIL/) - for enlarged detail views
- **Zone organization**: [`../ZONES/`](../ZONES/) - drawings organized by zone
- **Revisions**: [`../REVISIONS/`](../REVISIONS/) - revision management

## Best Practices

### Drawing Content
- Include all views necessary for complete definition
- Show section views for internal features
- Use detail views (2X, 4X) for small features
- Dimension from manufacturing datums
- Include process notes and special instructions

### Quality Requirements
- All dimensions toleranced (general or specific)
- Material callout complete with specifications
- Surface finish specified for all surfaces
- Critical features identified
- Manufacturing notes clear and unambiguous

## References

- **Parent README**: [`../README.md`](../README.md) - General drawing standards
- **MODELS**: [`../../MODELS/README.md`](../../MODELS/README.md) - Source CAD models
- **Standards**: `/00-PROGRAM/STANDARDS/` - Applicable drawing standards
