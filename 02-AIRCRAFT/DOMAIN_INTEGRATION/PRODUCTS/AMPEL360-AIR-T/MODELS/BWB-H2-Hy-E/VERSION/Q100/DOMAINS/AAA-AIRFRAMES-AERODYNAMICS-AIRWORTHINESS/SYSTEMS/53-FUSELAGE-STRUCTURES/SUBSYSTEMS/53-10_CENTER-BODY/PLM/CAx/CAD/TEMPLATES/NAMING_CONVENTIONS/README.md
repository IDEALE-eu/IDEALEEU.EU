# NAMING_CONVENTIONS — File and Feature Naming Standards

## Purpose

Standardized naming conventions for CAD files, features, assemblies, and drawings to ensure consistency across the 53-10 Center Body project.

## File Naming Conventions

### Part Files

**Format:**
```
<subsystem>_PRT_<description>_<variant>_v<version>.<ext>
```

**Examples:**
- `53-10_PRT_FRAME-F03_UPPER_v01.CATPart`
- `53-10_PRT_SKIN-PANEL-SP-001_v02.prt`
- `53-10_PRT_FITTING-WING-ATTACH_LEFT_v01.sldprt`

**Rules:**
- Use subsystem code (53-10) as prefix
- Include "PRT" to identify as part
- Use descriptive name with hyphens
- Add variant/position identifier if applicable
- Include version number (v01, v02, etc.)
- Use uppercase for keywords, hyphens for separators

### Assembly Files

**Format:**
```
<subsystem>_ASM_<assembly-name>_<variant>_v<version>.<ext>
```

**Examples:**
- `53-10_ASM_CENTER-BODY_COMPLETE_v01.CATProduct`
- `53-10_ASM_FRAME-SECTION_F01-F05_v02.asm`
- `53-10_ASM_SKIN-PANEL-ASSY_SP-001_v01.sldasm`

**Rules:**
- Use subsystem code (53-10) as prefix
- Include "ASM" to identify as assembly
- Use descriptive assembly name
- Include range or zone if applicable
- Include version number

### Drawing Files

**Format:**
```
<subsystem>_DWG_<part-or-assy-name>_<sheet>_v<version>.<ext>
```

**Examples:**
- `53-10_DWG_FRAME-F03_SH01_v01.CATDrawing`
- `53-10_DWG_CENTER-BODY_INSTALLATION_SH01_v02.drw`
- `53-10_DWG_SKIN-PANEL-SP-001_SH01_v01.slddrw`

**Rules:**
- Use subsystem code (53-10) as prefix
- Include "DWG" to identify as drawing
- Reference part or assembly name
- Include sheet number (SH01, SH02, etc.)
- Include version number

## Feature Naming Conventions

### Parametric Features

**Format:**
```
<feature-type>_<description>_<sequence>
```

**Examples:**
- `HOLE_FASTENER_PATTERN_001`
- `CUTOUT_LIGHTENING_FRAME_F03`
- `FILLET_CORNER_RADIUS_R5`
- `POCKET_WEIGHT_REDUCTION_001`

**Rules:**
- Use feature type as prefix (HOLE, CUTOUT, FILLET, etc.)
- Include descriptive purpose
- Add sequence number for multiple similar features
- Use uppercase for readability

### Datum and Reference Features

**Format:**
```
DATUM_<axis>_<description>
REF_<type>_<description>
```

**Examples:**
- `DATUM_X_FUSELAGE_STATION_FS1200`
- `DATUM_Y_BUTTLINE_BL0`
- `DATUM_Z_WATERLINE_WL500`
- `REF_PLANE_MOLD_LINE_OML`
- `REF_CURVE_SECTION_PROFILE`

## Material and Property Naming

### Material Names
```
<material-type>_<alloy>_<temper>
```

**Examples:**
- `ALUMINUM_2024_T3`
- `ALUMINUM_7075_T6`
- `TITANIUM_6AL4V_ANNEALED`
- `CFRP_AS4_3501-6`
- `STEEL_4340_QUENCHED-TEMPERED`

### Property Sets
```
PROP_<category>_<description>
```

**Examples:**
- `PROP_STRUCTURAL_FRAME_MEMBER`
- `PROP_SHEET_METAL_SKIN_PANEL`
- `PROP_FASTENER_HI-LOK`
- `PROP_COMPOSITE_LAMINATE`

## Parameter Naming Conventions

### Design Parameters

**Format:**
```
<PARAM_TYPE>_<description>
```

**Examples:**
- `LENGTH_FRAME_BAY_SPACING`
- `THICKNESS_SKIN_PANEL_T_NOM`
- `DIAMETER_HOLE_FASTENER_D_NOM`
- `ANGLE_SWEEP_CONTOUR_A_DEG`
- `RADIUS_FILLET_CORNER_R_MIN`

**Rules:**
- Use parameter type prefix (LENGTH, THICKNESS, DIAMETER, ANGLE, RADIUS)
- Include descriptive name
- Add unit suffix where appropriate (_DEG, _MM, _IN)
- Use _NOM for nominal, _MIN for minimum, _MAX for maximum

## Configuration and Variant Naming

### Configurations
```
CONFIG_<variant>_<description>
```

**Examples:**
- `CONFIG_LEFT_HAND_INSTALLED`
- `CONFIG_RIGHT_HAND_INSTALLED`
- `CONFIG_BASELINE_DESIGN`
- `CONFIG_ALT_MATERIAL_TITANIUM`

### Display States
```
STATE_<visibility>_<purpose>
```

**Examples:**
- `STATE_DETAILED_INSPECTION`
- `STATE_SIMPLIFIED_ASSEMBLY`
- `STATE_LIGHTWEIGHT_REVIEW`
- `STATE_MANUFACTURING_VIEW`

## Abbreviations and Acronyms

### Common Abbreviations
- **ASM**: Assembly
- **PRT**: Part
- **DWG**: Drawing
- **ASSY**: Assembly
- **OML**: Outer Mold Line
- **IML**: Inner Mold Line
- **FS**: Fuselage Station
- **BL**: Buttline
- **WL**: Waterline
- **FWD**: Forward
- **AFT**: Aft
- **LH**: Left Hand
- **RH**: Right Hand
- **UPR**: Upper
- **LWR**: Lower
- **CTR**: Center
- **INBD**: Inboard
- **OUTBD**: Outboard

### System-Specific Terms
- **CB**: Center Body
- **FR**: Frame
- **STR**: Stringer
- **SK**: Skin
- **SP**: Skin Panel
- **FTG**: Fitting
- **BRKT**: Bracket
- **CLR**: Clearance
- **INT**: Interface

## Usage Guidelines

### File Naming Best Practices
1. Always use consistent case (UPPERCASE for keywords)
2. Use hyphens (-) to separate words, underscores (_) to separate sections
3. Avoid spaces in file names
4. Keep names descriptive but concise (< 50 characters)
5. Include version numbers for revision tracking
6. Use standard abbreviations from approved list

### Feature Naming Best Practices
1. Name all significant features (don't use default names)
2. Use consistent naming across similar features
3. Include purpose or function in name
4. Use sequential numbering for feature groups
5. Update feature names during design changes

### Validation
- File names must match regex pattern: `^[A-Z0-9_-]+\.[a-z]+$`
- No special characters except hyphen and underscore
- Version numbers required for released files
- Subsystem prefix required (53-10)

## Related Directories

- **Properties**: [`../PROPERTIES/`](../PROPERTIES/) — Metadata field standards
- **Parameters**: [`../PARAMETERS/`](../PARAMETERS/) — Design parameter standards
- **Main templates**: [`../README.md`](../README.md)

## References

- ATA Chapter 53 naming conventions
- Company file naming standards
- Configuration management procedures: [`/00-PROGRAM/CONFIG_MGMT/`](/00-PROGRAM/CONFIG_MGMT/)
- Part numbering scheme: [`/00-PROGRAM/CONFIG_MGMT/02-PART_NUMBERING.md`](/00-PROGRAM/CONFIG_MGMT/02-PART_NUMBERING.md)
