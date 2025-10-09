# IGES — Initial Graphics Exchange Specification

## Purpose

This directory contains IGES (Initial Graphics Exchange Specification) format exports for 3D geometry exchange, particularly with legacy systems and specialized manufacturing tools.

## Overview

**IGES** is a veteran neutral CAD format (since 1980):
- **Widely supported**: Nearly universal CAD system compatibility
- **Mature standard**: Stable format with decades of use
- **Surfaces and wireframe**: Excellent for complex surface geometry
- **Manufacturing**: Commonly used in CAM and CNC systems
- **Legacy integration**: Many older systems only support IGES

## When to Use IGES

### Preferred Use Cases
- **Legacy systems**: Partner/supplier uses older CAD systems
- **CAM systems**: CNC programming tools that prefer IGES
- **Surface modeling**: Complex Class-A surfaces
- **Wireframe**: Curve and point data exchange
- **Supplier requirement**: Customer specifically requests IGES

### Limitations
- ❌ No PMI/GD&T: Annotations not supported
- ❌ No assembly structure: Limited assembly support
- ❌ No attributes: Minimal metadata capability
- ❌ Accuracy issues: Potential tolerance problems
- ⚠️ Ambiguous spec: Implementation varies by CAD vendor

### Modern Alternative
**Use STEP AP242 instead** unless:
- Partner specifically requires IGES
- Legacy system cannot read STEP
- CAM system performs better with IGES

## What to Store

### Part Files
- **Solid models**: B-rep solids (support varies by CAD system)
- **Surface models**: NURBS surfaces, trimmed surfaces
- **Wireframe**: Curves, lines, arcs, splines
- **Points**: Point clouds, construction points
- **Simple assemblies**: Limited assembly structure (not recommended)

### Geometry Types Supported
- ✅ NURBS surfaces
- ✅ Trimmed surfaces
- ✅ B-rep solids (with caveats)
- ✅ Curves and wireframe
- ✅ Points
- ⚠️ Assemblies (limited support)
- ❌ PMI/annotations
- ❌ Attributes/metadata (minimal)

## File Format

### File Extension
- `.iges` or `.igs` (both acceptable)
- Use lowercase for consistency: `.igs`

### File Structure
IGES files are ASCII text with fixed-width fields:
```
                                                                        S      1
1H,,1H;,7Hexample,11Hexample.igs,...                                   G      1
     308       1       0       0       0       0       0       000000000D      1
     308       0       2       1       0                               D      2
308,0.0,0.0,0.0,1.0,0.0,0.0,0.0,1.0,0.0;                             P      1
```

Sections:
- **S**: Start (comments)
- **G**: Global parameters
- **D**: Directory entry (entity index)
- **P**: Parameter data (entity data)
- **T**: Terminate

## IGES Versions

### Recommended Version
- **IGES 5.3** (1996): Most widely supported, stable
- Older versions (5.1, 5.2) also acceptable
- Avoid IGES 6.0 (limited adoption)

### Version Selection
Check with recipient for preferred version:
- Most systems support IGES 5.3
- Some older systems require IGES 5.1
- IGES 6.0 rarely required

## Naming Convention

Use the following naming pattern:
```
<subsystem>_<component>_<part-number>_<revision>_<date>.igs
```

Examples:
- `53-10_FRAME-F01_PN-12345_RevB_20250110.igs`
- `53-10_SKIN-PANEL_PN-12346_RevA_20250110.igs`
- `53-10_SURFACE_OML_PN-98765_RevA_20250110.igs`

## Export Settings

### Recommended Export Options

**Geometry Type**:
- ☑ Trimmed surfaces (for surfaces)
- ☑ B-rep solids (if supported)
- ☑ Export all visible entities
- ☑ Include construction geometry (if needed)

**Units**:
- ☑ Millimeters or inches (specify in global section)
- ☑ Match source model units

**Tolerance**:
- ☑ Set resolution: 0.001 mm (or 0.0001 inches)
- ☑ Use tight tolerance for precision

**Options**:
- ☑ IGES version: 5.3
- ☑ Entity type: Trimmed surfaces or B-rep
- ☑ Export all layers
- ☐ Skip PMI/annotations (not supported)

### CAD System-Specific Settings

#### CATIA V5/V6
- File → Export → IGES
- Version: `IGES 5.3`
- Output: Trimmed surfaces or B-rep solid

#### Siemens NX
- File → Export → IGES
- Version: `5.3`
- Type: Trimmed parametric surfaces or solid

#### SolidWorks
- File → Save As → IGES
- Options: Trimmed surfaces or solid entities

#### Creo (PTC)
- File → Save a Copy → IGES
- Version: 5.3
- Entities: Surfaces or solids

## Validation

### Opening and Checking IGES Files
Test IGES files by:
- Importing into CAD system (different from export system)
- Visual inspection in IGES viewer
- Checking geometry completeness
- Verifying units and scale
- Measuring critical dimensions

### Validation Checklist
Before committing IGES files:
- [ ] File opens without errors
- [ ] All surfaces/solids imported
- [ ] No missing or invalid geometry
- [ ] Units are correct
- [ ] Scale is 1:1 (no scaling applied)
- [ ] File size reasonable
- [ ] Naming convention followed

### Common Issues

**Missing surfaces**:
- Some surfaces may not export
- Check for unsupported geometry types
- Simplify complex features if needed

**Import errors**:
- Different CAD systems interpret IGES differently
- Test with recipient's CAD system if possible
- Use STEP if problems persist

**Inaccurate geometry**:
- IGES has lower precision than STEP
- Use tighter tolerance settings
- Consider STEP for high-precision work

**Large file size**:
- IGES files can be large
- Complex surfaces create many entities
- Consider simplification for distribution

## Use Cases

### Manufacturing
- **CAM programming**: CNC toolpath generation
- **Sheet metal**: Flat pattern development
- **Laser cutting**: 2D profiles for cutting
- **Reverse engineering**: Surface recreation

### Legacy Systems
- Partner/supplier with older CAD tools
- Systems that don't support STEP
- Established workflows requiring IGES

### Surface Modeling
- Exchange of Class-A surfaces
- Automotive body panels
- Aircraft exterior surfaces (OML)
- Complex lofted shapes

### Specialized Tools
- Inspection software
- CMM programming
- Optical scanning software
- Some FEA preprocessors

## Best Practices

### When to Use Each Format

| Requirement | Recommended Format |
|-------------|-------------------|
| Modern CAD exchange | STEP AP242 |
| Legacy system | IGES 5.3 |
| PMI/GD&T needed | STEP AP242 |
| Assembly structure | STEP AP242 |
| Surface-only | IGES or STEP |
| CAM programming | IGES or STEP |
| Long-term archival | STEP AP242 |

### Export Quality
- Start from validated CAD models
- Remove construction geometry unless needed
- Check surface normals (outward-facing)
- Verify closed volumes for solids
- Test import before distribution

### Metadata
IGES has limited metadata capability. Include separately:
- Part number and revision
- Material specification
- Units (mm or inches)
- Export date and CAD system
- Reference to STEP file (if available)

### Documentation
Accompany IGES files with:
- PDF drawings with dimensions
- Material specifications
- Special instructions or notes
- Reference to native CAD files

## File Size Considerations

### Typical File Sizes
- **Simple parts**: 50 KB - 2 MB
- **Complex surfaces**: 2 MB - 20 MB
- **Large assemblies**: 10 MB - 100 MB+

### Reducing File Size
If IGES files are too large:
- Simplify geometry (remove small features)
- Reduce surface complexity
- Export sub-assemblies separately
- Use tighter surface tolerance (fewer facets)

## Troubleshooting

### Import Errors
**"Invalid entity" errors**:
- Some CAD systems create non-standard entities
- Try exporting with different entity types
- Use STEP if problems persist

**Missing geometry**:
- Check export options (all layers visible)
- Verify geometry is valid in source model
- Some features may not be supported

**Scale problems**:
- Verify units match (mm vs. inches)
- Check global scale parameter
- Re-export with explicit unit setting

**Slow import**:
- Large file with many entities
- Simplify geometry if possible
- Use subset or level-of-detail export

### Compatibility Issues
Different CAD systems implement IGES differently:
- **Best practice**: Test with recipient's system
- **Fallback**: Use STEP AP242 instead
- **Alternative**: Provide both IGES and STEP

## Related Directories

- **Source models**: `../../MODELS/` and `../../ASSEMBLIES/`
- **Other formats**: `../STEP/`, `../JT/`, `../DXF/`
- **Drawings**: `../../DRAWINGS/`

## Standards and References

### IGES Standards
- **IGES 5.3** (1996): Current stable version
- **ANSI US PRO/IPO-100-1996**: Official standard
- **Legacy versions**: 5.1, 5.2, 4.0

### Documentation
- **IGES Specification**: Available from ANSI
- **CAD vendor documentation**: Implementation notes
- **CAx-IF**: Translator testing and validation

## Tools and Software

### IGES Viewers (Free)
- **eDrawings**: Free viewer from SolidWorks
- **FreeCAD**: Open-source with IGES import
- **IDA-STEP IGES Viewer**: Specialized IGES viewer

### IGES Translators
- **TransMagic**: Multi-format translator
- **Theorem CADverter**: Format conversion tool
- **Datakit CrossManager**: Universal translator
- Built-in CAD system import/export

## Migration Recommendation

### Transition to STEP
IGES is a legacy format. Plan to transition to STEP AP242:
- **New projects**: Use STEP as primary format
- **Existing workflows**: Gradually adopt STEP
- **Partner education**: Encourage STEP adoption
- **Maintain IGES**: Only when specifically required

### Benefits of STEP over IGES
- ✅ PMI/GD&T support
- ✅ Assembly structure
- ✅ Attributes and metadata
- ✅ Better accuracy
- ✅ Clear specification
- ✅ Long-term archival
- ✅ Aerospace industry standard

## Version Control

- Commit IGES files to Git repository
- Use Git LFS for files > 10 MB
- Tag releases with version identifiers
- Cross-reference to STEP files (provide both when possible)
- Document export parameters in commit messages
