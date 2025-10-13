# ASSEMBLY — Assembly Drawings

## Purpose

This directory contains assembly drawings showing how components are combined into structural assemblies for the 53-10 Center Body subsystem.

## What to Store

### Assembly Drawing Types
- **Major assemblies**: Complete center body sections
- **Sub-assemblies**: Frame+stringer+skin panel combinations
- **Installation assemblies**: Attachment to adjacent systems
- **Tooling assemblies**: Assembly jigs and fixtures
- **Test assemblies**: Qualification test configurations

## Content Requirements

### Mandatory Information
- **Assembly views**: Multiple views showing component relationships
- **Item balloons**: Numbered balloons referencing BOM
- **Bill of Materials (BOM)**: Complete parts list with quantities
- **Assembly notes**: Assembly sequence, torque specs, adhesives
- **Fastener schedules**: Bolt/rivet patterns and specifications
- **Interface callouts**: Connection points to other assemblies
- **Assembly dimensions**: Critical assembly tolerances and clearances

## Naming Convention

```
53-10_DWG_ASM_<assembly-name>_<drawing-number>_<sheet>_<revision>.<ext>
```

### Examples
- `53-10_DWG_ASM_CENTER-BODY-COMPLETE_D1000_SH1_RevA.pdf`
- `53-10_DWG_ASM_FRAME-SECTION-F01-F05_D1010_SH1_RevB.pdf`
- `53-10_DWG_ASM_SKIN-PANEL-SP-001_D1025_SH1_RevA.pdf`
- `53-10_DWG_ASM_WING-INTERFACE_D1100_SH1-2_RevA.pdf`

## BOM Requirements

### BOM Content
- **Item number**: Sequential numbering (1, 2, 3, ...)
- **Part number**: Unique part or assembly identifier
- **Description**: Component name and brief description
- **Quantity**: Number required per assembly
- **Material**: Material specification (for purchased items)
- **Notes**: Special requirements, alternates, or references

### BOM Format
- Include BOM on drawing sheet or separate sheet
- Reference item balloons to BOM item numbers
- Note any "Reference Only" or "As Required" items
- Link to EBOM via [`../../EBOM_LINKS.md`](../../EBOM_LINKS.md)

## Organization

Organize assembly drawings by:
- **Assembly level**: Top-level, sub-assembly, detail assembly
- **Zone**: Forward, center, aft center body sections
- **System interface**: Wing, nose, aft fuselage interfaces
- **Functional group**: Primary structure, secondary structure, installations

## Related Directories

- **CAD assemblies**: [`../../ASSEMBLIES/`](../../ASSEMBLIES/)
- **Part drawings**: [`../PART/`](../PART/)
- **Installation drawings**: [`../INSTALLATION/`](../INSTALLATION/)
- **Zone organization**: [`../ZONES/`](../ZONES/)
- **Revisions**: [`../REVISIONS/`](../REVISIONS/)

## Best Practices

### Assembly Views
- Show exploded view for assembly sequence
- Include section views to show internal configuration
- Use detail views for critical interfaces
- Show interface datums and mating features
- Include tooling access requirements

### Assembly Notes
- Specify assembly sequence in notes
- Define torque values for all fasteners
- Note adhesive application and cure requirements
- Specify shimming or adjustment procedures
- Include inspection points and acceptance criteria

### Fastener Information
- Create fastener schedules for bolt/rivet patterns
- Specify fastener types, sizes, and materials
- Note torque values or installation specs
- Show installation direction and accessibility
- Reference applicable installation standards

## Quality Requirements

### Pre-Release Checklist
- [ ] All components shown in BOM
- [ ] Item balloons match BOM
- [ ] Assembly sequence clear
- [ ] Fastener specifications complete
- [ ] Torque values specified
- [ ] Interface dimensions defined
- [ ] Assembly notes comprehensive
- [ ] Section views show critical areas

## References

- **Parent README**: [`../README.md`](../README.md) - General drawing standards
- **ASSEMBLIES**: [`../../ASSEMBLIES/README.md`](../../ASSEMBLIES/README.md) - Source CAD assemblies
- **Standards**: `/00-PROGRAM/STANDARDS/` - Applicable assembly standards
