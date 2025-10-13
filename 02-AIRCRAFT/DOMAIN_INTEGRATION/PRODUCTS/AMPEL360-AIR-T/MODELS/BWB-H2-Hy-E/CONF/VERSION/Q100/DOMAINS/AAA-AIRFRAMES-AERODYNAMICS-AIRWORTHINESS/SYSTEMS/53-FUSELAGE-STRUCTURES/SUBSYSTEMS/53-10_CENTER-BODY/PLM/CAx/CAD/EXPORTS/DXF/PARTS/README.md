# PARTS — Individual Part DXF Files

## Purpose
DXF files for individual structural parts and components.

## Contents
- **[FLAT_PATTERNS/](FLAT_PATTERNS/)** — Flat pattern developments for sheet metal parts
- **[SHEET_METAL/](SHEET_METAL/)** — Sheet metal parts with bend lines and forming details
- **[MACHINING_PROFILES/](MACHINING_PROFILES/)** — Machined part profiles and features

## Organization
Organize by:
- Part type (frame, skin, bracket, etc.)
- Manufacturing process
- Material type
- Part number sequence

## File Naming Convention
```
<part-number>_<description>_<revision>_<date>.dxf
```

Examples:
- `53-10-F001_FRAME-FWD_A_20250110.dxf`
- `53-10-SK042_SKIN-PANEL_B_20250110.dxf`
- `53-10-BRK15_BRACKET_A_20250110.dxf`

## Guidelines
- One part per file
- Include all manufacturing features
- Specify material thickness in metadata
- Document bend allowances for sheet metal
- Include dimensional tolerances

## Related Directories
- **[../../MODELS/](../../MODELS/)** — Source 3D models
- **[../../../CAM/NESTING/](../../../CAM/NESTING/)** — Nesting layouts
- **[../REVISIONS/](../REVISIONS/)** — Revision control

## Best Practices
- Export at 1:1 scale
- Use consistent layer structure
- Include critical dimensions
- Validate before committing
- Reference source file in metadata
