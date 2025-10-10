# MODELS — Check Fixture CAD Models

## Purpose

This directory contains the CAD models of check fixtures used for dimensional inspection and verification of the 53-10 Center Body components.

## Contents

### Model Types
- **Native CAD files**: CATIA, NX, SolidWorks, Creo formats
- **Fixture assemblies**: Complete check fixture assemblies
- **Component models**: Individual fixture components
- **Reference geometry**: Master coordinate systems and datums

## Naming Convention

Use the following pattern:
```
53-10_FIX_CHECK_<item-to-inspect>_<version>.<ext>
```

Examples:
- `53-10_FIX_CHECK_FRAME-F05-DIMS_v01.CATProduct`
- `53-10_FIX_CHECK_WING-INTERFACE_v02.prt`
- `53-10_FIX_CHECK_SKIN-PANEL-CONTOUR_v01.sldasm`

## File Formats

### Native Formats
- **CATIA**: `.CATProduct`, `.CATPart`
- **NX**: `.prt`
- **SolidWorks**: `.sldasm`, `.sldprt`
- **Creo**: `.asm`, `.prt`

## Model Requirements

All check fixture models should include:
- Master coordinate system definition
- Locating and clamping features
- Measurement reference points
- Material specifications
- Assembly instructions (if applicable)
- Tolerance specifications (±0.1mm typical)

## Related Directories

- **Drawings**: [`../DRAWINGS/`](../DRAWINGS/)
- **Setup procedures**: [`../SETUP/`](../SETUP/)
- **CMM programs**: [`../CMM/`](../CMM/)
