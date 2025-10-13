# TEMPLATES — Standard Templates and Examples

## Purpose

This directory contains **template files and examples** that demonstrate proper STEP export format, naming conventions, PMI standards, and best practices.

## What to Store

- STEP export templates
- Example files with proper formatting
- PMI/GD&T annotation templates
- Naming convention examples
- Metadata templates
- Configuration examples

## Template Types

### Export Templates
- Part template with standard metadata
- Assembly template with proper structure
- PMI template with GD&T examples
- Surface model template

### Naming Examples
```
53-10_TEMPLATE_PART_PN-XXXXX_Rev0_YYYYMMDD.step
53-10_TEMPLATE_ASSEMBLY_PN-XXXXX_Rev0_YYYYMMDD.step
53-10_TEMPLATE_PMI_PN-XXXXX_Rev0_YYYYMMDD.step
```

### Metadata Templates
Standard attributes to include:
- Part number
- Revision
- Material specification
- Mass properties
- Author and date
- CAD system version
- Export settings used

## Usage Guidelines

### For Engineers
1. Copy template file as starting point
2. Follow naming convention
3. Include required metadata
4. Use standard export settings
5. Validate before committing

### For New Team Members
- Review templates to understand standards
- Use examples as reference
- Follow established patterns
- Ask questions if unclear

## Best Practice Examples

Templates demonstrate:
- ✅ Proper file structure
- ✅ Complete metadata
- ✅ Correct naming convention
- ✅ Appropriate PMI inclusion
- ✅ Valid geometry export
- ✅ Assembly hierarchy

## Template Maintenance

- Keep templates updated with current standards
- Review and refresh annually
- Incorporate lessons learned
- Update for new CAD system versions
- Align with industry best practices

## Related Directories

- [**../PARTS/**](../PARTS/) — Actual part files following templates
- [**../ASSEMBLIES/**](../ASSEMBLIES/) — Assembly files
- [**../SCHEMAS/AP242/**](../SCHEMAS/AP242/) — Format specifications
- [**../QA/CHECKS/**](../QA/CHECKS/) — Validation criteria

## Export Settings Reference

Standard export settings for templates:

### CATIA V5/V6
```
Format: AP242
☑ Export PMI
☑ Assembly structure
☑ Attributes
☑ Exact geometry (not tessellated)
```

### Siemens NX
```
Protocol: AP242
☑ Export PMI
☑ Product structure
☑ Attributes
☑ Part transformations
```

### SolidWorks
```
Format: STEP AP242
☑ Include dimensions
☑ Include tolerances
☑ Geometry + PMI
```

## References

- Parent directory: [**../**](../)
- Main STEP README: [**../README.md**](../README.md)
- Standards: `00-PROGRAM/STANDARDS/04-CROSS_CUTTING/DATA_EXCHANGE/`
- Training materials: `00-PROGRAM/TRAINING/`
