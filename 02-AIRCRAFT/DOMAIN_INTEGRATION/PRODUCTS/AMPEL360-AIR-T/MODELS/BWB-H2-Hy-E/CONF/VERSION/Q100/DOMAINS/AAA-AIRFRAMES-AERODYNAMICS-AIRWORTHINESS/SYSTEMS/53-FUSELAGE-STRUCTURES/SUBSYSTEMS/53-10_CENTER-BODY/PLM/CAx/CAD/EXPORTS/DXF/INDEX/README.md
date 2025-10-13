# INDEX — DXF File Index and Catalog

## Purpose
Master index and catalog of all DXF files in this directory structure.

## Contents
- Master file index (spreadsheet)
- Cross-reference tables
- File location maps
- Version history summaries
- Quick reference guides

## Index Files

### Master Index
Primary index file (Excel/CSV):
```
DXF_MASTER_INDEX.xlsx
```

**Columns**:
- Part Number
- Description
- File Name
- Revision
- Date
- Location (subdirectory)
- Material
- Thickness (if applicable)
- Status (Draft/Released/Obsolete)
- Notes

### Cross-Reference Tables
Supporting indices:
- **Part Number Index**: By part number
- **Zone Index**: By structural zone (FWD/CTR/AFT)
- **Material Index**: By material type
- **Supplier Index**: By supplier/manufacturer
- **Date Index**: By creation/release date

## File Naming Convention
```
DXF_INDEX_<type>_<date>.xlsx
```

Examples:
- `DXF_INDEX_MASTER_20250110.xlsx`
- `DXF_INDEX_BY-ZONE_20250110.xlsx`
- `DXF_INDEX_BY-MATERIAL_20250110.xlsx`

## Index Maintenance

### Update Frequency
- **Daily/Weekly**: During active development
- **Monthly**: During production
- **Per release**: At each design release

### Update Process
1. Review new and changed files
2. Update master index
3. Verify all cross-references
4. Check for missing entries
5. Validate file locations
6. Version the index file
7. Commit to repository

## Index Information
For each file, track:
- **Identification**: Part number, revision, file name
- **Location**: Directory path
- **Status**: Draft, Released, Obsolete
- **Metadata**: Material, thickness, process
- **Dates**: Created, released, modified
- **Relationships**: Assembly, mating parts
- **References**: Drawing number, ECO number

## Quick Reference Guides

### New User Guide
Quick start for:
- Finding files by part number
- Understanding directory structure
- Accessing released vs. draft files
- Supplier package locations
- Quality documentation

### File Organization Map
Visual guide showing:
- Directory structure
- File flow (draft → released → obsolete)
- Supplier package workflow
- Quality assurance process
- Cross-directory relationships

## Search and Retrieval
Index supports searching by:
- Part number
- Description keywords
- Material type
- Zone (FWD/CTR/AFT)
- Revision
- Date range
- Status (Draft/Released/Obsolete)
- Supplier

## Related Directories
All directories in DXF structure:
- **[../PARTS/](../PARTS/)**
- **[../ASSEMBLIES/](../ASSEMBLIES/)**
- **[../INSTALLATION/](../INSTALLATION/)**
- **[../NESTING/](../NESTING/)**
- **[../ZONES/](../ZONES/)**
- **[../REVISIONS/](../REVISIONS/)**
- **[../SUPPLIERS/](../SUPPLIERS/)**
- **[../QA/](../QA/)**

## Automation
Consider automating:
- File discovery and listing
- Metadata extraction from files
- Index generation
- Change detection
- Report generation

## Validation
Regular index validation:
- Verify all indexed files exist
- Check for orphaned files (not indexed)
- Validate metadata accuracy
- Ensure cross-references correct
- Check for duplicates

## Reports
Generate periodic reports:
- File count by status
- New files this period
- Obsoleted files this period
- Files by material type
- Files by zone
- Supplier package summary

## Best Practices
- Keep index current
- Version index files
- Regular validation
- Clear documentation
- Easy to navigate
- Automated where possible
- Regular audits

## Version Control
- Track index file versions
- Document significant changes
- Maintain history
- Link to DXF file releases
- Regular backups
