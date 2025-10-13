# TEMPLATES — Drawing Templates and Standards

## Purpose

This directory contains standard drawing templates, title blocks, and reusable drawing resources for creating consistent, high-quality drawings for the 53-10 Center Body subsystem.

## What to Store

### Drawing Templates
- **Title block templates**: Standard title blocks with company/project information
- **Sheet formats**: Standard sheet sizes (A4, A3, A2, A1, A0, E-size, D-size, etc.)
- **Border templates**: Drawing borders and frames
- **Revision block templates**: Standard revision tracking blocks
- **BOM templates**: Bill of materials table formats
- **Note blocks**: Standard notes and specifications

### Standard Elements
- **Symbol libraries**: Standard symbols (GD&T, weld, surface finish, etc.)
- **Line styles**: Standard line types and weights
- **Text styles**: Standard fonts and text heights
- **Dimension styles**: Standard dimensioning conventions
- **Layer standards**: Drawing layer organization
- **View layouts**: Standard view arrangements

## Template Types

### Part Drawing Templates
```
53-10_TEMPLATE_PART_A4_PORTRAIT.dwg
53-10_TEMPLATE_PART_A3_LANDSCAPE.dwg
53-10_TEMPLATE_PART_A1_SHEET.dwg
```
- Pre-configured for part drawings
- Standard views layout (front, top, right)
- Part-specific title block fields
- Detail view callout standards

### Assembly Drawing Templates
```
53-10_TEMPLATE_ASSEMBLY_A3_LANDSCAPE.dwg
53-10_TEMPLATE_ASSEMBLY_A1_SHEET.dwg
53-10_TEMPLATE_ASSEMBLY_E-SIZE.dwg
```
- Pre-configured for assembly drawings
- BOM table included
- Balloon styles configured
- Exploded view layout guides
- Assembly-specific title block

### Installation Drawing Templates
```
53-10_TEMPLATE_INSTALLATION_A3_LANDSCAPE.dwg
53-10_TEMPLATE_INSTALLATION_A1_SHEET.dwg
```
- Pre-configured for installation drawings
- Interface dimension tables
- Installation sequence note blocks
- Torque specification tables

### Detail Drawing Templates
```
53-10_TEMPLATE_DETAIL_A4_PORTRAIT.dwg
53-10_TEMPLATE_DETAIL_A3_LANDSCAPE.dwg
```
- Pre-configured for detail drawings
- Multiple detail view layouts
- Enlarged scale callouts
- Parent drawing reference fields

## Title Block Content

### Standard Title Block Fields
- **Project**: AMPEL360-AIR-T / BWB-H2-Hy-E / Q100
- **System**: 53 - FUSELAGE STRUCTURES
- **Subsystem**: 53-10 CENTER BODY
- **Drawing title**: Component or assembly name
- **Drawing number**: Unique identifier
- **Sheet**: Sheet number and total sheets
- **Scale**: Drawing scale or "AS NOTED"
- **Units**: mm (millimeters) or in (inches)
- **Material**: Material specification (for parts)
- **Revision**: Current revision letter
- **Date**: Original or revision date
- **Drawn by**: Designer/drafter name
- **Checked by**: Checker name
- **Approved by**: Engineering approver
- **Company**: IDEALE Consortium logo and info

### Revision Block
Standard revision block includes:
- Revision letter/number column
- Description of change column
- Date column
- Approved by column
- ECO/ECN reference column

## File Formats

### Native CAD Formats
- **AutoCAD**: `.dwg`, `.dwt` (drawing template)
- **CATIA**: `.CATDrawing` template
- **SolidWorks**: `.drwdot` (drawing template)
- **NX**: `.prt` template file
- **Creo**: Drawing template files

### Exchange Formats
- **DXF**: For cross-platform use
- **PDF**: Template examples and guides
- **DWG**: AutoCAD-compatible templates

## Template Standards

### Dimensions and Units
- **Primary units**: Millimeters (mm) or Inches (in)
- **Decimal places**: Per drawing standard (e.g., .XX, .XXX)
- **Angular units**: Degrees, minutes, seconds or decimal degrees
- **Tolerance format**: Per general tolerance block

### Text and Fonts
- **Font**: Arial, Romans, or company standard font
- **Text height**: Standard heights (2.5mm, 3.5mm, 5mm, etc.)
- **Note text**: 2.5mm or 3mm height
- **Dimension text**: 3mm or 3.5mm height
- **Title block text**: 5mm for title, 3.5mm for fields

### Line Standards
- **Visible lines**: 0.5mm or 0.7mm thick
- **Hidden lines**: 0.35mm thick, dashed
- **Center lines**: 0.25mm thick, center line pattern
- **Dimension lines**: 0.25mm thick
- **Section lines**: 0.35mm thick

### Layers/Levels
Standard layer organization:
- **Layer 1**: Visible object lines
- **Layer 2**: Hidden lines
- **Layer 3**: Center lines
- **Layer 4**: Dimensions
- **Layer 5**: Notes and text
- **Layer 6**: Title block
- **Layer 7**: Hatching/section lines
- **Layer 8**: Construction/reference geometry

## GD&T Symbols

### Standard GD&T Symbol Library
Include symbols for:
- **Form**: Straightness, Flatness, Circularity, Cylindricity
- **Orientation**: Perpendicularity, Parallelism, Angularity
- **Location**: Position, Concentricity, Symmetry
- **Runout**: Circular runout, Total runout
- **Profile**: Profile of a line, Profile of a surface
- **Datum**: Datum feature symbols

### Material Condition Modifiers
- **MMC**: Maximum Material Condition
- **LMC**: Least Material Condition
- **RFS**: Regardless of Feature Size (default)

### Other Symbols
- **Surface finish**: Roughness symbols (Ra, Rz)
- **Weld symbols**: Standard weld symbol library
- **Reference dimensions**: Parentheses or REF notation

## Usage Guidelines

### Selecting Templates
- Choose template based on drawing type and size
- Select sheet size appropriate for content
- Use portrait for simple parts, landscape for complex
- Larger sheets (A1, A0, E-size) for assemblies

### Creating New Templates
- Start from existing template when possible
- Follow company standards strictly
- Include all required title block fields
- Set up standard layers/levels
- Configure dimension styles
- Include symbol libraries
- Document template usage in header

### Customizing Templates
- Modify only for specific project needs
- Document customizations
- Maintain backward compatibility
- Update related templates consistently
- Version control customized templates

## Best Practices

### Template Management
- Maintain templates in version control
- Update templates when standards change
- Distribute updated templates to all users
- Train users on template usage
- Periodically review and update
- Maintain template documentation

### Quality Control
- Verify templates meet standards
- Test templates before distribution
- Check title block fields populate correctly
- Ensure layers/levels configured properly
- Validate dimension styles
- Confirm symbol libraries complete

### Consistency
- Use templates for all drawings
- Don't modify title block layout
- Follow layer/level conventions
- Use standard text styles
- Apply standard line types
- Use standard symbols from library

## Related Directories

- **Parent drawings**: [`../`](../) - All drawing types
- **Checks**: [`../CHECKS/`](../CHECKS/) - Quality check templates
- **CAD templates**: [`../../TEMPLATES/`](../../TEMPLATES/) - CAD model templates
- **Standards**: `/00-PROGRAM/STANDARDS/` - Drawing standards documentation

## Template Checklist

### Template Content Verification
- [ ] Title block complete with all fields
- [ ] Revision block included
- [ ] Sheet border and frame correct
- [ ] Standard views laid out appropriately
- [ ] Layers/levels configured
- [ ] Text styles defined
- [ ] Dimension styles configured
- [ ] Symbol libraries included
- [ ] Line types defined
- [ ] Template tested and validated

## References

- **Parent README**: [`../README.md`](../README.md) - General drawing standards
- **Drawing standards**: `/00-PROGRAM/STANDARDS/04-CROSS_CUTTING/DRAWING_STANDARDS/`
- **ASME Y14.5**: GD&T standard
- **ISO 128**: Technical drawings standards
- **Company CAD manual**: Internal CAD standards and procedures
