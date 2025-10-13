# FASTENER_SETS — Fastener Set Definitions and Assemblies

## Purpose

This directory contains fastener set definitions, schedules, and assembly models for the 53-10 Center Body sub-assemblies. Fastener sets document the complete fastener requirements for specific assembly regions or joints.

## Contents

### Fastener Schedules
- **Frame-to-skin fasteners**: Rivets or bolts for skin-to-frame joints
- **Stringer-to-skin fasteners**: Rivets for stringer-to-skin attachment
- **Frame-to-stringer clips**: Bolts and clips for frame/stringer connections
- **Splice joint fasteners**: Bolts for structural splices
- **Doubler fasteners**: Fasteners for reinforcement attachments

### Fastener Types
- **Solid rivets**: Typical aluminum or titanium rivets
- **Blind rivets**: One-side access installations
- **Bolts**: High-load structural bolts
- **Lockbolts**: Self-locking collar fasteners
- **Hi-Loks**: Two-piece mechanical fasteners
- **Special fasteners**: Temperature-compensating, electrically isolated, etc.

## Naming Convention

Use the following pattern for fastener set documentation:
```
53-10_FASTENER-SET_<assembly>_<joint>_v<version>.<ext>
```

Examples:
- `53-10_FASTENER-SET_FRAME-F05_SKIN_v01.csv`
- `53-10_FASTENER-SET_STRINGER-L01_SPLICE_v02.xlsx`
- `53-10_FASTENER-SET_DOOR-SURROUND_v01.pdf`

## Fastener Schedule Format

A typical fastener schedule includes:

| Location | Fastener Type | Size | Material | Grip | Spacing | Rows | Edge Dist | Torque | Qty |
|----------|---------------|------|----------|------|---------|------|-----------|--------|-----|
| Frame F05-Skin | AN470 Rivet | AD4-6 | 2117-T4 | 0.25" | 1.0" | 2 | 2.5D | N/A | 120 |
| Stringer L01 Clip | NAS1352 Bolt | C6-12 | CRES | 0.50" | 4.0" | 1 | 3.0D | 40 in-lb | 24 |

## Design Considerations

### Fastener Selection
- **Material compatibility**: Match fastener to base material (aluminum/aluminum, etc.)
- **Corrosion protection**: Anodize, cadmium plate, or other coating
- **Load capability**: Select based on shear/tension loads
- **Installation access**: One-side or two-side access
- **Sealing requirements**: Wet installation if in fuel tank
- **Electrical bonding**: Conductive fasteners for grounding

### Joint Design
- **Edge distance**: Minimum 2.0-2.5D from hole center to edge
- **Spacing**: Minimum 3.0-4.0D between fasteners
- **Rows**: Multiple rows for wide joints (2-3 typical)
- **Load distribution**: Uniform spacing for even load sharing
- **Hole preparation**: Reamed or drilled to specified tolerance

### Installation Considerations
- **Driving method**: Pneumatic, hydraulic, or hand installation
- **Tooling access**: Clearance for installation tools
- **Inspection**: Accessibility for visual or NDT inspection
- **Torque requirements**: Specified for bolts and lockbolts
- **Installation sequence**: Order of fastener installation

## Fastener Load Analysis

Document for each fastener set:
- **Applied loads**: Shear, tension, or combined loads
- **Fastener capacity**: Allowable loads (bearing, shear, tension)
- **Margin of safety**: MS = (Allowable/Applied) - 1
- **Load distribution**: Load per fastener in multi-fastener joints
- **Critical fasteners**: Highest loaded or most critical fasteners

## Integration Points

Fastener sets are used throughout:
- **Frame sections**: Frame-to-skin and frame-to-stringer attachments
- **Stringer bays**: Stringer-to-skin and splice fasteners
- **Skin panel modules**: Skin-to-skin joints and doubler attachments
- **Floor modules**: Floor beam and panel fasteners
- **Bulkhead modules**: Bulkhead-to-frame attachments
- **All sub-assemblies**: Complete fastener schedules for assembly

## Related Directories

- **Frame sections**: [`../FRAME_SECTIONS/`](../FRAME_SECTIONS/)
- **Stringer bays**: [`../STRINGER_BAYS/`](../STRINGER_BAYS/)
- **All assembly directories**: Fastener schedules for each assembly
- **Component models**: [`../../../MODELS/`](../../../MODELS/)
- **Documentation**: [`../DOCS/`](../DOCS/)

## Design Guidelines

### Standardization
- Use standard fastener types where possible
- Maintain approved fastener list
- Minimize number of different fastener types
- Use common sizes and lengths
- Document fastener specifications

### Quality Assurance
- Specify fastener lot traceability for critical applications
- Include fastener inspection requirements
- Document installation quality checks
- Specify torque verification methods
- Include repair procedures for damaged holes

### Documentation
- Complete fastener schedule for each assembly
- Fastener location drawings or models
- Installation procedures and tooling
- Torque specifications and sequences
- Inspection and acceptance criteria

## Fastener Installation

### Solid Rivets
- Drill or ream holes to specified size
- Deburr holes and clean surfaces
- Install rivet and buck or squeeze
- Inspect driven head formation
- Document installation quality

### Blind Rivets
- Drill hole to specified size
- Install blind rivet from one side
- Pull stem to upset sleeve
- Inspect stem break and head formation
- Validate grip range

### Bolts and Lockbolts
- Drill or ream holes to bolt size
- Install bolt with washer (if required)
- Torque nut to specification
- Apply torque stripe or safety wire
- Verify torque after installation

## Special Installation Requirements

### Fuel Tank Fasteners
- Wet installation with sealant
- Apply sealant to fastener and hole
- Install fastener while sealant is wet
- Cure sealant per specification
- Leak test after assembly

### Interference-Fit Fasteners
- Cold-work or ream holes to specification
- Install oversized or interference-fit fastener
- Enhance fatigue life at critical locations
- Inspect installation for proper fit
- Document cold-work process

### Electrically Isolated Fasteners
- Install with non-conductive bushings
- Prevent galvanic corrosion
- Maintain electrical isolation
- Verify isolation with continuity test
- Document isolation requirements

## Metadata Requirements

Each fastener set should include:
- **Assembly reference**: Associated assembly part number
- **Joint description**: Joint or interface location
- **Fastener specification**: Complete fastener call-out
- **Quantity**: Total number of fasteners
- **Installation procedure**: Reference to installation document
- **Torque specification**: For bolts and lockbolts
- **Inspection criteria**: Visual or NDT requirements
- **Status**: Design state (draft, released, obsolete)

## Quality Control

### Inspection Requirements
- Visual inspection of installed fasteners
- Driven head formation (rivets)
- Torque verification (bolts)
- Edge distance and spacing verification
- Hole quality and damage inspection
- Seal application (if required)

### Non-Conformance
- Document fastener installation defects
- Define repair procedures (re-rivet, oversize hole, etc.)
- Track repaired locations
- Validate repairs by inspection or test
- Update as-built documentation

## Bill of Materials

Fastener set BOMs should include:
- Part number and description
- Quantity required
- Unit weight and total weight
- Material and finish specification
- Source/supplier information
- Procurement lead time

## Version Control

- Document fastener changes in revision history
- Tag design reviews and installation validations
- Maintain fastener schedule accuracy
- Coordinate changes with stress analysis
- Update installation procedures for changes
