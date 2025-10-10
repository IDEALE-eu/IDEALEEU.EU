# TEMPLATES — CAD Templates and Standards

## Purpose

This directory contains reusable CAD templates, libraries, and standard components for the 53_00 Structural Body design work.

## What to Store

### Template Types
- **Part templates**: Pre-configured part files with standard settings
- **Assembly templates**: Skeleton assemblies with reference geometry
- **Drawing templates**: Standard drawing sheets with title blocks
- **Material libraries**: Material property databases
- **Standard parts**: Fasteners, inserts, bushings, hardware

### Design Standards
- **Coordinate systems**: Standard datum reference frames
- **Layer/level standards**: Organization conventions
- **Naming conventions**: File and feature naming rules
- **Design parameters**: Standard dimension names and formulas
- **Feature libraries**: Common design features (holes, slots, pockets)

## Naming Convention

Use the following naming pattern:
```
Template_<type>_<description>_<variant>.<ext>
```

Examples:
- `Template_Part_Structural_Frame.CATPart`
- `Template_Assembly_StructuralBody_Section.CATProduct`
- `Template_Drawing_A3_Landscape_IDEALE.CATDrawing`

## Template Content

### Part Templates Include
- **Material assignment**: Default structural material (e.g., Al 2024-T3)
- **Coordinate system**: Origin and reference planes
- **Design parameters**: Standard dimension names
- **Layer structure**: Organized feature layers
- **Properties template**: Metadata fields (part number, revision, etc.)
- **Standard features**: Common holes, fillets, chamfers

### Assembly Templates Include
- **Reference geometry**: Master coordinate system, stations
- **Skeleton structure**: Layout curves and surfaces
- **Standard components**: Bushings, inserts, standard hardware
- **Constraint definitions**: Standard mate types
- **Level of detail**: Display configurations
- **BOM structure**: Product structure template

### Drawing Templates Include
- **Title block**: Company logo, approval blocks, revision table
- **Border and zones**: Standard sheet borders with zone markers
- **Standard views**: Pre-positioned projection views
- **Dimension styles**: Company standard dimension appearance
- **Layer standards**: Dimension, annotation, and geometry layers
- **Scale blocks**: Standard scale callouts

## Material Library

### Aluminum Alloys
- **2024-T3/T4**: High-strength sheet and plate
- **7075-T6/T73**: Ultra-high-strength forgings and extrusions
- **6061-T6**: Moderate strength, good formability
- **7050-T7451**: Thick plate, improved stress corrosion resistance

### Composites
- **Carbon fiber prepreg**: Various areal weights and resin systems
- **Fiberglass**: E-glass and S-glass fabrics
- **Core materials**: Honeycomb (aluminum, Nomex), foam

### Titanium
- **Ti-6Al-4V**: High-strength, high-temperature applications
- **Ti-6Al-2Sn-4Zr-2Mo**: Aerospace structural alloy

## Coordinate System Standards

### Spacecraft Coordinate System
- **X-axis**: Longitudinal, positive forward
- **Y-axis**: Lateral, positive right (starboard)
- **Z-axis**: Vertical, positive down or as defined

### Reference Geometry
Include in templates:
- Master reference planes
- Section cut planes at major stations
- Interface planes to adjacent systems

## Usage Guidelines

### Starting a New Part
1. Select appropriate part template
2. Save as new file with proper naming convention
3. Update part properties (part number, description)
4. Modify template geometry as needed
5. Maintain coordinate system orientation
6. Use standard feature names

### Starting a New Assembly
1. Select appropriate assembly template
2. Insert reference geometry (skeleton)
3. Add components using standard mates/constraints
4. Maintain product structure conventions
5. Document assembly intent in properties

### Creating Drawings
1. Select appropriate drawing template
2. Insert model views from CAD model
3. Apply standard dimension styles
4. Complete title block information
5. Add required notes and standards callouts
6. Export to PDF per standards

## References

### Standards
- **ECSS-E-ST-32C**: Structural design and verification
- **ASME Y14.5**: GD&T standards
- **ISO 1101**: Geometrical tolerancing
- **AS9100**: Quality management

### Related Directories
- **Standards**: [`../../STANDARDS/`](../../STANDARDS/)
- **EBOM**: [`../../EBOM_LINKS.md`](../../EBOM_LINKS.md)

## Best Practices

### Template Usage
- Always start from template (don't copy from previous project)
- Don't modify master templates (save as new file immediately)
- Follow template structure and conventions
- Update template properties before significant work
- Request template updates when common needs arise
