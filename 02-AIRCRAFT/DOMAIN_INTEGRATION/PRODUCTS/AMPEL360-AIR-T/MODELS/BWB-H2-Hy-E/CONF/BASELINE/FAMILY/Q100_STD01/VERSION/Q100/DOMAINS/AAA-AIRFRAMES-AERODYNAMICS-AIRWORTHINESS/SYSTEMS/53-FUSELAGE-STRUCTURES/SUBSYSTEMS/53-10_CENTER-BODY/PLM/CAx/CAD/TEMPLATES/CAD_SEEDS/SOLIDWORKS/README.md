# SOLIDWORKS — SOLIDWORKS Templates and Settings

## Purpose

SOLIDWORKS-specific templates, document templates, and system settings for the 53-10 Center Body design work.

## Contents

### Template Files
- **Part templates** (`.prtdot`)
- **Assembly templates** (`.asmdot`)
- **Drawing templates** (`.drwdot`)
- **Weldment profiles** (`.sldlfp`)

### Configuration Files
- **System options** (`.sldsettings`)
- **Document properties** (embedded in templates)
- **Custom property templates** (`.sldprpprp`)
- **Material databases** (`.sldmat`)

## File Naming Convention

```
SW_<type>_<description>.<ext>
```

**Examples:**
- `SW_Part_Template_Structural.prtdot`
- `SW_Assembly_Template_Frame_Section.asmdot`
- `SW_Drawing_Template_A3_Landscape.drwdot`
- `SW_System_Options.sldsettings`

## Template File Contents

### Part Template (.prtdot)
Pre-configured with:
- Origin and default planes (Front, Top, Right)
- Units: MMGS (millimeter, gram, second)
- Precision: 0.001 mm
- Design table placeholder
- Custom properties (Part Number, Description, Material, etc.)
- Configuration: Default configuration
- Material: Aluminum 2024-T3 (default)

### Assembly Template (.asmdot)
Pre-configured with:
- Origin and reference planes
- Units: MMGS
- Component patterns and configurations
- Custom properties (Assembly Number, Description, etc.)
- BOM template
- Display states (Detailed, Simplified)
- Mate references

### Drawing Template (.drwdot)
Pre-configured with:
- Sheet format (A4, A3, A2, A1, A0)
- Title block with custom properties
- Border with zone markers
- Standard 3 views (Front, Top, Right, Isometric)
- Dimension style (ISO or ANSI)
- Layer organization
- BOM table format

## SOLIDWORKS Settings

### System Options
**Tools → Options → System Options**

**General:**
- Input dimension value: On creation
- Units: Millimeters

**Drawings:**
- Display style: Shaded with edges
- Line font: ISO or ANSI
- Arrow style: Solid

**Performance:**
- Verification on rebuild: Off (for speed)
- Automatically save every: 10 minutes

**File Locations:**
- Document Templates: `C:\ProgramData\SOLIDWORKS\Templates\`
- Custom properties files: `C:\ProgramData\SOLIDWORKS\Templates\CustomProperties\`
- Material databases: `C:\ProgramData\SOLIDWORKS\Materials\`

### Document Properties
**Options → Document Properties** (embedded in each template)

**Detailing:**
- Dimensioning standard: ISO or ANSI
- Dual dimensions: Off (or On if needed)
- Precision: 0.01 mm

**Units:**
- Unit system: MMGS
- Length: Millimeters, 3 decimals
- Angle: Degrees, 1 decimal
- Mass: Kilograms, 3 decimals

**Model Display:**
- Display style: Shaded with edges
- Hidden edges: Visible (gray)
- Tangent edges: Visible

**DimXpert:**
- Dimensioning scheme: ASME Y14.41 or ISO 16792
- Tolerance type: Per standard

## Custom Properties

### Part Properties Template
Custom properties tab builder (`.sldprpprp`):
```
Part Number:         [TEXT - REQUIRED]
Description:         [TEXT - REQUIRED]
Revision:            [TEXT - DEFAULT: A]
Material:            [AUTO - FROM MATERIAL]
Mass:                [AUTO - FROM MODEL]
Drawn By:            [TEXT]
Drawn Date:          [DATE]
Checked By:          [TEXT]
Approved By:         [TEXT]
Status:              [DROPDOWN: In-Work, For-Review, Released]
```

### Assembly Properties Template
```
Assembly Number:     [TEXT - REQUIRED]
Description:         [TEXT - REQUIRED]
Revision:            [TEXT - DEFAULT: A]
Total Mass:          [AUTO - FROM MODEL]
Component Count:     [AUTO - FROM MODEL]
Assembly Level:      [DROPDOWN: Top-Level, Sub-Assembly, Detail]
Drawn By:            [TEXT]
Status:              [DROPDOWN: In-Work, For-Review, Released]
```

## Material Library Setup

### Standard Materials
Material database: `SW_Materials_53-10.sldmat`

Materials included:
- Aluminum 2024-T3 (density: 2.78 g/cm³)
- Aluminum 7075-T6 (density: 2.81 g/cm³)
- Titanium Ti-6Al-4V (density: 4.43 g/cm³)
- Steel 300M (density: 7.85 g/cm³)
- Carbon Fiber Composite (density: 1.58 g/cm³)

### Applying Materials
1. Right-click Material in Feature Manager
2. Edit Material
3. Select from custom material library
4. Verify density and properties

## Installation

### Installing Templates
1. Copy templates to: `C:\ProgramData\SOLIDWORKS\Templates\`
2. Or user folder: `%USERPROFILE%\Documents\SOLIDWORKS\Templates\`

### Setting Default Templates
**Tools → Options → System Options → File Locations**
1. Show folders for: Document Templates
2. Add template directory path
3. Move to top of list (highest priority)

**Tools → Options → System Options → Default Templates**
- Part template: `SW_Part_Template_Structural.prtdot`
- Assembly template: `SW_Assembly_Template_Frame_Section.asmdot`
- Drawing template: Prompt user to select

### Importing System Options
1. Copy `SW_System_Options.sldsettings` to local directory
2. **Tools → Options → System Options**
3. Load/Save Settings button → Load settings
4. Select `.sldsettings` file

## Usage Guidelines

### Creating New Part from Template
1. **File → New** (or Ctrl+N)
2. Select appropriate part template
3. Immediately **File → Save As** with proper name
4. **File → Properties → Custom** → Fill in custom properties
5. Apply material if not default
6. Begin modeling

### Best Practices
- Use Design Tables for family of parts
- Apply dimensions to sketches (fully define)
- Name features descriptively
- Use configurations for variants (LEFT, RIGHT, etc.)
- Roll back feature tree to suppress features cleanly
- Apply materials early for accurate mass properties
- Use Sensors to monitor critical dimensions or mass

### Assembly Best Practices
- Use in-context references sparingly (can cause external references)
- Use Component Patterns for repetitive components
- Create assembly-level BOMs early
- Use Display States to simplify large assemblies
- Apply mates intelligently (fix one part, float others)
- Use SpeedPak for large sub-assemblies

## Troubleshooting

**Issue:** Template not available in File → New
- **Solution:** Check File Locations settings, ensure template path is listed

**Issue:** Custom properties not populating
- **Solution:** Check custom property tab builder file (`.sldprpprp`) is in correct location

**Issue:** Material library not accessible
- **Solution:** Copy `.sldmat` file to SOLIDWORKS\Materials\ folder, or add custom location

**Issue:** System options reset after restart
- **Solution:** Save system options to `.sldsettings` file, reload after install/update

**Issue:** Drawing template title block not editable
- **Solution:** Edit Sheet Format (right-click sheet → Edit Sheet Format) to modify

## PDM Integration

### SOLIDWORKS PDM Professional
When using PDM:
- Templates stored in vault
- Check out template to modify
- Use data cards for properties
- Automatic part numbering via PDM
- Revision control managed by PDM

## Related Files

- Parent directory: [`../README.md`](../README.md)
- CATIA seeds: [`../CATIA/README.md`](../CATIA/README.md)
- NX seeds: [`../NX/README.md`](../NX/README.md)
- Creo seeds: [`../CREO/README.md`](../CREO/README.md)

## References

- SOLIDWORKS Help documentation
- SOLIDWORKS Administration Guide
- Company SOLIDWORKS standards
- SOLIDWORKS PDM documentation (if applicable)
