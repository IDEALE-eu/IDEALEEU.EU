# Subsystem: 10-00_STANDARDS_GENERAL

## Description

General standards and requirements for airport parking and mooring operations.

This subsystem contains cross-cutting standards, taxonomy definitions, safety requirements, and test methods that apply to all parking and mooring subsystems. Organized into specialized sub-subsystems for different aspects of standardization.

## Parent System

[10-PARKING.MOORING](../../) - Airport Adaptable Platforms parking and mooring system.

## Sub-Subsystems

This subsystem contains nested sub-subsystems organized by standards domain:

### Standards Organization

- [10-01_TAXONOMY_DEFS/](./SUBSYSTEMS/10-01_TAXONOMY_DEFS/) - Taxonomy definitions and nomenclature standards
- [10-02_STAND_GEOMETRY_MARKINGS/](./SUBSYSTEMS/10-02_STAND_GEOMETRY_MARKINGS/) - Stand geometry and ground marking standards
- [10-03_SAFETY_PERMITS_ESD_ATEX/](./SUBSYSTEMS/10-03_SAFETY_PERMITS_ESD_ATEX/) - Safety permits and hazardous area classifications
- [10-04_TEST_METHODS_QUAL/](./SUBSYSTEMS/10-04_TEST_METHODS_QUAL/) - Test methods and qualification standards

## Directory Structure

```
10-00_STANDARDS_GENERAL/
├─ README.md (this file)
├─ PLM/
│  └─ EBOM_LINKS.md
└─ SUBSYSTEMS/
   ├─ 10-01_TAXONOMY_DEFS/
   │  ├─ README.md
   │  └─ PLM/CAx/{CAD,CAE,CAO,CAI,CAM,CAV,CAP,CAS,CMP}/
   ├─ 10-02_STAND_GEOMETRY_MARKINGS/
   │  ├─ README.md
   │  └─ PLM/CAx/{CAD,CAE,CAO,CAI,CAM,CAV,CAP,CAS,CMP}/
   ├─ 10-03_SAFETY_PERMITS_ESD_ATEX/
   │  ├─ README.md
   │  └─ PLM/CAx/{CAD,CAE,CAO,CAI,CAM,CAV,CAP,CAS,CMP}/
   └─ 10-04_TEST_METHODS_QUAL/
      ├─ README.md
      └─ PLM/CAx/{CAD,CAE,CAO,CAI,CAM,CAV,CAP,CAS,CMP}/
```

## Key Design Considerations

- Cross-cutting standards applicable to all mooring subsystems
- Taxonomy alignment with ATA 100 and airport standards
- Safety requirements for hydrogen refueling operations
- Test and qualification procedures

## Navigation

- [⬆️ Back to 10-PARKING.MOORING](../../)
- [📋 System Integration View](../../INTEGRATION_VIEW.md)
- [🔗 System Interfaces](../../INTERFACE_MATRIX/)
- [📂 All Subsystems](../)
- [🏠 SYSTEMS Home](../../../)

## References

- Parent System: [10-PARKING.MOORING](../../README.md)
- Interface Matrix: [../../INTERFACE_MATRIX/](../../INTERFACE_MATRIX/)
- Validation: `scripts/validate-structure.sh`

---

**Status**: Ready for engineering artifact population  
**Owner**: TBD - Assign subsystem engineer  
**Last Updated**: 2025-10-11
