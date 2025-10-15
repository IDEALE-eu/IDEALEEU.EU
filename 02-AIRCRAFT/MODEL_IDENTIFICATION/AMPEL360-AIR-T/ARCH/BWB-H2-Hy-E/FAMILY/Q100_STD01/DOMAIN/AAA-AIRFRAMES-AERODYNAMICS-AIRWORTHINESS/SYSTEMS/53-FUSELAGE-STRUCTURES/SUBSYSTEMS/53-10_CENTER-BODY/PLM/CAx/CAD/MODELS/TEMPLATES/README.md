# TEMPLATES — CAD Model Templates

## Purpose

This directory contains reusable CAD templates for creating new models in the 53-10 Center Body design. Templates ensure consistency, embed design standards, and accelerate modeling work.

## Content

Templates may include:
- Part file templates with standard settings
- Assembly templates with skeleton structure
- Standard feature libraries
- Model property templates
- Naming and numbering templates

## Naming Convention

Use the following pattern for template files:
```
TEMPLATE_<TYPE>_<CATEGORY>_<DESCRIPTION>.<ext>
```

Examples:
- `TEMPLATE_PART_FRAME_STANDARD.CATPart`
- `TEMPLATE_ASSY_SUBCOMP_SKELETON.CATProduct`
- `TEMPLATE_PART_SKIN-PANEL_PARAMETRIC.prt`

## Template Types

### Part Templates
Pre-configured part files including:
- Standard coordinate system orientation
- Default material assignments
- Standard layers/levels
- Parameter naming conventions
- Feature templates (holes, slots, pockets)
- Model properties structure

### Assembly Templates
Assembly skeletons including:
- Reference geometry
- Standard coordinate systems
- Layout structure
- Interface placeholders
- Constraint templates
- Bill of materials structure

### Feature Libraries
Reusable design features:
- Standard hole patterns
- Bracket attach provisions
- Fastener patterns (pitch and gage)
- Standard cutouts and pockets
- Lightening hole patterns
- Corner and edge treatments

## Usage Guidelines

When using templates:
1. Copy template to appropriate directory
2. Rename following naming conventions
3. Update model properties (part number, title, etc.)
4. Modify geometry as needed
5. Do not alter standard settings or structure
6. Report template issues for improvement

## Template Settings

Templates embed standard settings:
- **Units**: SI (mm, kg, N)
- **Precision**: 0.01 mm modeling, 0.1 mm documentation
- **Coordinate system**: Right-handed, Z-up
- **Material library**: Standard material database
- **Layer standards**: Dimension, geometry, construction layers

## Design Rules in Templates

Templates include built-in design rules:
- Minimum bend radii by material/thickness
- Edge distance for holes
- Fastener spacing requirements
- Material thickness standards
- Manufacturing constraints

## Maintenance

Template maintenance:
- Regular review and updates
- User feedback incorporation
- Version control with change notes
- Communication of template changes
- Archive of obsolete templates

## Related Documentation

- **Design rules**: [`../CONFIG/DESIGN_RULES/`](../CONFIG/DESIGN_RULES/)
- **Standard parts**: [`../LIBRARY/`](../LIBRARY/)
- **Design parameters**: [`../CONFIG/PARAMETERS/`](../CONFIG/PARAMETERS/)
- **Structural standards**: [`../../../51-STRUCTURES-GENERAL/SUBSYSTEMS/51-00_GENERAL/`](../../../51-STRUCTURES-GENERAL/SUBSYSTEMS/51-00_GENERAL/)

## Template Sources

Templates are based on:
- Company design standards
- Industry best practices (ATA, ASME, ISO)
- Lessons learned from previous designs
- CAD system recommendations
- Manufacturing process requirements

## Quality Requirements

Templates must:
- [ ] Open without errors in target CAD system
- [ ] Include all standard settings
- [ ] Have complete documentation
- [ ] Be validated against design rules
- [ ] Include usage instructions
- [ ] Be version controlled
