# TEMPLATES — IGES Export Templates and Reference Files

## Purpose

This directory contains template files, reference geometry, and standardized IGES exports that serve as examples or starting points for new exports.

## Content

Store template files including:
- **Export templates**: Pre-configured IGES files with standard settings
- **Reference geometry**: Standard shapes and features for validation
- **Test files**: Known-good files for CAD system testing
- **Examples**: Sample exports demonstrating best practices
- **Configuration files**: Export settings and configurations
- **Guidelines**: Export procedure documents

## Template Types

### Export Settings Templates
- **CAD system configurations**: Pre-set export options for each CAD tool
- **IGES version settings**: Standard IGES 5.3 configurations
- **Entity type templates**: Preferred entity selections
- **Tolerance settings**: Standard tolerance configurations

### Geometry Templates
- **Test geometry**: Simple shapes for validation (cube, cylinder, etc.)
- **Reference parts**: Standard parts for comparison
- **Feature templates**: Common features (holes, fillets, etc.)
- **Assembly templates**: Standard assembly structures

### Documentation Templates
- **README templates**: Standard README file structures
- **Validation checklists**: QA check templates
- **Export procedures**: Step-by-step export guides
- **Metadata templates**: Standard file information

## File Naming Convention

```
TEMPLATE_<template-type>_<description>.<ext>
```

**Examples:**
- `TEMPLATE_EXPORT_CATIA-V5-SETTINGS.xml`
- `TEMPLATE_GEOMETRY_TEST-CUBE.igs`
- `TEMPLATE_README_PART-DIRECTORY.md`
- `TEMPLATE_CHECKLIST_VALIDATION.pdf`

## Using Templates

### For New Exports
1. Copy relevant template
2. Modify for specific part/assembly
3. Follow template structure and settings
4. Maintain template formatting
5. Update metadata appropriately

### For CAD Export Settings
1. Import configuration template into CAD system
2. Verify settings are appropriate
3. Adjust for specific part if needed
4. Execute export
5. Validate results

## Template Maintenance

Templates should be:
- **Reviewed regularly**: Update for new CAD versions or standards
- **Version controlled**: Track template changes
- **Documented**: Include usage instructions
- **Validated**: Ensure templates produce good results
- **Standardized**: Consistent across all templates

## Related Directories

- **Parent**: [`../`](../) — Root IGES directory
- **Parts**: [`../PARTS/`](../PARTS/) — Apply templates for part exports
- **Assemblies**: [`../ASSEMBLIES/`](../ASSEMBLIES/) — Assembly export templates
- **QA**: [`../QA/CHECKS/`](../QA/CHECKS/) — Validation templates

## Standard Export Settings Template

### CATIA V5/V6 Export Settings
```
IGES Version: 5.3
Output Type: Trimmed surfaces (or B-rep solid)
Units: Millimeters
Tolerance: 0.001 mm
Export Options:
  ☑ All visible entities
  ☑ Current model only (or assembly structure)
  ☐ Construction geometry (unless needed)
```

### Siemens NX Export Settings
```
Version: IGES 5.3
Type: Trimmed parametric surfaces (or solid)
Units: Millimeters
Resolution: 0.001 mm
Options:
  ☑ Export all layers
  ☑ Maintain layer structure
```

### SolidWorks Export Settings
```
Format: IGES 5.3
Options: Trimmed surfaces (or solid entities)
Units: Millimeters
Options:
  ☑ Export all components (for assemblies)
  ☑ Save all components to single file (or separate files)
```

### Creo (PTC) Export Settings
```
IGES Version: 5.3
Entities: Surfaces (or solids)
Units: Millimeters
Options:
  ☑ Trimmed surfaces
  ☑ Export all datum planes (if needed)
```

## Test Geometry Templates

Standard test geometries for validation:
- **Simple cube**: 100mm x 100mm x 100mm cube
- **Cylinder**: 50mm diameter x 100mm length
- **Complex surface**: NURBS surface with trim curves
- **Assembly test**: Simple 2-3 part assembly
- **Feature test**: Part with holes, fillets, chamfers

These can be exported and tested in various CAD systems to verify compatibility.

## README Template

Standard README structure for subdirectories:
```markdown
# [DIRECTORY NAME] — [Brief Description]

## Purpose
[What this directory contains and why]

## Content
[What types of files go here]

## File Naming Convention
[Standard naming pattern with examples]

## [Additional Sections as Needed]

## Related Directories
[Links to related directories]

## Best Practices
[Guidelines for using this directory]
```

## Best Practices

- Use templates for consistency
- Update templates when standards change
- Document template purpose and usage
- Test templates before deployment
- Version control template changes
- Train users on template usage
- Gather feedback for improvement
- Maintain template library

## Template Development

When creating new templates:
1. Identify need or recurring issue
2. Design template to address need
3. Document template usage
4. Test template thoroughly
5. Get feedback from users
6. Refine based on feedback
7. Deploy and communicate
8. Monitor usage and effectiveness

## Template Library

Maintain organized template library with:
- Clear organization by type
- Usage instructions for each template
- Version history and changelog
- Contact for template questions
- Regular review and updates
- Retirement of obsolete templates
