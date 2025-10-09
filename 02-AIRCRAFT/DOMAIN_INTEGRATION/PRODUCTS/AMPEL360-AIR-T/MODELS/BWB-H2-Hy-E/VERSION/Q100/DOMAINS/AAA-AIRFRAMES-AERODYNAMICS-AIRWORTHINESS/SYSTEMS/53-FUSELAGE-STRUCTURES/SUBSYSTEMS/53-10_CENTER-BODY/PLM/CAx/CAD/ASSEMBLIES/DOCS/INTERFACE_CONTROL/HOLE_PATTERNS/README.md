# HOLE_PATTERNS — Hole Patterns and Fastener Locations

## Purpose

This directory contains hole pattern definitions, fastener locations, and drilling specifications for interface attachments.

## Content Types

### Hole Pattern Definitions
- Fastener hole locations and coordinates
- Hole patterns for wing-to-body joints
- Door frame attachment patterns
- Equipment mounting patterns
- Temporary fastener locations

### Hole Specifications
- Hole diameters and tolerances
- Countersink dimensions
- Spot face requirements
- Edge distance requirements
- Pitch and spacing specifications

## File Formats

- `.csv` — Hole location tables with coordinates
- `.dxf` — 2D hole pattern drawings
- `.step` — 3D hole geometry
- `.pdf` — Hole pattern specifications and drawings
- `.xlsx` — Hole tables with specifications

## Data Structure (CSV)

```csv
hole_id,x_coord,y_coord,z_coord,diameter,type,depth,countersink_angle,countersink_dia,notes
HP-001,1000.0,500.0,0.0,6.35,THRU,N/A,100,10.0,Wing attach primary
HP-002,1050.0,500.0,0.0,6.35,THRU,N/A,100,10.0,Wing attach primary
```

## Naming Convention

```
HP_{interface}_{location}_{sequence}_v{version}.{ext}
```

Examples:
- `HP_WING-ATTACH_CENTER_FWD_v001.csv`
- `HP_DOOR-FRAME_ENTRY-1_v002.dxf`
- `HP_BULKHEAD_FWD_v001.pdf`

## Hole Types

### Through Holes
- Standard through holes
- Reamed holes
- Close tolerance holes

### Blind Holes
- Tapped holes
- Threaded inserts
- Anchor nuts

### Special Features
- Countersunk holes
- Spot faced holes
- Elongated holes
- Interference fit holes

## Quality Requirements

All hole patterns must specify:
- Hole diameter and tolerance class
- Position tolerance (GD&T)
- Surface finish requirements
- Inspection method
- Acceptance criteria

## Manufacturing Information

Include:
- Drilling sequence
- Tool specifications
- Fixture requirements
- Quality inspection points

## Cross-References

- [Fasteners](../FASTENERS/)
- [Interface Control Documents](../ICD/)
- [Tolerances](../TOLERANCES_GDT/)
- [Mates and Constraints](../MATES_CONSTRAINTS/)

## Standards

- **ASME Y14.5**: Position tolerancing for holes
- **NASM 33540**: Hole preparation for aerospace fasteners
- **MIL-STD-8**: Dimensioning and tolerancing
- **ISO 286**: ISO system of limits and fits
