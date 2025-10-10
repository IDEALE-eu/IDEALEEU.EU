# TITLE_BLOCKS — Title Block Templates

## Purpose

Standard title block templates with company logo, approval signatures, revision tables, and metadata fields.

## Contents

Title block templates for various drawing sizes and purposes:
- **A4/A3 title blocks**: Small format drawings
- **A1/A0 title blocks**: Large format drawings
- **ANSI size title blocks**: E, D, C, B, A sizes
- **Special purpose**: Sketches, calculations, redlines

## Title Block Elements

### Required Fields
- **Part number**: Unique identifier per part numbering scheme
- **Part name**: Descriptive part name
- **Revision**: Current revision letter/number
- **Drawing number**: Unique drawing identifier
- **Sheet number**: Sheet X of Y
- **Scale**: Drawing scale (1:1, 1:2, etc.)
- **Material**: Primary material specification
- **Finish**: Surface finish requirements
- **Weight**: Part weight (calculated or estimated)

### Approval Blocks
- **Drawn by**: Designer name and date
- **Checked by**: Checker name and date
- **Approved by**: Engineering manager name and date

### Revision Table
- **Revision letter**: A, B, C, etc.
- **Description**: Summary of changes
- **Date**: Revision date
- **Approved by**: Approver initials

### Company Information
- **Company logo**: IDEALE-EU logo
- **Company name**: Full legal name
- **Project**: AMPEL360-AIR-T / BWB-H2-Hy-E
- **System/subsystem**: 53-10 CENTER-BODY

## Naming Convention

```
TitleBlock_<size>_<orientation>_<variant>.<ext>
```

Examples:
- `TitleBlock_A3_Landscape_Standard.dwg`
- `TitleBlock_A1_Portrait_Assembly.dwg`
- `TitleBlock_E_Size_Landscape_Large.dwg`

## Usage Guidelines

1. Select title block matching drawing sheet size
2. Embed or link title block in drawing template
3. Complete all required fields before releasing drawing
4. Update revision table for each revision
5. Ensure approval signatures before release

## References

- Parent directory: [`../README.md`](../README.md)
- Drawing standards: [`../../DRAWINGS/README.md`](../../DRAWINGS/README.md)
- Properties definitions: [`../../PROPERTIES/README.md`](../../PROPERTIES/README.md)
