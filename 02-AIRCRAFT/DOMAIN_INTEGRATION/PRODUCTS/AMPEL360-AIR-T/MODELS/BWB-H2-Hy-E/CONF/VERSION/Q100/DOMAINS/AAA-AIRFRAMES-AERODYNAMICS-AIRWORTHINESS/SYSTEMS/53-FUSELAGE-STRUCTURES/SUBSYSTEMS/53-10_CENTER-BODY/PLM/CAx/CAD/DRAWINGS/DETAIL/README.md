# DETAIL — Detail Drawings

## Purpose

This directory contains detail drawings that provide enlarged views of specific features, critical areas, or complex details from part or assembly drawings.

## What to Store

### Detail Drawing Types
- **Enlarged details**: Close-up views of small or complex features (2X, 4X, 10X scale)
- **Section details**: Sectioned views showing internal construction
- **Interface details**: Close-up views of critical interfaces and joints
- **Feature details**: Specific features (holes, slots, pockets, fillets)
- **Construction details**: Typical construction methods and techniques
- **Repair details**: Standard repair procedures and patches

## Content Requirements

### Mandatory Information
- **Scale**: Enlarged scale factor (e.g., 2:1, 4:1, 10:1)
- **Detail reference**: Reference to parent drawing and view
- **Dimensions**: All dimensions for the detailed feature
- **Tolerances**: Specific tolerances for critical features
- **Surface finish**: Finish requirements for detailed surfaces
- **Notes**: Manufacturing or inspection notes specific to detail
- **Materials**: Material callouts if different from parent

## Naming Convention

```
53-10_DWG_DETAIL_<feature-name>_<drawing-number>_<sheet>_<revision>.<ext>
```

### Examples
- `53-10_DWG_DETAIL_FRAME-FITTING-TYPE-A_D3000_SH1_RevA.pdf`
- `53-10_DWG_DETAIL_STRINGER-CLIP-STANDARD_D3010_SH1_RevB.pdf`
- `53-10_DWG_DETAIL_SKIN-JOINT-TYPICAL_D3020_SH1_RevA.pdf`
- `53-10_DWG_DETAIL_FASTENER-PATTERN-FP-01_D3100_SH1_RevA.pdf`

## Detail Types

### Geometric Details
- **Hole patterns**: Bolt hole layouts and spacing
- **Edge treatments**: Edge distance, radius, chamfer details
- **Compound angles**: Complex angular features
- **Form features**: Pockets, bosses, ribs, gussets
- **Contoured surfaces**: Complex surface profiles

### Construction Details
- **Joint details**: Lap joints, butt joints, joggle joints
- **Fastener installations**: Countersunk, protruding, blind fasteners
- **Seal installations**: Seal groove details and specifications
- **Bonding**: Adhesive bond preparation and application
- **Welding**: Weld joint details and specifications

### Interface Details
- **Mating surfaces**: Surface preparation and flatness requirements
- **Alignment features**: Holes, pins, keys for alignment
- **Clearance details**: Minimum clearances at interfaces
- **Sealing surfaces**: O-ring grooves, gasket surfaces
- **Hardware installations**: Insert installations, bushing fits

## Organization

Organize detail drawings by:
- **Feature type**: Fittings, joints, fastener patterns, typical sections
- **Application**: Primary structure, secondary structure, installations
- **Reusability**: Standard details vs. unique details

## Detail Views

### View Types
- **Enlarged plan view**: Top view at enlarged scale
- **Enlarged section**: Section view at enlarged scale
- **Isometric detail**: 3D representation of complex feature
- **Exploded detail**: Showing assembly of detailed components
- **Multiple views**: Multiple orientations of same detail

### Dimensioning
- Dimension all features completely at detail scale
- Use appropriate precision for enlarged scale
- Apply GD&T to critical features
- Reference datums from parent drawing
- Note tolerances clearly

## Related Directories

- **CAD models**: [`../../MODELS/`](../../MODELS/)
- **Part drawings**: [`../PART/`](../PART/) - Parent part drawings
- **Assembly drawings**: [`../ASSEMBLY/`](../ASSEMBLY/) - Parent assembly drawings
- **Zone organization**: [`../ZONES/`](../ZONES/)
- **Revisions**: [`../REVISIONS/`](../REVISIONS/)

## Best Practices

### Creating Details
- Choose appropriate scale for clarity
- Include reference to parent drawing
- Show detail boundary on parent view
- Dimension completely at detail scale
- Include all necessary notes
- Maintain consistent standards

### Standard Details
- Create reusable standard details for common features
- Assign standard detail numbers (e.g., SD-001, SD-002)
- Reference standard details on parent drawings
- Maintain library of standard details
- Update standard details via revision control

### Detail References
- Use detail callout symbols on parent drawings
- Include drawing number and sheet reference
- Show detail boundary clearly
- Orient detail view logically relative to parent
- Note scale and orientation

## Quality Requirements

### Pre-Release Checklist
- [ ] Scale factor clearly shown
- [ ] Parent drawing referenced
- [ ] All features dimensioned
- [ ] Tolerances specified
- [ ] Surface finish noted
- [ ] Manufacturing notes complete
- [ ] Detail boundary clear on parent
- [ ] Orientation logical

## Typical Standard Details

### Structural Details
- **SD-001**: Standard frame-to-stringer clip
- **SD-002**: Standard skin splice joint
- **SD-003**: Standard doubler installation
- **SD-004**: Standard fastener edge distance
- **SD-005**: Standard repair patch

### Fastener Details
- **FD-001**: Standard countersunk fastener installation
- **FD-002**: Standard protruding head installation
- **FD-003**: Standard blind fastener installation
- **FD-004**: Standard rivet pattern - single row
- **FD-005**: Standard rivet pattern - double row

## References

- **Parent README**: [`../README.md`](../README.md) - General drawing standards
- **MODELS**: [`../../MODELS/README.md`](../../MODELS/README.md) - Source CAD models
- **Standards**: `/00-PROGRAM/STANDARDS/` - Detail drawing standards
