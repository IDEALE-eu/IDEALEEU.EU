# DXF — DXF Export Templates and Settings

## Purpose

Export settings and templates for DXF (Drawing Exchange Format), used for 2D drawings, profiles, and flat patterns.

## DXF Overview

**Format:** AutoCAD DXF (Drawing Exchange Format)

**Use Cases:**
- 2D drawing views for documentation
- Sheet metal flat patterns for laser/waterjet cutting
- 2D profiles for CNC machining
- Manufacturing documentation
- Cross-platform 2D data exchange

**Not Recommended For:**
- 3D models (use STEP instead)
- Assemblies (DXF is 2D only)
- PMI/GD&T (limited support)

## Export Settings Template

### Recommended Settings
```
Version: AutoCAD 2018 DXF (or later)
Format: ASCII (most compatible) or Binary (smaller file)

Content:
  ☑ 2D geometry (lines, arcs, circles, splines)
  ☑ Dimensions (if applicable)
  ☑ Text and annotations
  ☑ Layers (preserve layer structure)
  ☐ 3D geometry (exclude, not intended use)

Options:
  Units: Millimeters (mm)
  Precision: 0.01 mm (typical for manufacturing)
  Coordinate system: Absolute coordinates
  Export to: Model space (not paper space)
  
Layers:
  ☑ Preserve layer names
  ☑ Preserve layer colors
  ☑ Preserve line types
  
Dimensions:
  ☐ Explode dimensions (keep associative if supported)
  ☑ Include dimension text
  ☑ Include dimension lines
```

## CAD System Specific Settings

### CATIA V5
**File → Save As → DXF**
- Version: R2018 or later
- 2D output: From drawing view
- Units: mm
- Layers: Export all

### Siemens NX
**File → Export → DXF/DWG**
- File type: DXF
- Version: AutoCAD 2018
- Export from: Drawing sheet
- Units: Millimeters

### SOLIDWORKS
**File → Save As → DXF (*.dxf)**
- Options → Version: R2018/LT2018 DXF
- Output selection: Current sheet or specific view
- Mapping: Set layer/line style mapping

### PTC Creo
**File → Save As → Save a Copy**
- Type: DXF (*.dxf)
- Options → Configure export settings
- Export drawing or flatten 3D to 2D

## DXF Use Cases

### Flat Patterns for Sheet Metal
**Purpose:** Export developed (unfolded) sheet metal parts for manufacturing

**Settings:**
- Export flat pattern view only
- Include bend lines on separate layer
- Add material thickness note
- Include grain direction if applicable

**Layers:**
- Layer 0 (or PART): Part outline
- Layer BEND: Bend lines
- Layer TEXT: Annotations
- Layer DIM: Dimensions

**Example:**
```
53-10-001_SKIN-PANEL-SP-001_FLAT_DXF_v01.dxf
```

### 2D Profiles for Machining
**Purpose:** Export 2D profiles for CNC programming

**Settings:**
- Export profile view
- Include center marks for holes
- Specify start/end points for tool paths
- Remove dimensions (CAM software measures)

**Layers:**
- Layer PROFILE: Main outline
- Layer HOLES: Hole centers
- Layer POCKETS: Pocket outlines

### Drawing Views for Documentation
**Purpose:** Export 2D drawing views for documentation

**Settings:**
- Export all views from drawing sheet
- Include dimensions and annotations
- Preserve layer structure
- Include title block if needed

## Layer Organization

### Standard Layer Naming
```
0 or PART:        Main part geometry
CENTERLINE:       Centerlines and construction
DIMENSION:        Dimension lines and text
TEXT:             General annotations
HATCH:            Hatching and fill patterns
HIDDEN:           Hidden lines (dashed)
PHANTOM:          Phantom lines (chain dash)
BEND:             Bend lines (sheet metal)
CUTLINE:          Cutting paths
TOOLPATH:         Tool paths (manufacturing)
```

### Layer Properties
- **Line types:** Continuous, dashed, centerline, phantom
- **Colors:** By layer (0-7 standard colors, or true color)
- **Line weights:** Thin, medium, thick (0.18, 0.35, 0.70 mm typical)

## File Organization

### Naming Convention
```
<part-number>_<description>_<type>_DXF_v<version>.dxf
```

**Examples:**
- `53-10-001_FRAME-F01_PROFILE_DXF_v01.dxf`
- `53-10-013_SKIN-PANEL-SP-001_FLAT_DXF_v01.dxf`
- `53-10_DWG_CENTER-BODY_INSTALLATION_DXF_v01.dxf`

### Directory Structure
```
DXF/
├── FLAT_PATTERNS/
│   ├── 53-10-013_SKIN-PANEL-SP-001_FLAT_DXF_v01.dxf
│   ├── 53-10-014_SKIN-PANEL-SP-002_FLAT_DXF_v01.dxf
│   └── ...
├── PROFILES/
│   ├── 53-10-001_FRAME-F01_PROFILE_DXF_v01.dxf
│   ├── 53-10-002_FRAME-F02_PROFILE_DXF_v01.dxf
│   └── ...
├── DRAWINGS/
│   ├── 53-10_DWG_FRAME-F01_DXF_v01.dxf
│   └── ...
└── README.md
```

## Validation Checklist

After export, verify:
- [ ] File opens without errors in DXF viewer
- [ ] All geometry is visible
- [ ] Dimensions are readable (if included)
- [ ] Layers are organized correctly
- [ ] Units are correct (mm)
- [ ] Scale is 1:1 (full size)
- [ ] No overlapping or duplicate entities

## Quality Control

### Visual Inspection
- Open in AutoCAD, DraftSight, or DXF viewer
- Check geometry completeness
- Verify dimensions (if included)
- Check layer organization

### Dimensional Check
- Measure known dimensions
- Verify overall bounding box
- Check hole centers and spacing

### Manufacturing Review
- Verify flat pattern is correct
- Check bend allowances (sheet metal)
- Confirm grain direction noted
- Verify tool access and clearances

## Best Practices

### For Manufacturing
- Export flat patterns without dimensions (CAM measures directly)
- Place bend lines on separate layer
- Include material callout in separate text file
- Specify grain direction for sheet metal
- Use absolute coordinates (origin at convenient location)

### For Documentation
- Include dimensions and annotations
- Preserve layer structure from CAD
- Export at 1:1 scale
- Include title block if applicable

### General Tips
- Use ASCII format for maximum compatibility
- Set precision appropriate for manufacturing (0.01 mm typical)
- Remove construction geometry before export
- Verify units are millimeters
- Test import in receiving software

## Troubleshooting

### Common Issues

**Issue:** Dimensions not visible or corrupt
- **Solution:** Explode dimensions before export, or export without dimensions

**Issue:** Geometry scale incorrect
- **Solution:** Verify units in export settings (should be mm), check scale factor

**Issue:** Layers not preserved
- **Solution:** Check layer export options, ensure "export all layers" is enabled

**Issue:** Text not readable
- **Solution:** Verify font mapping, use standard fonts (Arial, Times)

**Issue:** Arcs/circles have facets (not smooth)
- **Solution:** Increase tessellation/arc quality settings in export

## DXF vs. DWG

**DXF (Drawing Exchange Format):**
- Open format, widely supported
- ASCII or binary format
- Good for data exchange
- Slightly larger file size than DWG

**DWG (AutoCAD native):**
- Proprietary format (AutoCAD)
- More efficient (smaller files)
- Better preserves AutoCAD-specific features
- May have compatibility issues across CAD systems

**Recommendation:** Use DXF for neutral exchange, DWG only if AutoCAD-specific features required.

## Related Files

- Parent directory: [`../README.md`](../README.md)
- STEP export: [`../STEP_AP242/README.md`](../STEP_AP242/README.md)
- Drawing templates: [`../../DRAWING/README.md`](../../DRAWING/README.md)
- Main exports: [`../../../EXPORTS/DXF/README.md`](../../../EXPORTS/DXF/README.md)

## References

- AutoCAD DXF Reference (Autodesk documentation)
- ISO 10303 (STEP) for 3D models (recommended over DXF for 3D)
- Company DXF export standards
- Manufacturing department requirements
