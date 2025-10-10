# FIXTURES_TOOLING — Manufacturing Fixtures and Tooling

## Purpose

This directory contains CAD models for manufacturing fixtures, tooling, and jigs used in the fabrication and assembly of 21-10 radiators and heat exchangers.

## Content

### Fixture Types
- **Drill templates**: Precision hole location templates
- **Bonding nests**: Fixtures for adhesive bonding processes
- **Assembly jigs**: Fixtures for part alignment during assembly
- **Welding fixtures**: Tooling for welding operations
- **Inspection fixtures**: Gauges and inspection tooling
- **Handling fixtures**: Lifting and transport fixtures

### What to Store
- 3D CAD models of fixtures (native and neutral formats)
- 2D drawings with dimensions and specifications
- Fixture usage instructions
- Material specifications for fixture construction
- Maintenance and calibration requirements

## Naming Convention

```
21-10_FIX_<type>_<description>__r<NN>__<status>.<ext>
```

Examples:
- `21-10_FIX_DRILL_RAD-PANEL-PATTERN__r01__REL.step`
- `21-10_FIX_BOND_FACESHEET-CORE__r02__RVW.prt`
- `21-10_FIX_WELD_MANIFOLD-TUBE__r01__WIP.asm`

### Status Codes
- **WIP**: Work in progress
- **RVW**: In review
- **REL**: Released

## Design Standards

### Units
- Length: millimeters (mm)
- Mass: kilograms (kg)
- Angles: degrees (deg)

### Material Selection
- Tooling materials: Steel (tool steel, stainless), aluminum, composite
- Consider thermal expansion matching for bonding fixtures
- Durability for expected production volume
- Cost vs. precision trade-offs

### Tolerances
- Fixture tolerances tighter than part tolerances
- Critical locating features: ±0.01 mm typical
- Reference ISO 2768-mK as baseline

## Fixture Categories

### Drill Templates
- Locate and guide drill holes precisely
- Match mounting patterns and interface requirements
- Include bushings for drill guide wear resistance
- Document drill bit sizes and depths

### Bonding Nests
- Maintain part alignment during cure cycle
- Provide uniform pressure distribution
- Accommodate thermal expansion during cure
- Include pressure application points
- Document cure cycle parameters

### Assembly Jigs
- Align components for assembly operations
- Provide access for fastener installation
- Support component weight during assembly
- Include locating pins and clamps

### Welding Fixtures
- Hold parts in correct position for welding
- Provide heat sink where needed
- Allow access for welding torch/equipment
- Minimize distortion during welding

### Inspection Fixtures
- Go/no-go gauges for critical dimensions
- Flatness check fixtures
- Hole pattern verification templates
- Interface fit-check fixtures

## Design Considerations

### Locating Features
- 3-2-1 locating principle (6 points of contact)
- Datum reference consistent with part datums
- Repeatable positioning
- Avoid over-constraint

### Clamping
- Adequate clamping force without part distortion
- Access for clamp actuation
- Quick-release mechanisms where appropriate
- Document clamping torque or force

### Material Handling
- Safe lifting points for fixtures >15 kg
- Ergonomic design for operator use
- Storage and transport considerations
- Maintenance access

## Documentation Requirements

### For Each Fixture
- [ ] 3D model in native CAD format
- [ ] STEP export for neutral format
- [ ] 2D drawing with full dimensions
- [ ] Usage instructions and setup procedures
- [ ] Material specifications
- [ ] Maintenance and inspection intervals
- [ ] Calibration requirements (if applicable)

### Process Integration
- Reference to CAP (Computer-Aided Process) documents
- Link to manufacturing process plans
- Part number references for applicable parts
- Quality control checkpoints

## Fixture Validation

### Design Validation
- [ ] Fixture design reviewed against part geometry
- [ ] Locating and clamping analyzed for adequacy
- [ ] Interference check with tooling and equipment
- [ ] Operator accessibility and ergonomics evaluated

### Physical Validation
- [ ] First article inspection using fixture
- [ ] Repeatability testing (multiple setups)
- [ ] Wear assessment after initial use
- [ ] Process capability study (if required)

## Maintenance and Control

### Configuration Control
- Fixture part numbers and revision control
- Change control for fixture modifications
- Traceability to parts manufactured using fixture

### Maintenance
- Periodic inspection schedule
- Wear limit specifications
- Calibration requirements for precision fixtures
- Repair and refurbishment procedures

## Related Directories

- **Assemblies**: [`../assemblies/`](../assemblies/) - Assemblies requiring fixtures
- **Parts**: [`../parts/`](../parts/) - Parts manufactured using fixtures
- **Drawings**: [`../drawings/`](../drawings/) - Fixture drawings
- **Exports (STEP)**: [`../exports_step/`](../exports_step/) - Neutral format exports
- **CAP**: [`../../CAP/`](../../CAP/) - Process plans referencing fixtures
- **CAM**: [`../../CAM/`](../../CAM/) - Manufacturing programs using fixtures

## Standards References

- **ISO 1101**: Geometrical tolerancing for fixture design
- **ISO 2768**: General tolerances
- **ASME B5.54**: Machine tool fixtures
- **AS9100**: Quality management for aerospace tooling

---

**Last Updated**: 2025-10-10
