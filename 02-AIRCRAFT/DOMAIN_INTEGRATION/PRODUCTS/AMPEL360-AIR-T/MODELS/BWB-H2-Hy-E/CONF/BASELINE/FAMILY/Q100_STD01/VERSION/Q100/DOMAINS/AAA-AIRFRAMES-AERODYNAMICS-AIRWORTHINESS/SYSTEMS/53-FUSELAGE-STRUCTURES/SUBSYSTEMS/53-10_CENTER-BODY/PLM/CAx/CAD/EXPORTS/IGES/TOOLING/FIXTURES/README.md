# FIXTURES — Fixture and Holding Device IGES Exports

## Purpose

This directory contains IGES exports of fixture geometries, holding devices, and work-holding tooling used in manufacturing and assembly processes.

## Content

Store IGES files (`.igs` or `.iges`) for:
- **Machining fixtures**: Work-holding for CNC operations
- **Assembly fixtures**: Positioning fixtures for assembly
- **Inspection fixtures**: Holding devices for measurement
- **Welding fixtures**: Fixtures for welding operations
- **Drilling fixtures**: Drill bushings and locating fixtures
- **Locating features**: Reference pins, blocks, and surfaces

## File Naming Convention

```
<subsystem>_FIXTURE_<purpose>_<tool-number>_<revision>_<date>.igs
```

**Examples:**
- `53-10_FIXTURE_MACHINING-FRAME_TL-6001_RevA_20250110.igs`
- `53-10_FIXTURE_ASSY-BULKHEAD_TL-6002_RevB_20250110.igs`
- `53-10_FIXTURE_DRILLING_TL-6003_RevA_20250110.igs`

## Export Requirements

When exporting fixture geometry to IGES:
- ✅ Use IGES version 5.3
- ✅ Export complete fixture assembly or components
- ✅ Include locating features and reference geometry
- ✅ Verify critical dimensions and tolerances
- ✅ Use millimeters for units
- ✅ Set tolerance to 0.001 mm

## Fixture Types

### Machining Fixtures
- **Vise fixtures**: Vise jaw inserts and work-holders
- **Pallet fixtures**: Tombstone and pallet-mounted fixtures
- **Vacuum fixtures**: Vacuum work-holding surfaces
- **Magnetic fixtures**: Magnetic holding devices

### Assembly Fixtures
- **Alignment fixtures**: Part positioning and alignment
- **Clamping fixtures**: Clamping and securing devices
- **Indexing fixtures**: Rotational or indexed positioning
- **Frame fixtures**: Large frame assembly fixtures

### Inspection Fixtures
- **CMM fixtures**: Coordinate measuring machine fixtures
- **Gauge fixtures**: Holding for gauging operations
- **Optical fixtures**: Fixtures for optical measurement

## Critical Features

Fixture IGES exports should include:
- **Locating surfaces**: Part contact and locating surfaces
- **Reference datums**: Datum A, B, C locations
- **Clamping areas**: Clamp contact zones
- **Clearance zones**: Tool clearance envelopes
- **Mounting holes**: Fixture mounting features
- **Part envelope**: Part containment boundaries

## Validation Checklist

Before committing fixture IGES files:
- [ ] All locating features included
- [ ] Reference datums correctly positioned
- [ ] Clearances verified
- [ ] Mounting interfaces correct
- [ ] Critical dimensions accurate
- [ ] Scale confirmed (1:1)
- [ ] Part fit verified

## Related Directories

- **Parent**: [`../`](../) — All TOOLING
- **Molds**: [`../MOLDS/`](../MOLDS/) — Mold geometry
- **Jigs**: [`../JIGS/`](../JIGS/) — Assembly jigs
- **Parts**: [`../../PARTS/`](../../PARTS/) — Part geometry (for fit check)
- **Installation**: [`../../INSTALLATION/`](../../INSTALLATION/) — Installation tooling
- **Source**: [`../../../MODELS/`](../../../MODELS/) — Native CAD tooling models

## Best Practices

- Export complete fixture geometry or logical components
- Include all locating and clamping features
- Document fixture setup and orientation
- Verify part-to-fixture fit in CAD before export
- Test import in manufacturing CAD/CAM system
- Provide fixture drawing (PDF) with dimensions and setup instructions

## Manufacturing Notes

When providing fixture IGES files:
- **Include**: Complete fixture geometry or buildable components
- **Document**: Setup procedure, part orientation
- **Specify**: Material requirements (e.g., steel, aluminum)
- **Reference**: Part geometry for fit verification
- **Coordinate**: With manufacturing engineering

## Design Considerations

Fixtures should be designed with:
- **Accessibility**: Tool access for machining or assembly
- **Repeatability**: Consistent part location
- **Rigidity**: Adequate stiffness for process forces
- **Clearance**: Sufficient clearance for tools and operations
- **3-2-1 locating**: Proper kinematic constraint (if applicable)

## Usage in Manufacturing

Fixture IGES files support:
- Fixture fabrication (CNC machining)
- Fit verification with part geometry
- Clearance analysis for tooling
- Manufacturing simulation
- Process planning and validation
