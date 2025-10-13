# CAD - Computer-Aided Design

[↑ Up to 10-02_STAND_GEOMETRY_MARKINGS](../../../README.md)

Computer-Aided Design artifacts for airport stand geometry and ground marking standards.

## Purpose

Stores 3D models, drawings, and design documentation supporting airport stand geometry and ground marking standards development, visualization, and implementation.

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

- Airport stand layout drawings
- Ground marking pattern models
- Coordinate reference system definitions
- Clearance zone visualizations
- Lighting position models

## Naming Convention

```
10-02_{ITEM_TYPE}_{DESCRIPTION}_v{VER}.{ext}
```

Examples:
- `10-02_MODEL_StandLayout_v001.step`
- `10-02_DRAWING_MarkingPattern_v002.dwg`

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
