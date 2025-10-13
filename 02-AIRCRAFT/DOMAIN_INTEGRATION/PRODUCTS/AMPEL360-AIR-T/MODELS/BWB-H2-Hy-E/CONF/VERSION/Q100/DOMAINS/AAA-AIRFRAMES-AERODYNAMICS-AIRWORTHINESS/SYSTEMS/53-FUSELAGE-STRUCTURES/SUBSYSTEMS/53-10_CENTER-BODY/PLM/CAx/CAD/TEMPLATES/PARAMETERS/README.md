# PARAMETERS — Design Parameter Standards

## Purpose

Standardized design parameters, dimensional relationships, and parametric modeling conventions for the 53-10 Center Body design.

## Parameter Categories

### Geometric Parameters

#### Linear Dimensions
- **LENGTH_**: Overall length dimensions
- **WIDTH_**: Width and span dimensions  
- **HEIGHT_**: Height and depth dimensions
- **THICKNESS_**: Material thickness, wall thickness
- **OFFSET_**: Offset distances and spacing
- **PITCH_**: Repetitive spacing (fasteners, ribs, etc.)

**Examples:**
```
LENGTH_FRAME_BAY = 500.0 mm
WIDTH_PANEL_OVERALL = 800.0 mm
HEIGHT_FRAME_WEB = 150.0 mm
THICKNESS_SKIN_NOMINAL = 2.0 mm
OFFSET_STRINGER_SPACING = 180.0 mm
PITCH_FASTENER_LONGITUDINAL = 30.0 mm
```

#### Angular Dimensions
- **ANGLE_**: Angular dimensions and rotations
- **SWEEP_**: Sweep angles for aerodynamic surfaces
- **DIHEDRAL_**: Dihedral/anhedral angles

**Examples:**
```
ANGLE_FRAME_SLOPE = 5.0 deg
SWEEP_LEADING_EDGE = 35.0 deg
DIHEDRAL_WING_SECTION = 3.5 deg
```

#### Radii and Fillets
- **RADIUS_**: Bend radii, corner radii
- **FILLET_**: Fillet radii

**Examples:**
```
RADIUS_BEND_MIN_2024T3 = 2.0 * t (t = thickness)
RADIUS_CORNER_CUTOUT = 5.0 mm
FILLET_EDGE_STANDARD = 1.0 mm
```

### Material Parameters

#### Material Properties
- **MAT_DENSITY**: Material density (kg/m³)
- **MAT_ELASTIC_MODULUS**: Young's modulus (GPa)
- **MAT_POISSON_RATIO**: Poisson's ratio
- **MAT_YIELD_STRENGTH**: Yield strength (MPa)
- **MAT_ULTIMATE_STRENGTH**: Ultimate strength (MPa)

**Examples:**
```
MAT_DENSITY_AL2024T3 = 2780 kg/m³
MAT_ELASTIC_MODULUS_AL2024T3 = 73.1 GPa
MAT_POISSON_RATIO_AL2024T3 = 0.33
MAT_YIELD_STRENGTH_AL2024T3 = 345 MPa
MAT_ULTIMATE_STRENGTH_AL2024T3 = 483 MPa
```

### Manufacturing Parameters

#### Bend Allowances
- **BA_**: Bend allowance for sheet metal
- **BD_**: Bend deduction

**Examples:**
```
BA_AL2024_T090_R2T = 1.57 * t (for 90° bend, R=2t)
BD_AL2024_T090_R2T = 0.43 * t
```

#### Clearances
- **CLR_**: Clearance dimensions
- **GAP_**: Gap dimensions

**Examples:**
```
CLR_FASTENER_EDGE_MIN = 2.0 * D (D = fastener diameter)
CLR_TOOL_ACCESS = 50.0 mm
GAP_ASSEMBLY_TOLERANCE = 1.0 mm
```

#### Tolerances
- **TOL_**: Tolerance values
- **FIT_**: Fit classes

**Examples:**
```
TOL_GENERAL_LINEAR = ±0.5 mm
TOL_HOLE_DIAMETER_FASTENER = +0.1/+0.2 mm
TOL_ANGLE_GENERAL = ±0.5 deg
FIT_BUSHING_PRESS = H7/m6
```

### Interface Parameters

#### Station References
- **FS_**: Fuselage Station (longitudinal, X-axis)
- **BL_**: Buttline (lateral, Y-axis)
- **WL_**: Waterline (vertical, Z-axis)

**Examples:**
```
FS_CENTER_BODY_FWD = 1000.0 mm
FS_CENTER_BODY_AFT = 1500.0 mm
BL_CENTERLINE = 0.0 mm
WL_REFERENCE = 500.0 mm
```

#### Interface Dimensions
- **INT_**: Interface dimensions and references

**Examples:**
```
INT_WING_ATTACH_FS = 1200.0 mm
INT_WING_ATTACH_BL = 800.0 mm
INT_FLOOR_LEVEL_WL = 650.0 mm
```

### Configuration Parameters

#### Design Options
- **OPT_**: Design option toggles
- **CONFIG_**: Configuration switches

**Examples:**
```
OPT_LIGHTENING_HOLES = TRUE/FALSE
OPT_REINFORCEMENT_DOUBLER = TRUE/FALSE
CONFIG_HAND = LEFT/RIGHT
CONFIG_MATERIAL = ALUMINUM/TITANIUM/COMPOSITE
```

## Parameter Naming Conventions

### General Rules
1. Use UPPERCASE for parameter names
2. Use underscores (_) to separate words
3. Start with parameter type prefix
4. Include descriptive name
5. Add unit suffix where appropriate

### Standard Prefixes
- **LENGTH_**, **WIDTH_**, **HEIGHT_**: Linear dimensions
- **ANGLE_**, **SWEEP_**, **DIHEDRAL_**: Angular dimensions
- **RADIUS_**, **FILLET_**: Radii
- **THICKNESS_**, **OFFSET_**, **PITCH_**: Specific dimensions
- **MAT_**: Material properties
- **BA_**, **BD_**: Bend allowances/deductions
- **CLR_**, **GAP_**: Clearances and gaps
- **TOL_**, **FIT_**: Tolerances and fits
- **FS_**, **BL_**, **WL_**: Station references
- **INT_**: Interface parameters
- **OPT_**, **CONFIG_**: Configuration parameters

### Standard Suffixes
- **_NOM**: Nominal dimension
- **_MIN**: Minimum dimension
- **_MAX**: Maximum dimension
- **_TOL**: Tolerance value
- **_DEG**: Angle in degrees
- **_MM**: Dimension in millimeters
- **_IN**: Dimension in inches

## Parameter Tables

### Standard Frame Dimensions
| Parameter | Value | Units | Description |
|-----------|-------|-------|-------------|
| LENGTH_FRAME_BAY_STANDARD | 500 | mm | Standard frame bay spacing |
| HEIGHT_FRAME_WEB_TYPICAL | 150 | mm | Typical frame web height |
| THICKNESS_FRAME_WEB | 2.0 | mm | Frame web thickness |
| THICKNESS_FRAME_CAP | 3.0 | mm | Frame cap thickness |
| RADIUS_FRAME_CORNER | 5.0 | mm | Frame corner radius |

### Standard Skin Dimensions
| Parameter | Value | Units | Description |
|-----------|-------|-------|-------------|
| THICKNESS_SKIN_OUTER | 2.0 | mm | Outer skin nominal thickness |
| THICKNESS_SKIN_INNER | 1.6 | mm | Inner skin nominal thickness |
| RADIUS_SKIN_BEND_MIN | 4.0 | mm | Minimum skin bend radius (2t) |

### Standard Fastener Parameters
| Parameter | Value | Units | Description |
|-----------|-------|-------|-------------|
| DIA_FASTENER_NOMINAL | 4.0 | mm | Standard fastener diameter |
| PITCH_FASTENER_LONG | 30.0 | mm | Longitudinal fastener pitch |
| PITCH_FASTENER_TRANS | 25.0 | mm | Transverse fastener pitch |
| CLR_FASTENER_EDGE_MIN | 8.0 | mm | Minimum edge distance (2D) |

## Parameter Relationships

### Driven Parameters
Parameters calculated from other parameters:

```
# Bend allowance relationship
BA = (π/180) * ANGLE * (RADIUS + K * THICKNESS)

# Edge distance from fastener diameter
CLR_EDGE_MIN = 2.0 * DIA_FASTENER

# Minimum bend radius from thickness
RADIUS_BEND_MIN = 2.0 * THICKNESS

# Frame bay mass (approximate)
MASS_FRAME_BAY = DENSITY * AREA * LENGTH
```

### Design Rules
Parameter limits and constraints:

```
# Sheet metal bend radius
RADIUS_BEND >= 2.0 * THICKNESS  (Al 2024-T3)
RADIUS_BEND >= 1.5 * THICKNESS  (Al 5052-H32)

# Fastener spacing
PITCH_MIN = 3.0 * DIA_FASTENER
PITCH_MAX = 6.0 * DIA_FASTENER  (unsealed joint)
PITCH_MAX = 4.0 * DIA_FASTENER  (sealed joint)

# Edge distance
CLR_EDGE >= 2.0 * DIA_FASTENER
CLR_EDGE >= 2.5 * DIA_FASTENER  (for high loads)
```

## Parameter Management

### Parameter Files
- **master_parameters.txt**: Global parameter definitions
- **frame_parameters.txt**: Frame-specific parameters
- **skin_parameters.txt**: Skin panel parameters
- **interface_parameters.txt**: Interface definitions

### Parameter Propagation
- Use design tables for parameter families
- Link parameters across part/assembly hierarchy
- Publish key parameters to assembly level
- Maintain parameter integrity through updates

### Parameter Documentation
- Document parameter purpose and usage
- Include formulas for calculated parameters
- Note parameter relationships and dependencies
- Update parameter values through ECRs

## Related Directories

- **Naming Conventions**: [`../NAMING_CONVENTIONS/`](../NAMING_CONVENTIONS/) — Naming standards
- **Properties**: [`../PROPERTIES/`](../PROPERTIES/) — Metadata standards
- **Materials**: [`../MATERIALS/`](../MATERIALS/) — Material properties
- **Scripts/Macros**: [`../SCRIPTS_MACROS/`](../SCRIPTS_MACROS/) — Parameter automation

## References

- Main templates: [`../README.md`](../README.md)
- Design standards: [`../../README.md`](../../README.md)
- Dimensions & Stations: [`../../../../06-DIMENSIONS-STATIONS/`](../../../../06-DIMENSIONS-STATIONS/)
- NACA TN 2661 — Bend allowances
- Company parametric modeling standards
