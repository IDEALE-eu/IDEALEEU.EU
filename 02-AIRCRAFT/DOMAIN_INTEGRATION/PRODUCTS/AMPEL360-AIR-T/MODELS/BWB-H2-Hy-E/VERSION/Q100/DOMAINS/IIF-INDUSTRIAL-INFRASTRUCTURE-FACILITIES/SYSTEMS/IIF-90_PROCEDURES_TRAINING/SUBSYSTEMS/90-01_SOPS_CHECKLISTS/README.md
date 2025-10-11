# Subsystem: 90-01_SOPS_CHECKLISTS

## Description

Standard Operating Procedures (SOPs) and checklists for all IIF equipment operations.

This subsystem contains comprehensive operating procedures, pre-operation checklists, safety checklists, and emergency procedures for all lifting, shoring, and ground support equipment.

## Parent System

[IIF-90_PROCEDURES_TRAINING](../../) - Procedures and Training system.

## PLM Structure

This subsystem contains engineering artifacts organized by CAx discipline:

### Engineering BOM
- [EBOM_LINKS.md](./PLM/EBOM_LINKS.md) - Links to authoritative ERP/PLM items

### CAx Directories

- [CAD/](./PLM/CAx/CAD/) - Computer-Aided Design (procedure diagrams, illustrations)
- [CAE/](./PLM/CAx/CAE/) - Computer-Aided Engineering (procedure validation)
- [CAO/](./PLM/CAx/CAO/) - Computer-Aided Optimization (workflow optimization)
- [CAM/](./PLM/CAx/CAM/) - Computer-Aided Manufacturing (procedure templates)
- [CAI/](./PLM/CAx/CAI/) - Computer-Aided Installation (installation procedures)
- [CAV/](./PLM/CAx/CAV/) - Computer-Aided Validation (procedure validation data)
- [CAP/](./PLM/CAx/CAP/) - Computer-Aided Process Planning (process flows)
- [CAS/](./PLM/CAx/CAS/) - Computer-Aided Simulation (procedure simulations)
- [CMP/](./PLM/CAx/CMP/) - Composite Materials Processing (documentation)

## Directory Structure

```
90-01_SOPS_CHECKLISTS/
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
2. Use PDF for controlled procedure documents
3. Update `PLM/EBOM_LINKS.md` with ERP/PLM references
4. Follow naming conventions: `{PROC_ID}_{DESCRIPTION}_{REV}.{ext}`

### BOM Management
Update [PLM/EBOM_LINKS.md](./PLM/EBOM_LINKS.md) with:
- Document numbers and revision information
- Links to authoritative PLM/ERP systems
- Configuration control references
- Approval and validation status

### File Formats
- **PDF**: Controlled procedure documents
- **DOCX**: Working procedure drafts
- **PPTX**: Training presentations
- **Videos**: Procedure demonstrations

## Key Design Considerations

- Regulatory compliance (OSHA, EN standards)
- Clear and unambiguous language
- Visual aids and illustrations
- Safety warnings and cautions
- Prerequisites and required resources
- Quality checkpoints and verification steps

## Navigation

- [⬆️ Back to IIF-90_PROCEDURES_TRAINING](../../)
- [📋 System Integration View](../../INTEGRATION_VIEW.md)
- [🔗 System Interfaces](../../INTERFACE_MATRIX/)
- [📂 All Subsystems](../)
- [🏠 SYSTEMS Home](../../../)

## References

- Parent System: [IIF-90_PROCEDURES_TRAINING](../../README.md)
- Interface Matrix: [../../INTERFACE_MATRIX/](../../INTERFACE_MATRIX/)
- Validation: `scripts/validate-structure.sh`

---

**Status**: Ready for engineering artifact population  
**Owner**: TBD - Assign subsystem engineer  
**Last Updated**: 2025-10-11
