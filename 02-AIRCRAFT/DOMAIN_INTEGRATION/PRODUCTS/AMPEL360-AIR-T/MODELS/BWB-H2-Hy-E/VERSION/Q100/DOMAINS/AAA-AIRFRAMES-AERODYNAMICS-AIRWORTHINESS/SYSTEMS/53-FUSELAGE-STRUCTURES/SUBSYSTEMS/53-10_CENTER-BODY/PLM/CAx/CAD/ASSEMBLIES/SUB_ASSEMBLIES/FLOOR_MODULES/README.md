# FLOOR_MODULES — Floor Module Sub-Assemblies

## Purpose

This directory contains sub-assembly models for floor modules of the 53-10 Center Body. Floor modules include floor beams, floor panels, seat tracks, and cargo loading systems for each bay between frame stations.

## Organization

Floor modules are organized by bay identifier (BAY_XX):
- **BAY_01-10**: Forward cabin bays (passenger area)
- **BAY_11-15**: Center cabin/galley bays
- **BAY_16-20**: Aft cabin/cargo bays
- **BAY_CARGO**: Dedicated cargo floor sections

## Directory Structure

Each floor module (BAY_XX) contains:
- **MODELS/**: CAD assembly files for the floor module
- **DRAWINGS/**: Engineering drawings and manufacturing prints
- **DOCS/**: Documentation including BOM, load ratings, and installation procedures

## Naming Convention

Use the following pattern for floor module assemblies:
```
53-10_ASM_FLOOR-MODULE_BAY-<nn>_v<version>.<ext>
```

Examples:
- `53-10_ASM_FLOOR-MODULE_BAY-01_v01.CATProduct`
- `53-10_ASM_FLOOR-MODULE_BAY-05_v02.asm`
- `53-10_ASM_FLOOR-MODULE_BAY-12_v01.sldasm`

## Typical Floor Module Contents

A floor module assembly typically includes:
- **Floor beams**: Transverse beams between frame stations (2-4 beams per bay)
- **Floor panels**: Honeycomb or composite floor panels
- **Seat tracks**: Longitudinal tracks for seat attachment
- **Cargo rails**: Cargo loading and restraint system
- **Fittings**: Beam-to-frame attachment fittings
- **Support struts**: Diagonal or vertical supports under floor
- **Access panels**: Removable panels for below-floor access

## Assembly Structure Example

```
53-10_ASM_FLOOR-MODULE_BAY-05
├── Floor_Beam_FB-01 (at F05)
├── Floor_Beam_FB-02 (mid-bay)
├── Floor_Beam_FB-03 (at F06)
├── Floor_Panel_FP-001 (fwd half)
├── Floor_Panel_FP-002 (aft half)
├── Seat_Track_Left
├── Seat_Track_Right
├── Frame_Fittings (x6)
├── Support_Struts (x4)
└── Fasteners
```

## Integration Points

Floor modules interface with:
- **Frame sections**: Floor beam-to-frame attachments at each station
- **Fuselage stringers**: Support struts connecting to lower stringers
- **Seat installations**: Seat tracks for passenger seats
- **Galley units**: Reinforced floor areas for galley installations
- **Lavatories**: Plumbing and waste system routing under floor
- **Cargo systems**: ULD (Unit Load Device) restraint systems
- **Systems routing**: Cable, hydraulic, and pneumatic lines under floor

## Floor Types

### Passenger Cabin Floors
- **Standard passenger**: Typical seat track configuration
- **Premium cabin**: Enhanced sound insulation and comfort
- **Galley floors**: Reinforced for equipment weight
- **Lavatory floors**: Waterproof and chemical resistant

### Cargo Compartment Floors
- **Lower deck cargo**: Main cargo area with ULD restraints
- **Bulk cargo**: Loose cargo with nets and restraints
- **Belly cargo**: Lower fuselage cargo compartment

## Related Directories

- **Component models**: [`../../../MODELS/`](../../../MODELS/)
- **Frame sections**: [`../FRAME_SECTIONS/`](../FRAME_SECTIONS/)
- **Mounting units**: [`../MOUNTING_UNITS/`](../MOUNTING_UNITS/)
- **Documentation**: [`../DOCS/`](../DOCS/)
- **Top-level assembly**: [`../../TOP_LEVEL/`](../../TOP_LEVEL/)

## Design Guidelines

### Structural Design
- Design for distributed passenger/cargo loads
- Include safety factors per regulations (CS-25/FAR-25)
- Validate floor beam sizing for ultimate loads
- Design for emergency landing loads (16g forward, 9g up)
- Include proper attachment to primary structure

### Load Considerations
- **Static loads**: Passengers, cargo, equipment
- **Dynamic loads**: Turbulence, landing, emergency conditions
- **Point loads**: Galley equipment, lavatories, seats
- **Distributed loads**: Passenger area, cargo pallets

### Accessibility
- Include removable panels for systems access
- Design for wiring and systems installation
- Plan for maintenance access to below-floor systems
- Consider manufacturing and installation sequence

## Load Ratings

Document load ratings for each bay:
- **Passenger area**: Typically 100-120 kg/m² (20-25 lbs/ft²)
- **Galley area**: 200-300 kg/m² (40-60 lbs/ft²)
- **Cargo area**: 500-1000 kg/m² (100-200 lbs/ft²)
- **Point loads**: Seat/equipment attachment points

## Seat Track Specifications

Standard seat track requirements:
- **Track type**: AA series, extruded aluminum
- **Pitch**: 1-inch (25.4 mm) spacing
- **Load rating**: Per seat track manufacturer specifications
- **Attachment**: Fasteners at each floor beam
- **Inspection**: Regular inspection for wear and damage

## Cargo System Integration

For cargo floor modules:
- **ULD restraint**: Locks and latches per ULD type
- **Roller systems**: Ball mats or roller trays
- **Restraint nets**: Net attachment fittings
- **Fire protection**: Fire barriers and smoke detection
- **Drainage**: Spill containment and drainage

## Metadata Requirements

Each floor module should include:
- **Part number**: Following 53-10 numbering system
- **Description**: Bay location and type
- **Bay limits**: Start and end frame stations
- **Load rating**: Maximum allowable loads
- **Floor area**: Usable floor area in square meters
- **Material**: Primary materials and finishes
- **Mass properties**: Weight and CG
- **Status**: Design state (draft, released, obsolete)

## Safety and Certification

### Regulatory Requirements
- Comply with CS-25/FAR-25 for floor strength
- Meet emergency evacuation requirements
- Include fire protection per regulations
- Design for survivable crash conditions
- Document compliance in certification reports

### Testing Requirements
- Static load testing of floor beams
- Fatigue testing of critical joints
- Ultimate load testing to failure
- Fire resistance testing of materials
- Certification test reports

## Version Control

- Use Git LFS for large assembly files (> 10 MB)
- Tag design reviews and load test validations
- Document load rating or configuration changes
- Maintain revision history for each bay
- Track seat track or cargo system modifications
