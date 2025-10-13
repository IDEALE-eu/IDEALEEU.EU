# TEMPLATES — Reference Plane Templates and Standard Files

## Purpose

This directory contains template files and standard reference plane definitions that can be reused across the 53-10 Center Body design, ensuring consistency and reducing modeling effort.

## Contents

### Template Types

#### 1. Global Coordinate Plane Templates
Pre-configured global reference planes ready for use:
- **XY Plane Template**: Horizontal reference plane
- **XZ Plane Template**: Vertical longitudinal plane (symmetry)
- **YZ Plane Template**: Vertical transverse plane (stations)

#### 2. Station Plane Templates
Standard station plane templates with proper orientation:
- **FS Template**: Fuselage station plane template
- **WL Template**: Waterline plane template
- **BL Template**: Buttock line plane template

#### 3. Local Component Templates
Templates for component-specific reference planes:
- **Frame Reference Template**: For frame local planes
- **Stringer Reference Template**: For stringer local planes
- **Panel Reference Template**: For panel local planes
- **Door Reference Template**: For door local planes

#### 4. Interface Plane Templates
Templates for structural interface definitions:
- **Splice Interface Template**: For fuselage splices
- **Attachment Interface Template**: For component attachments
- **Systems Interface Template**: For systems pass-through

#### 5. Offset Plane Templates
Templates for creating offset surfaces:
- **Positive Offset Template**: For +offset planes
- **Negative Offset Template**: For -offset planes
- **Variable Offset Template**: For non-uniform offsets

## Template Usage

### How to Use Templates

1. **Copy Template File**
   - Copy appropriate template to working directory
   - Rename following naming convention
   - Update version to v01

2. **Position Plane**
   - Open template in CAD system
   - Position plane at required location
   - Set orientation and normal direction
   - Verify against reference coordinates

3. **Update Metadata**
   - Fill in part number/file name
   - Add description
   - Document coordinate system reference
   - Record creation date and author

4. **Validate**
   - Run geometric validation checks
   - Verify naming convention compliance
   - Check metadata completeness
   - Generate validation report

5. **Save and Release**
   - Save with proper file name
   - Check into PLM system
   - Link to related documents
   - Request review and approval

## Template File List

### Global Plane Templates

```
53-10_TEMPLATE_GLOBAL_PLANE_XY.CATPart
53-10_TEMPLATE_GLOBAL_PLANE_XZ.CATPart
53-10_TEMPLATE_GLOBAL_PLANE_YZ.CATPart
```

**Properties**:
- Origin at (0, 0, 0)
- Standard orientation per axis
- Unit normal vectors
- Infinite extent

### Station Plane Templates

```
53-10_TEMPLATE_STATION_FS.CATPart
53-10_TEMPLATE_STATION_WL.CATPart
53-10_TEMPLATE_STATION_BL.CATPart
```

**Properties**:
- Positioned at origin, ready for translation
- Proper orientation for each type
- Standard extent (can be adjusted)
- Linked to global coordinate system

### Local Component Templates

```
53-10_TEMPLATE_LOCAL_FRAME.CATPart
53-10_TEMPLATE_LOCAL_STRINGER.CATPart
53-10_TEMPLATE_LOCAL_PANEL.CATPart
53-10_TEMPLATE_LOCAL_DOOR.CATPart
```

**Properties**:
- Local coordinate system pre-defined
- Common plane orientations included
- Relationship parameters ready for input
- Metadata fields pre-populated

### Interface Templates

```
53-10_TEMPLATE_INTERFACE_SPLICE.CATPart
53-10_TEMPLATE_INTERFACE_ATTACH.CATPart
53-10_TEMPLATE_INTERFACE_SYSTEMS.CATPart
```

**Properties**:
- Interface zone definition
- Mating surface references
- Fastener pattern placeholders
- Systems penetration markers

### Offset Templates

```
53-10_TEMPLATE_OFFSET_PLUS_5.CATPart
53-10_TEMPLATE_OFFSET_MINUS_5.CATPart
53-10_TEMPLATE_OFFSET_CUSTOM.CATPart
```

**Properties**:
- Offset distance parameter
- Reference surface link
- Normal direction definition
- Tolerance zone markers

## Template Configuration

### Standard Template Settings

All templates should be configured with:

**Units**:
- Length: millimeters (mm)
- Angle: degrees (°)
- Mass: kilograms (kg)

**Precision**:
- Coordinates: 3 decimal places (0.001 mm)
- Angles: 2 decimal places (0.01°)
- Display: 2 decimal places for dimensions

**Layers/Levels**:
- Reference geometry on dedicated layer
- Construction geometry separate
- Annotation layer for labels
- Metadata on non-plotting layer

**Properties**:
- Material: N/A (reference geometry)
- Mass: 0 kg
- Color: By standard (typically cyan or yellow)
- Line type: Dashed or construction

**Parameters**:
- Parametric where beneficial
- Named parameters for key dimensions
- Formulas for derived values
- Links to external references

## Template Customization

### Creating Custom Templates

For project-specific requirements:

1. **Start with Standard Template**
   - Copy closest matching standard template
   - Preserve standard structure

2. **Add Custom Features**
   - Add project-specific parameters
   - Include custom metadata fields
   - Add specialized reference features

3. **Document Customization**
   - Describe modifications made
   - Explain reason for customization
   - Note any standard deviations

4. **Validate Custom Template**
   - Test with representative use cases
   - Verify compatibility with workflow
   - Check PLM system integration

5. **Distribute to Team**
   - Store in shared template library
   - Communicate availability
   - Provide usage instructions
   - Train users if needed

## Template Maintenance

### Version Control

- **Template Version**: Independent from usage versions
- **Format**: `TEMPLATE_vXX`
- **Update Policy**: Only when standards change or errors found
- **Communication**: Notify all users of template updates

### Quality Assurance

- **Regular Review**: Annual review of all templates
- **Validation**: Test templates with each CAD system upgrade
- **Feedback**: Collect user feedback on template usability
- **Improvement**: Enhance based on lessons learned

### Documentation

Each template should have accompanying documentation:
- Purpose and intended use
- Setup and configuration instructions
- Customization guidelines
- Example usage
- Troubleshooting tips

## Template Library Organization

```
TEMPLATES/
├── GLOBAL/
│   ├── 53-10_TEMPLATE_GLOBAL_PLANE_XY.CATPart
│   ├── 53-10_TEMPLATE_GLOBAL_PLANE_XZ.CATPart
│   ├── 53-10_TEMPLATE_GLOBAL_PLANE_YZ.CATPart
│   └── GLOBAL_TEMPLATES_README.md
├── STATIONS/
│   ├── 53-10_TEMPLATE_STATION_FS.CATPart
│   ├── 53-10_TEMPLATE_STATION_WL.CATPart
│   ├── 53-10_TEMPLATE_STATION_BL.CATPart
│   └── STATION_TEMPLATES_README.md
├── LOCAL/
│   ├── 53-10_TEMPLATE_LOCAL_FRAME.CATPart
│   ├── 53-10_TEMPLATE_LOCAL_STRINGER.CATPart
│   ├── 53-10_TEMPLATE_LOCAL_PANEL.CATPart
│   ├── 53-10_TEMPLATE_LOCAL_DOOR.CATPart
│   └── LOCAL_TEMPLATES_README.md
├── INTERFACES/
│   ├── 53-10_TEMPLATE_INTERFACE_SPLICE.CATPart
│   ├── 53-10_TEMPLATE_INTERFACE_ATTACH.CATPart
│   ├── 53-10_TEMPLATE_INTERFACE_SYSTEMS.CATPart
│   └── INTERFACE_TEMPLATES_README.md
├── OFFSETS/
│   ├── 53-10_TEMPLATE_OFFSET_PLUS_5.CATPart
│   ├── 53-10_TEMPLATE_OFFSET_MINUS_5.CATPart
│   ├── 53-10_TEMPLATE_OFFSET_CUSTOM.CATPart
│   └── OFFSET_TEMPLATES_README.md
└── USAGE_GUIDE.md
```

## Benefits of Using Templates

### Consistency
- All planes follow same standard
- Reduces variation between designers
- Ensures compliance with requirements

### Efficiency
- Faster plane creation
- Less setup time
- Reduced errors

### Quality
- Pre-validated geometry
- Standard metadata structure
- Known good configuration

### Maintainability
- Easier to update standards (update templates)
- Centralized control
- Version management simplified

## CAD System Compatibility

Templates available for:
- **CATIA V5**: `.CATPart` format
- **NX/Unigraphics**: `.prt` format
- **SolidWorks**: `.sldprt` format
- **Creo/Pro-E**: `.prt` format

Note: Ensure template format matches your CAD system version

## Support and Training

### Resources Available

- **Template Library**: Access point for all standard templates
- **Usage Guide**: Step-by-step instructions (this document)
- **Video Tutorials**: Demonstration of template usage
- **Support Contact**: CAD support team for questions

### Training

- **New User Orientation**: Introduction to template library
- **Advanced Topics**: Customizing templates for specific needs
- **Best Practices**: Efficient workflow with templates
- **Troubleshooting**: Common issues and solutions

## Standards Compliance

Follow:
- **ATA iSpec 2200**: Reference plane conventions
- **ISO 10303 (STEP)**: Product data representation
- **Company CAD standards**: Template formatting and organization
- **PLM integration standards**: Metadata and properties

## Related Directories

- **All plane directories**: [`../`](../) (parent PLANES directory)
- **Metadata standards**: [`../METADATA/`](../METADATA/)
- **Validation tools**: [`../VALIDATION/`](../VALIDATION/)
- **General CAD templates**: [`../../../../TEMPLATES/`](../../../../TEMPLATES/)
