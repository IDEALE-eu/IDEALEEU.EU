# STATIONS — Aircraft Station Reference Planes

## Purpose

This directory contains CAD models of aircraft station reference planes used to locate structural elements and define positions along the center body coordinate axes.

## Contents

### FS/ — Fuselage Stations
- **Description**: Longitudinal reference planes (perpendicular to X-axis)
- **Definition**: Planes perpendicular to the aircraft longitudinal axis
- **Measurement**: Distance from aircraft reference point along X-axis
- **Positive Direction**: Aft (rearward)
- **Typical Spacing**: 100-500mm depending on structural density
- **Usage**: Frame locations, bulkhead positions, longitudinal dimensions

**Center Body Key Stations**:
- FS 1000-1500: Center body extent (example range)
- Forward bulkhead station
- Aft bulkhead station
- Wing attachment stations
- Major frame stations (F01-F20)

### WL/ — Waterlines
- **Description**: Horizontal reference planes (perpendicular to Z-axis)
- **Definition**: Planes perpendicular to the vertical axis
- **Measurement**: Distance from aircraft datum (ground line or keel)
- **Positive Direction**: Up (vertical)
- **Typical Spacing**: 50-200mm depending on design
- **Usage**: Vertical dimensions, floor levels, equipment mounting heights

**Center Body Key Waterlines**:
- Keel waterline (reference)
- Floor level waterlines
- Equipment mounting waterlines
- Upper deck waterlines

### BL/ — Buttock Lines
- **Description**: Vertical lateral reference planes (perpendicular to Y-axis)
- **Definition**: Planes parallel to aircraft centerline (FRP)
- **Measurement**: Distance from centerline along Y-axis
- **Positive Direction**: Starboard (right)
- **Typical Spacing**: 50-200mm depending on design
- **Usage**: Lateral dimensions, symmetry checks, width measurements

**Center Body Key Buttock Lines**:
- BL 0: Fuselage centerline (symmetry plane)
- Wing root buttock lines
- Door edge buttock lines
- Equipment mounting buttock lines

## Station Numbering Convention

### Fuselage Stations (FS)
Format: `FS-<value>` where value is in millimeters from reference point

Examples:
- `FS-1000`: 1000mm aft of reference point
- `FS-1250`: 1250mm aft of reference point

### Waterlines (WL)
Format: `WL-<value>` where value is height in millimeters from datum

Examples:
- `WL-0`: Aircraft datum waterline
- `WL-1000`: 1000mm above datum
- `WL-FLOOR`: Floor level waterline

### Buttock Lines (BL)
Format: `BL-<value>` where value is lateral distance in millimeters

Examples:
- `BL-0`: Centerline (symmetry plane)
- `BL-500`: 500mm starboard of centerline
- `BL--500`: 500mm port of centerline (negative)

## File Naming Convention

Use the following pattern:
```
53-10_STATION_<type>-<location>_<version>.<ext>
```

Examples:
- `53-10_STATION_FS-1200_v01.CATPart`
- `53-10_STATION_WL-1000_v01.prt`
- `53-10_STATION_BL-0_CENTERLINE_v01.sldprt`

## Usage Guidelines

### Design Applications
- Component positioning and layout
- Structural member location
- Section view creation
- Dimension reference

### Manufacturing Applications
- Tooling station references
- Assembly fixture locations
- Inspection plane setup
- Measurement references

### Documentation Applications
- Drawing views and sections
- Installation drawings
- Interface control drawings
- Inspection reports

## Standards Compliance

Follow:
- **ATA iSpec 2200**: Station numbering conventions
- **ISO 5458**: Positional tolerancing
- **ASME Y14.5**: Datum reference frames
- **Company standards**: Internal station numbering system

## Related Directories

- **Global planes**: [`../GLOBAL/`](../GLOBAL/)
- **Local planes**: [`../LOCAL/`](../LOCAL/)
- **Interface planes**: [`../INTERFACES/`](../INTERFACES/)
- **Coordinate systems**: [`../../COORDINATE_SYSTEMS/`](../../COORDINATE_SYSTEMS/)
