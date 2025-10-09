# TEMPLATES — CAD Templates and Standards

## Purpose

This directory contains reusable CAD templates, libraries, and standard components for the 53-10 Center Body design work.

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

## Template Organization

### Part Templates
```
TEMPLATES/
├── Part_Template_Structural.CATPart
├── Part_Template_Sheet_Metal.CATPart
├── Part_Template_Machined.CATPart
└── Part_Template_Composite.CATPart
```

### Assembly Templates
```
TEMPLATES/
├── Assembly_Template_Frame_Section.CATProduct
├── Assembly_Template_Skin_Panel.CATProduct
└── Assembly_Template_Full_Section.CATProduct
```

### Drawing Templates
```
TEMPLATES/
├── Drawing_Template_A4_Portrait.CATDrawing
├── Drawing_Template_A3_Landscape.CATDrawing
├── Drawing_Template_A1_Assembly.CATDrawing
└── Drawing_Template_E_Size.CATDrawing
```

## Naming Convention

Use the following naming pattern:
```
Template_<type>_<description>_<variant>.<ext>
```

Examples:
- `Template_Part_Structural_Frame.CATPart`
- `Template_Assembly_CenterBody_Section.CATProduct`
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
- **Reference geometry**: Master coordinate system, stations, waterlines
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

## Standard Parts Library

### Fasteners
- **Aerospace fasteners**: NAS, MS, AN, BACR series
- **Rivets**: Solid rivets, blind rivets (e.g., Cherry rivets)
- **Bolts and nuts**: Hex head, close tolerance, Hi-Lok, Lockbolt
- **Screws**: Machine screws, self-locking screws

### Hardware
- **Inserts**: Threaded inserts, heat-set inserts
- **Bushings**: Sleeve bearings, spherical bearings
- **Washers**: Flat washers, lock washers, fender washers
- **Clips and clamps**: Spring clips, cable clamps

### Interface Components
- **Brackets**: Standard mounting brackets
- **Lugs**: Attachment lugs, clevis fittings
- **Fittings**: Angle fittings, splice fittings

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

### Steel
- **300M**: High-strength steel for landing gear
- **15-5 PH**: Precipitation hardening stainless steel
- **4340**: High-strength alloy steel

## Coordinate System Standards

### Aircraft Coordinate System
- **X-axis**: Fuselage station (FS), positive aft
- **Y-axis**: Buttline (BL), positive right (starboard)
- **Z-axis**: Waterline (WL), positive up

### Center Body Stations
- **FS 1000-1500**: Center body extent (example values)
- **BL 0**: Fuselage centerline
- **WL reference**: From ground line or keel

### Reference Geometry
Include in templates:
- Master reference planes (FS, BL, WL)
- Section cut planes at major stations
- Mold lines (OML, IML)
- Interface planes to adjacent sections

## Design Rules Embedded in Templates

### Structural Design
- **Minimum bend radius**: Per material thickness and grain direction
- **Edge distance**: For holes near edges
- **Fastener spacing**: Pitch and gage dimensions
- **Material thickness**: Standard gauge thicknesses

### Manufacturing Constraints
- **Tool access**: Minimum clearances for fastener installation
- **Weld preparation**: Standard joint preps and weld symbols
- **Machine limitations**: Max part envelope, feature sizes
- **Assembly clearances**: Gap requirements for assembly

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

## Template Maintenance

### Version Control
- Templates are configuration-controlled
- Changes require engineering approval
- Version templates with release dates
- Archive superseded templates

### Update Process
1. Identify need for template change
2. Document change request
3. Engineering review and approval
4. Update template file
5. Notify all users of change
6. Archive previous version

## References

### Standards
- **ATA Chapter 53**: Fuselage structures
- **ASME Y14.5**: GD&T standards
- **ISO 1101**: Geometrical tolerancing
- **AS9100**: Quality management
- **Company design manual**: Internal standards

### Related Directories
- **General structures**: [`../../../51-STRUCTURES-GENERAL/SUBSYSTEMS/51-00_GENERAL/`](../../../51-STRUCTURES-GENERAL/SUBSYSTEMS/51-00_GENERAL/)
- **Standards**: [`../../STANDARDS/`](../../STANDARDS/)
- **EBOM**: [`../../EBOM_LINKS.md`](../../EBOM_LINKS.md)

## Best Practices

### Template Usage
- Always start from template (don't copy from previous project)
- Don't modify master templates (save as new file immediately)
- Follow template structure and conventions
- Update template properties before significant work
- Request template updates when common needs arise

### Design Efficiency
- Use templates to enforce design standards
- Leverage parametric design in templates
- Create family tables for similar parts
- Build libraries of proven designs
- Share successful templates with team

### Quality Assurance
- Templates undergo same review as released parts
- Test templates before deployment
- Validate material properties and parameters
- Ensure template metadata is complete
- Check compatibility across CAD versions
