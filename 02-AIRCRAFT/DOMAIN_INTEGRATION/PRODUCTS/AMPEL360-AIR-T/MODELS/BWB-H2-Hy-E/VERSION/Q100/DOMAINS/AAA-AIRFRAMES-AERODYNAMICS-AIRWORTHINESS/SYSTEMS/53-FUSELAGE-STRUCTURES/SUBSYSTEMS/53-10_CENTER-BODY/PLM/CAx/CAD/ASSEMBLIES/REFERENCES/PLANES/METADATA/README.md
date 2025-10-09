# METADATA — Reference Plane Metadata and Standards

## Purpose

This directory contains metadata, naming conventions, unit standards, and documentation guidelines for reference planes used in the 53-10 Center Body design.

## Contents

### CONVENTIONS/ — Naming and Organizational Conventions
- **Description**: Standards for naming, numbering, and organizing reference planes
- **Documents**:
  - Naming convention rules
  - File organization guidelines
  - Version control procedures
  - Change documentation standards
- **Applications**:
  - Consistent plane identification across teams
  - Automated file management
  - CAD system integration
  - PLM system compatibility

### UNITS/ — Unit Standards and Conversion
- **Description**: Unit system definitions, conversion factors, and precision requirements
- **Documents**:
  - Primary unit system (metric/imperial)
  - Conversion tables and factors
  - Precision and rounding rules
  - Display format standards
- **Applications**:
  - Ensure dimensional consistency
  - Support multi-system requirements
  - Validation and checking
  - Documentation standards

## Naming Conventions

### Standard Format

General pattern for all reference plane files:
```
<subsystem>_<category>_<type>_<identifier>_<version>.<extension>
```

Components:
- **subsystem**: `53-10` (ATA chapter and subsystem)
- **category**: Type of reference (e.g., STATION, GLOBAL, LOCAL, INTERFACE)
- **type**: Specific plane type (e.g., FS, WL, BL, XY, XZ, YZ)
- **identifier**: Location or unique ID (e.g., FS-1200, BL-0, FRAME_F05)
- **version**: Version number (e.g., v01, v02)
- **extension**: CAD system file type (e.g., CATPart, prt, sldprt)

### Examples by Category

**Global Planes**:
- `53-10_GLOBAL_PLANE_XY_v01.CATPart`
- `53-10_GLOBAL_PLANE_XZ_SYMMETRY_v01.prt`
- `53-10_GLOBAL_PLANE_YZ_STATION_v01.sldprt`

**Station Planes**:
- `53-10_STATION_FS-1000_v01.CATPart`
- `53-10_STATION_WL-1500_v02.prt`
- `53-10_STATION_BL-0_CENTERLINE_v01.sldprt`

**Local Planes**:
- `53-10_LOCAL_FRAME_F05_WEB_v01.CATPart`
- `53-10_LOCAL_STRINGER_L03_CAP_v01.prt`
- `53-10_LOCAL_PANEL_P01_OML_v01.sldprt`

**Interface Planes**:
- `53-10_INTERFACE_53_TO_57_WING_ROOT_v01.CATPart`
- `53-10_INTERFACE_53_TO_20_NOSE_SPLICE_v01.prt`

**Offset Planes**:
- `53-10_OFFSET_OML_PLUS_5_v01.CATPart`
- `53-10_OFFSET_IML_MINUS_5_v01.prt`

**Datum Features**:
- `53-10_DATUM_A_PRIMARY_v01.CATPart`
- `53-10_LOCATOR_DIAMOND_01_FWD_v01.prt`

### Version Control

- **Format**: `vXX` where XX is zero-padded integer (v01, v02, ..., v99)
- **Increment Rules**:
  - Minor changes (cosmetic, non-geometric): Same version
  - Geometric changes (affect downstream): Increment version
  - New configuration: New file with incremented version
- **Legacy Versions**: Retain previous versions for traceability
- **Latest Version**: Clearly marked in PLM system

## Unit Systems

### Primary Unit System

**Metric (SI) Units** - Primary for all designs:
- **Length**: millimeters (mm)
- **Mass**: kilograms (kg)
- **Force**: newtons (N)
- **Pressure**: pascals (Pa) or megapascals (MPa)
- **Temperature**: degrees Celsius (°C) or kelvin (K)

**Angular Measurements**:
- **Rotation**: degrees (°)
- **Slope**: percentage (%) or ratio

### Secondary Unit System

**Imperial Units** - For reference and legacy compatibility:
- **Length**: inches (in)
- **Mass**: pounds-mass (lbm)
- **Force**: pounds-force (lbf)
- **Pressure**: pounds per square inch (psi)
- **Temperature**: degrees Fahrenheit (°F)

### Conversion Factors

**Length**:
- 1 inch = 25.4 mm (exact)
- 1 foot = 304.8 mm (exact)
- 1 mm = 0.0393701 inch

**Mass**:
- 1 lbm = 0.453592 kg
- 1 kg = 2.20462 lbm

**Force**:
- 1 lbf = 4.44822 N
- 1 N = 0.224809 lbf

**Pressure**:
- 1 psi = 6894.76 Pa
- 1 MPa = 145.038 psi

### Precision Requirements

| Dimension Type | Metric Precision | Imperial Precision |
|----------------|------------------|-------------------|
| Station locations | 0.1 mm | 0.005 in |
| Component dimensions | 0.01 mm | 0.001 in |
| Hole positions | 0.01 mm | 0.0005 in |
| Surface profiles | 0.001 mm | 0.0001 in |
| Angles | 0.01° | 0.01° |

### Display Format Standards

**CAD Model Settings**:
- Units: Millimeters
- Decimal places: 2 for dimensions, 3 for coordinates
- Angle format: Decimal degrees, 2 decimal places
- Mass properties: kg and mm units

**Drawing Settings**:
- Primary dimension units: Millimeters
- Tolerance notation: Plus/minus or GD&T
- Decimal places: Per company drawing standards
- Dual dimensioning: Optional, imperial in brackets

## Metadata Fields

### Required Metadata for Each Plane

All reference plane files should include:

1. **Identification**
   - Part number or file name
   - Description
   - Version number
   - Creation date
   - Last modified date

2. **Geometric Definition**
   - Plane type (XY, XZ, YZ, FS, WL, BL, etc.)
   - Origin point coordinates (X, Y, Z)
   - Normal vector (i, j, k)
   - Extent or boundaries (if limited)

3. **Coordinate System**
   - Reference coordinate system (global, local)
   - Coordinate system origin
   - Axis orientation definitions

4. **Relationships**
   - Parent planes or features
   - Child or derived planes
   - Related assemblies or components

5. **Standards and Compliance**
   - Applicable ATA chapter
   - Design standard references
   - Tolerance specifications
   - Quality requirements

6. **Change History**
   - Version history
   - Change descriptions
   - Approval records
   - Effectivity dates

### Metadata Storage

**In CAD Files** (Properties/Parameters):
- Part number
- Description
- Version
- Author
- Date created/modified
- Material (N/A for reference planes)
- Mass (zero for reference geometry)

**In PLM System**:
- Complete metadata set
- Relationships and where-used
- Approval workflows
- Configuration management
- Effectivity and applicability

**In Documentation Files**:
- Detailed plane definitions
- Usage guidelines
- Design rationale
- Interface requirements

## Documentation Standards

### Reference Plane Definition Document

Each critical reference plane should have a definition document containing:

1. **Overview**
   - Purpose and function
   - Applicable structures
   - Design constraints

2. **Geometric Definition**
   - Mathematical plane equation
   - Coordinate system reference
   - Key points and boundaries

3. **Tolerances**
   - Position tolerance
   - Orientation tolerance
   - Form requirements

4. **Usage Instructions**
   - Design applications
   - Manufacturing setup
   - Inspection procedures

5. **Related Documents**
   - Interface control drawings
   - Assembly procedures
   - Quality specifications

### File Organization

```
METADATA/
├── CONVENTIONS/
│   ├── NAMING_STANDARDS.md
│   ├── VERSION_CONTROL.md
│   ├── FILE_ORGANIZATION.md
│   └── PLM_INTEGRATION.md
└── UNITS/
    ├── UNIT_SYSTEMS.md
    ├── CONVERSION_TABLES.md
    ├── PRECISION_REQUIREMENTS.md
    └── DISPLAY_FORMATS.md
```

## Standards Compliance

Follow:
- **ATA iSpec 2200**: Data naming and organization
- **ISO 10303 (STEP)**: Product data representation
- **ISO 16792**: Digital product definition
- **ASME Y14.41**: Digital product definition practices
- **Company PLM standards**: Internal data management procedures

## Related Directories

- **All plane directories**: [`../`](../) (parent PLANES directory)
- **Templates**: [`../TEMPLATES/`](../TEMPLATES/)
- **Validation**: [`../VALIDATION/`](../VALIDATION/)
- **CAD standards**: [`../../../../TEMPLATES/`](../../../../TEMPLATES/)
