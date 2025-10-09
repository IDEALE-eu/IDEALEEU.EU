# CATIA — CATIA V5/V6 Seed Files and Templates

## Purpose

CATIA-specific seed files, configuration templates, and startup settings for the 53-10 Center Body design work.

## Contents

### Seed Files
- **Part seed files** (`.CATPart`)
- **Assembly seed files** (`.CATProduct`)
- **Drawing seed files** (`.CATDrawing`)
- **Material libraries** (`.CATMaterial`)

### Configuration Files
- **Environment settings** (`.CATSettings`)
- **Standards files** (`.CATStandard`)
- **Analysis catalogs** (`.CATAnalysis`)

## File Naming Convention

```
CATIA_<type>_<description>.<ext>
```

**Examples:**
- `CATIA_Part_Seed_Structural.CATPart`
- `CATIA_Assembly_Seed_Frame_Section.CATProduct`
- `CATIA_Drawing_Seed_A3_Landscape.CATDrawing`
- `CATIA_Environment_53-10.CATSettings`

## Seed File Contents

### Part Seed (CATPart)
Pre-configured with:
- Origin and reference planes (xy plane, yz plane, zx plane)
- Parameters: `LENGTH`, `WIDTH`, `HEIGHT`, `THICKNESS`
- Material: Placeholder (Aluminum 2024-T3)
- Units: mm, deg, kg
- Geometrical sets organized
- Publication of key geometric elements

### Assembly Seed (CATProduct)
Pre-configured with:
- Master reference product (coordinate system)
- Reference geometry (FS, BL, WL planes)
- Skeleton part (optional)
- Standard constraints (coincidence, fix)
- Product structure
- Publication strategy

### Drawing Seed (CATDrawing)
Pre-configured with:
- Title block (A4, A3, A2, A1, A0 sizes)
- Border with zone markers
- Standard view layout (front, top, right)
- Dimension styles (ISO or ASME)
- Text styles and fonts
- Scale blocks

## CATIA Settings

### Environment Settings
**Tools → Options → General**
- Units: mm, deg, kg
- Language: English
- Precision: 0.001 mm
- Display: Shading with edges and hidden edges

**Tools → Options → Mechanical Design → Part Design**
- Keep link with selected object: On
- Hybrid design: On
- Parameters: Create parameters for constraints

**Tools → Options → Mechanical Design → Assembly Design**
- Clash detection: On during constraints
- Update: Automatic update
- Cache management: Activate cache

**Tools → Options → Mechanical Design → Drafting**
- Standard: ISO or ASME (per project)
- Dimension properties: Drive dimensions by parameters
- Sheet background: White

### Workbench Standards
- **Part Design**: ISO standard
- **Assembly Design**: Top-down approach with skeleton
- **Drafting**: ASME Y14.5 or ISO 1101
- **GSD (Generative Shape Design)**: For complex surfaces

## Material Library Setup

### Standard Materials
Located in: `CATIA_Material_Library.CATMaterial`

Materials included:
- Aluminum 2024-T3
- Aluminum 7075-T6
- Titanium Ti-6Al-4V
- Steel 300M
- CFRP (Carbon Fiber Reinforced Plastic)

### Material Assignment
1. Apply → Material from material library
2. Verify density and properties
3. Render material appearance if needed

## Installation

### Installing Seed Files
1. Copy seed files to: `C:\CATIA_V5\Templates\`
2. Or user directory: `%USERPROFILE%\AppData\Local\CATIA\Templates\`

### Setting Seed Path
**Tools → Options → General → File Tab**
- Set "Templates" path to seed file location
- Check "Use templates by default"

### Environment Setup
**Tools → Options → General → Parameters and Measure**
- Import environment file: `CATIA_Environment_53-10.CATSettings`
- Or manually configure units and precision

## Usage Guidelines

### Creating New Part from Seed
1. **File → New → Part** (will use seed file if configured)
2. Or **File → New From…** → Select seed file
3. Immediately **Save As** with proper name
4. Update properties (part number, description)
5. Verify material and parameters

### Best Practices
- Never modify seed files directly
- Use Publications for key geometry
- Organize feature tree (use Geometrical Sets)
- Name all significant features
- Apply materials early
- Use Parameters for dimensional control

## Troubleshooting

**Issue:** Seed file not used on File → New
- **Solution:** Check Tools → Options → General → File → Templates path

**Issue:** Material library not accessible
- **Solution:** Copy .CATMaterial file to correct location, or set material library path

**Issue:** Environment settings not applied
- **Solution:** Import .CATSettings file, or manually configure Tools → Options

## Related Files

- Parent directory: [`../README.md`](../README.md)
- NX seeds: [`../NX/README.md`](../NX/README.md)
- SOLIDWORKS seeds: [`../SOLIDWORKS/README.md`](../SOLIDWORKS/README.md)
- Creo seeds: [`../CREO/README.md`](../CREO/README.md)

## References

- CATIA V5 documentation (Dassault Systèmes)
- CATIA standards and administration guide
- Company CATIA configuration management
