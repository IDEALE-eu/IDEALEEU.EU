# STEP_DRAWINGS — Assembly Step Technical Drawings

## Purpose

This directory contains 2D technical drawings that illustrate each assembly step for the 53-10 Center Body.

## Contents

### Drawing Types
- **Step-by-step drawings**: Detailed drawings for each assembly step
- **Installation drawings**: Component installation procedures
- **Fastener schedules**: Fastener installation drawings and patterns
- **Detail callouts**: Zoomed views of critical details

## Drawing Format

### File Formats
- **PDF**: Released drawings for production use
- **DWG/DXF**: Source CAD drawings
- **PNG/JPEG**: Reference images for documentation

### Drawing Contents
Each step drawing should include:
- Step number and title
- Components being installed
- Installation procedure notes
- Critical dimensions and tolerances
- Fastener types, quantities, and torques
- Quality inspection points
- Reference to 3D models

## Naming Convention

Use the following pattern:
```
53-10_STEP-DWG_<step-number>_<description>_<version>.<ext>
```

Examples:
- `53-10_STEP-DWG_001_FRAME-F05-INSTALL_v01.pdf`
- `53-10_STEP-DWG_002_STRINGER-ATTACH_v02.pdf`
- `53-10_STEP-DWG_003_FASTENER-PATTERN_v01.pdf`

## Drawing Standards

### Requirements
- Follow ATA iSpec 2200 format
- Include title block with metadata
- Show multiple views as needed
- Add section views for clarity
- Include detail views for critical features
- Add notes and callouts

### Title Block Information
- Drawing number
- Step number and description
- Assembly identification (53-10)
- Revision level
- Approval signatures
- Issue date

## Drawing Views

### Standard Views
- **Plan view**: Top-down assembly view
- **Section views**: Cross-sections showing internal details
- **Detail views**: Enlarged views of critical areas
- **Isometric/3D views**: Overall assembly orientation

### Annotations
- Dimensions and tolerances
- Geometric tolerancing (GD&T)
- Surface finish requirements
- Material callouts
- Fastener specifications
- Assembly notes

## Related Directories

- **STEP_MODELS**: [`../STEP_MODELS/`](../STEP_MODELS/) — 3D models of steps
- **Quality**: [`../../QUALITY/`](../../QUALITY/) — Quality checkpoints
- **Assembly Drawings**: [`../../../DRAWINGS/`](../../../DRAWINGS/) — Overall assembly drawings
