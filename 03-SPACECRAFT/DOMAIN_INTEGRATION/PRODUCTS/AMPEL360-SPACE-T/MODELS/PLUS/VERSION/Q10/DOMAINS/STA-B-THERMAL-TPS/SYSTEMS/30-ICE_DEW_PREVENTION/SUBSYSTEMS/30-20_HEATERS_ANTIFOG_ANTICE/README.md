# Subsystem: 30-20_HEATERS_ANTIFOG_ANTICE

## Description

Anti-fog and anti-ice heating elements and systems

## Parent System

[30-ICE_DEW_PREVENTION](../../) - Ice and dew prevention systems including sensors, heaters, purge systems, coatings, drains, control algorithms, environmental models, and TVAC testing.

## PLM Structure

This subsystem contains engineering artifacts organized by CAx discipline:

### Engineering BOM
- [EBOM_LINKS.md](./PLM/EBOM_LINKS.md) - Links to authoritative ERP/PLM items

### CAx Directories

- [CAD/](./PLM/CAx/CAD/) - Computer-Aided Design (3D models, drawings)
- [CAE/](./PLM/CAx/CAE/) - Computer-Aided Engineering (FEA, thermal analysis)
- [CAM/](./PLM/CAx/CAM/) - Computer-Aided Manufacturing (NC programming, tooling)
- [CAI/](./PLM/CAx/CAI/) - Computer-Aided Integration (integration drawings, procedures)
- [CAV/](./PLM/CAx/CAV/) - Computer-Aided Validation (test models, validation data)
- [CAP/](./PLM/CAx/CAP/) - Computer-Aided Process Planning (process plans, work instructions)
- [CAS/](./PLM/CAx/CAS/) - Computer-Aided Service and Sustainment (maintenance procedures)
- [CMP/](./PLM/CAx/CMP/) - Computer-Aided Compliance and Certification (test evidence, certificates)

## Directory Structure

```
30-20_HEATERS_ANTIFOG_ANTICE/
├─ README.md (this file)
└─ PLM/
   ├─ EBOM_LINKS.md
   └─ CAx/
      ├─ README.md
      ├─ CAD/
      ├─ CAE/
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
- **CAD**: STEP, IGES, native CAD formats
- **CAE**: Analysis input/output, simulation results
- **CAM**: CNC programs, tooling definitions
- **Documents**: PDF for controlled documents

## Navigation

- [⬆️ Back to 30-ICE_DEW_PREVENTION](../../)
- [📋 System Integration View](../../INTEGRATION_VIEW.md)
- [🔗 System Interfaces](../../INTERFACE_MATRIX/)
- [📂 All Subsystems](../)
- [🏠 SYSTEMS Home](../../../)

## References

- Parent System: [30-ICE_DEW_PREVENTION](../../README.md)
- Interface Matrix: [../../INTERFACE_MATRIX/](../../INTERFACE_MATRIX/)
- Validation: `scripts/validate-spacecraft-systems.sh`

---

**Status**: Ready for engineering artifact population  
**Owner**: TBD - Assign subsystem engineer  
**Last Updated**: 2025-10-10
