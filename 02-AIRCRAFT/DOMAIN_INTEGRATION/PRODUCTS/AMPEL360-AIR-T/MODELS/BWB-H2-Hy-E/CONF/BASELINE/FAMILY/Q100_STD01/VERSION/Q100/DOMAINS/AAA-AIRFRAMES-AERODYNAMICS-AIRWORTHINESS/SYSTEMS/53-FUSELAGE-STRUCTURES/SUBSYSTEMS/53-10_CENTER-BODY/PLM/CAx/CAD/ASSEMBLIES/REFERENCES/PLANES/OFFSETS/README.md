# OFFSETS — Offset Reference Planes

## Purpose

This directory contains CAD models of offset reference planes used for tolerance zones, inspection surfaces, and manufacturing allowances for the 53-10 Center Body structures.

## Contents

### PLUS_5/ — Positive 5mm Offset Planes
- **Description**: Reference planes offset +5mm from nominal surfaces
- **Direction**: Outward from structure (material side)
- **Applications**:
  - Outer mold line (OML) inspection tolerance zone
  - Positive thickness variation allowance
  - Clearance envelope definition
  - Tool clearance verification
- **Typical Usage**:
  - Maximum material condition check
  - Assembly clearance verification
  - Aerodynamic envelope validation

### MINUS_5/ — Negative 5mm Offset Planes
- **Description**: Reference planes offset -5mm from nominal surfaces
- **Direction**: Inward from structure (space side)
- **Applications**:
  - Inner mold line (IML) inspection tolerance zone
  - Negative thickness variation allowance
  - Minimum material condition
  - Interference checking
- **Typical Usage**:
  - Minimum material condition check
  - Equipment clearance verification
  - Internal volume validation

### CUSTOM/ — Custom Offset Planes
- **Description**: Reference planes with non-standard offset distances
- **Applications**:
  - Special tolerance zones
  - Customer-specific requirements
  - Unusual clearance requirements
  - Non-uniform offset surfaces
- **Typical Values**:
  - ±1mm: High-precision areas
  - ±10mm: Large clearance zones
  - ±20mm: Major structural variations
  - Variable offsets: Tapered or complex geometries

## Offset Plane Types

### Surface Offset Planes

1. **OML (Outer Mold Line) Offsets**
   - Nominal OML
   - OML + tolerance
   - OML - tolerance
   - Aerodynamic smoothness zones

2. **IML (Inner Mold Line) Offsets**
   - Nominal IML
   - IML + tolerance
   - IML - tolerance
   - Equipment clearance zones

3. **Structural Offsets**
   - Frame web centerline ± offset
   - Stringer cap edges ± offset
   - Skin thickness zones
   - Fastener grip length zones

### Station Offset Planes

1. **Longitudinal Offsets (FS)**
   - Forward stations: FS ± offset
   - Aft stations: FS ± offset
   - Tolerance zones for station locations

2. **Vertical Offsets (WL)**
   - Upper waterlines: WL ± offset
   - Lower waterlines: WL ± offset
   - Height tolerance zones

3. **Lateral Offsets (BL)**
   - Port buttock lines: BL ± offset
   - Starboard buttock lines: BL ± offset
   - Width tolerance zones

## Offset Specifications

### Standard Offset Values

| Zone Type | Offset Value | Application |
|-----------|-------------|-------------|
| Precision | ±1mm | Critical interfaces, seals |
| Standard | ±5mm | General structure, typical tolerance |
| Clearance | ±10mm | Equipment installation, access |
| Major | ±20mm | Large assemblies, major variations |

### Tolerance Zone Definition

For each critical surface:
1. Define nominal surface
2. Specify positive tolerance (maximum)
3. Specify negative tolerance (minimum)
4. Create offset planes at tolerance limits
5. Document inspection requirements

## Usage Applications

### Design Verification

- **Maximum Material Condition**: Check using positive offset
- **Minimum Material Condition**: Check using negative offset
- **Clearance Analysis**: Verify gaps using offset envelopes
- **Tolerance Stack-up**: Analyze cumulative effects

### Manufacturing

- **Tool Design**: Define tool clearances using offset planes
- **Trim Lines**: Establish cut planes with offset allowances
- **Inspection**: Set up CMM measurement zones
- **Rework Limits**: Define acceptable repair boundaries

### Quality Control

- **Inspection Zones**: Define acceptable part envelope
- **GD&T Verification**: Check form and position tolerances
- **First Article**: Validate dimensional compliance
- **In-Process**: Monitor manufacturing variations

### Assembly

- **Fit Check**: Verify component mating with offset models
- **Shimming**: Determine shim requirements from offset analysis
- **Gap Control**: Maintain gaps within offset limits
- **Interface Verification**: Check mating surfaces align

## Naming Convention

Use the following pattern:
```
53-10_OFFSET_<base-plane>_<direction><value>_<version>.<ext>
```

Examples:
- `53-10_OFFSET_OML_PLUS_5_v01.CATPart`
- `53-10_OFFSET_IML_MINUS_5_v01.prt`
- `53-10_OFFSET_FS-1200_PLUS_10_v01.sldprt`
- `53-10_OFFSET_CUSTOM_WING_ROOT_v01.CATPart`

## Documentation Requirements

Each offset plane should document:
- Base reference plane or surface
- Offset distance and direction
- Tolerance specification
- Applicable zone or region
- Inspection requirements
- Design intent/purpose

## Inspection Planning

### CMM Measurement

1. **Setup**: Use offset planes to define measurement zones
2. **Scanning**: Program inspection paths along offset surfaces
3. **Comparison**: Compare measured data to offset tolerance zone
4. **Reporting**: Document deviations from nominal and limits

### Optical Scanning

1. **Capture**: 3D scan actual part surfaces
2. **Alignment**: Register scan data to CAD model
3. **Comparison**: Generate deviation map against offset planes
4. **Validation**: Verify all points within tolerance envelope

## Standards Compliance

Follow:
- **ASME Y14.5**: Geometric dimensioning and tolerancing
- **ISO 1101**: Geometrical tolerancing - Tolerances of form, orientation, location
- **ISO 2768**: General tolerances
- **AS9102**: First article inspection requirements

## Related Directories

- **Nominal planes**: [`../STATIONS/`](../STATIONS/), [`../GLOBAL/`](../GLOBAL/)
- **Validation tools**: [`../VALIDATION/`](../VALIDATION/)
- **Templates**: [`../TEMPLATES/`](../TEMPLATES/)
- **Inspection procedures**: [`../../../../../CAV/PROCEDURES/`](../../../../../CAV/PROCEDURES/)
