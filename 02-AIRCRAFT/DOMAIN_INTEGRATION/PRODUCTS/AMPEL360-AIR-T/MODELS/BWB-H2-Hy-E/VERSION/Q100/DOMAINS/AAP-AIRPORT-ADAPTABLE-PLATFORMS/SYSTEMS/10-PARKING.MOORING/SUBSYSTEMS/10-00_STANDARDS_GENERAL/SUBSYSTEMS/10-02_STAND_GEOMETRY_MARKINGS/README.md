# Subsystem: 10-02_STAND_GEOMETRY_MARKINGS

## Description

Airport stand geometry definitions and ground marking standards for aircraft positioning.

This subsystem defines the geometric requirements and visual marking standards for airport parking stands. Includes coordinate reference systems, painted markings, lighting positions, and clearance zones required for safe aircraft parking and ground operations.

## Parent System

[10-00_STANDARDS_GENERAL](../../) - Standards and general requirements subsystem.

## PLM Structure

This subsystem contains engineering artifacts organized by CAx discipline:

### Engineering BOM
- [EBOM_LINKS.md](./PLM/EBOM_LINKS.md) - Links to authoritative ERP/PLM items

### CAx Directories

- [CAD/](./PLM/CAx/CAD/) - Computer-Aided Design (3D models, drawings)
- [CAE/](./PLM/CAx/CAE/) - Computer-Aided Engineering (FEA, analysis)
- [CAO/](./PLM/CAx/CAO/) - Computer-Aided Optimization (design optimization)
- [CAM/](./PLM/CAx/CAM/) - Computer-Aided Manufacturing (NC programming, tooling)
- [CAI/](./PLM/CAx/CAI/) - Computer-Aided Installation (installation drawings, procedures)
- [CAV/](./PLM/CAx/CAV/) - Computer-Aided Validation (test models, validation data)
- [CAP/](./PLM/CAx/CAP/) - Computer-Aided Process Planning (process plans, work instructions)
- [CAS/](./PLM/CAx/CAS/) - Computer-Aided Simulation (system simulations)
- [CMP/](./PLM/CAx/CMP/) - Composite Materials Processing (layup data, curing)

## Directory Structure

```
10-02_STAND_GEOMETRY_MARKINGS/
├─ README.md (this file)
└─ PLM/
   ├─ EBOM_LINKS.md
   └─ CAx/
      ├─ CAD/
      ├─ CAE/
      ├─ CAO/
      ├─ CAM/
      ├─ CAI/
      ├─ CAV/
      ├─ CAP/
      ├─ CAS/
      └─ CMP/
```

## Working with This Subsystem

### Adding Engineering Artifacts
1. Place files in appropriate CAx subdirectory based on discipline
2. Use neutral formats (STEP, JT, glTF) alongside native where possible
3. Update `PLM/EBOM_LINKS.md` with ERP/PLM references
4. Follow naming conventions: `{PART_ID}_{DESCRIPTION}_{REV}.{ext}`

### BOM Management
Update [PLM/EBOM_LINKS.md](./PLM/EBOM_LINKS.md) with:
- Part numbers and sourcing information
- Links to authoritative PLM/ERP systems
- Configuration control references
- Supplier information

### File Formats
- **CAD**: STEP, JT, native CAD formats
- **CAE**: Nastran, ANSYS, solver input/output
- **CAM**: CNC programs, tooling definitions
- **Documents**: PDF for controlled documents

## Key Design Considerations

- Stand geometry compatible with BWB-H2-Hy-E aircraft dimensions
- Visual marking standards (colors, dimensions, materials)
- Coordinate reference system alignment with airport datum
- Clearance zones for wingtips, engines, and ground equipment
- Lighting requirements for night operations

## Navigation

- [⬆️ Back to 10-00_STANDARDS_GENERAL](../../)
- [📂 All Standards Subsystems](../)
- [🏠 SYSTEMS Home](../../../../../)

## References

- Parent Subsystem: [10-00_STANDARDS_GENERAL](../../README.md)
- Validation: `scripts/validate-structure.sh`

---

**Status**: Ready for engineering artifact population  
**Owner**: TBD - Assign subsystem engineer  
**Last Updated**: 2025-10-11
