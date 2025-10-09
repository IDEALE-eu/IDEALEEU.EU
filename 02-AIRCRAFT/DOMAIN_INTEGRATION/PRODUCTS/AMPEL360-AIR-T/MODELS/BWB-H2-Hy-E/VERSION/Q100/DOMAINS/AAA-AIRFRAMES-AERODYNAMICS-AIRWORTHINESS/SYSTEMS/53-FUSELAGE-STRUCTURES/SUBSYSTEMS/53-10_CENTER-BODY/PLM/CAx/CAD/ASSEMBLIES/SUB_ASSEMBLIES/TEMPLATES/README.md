# TEMPLATES — Sub-Assembly Templates and Standards

## Purpose

This directory contains reusable templates, standard sub-assemblies, and configuration templates for 53-10 Center Body sub-assemblies. Templates ensure consistency, reduce design time, and enforce design standards across all sub-assemblies.

## Contents

### Assembly Templates
- **Frame section templates**: Standard frame+stringer+skin configurations
- **Bay templates**: Standard bay assembly structure
- **Interface templates**: Standard interface assembly patterns
- **Panel templates**: Standard panel assembly configurations

### Standard Sub-Assemblies
- **Clip assemblies**: Frame-to-stringer clip standards
- **Splice assemblies**: Standard splice configurations
- **Reinforcement patterns**: Standard doubler and reinforcement designs
- **Fastener patterns**: Standard fastener spacing and patterns

### Configuration Templates
- **BOM templates**: Standard bill of materials formats
- **Drawing templates**: Standard drawing layouts for sub-assemblies
- **Documentation templates**: Standard document formats
- **Checklist templates**: Standard inspection and verification checklists

## Naming Convention

Use the following pattern for template files:
```
TEMPLATE_<assembly-type>_<configuration>.<ext>
```

Examples:
- `TEMPLATE_FRAME-SECTION_STANDARD.CATProduct`
- `TEMPLATE_STRINGER-BAY_WITH-SPLICE.asm`
- `TEMPLATE_BOM_SUB-ASSEMBLY.xlsx`
- `TEMPLATE_DRAWING_ASSEMBLY-VIEW.CATDrawing`

## Template Types

### Parametric Templates
- **Configurable dimensions**: Adjustable key dimensions
- **Design tables**: Family of parts from single template
- **Formulas and relations**: Automatic sizing and relationships
- **Configuration options**: Switchable design variants

### Skeleton Templates
- **Reference geometry**: Coordinate systems, datum planes
- **Layout structure**: Basic assembly structure
- **Interface definitions**: Standard interface points
- **Design intent**: Captured design principles

### Standard Assemblies
- **Proven designs**: Pre-validated standard assemblies
- **Reusable modules**: Common sub-assemblies used repeatedly
- **Best practices**: Embodiment of design best practices
- **Quality built-in**: Standard quality features included

## Template Usage

### Starting New Design
1. **Select template**: Choose appropriate template for assembly type
2. **Copy template**: Create copy (don't modify original)
3. **Rename**: Apply proper naming convention
4. **Configure**: Adjust parameters for specific application
5. **Customize**: Add unique features as needed
6. **Validate**: Verify design meets requirements

### Template Modification
- **Never modify master templates directly**
- **Save as new file immediately after opening**
- **Maintain template structure and organization**
- **Follow template conventions and standards**
- **Request template updates if improvements needed**

## Standard Assembly Structures

### Frame Section Template Structure
```
FRAME-SECTION-TEMPLATE
├── Frame (parametric - length, height, cross-section)
├── Stringers (quantity, type, spacing)
├── Skin Panels (inner/outer, thickness)
├── Clips (standard clip assembly)
├── Fasteners (standard pattern)
└── Reference Geometry (coordinate system, planes)
```

### Stringer Bay Template Structure
```
STRINGER-BAY-TEMPLATE
├── Stringer (parametric - length, cross-section)
├── Splice Fittings (standard splice assembly)
├── Skin Panels (attached panels)
├── Clips (frame-to-stringer clips)
├── Fasteners (standard pattern)
└── Reference Geometry (bay limits, stations)
```

### Panel Module Template Structure
```
PANEL-MODULE-TEMPLATE
├── Primary Panel (parametric - dimensions, thickness)
├── Doublers (edge, corner reinforcements)
├── Cutout Reinforcements (parametric positions)
├── Edge Stiffeners (standard edge treatment)
├── Fastener Pattern (standard spacing)
└── Reference Geometry (panel boundaries)
```

## Template Parameters

### Dimensional Parameters
- **Length**: Overall length or span
- **Width**: Width or bay spacing
- **Height**: Height or depth
- **Thickness**: Material thickness
- **Spacing**: Fastener or feature spacing

### Configuration Parameters
- **Quantity**: Number of repeated features
- **Type**: Component type selection
- **Material**: Material specification
- **Side**: Left/right or upper/lower
- **Option**: Optional features on/off

## Design Standards

Templates enforce:
- **Material standards**: Approved materials and specifications
- **Fastener standards**: Standard fastener types and sizes
- **Joint standards**: Standard joint designs and details
- **Tolerance standards**: Standard dimensional tolerances
- **Finish standards**: Standard surface finishes

## Template Library

### Maintain Library of:
- **Structural templates**: Primary structure sub-assemblies
- **Joint templates**: Standard joint designs
- **Interface templates**: Standard interface configurations
- **Hardware templates**: Standard hardware assemblies
- **Fixture templates**: Standard assembly fixtures

## Documentation Templates

### BOM Template
- Standard bill of materials format
- Required fields and columns
- Formatting and layout standards
- Formula for rollups and totals

### Drawing Template
- Standard title block
- View arrangement
- Dimensioning standards
- Note and callout standards

### Inspection Template
- Standard inspection checklist format
- Required inspection points
- Acceptance criteria format
- Documentation requirements

## Related Directories

- **Frame sections**: [`../FRAME_SECTIONS/`](../FRAME_SECTIONS/) - Use frame templates
- **Stringer bays**: [`../STRINGER_BAYS/`](../STRINGER_BAYS/) - Use stringer templates
- **All sub-assemblies**: Templates applicable to all types
- **CAD templates**: [`../../../../TEMPLATES/`](../../../../TEMPLATES/) - CAD-specific templates
- **Documentation**: [`../DOCS/`](../DOCS/) - Documentation templates

## Template Maintenance

### Template Updates
- Review templates periodically
- Incorporate lessons learned
- Update for design improvements
- Validate changes before release
- Notify users of template changes

### Template Validation
- Test templates before release
- Verify parameter functionality
- Check for errors and issues
- Validate against standards
- Document template usage

### Version Control
- Maintain template revision history
- Tag template releases
- Document changes to templates
- Archive obsolete templates
- Maintain template library

## Standard Parts Library

Include library of:
- **Fasteners**: Standard fastener catalog
- **Hardware**: Bushings, inserts, fittings
- **Clips and brackets**: Standard attachment hardware
- **Seals and gaskets**: Standard sealing components
- **Reference geometry**: Standard datum and coordinate systems

## Best Practices

### Template Design
- **Parametric**: Make key dimensions adjustable
- **Modular**: Design for reusability
- **Documented**: Include usage instructions
- **Validated**: Test before releasing
- **Standardized**: Follow design standards

### Template Usage
- **Always start from template**: Don't copy from previous project
- **Don't modify master**: Save as new file immediately
- **Follow conventions**: Maintain template structure
- **Update properties**: Fill in metadata before starting work
- **Request improvements**: Suggest template enhancements

### Quality Assurance
- Templates undergo design review
- Test templates before deployment
- Validate parameters and formulas
- Ensure template metadata is complete
- Check compatibility across CAD versions
- Verify standard parts are current

## Metadata Requirements

Each template should include:
- **Template name**: Descriptive template identifier
- **Template type**: Assembly, part, drawing, document
- **Description**: Purpose and usage
- **Parameters**: List of configurable parameters
- **Version**: Template revision level
- **Date**: Template creation or revision date
- **Author**: Template creator
- **Status**: Draft, released, or obsolete
- **Usage instructions**: How to use the template

## Training and Support

### Template Training
- Training on template library
- How to select appropriate template
- How to configure parameters
- Best practices for template usage
- When to request new templates

### Template Support
- Helpdesk for template questions
- Documentation and user guides
- Example assemblies using templates
- FAQs and troubleshooting
- Template request process

## Continuous Improvement

### Feedback Loop
- Collect user feedback on templates
- Track template usage and issues
- Identify opportunities for new templates
- Improve existing templates based on experience
- Share best practices across projects

### Template Development
- Identify common assembly patterns
- Develop templates for repetitive designs
- Validate with users before release
- Document and train on new templates
- Maintain template library currency

## Version Control

- Track template revisions in Git
- Tag template releases
- Document template changes
- Notify users of updates
- Archive obsolete templates but keep accessible
- Maintain template change history
