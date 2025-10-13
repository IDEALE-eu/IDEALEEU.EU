# CREO — PTC Creo Start Models and Configuration

## Purpose

PTC Creo-specific start models, configuration files, and template settings for the 53-10 Center Body design work.

## Contents

### Start Models
- **Part start models** (`.prt`)
- **Assembly start models** (`.asm`)
- **Drawing templates** (`.drw`)
- **Format files** (`.frm`) for drawing sheets

### Configuration Files
- **Config.pro** (system configuration)
- **Config.sup** (site/user configuration)
- **DTL files** (`.dtl`) for drawing settings
- **Material libraries** (`.mtl`)

## File Naming Convention

```
Creo_<type>_<description>.<ext>
```

**Examples:**
- `Creo_Start_Part_Structural.prt`
- `Creo_Start_Assembly_Frame_Section.asm`
- `Creo_Drawing_Template_A3.drw`
- `Creo_Format_A3_Landscape.frm`
- `config.pro`

## Start Model Contents

### Part Start Model (.prt)
Pre-configured with:
- Datum coordinate system (PRT_CSYS_DEF)
- Datum planes (FRONT, TOP, RIGHT)
- Parameters: `LENGTH`, `WIDTH`, `HEIGHT`, `THICKNESS`
- Units: Millimeter Newton Second (mmNs)
- Material: ALUMINUM_2024_T3 (default)
- Model properties pre-defined

### Assembly Start Model (.asm)
Pre-configured with:
- Master coordinate system (ASM_DEF_CSYS)
- Default datums (ASM_FRONT, ASM_TOP, ASM_RIGHT)
- Skeleton model reference (optional)
- Default constraints (CSYS alignment)
- Assembly parameters
- Product structure

### Drawing Template (.drw)
Pre-configured with:
- Format file reference (title block)
- Drawing views layout
- Drawing parameters
- Detail options (ISO or ASME)
- Dimension style and tolerance format
- Note templates

## Creo Configuration (config.pro)

### Essential Settings
```
! Units and Precision
pro_unit_length             unit_mm
pro_unit_mass               unit_kilogram
linear_tol                  0.001
angular_tol                 0.5

! Start Models
template_designasm          $PRO_DIRECTORY\Creo_Start_Assembly_Frame_Section.asm
template_solidpart          $PRO_DIRECTORY\Creo_Start_Part_Structural.prt
template_drawing            $PRO_DIRECTORY\Creo_Drawing_Template_A3.drw
start_model_dir             $PRO_DIRECTORY\templates

! Display Settings
display                     shadewithedges
tangent_edge_display        yes
spin_center_display         yes
datum_point_size            10

! Feature Settings
sketcher_intent_manager     yes
regen_failure_handling      resolve_mode
bell                        no

! File Management
save_model_display          wireframe
remember_dependencies       yes
file_open_default_folder    working_directory

! Drawing Settings
drawing_setup_file          $PRO_DIRECTORY\Creo_Drawing_Setup.dtl
format_setup_file           $PRO_DIRECTORY\Creo_Format_A3_Landscape.frm
detail_options_file         iso.dtl

! Misc
allow_anatomic_features     yes
default_draw_scale          1.000000
tolerance_standard          iso
```

### Site Configuration (config.sup)
Locked settings that cannot be changed by users:
```
pro_unit_length             unit_mm
pro_unit_mass               unit_kilogram
template_solidpart          $PRO_DIRECTORY\Creo_Start_Part_Structural.prt
tolerance_standard          iso
```

## Drawing Setup File (DTL)

### Drawing Standards
`Creo_Drawing_Setup.dtl` configures:
- Dimension format and precision
- Tolerance display
- Arrow styles and sizes
- Text height and font
- Line styles and weights
- Annotation standards

**Example DTL settings:**
```
drawing_units               millimeter
decimal_marker              period
dim_fraction_format         decimal
text_height_factor          3.5
```

## Material Library

### Standard Materials
Material file: `Creo_Materials_53-10.mtl`

Materials defined:
- **ALUMINUM_2024_T3**
  - Density: 2780 kg/m³
  - Young's Modulus: 73.1 GPa
  - Poisson's Ratio: 0.33
  
- **ALUMINUM_7075_T6**
  - Density: 2810 kg/m³
  - Young's Modulus: 71.7 GPa

- **TITANIUM_TI6AL4V**
  - Density: 4430 kg/m³
  - Young's Modulus: 113.8 GPa

### Applying Materials
1. **Edit → Setup → Material**
2. Select from material library
3. Or **File → Prepare → Model Properties → Materials**
4. Assign material to part

## Parameters and Relations

### Standard Parameters
Pre-defined in start models:
```
LENGTH          = 100
WIDTH           = 50
HEIGHT          = 30
THICKNESS       = 2
MATERIAL        = "ALUMINUM_2024_T3"
PART_NUMBER     = ""
DESCRIPTION     = ""
REVISION        = "A"
DRAWN_BY        = ""
```

### Relations Examples
```
/* Parametric relationships */
d1 = LENGTH / 2
d2 = WIDTH - 2 * THICKNESS
d3 = HEIGHT + OFFSET

/* Conditional logic */
IF LENGTH > 100
  THICKNESS = 3
ELSE
  THICKNESS = 2
ENDIF
```

## Installation

### Installing Start Models
1. Copy start models to: `C:\Creo_Templates\`
2. Or project directory: `[PROJECT]\Creo_Templates\`

### Setting Configuration
1. Copy `config.pro` to Creo startup directory
2. Or set environment variable: `PTC_WF_ROOT`
3. Restart Creo for settings to take effect

**Config.pro search order:**
1. Current working directory
2. Creo loadpoint directory (installation folder)
3. User's home directory

### Setting Start Model Directory
In `config.pro`:
```
start_model_dir  C:\Creo_Templates
template_solidpart  $PRO_DIRECTORY\Creo_Start_Part_Structural.prt
```

## Usage Guidelines

### Creating New Part from Start Model
1. **File → New**
2. Type: Part, Sub-type: Solid
3. Name: Enter part name
4. Use default template: Yes (uses start model if configured)
5. **OK**
6. Immediately **File → Save As** with proper name
7. Update model properties (part number, description)

### Best Practices
- Use parameters for dimensional control
- Organize feature tree with groups
- Use relations for parametric logic
- Name all datums and features
- Apply materials early
- Use family tables for variants
- Document design intent in comments

### Assembly Best Practices
- Use skeleton models for layout control
- Define interfaces between components
- Use component arrays for patterns
- Simplified reps for performance
- Assemble using coordinate systems when possible

## Troubleshooting

**Issue:** Start model not used on File → New
- **Solution:** Check config.pro settings for `template_solidpart` and `start_model_dir`

**Issue:** Config.pro settings not applied
- **Solution:** Verify config.pro is in correct directory, restart Creo

**Issue:** Material library not found
- **Solution:** Set `pro_material_dir` in config.pro, or place `.mtl` file in correct folder

**Issue:** Drawing template not loading format
- **Solution:** Check `format_setup_file` and `drawing_setup_file` in config.pro

**Issue:** Units incorrect
- **Solution:** Verify `pro_unit_length` and `pro_unit_mass` in config.pro

## Windchill Integration

### Managed Mode (with Windchill PDM)
When using Windchill:
- Templates stored in Windchill CommonSpace
- Use "New from Template" in Windchill
- Part numbers from Windchill numbering scheme
- Lifecycle and revisions managed by Windchill
- Check-in/check-out workflow

### Standalone Mode
When not using Windchill:
- Templates stored in file system
- Manual part numbering
- File-based version control

## Related Files

- Parent directory: [`../README.md`](../README.md)
- CATIA seeds: [`../CATIA/README.md`](../CATIA/README.md)
- NX seeds: [`../NX/README.md`](../NX/README.md)
- SOLIDWORKS seeds: [`../SOLIDWORKS/README.md`](../SOLIDWORKS/README.md)

## References

- PTC Creo Parametric documentation
- Creo configuration options guide
- Company Creo standards
- Windchill integration guide (if applicable)
