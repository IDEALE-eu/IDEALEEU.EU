# IGES — IGES Format Exports

## Purpose

This directory contains IGES (Initial Graphics Exchange Specification) format exports for legacy system compatibility.

## IGES Format

### Standard
- **ANSI/US PRO/IPO-100**: IGES specification
- **Version**: IGES 5.3 (most common)

### Important Note
**IGES is a legacy format. Use STEP (AP242) whenever possible.**

IGES has significant limitations:
- No assembly structure support
- No PMI (annotations, GD&T)
- Limited solid model support
- Potential geometry translation errors
- No material properties

## When to Use IGES

### Acceptable Use Cases
- Partner/supplier requires IGES (no STEP capability)
- Legacy system compatibility
- Specific analysis tools requiring IGES
- Customer contract specifies IGES

### Always Prefer STEP
- STEP is the industry standard
- Better geometry fidelity
- Includes assembly structure
- Supports PMI and annotations
- Better long-term support

## Export Settings

### Recommended Settings
- **Version**: IGES 5.3
- **Geometry**: Bounded surfaces or solids (if supported)
- **Units**: Millimeters (consistent with CAD)
- **Tolerances**: Tight tolerances (0.001 mm)
- **Assembly**: Export as multiple files (no assembly structure)

## File Types

- `.igs` / `.iges` — IGES format files

## Naming Convention

```
53-10_ASM_CENTER-BODY_<config>_<version>.igs
```

Examples:
- `53-10_ASM_CENTER-BODY_COMPLETE_v01.igs`
- `53-10_ASM_CENTER-BODY_SIMPLIFIED_v02.iges`

## Export Validation

### Critical Checks
- [ ] File opens in target system
- [ ] Geometry is complete (no missing surfaces)
- [ ] Dimensions are accurate (±0.01mm)
- [ ] No gaps or overlaps
- [ ] Surface normals correct
- [ ] File size reasonable

### Known Issues
- **Gap tolerance**: May create gaps between surfaces
- **Solid conversion**: May convert solids to surfaces
- **Trimmed surfaces**: May lose trim boundaries
- **Assembly**: No assembly structure preserved
- **PMI**: All annotations lost

## Alternative Recommendations

If partner requires IGES, consider:
1. **Request STEP support**: Modern CAD systems support STEP
2. **Provide both formats**: STEP as primary, IGES as fallback
3. **Validate thoroughly**: Check imported geometry carefully
4. **Document issues**: Note any translation problems

## Related Formats

- **STEP**: [`../STEP/`](../STEP/) — Preferred modern format (use instead!)
- **JT**: [`../JT/`](../JT/) — Lightweight visualization
