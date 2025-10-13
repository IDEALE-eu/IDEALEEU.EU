# INDEX — Sub-Assembly Index and Cross-Reference

## Purpose

This directory contains index files, cross-reference tables, and navigation aids for the 53-10 Center Body sub-assembly structure. The index provides quick access to assemblies, parts, and documentation throughout the sub-assembly hierarchy.

## Contents

### Master Index Files
- **Assembly index**: Complete list of all sub-assemblies
- **Part index**: Cross-reference of parts to assemblies
- **Document index**: Documentation by type and assembly
- **Interface index**: Interface definitions and locations
- **Revision index**: Current revision status of all assemblies

### Cross-Reference Tables
- **Part-to-assembly**: Where is each part used?
- **Assembly-to-BOM**: BOM for each assembly
- **Drawing-to-model**: Drawing to CAD model mapping
- **Interface-to-assembly**: Interface locations
- **Fastener-to-joint**: Fastener specifications by joint

### Navigation Aids
- **Directory tree**: Complete directory structure
- **File location guide**: Where to find specific files
- **Naming convention guide**: File naming standards
- **Template guide**: Available templates and usage
- **Quick reference**: Common tasks and locations

## Index File Formats

### CSV Format
Simple comma-separated values for easy import/export:
```csv
Assembly_ID,Assembly_Name,Type,Location,Status,Revision,Date
53-10-ASM-F05,Frame Section F05,FRAME_SECTIONS,FRAME_SECTIONS/FXX/,Released,R01,2024-02-15
53-10-ASM-L01,Stringer Bay L01,STRINGER_BAYS,STRINGER_BAYS/LXX/,Released,R01,2024-02-20
```

### Excel Format
Spreadsheet with multiple worksheets:
- **Assemblies**: Master assembly list
- **Parts**: Part-to-assembly cross-reference
- **Documents**: Documentation index
- **Interfaces**: Interface locations
- **Revisions**: Revision tracking

### JSON Format
Machine-readable hierarchical structure:
```json
{
  "assembly": {
    "id": "53-10-ASM-F05",
    "name": "Frame Section F05",
    "type": "FRAME_SECTIONS",
    "status": "Released",
    "revision": "R01",
    "location": "FRAME_SECTIONS/FXX/",
    "parts": ["53-10-FRM-F05", "53-10-STR-L01"]
  }
}
```

## Master Assembly Index

Complete list of all sub-assemblies:

| Assembly ID | Name | Type | Status | Revision | Location | Notes |
|-------------|------|------|--------|----------|----------|-------|
| 53-10-ASM-F01 | Frame Section F01 | Frame | Released | R01 | FRAME_SECTIONS/FXX/ | Forward |
| 53-10-ASM-F05 | Frame Section F05 | Frame | Released | R01 | FRAME_SECTIONS/FXX/ | Mid-fwd |
| 53-10-ASM-L01 | Stringer Bay L01 | Stringer | Released | R01 | STRINGER_BAYS/LXX/ | Left upper |
| ... | ... | ... | ... | ... | ... | ... |

## Part Cross-Reference

Where each part is used:

| Part Number | Description | Used In Assemblies | Quantity Per | Total Qty |
|-------------|-------------|-------------------|--------------|-----------|
| 53-10-FRM-F05 | Frame F05 | 53-10-ASM-F05 | 1 | 1 |
| 53-10-STR-L01 | Stringer L01 | 53-10-ASM-F05, 53-10-ASM-L01 | 1, 1 | 2 |
| AN470AD4-6 | Rivet AD4-6 | Multiple | Varies | 2000+ |

## Document Index

Documentation organized by type:

| Document ID | Title | Type | Assembly | Location | Revision |
|-------------|-------|------|----------|----------|----------|
| 53-10-BOM-F05 | BOM Frame F05 | BOM | 53-10-ASM-F05 | DOCS/BOM/ | v01 |
| 53-10-SEQ-F05 | Assembly Sequence F05 | Sequence | 53-10-ASM-F05 | DOCS/SEQUENCE/ | v01 |
| 53-10-CHK-F05 | Inspection Checklist F05 | Check | 53-10-ASM-F05 | DOCS/CHECKS/ | v01 |

## Interface Index

Interface definitions and locations:

| Interface ID | From | To | Type | Location | ICD Reference |
|--------------|------|-----|------|----------|---------------|
| IFX-53-51-001 | Center Body | Nose Section | Structural | NOSE_INTERFACE | ICD-001 |
| IFX-53-57-001 | Center Body | Wing | Structural | WING_INTERFACE | ICD-002 |
| IFX-53-53-001 | Center Body | Aft Section | Structural | AFT_INTERFACE | ICD-003 |

## Revision Status Summary

Current revision status of all assemblies:

| Assembly Type | Total | Draft | Released | Obsolete |
|---------------|-------|-------|----------|----------|
| Frame Sections | 20 | 5 | 12 | 3 |
| Stringer Bays | 24 | 8 | 14 | 2 |
| Skin Panel Modules | 80 | 20 | 55 | 5 |
| Floor Modules | 15 | 3 | 10 | 2 |
| Bulkhead Modules | 12 | 2 | 8 | 2 |
| Other | 30 | 10 | 18 | 2 |
| **Total** | **181** | **48** | **117** | **16** |

## Directory Structure Overview

Complete directory tree for quick reference:
```
SUB_ASSEMBLIES/
├── FRAME_SECTIONS/
│   └── FXX/
│       ├── MODELS/
│       ├── DRAWINGS/
│       └── DOCS/
├── STRINGER_BAYS/
│   └── LXX/
│       ├── MODELS/
│       ├── DRAWINGS/
│       └── DOCS/
├── SKIN_PANEL_MODULES/
│   └── PXX/
│       ├── MODELS/
│       ├── DRAWINGS/
│       └── DOCS/
├── FLOOR_MODULES/
│   └── BAY_XX/
│       ├── MODELS/
│       ├── DRAWINGS/
│       └── DOCS/
├── BULKHEAD_MODULES/
│   └── BH_XX/
│       ├── MODELS/
│       ├── DRAWINGS/
│       └── DOCS/
├── INTERFACE_GROUPS/
│   ├── WING_INTERFACE/
│   ├── NOSE_INTERFACE/
│   └── AFT_INTERFACE/
├── DOOR_SURROUNDS/
├── WINDOW_BAYS/
├── MOUNTING_UNITS/
├── TANK_SUPPORT_MODULES/
├── FASTENER_SETS/
├── JIG_READY/
├── DOCS/
│   ├── BOM/
│   ├── SEQUENCE/
│   └── CHECKS/
├── REVISIONS/
│   ├── DRAFT/
│   ├── RELEASED/
│   └── OBSOLETE/
├── TEMPLATES/
└── INDEX/ (this directory)
```

## Quick Reference Guide

### Common Tasks

**To create a new frame section assembly:**
1. Go to `TEMPLATES/`
2. Copy `TEMPLATE_FRAME-SECTION_STANDARD.CATProduct`
3. Save to `FRAME_SECTIONS/FXX/MODELS/` with proper naming
4. Configure parameters for specific frame station
5. Create associated BOM and documentation

**To find all uses of a part:**
1. Check `INDEX/part_cross_reference.csv`
2. Search for part number
3. Lists all assemblies using the part

**To check revision status:**
1. Check `INDEX/revision_status_summary.xlsx`
2. Find assembly in list
3. See current status and revision

## Search and Navigation

### File Naming Patterns
- Frame sections: `53-10_ASM_FRAME-SECTION_F<nn>_v<ver>.<ext>`
- Stringer bays: `53-10_ASM_STRINGER-BAY_L<nn>_v<ver>.<ext>`
- Skin panels: `53-10_ASM_SKIN-PANEL_P<nn>_v<ver>.<ext>`
- Floor modules: `53-10_ASM_FLOOR-MODULE_BAY-<nn>_v<ver>.<ext>`
- Bulkheads: `53-10_ASM_BULKHEAD_BH-<nn>_v<ver>.<ext>`

### Location Patterns
- Models: `<type>/<identifier>/MODELS/`
- Drawings: `<type>/<identifier>/DRAWINGS/`
- Documentation: `<type>/<identifier>/DOCS/`
- BOMs: `DOCS/BOM/`
- Procedures: `DOCS/SEQUENCE/`
- Inspections: `DOCS/CHECKS/`

## Related Directories

- **Frame sections**: [`../FRAME_SECTIONS/`](../FRAME_SECTIONS/)
- **Stringer bays**: [`../STRINGER_BAYS/`](../STRINGER_BAYS/)
- **All sub-assembly types**: Index covers entire SUB_ASSEMBLIES/ structure
- **Documentation**: [`../DOCS/`](../DOCS/)
- **Templates**: [`../TEMPLATES/`](../TEMPLATES/)
- **Top-level assembly**: [`../../TOP_LEVEL/`](../../TOP_LEVEL/)

## Index Maintenance

### Update Frequency
- **Real-time**: Automated index from PLM/PDM system
- **Daily**: Daily automated index generation
- **Weekly**: Weekly manual index verification
- **On-demand**: Generate index when needed

### Index Generation
- **Automated**: Scripts to generate index from file system
- **PLM/PDM**: Extract index from product data management system
- **Manual**: Maintain index manually (for small projects)

### Quality Checks
- Verify all assemblies are indexed
- Check for broken links
- Validate part numbers and references
- Ensure revision status is current
- Update for new assemblies or changes

## Metadata Requirements

Each index file should include:
- **Index name**: Descriptive index identifier
- **Index type**: Assembly, part, document, interface, revision
- **Generation date**: When index was created
- **Data source**: Where index data came from
- **Coverage**: What is included in the index
- **Version**: Index version or revision
- **Status**: Current, outdated, or archived

## Integration with Other Systems

Index files support integration with:
- **PLM/PDM systems**: Product data management
- **ERP systems**: Enterprise resource planning
- **MES systems**: Manufacturing execution systems
- **Quality systems**: Quality management systems
- **Documentation systems**: Technical publications

## Usage Guidelines

### For Engineers
- Use index to locate assemblies quickly
- Check part usage before making changes
- Verify interface locations
- Track revision status

### For Manufacturing
- Find assembly procedures and BOMs
- Locate jig-ready configurations
- Access inspection checklists
- Check current revisions for production

### For Quality
- Access inspection procedures
- Track revision history
- Locate certification documents
- Find test results and reports

## Version Control

- Maintain index file revision history
- Tag index releases with date
- Document significant index changes
- Archive obsolete index versions
- Coordinate index updates with data changes
