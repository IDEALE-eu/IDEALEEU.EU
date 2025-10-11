# CAD - Computer-Aided Design

[↑ Up to 10-01_TAXONOMY_DEFS](../../../README.md)

Computer-Aided Design artifacts for taxonomy definitions and classification standards.

## Purpose

Stores 3D models, drawings, and design documentation supporting taxonomy visualization, classification hierarchies, and standard nomenclature systems for airport parking and mooring equipment.

## Structure

- **MODELS/** - 3D CAD models of standard components and assemblies
- **DRAWINGS/** - Technical drawings and schematics
- **EXPORTS/** - Neutral format exports (STEP, JT, IGES, DXF)
  - **STEP/** - STEP AP242 files for interoperability
  - **JT/** - JT format for visualization
  - **DXF/** - 2D drawings in DXF format
- **TEMPLATES/** - Standard templates and symbols
- **LIBRARIES/** - Reusable component libraries

## Key Artifacts

- Taxonomy visualization models
- Classification diagram drawings
- Standard symbol libraries
- Component catalog models
- Interface definition drawings

## Naming Convention

```
10-01_{ITEM_TYPE}_{DESCRIPTION}_v{VER}.{ext}
```

Examples:
- `10-01_SYMBOL_MooringPoint_v001.dwg`
- `10-01_DIAGRAM_TaxonomyTree_v002.step`

## Standards

- **Units:** Millimeters (mm) for mechanical, degrees for angular
- **Coordinate System:** Airport datum reference (FS/WL/BL)
- **Export Format:** STEP AP242 mandatory for release
- **Neutral Formats:** STEP, JT, glTF alongside native
- **Drawing Standards:** ISO/ATA standards for technical drawings

## File Formats

- **Native:** CATIA V5, NX, SolidWorks, AutoCAD (as applicable)
- **Neutral:** STEP AP242 (primary), JT (visualization), IGES (legacy)
- **2D:** DXF, PDF/A (controlled documents)

## Traceability

All CAD artifacts must:
- Link to EBOM items in [PLM/EBOM_LINKS.md](../EBOM_LINKS.md)
- Reference applicable standards and specifications
- Include revision history and approval status
- Maintain configuration control per CM plan

## References

- [Parent Subsystem README](../../../README.md)
- [EBOM Links](../EBOM_LINKS.md)
- [Configuration Management](../../../../../../../../../../../../../00-PROGRAM/CONFIG_MGMT/)
- [CAD Standards](../../../../../../../../../../../../../00-PROGRAM/STANDARDS/CAD/)

## Related CAx Areas

- [CAE](../CAE/) - Analysis geometry derived from CAD
- [CAM](../CAM/) - Manufacturing from CAD models
- [CAI](../CAI/) - Installation drawings and procedures
- [CAV](../CAV/) - Validation test fixtures

## Version Control

- Use Git LFS for large binary files
- Include README.md per model describing inputs/outputs
- Tag releases with version numbers
- Maintain change logs for major revisions

---

**Status**: Ready for artifact population  
**Owner**: TBD - Assign CAD lead  
**Last Updated**: 2025-10-11
