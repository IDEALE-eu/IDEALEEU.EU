# MATES_CONSTRAINTS — Assembly Mates and Constraints

## Purpose

This directory contains documentation and definitions of assembly mates, constraints, and relationships used in the top-level assembly.

## Contents

### Constraint Types
- **Coincident mates**: Aligned faces, edges, or points
- **Concentric mates**: Aligned cylindrical or spherical features
- **Distance mates**: Fixed spacing between components
- **Angle mates**: Angular relationships between components
- **Parallel/Perpendicular**: Orientation constraints
- **Tangent mates**: Tangential relationships

## Documentation

### Mate Definition Files
Document each mate/constraint with:
- **Components involved**: Parts being constrained
- **Constraint type**: Coincident, distance, angle, etc.
- **Reference features**: Faces, edges, points used
- **Values**: Distance, angle, or other parameters
- **Degrees of freedom**: Remaining mobility

## File Formats

- `.txt` — Text-based mate descriptions
- `.csv` — Tabular mate listing
- `.pdf` — Engineering documentation
- Native CAD mate features in assembly files

## Naming Convention

```
53-10_MATES_<assembly>_<version>.<ext>
```

Examples:
- `53-10_MATES_CENTER-BODY_v01.csv`
- `53-10_MATES_WING-INTERFACE_v01.pdf`

## Mate Organization

### By System Interface
- **Wing-to-body mates**: Attachment constraints
- **Floor-to-frame mates**: Internal structure
- **Bulkhead mates**: Pressure bulkhead interfaces
- **Equipment mates**: System installation constraints

### Mate Validation
- **Degrees of freedom**: Verify fully constrained or intentional mobility
- **Over-constraint**: Check for conflicting mates
- **Mate errors**: Resolve failed or suppressed mates
- **Performance**: Optimize mate scheme for rebuild speed

## Best Practices

- Use **reference geometry** for positioning rather than component faces when possible
- Document **critical mates** that define interfaces
- Maintain **mate schemes** consistent across configurations
- Use **mate groups** to organize related constraints

## Related Directories

- **Assembly**: [`../ASM/`](../ASM/) — Assembly files with mate definitions
- **Reference Geometry**: [`../REFERENCE_GEOMETRY/`](../REFERENCE_GEOMETRY/) — Positioning references
- **Interface Control**: [`../DOCS/INTERFACE_CONTROL/`](../DOCS/INTERFACE_CONTROL/) — Interface requirements
