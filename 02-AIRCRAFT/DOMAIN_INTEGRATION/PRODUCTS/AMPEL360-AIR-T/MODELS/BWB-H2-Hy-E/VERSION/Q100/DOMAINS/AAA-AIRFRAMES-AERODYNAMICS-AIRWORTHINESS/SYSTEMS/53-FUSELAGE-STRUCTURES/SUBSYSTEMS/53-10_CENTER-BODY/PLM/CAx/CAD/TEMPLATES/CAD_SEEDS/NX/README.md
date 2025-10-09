# NX — Siemens NX Seed Files and Templates

## Purpose

Siemens NX-specific seed files, configuration templates, and customer defaults for the 53-10 Center Body design work.

## Contents

### Seed Files
- **Part seed files** (`.prt`)
- **Assembly seed files** (`.prt` with assembly context)
- **Drawing seed files** (`.prt` with drafting sheets)
- **Template parts** (pre-configured features)

### Configuration Files
- **Customer defaults** (`.dpv`)
- **Role preferences** (XML configurations)
- **Symbol libraries** (`.sbf`)

## File Naming Convention

```
NX_<type>_<description>.prt
```

**Examples:**
- `NX_Part_Seed_Structural.prt`
- `NX_Assembly_Seed_Frame_Section.prt`
- `NX_Drawing_Seed_A3_Landscape.prt`
- `NX_Customer_Defaults.dpv`

## Seed File Contents

### Part Seed (.prt)
Pre-configured with:
- Datum coordinate system (CSYS) at origin
- Datum planes (XY, YZ, ZX)
- Expressions: `LENGTH`, `WIDTH`, `HEIGHT`, `THICKNESS`
- Layers organized (1-256)
- Part units: mm, deg, kg
- Material: Aluminum 2024-T3 (default)

### Assembly Seed (.prt)
Pre-configured with:
- Assembly context
- Work part and displayed part
- CSYS for assembly coordination
- Component arrangements
- Constraints/relationships
- Layers for components

### Drawing Seed (.prt)
Pre-configured with:
- Drawing sheets (A4, A3, A2, A1, A0)
- Title block (embedded or referenced)
- Border with zone markers
- View templates (front, top, right, isometric)
- Dimension styles (ISO or ASME)
- Note templates

## NX Settings

### Customer Defaults
**File → Utilities → Customer Defaults**

**Gateway:**
- Units: Millimeters
- Modeling tolerance: 0.001 mm
- Angle tolerance: 0.5 deg

**Assemblies:**
- Use Lightweight Mode: On
- Load options: As needed
- Reference set: Model

**Drafting:**
- Standard: ASME Y14.5M or ISO 1101
- Annotation type: Retained
- Dimension preferences: Associative

**User Interface:**
- Selection: Preselection highlight on
- Graphics: Shaded with edges
- View orientation: Trimetric

### Expression Management
Standard expressions in seed file:
```
LENGTH = 100 mm
WIDTH = 50 mm
HEIGHT = 30 mm
THICKNESS = 2 mm
FS_STATION = 1000 mm
BL_POSITION = 0 mm
WL_POSITION = 500 mm
```

### Layer Standards
- **1-10**: Primary geometry features
- **11-20**: Construction geometry
- **21-30**: Reference geometry (datums, planes)
- **41-50**: Dimensions (drawings)
- **51-60**: Annotations (drawings)
- **100-110**: Assembly components
- **200-256**: Temporary/working layers

## Material Library Setup

### Assigning Materials
**Tools → Materials → Assign**
- Material database: `NX_Materials.mtl`
- Standard materials: Al 2024-T3, Al 7075-T6, Ti-6Al-4V, Steel 300M, CFRP

### Material Properties
Verify properties:
- Density (kg/m³)
- Young's modulus (GPa)
- Poisson's ratio
- Yield strength (MPa)
- Ultimate strength (MPa)

## Installation

### Installing Seed Files
1. Copy seed files to: `C:\Program Files\Siemens\NX\TEMPLATES\`
2. Or user directory: `%UGII_BASE_DIR%\TEMPLATES\`

### Setting Customer Defaults
1. File → Utilities → Customer Defaults
2. Import `.dpv` file: `NX_Customer_Defaults.dpv`
3. Or set environment variable: `UGII_DEFAULTS_FILE`

### Template Directory
Set environment variable:
```
UGII_TEMPLATE_DIR = C:\NX_Templates\
```

## Usage Guidelines

### Creating New Part from Seed
1. **File → New** (uses seed file if configured)
2. Select template: Choose appropriate seed file
3. Immediately **Save As** with proper name
4. Update Part Properties (part number, description)
5. Verify expressions and material

### Modeling Best Practices
- Use modeling features (not just primitives)
- Name all significant features
- Use expressions for parametric control
- Organize features in feature tree
- Use layers for organization
- Apply PMI (Product Manufacturing Information) for GD&T

### Assembly Best Practices
- Use WAVE geometry linker for top-down design
- Define relationships between components
- Use component arrays for patterns
- Manage reference sets (Model, Empty, etc.)
- Use assembly constraints intelligently

## Troubleshooting

**Issue:** Seed file not found on File → New
- **Solution:** Check `UGII_TEMPLATE_DIR` environment variable

**Issue:** Customer defaults not applied
- **Solution:** Import `.dpv` file or check `UGII_DEFAULTS_FILE` variable

**Issue:** Expressions not defined
- **Solution:** Verify seed file has expressions, or create manually

**Issue:** Materials not available
- **Solution:** Check material library path, import `NX_Materials.mtl`

**Issue:** Drawing template not loading
- **Solution:** Verify drawing seed path in Customer Defaults → Drafting

## Teamcenter Integration

### Managed Mode
When using Teamcenter PLM:
- Templates stored in Teamcenter database
- Use "New from Template" in Teamcenter
- Part numbers assigned automatically
- Revision control managed by Teamcenter

### Native Mode
When not using Teamcenter:
- Templates stored in file system
- Manual part numbering
- File-based revision control

## Related Files

- Parent directory: [`../README.md`](../README.md)
- CATIA seeds: [`../CATIA/README.md`](../CATIA/README.md)
- SOLIDWORKS seeds: [`../SOLIDWORKS/README.md`](../SOLIDWORKS/README.md)
- Creo seeds: [`../CREO/README.md`](../CREO/README.md)

## References

- Siemens NX documentation
- NX customer defaults guide
- Company NX configuration standards
- Teamcenter integration guide (if applicable)
