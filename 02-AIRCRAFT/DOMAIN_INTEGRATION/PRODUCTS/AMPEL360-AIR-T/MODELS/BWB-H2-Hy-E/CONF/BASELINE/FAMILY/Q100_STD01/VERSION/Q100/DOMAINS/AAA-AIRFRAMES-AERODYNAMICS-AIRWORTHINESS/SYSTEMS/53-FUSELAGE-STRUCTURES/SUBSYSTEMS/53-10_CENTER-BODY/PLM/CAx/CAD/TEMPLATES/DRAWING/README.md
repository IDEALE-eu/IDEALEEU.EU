# DRAWING — Drawing Templates and Standards

## Purpose

This directory contains drawing templates with standardized title blocks, borders, sheet formats, and annotation standards for the 53-10 Center Body documentation.

## Directory Structure

```
DRAWING/
├── TITLE_BLOCKS/    # Company-standard title block templates
├── BORDERS/         # Standard sheet borders with zone markers
├── SHEET_FORMATS/   # Drawing sheet formats (A4, A3, A1, etc.)
├── SYMBOLS_GDT/     # GD&T symbols and feature control frames
├── NOTES/           # Standard notes and callouts
└── README.md        # This file
```

## Contents

### Drawing Components
- **Title blocks**: Company logo, approval blocks, revision tables
- **Borders**: Standard sheet borders with zone markers (A-Z, 1-9)
- **Sheet formats**: Standard drawing sizes (ISO A-series, ANSI sizes)
- **GD&T symbols**: Geometric dimensioning and tolerancing symbols
- **Standard notes**: Reusable notes for common requirements

## Template Files

Standard drawing templates should include:
- Pre-positioned title block with metadata fields
- Border with zone markers
- Standard view configurations
- Dimension styles per company standards
- Layer standards (dimensions, annotations, geometry)
- Scale blocks and callouts

## Naming Convention

```
DWG_<sheet-size>_<orientation>_<variant>.<ext>
```

Examples:
- `DWG_A4_Portrait_IDEALE.CATDrawing`
- `DWG_A3_Landscape_Standard.drw`
- `DWG_A1_Assembly_Detailed.slddrw`
- `DWG_E_Size_Large_Assembly.drw`

## Usage Guidelines

### Creating a New Drawing
1. Select appropriate drawing template based on content and size
2. Insert model views from CAD model
3. Apply standard dimension styles
4. Complete title block information (part number, description, etc.)
5. Add required notes and standards callouts
6. Add GD&T callouts per ASME Y14.5 or ISO 1101
7. Export to PDF per standards (see `../EXPORT/`)

### Drawing Standards
- **Dimension styles**: Per ASME Y14.5 or ISO 1101
- **View arrangement**: Third-angle projection (ANSI) or first-angle (ISO)
- **Line weights**: Standard line thickness hierarchy
- **Text height**: Minimum 3mm on printed drawing
- **Scale**: Clearly indicated on each view

### Best Practices
- Use appropriate sheet size for content
- Maintain consistent title block completion
- Use standard notes from `NOTES/` directory
- Apply GD&T symbols from `SYMBOLS_GDT/` library
- Export to PDF with embedded fonts

## Related Directories

- **Title Blocks**: [`./TITLE_BLOCKS/`](./TITLE_BLOCKS/) — Title block templates
- **Borders**: [`./BORDERS/`](./BORDERS/) — Border templates
- **Sheet Formats**: [`./SHEET_FORMATS/`](./SHEET_FORMATS/) — Sheet size templates
- **GD&T Symbols**: [`./SYMBOLS_GDT/`](./SYMBOLS_GDT/) — Geometric tolerancing symbols
- **Notes**: [`./NOTES/`](./NOTES/) — Standard note libraries
- **Export**: [`../EXPORT/`](../EXPORT/) — Export format standards

## References

- Main templates documentation: [`../README.md`](../README.md)
- Drawing best practices: [`../../DRAWINGS/README.md`](../../DRAWINGS/README.md)
- ASME Y14.5 — Dimensioning and Tolerancing
- ISO 1101 — Geometrical Product Specifications
- Company drawing standards manual
