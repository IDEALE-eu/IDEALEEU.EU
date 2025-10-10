# PARTS — CAD Part Files by Component Type

## Purpose

This directory organizes individual CAD part files for the 53_00 Structural Body subsystem by component type. It provides a structured classification system for managing the diverse range of structural and detail parts that comprise the spacecraft structural body.

## Naming Convention

Use the following naming pattern for part files:
```
53_00_<component-type>_<part-number>_<description>_<version>.<ext>
```

Examples:
- `53_00_FRAME_F01_FWD_v01.CATPart`
- `53_00_STRINGER_STR-L01_UPPER-LEFT_v02.prt`
- `53_00_SKIN-PANEL_SP-001_OML-FWD_v01.sldprt`
- `53_00_BRACKET_BKT-123_MOUNT-FITTING_v01.prt`

## File Formats

### Native CAD Formats
- **CATIA V5/V6**: `.CATPart`
- **NX (Siemens)**: `.prt`
- **SolidWorks**: `.sldprt`
- **Creo (PTC)**: `.prt`

### Best Practices
- Store parts in appropriate component type directory
- Export to neutral formats in [`../EXPORTS/`](../EXPORTS/)
- Reference assemblies in [`../ASSEMBLIES/`](../ASSEMBLIES/)

## Metadata Requirements

Include the following in part file properties or accompanying metadata:
- **Part number**: Unique identifier per nomenclature system
- **Revision**: Version letter or number
- **Material**: Material specification (e.g., Al 2024-T3, Ti-6Al-4V)
- **Mass**: Calculated mass in kg
- **Finish**: Surface treatment or coating specification
- **Author**: Designer name/ID
- **Date**: Creation/modification date
- **Status**: WIP, Released, Obsolete
- **Notes**: Design intent, special requirements

## Cross-References

### Related CAD Directories
- **Component models**: [`../MODELS/`](../MODELS/) — Alternative model organization
- **Assembly integration**: [`../ASSEMBLIES/`](../ASSEMBLIES/) — Where parts are assembled
- **Engineering drawings**: [`../DRAWINGS/`](../DRAWINGS/) — Manufacturing drawings
- **Neutral exports**: [`../EXPORTS/`](../EXPORTS/) — STEP, IGES, JT formats
- **Design templates**: [`../TEMPLATES/`](../TEMPLATES/) — CAD templates and standards

### PLM and Configuration Management
- **EBOM links**: [`../../EBOM_LINKS.md`](../../EBOM_LINKS.md)
- **Interface definitions**: [`../../CAI/INTERFACES/`](../../CAI/INTERFACES/)
- **Change control**: Reference ECO/ECR in configuration management system

## Quality Standards

All parts must comply with:
- **ECSS-E-ST-10C**: Space engineering standards
- **ECSS-E-ST-32C**: Structural design and verification
- **ISO 10303-242** (STEP AP242): CAD data exchange standard
- **AS9100**: Quality management for aerospace

## Validation Checklist

Before releasing parts:
- [ ] Part opens without errors in native CAD system
- [ ] All features rebuild successfully
- [ ] Material properties assigned
- [ ] Mass properties calculated and documented
- [ ] Design parameters and intent documented
- [ ] Neutral format export verified (STEP)
- [ ] File metadata complete
- [ ] Engineering drawing created (if required)
- [ ] Design review completed
- [ ] ECO approval obtained

## Support

For questions about:
- **Part organization**: Contact PLM Administrator
- **Design standards**: Reference ECSS-E-ST-32C
- **CAD system support**: Contact CAD Administrator
- **Configuration management**: Contact CCB (Configuration Control Board)
