# STRINGER_BAYS — Stringer Bay Sub-Assemblies

## Purpose

This directory contains sub-assembly models for stringer bays of the 53-10 Center Body. Stringer bays are longitudinal assemblies that include continuous stringers with their attached skin panels between frame stations.

## Organization

Stringer bays are organized by longitudinal identifier (LXX):
- **L01-L10**: Left side upper stringers
- **L11-L20**: Left side lower stringers
- **R01-R10**: Right side upper stringers
- **R11-R20**: Right side lower stringers
- **C01-C05**: Crown/centerline stringers

## Directory Structure

Each stringer bay (LXX) contains:
- **MODELS/**: CAD assembly files for the stringer bay
- **DRAWINGS/**: Engineering drawings and manufacturing prints
- **DOCS/**: Documentation including BOM, splice details, and specifications

## Naming Convention

Use the following pattern for stringer bay assemblies:
```
53-10_ASM_STRINGER-BAY_L<nn>_v<version>.<ext>
```

Examples:
- `53-10_ASM_STRINGER-BAY_L01_v01.CATProduct`
- `53-10_ASM_STRINGER-BAY_R05_v02.asm`
- `53-10_ASM_STRINGER-BAY_C02_v01.sldasm`

## Typical Stringer Bay Contents

A stringer bay assembly typically includes:
- **Continuous stringer**: Running multiple frame stations (e.g., F01-F05)
- **Stringer segments**: Individual stringer pieces with splices
- **Skin panels**: Attached to stringer (4-8 panels per bay)
- **Stringer clips**: Frame-to-stringer attachment fittings
- **Splice fittings**: Stringer-to-stringer joint hardware
- **Fasteners**: Complete fastener schedule along the bay

## Assembly Structure Example

```
53-10_ASM_STRINGER-BAY_L01
├── Stringer_L01_Segment_01 (F01-F05)
├── Stringer_L01_Segment_02 (F05-F10)
├── Splice_Fitting_F05
├── Skin_Panel_SP-001
├── Skin_Panel_SP-002
├── Skin_Panel_SP-003
├── Frame_Clips (x10)
└── Fasteners
```

## Integration Points

Stringer bays interface with:
- **Frame sections**: Stringer-to-frame connections at each station
- **Skin panel modules**: Overlapping skin attachments
- **Window bays**: Reinforcements around window cutouts
- **Door surrounds**: Reinforced stringer terminations at doors
- **Wing interfaces**: Special stringer terminations at wing-body joint

## Related Directories

- **Component models**: [`../../../MODELS/`](../../../MODELS/)
- **Frame sections**: [`../FRAME_SECTIONS/`](../FRAME_SECTIONS/)
- **Skin panel modules**: [`../SKIN_PANEL_MODULES/`](../SKIN_PANEL_MODULES/)
- **Documentation**: [`../DOCS/`](../DOCS/)
- **Top-level assembly**: [`../../TOP_LEVEL/`](../../TOP_LEVEL/)

## Design Guidelines

### Assembly Practices
- Define stringer as primary component
- Constrain clips to frames and stringers
- Attach skin panels with proper fastener spacing
- Include all splice fittings and details
- Document splice locations and torque requirements

### Stringer Continuity
- Maintain stringer alignment across splices
- Ensure proper load transfer at joints
- Design for manufacturing break points
- Consider transportation and assembly constraints
- Validate structural continuity in analysis

### Quality Requirements
- Verify alignment tolerances across splices
- Check fastener edge distances and spacing
- Validate skin-to-stringer bond line
- Export complete BOM with splice details
- Document critical-to-quality characteristics

## Special Considerations

### Stringer Types
- **J-stringers**: Typical configuration
- **Hat-stringers**: Composite sections
- **Z-stringers**: Sheet metal formed sections
- **Blade-stringers**: Machined configurations

### Splice Design
- Locate splices away from high-stress regions
- Avoid splices near cutouts or penetrations
- Design for 100% load transfer capability
- Include proper edge preparation for assembly
- Document splice inspection requirements

## Metadata Requirements

Each stringer bay assembly should include:
- **Part number**: Following 53-10 numbering system
- **Description**: Stringer location and span
- **Bay limits**: Start and end frame stations
- **Splice locations**: Frame stations where splices occur
- **Material**: Stringer and skin materials
- **Mass properties**: Weight and CG per bay
- **Status**: Design state (draft, released, obsolete)

## Version Control

- Use Git LFS for large assembly files (> 10 MB)
- Tag splice design reviews
- Document stringer run-out changes
- Maintain revision history for each bay configuration
