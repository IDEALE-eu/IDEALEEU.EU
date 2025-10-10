# INDEX — Drawing Index and Master Lists

## Purpose

This directory contains master drawing indices, lists, and tracking databases that provide a comprehensive view of all drawings for the 53-10 Center Body subsystem.

## What to Store

### Index Files
- **Master drawing index**: Complete list of all drawings
- **Drawing registers**: Organized drawing lists by type, zone, or status
- **Drawing trees**: Hierarchical organization of drawing relationships
- **Cross-reference matrices**: Drawing relationships and dependencies

### Tracking Documents
- **Drawing status report**: Current status of all drawings
- **Revision tracking**: Latest revision status for each drawing
- **Release schedule**: Planned drawing release dates
- **Issue tracking**: Outstanding drawing issues and actions

### Reports
- **Drawing statistics**: Counts, status summaries, progress metrics
- **Missing drawing list**: Identified but not yet created drawings
- **Obsolete drawing list**: Superseded or retired drawings
- **Change summary**: Recent changes and revisions

## Master Drawing Index

### Index Content
The master index should include for each drawing:
- **Drawing number**: Unique identifier
- **Drawing title**: Component or assembly description
- **Drawing type**: Part, Assembly, Installation, Detail, ICD
- **Revision**: Current revision letter/number
- **Status**: Draft, Released, Obsolete
- **Date**: Creation or release date
- **Designer**: Responsible engineer/drafter
- **File location**: Path to drawing file
- **Related drawings**: Parent, child, or reference drawings
- **Notes**: Special information or flags

### Index Format Options

#### Spreadsheet (CSV/Excel)
```csv
Drawing Number,Title,Type,Rev,Status,Date,Designer,File Path
53-10_DWG_PART_FRAME-F01_D0001,Frame F01,Part,A,Released,2025-01-15,J.Smith,/PART/53-10_DWG_PART_FRAME-F01_D0001_SH1_RevA.pdf
53-10_DWG_ASM_CENTER-BODY_D1000,Center Body Complete,Assembly,B,Released,2025-02-01,M.Johnson,/ASSEMBLY/53-10_DWG_ASM_CENTER-BODY_D1000_SH1_RevB.pdf
```

#### Markdown Table
```markdown
| Drawing Number | Title | Type | Rev | Status | Date | Designer |
|----------------|-------|------|-----|--------|------|----------|
| D0001 | Frame F01 | Part | A | Released | 2025-01-15 | J. Smith |
| D1000 | Center Body Complete | Assembly | B | Released | 2025-02-01 | M. Johnson |
```

#### JSON Database
```json
{
  "drawings": [
    {
      "number": "D0001",
      "title": "Frame F01",
      "type": "Part",
      "revision": "A",
      "status": "Released",
      "date": "2025-01-15",
      "designer": "J. Smith",
      "path": "/PART/53-10_DWG_PART_FRAME-F01_D0001_SH1_RevA.pdf"
    }
  ]
}
```

## Specialized Indices

### By Drawing Type
- **Part drawing index**: All part drawings
- **Assembly drawing index**: All assembly drawings
- **Installation drawing index**: All installation drawings
- **Detail drawing index**: All detail drawings
- **ICD index**: All interface control drawings/documents

### By Zone
- **FWD zone index**: All forward zone drawings
- **CTR zone index**: All center zone drawings
- **AFT zone index**: All aft zone drawings

### By Status
- **Draft drawing list**: Drawings in development
- **Released drawing list**: Current released drawings
- **Obsolete drawing list**: Superseded drawings

### By Component
- **Frames index**: All frame drawings
- **Stringers index**: All stringer drawings
- **Skin panels index**: All skin panel drawings
- **Fittings index**: All fitting and bracket drawings

## Drawing Tree Structure

### Hierarchical Organization
Show parent-child relationships:
```
53-10_DWG_ASM_CENTER-BODY-COMPLETE_D1000 (Top Assembly)
├── 53-10_DWG_ASM_FWD-ZONE_D1001 (Sub-assembly)
│   ├── 53-10_DWG_PART_FRAME-F01_D0001 (Part)
│   ├── 53-10_DWG_PART_FRAME-F02_D0002 (Part)
│   └── 53-10_DWG_ASM_FWD-SECTION_D1011 (Sub-assembly)
├── 53-10_DWG_ASM_CTR-ZONE_D1002 (Sub-assembly)
│   ├── 53-10_DWG_PART_FRAME-F11_D0011 (Part)
│   └── 53-10_DWG_INST_WING-INTERFACE_D2000 (Installation)
└── 53-10_DWG_ASM_AFT-ZONE_D1003 (Sub-assembly)
    ├── 53-10_DWG_PART_FRAME-F21_D0021 (Part)
    └── 53-10_DWG_PART_FRAME-F22_D0022 (Part)
```

## Cross-Reference Matrix

### Drawing Dependencies
Track which drawings reference other drawings:
- Assembly drawings → Part drawings in BOM
- Installation drawings → Mating part drawings
- Detail drawings → Parent drawings
- ICDs → Related system drawings

### Drawing-to-Model Links
Link drawings to source CAD models:
- Drawing number → Model file name
- Drawing revision → Model version/tag
- Verify consistency

## Status Tracking

### Drawing Status Report
Generate periodic status reports:
- Total number of drawings planned
- Number of drawings completed (by type)
- Number of drawings in draft
- Number of drawings released
- Number of drawings obsolete
- Completion percentage

### Release Schedule
Track planned and actual release dates:
- Drawing number
- Planned release date
- Actual release date
- Status (On schedule, Delayed, Released)
- Blocking issues

## Index Maintenance

### Update Frequency
- **Continuous**: Update as drawings created/revised
- **Weekly**: Generate status reports
- **Monthly**: Comprehensive index review
- **Milestone**: Complete audit before major reviews

### Responsibilities
- **Designer**: Notify index owner of new/revised drawings
- **Configuration management**: Maintain master index
- **Project management**: Use index for status tracking
- **Quality**: Audit index accuracy

### Automated vs. Manual
- **Automated**: Generate indices from CAD system or PLM
- **Manual**: Maintain manually if automated not available
- **Hybrid**: Automated generation, manual validation

## Index Usage

### For Design Teams
- Identify existing drawings
- Find related drawings
- Check drawing status
- Avoid duplicate drawing numbers
- Coordinate drawing releases

### For Manufacturing
- Identify required drawings for production
- Verify latest revisions
- Track drawing availability
- Report missing drawings

### For Configuration Management
- Track all configuration items
- Verify completeness
- Support audits
- Manage baselines
- Control changes

### For Management
- Monitor progress
- Identify bottlenecks
- Plan resources
- Report status
- Support decision-making

## Quality Requirements

### Index Accuracy
- Index must be current and accurate
- All drawings listed
- Status correctly reflected
- Revisions up to date
- Links valid

### Index Completeness
- All drawings included
- All required fields populated
- Cross-references complete
- Relationships documented
- No orphaned drawings

## Best Practices

### Index Management
- Designate index owner
- Establish update procedures
- Automate where possible
- Validate regularly
- Distribute updates
- Support queries

### Integration
- Link to PLM/PDM system
- Coordinate with EBOM
- Integrate with CAD system
- Support CM processes
- Enable reporting

### Accessibility
- Make indices easily accessible
- Provide multiple views (type, zone, status)
- Enable search and filtering
- Export to common formats
- Support stakeholder needs

## Related Directories

- **All drawing types**: [`../PART/`](../PART/), [`../ASSEMBLY/`](../ASSEMBLY/), [`../INSTALLATION/`](../INSTALLATION/), [`../DETAIL/`](../DETAIL/), [`../ICD/`](../ICD/)
- **Zone organization**: [`../ZONES/`](../ZONES/)
- **Revision management**: [`../REVISIONS/`](../REVISIONS/)
- **CAD models**: [`../../MODELS/`](../../MODELS/)
- **EBOM**: [`../../../EBOM_LINKS.md`](../../../EBOM_LINKS.md)

## Example Index Files

### Master Drawing Index
- `MASTER_DRAWING_INDEX.xlsx` - Complete drawing list
- `MASTER_DRAWING_INDEX.csv` - CSV export for tools
- `MASTER_DRAWING_INDEX.md` - Markdown version for Git

### Status Reports
- `DRAWING_STATUS_REPORT_2025-01.pdf` - Monthly status
- `RELEASE_SCHEDULE.xlsx` - Release planning

### Specialized Indices
- `PART_DRAWINGS_INDEX.md` - Part drawings only
- `ASSEMBLY_DRAWINGS_INDEX.md` - Assembly drawings only
- `ZONE_FWD_INDEX.md` - Forward zone drawings
- `OBSOLETE_DRAWINGS_LOG.md` - Obsolete drawing tracking

## References

- **Parent README**: [`../README.md`](../README.md) - General drawing standards
- **Configuration Management**: `/00-PROGRAM/CONFIG_MGMT/` - CM procedures
- **PLM integration**: [`../../../PLM/README.md`](../../../PLM/README.md) - PLM system links
