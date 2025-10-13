# BORDERS — Drawing Border Templates

## Purpose

Standard drawing borders with zone markers for reference and coordination.

## Contents

Border templates for all standard drawing sizes:
- **ISO A-series**: A0, A1, A2, A3, A4
- **ANSI sizes**: E, D, C, B, A
- **Custom sizes**: As required for specific applications

## Border Elements

### Zone Markers
- **Horizontal zones**: Numbers (1-9, 1-12, etc.) top and bottom
- **Vertical zones**: Letters (A-Z) left and right
- **Purpose**: Enable quick location reference on drawings

### Border Layout
- **Drawing frame**: Outer boundary of drawing area
- **Margin**: Standard margin around sheet edge (typically 10-20mm)
- **Fold marks**: For large drawings (folding to A4 size)
- **Trim marks**: Corner registration marks

### Border Spacing
- **A4/A3**: 10mm margin, zones every 50mm or letter/number
- **A1/A0**: 15-20mm margin, zones appropriate to sheet size
- **ANSI sizes**: Per ASME Y14.1 standards

## Naming Convention

```
Border_<size>_<orientation>_<zones>.<ext>
```

Examples:
- `Border_A3_Landscape_8x6zones.dwg`
- `Border_A1_Portrait_12x8zones.dwg`
- `Border_E_Size_Landscape_Standard.dwg`

## Usage Guidelines

1. Select border matching drawing sheet size and orientation
2. Ensure zone markers are visible and clear
3. Do not place drawing content outside border
4. Use zones for referencing (e.g., "See detail A in zone C-4")
5. Include fold marks for drawings larger than A3

## References

- Parent directory: [`../README.md`](../README.md)
- Drawing standards: ASME Y14.1, ISO 5457
- Sheet formats: [`../SHEET_FORMATS/README.md`](../SHEET_FORMATS/README.md)
