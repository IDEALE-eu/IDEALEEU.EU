# SYMMETRY — Symmetry Reference Planes

## Purpose

This directory contains CAD models of symmetry reference planes used for symmetric design, analysis, and manufacturing of the 53-10 Center Body. These planes enable efficient modeling by exploiting geometric symmetry.

## Primary Symmetry Plane

### Fuselage Centerline (BL0)
- **Description**: Primary aircraft symmetry plane
- **Definition**: Vertical plane containing X-axis and Z-axis
- **Location**: Buttock Line 0 (BL0)
- **Normal Direction**: Y-axis (lateral)
- **Extent**: Full length of center body

## Symmetry Types

### Full Symmetry
- **Application**: Symmetric structures modeled on one side only
- **Usage**: 
  - Fuselage skin panels (left/right mirror)
  - Symmetric frame structures
  - Internal layout with no lateral asymmetry
  - Load cases with symmetric loading
- **CAD Technique**: Mirror feature or assembly pattern
- **Benefits**: 50% reduction in modeling effort, automatic consistency

### Partial Symmetry
- **Application**: Mostly symmetric with local asymmetric features
- **Usage**:
  - Doors on one side only
  - Asymmetric equipment installations
  - Service access panels
  - Emergency exits
- **CAD Technique**: Base symmetric model with asymmetric features added
- **Benefits**: Efficient modeling while accommodating real design

### Asymmetric Features
Features that break symmetry:
- Passenger door locations
- Cargo door locations (if on one side)
- Emergency exits (may differ left/right)
- Galley installations
- Lavatory locations
- Flight attendant seats
- Systems equipment (if asymmetrically located)

## Symmetry Modeling Approach

### For Symmetric Designs

1. **Model Half Structure**
   - Model right side (starboard) as primary
   - Use symmetry plane (BL0) as boundary
   - Include all features present on both sides

2. **Apply Symmetry**
   - Mirror about BL0 plane
   - Create mirrored assembly or part
   - Verify no interference at centerline

3. **Add Asymmetric Features**
   - Add left-side-only or right-side-only features
   - Document asymmetry in design notes
   - Update BOM to reflect actual quantities

### For Analysis Models

1. **Symmetric Boundary Conditions**
   - Apply symmetry constraints at BL0
   - Constrain lateral (Y) displacement to zero
   - Allow rotation about Y-axis to remain free
   - Prevent penetration across symmetry plane

2. **Symmetric Loading**
   - Apply half of total load to symmetric model
   - Ensure load distribution is symmetric
   - Verify reaction forces are symmetric

3. **Asymmetric Loading**
   - Model full structure (both sides)
   - Apply actual asymmetric loads
   - Cannot use symmetry boundary conditions

## File Contents

### Symmetry Plane Models
- `53-10_SYMMETRY_BL0_PRIMARY.CATPart`: Main symmetry plane
- `53-10_SYMMETRY_BL0_EXTENDED.prt`: Extended symmetry plane for larger models

### Symmetry Check Models
- `53-10_SYMMETRY_CHECK_FRAME.CATPart`: Frame symmetry verification
- `53-10_SYMMETRY_CHECK_SKIN.CATPart`: Skin symmetry verification

### Symmetry Templates
- `53-10_SYMMETRY_TEMPLATE_HALF.CATPart`: Template for half-model approach
- `53-10_SYMMETRY_TEMPLATE_FULL.CATPart`: Template for full-model approach

## Naming Convention

Use the following pattern:
```
53-10_SYMMETRY_<description>_<version>.<ext>
```

Examples:
- `53-10_SYMMETRY_BL0_PRIMARY_v01.CATPart`
- `53-10_SYMMETRY_CHECK_v01.prt`
- `53-10_SYMMETRY_BOUNDARY_v01.sldprt`

## Usage Guidelines

### Design Phase
- Establish symmetry plane early in design
- Plan symmetric features first
- Document asymmetric features explicitly
- Verify symmetry with check models

### Analysis Phase
- Use half-model for symmetric load cases
- Use full-model for asymmetric load cases
- Apply appropriate boundary conditions
- Verify results show expected symmetry

### Manufacturing Phase
- Mirror drawings for left/right parts
- Note handed/mirrored callouts clearly
- Verify tooling accommodates both sides
- Inspect both sides independently

### Documentation Phase
- Call out symmetric features in notes
- Identify asymmetric exceptions
- Show symmetry plane on drawings
- Reference BL0 consistently

## Quality Checks

### Symmetry Verification

1. **Geometric Check**
   - Measure distances from centerline
   - Verify left/right dimensions match
   - Check for unintended asymmetry
   - Validate mirror consistency

2. **Mass Properties Check**
   - Calculate half-model mass and CG
   - Verify doubled mass equals full model
   - Check CG is on or near centerline
   - Validate moment of inertia symmetry

3. **Interface Check**
   - Verify centerline components fit properly
   - Check for gaps or interference
   - Validate fastener patterns are symmetric
   - Ensure symmetric load transfer

## Asymmetry Documentation

For asymmetric features, document:
- Location and extent of asymmetry
- Reason for asymmetry (functional requirement)
- Impact on mass and CG location
- Load path implications
- Manufacturing considerations

## Standards Compliance

Follow:
- **ATA iSpec 2200**: Aircraft symmetry conventions
- **ISO 10303 (STEP)**: Symmetric feature representation
- **ASME Y14.5**: Datum reference frames
- **Company design standards**: Symmetry modeling practices

## Related Directories

- **Global planes**: [`../GLOBAL/`](../GLOBAL/)
- **Station planes**: [`../STATIONS/`](../STATIONS/)
- **Templates**: [`../TEMPLATES/`](../TEMPLATES/)
- **Coordinate systems**: [`../../COORDINATE_SYSTEMS/`](../../COORDINATE_SYSTEMS/)
