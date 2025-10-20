# PERIMETER_PROFILES

This directory contains shared geometry profiles and sketches used across multiple bulkhead modules in the center body assembly.

## Contents

### Curve Files (.curve)
- **FUSELAGE_FS350.curve**: Perimeter curve for Fuselage Station 350
  - Curvature Radius: 1385 mm
  - Used by: BH-STA350_FWD_PRESSURE

### Sketch Files (.sketch)
- **FRAME_10HOLE.sketch**: Frame interface sketch with 10 holes
  - Hole Count: 10
  - Hole Diameter: 6.35 mm (standard fastener size)
  - Pattern: Radial, equally spaced
  - Used by: BH-STA350_FWD_PRESSURE

## Usage

These files are imported by CAD assemblies as reference geometry. They define:
- Cross-sectional shapes at specific fuselage stations
- Standard hole patterns for frame interfaces
- Attachment points for structural connections

## File Format

The files use a pseudo-CAD format with:
- Comments starting with `!`
- Parameter definitions
- Point/coordinate data
- Reference to coordinate systems and datums

## Maintenance

When updating these files:
1. Verify compatibility with all assemblies that reference them
2. Update version information in the file header
3. Document changes in the assembly CHANGELOG.md files
4. Run validation checks to ensure geometry integrity

## Related Files

- Parameter tables: `../<BULKHEAD>/53-10-BH-STA###_MASTER_ASM.asm.csv`
- Configuration: `../<BULKHEAD>/BH-STA###.yaml`
- Validation: `../<BULKHEAD>/modelcheck.yml`
