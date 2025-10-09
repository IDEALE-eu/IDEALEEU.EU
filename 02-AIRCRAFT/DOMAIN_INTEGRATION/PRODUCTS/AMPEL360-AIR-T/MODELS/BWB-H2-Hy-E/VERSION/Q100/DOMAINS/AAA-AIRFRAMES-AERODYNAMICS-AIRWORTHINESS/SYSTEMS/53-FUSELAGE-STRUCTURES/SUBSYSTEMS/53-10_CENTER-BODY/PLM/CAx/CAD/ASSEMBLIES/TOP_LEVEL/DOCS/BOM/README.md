# BOM — Bill of Materials

## Purpose

This directory contains Bill of Materials (BOM) exports and documentation for the top-level assembly.

## BOM Types

### Engineering BOM (EBOM)
- **As-designed**: Structure from CAD assembly
- **All components**: Parts, sub-assemblies, standard hardware
- **Quantities**: Per-assembly counts
- **References**: Part numbers and descriptions

### Manufacturing BOM (MBOM)
- **As-built**: Manufacturing sequence
- **Process steps**: Assembly operations
- **Tooling**: Required fixtures and tools
- **Work instructions**: Assembly procedures

## BOM Formats

### File Types
- `.xlsx` — Excel spreadsheet format
- `.csv` — Comma-separated values
- `.xml` — Structured BOM data
- `.pdf` — Released BOM documents

## BOM Content

Each BOM should include:
- **Item number**: Sequential item identifier
- **Part number**: Unique part identifier
- **Description**: Part or assembly name
- **Quantity**: Number required per assembly
- **Unit of measure**: Each, pair, set, etc.
- **Material**: Material specification
- **Source**: Make/buy decision
- **Notes**: Additional information

## BOM Levels

### Top-Level BOM
- Shows immediate children only
- Summary view of major assemblies
- Useful for high-level planning

### Indented BOM
- Shows full hierarchy
- All levels of sub-assemblies
- Complete part list

### Flattened BOM
- All parts at one level
- No hierarchy shown
- Useful for procurement

## Naming Convention

```
53-10_BOM_<type>_<version>.<ext>
```

Examples:
- `53-10_BOM_EBOM_v01.xlsx`
- `53-10_BOM_INDENTED_v01.csv`
- `53-10_BOM_FLAT_v01.pdf`

## BOM Validation

Check before release:
- [ ] All components included
- [ ] Quantities correct
- [ ] Part numbers valid
- [ ] Descriptions accurate
- [ ] No missing information
- [ ] Matches CAD assembly

## Related Documents

- **Interface Control**: [`../INTERFACE_CONTROL/`](../INTERFACE_CONTROL/) — Interface part requirements
- **Assembly**: [`../../ASM/`](../../ASM/) — Source assembly model
