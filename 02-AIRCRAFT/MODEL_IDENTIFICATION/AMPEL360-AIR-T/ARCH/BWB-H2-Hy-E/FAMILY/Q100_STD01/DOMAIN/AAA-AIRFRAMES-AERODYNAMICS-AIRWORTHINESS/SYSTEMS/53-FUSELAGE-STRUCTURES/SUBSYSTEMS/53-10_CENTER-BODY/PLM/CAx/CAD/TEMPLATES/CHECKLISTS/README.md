# CHECKLISTS — Design and Release Checklists

## Purpose

Quality assurance checklists for CAD design, review, and release processes for the 53-10 Center Body project.

## Checklist Categories

### Design Checklists
- Part modeling checklist
- Assembly design checklist
- Drawing creation checklist
- Model validation checklist

### Review Checklists
- Design review checklist
- Peer review checklist
- Interface review checklist
- Tolerance analysis checklist

### Release Checklists
- Pre-release checklist
- Export validation checklist
- Documentation completeness checklist
- Archive and backup checklist

## Part Modeling Checklist

### File Setup
- [ ] Part created from approved seed file/template
- [ ] File named per naming convention (see `../NAMING_CONVENTIONS/`)
- [ ] Part number assigned correctly
- [ ] Units set to millimeters (mm)
- [ ] Coordinate system matches aircraft reference frame (FS, BL, WL)

### Geometry
- [ ] All features properly constrained (fully defined)
- [ ] No failed or suppressed features (unless intentional)
- [ ] No unintended overlapping or interfering geometry
- [ ] Minimum bend radii met for sheet metal parts (2t for Al 2024-T3)
- [ ] Edge distances for holes meet requirements (≥ 2D from edge)
- [ ] Chamfers/fillets applied to sharp edges (0.5mm typical)

### Properties and Metadata
- [ ] Material assigned from approved library
- [ ] Mass properties calculated and reasonable
- [ ] Custom properties completed (part number, description, revision, author)
- [ ] Part description is clear and accurate
- [ ] Revision level set correctly (default: A)

### Parameters and Features
- [ ] Key dimensions controlled by parameters
- [ ] Features named descriptively (not "Extrude1", "Cut2", etc.)
- [ ] Design intent documented in feature comments or notes
- [ ] Feature tree organized logically (grouped if applicable)
- [ ] Reference geometry on appropriate layers/sets

### Standards Compliance
- [ ] Design follows company modeling standards
- [ ] Manufacturing constraints considered (tool access, tolerances)
- [ ] No proprietary features that break interoperability
- [ ] Model validates without errors

## Assembly Design Checklist

### Structure
- [ ] Assembly created from approved seed file/template
- [ ] File named per naming convention
- [ ] Assembly structure logical and hierarchical
- [ ] Sub-assemblies used appropriately (not flat BOM)
- [ ] Skeleton or master model used for top-down design (if applicable)

### Components
- [ ] All components load without errors
- [ ] No missing references or suppressed components (unless intentional)
- [ ] Component instances positioned correctly
- [ ] Configurations/variants defined appropriately (LEFT/RIGHT, etc.)
- [ ] Standard parts (fasteners) from approved libraries

### Constraints and Mates
- [ ] All components properly constrained (not under-defined)
- [ ] No over-constrained assemblies (conflicts)
- [ ] Interface datums aligned correctly (FS, BL, WL stations)
- [ ] Clearances verified (no unintended interferences)
- [ ] Assembly updates without errors

### Properties and BOM
- [ ] Assembly properties completed (assembly number, description, revision)
- [ ] BOM structure correct (hierarchical or flattened as needed)
- [ ] Quantities correct for all components
- [ ] Standard parts included in BOM
- [ ] Mass properties calculated and reasonable

### Performance
- [ ] Large assemblies use simplified representations or LOD
- [ ] Lightweight mode enabled for external components (if applicable)
- [ ] Assembly loads and updates in reasonable time (< 5 min for large)

## Drawing Creation Checklist

### Setup
- [ ] Drawing created from approved template
- [ ] Sheet size appropriate for content (A4, A3, A1, etc.)
- [ ] Title block completed (part number, description, scale, etc.)
- [ ] Border and zone markers visible
- [ ] Drawing file named per convention

### Views
- [ ] Minimum necessary views included (front, top, right, sections)
- [ ] Views properly scaled and positioned
- [ ] Hidden lines appropriate (visible, hidden, or removed)
- [ ] Section views clearly labeled (A-A, B-B, etc.)
- [ ] Detail views for complex features
- [ ] Isometric or pictorial view for complex parts

### Dimensions
- [ ] All critical dimensions shown
- [ ] Dimensions reference datum features (GD&T best practice)
- [ ] Dimension style consistent (ISO or ASME)
- [ ] Tolerances specified where required
- [ ] No duplicate or redundant dimensions
- [ ] Dimensions not crowded (readable when printed)

### Annotations
- [ ] GD&T callouts per ASME Y14.5 or ISO 1101
- [ ] Datum reference frame clearly defined
- [ ] Surface finish symbols applied where needed
- [ ] Material specified in title block or notes
- [ ] General notes included (see `../DRAWING/NOTES/`)
- [ ] Welding symbols (if applicable) per AWS A2.4

### Quality
- [ ] Spelling and grammar checked
- [ ] No conflicting or ambiguous dimensions
- [ ] Drawing validates without errors
- [ ] Views update correctly when model changes
- [ ] Drawing prints legibly at intended size

## Design Review Checklist

### Pre-Review Preparation
- [ ] Design is complete and stable (no WIP features)
- [ ] Models validate without errors
- [ ] Mass properties calculated
- [ ] Drawings created and checked
- [ ] Design documentation prepared (design rationale, calculations)
- [ ] Interface definitions confirmed

### Review Meeting
- [ ] Design intent explained clearly
- [ ] Critical features and constraints discussed
- [ ] Interface requirements verified
- [ ] Manufacturing considerations reviewed
- [ ] Assembly sequence feasible
- [ ] Maintenance access confirmed
- [ ] Action items documented

### Post-Review Actions
- [ ] Review comments addressed
- [ ] Models updated per action items
- [ ] Re-review scheduled if major changes
- [ ] Review sign-off obtained
- [ ] Design frozen or approved for next phase

## Pre-Release Checklist

### Model Validation
- [ ] All parts/assemblies validate without errors
- [ ] No missing references or broken links
- [ ] Mass properties up-to-date and reasonable
- [ ] All configurations tested (LEFT, RIGHT, variants)
- [ ] Interference check passed (clearances verified)

### Documentation
- [ ] Drawings completed and checked
- [ ] BOM generated and validated
- [ ] Material specifications documented
- [ ] Design analysis completed (stress, tolerance, etc.)
- [ ] Interface control documents (ICD) updated
- [ ] Manufacturing notes and instructions prepared

### Properties and Metadata
- [ ] All custom properties completed
- [ ] Revision level set correctly
- [ ] Approval signatures obtained
- [ ] Change documentation (ECR/ECO) linked
- [ ] Traceability to requirements verified

### Export and Data Exchange
- [ ] STEP AP242 exports generated and validated
- [ ] PDF drawings exported
- [ ] Neutral formats tested (IGES if required)
- [ ] File naming per convention
- [ ] Export checksums calculated (SHA-256)

### Archive and Backup
- [ ] Native CAD files archived
- [ ] Neutral format exports archived
- [ ] Drawings (PDF) archived
- [ ] Documentation archived
- [ ] Backup to secondary location
- [ ] Release package created

## Export Validation Checklist

### Pre-Export
- [ ] Native CAD model validates without errors
- [ ] Properties and metadata up-to-date
- [ ] Appropriate configuration/variant selected
- [ ] Export settings configured per standards (see `../EXPORT/`)

### Post-Export (STEP)
- [ ] STEP file opens without errors in viewer
- [ ] Geometry complete (no missing faces/edges)
- [ ] Assembly structure preserved (if assembly)
- [ ] Units correct (mm)
- [ ] PMI/annotations included (if applicable)
- [ ] Properties exported correctly
- [ ] File size reasonable (not corrupted)

### Post-Export (IGES)
- [ ] IGES file opens without errors
- [ ] Surfaces trimmed correctly
- [ ] Solids exported as BREP (if applicable)
- [ ] No gaps or overlaps in geometry

### Post-Export (DXF)
- [ ] DXF file opens in viewer/CAD system
- [ ] 2D geometry complete and accurate
- [ ] Layers organized correctly
- [ ] Dimensions readable (if included)
- [ ] Scale is 1:1 (full size)

### Validation Testing
- [ ] Import exported file into receiving CAD system
- [ ] Measure known dimensions (spot check)
- [ ] Verify geometry integrity
- [ ] Confirm no data loss or corruption

## Related Directories

- **Naming Conventions**: [`../NAMING_CONVENTIONS/`](../NAMING_CONVENTIONS/) — File naming rules
- **Properties**: [`../PROPERTIES/`](../PROPERTIES/) — Metadata standards
- **Export**: [`../EXPORT/`](../EXPORT/) — Export format standards
- **Drawing**: [`../DRAWING/`](../DRAWING/) — Drawing templates and standards
- **BOM**: [`../BOM/`](../BOM/) — BOM structure and requirements

## References

- Main templates documentation: [`../README.md`](../README.md)
- Quality management system (QMS) procedures
- AS9100 quality standards
- Company design review process
- Configuration management: [`/00-PROGRAM/CONFIG_MGMT/`](/00-PROGRAM/CONFIG_MGMT/)
