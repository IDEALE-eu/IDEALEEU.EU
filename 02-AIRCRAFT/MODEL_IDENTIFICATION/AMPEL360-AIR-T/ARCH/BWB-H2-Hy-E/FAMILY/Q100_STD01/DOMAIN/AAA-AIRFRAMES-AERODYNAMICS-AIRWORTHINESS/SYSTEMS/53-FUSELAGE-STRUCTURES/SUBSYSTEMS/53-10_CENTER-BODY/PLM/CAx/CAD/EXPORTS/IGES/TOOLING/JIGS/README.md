# JIGS — Assembly Jig and Template IGES Exports

## Purpose

This directory contains IGES exports of assembly jig geometries, templates, and layout tools used for part positioning, alignment, and assembly operations.

## Content

Store IGES files (`.igs` or `.iges`) for:
- **Assembly jigs**: Part alignment and assembly jigs
- **Layout jigs**: Master layout and template jigs
- **Drilling jigs**: Hole drilling guide jigs
- **Bonding jigs**: Adhesive bonding alignment jigs
- **Welding jigs**: Weld joint alignment jigs
- **Alignment templates**: Positioning templates and gauges

## File Naming Convention

```
<subsystem>_JIG_<purpose>_<tool-number>_<revision>_<date>.igs
```

**Examples:**
- `53-10_JIG_ASSY-FRAME-SECTION_TL-7001_RevA_20250110.igs`
- `53-10_JIG_DRILLING-TEMPLATE_TL-7002_RevB_20250110.igs`
- `53-10_JIG_BONDING-PANEL_TL-7003_RevA_20250110.igs`

## Export Requirements

When exporting jig geometry to IGES:
- ✅ Use IGES version 5.3
- ✅ Export complete jig or template geometry
- ✅ Include all locating and reference features
- ✅ Verify hole locations and critical dimensions
- ✅ Use millimeters for units
- ✅ Set tolerance to 0.001 mm or better

## Jig Types

### Assembly Jigs
- **Frame assembly jigs**: Large structure alignment
- **Panel assembly jigs**: Skin panel positioning
- **Sub-assembly jigs**: Component pre-assembly
- **Master jigs**: Master layout and setup jigs

### Drilling Jigs
- **Hole drilling jigs**: Drill bushing plates
- **Pattern drilling jigs**: Multi-hole pattern guides
- **Angle drilling jigs**: Compound angle drilling
- **Transfer drilling jigs**: Matched-hole drilling

### Special Purpose Jigs
- **Bonding jigs**: Adhesive bonding alignment
- **Fastening jigs**: Rivet/fastener installation guides
- **Inspection jigs**: Dimensional verification jigs
- **Layout templates**: Shop floor layout templates

## Critical Features

Jig IGES exports should include:
- **Locating pins and holes**: Part locating features
- **Reference edges**: Datum edges and surfaces
- **Drill bushings**: Hole locations and diameters
- **Alignment marks**: Visual alignment indicators
- **Mounting features**: Jig attachment points
- **Part outline**: Part containment envelope

## Validation Checklist

Before committing jig IGES files:
- [ ] All holes and features accurately positioned
- [ ] Reference datums correctly located
- [ ] Part fit verified in CAD
- [ ] Critical dimensions checked
- [ ] Bushing sizes correct
- [ ] Scale confirmed (1:1)
- [ ] Jig orientation documented

## Related Directories

- **Parent**: [`../`](../) — All TOOLING
- **Molds**: [`../MOLDS/`](../MOLDS/) — Mold geometry
- **Fixtures**: [`../FIXTURES/`](../FIXTURES/) — Holding fixtures
- **Parts**: [`../../PARTS/`](../../PARTS/) — Part geometry (for alignment)
- **Assemblies**: [`../../ASSEMBLIES/`](../../ASSEMBLIES/) — Assembly models
- **Source**: [`../../../MODELS/`](../../../MODELS/) — Native CAD tooling models

## Best Practices

- Export jigs with all critical features and hole patterns
- Document jig setup and part orientation
- Include reference geometry for alignment
- Verify hole locations against part geometry
- Test jig design with assembly simulation
- Provide jig drawing (PDF) with setup instructions
- Include material and fabrication specifications

## Manufacturing Notes

When providing jig IGES files:
- **Include**: Complete jig geometry with all features
- **Document**: Assembly sequence, part orientation, setup procedure
- **Specify**: Material (often aluminum for templates, steel for production)
- **Reference**: Part and assembly geometry for verification
- **Coordinate**: With manufacturing and assembly teams
- **Verify**: Hole patterns and dimensions with engineering drawings

## Design Considerations

Jigs should be designed for:
- **Accuracy**: Precise hole and feature locations
- **Repeatability**: Consistent part positioning
- **Durability**: Adequate strength for production use
- **Ease of use**: Simple setup and operation
- **Flexibility**: Accommodate part tolerances
- **Maintenance**: Easy to inspect and maintain

## Usage in Manufacturing

Jig IGES files support:
- Jig fabrication (CNC machining, waterjet cutting)
- Hole pattern verification
- Assembly sequence planning
- Shop floor setup and training
- Manufacturing simulation and validation
- Quality assurance and inspection

## Assembly Integration

Jigs are typically used in conjunction with:
- Assembly procedures and work instructions
- Part geometry and assemblies
- Fastener specifications
- Quality control plans
- Inspection gauges and fixtures
