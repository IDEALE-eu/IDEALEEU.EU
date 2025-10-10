# PART — Part Templates

## Purpose

This directory contains reusable part templates pre-configured with standard settings, coordinate systems, and material assignments for the 53-10 Center Body design work.

## Contents

### Part Template Types
- **Structural parts**: Frame members, bulkheads, longerons
- **Sheet metal parts**: Skin panels, brackets, clips
- **Machined parts**: Fittings, lugs, machined details
- **Composite parts**: Composite panels, sandwich structures

## Template Files

Standard part templates should include:
- Pre-configured coordinate systems and datum planes
- Material properties (e.g., Al 2024-T3, Ti-6Al-4V, CFRP)
- Standard layer/level structure
- Metadata fields (part number, revision, author, date)
- Design parameters for common dimensions
- Standard feature libraries

## Naming Convention

```
PART_<material-type>_<part-category>_<variant>.<ext>
```

Examples:
- `PART_Aluminum_Structural_Frame.CATPart`
- `PART_SheetMetal_Skin_Panel.CATPart`
- `PART_Composite_Sandwich.CATPart`
- `PART_Titanium_Fitting.prt`

## Usage Guidelines

### Starting a New Part
1. Select appropriate part template based on material and manufacturing process
2. Save as new file with proper naming convention (see `../NAMING_CONVENTIONS/`)
3. Update part properties (part number, description, author)
4. Verify material assignment
5. Maintain coordinate system orientation per `../PARAMETERS/`
6. Use standard feature naming conventions

### Best Practices
- Always start from template (don't copy from existing parts)
- Don't modify master templates directly
- Update properties immediately after saving template as new part
- Follow coordinate system standards (see `../PARAMETERS/`)
- Use standard material definitions (see `../MATERIALS/`)

## Related Directories

- **Materials**: [`../MATERIALS/`](../MATERIALS/) — Material property definitions
- **Parameters**: [`../PARAMETERS/`](../PARAMETERS/) — Design parameter standards
- **Properties**: [`../PROPERTIES/`](../PROPERTIES/) — Metadata field definitions
- **Naming Conventions**: [`../NAMING_CONVENTIONS/`](../NAMING_CONVENTIONS/) — File naming rules

## References

- Main templates documentation: [`../README.md`](../README.md)
- CAD standards: [`../../README.md`](../../README.md)
- ATA Chapter 53 standards
- Company design manual
