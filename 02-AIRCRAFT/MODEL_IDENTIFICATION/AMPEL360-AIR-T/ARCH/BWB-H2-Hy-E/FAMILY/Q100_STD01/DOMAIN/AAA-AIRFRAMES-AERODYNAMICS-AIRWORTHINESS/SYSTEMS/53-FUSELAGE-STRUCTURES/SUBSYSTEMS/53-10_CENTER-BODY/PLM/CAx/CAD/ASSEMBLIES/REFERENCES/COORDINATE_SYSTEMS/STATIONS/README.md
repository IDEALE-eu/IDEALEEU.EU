# STATIONS — Station-Based Coordinate Systems

## Purpose

This directory contains coordinate system definitions based on standard aircraft stations (FS, WL, BL) for the 53-10 Center Body.

## Contents

### FUSELAGE_STATION_FS/
Fuselage Station coordinate systems:
- Longitudinal reference planes perpendicular to X-axis
- Station numbers per ATA-06 STATIONING_MASTER.csv
- Typical spacing: 50mm or 100mm increments
- Used for longitudinal positioning and sectioning

### WATERLINE_WL/
Waterline coordinate systems:
- Horizontal reference planes perpendicular to Z-axis
- Height references from keel datum
- Used for vertical positioning and clearance verification
- Ground line and cabin floor references

### BUTTOCKLINE_BL/
Buttline coordinate systems:
- Vertical reference planes perpendicular to Y-axis
- BL 0 = fuselage centerline
- Positive BL = starboard (right), Negative BL = port (left)
- Used for lateral positioning and symmetry checks

## Naming Convention

Station coordinate systems follow:
```
53-10_REF_CS_<station_type>_<value>_v<version>.<ext>
```

Examples:
- `53-10_REF_CS_FS_1200_v01.CATPart`
- `53-10_REF_CS_WL_500_v01.prt`
- `53-10_REF_CS_BL_0_v01.sldprt`

## Cross-References

- [Parent: COORDINATE_SYSTEMS](../README.md)
- [ATA-06: Dimensions & Stations](../../../../../../../06-DIMENSIONS-STATIONS/README.md)
- [STATIONING_MASTER.csv](../../../../../../../06-DIMENSIONS-STATIONS/SUBSYSTEMS/06-00_GENERAL/STATIONING_MASTER.csv)

## Usage Guidelines

### Design
- Reference for component positioning along/across/above fuselage
- Section plane definitions for drawings
- Interface location specification

### Manufacturing
- Tooling reference stations
- Assembly fixture positioning
- Inspection measurement datums

### Analysis
- FEA model sectioning
- Load distribution planes
- Results presentation locations

---

**Owner**: 53-10 Center Body Integration  
**Derived from**: ATA-06 Master Stations  
**Update frequency**: As needed per design iterations
