# COATING_MASKS — Coating and Masking Geometry

## Purpose

This directory contains CAD models for coating masks, paint masks, secondary surface mirror (SSM) masks, and keep-out geometry used in surface treatment processes for 21-10 radiators and heat exchangers.

## Content

### Mask Types
- **Paint masks**: Templates for selective painting
- **SSM masks**: Masks for secondary surface mirror (SSM) coating application
- **Coating masks**: General coating application masks
- **Keep-out geometry**: Areas to be protected from coating
- **Masking templates**: Tape/film application guides

### What to Store
- 3D CAD models of masks (native and neutral formats)
- 2D patterns for flat masks
- Keep-out zone geometry definitions
- Application instructions
- Material specifications for mask construction

## Naming Convention

```
21-10_MASK_<type>_<description>__r<NN>__<status>.<ext>
```

Examples:
- `21-10_MASK_PAINT_RAD-PANEL-WHITE__r01__REL.step`
- `21-10_MASK_SSM_FACESHEET-AREA__r02__RVW.dxf`
- `21-10_MASK_KEEPOUT_MOUNTING-HOLES__r01__WIP.prt`

### Status Codes
- **WIP**: Work in progress
- **RVW**: In review
- **REL**: Released

## Design Standards

### Units
- Length: millimeters (mm)
- Thickness: millimeters (mm)
- Angles: degrees (deg)

### Material Selection
- **Rigid masks**: Aluminum sheet, plastic, composite
- **Flexible masks**: Polyimide tape, vinyl, rubber
- **High-temperature masks**: Silicone, metal foil
- Consider coating process temperature and chemistry

### Tolerances
- Mask edge tolerances: ±0.5 mm typical
- Critical boundary edges: ±0.1 mm
- Registration features: ±0.05 mm

## Mask Design Considerations

### Paint Masks
- Define painted vs. unpainted areas
- Include registration features for alignment
- Provide adequate coverage beyond edge boundaries
- Consider over-spray protection
- Document paint type and thickness

### SSM Masks
- Precise definition of SSM application area
- Protect non-SSM surfaces (mounting interfaces, etc.)
- Account for edge taper in SSM deposition
- Temperature resistance for vacuum deposition process
- Clean room compatible materials

### Keep-Out Geometry
- Define areas that must remain uncoated
- Mounting hole patterns
- Electrical bonding surfaces
- Threaded holes and inserts
- Mating surfaces requiring specific finish

## Color Coding for PMI

Use consistent color coding in CAD models:
- **Structure**: Gray
- **Fluid passages**: Blue
- **TIM areas**: Orange
- **Coating areas**: Pink

## Application Requirements

### Mask Design
- [ ] Covers intended area with adequate margin
- [ ] Registration features for repeatable positioning
- [ ] Attachment method defined (adhesive, mechanical, magnetic)
- [ ] Handling features for application and removal
- [ ] Durability for expected number of uses

### Process Integration
- [ ] Compatible with coating process (spray, dip, vacuum)
- [ ] Temperature and chemical resistance adequate
- [ ] Cleaning and maintenance procedures defined
- [ ] Storage requirements documented

## Documentation Requirements

### For Each Mask
- [ ] 3D model showing mask installed on part
- [ ] 2D pattern for flat masks (DXF export)
- [ ] STEP export for complex 3D masks
- [ ] Application procedure with photos/diagrams
- [ ] Material specification
- [ ] Reuse limits and inspection criteria
- [ ] Link to coating specification (CAP/coating_spec)

### Coating Specifications
- Reference coating specification documents
- Paint/coating type and supplier
- Application method and parameters
- Cure schedule
- Thickness requirements
- Quality acceptance criteria

## Keep-Out Zones

### Areas Typically Protected
- **Mounting surfaces**: Maintain metal-to-metal contact
- **Threaded holes**: Prevent thread contamination
- **Bonding surfaces**: Ensure proper adhesion
- **Electrical contact points**: Ground/bond connections per 51 standards
- **Fluid ports**: Threads and sealing surfaces
- **Optical surfaces**: Maintain specified reflectivity/emissivity

### Documentation
- Clearly mark keep-out zones on drawings
- Reference interface control documents (ICDs)
- Cross-reference with thermal control requirements
- Document rationale for each keep-out zone

## Surface Treatment Requirements

### Radiator Surfaces
- **Thermal emissivity**: High emissivity coating (ε > 0.85)
- **Solar absorptivity**: Low absorptivity desired (α < 0.25)
- **Coating type**: White paint, SSM, or other per thermal analysis
- **Thickness control**: Minimize mass impact

### Interface Surfaces
- **Coldplate interfaces**: No coating, maintain flatness
- **TIM contact areas**: Clean, specified surface finish
- **Mounting surfaces**: Bare metal or specified finish
- **Ground points**: Bare metal for electrical continuity

## Quality Control

### Mask Verification
- [ ] First article inspection against 3D model
- [ ] Fit check on actual part or master model
- [ ] Edge alignment within tolerance
- [ ] Coverage area verified
- [ ] Registration features functional

### Coating Verification
- [ ] Coating thickness measured (if specified)
- [ ] Coverage area inspected (no overspray on protected areas)
- [ ] Keep-out zones verified clean
- [ ] Visual inspection per acceptance criteria
- [ ] Adhesion testing (if required)

## Revision and Change Control

### Mask Updates
- Mask revisions follow part drawing revisions
- Document reason for change (e.g., "Adjusted SSM boundary per thermal analysis rev 3")
- Update application instructions if procedure changes
- Re-verify mask after modifications

## Related Directories

- **Parts**: [`../parts/`](../parts/) - Parts requiring coating/masking
- **Assemblies**: [`../assemblies/`](../assemblies/) - Assemblies with coating requirements
- **Drawings**: [`../drawings/`](../drawings/) - Drawings showing coating areas
- **Exports (DXF)**: [`../exports_dxf/`](../exports_dxf/) - Flat pattern masks
- **Exports (STEP)**: [`../exports_step/`](../exports_step/) - 3D mask exports
- **CAP**: [`../../CAP/`](../../CAP/) - Coating process specifications

## Standards References

- **ECSS-Q-ST-70-03C**: Surface cleanliness and contamination control
- **ASTM E595**: Outgassing properties of materials
- **NASA-STD-6001**: Flammability, odor, offgassing for spacecraft materials
- **ISO 8501**: Surface preparation standards

---

**Last Updated**: 2025-10-10
