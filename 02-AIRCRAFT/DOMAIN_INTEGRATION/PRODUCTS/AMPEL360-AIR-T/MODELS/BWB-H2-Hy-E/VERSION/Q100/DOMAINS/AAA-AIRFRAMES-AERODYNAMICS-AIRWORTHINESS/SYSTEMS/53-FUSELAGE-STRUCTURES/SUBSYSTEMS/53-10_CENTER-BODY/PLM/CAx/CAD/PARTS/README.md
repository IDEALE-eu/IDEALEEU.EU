# PARTS — CAD Part Files by Component Type

## Purpose

This directory organizes individual CAD part files for the 53-10 Center Body subsystem by component type and lifecycle status. It provides a structured classification system for managing the diverse range of structural and detail parts that comprise the center body fuselage section.

## Directory Structure

### Component Type Directories

#### Primary Structure
- **[FRAMES/](FRAMES/)** — Fuselage frames and rings providing cross-sectional rigidity
- **[STRINGERS/](STRINGERS/)** — Longitudinal stiffening members
- **[SKIN_PANELS/](SKIN_PANELS/)** — Outer and inner skin panels forming the pressure boundary
- **[FLOORS/](FLOORS/)** — Floor panels and beams for cabin deck structure
- **[BULKHEADS/](BULKHEADS/)** — Pressure and structural bulkheads

#### Interface and Attachment Hardware
- **[INTERFACE_FITTINGS/](INTERFACE_FITTINGS/)** — Interface attachments to adjacent systems (wings, nose, aft sections)
- **[MOUNTS/](MOUNTS/)** — Equipment mounting provisions and brackets
- **[TANK_SUPPORTS/](TANK_SUPPORTS/)** — Hydrogen tank support structures and cradles

#### Detail Parts
- **[BRACKETS_CLIPS/](BRACKETS_CLIPS/)** — Small attachment brackets, clips, and supports
- **[DOOR_SURROUNDS/](DOOR_SURROUNDS/)** — Door frame reinforcements and edge members
- **[WINDOW_BAYS/](WINDOW_BAYS/)** — Window cutout reinforcements and frames
- **[ACCESS_PANELS/](ACCESS_PANELS/)** — Removable access panels and covers
- **[SEALS_GASKETS/](SEALS_GASKETS/)** — Sealing elements and gasket components
- **[INSERTS_DOUBLERS/](INSERTS_DOUBLERS/)** — Reinforcement doublers and threaded inserts
- **[STIFFENERS/](STIFFENERS/)** — Local stiffening elements and reinforcements

#### Standard Components
- **[STANDARD_PARTS/](STANDARD_PARTS/)** — Catalog standard parts (bushings, inserts, hardware)
- **[FASTENERS/](FASTENERS/)** — Bolts, rivets, screws, and fastening hardware

#### Templates and References
- **[TEMPLATES/](TEMPLATES/)** — Part templates, standard features, and design libraries

### Lifecycle Status Directories

- **[WIP/](WIP/)** — Work in progress parts under active development
- **[RELEASED/](RELEASED/)** — Released parts approved for production
- **[OBSOLETE/](OBSOLETE/)** — Superseded or discontinued parts (archived)

## Organization Strategy

### By Component Type
Parts are primarily organized by their functional component type (e.g., FRAMES, STRINGERS) to facilitate:
- Rapid location of similar design elements
- Family-based design approaches
- Component-specific design reviews
- Discipline-focused work packages

### By Lifecycle Status
The WIP, RELEASED, and OBSOLETE directories provide configuration management by:
- Segregating active development from approved designs
- Tracking design maturity and release status
- Archiving superseded parts with traceability

## Naming Convention

Use the following naming pattern for part files:
```
53-10_<component-type>_<part-number>_<description>_<version>.<ext>
```

Examples:
- `53-10_FRAME_F01_FWD_v01.CATPart`
- `53-10_STRINGER_STR-L01_UPPER-LEFT_v02.prt`
- `53-10_SKIN-PANEL_SP-001_OML-FWD_v01.sldprt`
- `53-10_BRACKET_BKT-123_MOUNT-FITTING_v01.prt`

## File Formats

### Native CAD Formats
- **CATIA V5/V6**: `.CATPart`
- **NX (Siemens)**: `.prt`
- **SolidWorks**: `.sldprt`
- **Creo (PTC)**: `.prt`

### Best Practices
- Store parts in appropriate component type directory
- Move parts to RELEASED when approved via ECO/ECR process
- Archive obsolete parts to OBSOLETE with reference to superseding part
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
- **ATA iSpec 2200**: Technical publications data module standards
- **ISO 10303-242** (STEP AP242): CAD data exchange standard
- **AS9100**: Quality management for aerospace
- **Internal design standards**: See `../../../51-STRUCTURES-GENERAL/`

## Usage Guidelines

### For Designers
1. Start designs in appropriate component type directory
2. Use part templates from TEMPLATES/ when available
3. Store active work in WIP/ during development
4. Request release review when design is complete
5. Move to RELEASED/ after approval via ECO

### For Configuration Managers
1. Monitor WIP/ for parts ready for release
2. Verify metadata completeness before release
3. Move approved parts to RELEASED/
4. Archive superseded parts to OBSOLETE/ with traceability

### For Manufacturing Engineers
1. Use RELEASED/ parts only for production
2. Reference drawings in [`../DRAWINGS/`](../DRAWINGS/)
3. Report discrepancies via engineering change process
4. Coordinate with design for manufacturing issues

## Version Control

- Use Git LFS for large binary CAD files (> 10 MB)
- Tag major milestones (PDR, CDR, release baselines)
- Document design changes in commit messages
- Maintain part design history for traceability
- Link commits to ECO/ECR numbers

## Validation Checklist

Before moving parts to RELEASED/:
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
- **Design standards**: Reference `../../../51-STRUCTURES-GENERAL/`
- **CAD system support**: Contact CAD Administrator
- **Configuration management**: Contact CCB (Configuration Control Board)
