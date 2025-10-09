# STEP — STEP Format Exports

## Purpose

This directory contains STEP (Standard for the Exchange of Product model data) format exports of the top-level assembly.

## STEP Format

### Standard
- **ISO 10303-242** (AP242): Managed model-based 3D engineering
- **ISO 10303-214** (AP214): Automotive design (legacy)

### Advantages
- **Complete geometry**: Solids, surfaces, curves
- **Assembly structure**: Hierarchical product structure
- **PMI support**: Product Manufacturing Information (AP242)
- **Long-term archival**: Stable, well-documented format
- **Wide compatibility**: Supported by all major CAD systems

## Export Settings

### Recommended Settings
- **Protocol**: AP242 (preferred) or AP214
- **Geometry**: Include all solid and surface data
- **Assembly**: Preserve full assembly hierarchy
- **PMI**: Include annotations and GD&T (AP242)
- **Units**: Millimeters (consistent with CAD model)
- **Validation**: Enable geometry validation

### Configuration
- **Level of detail**: Match source model
- **Tessellation**: Use high-quality settings
- **Colors/layers**: Export visual attributes
- **Properties**: Include material properties

## File Types

- `.stp` / `.step` — STEP format files
- `.stpx` — Compressed STEP (AP242)

## Naming Convention

```
53-10_ASM_CENTER-BODY_<config>_<version>.stp
```

Examples:
- `53-10_ASM_CENTER-BODY_COMPLETE_v01.stp`
- `53-10_ASM_CENTER-BODY_SIMPLIFIED_v02.step`
- `53-10_ASM_CENTER-BODY_LIGHTWEIGHT_v01.stpx`

## Export Validation

### Geometry Checks
- [ ] All surfaces and solids present
- [ ] No gaps or missing geometry
- [ ] Assembly structure intact
- [ ] Part instances correct
- [ ] Units match source model

### Quality Checks
- [ ] File opens in neutral viewer
- [ ] File opens in target CAD system
- [ ] Geometry accuracy within tolerance (< 0.01mm)
- [ ] File size reasonable (< 500 MB for assemblies)
- [ ] PMI preserved (if using AP242)

## Use Cases

### Internal Use
- CAD system interoperability
- Long-term data archival
- Backup and recovery

### External Exchange
- Customer deliveries
- Supplier interfaces
- Analysis preparation (CAE)
- Certification submissions

## Related Formats

- **JT**: [`../JT/`](../JT/) — Lightweight visualization
- **IGES**: [`../IGES/`](../IGES/) — Legacy format
