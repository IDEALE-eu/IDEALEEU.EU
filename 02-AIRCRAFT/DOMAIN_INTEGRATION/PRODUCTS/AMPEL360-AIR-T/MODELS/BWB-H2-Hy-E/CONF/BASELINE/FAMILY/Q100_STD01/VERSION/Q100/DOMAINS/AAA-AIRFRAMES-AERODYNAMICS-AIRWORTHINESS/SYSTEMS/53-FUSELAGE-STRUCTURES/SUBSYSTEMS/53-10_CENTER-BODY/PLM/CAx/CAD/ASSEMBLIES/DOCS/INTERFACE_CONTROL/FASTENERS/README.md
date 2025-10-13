# FASTENERS — Fastener Specifications and Installation

## Purpose

This directory contains fastener specifications, installation procedures, and torque requirements for all interface attachments.

## Content Types

### Fastener Specifications
- Part numbers and manufacturers
- Material specifications
- Size and grip length
- Head style and drive type
- Finish and coating requirements

### Installation Data
- Installation procedures
- Torque specifications
- Sealant requirements
- Interference fit requirements
- Lock wire/safety wire requirements

### Bill of Fasteners
- Complete fastener lists by interface
- Quantities and locations
- Alternative fasteners (if applicable)
- Spare requirements

## File Formats

- `.csv` — Fastener bills of materials
- `.xlsx` — Detailed fastener specifications
- `.pdf` — Installation procedures and drawings
- `.json` — Machine-readable fastener database

## Data Structure (CSV)

```csv
fastener_id,part_number,description,material,size,grip_length,quantity,location,torque,notes
FTN-001,NAS1303-6,Hex Bolt,A286,1/4-28,1.50,24,Wing attach,60-70 lb-in,Primary structure
FTN-002,NAS1352N6-8,Close Tolerance Bolt,A286,3/8-24,2.00,48,Bulkhead,120-140 lb-in,Critical joint
```

## Naming Convention

```
FTN_{interface}_{type}_v{version}.{ext}
```

Examples:
- `FTN_WING-ATTACH_BOLTS_v001.csv`
- `FTN_DOOR-FRAME_RIVETS_v002.xlsx`
- `FTN_INSTALLATION-PROC_v001.pdf`

## Fastener Categories

### Permanent Fasteners
- Solid rivets
- Blind rivets
- Hi-Loks
- Lockbolts

### Removable Fasteners
- Bolts with nuts
- Screws
- Studs
- Quick release fasteners

### Special Fasteners
- Interference fit bolts
- Tension bolts
- Shear bolts
- Self-locking fasteners

## Installation Requirements

### Installation Procedure
1. Hole preparation and inspection
2. Sealant application (if required)
3. Fastener installation
4. Torque application
5. Safety wire/lock wire (if required)
6. Final inspection

### Quality Control
- Torque verification
- Visual inspection
- Gap inspection
- Lock wire verification
- Documentation

## Material Specifications

Common materials:
- **A286**: Corrosion-resistant steel
- **Titanium**: Weight critical applications
- **Monel**: High corrosion resistance
- **Aluminum**: Non-structural applications
- **Inconel**: High temperature applications

## Cross-References

- [Hole Patterns](../HOLE_PATTERNS/)
- [Torque Specifications](../TORQUE_SPECS/)
- [Sealants and Gaskets](../SEALANTS_GASKETS/)
- [Interface Control Documents](../ICD/)

## Standards

- **NASM**: National Aerospace Standard for Fasteners
- **NAS**: Aerospace fastener standards
- **MS**: Military Standard fasteners
- **AN**: Air Force-Navy aeronautical standards
- **ASME B18**: Fastener standards
- **ISO 3506**: Mechanical properties of corrosion-resistant stainless steel fasteners
