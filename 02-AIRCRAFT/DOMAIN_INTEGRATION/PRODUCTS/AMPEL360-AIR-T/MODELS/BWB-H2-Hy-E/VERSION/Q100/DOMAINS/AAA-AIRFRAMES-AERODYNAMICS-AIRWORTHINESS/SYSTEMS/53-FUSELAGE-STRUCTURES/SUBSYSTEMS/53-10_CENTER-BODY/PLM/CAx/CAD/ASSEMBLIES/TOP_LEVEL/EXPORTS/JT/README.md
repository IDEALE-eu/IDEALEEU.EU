# JT — JT Format Exports

## Purpose

This directory contains JT (Jupiter Tessellation) format exports of the top-level assembly for lightweight visualization and collaboration.

## JT Format

### Standard
- **ISO 14306**: Industrial automation systems — JT file format specification
- **Current version**: JT Open v10.x or later

### Advantages
- **Lightweight**: 5-20x smaller than native CAD
- **Fast loading**: Optimized for visualization
- **PMI support**: Product Manufacturing Information
- **Multi-CAD**: Neutral across CAD systems
- **Secure**: Can exclude proprietary geometry
- **Progressive loading**: Level-of-detail (LOD) streaming

## JT File Types

### By Detail Level
- **JT with geometry**: Full geometric representation
- **JT with tessellation only**: Faceted representation
- **JT with PMI**: Includes annotations and GD&T
- **Monolithic JT**: Single file with all references
- **Shattered JT**: Multiple files with assembly structure

## Export Settings

### Recommended Settings
- **Format**: JT Open (not proprietary JT)
- **LOD**: Multiple levels of detail
- **Tessellation quality**: Fine or extra fine
- **PMI**: Include if available
- **Structure**: Preserve assembly hierarchy
- **Attributes**: Include material and color

### Performance Options
- **Target file size**: < 50 MB for assemblies
- **Target load time**: < 5 seconds
- **LOD levels**: 3-5 levels for large assemblies

## File Types

- `.jt` — JT format files

## Naming Convention

```
53-10_ASM_CENTER-BODY_<config>_<version>.jt
```

Examples:
- `53-10_ASM_CENTER-BODY_COMPLETE_v01.jt`
- `53-10_ASM_CENTER-BODY_LIGHTWEIGHT_v02.jt`
- `53-10_ASM_CENTER-BODY_REVIEW_v01.jt`

## Export Validation

### Quality Checks
- [ ] File opens in JT viewer
- [ ] Visual quality acceptable
- [ ] Assembly structure preserved
- [ ] LOD transitions smooth
- [ ] File size meets target
- [ ] Load time acceptable

### Visual Verification
- [ ] Colors and materials correct
- [ ] Overall dimensions accurate
- [ ] Key features visible
- [ ] No missing components

## Use Cases

### Visualization
- Design reviews and presentations
- Web-based 3D viewers
- Mobile device viewing
- Marketing and sales

### Collaboration
- Sharing with external partners
- Supplier coordination
- Customer reviews
- Non-CAD user access

### Analysis
- Digital mock-ups (DMU)
- Interference checking
- Kinematics simulation
- Assembly planning

## Viewing Tools

- **Siemens JT2Go**: Free JT viewer
- **3DViewStation**: Commercial viewer
- **Web viewers**: Various browser-based options

## Related Formats

- **STEP**: [`../STEP/`](../STEP/) — Full geometry exchange
- **IGES**: [`../IGES/`](../IGES/) — Legacy format
