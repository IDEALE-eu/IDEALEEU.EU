# SOLIDS — B-rep Solid Body IGES Exports

## Purpose

This directory contains IGES exports of solid body geometries represented as Boundary Representation (B-rep) models.

## Content

Store IGES files (`.igs` or `.iges`) for:
- **Solid parts**: Complete 3D solid bodies
- **B-rep models**: Boundary representation solids
- **Closed volumes**: Watertight solid geometry
- **Manufacturing parts**: Parts intended for machining or fabrication

## File Naming Convention

```
<subsystem>_<component>_<part-number>_<revision>_<date>.igs
```

**Examples:**
- `53-10_FRAME-F01_PN-12345_RevB_20250110.igs`
- `53-10_BULKHEAD_PN-12346_RevA_20250110.igs`

## Export Requirements

When exporting solids to IGES:
- ✅ Use IGES version 5.3
- ✅ Select B-rep solid entity type (typically entity 186)
- ✅ Verify closed volumes before export
- ✅ Use millimeters for units (document in file metadata)
- ✅ Set tolerance to 0.001 mm for precision

## CAD System Export Paths

- **CATIA V5/V6**: File → Export → IGES → Select "B-rep solid"
- **Siemens NX**: File → Export → IGES → Type: "Solid"
- **SolidWorks**: File → Save As → IGES → Options: "Solid entities"
- **Creo (PTC)**: File → Save a Copy → IGES → Entities: "Solids"

## Validation Checklist

Before committing IGES solid files:
- [ ] File opens without errors in target system
- [ ] All solid bodies imported correctly
- [ ] No missing faces or surfaces
- [ ] Volume is closed (no gaps or holes)
- [ ] Units and scale are correct (1:1)
- [ ] File size is reasonable

## Related Directories

- **Parent**: [`../`](../) — All PARTS exports
- **Alternatives**: [`../SURFACES/`](../SURFACES/) — Surface-only geometry
- **Alternatives**: [`../CURVES/`](../CURVES/) — Wireframe geometry
- **Source**: [`../../../MODELS/`](../../../MODELS/) — Native CAD models

## Best Practices

- Export from validated, error-free CAD models
- Remove construction geometry before export
- Test import in neutral viewer before distribution
- Cross-reference to STEP files when possible (STEP has better solid support)
- Document any export issues or limitations

## Migration Note

**Consider using STEP AP242** for solid exchanges:
- Better accuracy and solid representation
- Broader CAD system support
- Includes PMI and metadata
- Preferred format for modern workflows

Use IGES solids only when specifically required by legacy systems or partners.
