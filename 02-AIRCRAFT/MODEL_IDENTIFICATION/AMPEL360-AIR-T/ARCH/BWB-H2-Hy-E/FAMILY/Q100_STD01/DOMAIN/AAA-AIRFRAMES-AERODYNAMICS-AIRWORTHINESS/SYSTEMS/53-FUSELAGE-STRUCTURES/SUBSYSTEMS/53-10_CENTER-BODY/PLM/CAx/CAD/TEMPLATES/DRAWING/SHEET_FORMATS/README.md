# SHEET_FORMATS — Drawing Sheet Format Templates

## Purpose

Complete drawing sheet templates combining title blocks, borders, and standard layout configurations.

## Contents

Pre-configured sheet formats for immediate use:
- **ISO A-series**: A4, A3, A2, A1, A0 (portrait and landscape)
- **ANSI sizes**: A, B, C, D, E (portrait and landscape)
- **Special formats**: Half-size, oversize, custom

## Sheet Format Components

### Integrated Elements
- **Title block**: Embedded in sheet format
- **Border with zones**: Standard zone markers
- **Default views**: Pre-positioned view areas
- **Note areas**: Standard note placement zones
- **Revision block**: Integrated with title block

### Sheet Sizes

#### ISO A-Series
- **A4**: 210 × 297 mm
- **A3**: 297 × 420 mm
- **A2**: 420 × 594 mm
- **A1**: 594 × 841 mm
- **A0**: 841 × 1189 mm

#### ANSI Sizes
- **A**: 8.5 × 11 in (216 × 279 mm)
- **B**: 11 × 17 in (279 × 432 mm)
- **C**: 17 × 22 in (432 × 559 mm)
- **D**: 22 × 34 in (559 × 864 mm)
- **E**: 34 × 44 in (864 × 1118 mm)

## Naming Convention

```
SheetFormat_<size>_<orientation>_<type>.<ext>
```

Examples:
- `SheetFormat_A3_Landscape_Part.CATDrawing`
- `SheetFormat_A1_Portrait_Assembly.drw`
- `SheetFormat_D_Landscape_Installation.slddrw`
- `SheetFormat_A4_Portrait_Sketch.drw`

## Usage Guidelines

### Selecting Sheet Format
1. **Part drawings**: Typically A3 or A4
2. **Assembly drawings**: A1 or larger
3. **Installation drawings**: ANSI D or E size
4. **Detail drawings**: A4 or A3
5. **Layouts/arrangements**: A1, A0, or E size

### Best Practices
- Choose smallest sheet size that accommodates content clearly
- Use landscape orientation for most mechanical drawings
- Use portrait for tall, narrow parts or assemblies
- Maintain consistent scale across related drawings
- Leave white space - don't crowd the drawing

### File Management
- Store sheet formats in CAD system library
- Link (don't embed) for easier updates
- Version control sheet format templates
- Archive old formats when updating

## References

- Parent directory: [`../README.md`](../README.md)
- Title blocks: [`../TITLE_BLOCKS/README.md`](../TITLE_BLOCKS/README.md)
- Borders: [`../BORDERS/README.md`](../BORDERS/README.md)
- ISO 5457 — Technical drawings, Sheet sizes
- ASME Y14.1 — Decimal inch drawing sheet size
