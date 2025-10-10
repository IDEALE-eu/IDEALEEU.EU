# DRAWINGS — Assembly Drawings

## Purpose

This directory contains 2D engineering drawings derived from the top-level assembly models.

## Contents

### Drawing Types
- **General arrangement drawings**: Overall assembly layout
- **Installation drawings**: Interface and mounting details
- **Detail drawings**: Specific assembly features
- **Interface control drawings**: Mating part requirements

## Drawing Standards

Follow:
- **ATA iSpec 2200**: Technical documentation standards
- **ASME Y14.5**: Dimensioning and tolerancing
- **ISO 128**: Technical drawings general principles
- **Company standards**: Internal drawing practices

## File Types

- `.CATDrawing` — CATIA drawings
- `.prt` — NX drawings
- `.slddrw` — SolidWorks drawings
- `.drw` — Creo drawings
- `.pdf` — Released drawing PDFs
- `.dxf` — 2D CAD exchange format

## Naming Convention

```
53-10_DRW_CENTER-BODY_<type>_<version>.<ext>
```

Examples:
- `53-10_DRW_CENTER-BODY_GA_v01.CATDrawing`
- `53-10_DRW_CENTER-BODY_INSTALLATION_v02.pdf`

## Drawing Contents

Each drawing should include:
- **Title block**: Part number, revision, dates
- **Views**: Multiple orthogonal and isometric views
- **Dimensions**: Critical interface dimensions
- **Notes**: Assembly instructions and specifications
- **BOM**: Component list with quantities

## Related Directories

- **Assembly**: [`../ASM/`](../ASM/) — Source assembly models
- **Documentation**: [`../DOCS/`](../DOCS/) — Supporting documentation
