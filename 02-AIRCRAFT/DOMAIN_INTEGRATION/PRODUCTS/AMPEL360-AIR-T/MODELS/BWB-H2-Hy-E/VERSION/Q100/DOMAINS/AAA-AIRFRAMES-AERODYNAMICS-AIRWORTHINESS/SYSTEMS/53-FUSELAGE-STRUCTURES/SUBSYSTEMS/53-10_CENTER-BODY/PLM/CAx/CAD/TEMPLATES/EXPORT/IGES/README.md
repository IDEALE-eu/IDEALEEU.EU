# IGES — IGES Export Templates and Settings

## Purpose

Export settings and templates for IGES (Initial Graphics Exchange Specification) format, a legacy 3D neutral format.

## IGES Overview

**Standard:** IGES 5.3 (most widely supported version)

**Use Cases:**
- Legacy CAD systems that don't support STEP
- Supplier requirement for IGES specifically
- Surface modeling and surfacing work
- CAM systems (older versions)

**Limitations:**
- No PMI (Product Manufacturing Information) support
- Limited attribute preservation
- May lose assembly structure
- Less robust than STEP AP242
- Not recommended for new projects (use STEP instead)

## Export Settings Template

### Recommended Settings
```
Version: IGES 5.3
File Type: Binary or ASCII (Binary recommended for size)

Geometry:
  ☑ Surfaces (trimmed NURBS surfaces)
  ☑ Solids (BREP, entity type 186)
  ☑ Wireframe (curves, entity type 126)
  ☐ Construction geometry (exclude)

Conversion:
  ☑ Convert to NURBS
  ☑ Trim surfaces
  ☑ Maintain topology
  Tolerance: 0.001 mm

Assembly:
  ☐ Single file (all parts in one file)
  ☑ Multiple files (one per part, recommended)
  Structure: Instance reference (entity type 430)

Units: Millimeters (mm)
Precision: 0.001 mm
Validation: Enable
```

## CAD System Specific Settings

### CATIA V5
**File → Save As → IGES**
- Version: IGES 5.3
- Surfaces: Trimmed surfaces
- Output: One file per part
- Solid export: BREP entity

### Siemens NX
**File → Export → IGES**
- Protocol: 5.3
- Output type: Trimmed surfaces and solids
- Assembly: Component parts
- Units: mm

### SOLIDWORKS
**File → Save As → IGES (*.igs; *.iges)**
- Options → IGES standard: 5.3
- Surface entities: Trimmed surfaces
- Save assembly as: Multiple files

### PTC Creo
**File → Save As → Save a Copy**
- Type: IGES (*.igs)
- Version: 5.3
- Export: Surfaces and solids
- Configuration: intf3d_out_extend_surface yes

## IGES Entity Types

### Common Entity Types
- **100**: Circular arc
- **102**: Composite curve
- **110**: Line
- **126**: Rational B-spline curve (NURBS curve)
- **128**: Rational B-spline surface (NURBS surface)
- **142**: Curve on a parametric surface
- **144**: Trimmed parametric surface
- **186**: Manifold solid BREP object (solid)
- **314**: Color definition
- **406**: Property entity (attributes)
- **430**: Solid assembly (instance reference)

## Validation Checklist

After export, verify:
- [ ] File opens without errors
- [ ] Geometry is complete
- [ ] Surfaces are trimmed correctly
- [ ] No missing faces or edges
- [ ] Units are correct (mm)
- [ ] File size is reasonable
- [ ] Assembly structure preserved (if multi-part)

## Quality Control

### Visual Inspection
- Open in IGES viewer or receiving CAD system
- Check for gaps or overlaps in surfaces
- Verify solid integrity (if exporting solids)
- Check for missing or corrupted geometry

### Dimensional Check
- Measure known dimensions
- Verify overall bounding box
- Check critical features

## File Organization

### Naming Convention
```
<part-number>_<description>_IGES_v<version>.igs
```

**Examples:**
- `53-10-001_FRAME-F01_IGES_v01.igs`
- `53-10-002_FRAME-F02_IGES_v01.igs`

### Directory Structure
```
IGES/
├── 53-10-001_FRAME-F01_IGES_v01.igs
├── 53-10-002_FRAME-F02_IGES_v01.igs
├── 53-10-003_FRAME-F03_IGES_v01.igs
└── README.md
```

## Best Practices

### When to Use IGES
- ✓ Supplier specifically requests IGES
- ✓ Receiving system doesn't support STEP
- ✓ Surfacing/styling work (surfaces only)
- ✓ Legacy compatibility required

### When NOT to Use IGES
- ✗ STEP is available and supported (use STEP instead)
- ✗ Need to preserve PMI/annotations
- ✗ Need to preserve assembly structure robustly
- ✗ Archival/baseline (use STEP instead)

### Export Tips
- Export surfaces as trimmed NURBS
- Use BREP solids (entity 186) for solid parts
- Export one file per part for assemblies
- Include sufficient tolerance (0.001 mm typical)
- Validate after export (import back into CAD)

## Troubleshooting

### Common Issues

**Issue:** Surfaces not trimmed correctly
- **Solution:** Check "trim surfaces" option, increase export tolerance slightly

**Issue:** Assembly structure lost
- **Solution:** Export as multiple files, one per component, with assembly instance file

**Issue:** Solid models corrupt or incomplete
- **Solution:** Check BREP export settings, may need to export as surfaces instead

**Issue:** File size too large
- **Solution:** Use binary format instead of ASCII, reduce precision if acceptable

**Issue:** Gaps in surfaces
- **Solution:** Check surface continuity in source CAD, may need to heal or stitch

**Issue:** Units incorrect
- **Solution:** Verify unit settings in export dialog (should be mm, entity 316)

## IGES Header Information

Typical IGES file header includes:
```
Units: Millimeters (flag 2)
Max line weight: 0.001
Model space scale: 1.0
Author: [Designer name]
Organization: IDEALE-EU
Date: [Export date]
```

## Migration to STEP

**Recommendation:** Transition to STEP AP242 for all new exports.

**Why:**
- STEP is more robust and reliable
- STEP supports PMI (GD&T, annotations)
- STEP preserves assembly structure better
- STEP is the industry standard for aerospace
- IGES is legacy and no longer actively developed

**Migration strategy:**
- Provide both IGES and STEP initially
- Encourage suppliers to adopt STEP
- Phase out IGES over time

## Related Files

- Parent directory: [`../README.md`](../README.md)
- STEP export (recommended): [`../STEP_AP242/README.md`](../STEP_AP242/README.md)
- JT export: [`../JT/README.md`](../JT/README.md)
- Main exports: [`../../../EXPORTS/IGES/README.md`](../../../EXPORTS/IGES/README.md)

## References

- IGES 5.3 specification (ANSI/US PRO/IPO-100-1996)
- US Product Data Association (USPRO)
- Company IGES export procedures
- CAD system documentation for IGES export
