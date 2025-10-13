# AFT — Aft Zone Drawings

## Purpose

This directory contains or references drawings for components located in the Aft (AFT) zone of the 53-10 Center Body subsystem.

## Zone Definition

### Aft Zone Boundaries
- **Forward limit**: Approximately at wing trailing edge
- **Aft limit**: Aft fuselage interface
- **Typical stations**: FS 1000 to FS 1500 (example - adjust based on actual design)

### Major Components

#### Primary Structure
- **Frames**: F21, F22, F23, F24, F25, F26, F27, F28, F29, F30
- **Stringers**: Aft stringers (upper and lower)
- **Skin panels**: Aft outer and inner skin panels
- **Keel beam**: Aft section of keel beam

#### Secondary Structure
- **Floor beams**: Aft cabin floor structure
- **Doublers**: Local reinforcements in aft zone
- **Splice plates**: Aft joint fittings
- **Pressure bulkhead support**: If pressurized cabin

#### Interfaces
- **Aft fuselage interface**: Aft center body to aft fuselage attachment
- **Empennage provisions**: Tail attachment load paths (if applicable)
- **APU mounting**: Auxiliary Power Unit mounting provisions
- **Aft systems**: APU, tail rotor (if applicable), aft equipment

## Organization

### Drawing References
This directory can contain:
- **Symbolic links**: Links to drawings in type directories (PART/, ASSEMBLY/, etc.)
- **Index file**: List of all AFT zone drawings with references
- **Zone package**: Combined PDF package of all AFT zone drawings

### Index File
Create `AFT_ZONE_INDEX.md` listing:
- Component name and part number
- Drawing number and revision
- Drawing type (Part, Assembly, Installation, etc.)
- Path to drawing file
- Status (Draft, Released, Obsolete)

## Major Assemblies

### AFT Zone Assembly
- **Drawing**: `53-10_DWG_ASM_AFT-ZONE-COMPLETE_D1003_SH1_RevA.pdf`
- **Description**: Complete aft zone assembly
- **Components**: All frames, stringers, and skins in AFT zone

### Aft Fuselage Interface Assembly
- **Drawing**: `53-10_DWG_INST_AFT-INTERFACE_D2020_SH1_RevA.pdf`
- **Description**: Interface between center body AFT zone and aft fuselage
- **Reference ICD**: `53-10_ICD_AFT-FUSELAGE_ICD-003_RevA.pdf`

### Empennage Support Structure (if applicable)
- **Drawing**: `53-10_DWG_ASM_EMPENNAGE-SUPPORT_D1070_SH1_RevA.pdf`
- **Description**: Load path structure for empennage attachment
- **Notes**: Coordinate with ATA 55 (Stabilizers)

## Manufacturing Sequence

### AFT Zone Build Sequence
1. **Frame sub-assemblies**: Assemble aft frames with clips and fittings
2. **Stringer installation**: Install stringers on frames
3. **Inner skin**: Install inner skin panels
4. **Floor structure**: Install aft floor beams (if applicable)
5. **Keel beam**: Complete aft section of keel beam
6. **Outer skin**: Install outer skin panels
7. **Systems provisions**: Install APU mounts, equipment brackets
8. **Interface preparation**: Prepare for aft fuselage installation

## Critical Features

### High-Load Areas
- Aft fuselage attachment fittings
- Empennage load path (if applicable)
- APU mounting provisions
- Keel beam termination
- Pressure bulkhead support (if pressurized)

### Interfaces Requiring Special Attention
- Aft fuselage joint alignment
- Empennage attachment interfaces (if applicable)
- APU vibration isolation mounts
- Systems penetrations
- Access provisions for maintenance

## Quality Control

### AFT Zone Inspection Points
- Frame assembly dimensional check
- Stringer alignment verification
- Skin panel fit and gap check
- Aft interface dimensional check
- Fastener installation inspection
- Keel beam continuity verification
- Systems mounting verification
- Final zone dimensional audit

## Related Drawings

### Component Drawings
Reference drawings in type directories:
- [`../../PART/`](../../PART/) - Individual component drawings
- [`../../ASSEMBLY/`](../../ASSEMBLY/) - Assembly drawings
- [`../../INSTALLATION/`](../../INSTALLATION/) - Installation drawings
- [`../../DETAIL/`](../../DETAIL/) - Detail drawings
- [`../../ICD/`](../../ICD/) - Interface control drawings

### Adjacent Zones
- [`../CTR/`](../CTR/) - Center zone (forward boundary of AFT zone)
- **Aft Fuselage**: See 53-30_AFT-FUSELAGE subsystem (if exists)
- **Empennage**: See 55-STABILIZERS system (if applicable)

## Special Considerations

### Aft Body Configuration
The aft zone configuration depends on aircraft type:
- **Conventional tail**: Load path to empennage
- **BWB configuration**: May integrate with wing structure
- **Blended design**: Smooth transition to aft body shape

### Systems Integration
- **APU installation**: Mounting, intake, exhaust provisions
- **Aft equipment**: Batteries, avionics, environmental systems
- **Access panels**: Maintenance access to aft equipment
- **Fire protection**: APU fire protection provisions

## Best Practices

### Zone Organization
- Keep zone index up to date
- Link to latest revision of drawings
- Note any multi-zone components
- Coordinate with aft fuselage and empennage teams
- Track zone completion status

### Manufacturing Support
- Provide complete drawing packages
- Include assembly sequence drawings
- Supply tooling drawings if applicable
- Document inspection requirements
- Support manufacturing questions
- Coordinate aft fuselage installation sequence

### Interface Management
- Maintain aft interface dimensions rigorously
- Coordinate with aft fuselage integration team
- Verify empennage load path continuity
- Track interface changes through CCB
- Document interface verification results

## References

- **Parent README**: [`../README.md`](../README.md) - ZONES organization
- **Forward Zone**: [`../FWD/README.md`](../FWD/README.md)
- **Center Zone**: [`../CTR/README.md`](../CTR/README.md)
- **Aft Fuselage**: See 53-30_AFT-FUSELAGE subsystem
- **Stabilizers**: See 55-STABILIZERS in AAA domain (if applicable)
