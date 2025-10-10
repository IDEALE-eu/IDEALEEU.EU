# EXPORTS_STEP — STEP Format Exports

## Purpose

This directory contains STEP (Standard for the Exchange of Product model data) format exports for all REL (Released) status assemblies and parts in the 21-10 radiators and heat exchangers subsystem.

## STEP Format

### Standard
- **ISO 10303-242** (AP242): Managed model-based 3D engineering (preferred)
- **ISO 10303-214** (AP214): Automotive design (legacy, if needed)

### Advantages
- **Complete geometry**: Solids, surfaces, curves
- **Assembly structure**: Hierarchical product structure preserved
- **PMI support**: Product Manufacturing Information (AP242)
- **Long-term archival**: Stable, well-documented format
- **Wide compatibility**: Supported by all major CAD systems
- **Vendor neutral**: No dependency on specific CAD software

## Export Requirements

### When to Export
- **Mandatory**: All assemblies and parts at REL status
- **Optional**: RVW status for review purposes
- **Not required**: WIP status

### What to Export
- Top-level assemblies (RAD-PANEL, LPHX, COLDPLATE)
- Subassemblies referenced in top-level assemblies
- Individual parts (facesheets, cores, tubes, manifolds, fins, shims, TIMs)
- Critical interface geometry

## Naming Convention

```
21-10_<type>_<description>__r<NN>__REL.step
```

Examples:
- `21-10_ASSY_RAD-PANEL-L1__r03__REL.step`
- `21-10_ASSY_LPHX-AV__r02__REL.step`
- `21-10_PART_FACESHEET_AL2024__r02__REL.step`
- `21-10_PART_HONEYCOMB-CORE__r01__REL.step`

### File Extensions
- `.stp` or `.step` — Standard STEP format
- `.stpx` — Compressed STEP (AP242 only)

## Export Settings

### Recommended Settings
- **Protocol**: AP242 (preferred) or AP214
- **Geometry**: Include all solid and surface data
- **Assembly**: Preserve full assembly hierarchy
- **PMI**: Include annotations and GD&T (AP242 only)
- **Units**: Millimeters (consistent with CAD model)
- **Validation**: Enable geometry validation before export
- **Coordinate system**: Origin at part/assembly datum origin

### Configuration
- **Level of detail**: Match source model (no simplification)
- **Tessellation**: Not applicable for STEP (use high quality if faces are converted)
- **Colors/layers**: Export visual attributes for reference
- **Properties**: Include material properties and mass
- **Metadata**: Part number, revision, description

## Quality Checks

### Pre-Export Validation
- [ ] CAD model is at REL status
- [ ] Model is error-free (no open surfaces, gaps, invalid geometry)
- [ ] Assembly structure is correct
- [ ] Part/assembly properties populated (mass, material, part number)
- [ ] Coordinate system at correct origin
- [ ] Units set to millimeters

### Post-Export Validation
- [ ] File size reasonable (< 100 MB per file typical)
- [ ] STEP file opens in neutral viewer without errors
- [ ] All geometry present (no missing components)
- [ ] Assembly structure intact with correct hierarchy
- [ ] Part instances correct (quantities match BOM)
- [ ] Units match source model (millimeters)
- [ ] Geometry accuracy within tolerance (< 0.01 mm deviation)
- [ ] PMI preserved (if using AP242 and PMI was included)

### Validation Tools
- CAD system built-in validator
- Neutral STEP viewers (e.g., FreeCAD, SolidView)
- Import into target CAD system (if known)
- Geometry comparison tools

## Use Cases

### Internal Use
- Cross-platform collaboration (mixed CAD environments)
- Long-term archival (vendor-neutral format)
- FEA/CFD pre-processing (import into analysis tools)
- Manufacturing (import into CAM software)

### External Use
- Supplier data exchange (manufacturing partners)
- Customer deliverables (as specified in contract)
- Interface coordination with other subsystems
- Third-party analysis and simulation

## File Organization

### Structure
```
exports_step/
├─ 21-10_ASSY_RAD-PANEL-L1__r03__REL.step
├─ 21-10_ASSY_RAD-PANEL-R1__r03__REL.step
├─ 21-10_ASSY_LPHX-AV__r02__REL.step
├─ 21-10_ASSY_COLDPLATE__r01__REL.step
├─ 21-10_PART_FACESHEET_AL2024__r02__REL.step
├─ 21-10_PART_HONEYCOMB-CORE__r01__REL.step
└─ ...
```

### Version Control
- Keep only current REL revision in directory
- Archive superseded versions (if archival system exists)
- File name revision must match CAD model revision
- Maintain traceability to source CAD file

## Traceability

### EBOM Integration
- STEP exports referenced in EBOM_LINKS.md
- Part numbers in STEP file properties match EBOM
- Assembly structure matches EBOM hierarchy
- BOM quantities verifiable from STEP assembly

### Source Traceability
- Document source CAD file name and location
- Record export date and CAD system version
- Link to corresponding drawing in `../drawings/`
- Cross-reference with CAP process documents

## Export Process

### Standard Workflow
1. Complete CAD model and achieve REL status
2. Verify model quality (no errors, complete geometry)
3. Set export options (AP242, full assembly, millimeters, PMI)
4. Export to STEP format
5. Validate exported file (open in neutral viewer)
6. Name file according to convention
7. Place in `exports_step/` directory
8. Update EBOM_LINKS.md with STEP file reference
9. Archive source CAD file and STEP together

### Quality Gate
- REL status STEP exports reviewed by design authority
- Validation report documenting checks performed
- Approval before distribution to external parties

## Related Directories

- **Assemblies**: [`../assemblies/`](../assemblies/) - Source assembly models
- **Parts**: [`../parts/`](../parts/) - Source part models
- **Drawings**: [`../drawings/`](../drawings/) - Corresponding drawings
- **Exports (DXF)**: [`../exports_dxf/`](../exports_dxf/) - Flat pattern exports
- **EBOM**: [`../../EBOM_LINKS.md`](../../EBOM_LINKS.md) - Engineering BOM with STEP references

## Standards References

- **ISO 10303-242** (AP242): Managed model-based 3D engineering
- **ISO 10303-214** (AP214): Core data for automotive mechanical design processes
- **ASME Y14.41**: Digital Product Definition Data Practices
- **ISO 1101**: Geometrical tolerancing (for PMI in AP242)

---

**Last Updated**: 2025-10-10
