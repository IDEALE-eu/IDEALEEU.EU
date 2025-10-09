# JT — ISO 14306 Lightweight Visualization Format

## Purpose

This directory contains JT (Jupiter Tessellation) format exports for lightweight visualization, design reviews, and PLM system integration.

## Overview

**JT** is an industry-standard format for 3D visualization:
- **Lightweight**: Highly compressed for fast loading and viewing
- **Visualization**: Optimized for display, not editing
- **Large assemblies**: Handles complex assemblies efficiently
- **PLM integration**: Native format for many PLM systems
- **Free viewers**: JT2Go free viewer from Siemens
- **ISO standard**: ISO 14306 international standard

## When to Use JT

### Primary Use Cases
- **Design reviews**: Share models with non-CAD users
- **Visualization**: 3D model viewing without CAD license
- **Large assemblies**: Fast loading of complex assemblies
- **PLM systems**: Teamcenter, Windchill, 3DEXPERIENCE
- **Collaboration**: Stakeholder reviews, supplier coordination
- **Marketing**: Product presentations, sales demonstrations

### Advantages
- ✅ Very small file sizes (compression)
- ✅ Fast loading and rendering
- ✅ Free viewer available (JT2Go)
- ✅ PMI visualization (annotations, GD&T)
- ✅ Assembly structure preserved
- ✅ Multiple levels of detail (LOD)
- ✅ Metadata and attributes

### Limitations
- ❌ Not editable: View-only format
- ❌ Tessellated geometry: Not exact (faceted)
- ❌ Not for manufacturing: Use STEP for production
- ⚠️ Proprietary origin: Siemens format (now ISO standard)

## What to Store

### Visualization Files
- **Part models**: Individual components for review
- **Assemblies**: Complete product structures
- **Large assemblies**: Aircraft-level assemblies
- **PMI views**: Models with embedded GD&T
- **Review sets**: Design review packages

### Content Included
- ✅ Tessellated geometry (triangle meshes)
- ✅ Assembly structure and hierarchy
- ✅ PMI/annotations (if exported)
- ✅ Metadata and attributes
- ✅ Multiple representations (LOD)
- ✅ Viewpoints and section planes
- ✅ Mass properties

## File Format

### File Extension
- `.jt` (only option)

### JT Versions
- **JT 10.x**: Latest version, ISO 14306 standard
- **JT 9.5**: Widely supported, stable
- **JT 8.1**: Legacy, Teamcenter compatibility

**Recommended**: Use latest JT version unless PLM system requires specific version.

## Naming Convention

Use the following naming pattern:
```
<subsystem>_<component>_<part-number>_<revision>_<date>.jt
```

Examples:
- `53-10_FRAME-F01_PN-12345_RevB_20250110.jt`
- `53-10_ASM_CENTER-BODY_PN-10000_RevA_20250110.jt`
- `53-10_SKIN-PANEL_PN-12346_RevA_20250110.jt`

## Export Settings

### Recommended Export Options

**Geometry**:
- ☑ Tessellated (triangle mesh)
- ☑ Medium to high resolution
- ☑ Export all visible bodies
- ☑ Assembly structure

**Compression**:
- ☑ High compression (for distribution)
- ☑ Medium compression (for PLM)
- ☑ Balance size vs. visual quality

**PMI**:
- ☑ Include PMI/annotations
- ☑ Dimension and tolerance data
- ☑ GD&T feature control frames
- ☑ Notes and callouts

**Metadata**:
- ☑ Part number and revision
- ☑ Material
- ☑ Mass properties
- ☑ Custom attributes

**Level of Detail (LOD)**:
- ☑ Multiple LOD representations
- ☑ High detail for close views
- ☑ Low detail for overview

### CAD System-Specific Settings

#### CATIA V5/V6
- File → Export → JT
- Version: Latest (JT 10.x)
- Options: Tessellated, assembly structure, PMI

#### Siemens NX
- File → Export → JT
- Version: JT 10.x
- Quality: High
- Include: PMI, attributes, structure

#### SolidWorks
- File → Save As → JT
- Options: Include annotations, assembly structure
- Quality: High

#### Creo (PTC)
- File → Save a Copy → JT
- Version: Latest
- Include: Annotations, structure

## JT File Size

### Typical File Sizes
- **Simple parts**: 10 KB - 500 KB
- **Complex parts**: 500 KB - 5 MB
- **Sub-assemblies**: 1 MB - 20 MB
- **Large assemblies**: 10 MB - 200 MB

### Compression Levels
JT offers excellent compression (10:1 to 100:1 vs. STEP):
- **High compression**: Smaller files, slightly lower visual quality
- **Medium compression**: Balanced size and quality
- **Low compression**: Larger files, best visual quality

**Recommendation**: Use high compression for distribution, medium for PLM.

## Validation

### Viewing JT Files
Use **JT2Go** (free from Siemens):
1. Download JT2Go from Siemens website
2. Open JT file
3. Verify geometry displays correctly
4. Check assembly structure (tree view)
5. Inspect PMI if included
6. Validate metadata

### Validation Checklist
Before committing JT files:
- [ ] File opens in JT2Go without errors
- [ ] Geometry visually correct
- [ ] Assembly structure preserved
- [ ] PMI visible and complete (if applicable)
- [ ] Metadata present (part number, etc.)
- [ ] File size reasonable
- [ ] Naming convention followed

## Use Cases

### Design Reviews
- **Internal reviews**: Share with engineering team
- **Management reviews**: Present to leadership
- **Customer reviews**: Coordinate with partners
- **Supplier reviews**: Coordinate with manufacturers

**Benefits**:
- No CAD license required
- Fast loading on standard PCs
- Markup and commenting tools
- Cross-platform (Windows, Mac, Linux)

### PLM System Integration
- **Teamcenter**: Native JT visualization
- **Windchill**: JT for visualization and structure
- **3DEXPERIENCE**: JT import/export
- **Aras Innovator**: JT visualization

### Stakeholder Communication
- **Non-engineers**: Sales, marketing, management
- **Customers**: Design coordination
- **Regulators**: Certification reviews (visual only)
- **Public**: Marketing and demonstrations

### Large Assembly Performance
- **Aircraft assembly**: Entire aircraft in one file
- **Section assemblies**: Major sections (center body, wings)
- **System assemblies**: System-level models

**Benefits**:
- Fast loading (compressed geometry)
- Multiple LOD for performance
- Simplified geometry for overviews
- Detailed geometry for close inspection

## Best Practices

### Complementary Formats
Always provide JT **in addition to** STEP, not instead of:
- **STEP**: For manufacturing and archival
- **JT**: For visualization and reviews
- **PDF**: For drawings and documentation

### Metadata
Include comprehensive metadata:
- Part number and revision
- Material specification
- Mass properties
- Author and date
- Design status (draft, released)
- Effectivity (if applicable)

### Assembly Structure
Maintain logical assembly hierarchy:
- Top-level assembly
- Major sub-assemblies
- Components
- Standard parts

### PMI Export
If exporting PMI:
- Include all critical dimensions
- Export GD&T datums and tolerances
- Add manufacturing notes
- Validate PMI visibility in JT2Go

### Version Control
- Commit JT files to Git repository
- Use Git LFS for files > 10 MB
- Tag releases with version identifiers
- Synchronize with STEP exports
- Document export settings in commit messages

## JT Viewer Software

### Free Viewers
- **JT2Go** (Siemens): Full-featured, free, Windows/Mac/Linux
- **JT Open Toolkit**: Developer toolkit for JT integration

### Commercial Software with JT Support
- **Teamcenter** (Siemens): Native JT PLM system
- **Windchill** (PTC): JT visualization
- **3DEXPERIENCE** (Dassault): JT import/export
- **Aras Innovator**: JT viewing and markup

## Comparison with Other Formats

### JT vs. STEP
| Feature | JT | STEP |
|---------|----|----|
| **Purpose** | Visualization | Manufacturing |
| **Geometry** | Tessellated | Exact (B-rep) |
| **File size** | Very small | Medium to large |
| **Editable** | No | Yes (in CAD) |
| **PMI** | View only | Full definition |
| **Archival** | Not recommended | Primary format |
| **Distribution** | Excellent | Good |

**Recommendation**: Use both formats - JT for reviews, STEP for manufacturing.

### JT vs. 3D PDF
| Feature | JT | 3D PDF |
|---------|----|----|
| **Viewer** | JT2Go | Acrobat Reader |
| **File size** | Smaller | Larger |
| **PMI** | Excellent | Good |
| **Assemblies** | Better support | Limited |
| **Ubiquity** | CAD community | General public |

**Recommendation**: JT for engineering, 3D PDF for general distribution.

## Integration with PLM

### PLM System Workflows
1. **CAD → PLM**: Export JT from CAD, upload to PLM
2. **PLM storage**: JT as visualization representation
3. **PLM distribution**: Distribute JT to stakeholders
4. **PLM visualization**: View JT in PLM web interface

### Metadata Synchronization
Ensure JT metadata matches PLM:
- Part number
- Revision/version
- Material
- Mass
- Custom attributes

### Configuration Management
- Link JT files to CAD source in PLM
- Manage effectivity and variants
- Track design changes
- Control access and permissions

## Standards and References

### ISO Standard
- **ISO 14306**: Industrial automation systems and integration - JT file format specification for 3D visualization

### Industry Adoption
- **ProSTEP iViP**: JT usage recommendations
- **Boeing**: JT for supplier collaboration
- **Airbus**: JT for visualization
- **Automotive OEMs**: Ford, GM, VW use JT extensively

### Documentation
- **JT Open**: Open-source toolkit and specification
- **Siemens PLM**: JT format documentation
- **ProSTEP iViP**: Best practices guides

## Related Directories

- **Source models**: `../../MODELS/` and `../../ASSEMBLIES/`
- **Other formats**: `../STEP/`, `../IGES/`, `../DXF/`
- **Drawings**: `../../DRAWINGS/`
- **Data exchange**: `/00-PROGRAM/STANDARDS/04-CROSS_CUTTING/DATA_EXCHANGE/`

## Best Use Strategy

### Recommended Workflow
1. **Design**: Create in native CAD (CATIA, NX, etc.)
2. **Archive**: Export to STEP AP242 (exact geometry)
3. **Visualize**: Export to JT (lightweight review)
4. **Document**: Create PDF drawings
5. **Distribute**: Provide STEP + JT + PDF

### File Package
When distributing to partners:
```
Package/
├── STEP/          # Manufacturing files
├── JT/            # Visualization files
├── PDF/           # Drawings
└── README.txt     # Instructions and metadata
```

## Troubleshooting

### Cannot Open JT File
- Download latest JT2Go viewer
- Check JT version compatibility
- Verify file is not corrupted (re-export)

### Missing PMI
- Verify PMI export option enabled
- Check CAD system supports JT PMI
- Use JT 9.5 or later for PMI

### Poor Visual Quality
- Increase tessellation resolution
- Use lower compression level
- Check LOD settings

### Large File Size
- Increase compression level
- Reduce tessellation resolution
- Simplify geometry if appropriate
- Export sub-assemblies separately

## Future Direction

JT is evolving with:
- Enhanced PMI capabilities
- Improved compression
- Better metadata support
- Tighter PLM integration
- Cloud-based viewing
- Mobile device support

Stay current with JT standard updates and PLM system requirements.
