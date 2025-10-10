# TEMPLATES — CAD Templates and Standards

## Purpose

This directory contains reusable CAD templates, standard components, and reference data for 21-10 radiators and heat exchangers design work, including title blocks, GD&T symbols, and note packs.

## Content

### Template Types
- **Part templates**: Pre-configured part files with standard settings
- **Assembly templates**: Skeleton assemblies with reference geometry
- **Drawing templates**: Standard drawing sheets with title blocks
- **Title blocks**: Company/project standard title blocks
- **GD&T libraries**: Geometric dimensioning and tolerancing symbol libraries
- **Note packs**: Standard notes for common manufacturing processes
- **Material libraries**: Material property databases

## Naming Convention

```
Template_<type>_<description>_<variant>.<ext>
```

Examples:
- `Template_Part_Radiator_Panel.prt`
- `Template_Assembly_LPHX.asm`
- `Template_Drawing_A3_Landscape_21-10.dwg`
- `Template_TitleBlock_IDEALE_Rev2.blk`
- `Notes_Bonding_Adhesive_Standard.txt`

## Template Categories

### Part Templates

#### Radiator Components
- **Facesheet template**: Pre-configured with material (Al 2024), standard thickness options
- **Honeycomb core template**: Cell size, density, orientation parameters
- **Heat pipe template**: Standard diameters, wall thickness, materials
- **Manifold template**: Port standards, thread specifications
- **Fin template**: Fin pitch, thickness, height parameters

#### Configuration
- **Material assignment**: Default thermal materials from CAP material database
- **Coordinate system**: Origin and datum reference frames (A, B, C)
- **Design parameters**: Standard dimension names and formulas
- **Layer structure**: Organized feature layers
- **Properties template**: Metadata fields (part number, revision, material, mass)
- **Units**: mm, kg, deg (consistently applied)

### Assembly Templates

#### Assembly Types
- **Radiator panel assembly**: Facesheet + core + heat pipes skeleton
- **LPHX assembly**: Manifolds + tubes + fins structure
- **Coldplate assembly**: Baseplate + channels + cover skeleton

#### Structure
- **Reference geometry**: Master coordinate system, interface planes
- **Skeleton structure**: Layout curves and reference surfaces
- **Standard components**: Fasteners, inserts, TIMs
- **Constraint definitions**: Standard mate types and reference datums
- **BOM structure**: Product structure template matching EBOM hierarchy
- **Interface definitions**: Mounting patterns per 51 standards

### Drawing Templates

#### Sheet Sizes and Formats
- **A4 (210 x 297 mm)**: Small parts, detail drawings
- **A3 (297 x 420 mm)**: Most common for parts and small assemblies
- **A2 (420 x 594 mm)**: Large assemblies
- **A1 (594 x 841 mm)**: Very large assemblies, installation drawings
- **A0 (841 x 1189 mm)**: Spacecraft-level layouts

#### Layout Options
- Portrait orientation (standard for A4)
- Landscape orientation (preferred for A3 and larger)

#### Drawing Template Contents
- **Title block**: Company logo, project identification, approval blocks
- **Revision table**: Standard revision tracking block
- **Border and zones**: Sheet borders with alphanumeric zone markers
- **Standard views**: Pre-positioned projection view locations
- **Dimension styles**: Company standard dimension appearance
- **Layer standards**: Dimensions, annotations, geometry organized by layer
- **Scale blocks**: Standard scale callouts
- **General notes section**: Space for standard manufacturing notes

### Title Blocks

#### Required Information Fields
- Part number / assembly number
- Part/assembly description
- Designer name and signature
- Checker name and signature
- Approval authority signature
- Dates (designed, checked, approved)
- Revision level
- Sheet number (Sheet X of Y)
- Material specification
- Mass (from 3D model)
- Scale (typically 1:1, 1:2, 2:1, etc.)
- Company/project logo
- Drawing number
- Unit specification (mm)
- Tolerance specification (ISO 2768-mK unless noted)

#### Project-Specific Information
- **Project**: AMPEL360-SPACE-T
- **System**: 21-THERMAL_CONTROL
- **Subsystem**: 21-10_RADIATORS_HEAT_EXCHANGERS
- **Domain**: STA-B-THERMAL-TPS

### GD&T Libraries

#### Geometric Tolerancing Symbols
- **Form**: Flatness, straightness, circularity, cylindricity
- **Orientation**: Parallelism, perpendicularity, angularity
- **Location**: Position, concentricity, symmetry
- **Profile**: Surface profile, line profile
- **Runout**: Circular runout, total runout

#### Datum Reference Frames
- Datum symbols (A, B, C, ...)
- Datum target symbols
- Datum feature control frames

#### Material Condition Modifiers
- MMC (Maximum Material Condition)
- LMC (Least Material Condition)
- RFS (Regardless of Feature Size)

#### Standards
- ISO 1101: Geometrical tolerancing
- ASME Y14.5: Dimensioning and tolerancing

### Note Packs

#### Standard Manufacturing Notes

**General Machining Notes**:
```
1. Remove all burrs and sharp edges (0.2-0.5 mm chamfer unless noted).
2. All dimensions in millimeters unless otherwise stated.
3. Tolerances per ISO 2768-mK unless individually specified.
4. Interpret GD&T per ISO 1101.
5. Material: [SPECIFY] per AMS/ASTM standard.
6. Surface finish: Ra 3.2 μm unless otherwise noted.
```

**Sheet Metal Forming Notes**:
```
1. Material: [SPECIFY] thickness per drawing.
2. Bend radii: [SPECIFY] unless noted.
3. Grain direction: [PARALLEL/PERPENDICULAR] to longest dimension.
4. All dimensions apply to flat pattern before forming.
5. Bend allowance calculated per [SPECIFY METHOD].
```

**Bonding Process Notes**:
```
1. Adhesive: [SPECIFY] per CAP/bonding specification.
2. Surface preparation: [SPECIFY] cleaning and treatment.
3. Cure cycle: [SPECIFY] temperature and duration per CAP.
4. Bondline thickness: [SPECIFY] ± [TOL] mm.
5. Inspection: Visual and NDT per CAP/bonding_inspection.
```

**Coating Application Notes**:
```
1. Coating type: [SPECIFY] per CAP/coating specification.
2. Surface preparation: Clean per ECSS-Q-ST-70-03C.
3. Masking: Per coating mask [MASK P/N].
4. Application method: [SPRAY/DIP/VACUUM DEPOSITION].
5. Thickness: [SPECIFY] ± [TOL] μm.
6. Cure: [SPECIFY] per coating spec.
```

**Heat Pipe Integration Notes**:
```
1. Heat pipe type: [SPECIFY] per supplier specification.
2. Bonding: Thermal epoxy per CAP/heatpipe_bondline_cure.
3. Routing: Per assembly model, avoid sharp bends.
4. Working fluid: [SPECIFY] (NH3, propylene, etc.).
5. Leak test: [SPECIFY] per CAI/leak_test_procedure.
```

**TIM Application Notes**:
```
1. TIM type: [SPECIFY] thermal conductivity [XX] W/m·K.
2. Application: Per CAP/tim_application_torque.
3. Thickness: [SPECIFY] ± [TOL] mm.
4. Torque sequence: [SPECIFY] per drawing.
5. Verification: Flatness check per CAI/flatness_inspection.
```

**Welding Notes**:
```
1. Welding process: [TIG/MIG/LASER] per CAP/lphx_braze_weld_spec.
2. Filler material: [SPECIFY] per AWS specification.
3. Weld preparation: [SPECIFY] joint type and fit-up.
4. Post-weld treatment: [SPECIFY] if required.
5. Inspection: Visual, dye penetrant, or radiographic per [SPEC].
```

#### Inspection and Quality Notes
```
1. Dimensional inspection per CAI/flatness_inspection_plan.
2. Leak test per CAI/leak_test_procedure (if pressure vessel).
3. Visual inspection: No cracks, voids, delamination.
4. Mass measurement: [SPECIFY] ± [TOL]% of nominal.
5. Documentation: Inspection report with serial number traceability.
```

## Material Library

### Aluminum Alloys
- **2024-T3**: High-strength sheet, facesheets
- **6061-T6**: Moderate strength, good formability, manifolds
- **6063-T5**: Extrusions, fins
- **5052-H32**: Excellent corrosion resistance, fluid components

### Thermal Interface Materials
- **Gap filler pads**: Various thermal conductivities (2-10 W/m·K)
- **Thermal greases**: High conductivity (>5 W/m·K)
- **Phase change materials**: Low contact resistance

### Core Materials
- **Aluminum honeycomb**: Various cell sizes (3/16", 1/4", 1/8")
- **Nomex honeycomb**: Lightweight, lower thermal conductivity

### Coatings
- **White paint**: High emissivity (ε ~0.90), low solar absorptivity
- **SSM (Secondary Surface Mirror)**: Very high emissivity (ε ~0.85)
- **Black paint**: High emissivity and absorptivity (for absorbers)

## Coordinate System Standards

### Spacecraft Coordinate System (STA-B Reference)
- **X-axis**: Longitudinal, positive forward (toward payload)
- **Y-axis**: Lateral, positive right (starboard when viewed from aft)
- **Z-axis**: Vertical, positive down (toward nadir in nominal attitude)

### Datum Reference Frames
- **Datum A**: Primary datum (typically largest/flattest mounting surface)
- **Datum B**: Secondary datum (perpendicular to A, defines rotation)
- **Datum C**: Tertiary datum (defines final orientation)

### Interface Mounting Per 51 Standards
- Align mounting hole patterns to 51 structural reference grid
- Document interface coordinate system in assembly drawings
- Maintain consistency with spacecraft master coordinate system

## Usage Guidelines

### Starting a New Part
1. Select appropriate part template from this directory
2. Save as new file with proper naming convention (21-10_PART_...)
3. Update part properties (part number, description, material)
4. Set material from material library
5. Modify template geometry as needed
6. Maintain coordinate system orientation (datum origin)
7. Apply PMI color coding (structure gray, fluid blue, TIM orange, coating pink)

### Starting a New Assembly
1. Select appropriate assembly template
2. Save as new file with proper naming (21-10_ASSY_...)
3. Insert or reference skeleton geometry
4. Add components using standard constraints
5. Maintain product structure conventions (matches EBOM)
6. Update assembly properties and mass properties
7. Verify interface alignments

### Creating a New Drawing
1. Select appropriate drawing template (A3 landscape most common)
2. Insert model views from 3D CAD model
3. Apply standard dimension styles
4. Add GD&T symbols and feature control frames
5. Complete title block information
6. Add applicable standard notes from note packs
7. Add revision table and initial revision (typically "A" or "01")
8. Export to PDF per standards for REL status

## Maintenance and Updates

### Template Updates
- Templates maintained by CAD administrator/design lead
- Request template updates when common needs arise
- Document template changes in revision notes
- Distribute updated templates to design team

### Best Practices
- **Always start from template** (don't copy from previous project files)
- **Don't modify master templates** (save as new file immediately)
- **Follow template structure and conventions** consistently
- **Update template properties before significant work** begins
- **Maintain template compatibility** with CAD system versions

## Related Directories

- **Assemblies**: [`../assemblies/`](../assemblies/) - Use assembly templates
- **Parts**: [`../parts/`](../parts/) - Use part templates
- **Drawings**: [`../drawings/`](../drawings/) - Use drawing templates
- **EBOM**: [`../../EBOM_LINKS.md`](../../EBOM_LINKS.md) - BOM structure reference

## Standards References

- **ISO 1101**: Geometrical Product Specifications (GPS) - Geometrical tolerancing
- **ISO 2768**: General tolerances for linear and angular dimensions
- **ASME Y14.5**: Dimensioning and tolerancing
- **ASME Y14.41**: Digital product definition data practices
- **ECSS-E-ST-32C**: Space engineering - Structural design and verification
- **ECSS-Q-ST-70-03C**: Surface cleanliness and contamination control

---

**Last Updated**: 2025-10-10
