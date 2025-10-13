# MACHINING_PROFILES — Machined Part Profiles

## Purpose
DXF files for machined part profiles and features for CNC programming.

## Contents
- Machining profiles and contours
- Pocket and slot geometry
- Hole patterns and locations
- Threading and tapping locations
- Surface finish zones

## Part Types
- Machined frames and ribs
- Machined fittings and brackets
- Precision-machined details
- Tooling and fixture components
- Custom machined parts

## Layer Structure
**Standard layers**:
- **PROFILE**: Outer contour/profile
- **POCKETS**: Internal pockets and recesses
- **HOLES**: Hole locations and diameters
- **THREADS**: Threaded hole locations
- **TOOLING**: Tool paths (if applicable)
- **TEXT**: Manufacturing notes and callouts
- **DIMENSIONS**: Critical dimensions and tolerances

## Machining Information
Specify for features:
- Depth of cut for pockets/slots
- Hole diameters and depths
- Thread specifications (M6x1.0, etc.)
- Counterbore/countersink details
- Surface finish requirements (Ra values)
- Tolerance zones

## Manufacturing Specifications
Include as annotations:
- Material: e.g., AL 7075-T6, Ti-6Al-4V
- Stock size: Starting material dimensions
- Machining sequence if critical
- Tool requirements: End mill, drill sizes
- Surface finish: Ra 1.6, Ra 3.2, etc.
- Heat treatment: If applicable

## File Naming
```
<part-number>_<description>_<profile-type>_<revision>_<date>.dxf
```

Examples:
- `53-10-FRM05_FRAME-PROFILE_OUTER_A_20250110.dxf`
- `53-10-FIT12_FITTING-POCKETS_B_20250110.dxf`

## Related Directories
- **[../../../../CAM/NC_PROGRAMS/](../../../../CAM/NC_PROGRAMS/)** — CNC programs
- **[../../../../CAM/TOOLING/](../../../../CAM/TOOLING/)** — Tooling and fixtures
- **[../../REVISIONS/](../../REVISIONS/)** — Revision history

## Export Requirements
- Profile geometry must be closed polylines
- Dimensions in mm or inches (specify)
- Include critical tolerances
- Verify scale is 1:1
- Test file in CAM software before committing

## CAM Programming Notes
- DXF provides geometry only
- Tool selection done in CAM software
- Cutting parameters defined separately
- Reference 3D model for depth information
- Coordinate with process engineer
