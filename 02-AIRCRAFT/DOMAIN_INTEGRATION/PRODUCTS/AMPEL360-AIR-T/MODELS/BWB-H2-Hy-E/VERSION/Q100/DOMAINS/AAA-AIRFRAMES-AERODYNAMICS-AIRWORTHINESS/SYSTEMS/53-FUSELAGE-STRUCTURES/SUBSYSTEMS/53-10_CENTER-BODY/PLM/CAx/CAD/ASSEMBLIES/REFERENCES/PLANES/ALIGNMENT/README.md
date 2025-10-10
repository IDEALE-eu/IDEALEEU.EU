# ALIGNMENT — Alignment and Datum Reference Planes

## Purpose

This directory contains CAD models of alignment reference planes and datum features used for precise positioning, assembly, and inspection of the 53-10 Center Body structures.

## Contents

### DATUMS/ — Datum Reference Frames
- **Description**: Primary datum features defining part-level and assembly-level reference frames
- **Applications**:
  - GD&T datum reference frames
  - Component positioning datums
  - Assembly master datums
  - Inspection setup datums
  - Tooling alignment datums
- **Usage**: Establish repeatable, stable reference systems for all downstream operations

**Datum Types**:
- **Primary Datum (A)**: Most stable, typically planar surface with large area
- **Secondary Datum (B)**: Constrains additional degrees of freedom, perpendicular or related to A
- **Tertiary Datum (C)**: Fully constrains position and orientation, completes 3-2-1 locating scheme

### LOCATORS/ — Physical Locator Reference Planes
- **Description**: Reference planes for physical locating features (pins, holes, pads)
- **Applications**:
  - Tooling pin locations
  - Alignment hole positions
  - Locating pad surfaces
  - Jig reference points
  - Assembly indexing features
- **Usage**: Define precise locations for physical alignment features

**Locator Types**:
- **Diamond Pin Locators**: Constrain X and Y, allow Z float
- **Round Pin Locators**: Constrain rotation and one axis
- **Pad Locators**: Constrain Z height, support surface
- **V-Block Locators**: Constrain cylindrical features
- **Slot Locators**: Allow thermal expansion in one direction

## Datum Reference Frame (DRF) Design

### 3-2-1 Locating Principle

Standard aerospace locating scheme:
1. **Primary Datum (3 points)**: Constrains 3 DOF (typically Z, Rx, Ry)
2. **Secondary Datum (2 points)**: Constrains 2 DOF (typically Y, Rz)
3. **Tertiary Datum (1 point)**: Constrains 1 DOF (typically X)

Result: Fully constrained (6 DOF locked), kinematically stable

### Center Body Datum Structure

#### Assembly Master Datums

- **Datum A**: Lower fuselage skin panel (large planar reference)
  - Establishes vertical reference (WL)
  - Provides stable base for assembly
  
- **Datum B**: Forward bulkhead vertical surface
  - Establishes longitudinal reference (FS)
  - Perpendicular to Datum A
  
- **Datum C**: Centerline reference feature (left or right side)
  - Establishes lateral reference (BL)
  - Completes coordinate system definition

#### Component-Level Datums

Each major component should specify:
- Primary datum: Largest, most stable feature
- Secondary datum: Perpendicular or related feature
- Tertiary datum: Completes positional definition
- Datum precedence order: A, B, C

## Locating Feature Design

### Pin and Hole Locators

1. **Diamond Pin (Primary Locator)**
   - Shape: Two perpendicular flats on round pin
   - Function: Prevents X and Y movement, allows Z float
   - Location: Should be accessible, stable, load-bearing area
   - Tolerance: ±0.05mm typical for precision alignment

2. **Round Pin (Secondary Locator)**
   - Shape: Cylindrical pin
   - Function: Prevents rotation and one axis translation
   - Location: Maximum distance from diamond pin for best stability
   - Tolerance: ±0.10mm typical

3. **Pad/Float (Support Locators)**
   - Shape: Flat surface or clearance holes
   - Function: Support structure, allow thermal expansion
   - Location: Distributed to support weight and loads
   - Tolerance: ±0.20mm typical

### Locating Scheme Examples

**Frame Assembly**:
- Diamond pin at frame centerline, lower cap
- Round pin at frame upper cap, one side
- Support pads at intermediate locations

**Skin Panel Assembly**:
- Diamond pin at panel geometric center
- Round pin at panel corner or edge
- Support pads along panel edges

**Door Frame Assembly**:
- Diamond pin at door sill, centerline
- Round pin at door header, one side
- Support pads at hinge/latch locations

## File Organization

### DATUMS/ Subdirectory

```
DATUMS/
├── PRIMARY_A/
│   ├── 53-10_DATUM_A_LOWER_SKIN_v01.CATPart
│   └── 53-10_DATUM_A_DEFINITION.pdf
├── SECONDARY_B/
│   ├── 53-10_DATUM_B_FWD_BULKHEAD_v01.CATPart
│   └── 53-10_DATUM_B_DEFINITION.pdf
└── TERTIARY_C/
    ├── 53-10_DATUM_C_CENTERLINE_v01.CATPart
    └── 53-10_DATUM_C_DEFINITION.pdf
```

### LOCATORS/ Subdirectory

```
LOCATORS/
├── TOOLING_PINS/
│   ├── 53-10_LOCATOR_DIAMOND_01_v01.CATPart
│   └── 53-10_LOCATOR_ROUND_02_v01.CATPart
├── ASSEMBLY_HOLES/
│   ├── 53-10_LOCATOR_HOLE_PATTERN_v01.CATPart
│   └── 53-10_LOCATOR_HOLE_LAYOUT.pdf
└── SUPPORT_PADS/
    ├── 53-10_LOCATOR_PAD_01_v01.CATPart
    └── 53-10_LOCATOR_PAD_LAYOUT.pdf
```

## Naming Convention

### Datum Features

```
53-10_DATUM_<level>_<description>_<version>.<ext>
```

Examples:
- `53-10_DATUM_A_PRIMARY_v01.CATPart`
- `53-10_DATUM_B_SECONDARY_v01.prt`
- `53-10_DATUM_C_TERTIARY_v01.sldprt`

### Locator Features

```
53-10_LOCATOR_<type>_<id>_<location>_<version>.<ext>
```

Examples:
- `53-10_LOCATOR_DIAMOND_01_FWD_v01.CATPart`
- `53-10_LOCATOR_ROUND_02_AFT_v01.prt`
- `53-10_LOCATOR_PAD_03_LEFT_v01.sldprt`

## Usage Guidelines

### Design Phase
- Define datum reference frames early
- Select stable, accessible features
- Plan locator positions for stability
- Minimize thermal expansion effects

### Manufacturing Phase
- Use datums for fixture design
- Verify locator hole tolerances
- Check for adequate access
- Validate repeatability

### Assembly Phase
- Set up jigs using datum references
- Install locating pins carefully
- Verify component seating
- Check alignment before fastening

### Inspection Phase
- Establish CMM datum alignment
- Measure locator positions first
- Reference all dimensions to datums
- Verify GD&T compliance

## Quality Requirements

### Datum Feature Requirements

- Surface finish: Ra 1.6μm or better
- Flatness: 0.10mm over datum area
- Perpendicularity: 0.10mm between datum planes
- Accessibility: Clear access for measurement and fixturing

### Locator Feature Requirements

- Hole position tolerance: ±0.05mm for diamond, ±0.10mm for round
- Hole diameter tolerance: ±0.02mm typical
- Pad flatness: 0.05mm over pad area
- Surface condition: Clean, burr-free

## Standards Compliance

Follow:
- **ASME Y14.5**: Geometric dimensioning and tolerancing
- **ISO 5458**: Positional tolerancing
- **ISO 10579**: Dimensioning and tolerancing - Non-rigid parts
- **AS9102**: First article inspection (datum establishment)
- **Company fixture design standards**: Internal tooling practices

## Related Directories

- **Coordinate systems**: [`../../COORDINATE_SYSTEMS/`](../../COORDINATE_SYSTEMS/)
- **Station planes**: [`../STATIONS/`](../STATIONS/)
- **Assembly fixtures**: [`../../../FIXTURES/`](../../../FIXTURES/)
- **Inspection procedures**: [`../../../../../CAV/PROCEDURES/`](../../../../../CAV/PROCEDURES/)
