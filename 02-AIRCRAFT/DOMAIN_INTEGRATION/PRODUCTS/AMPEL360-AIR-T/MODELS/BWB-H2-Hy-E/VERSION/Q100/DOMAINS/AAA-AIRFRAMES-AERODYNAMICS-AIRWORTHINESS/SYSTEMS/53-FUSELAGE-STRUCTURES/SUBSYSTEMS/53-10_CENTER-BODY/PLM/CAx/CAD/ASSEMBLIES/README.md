# ASSEMBLIES — CAD Assembly Files 

## Purpose

This directory contains CAD assembly models that combine multiple components from the 53-10 Center Body subsystem into integrated structures.

## What to Store

### Assembly Types
- **Major assemblies**: Complete center body sections
- **Sub-assemblies**: Frame+stringer+skin panel assemblies
- **Installation assemblies**: Attachments with adjacent systems
- **Test assemblies**: Fixture and tooling assemblies for qualification

### Assembly Models
- **Structural assemblies**: Primary structure combinations
- **Interface assemblies**: Connections to wings, nose, and aft sections
- **Installation aids**: Assembly jigs and fixtures
- **Check fixtures**: Inspection and dimensional verification tooling

## Naming Convention

Use the following naming pattern:
```

<subsystem>*ASM*<assembly-name>_<version>.<ext>

```

Examples:
- `53-10_ASM_CENTER-BODY_COMPLETE_v01.CATProduct`
- `53-10_ASM_FRAME-SECTION_F01-F05_v02.asm`
- `53-10_ASM_SKIN-PANEL_SP-001_v01.sldasm`

## Organization

Organize assemblies by:
- **Assembly level**: Top-level, sub-assembly, detail assembly
- **Zone**: Forward, center, aft center body sections
- **System interface**: Wing interface, door interface, etc.

### Directory Structure

Assemblies are organized into the following subdirectories:

- **[TOP_LEVEL/](./TOP_LEVEL/)** — Top-level assembly models (complete center body)
- **[SUB_ASSEMBLIES/](./SUB_ASSEMBLIES/)** — Sub-assembly models (frame sections, panel groups)
- **[INSTALLATION/](./INSTALLATION/)** — Installation assemblies (interfaces with adjacent systems)
- **[TEST/](./TEST/)** — Test article assemblies (qualification and verification)
- **[FIXTURES/](./FIXTURES/)** — Assembly fixtures and tooling
  - **[FIXTURES/JIGS/](./FIXTURES/JIGS/)** — Assembly jigs and positioning fixtures
  - **[FIXTURES/CHECK_FIXTURES/](./FIXTURES/CHECK_FIXTURES/)** — Inspection and verification tooling
- **[CONFIGURATIONS/](./CONFIGURATIONS/)** — Configuration variants
  - **[CONFIGURATIONS/SIMPLIFIED/](./CONFIGURATIONS/SIMPLIFIED/)** — Simplified models for reviews
  - **[CONFIGURATIONS/LIGHTWEIGHT/](./CONFIGURATIONS/LIGHTWEIGHT/)** — Lightweight models for performance
- **[REFERENCES/](./REFERENCES/)** — Reference geometry
  - **[REFERENCES/COORDINATE_SYSTEMS/](./REFERENCES/COORDINATE_SYSTEMS/)** — Coordinate system definitions
  - **[REFERENCES/PLANES/](./REFERENCES/PLANES/)** — Reference planes and datum surfaces
- **[DOCS/](./DOCS/)** — Assembly documentation
  - **[DOCS/BOM/](./DOCS/BOM/)** — Bills of Materials
  - **[DOCS/INTERFACE_CONTROL/](./DOCS/INTERFACE_CONTROL/)** — Interface control documents
  - **[DOCS/SEQUENCE/](./DOCS/SEQUENCE/)** — Assembly sequence documentation

## Assembly Structure

### Top-Level Assembly
```

53-10_CENTER-BODY_COMPLETE
├── Frames (F01-F20)
├── Stringers (L/R, Upper/Lower)
├── Skin Panels (Outer/Inner)
├── Floors
├── Bulkheads
└── Interface Fittings

```

### Sub-Assembly Example
```

53-10_ASM_FRAME-SECTION_F05
├── Frame F05
├── Stringers (4x)
├── Skin panels (2x)
└── Fasteners (clips, rivets)

```

## File Formats

### Native Assembly Formats
- **CATIA**: `.CATProduct`
- **NX**: `.prt` (assemblies are also .prt files)
- **SolidWorks**: `.sldasm`
- **Creo**: `.asm`

## Best Practices

### Assembly Design
- Use **mating/constraints** to define component relationships
- Define **assembly features** (holes, cuts across parts)
- Include **reference geometry** (coordinate systems, planes)
- Document **assembly sequence** in properties
- Specify **fastener types** and locations

### Performance
- Use **simplified representations** for large assemblies
- Apply **display states** to reduce graphics load
- Create **lightweight configurations** for reviews
- Use **assembly-level suppression** for options/variants

### Configuration Management
- Track **effectivity** of components (serial numbers, dates)
- Maintain **configuration control** per design freeze
- Document **interchangeability** rules
- Define **build variants** (test articles vs. production)

## Assembly Documentation

Each assembly should include:
- **Bill of Materials (BOM)**: Component list with quantities
- **Interface Control**: Mating part requirements
- **Assembly instructions**: Build sequence and tooling needs
- **Fastener schedule**: Type, size, torque specs
- **Mass properties**: Total assembly weight and CG

## Validation Checks

Before committing assemblies:
- [ ] All components load without errors
- [ ] Mates/constraints fully defined
- [ ] No interference between parts
- [ ] Assembly mass properties calculated
- [ ] BOM exported and accurate
- [ ] Neutral format (STEP) exported to [`../EXPORTS/STEP/`](../EXPORTS/STEP/)
- [ ] Assembly sequence documented

## Integration Points

### Adjacent Systems
- **51-00 General Structures**: Standard fasteners and joints
- **52-00 Doors**: Door frame interfaces
- **53-20 Nose Section**: Forward bulkhead interface
- **53-30 Aft Section**: Aft bulkhead interface
- **56-00 Windows**: Window frame cutouts
- **57-00 Wings**: Wing-to-body attachment

### Related Directories
- **Component models**: [`../MODELS/`](../MODELS/)
- **Assembly drawings**: [`../DRAWINGS/`](../DRAWINGS/)
- **Neutral exports**: [`../EXPORTS/STEP/`](../EXPORTS/STEP/)
- **Interface definitions**: [`../../INTERFACE_MATRIX/`](../../INTERFACE_MATRIX/)

## Version Control

- Use Git LFS for large assembly files (> 10 MB)
- Tag design reviews and critical milestones
- Document configuration changes in commit messages
- Maintain assembly history for design lineage

## Quality Standards

Follow:
- **ATA iSpec 2200**: Data module standards
- **ISO 10303-242** (STEP AP242): Assembly structure exchange
- **AS9100**: Quality management requirements
- **Internal design standards**: `../../STANDARDS/`
```
