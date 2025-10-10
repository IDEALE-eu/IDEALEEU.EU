# CAD_SEEDS — CAD System Seed Files and Startup Templates

## Purpose

CAD system-specific seed files, startup files, and configuration templates for consistent setup across different CAD platforms.

## Directory Structure

```
CAD_SEEDS/
├── CATIA/           # CATIA V5/V6 seed files and configurations
├── NX/              # Siemens NX seed files and templates
├── SOLIDWORKS/      # SOLIDWORKS templates and settings
├── CREO/            # PTC Creo start models and configs
└── README.md        # This file
```

## What are Seed Files?

**Seed files** (also called start models or startup files) are pre-configured template files that contain:
- Standard coordinate systems and datums
- Pre-defined parameters and variables
- Layer/level organizational structure
- Material libraries
- Standard colors and display settings
- Units and precision settings
- Modeling preferences

**Benefits:**
- Ensures consistency across all designers
- Reduces setup time for new parts/assemblies
- Embeds company standards automatically
- Minimizes errors from incorrect setup
- Facilitates data exchange between systems

## Seed File Types

### Part Seed Files
Pre-configured part files with:
- Origin and reference planes (XY, YZ, XZ)
- Standard parameters (LENGTH, WIDTH, HEIGHT, etc.)
- Material assignment placeholder
- Layer structure
- Units (mm) and precision (0.001 mm)

### Assembly Seed Files
Pre-configured assembly files with:
- Master coordinate system
- Reference geometry (FS, BL, WL stations)
- Skeleton structure (optional)
- Standard constraints/mates
- Level of detail configurations
- BOM structure template

### Drawing Seed Files
Pre-configured drawing files with:
- Title block
- Border with zone markers
- Standard sheet sizes (A4, A3, A1, etc.)
- Dimension styles
- Layer standards
- Scale blocks

## CAD System Seed Locations

### CATIA V5
**Seed file location:** `CAD_SEEDS/CATIA/`
- Part seed: `CATIA_Part_Seed_53-10.CATPart`
- Assembly seed: `CATIA_Assembly_Seed_53-10.CATProduct`
- Drawing seed: `CATIA_Drawing_Seed_A3.CATDrawing`
- Environment file: `CATIA_Environment_53-10.CATSettings`

### Siemens NX
**Seed file location:** `CAD_SEEDS/NX/`
- Part seed: `NX_Part_Seed_53-10.prt`
- Assembly seed: `NX_Assembly_Seed_53-10.prt`
- Drawing seed: `NX_Drawing_Seed_A3.prt`
- Customer defaults: `nx_customer_defaults.dpv`

### SOLIDWORKS
**Seed file location:** `CAD_SEEDS/SOLIDWORKS/`
- Part template: `SW_Part_Template_53-10.prtdot`
- Assembly template: `SW_Assembly_Template_53-10.asmdot`
- Drawing template: `SW_Drawing_Template_A3.drwdot`
- System options: `SW_System_Options.sldsettings`

### PTC Creo
**Seed file location:** `CAD_SEEDS/CREO/`
- Part start model: `Creo_Start_Part_53-10.prt`
- Assembly start model: `Creo_Start_Assembly_53-10.asm`
- Drawing template: `Creo_Drawing_Template_A3.drw`
- Config file: `config.pro`

## Configuration Standards

### Units and Precision
- **Units**: Millimeters (mm)
- **Angular units**: Degrees (deg)
- **Precision**: 0.001 mm for dimensions
- **Mass units**: Kilograms (kg)
- **Time units**: Seconds (s)

### Coordinate System
- **X-axis (FS)**: Fuselage Station, positive aft
- **Y-axis (BL)**: Buttline, positive right (starboard)
- **Z-axis (WL)**: Waterline, positive up
- **Origin**: Aircraft reference point (per project definition)

### Layer/Level Standards
Common layer naming across CAD systems:
- **Layer 1**: Primary geometry
- **Layer 2**: Reference geometry (datums, planes)
- **Layer 3**: Construction geometry
- **Layer 10**: Dimensions (drawings)
- **Layer 11**: Annotations (drawings)
- **Layer 20**: Hidden/auxiliary

### Color Standards
- **Blue**: Primary solid geometry
- **Green**: Surfaces
- **Yellow**: Construction/reference geometry
- **Red**: Critical features or highlights
- **Gray**: Standard hardware/catalog parts

## Installation and Setup

### Installing Seed Files

**CATIA V5:**
1. Copy seed files to: `C:\CATIA_Templates\`
2. Set environment variable: `CATStartupPath`
3. Configure Tools → Options → General → File

**Siemens NX:**
1. Copy seed files to: `C:\NX_Templates\`
2. Set customer defaults: `UGII_TEMPLATE_DIR`
3. Configure Preferences → User Interface → Startup

**SOLIDWORKS:**
1. Copy templates to: `C:\ProgramData\SOLIDWORKS\Templates\`
2. Configure Tools → Options → File Locations → Document Templates
3. Set as default templates

**PTC Creo:**
1. Copy start models to: `C:\Creo_Templates\`
2. Set config.pro: `template_designasm`, `template_solidpart`
3. Set `start_model_dir` in config.pro

## Seed File Maintenance

### Version Control
- Seed files are configuration-controlled
- Changes require engineering approval
- Version seed files with release dates
- Archive superseded seed files
- Document changes in revision log

### Update Process
1. Identify need for seed file change
2. Document change request (ECR)
3. Engineering review and approval
4. Update seed files
5. Notify all users of change
6. Provide training if significant changes
7. Archive previous version

### Testing
Before deploying updated seed files:
- Create test parts/assemblies
- Verify all settings are correct
- Check parameter definitions
- Test export to neutral formats
- Validate with multiple users

## Usage Guidelines

### Starting a New Part
1. Use appropriate seed file for CAD system
2. Save As with proper naming convention immediately
3. Update properties (part number, description)
4. Verify material assignment
5. Maintain coordinate system orientation
6. Follow modeling best practices

### Do NOT Modify Seed Files Directly
- Never edit master seed files
- Always "Save As" with new name immediately
- Request seed file updates through proper channels
- Use version-controlled seed files only

## Related Directories

- **Part Templates**: [`../PART/`](../PART/)
- **Assembly Templates**: [`../ASSEMBLY/`](../ASSEMBLY/)
- **Drawing Templates**: [`../DRAWING/`](../DRAWING/)
- **CATIA Seeds**: [`./CATIA/`](./CATIA/)
- **NX Seeds**: [`./NX/`](./NX/)
- **SOLIDWORKS Seeds**: [`./SOLIDWORKS/`](./SOLIDWORKS/)
- **Creo Seeds**: [`./CREO/`](./CREO/)

## References

- Main templates documentation: [`../README.md`](../README.md)
- CAD standards: [`../../README.md`](../../README.md)
- Configuration management: [`/00-PROGRAM/CONFIG_MGMT/`](/00-PROGRAM/CONFIG_MGMT/)
- CAD system administration guides
