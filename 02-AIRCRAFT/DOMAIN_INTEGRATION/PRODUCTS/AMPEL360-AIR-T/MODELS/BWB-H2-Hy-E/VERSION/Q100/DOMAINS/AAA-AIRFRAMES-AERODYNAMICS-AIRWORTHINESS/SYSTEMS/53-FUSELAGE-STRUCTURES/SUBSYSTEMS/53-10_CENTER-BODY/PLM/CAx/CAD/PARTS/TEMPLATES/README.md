# TEMPLATES — Part Templates and Design Libraries

## Purpose

This directory contains reusable CAD templates, master parts, and design libraries for creating new parts in the 53-10 Center Body subsystem. Templates standardize part creation, ensure consistency, and embed design rules and company standards.

## Content Types

### Part Templates
- **Structural member templates**: Frame, stringer, skin panel templates
- **Detail part templates**: Bracket, fitting, clip templates
- **Sheet metal templates**: Standard bend radii and forming parameters
- **Machined part templates**: Standard material removal operations
- **Composite part templates**: Layup definitions and ply orientations

### Feature Libraries
- **Standard holes**: Fastener holes, lightening holes, access holes
- **Chamfers and fillets**: Standard edge treatments
- **Slots and pockets**: Common machined features
- **Bend zones**: Standard sheet metal bends
- **Surface finishes**: Standard texture and coating callouts

### Design Tables
- **Parametric families**: Size-scalable parts (frames, stringers)
- **Configuration tables**: Options and variants
- **Material properties**: Standard material definitions
- **Dimension standards**: Standard sizes and increments

## Naming Convention

```
TEMPLATE_<component-type>_<description>.<ext>
```

Examples:
- `TEMPLATE_FRAME_CIRCUMFERENTIAL.CATPart`
- `TEMPLATE_STRINGER_HAT-SECTION.prt`
- `TEMPLATE_BRACKET_L-SHAPED.sldprt`
- `TEMPLATE_FEATURES_FASTENER-HOLES.catpart`

## Template Structure

### Embedded Content
Templates should include:
- **Coordinate system**: Origin at standard reference point
- **Material assignment**: Default structural material
- **Properties template**: Metadata fields (part number, revision, etc.)
- **Design parameters**: Driven dimensions with descriptive names
- **Standard features**: Common design elements
- **Layer/level structure**: Organized feature layers
- **Units**: Consistent unit system (metric or imperial)

### Design Intent
- Parametric relationships for design flexibility
- Geometric constraints for design rules
- Equations for derived dimensions
- Configurable options using design tables

## Usage Guidelines

### Creating New Parts from Templates
1. Select appropriate template for part type
2. Save as new part with proper naming convention
3. Modify parameters to suit specific design
4. Add custom features as needed
5. Update metadata (part number, description)
6. Validate design rules and constraints

### Maintaining Templates
- Review templates quarterly for improvements
- Update based on lessons learned
- Incorporate new design standards
- Test templates with representative designs
- Version control template changes

## Template Categories

### Primary Structure Templates
- **Frame templates**: Various frame profiles and sizes
- **Stringer templates**: Hat, Z, blade, and I-beam sections
- **Skin panel templates**: Flat and contoured panels
- **Bulkhead templates**: Flat, domed, and corrugated

### Detail Part Templates
- **Bracket templates**: L, T, Z, and gusset configurations
- **Fitting templates**: Lug, clevis, and pin fittings
- **Clip templates**: Sheet metal clips and fastener clips

### Standard Features
- **Hole feature library**: Countersunk, counterbored, clearance holes
- **Fillet library**: Standard radii for different applications
- **Chamfer library**: Standard angles and sizes
- **Surface finish library**: Standard callouts and symbols

## Cross-References

- **CAD standards**: [`../../TEMPLATES/`](../../TEMPLATES/) (system-level templates)
- **Design standards**: `../../../51-STRUCTURES-GENERAL/SUBSYSTEMS/51-00_GENERAL/`
- **Material libraries**: [`../../../CAE/DATA/MATERIALS_DB/`](../../../CAE/DATA/MATERIALS_DB/)
- **Component directories**: See parent [`../README.md`](../README.md)

## Best Practices

### Template Design
- Keep templates simple and flexible
- Use clear parameter names
- Document design intent in comments
- Avoid over-constraining geometry
- Test template with multiple configurations

### Consistency
- Use consistent coordinate systems across templates
- Apply standard material assignments
- Follow naming conventions
- Maintain uniform units and precision

## Quality Standards

Templates must meet:
- Company CAD standards
- Parametric modeling best practices
- Rebuild reliability (no broken references)
- Documentation completeness
- Validation with representative designs
