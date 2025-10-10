# TEMPLATES — Assembly Templates

## Purpose

This directory contains template files and standard resources for creating top-level assemblies.

## Template Types

### Assembly Templates
- **Skeleton assemblies**: Pre-configured assembly structure
- **Reference geometry**: Standard coordinate systems and planes
- **Material libraries**: Standard material definitions
- **Property templates**: Standard property sets

### CAD System Templates
- **CATIA**: `.CATProduct` template with standard settings
- **NX**: `.prt` assembly template
- **SolidWorks**: `.asmdot` assembly template
- **Creo**: `.asm` start assembly

## Template Contents

### Standard Elements
- **Reference coordinate systems**: Aircraft frame, local frames
- **Reference planes**: Symmetry plane, bulkhead planes, floor planes
- **Standard views**: Front, top, right, isometric
- **Standard layers/levels**: Organizational structure
- **Standard colors**: Material or system-based coloring
- **Drawing templates**: Title blocks and formats

### Configuration
- **Units**: Millimeters, degrees
- **Tolerances**: Default tolerance values
- **Display settings**: Graphics quality, lighting
- **Analysis settings**: Standard analysis parameters

## Template Files

### File Types
- `.CATProduct` — CATIA assembly template
- `.prt` — NX assembly template
- `.asmdot` — SolidWorks assembly template
- `.asm` — Creo assembly template
- `.txt` — Configuration files
- `.pdf` — Template documentation

## Naming Convention

```
53-10_TEMPLATE_<type>_<version>.<ext>
```

Examples:
- `53-10_TEMPLATE_ASSEMBLY_v01.CATProduct`
- `53-10_TEMPLATE_SKELETON_v01.prt`
- `53-10_TEMPLATE_CONFIG_v01.txt`

## Using Templates

### Starting New Assembly
1. Copy template to working directory
2. Rename per naming convention
3. Verify reference geometry
4. Begin adding components
5. Update properties (part number, description)

### Customizing Templates
- Add project-specific references
- Configure display settings
- Set up standard mates/constraints
- Define configurations

## Template Maintenance

### Updates
- Review templates quarterly
- Incorporate lessons learned
- Update for CAD system upgrades
- Improve based on user feedback

### Version Control
- Track template versions
- Document changes
- Test before releasing
- Communicate updates to team

## Standard References

### Reference Geometry Files
- `53-10_REF_COORD-SYSTEMS.txt` — Coordinate system definitions
- `53-10_REF_DATUMS.pdf` — Datum definitions
- `53-10_REF_INTERFACES.xlsx` — Interface locations

### Configuration Files
- `cad-settings.txt` — CAD system settings
- `material-library.xml` — Standard materials
- `color-scheme.txt` — Standard color assignments

## Best Practices

### Template Design
- Keep templates **simple and generic**
- Include only **essential elements**
- Document **how to use** the template
- Provide **examples** of completed assemblies
- Test templates **before release**

### Template Usage
- **Always start from template** for consistency
- **Don't modify templates** in place
- **Suggest improvements** to template owners
- **Follow naming conventions**

## Documentation

Each template should include:
- **Purpose**: What the template is for
- **Instructions**: How to use it
- **Assumptions**: What is pre-configured
- **Customization**: What to change
- **Examples**: Sample usage
- **Support**: Who to contact for help

## Related Resources

- **Reference Geometry**: [`../REFERENCE_GEOMETRY/`](../REFERENCE_GEOMETRY/) — Standard references
- **Documentation**: [`../DOCS/`](../DOCS/) — Assembly documentation standards
- **Examples**: Completed assemblies as reference
