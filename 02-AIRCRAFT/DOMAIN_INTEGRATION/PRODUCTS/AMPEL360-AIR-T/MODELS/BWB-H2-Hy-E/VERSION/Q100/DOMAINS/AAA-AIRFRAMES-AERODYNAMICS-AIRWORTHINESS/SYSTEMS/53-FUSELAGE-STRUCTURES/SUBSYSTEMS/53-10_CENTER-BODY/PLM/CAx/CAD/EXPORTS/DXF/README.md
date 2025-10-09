# DXF — Drawing Exchange Format (2D)

## Purpose

This directory contains DXF (Drawing Exchange Format) files for 2D drawing geometry, manufacturing documentation, and CAM programming.

## Overview

**DXF** is the de facto standard for 2D CAD data exchange:
- **Universal support**: Compatible with virtually all CAD and graphics software
- **2D geometry**: Lines, arcs, circles, polylines, dimensions, text
- **Manufacturing**: CNC programming, laser cutting, sheet metal
- **ASCII format**: Human-readable text file
- **AutoCAD origin**: Created by Autodesk, now universal standard

## When to Use DXF

### Primary Use Cases
- **Sheet metal fabrication**: Flat patterns for cutting and forming
- **Laser/waterjet cutting**: 2D profiles for cutting operations
- **CNC machining**: 2D profiles for mill/router programming
- **PCB design**: Board outlines and component footprints
- **Architectural/civil**: Floor plans, site layouts
- **Technical illustrations**: 2D schematics and diagrams

### Advantages
- ✅ Universal 2D format
- ✅ Free viewers widely available
- ✅ Small file sizes
- ✅ Supports layers and colors
- ✅ Dimensions and annotations
- ✅ ASCII (human-readable)

### Limitations
- ❌ 2D only: No 3D solid geometry
- ⚠️ 3D wireframe: Limited 3D support
- ❌ No assemblies: Single file per drawing
- ⚠️ Vendor variations: Implementation differences

## What to Store

### 2D Geometry
- **Drawing views**: Orthographic projections from 3D models
- **Flat patterns**: Sheet metal development
- **Profiles**: Cross-sections and contours
- **Templates**: Cutting patterns and blanks
- **Schematics**: System diagrams and layouts

### Content Types
- ✅ Lines, arcs, circles, ellipses
- ✅ Polylines and splines
- ✅ Dimensions and tolerances
- ✅ Text and annotations
- ✅ Hatching and fills
- ✅ Layers and colors
- ✅ Blocks (reusable symbols)
- ⚠️ 3D wireframe (limited)
- ❌ 3D solids (not supported)

## File Format

### File Extension
- `.dxf` (only option)

### File Types
- **ASCII DXF**: Text format, human-readable, larger file size
- **Binary DXF**: Binary format, faster to read, smaller file size

**Recommendation**: Use ASCII DXF for maximum compatibility.

### DXF Versions
- **AutoCAD 2018 DXF**: Latest widely-supported version
- **AutoCAD 2013 DXF**: Good compatibility balance
- **AutoCAD 2007 DXF**: Maximum compatibility with older systems
- **AutoCAD 2000 DXF**: Legacy systems only

**Recommendation**: Use AutoCAD 2013 or 2018 DXF unless partner specifies otherwise.

## Naming Convention

Use the following naming pattern:
```
<subsystem>_<component>_<drawing-number>_<sheet>_<date>.dxf
```

Examples:
- `53-10_FRAME-F01_D0001_SH1_20250110.dxf`
- `53-10_SKIN-PANEL_FLAT-PATTERN_SP-001_20250110.dxf`
- `53-10_PROFILE_SECTION-A_20250110.dxf`

## Export Settings

### Recommended Export Options

**File Format**:
- ☑ ASCII DXF (not binary)
- ☑ AutoCAD 2013 or 2018 DXF version
- ☑ Full precision (14 decimal places)

**Content**:
- ☑ All layers (or selected layers)
- ☑ Dimensions and annotations
- ☑ Text and labels
- ☑ Hatching
- ☑ Line types and weights

**Units**:
- ☑ Millimeters or inches (specify clearly)
- ☑ Match source drawing units

**Options**:
- ☑ Explode blocks (if needed for manufacturing)
- ☑ Convert splines to polylines (if required)
- ☑ Flatten 3D geometry to 2D (if applicable)

### CAD System-Specific Settings

#### CATIA V5/V6
- File → Export → DXF
- Version: AutoCAD 2013 or later
- Include: All layers, dimensions, text

#### Siemens NX
- File → Export → DXF/DWG
- Version: AutoCAD 2013
- Options: Dimensions, annotations, layers

#### SolidWorks
- File → Save As → DXF
- Version: AutoCAD 2013/2018
- Include: Dimensions, annotations

#### AutoCAD
- File → Save As → AutoCAD 2013/2018 DXF
- Type: ASCII DXF
- Options: All objects

## Organization

### Layer Structure
Organize geometry by layers:

**Standard Layers**:
- **0 (zero)**: Default layer
- **GEOMETRY**: Main geometry (profiles, outlines)
- **DIMENSIONS**: Dimension lines and text
- **TEXT**: Notes and labels
- **CENTERLINES**: Center marks and axes
- **HATCHING**: Cross-hatching and fills
- **CONSTRUCTION**: Reference geometry
- **HIDDEN**: Hidden lines (dashed)

### Color Coding
Use colors to indicate:
- **Red**: Cutting paths
- **Blue**: Bend lines
- **Green**: Reference/construction
- **Yellow**: Annotations
- **Cyan**: Dimensions

### Line Types
- **Continuous**: Visible edges
- **Dashed**: Hidden edges
- **Center**: Center lines and axes
- **Phantom**: Reference lines

## Use Cases by Industry

### Sheet Metal Fabrication
**Content**: Flat patterns with bend lines
- Export flat pattern from 3D model
- Include bend lines and bend angles
- Add material thickness notes
- Specify bend radius and K-factor

**Layers**:
- CUTTING: Outer profile for cutting
- BENDING: Bend lines
- HOLES: Hole locations and sizes
- TEXT: Material and thickness callouts

### Laser/Waterjet Cutting
**Content**: Cutting profiles
- Export outer contours
- Include internal features (holes, slots)
- Nest multiple parts if appropriate
- Add material callout

**Requirements**:
- Closed polylines for cut paths
- No duplicate or overlapping geometry
- Proper scaling (1:1)
- Clear layer structure

### CNC Machining
**Content**: Machining profiles
- Export pockets, slots, and profiles
- Include tooling notes
- Add material callout
- Specify depth of cut

**Layers**:
- PROFILE: Outer contour
- POCKETS: Internal pockets
- HOLES: Hole locations and sizes
- TOOLING: Tool paths (if applicable)

### Technical Documentation
**Content**: 2D views from 3D models
- Export orthographic views
- Include dimensions and tolerances
- Add notes and callouts
- Maintain drawing standards

## Validation

### Opening and Checking DXF Files
Test DXF files in:
- **AutoCAD** or **DraftSight**: Full-featured CAD
- **LibreCAD**: Free open-source 2D CAD
- **QCAD**: Free 2D CAD software
- **Viewer**: Various free DXF viewers

### Validation Checklist
Before committing DXF files:
- [ ] File opens without errors
- [ ] All geometry visible and correct
- [ ] Dimensions readable and accurate
- [ ] Text displays properly
- [ ] Layers organized correctly
- [ ] Units are correct (mm or inches)
- [ ] Scale is 1:1
- [ ] File size reasonable
- [ ] Naming convention followed

### Common Issues

**Missing geometry**:
- Check layer visibility
- Verify all layers exported
- Ensure geometry on proper layers

**Incorrect scale**:
- Measure known dimension to verify scale
- Re-export with explicit unit setting
- Check import scale in receiving system

**Dimension errors**:
- Verify dimension style exported
- Check dimension associativity
- Re-create dimensions if necessary

**Text display problems**:
- Use standard fonts (Arial, Times, etc.)
- Avoid special characters
- Check text height is reasonable

## Manufacturing Handoff

### Documentation Package
Provide with DXF files:
- **PDF drawing**: Reference with full dimensions
- **Material spec**: Material type and thickness
- **Process notes**: Cutting, bending, finishing
- **Quality requirements**: Tolerances, inspection

### Metadata
Include in accompanying text file:
- Part number and revision
- Material specification
- Thickness (for sheet metal)
- Units (mm or inches)
- Special instructions
- Contact information

## Best Practices

### Geometry Preparation
- **Clean geometry**: Remove duplicates and overlaps
- **Closed contours**: Ensure profiles are closed for cutting
- **Proper orientation**: Orient parts for manufacturing
- **Nesting**: Arrange multiple parts efficiently if appropriate

### Layer Management
- Use consistent layer naming
- Organize by function (cutting, bending, reference)
- Use colors meaningfully
- Document layer structure

### Dimension and Annotation
- Include critical dimensions
- Add manufacturing notes
- Specify tolerances clearly
- Use standard symbols (e.g., ⌀ for diameter)

### File Size
- DXF files are typically small (< 1 MB)
- If large (> 10 MB), consider simplifying
- Remove unnecessary layers
- Reduce spline/arc resolution if acceptable

## Complementary Formats

### Provide Multiple Formats
For complete documentation:
- **PDF**: Primary reference drawing
- **DXF**: Machine-readable geometry
- **STEP**: 3D model for reference
- **Text file**: Metadata and instructions

### Cross-Reference
Link DXF to other files:
- Reference 3D model in `../../MODELS/`
- Link to drawing in `../../DRAWINGS/`
- Reference STEP file in `../STEP/`

## Tools and Software

### Free DXF Viewers
- **LibreCAD**: Open-source 2D CAD
- **QCAD**: Free 2D CAD with DXF support
- **eDrawings**: Free viewer from SolidWorks
- **DWG TrueView**: Free from Autodesk

### Commercial Software
- **AutoCAD**: Industry-standard CAD
- **DraftSight**: Professional 2D CAD
- **CorelCAD**: CAD with DXF support
- **CAM software**: Mastercam, Fusion 360, etc.

### Online Viewers
- **ShareCAD**: Online DXF viewer
- **A360 Viewer**: Autodesk online viewer
- **Various others**: Search "online DXF viewer"

## Standards and References

### DXF Specification
- **AutoCAD DXF Reference**: Available from Autodesk
- **Open Design Alliance**: DXF specification documentation
- **CAD file format documentation**: Various sources

### Industry Standards
- **ISO 128**: Technical drawings general principles
- **ASME Y14.5**: Dimensioning and tolerancing
- **Company standards**: Internal CAD standards

## Version Control

- Commit DXF files to Git repository
- DXF files are text (ASCII), Git-friendly
- Use Git LFS if binary DXF or large files
- Tag releases with version identifiers
- Document export settings in commit messages

## Related Directories

- **Source drawings**: `../../DRAWINGS/`
- **3D models**: `../../MODELS/` and `../../ASSEMBLIES/`
- **Other formats**: `../STEP/`, `../IGES/`, `../JT/`
- **Data exchange standards**: `/00-PROGRAM/STANDARDS/04-CROSS_CUTTING/DATA_EXCHANGE/`

## Troubleshooting

### Cannot Open File
- Try different DXF viewer
- Check DXF version (try older version)
- Verify file is not corrupted
- Re-export from source

### Geometry Issues
- **Missing lines**: Check layer visibility
- **Incorrect scale**: Verify units on export
- **Duplicate geometry**: Clean up in source
- **Open contours**: Check endpoint connections

### Dimension Problems
- **Missing dimensions**: May not export from some systems
- **Incorrect values**: Check dimension associativity
- **Display issues**: Dimension style compatibility

### Text Issues
- **Missing text**: Check font substitution
- **Wrong size**: Text height not exported
- **Special characters**: Use standard ASCII characters

## Best Use Strategy

### Workflow Recommendation
1. **Create 3D model** in CAD system
2. **Generate 2D drawing** with dimensions
3. **Export to PDF** for reference
4. **Export to DXF** for manufacturing
5. **Validate** DXF in neutral viewer
6. **Package** with documentation
7. **Distribute** to manufacturer

### Quality Assurance
- Always validate DXF before distribution
- Test in recipient's software if possible
- Provide PDF as reference
- Support with clear documentation
- Respond promptly to manufacturer questions

## Future Considerations

DXF remains the 2D standard, but consider:
- **3D formats**: STEP for 3D geometry
- **PDF/3D**: For integrated documentation
- **Native formats**: If using common tools
- **Cloud collaboration**: Online platforms for design sharing

DXF will remain relevant for 2D manufacturing for the foreseeable future.
