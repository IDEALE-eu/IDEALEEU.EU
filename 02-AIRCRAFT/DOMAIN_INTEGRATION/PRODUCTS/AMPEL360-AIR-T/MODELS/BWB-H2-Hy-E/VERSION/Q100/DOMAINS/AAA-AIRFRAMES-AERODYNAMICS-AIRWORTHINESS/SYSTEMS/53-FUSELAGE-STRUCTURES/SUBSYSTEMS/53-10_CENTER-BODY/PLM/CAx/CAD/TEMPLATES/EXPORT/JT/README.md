# JT — JT Export Templates and Settings

## Purpose

Export settings and templates for JT (ISO 14306) format, a lightweight 3D format optimized for visualization and collaboration.

## JT Overview

**Standard:** JT (ISO 14306:2012)

**Advantages:**
- Lightweight file format (10-20x smaller than native CAD)
- Fast loading and viewing of large assemblies
- Supports PMI (Product Manufacturing Information)
- Excellent for design reviews and collaboration
- Widely used in automotive and aerospace
- Compatible with digital mockup (DMU) tools

**Use Cases:**
- Design reviews (non-CAD users)
- Large assembly visualization
- Digital mockup and ergonomics studies
- Collaboration with partners (view-only)
- Mobile/tablet viewing
- Virtual reality (VR) applications

## Export Settings Template

### Recommended Settings
```
Version: JT 10.5 or later
Format: JT

Geometry:
  ☑ Tessellation (faceted representation)
  ☑ BREP (optional, for precise geometry)
  Quality: Medium to High
  ☑ Preserve assembly structure
  ☑ Include component instances

Appearance:
  ☑ Colors (part colors)
  ☑ Textures (if applicable)
  ☑ Transparency
  ☑ Materials (visual appearance)

PMI:
  ☑ Annotations (if needed for review)
  ☑ Dimensions (if needed)
  ☑ GD&T (if applicable)
  ☐ Exclude PMI for lightweight files

Attributes:
  ☑ Part names
  ☑ Part numbers
  ☑ Descriptions
  ☐ Mass properties (optional)

Compression:
  ☑ Enable compression
  Level: Standard or High
  
Units: Millimeters (mm)
Coordinate system: Global aircraft frame
LOD (Level of Detail): Medium to High
```

## CAD System Specific Settings

### CATIA V5
**File → Save As → JT**
- Version: JT 10.5
- Output: Tessellation + BREP (optional)
- Assembly: Preserve structure
- Options: Include attributes

### Siemens NX
**File → Export → JT**
- Version: JT 10.5 or latest
- Output type: Assembly
- Geometry: Facets + BREP (optional)
- PMI: Include if needed
- Compression: High

### SOLIDWORKS
**File → Save As → JT (*.jt)**
- Version: JT 10.5 or later
- Assembly mode: Multi-file (preserves structure)
- Quality: High
- Include: Appearance, structure

### PTC Creo
**File → Save As → Save a Copy**
- Type: JT (*.jt)
- Version: JT 10.5
- Options → Assembly export: Yes
- Options → Include PMI: Optional

## JT Quality Levels

### Tessellation Quality

**Low (Draft):**
- File size: Smallest
- Visual quality: Coarse, faceted appearance
- Use: Quick reviews, very large assemblies

**Medium (Standard):**
- File size: Balanced
- Visual quality: Good appearance, minor faceting
- Use: General design reviews, collaboration
- **Recommended for most uses**

**High (Precise):**
- File size: Larger
- Visual quality: Smooth, minimal faceting
- Use: Detailed reviews, presentations, marketing

### BREP Inclusion

**Tessellation Only:**
- Smallest file size
- Good for visualization only
- No precise measurements

**Tessellation + BREP:**
- Larger file size
- Allows precise measurements
- Better for engineering reviews
- Recommended for design reviews

## File Organization

### Naming Convention
```
<part-number>_<description>_JT_v<version>.jt
```

**Examples:**
- `53-10-001_FRAME-F01_JT_v01.jt`
- `53-10_ASM_CENTER-BODY_COMPLETE_JT_v01.jt`

### Directory Structure
```
JT/
├── ASSEMBLIES/
│   ├── 53-10_ASM_CENTER-BODY_COMPLETE_JT_v01.jt
│   ├── 53-11_ASM_FRAME-SECTION_FWD_JT_v01.jt
│   └── ...
├── PARTS/
│   ├── 53-10-001_FRAME-F01_JT_v01.jt
│   ├── 53-10-002_FRAME-F02_JT_v01.jt
│   └── ...
└── README.md
```

## Validation Checklist

After export, verify:
- [ ] File opens in JT viewer without errors
- [ ] All parts/assemblies are visible
- [ ] Assembly structure is preserved
- [ ] Colors and appearance correct
- [ ] Transparency works (if applicable)
- [ ] File size is reasonable (should be much smaller than native)
- [ ] PMI visible (if included)

## Quality Control

### Visual Inspection
- Open in JT viewer (e.g., Siemens JT2Go, free viewer)
- Check geometry appearance
- Verify assembly structure/hierarchy
- Check colors and transparency
- Review PMI if included

### Performance Check
- File loads quickly (< 30 seconds for large assembly)
- Navigation is smooth (rotation, pan, zoom)
- Selection works correctly
- Cross-sections work (if supported)

## JT Viewers

### Free Viewers
- **Siemens JT2Go**: Free, Windows/Linux, full functionality
- **JT Open Toolkit**: Open source library for developers

### Commercial Viewers
- **Teamcenter Visualization**: Advanced collaboration features
- **Kineo JT**: Collision detection, path planning
- **Cortona3D**: 3D PDF and JT viewing

### Web-Based Viewers
- **3DViewStation WebViewer**: Browser-based JT viewing
- **Cortona3D RapidAuthor**: Web publishing

## Best Practices

### For Design Reviews
- Include PMI (dimensions, GD&T) for engineering reviews
- Use medium to high tessellation quality
- Include BREP for precise measurements
- Preserve assembly structure
- Add part properties for traceability

### For Large Assemblies
- Use medium or low tessellation quality
- Compress aggressively
- Tessellation only (no BREP) for file size
- Consider Level of Detail (LOD) for sub-assemblies

### For Collaboration with Partners
- Medium quality, no BREP (smaller files)
- Include basic attributes (part number, description)
- Exclude sensitive PMI/dimensions if confidential
- Provide JT viewer link for recipients

### For Marketing/Presentations
- High tessellation quality for smooth appearance
- Include colors, textures, transparency
- Exclude technical annotations
- Consider rendering instead if photorealistic needed

## JT vs. Other Formats

### JT vs. STEP
- **JT**: Lightweight, visualization, faster loading
- **STEP**: Precise geometry, data exchange, archival
- **Use JT for:** Reviews, visualization
- **Use STEP for:** Manufacturing, analysis, baseline

### JT vs. PDF 3D
- **JT**: Better for large assemblies, native format for many PLM systems
- **PDF 3D**: More universal (Adobe Reader), smaller ecosystems
- **Use JT for:** Engineering/manufacturing reviews
- **Use PDF 3D for:** Non-technical audiences, documentation

## Troubleshooting

### Common Issues

**Issue:** File size too large
- **Solution:** Reduce tessellation quality, enable compression, exclude BREP

**Issue:** Parts missing or transparent
- **Solution:** Check export settings, verify all components exported, check appearance settings

**Issue:** Assembly structure flattened
- **Solution:** Verify "preserve assembly structure" option enabled

**Issue:** PMI not visible
- **Solution:** Check PMI export option, verify JT viewer supports PMI display

**Issue:** Colors incorrect
- **Solution:** Check appearance export settings, verify material/color assignments in source CAD

**Issue:** Slow loading/performance
- **Solution:** Reduce file size (lower quality, compression), simplify geometry, use LOD

## Related Files

- Parent directory: [`../README.md`](../README.md)
- STEP export: [`../STEP_AP242/README.md`](../STEP_AP242/README.md)
- Main exports: [`../../../EXPORTS/JT/README.md`](../../../EXPORTS/JT/README.md)

## References

- ISO 14306:2012 standard (JT format specification)
- JT Open program (www.plm.automation.siemens.com/jt)
- Siemens JT2Go viewer (free download)
- ProSTEP iViP recommendations for JT usage
