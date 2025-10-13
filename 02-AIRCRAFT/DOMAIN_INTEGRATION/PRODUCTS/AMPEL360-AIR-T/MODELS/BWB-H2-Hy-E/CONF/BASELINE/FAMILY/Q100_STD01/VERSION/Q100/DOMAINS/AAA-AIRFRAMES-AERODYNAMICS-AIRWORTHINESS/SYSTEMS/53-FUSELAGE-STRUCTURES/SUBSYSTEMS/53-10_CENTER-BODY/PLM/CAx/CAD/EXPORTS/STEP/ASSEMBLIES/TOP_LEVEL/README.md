# TOP_LEVEL — Complete Assembly Files

## Purpose

This directory contains **top-level assembly files** representing the complete center body structure (53-10) as a single integrated assembly with all sub-assemblies and parts.

## What to Store

- **Master assembly**: Complete 53-10 Center Body assembly
- **Integration assemblies**: Full system-level integrations
- **Configuration variants**: Different design configurations
- **As-designed models**: Complete product structure as designed
- **Interface demonstrations**: Full assembly with mating systems

## File Naming Convention

Follow the standard naming pattern:
```
<subsystem>_ASM_<assembly-name>_<part-number>_<revision>_<date>.step
```

Example:
```
53-10_ASM_CENTER-BODY_PN-10000_RevA_20250110.step
```

## Assembly Structure

Top-level assemblies should include:
- Complete hierarchical product structure
- All sub-assemblies with proper placement
- All individual parts with transformations
- Assembly constraints (optional)
- Configuration metadata
- BOM data and effectivity

## Export Guidelines

When exporting top-level assemblies:
- ✅ Use **STEP AP242** for full assembly structure
- ✅ Include complete product hierarchy
- ✅ Export part instances with transformations
- ✅ Include component names and part numbers
- ✅ Preserve assembly tree structure
- ✅ Include metadata and attributes

## Related Directories

- [**../SUB_ASSEMBLIES/**](../SUB_ASSEMBLIES/) — Component sub-assemblies
- [**../../PARTS/**](../../PARTS/) — Individual part files
- [**../../INSTALLATION/INTERFACES/**](../../INSTALLATION/INTERFACES/) — Interface definitions
- [**../../REVISIONS/RELEASED/**](../../REVISIONS/RELEASED/) — Released versions
- [**../../INDEX/**](../../INDEX/) — Assembly catalogs and BOMs

## Configuration Management

- Coordinate with [**../../REVISIONS/**](../../REVISIONS/) for version control
- Cross-reference with BOM in [**../../INDEX/**](../../INDEX/)
- Link to interface definitions in [**../../INSTALLATION/INTERFACES/**](../../INSTALLATION/INTERFACES/)

## Validation

Before committing assembly files:
- [ ] Complete product structure present
- [ ] All components load without errors
- [ ] Transformations and placements correct
- [ ] Part numbers and metadata complete
- [ ] Assembly tree hierarchy logical
- [ ] File size reasonable (< 500 MB)

## References

- Parent directory: [**../**](../)
- Main STEP README: [**../../README.md**](../../README.md)
- Assembly standards: `00-PROGRAM/STANDARDS/04-CROSS_CUTTING/DATA_EXCHANGE/`
