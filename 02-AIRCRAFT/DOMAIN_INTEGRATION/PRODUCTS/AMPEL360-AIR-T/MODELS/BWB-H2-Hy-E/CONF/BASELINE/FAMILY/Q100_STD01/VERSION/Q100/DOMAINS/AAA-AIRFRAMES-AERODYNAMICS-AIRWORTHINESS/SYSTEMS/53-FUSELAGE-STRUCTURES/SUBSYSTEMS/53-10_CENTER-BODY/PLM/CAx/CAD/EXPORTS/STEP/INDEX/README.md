# INDEX — Catalogs and File Indices

## Purpose

This directory contains **index files, catalogs, and master lists** that track all STEP files in the structure, providing searchable references and metadata.

## What to Store

- Master file index (CSV or spreadsheet)
- BOM cross-reference
- Revision history logs
- File location maps
- Metadata catalogs
- Change history tracking

## Index File Formats

### Master Index (CSV)
```csv
filename,part_number,revision,date,status,location,author,description
53-10_FRAME-F01_PN-12345_RevB_20250110.step,PN-12345,B,2025-01-10,RELEASED,PARTS/SOLIDS/,J.Smith,Forward frame
```

### BOM Cross-Reference
Links STEP files to:
- Engineering BOM (EBOM)
- Manufacturing BOM (MBOM)
- Part numbers
- Assembly hierarchy

### Revision History
Tracks file evolution:
- Previous revisions
- ECO numbers
- Change descriptions
- Supersession chains

## Index Maintenance

Update indices when:
- New files are added
- Files are released or revised
- Files become obsolete
- Metadata changes
- Directory reorganization

## Search and Discovery

Use index files to find:
- Files by part number
- Files by revision status
- Files by date range
- Files by author
- Files by component type
- Files by zone or location

## Index Structure Examples

### By Component Type
- Parts index: All individual parts
- Assembly index: All assemblies
- Tooling index: All tooling files
- Interface index: All interface definitions

### By Status
- Draft files listing
- Released files catalog
- Obsolete files archive list

### By Zone
- FWD zone files
- CTR zone files
- AFT zone files

## Related Directories

All directories should be referenced in index:
- [**../PARTS/**](../PARTS/) — Part files
- [**../ASSEMBLIES/**](../ASSEMBLIES/) — Assembly files
- [**../TOOLING/**](../TOOLING/) — Tooling files
- [**../REVISIONS/**](../REVISIONS/) — Status tracking
- [**../SUPPLIERS/**](../SUPPLIERS/) — Supplier packages
- [**../QA/**](../QA/) — QA files

## Automation

Consider automating index generation:
- Script to scan directories
- Extract metadata from STEP files
- Generate CSV/Excel indices
- Update on file changes
- Integrate with PLM system

## Integration

Link indices to:
- PDM/PLM systems
- BOM management tools
- Configuration management database
- Change control system
- Document management system

## Example Index Entry

```csv
filename,part_number,revision,date,status,category,zone,location,ECO,author,notes
53-10_FRAME-F01_PN-12345_RevB_20250110.step,PN-12345,B,2025-01-10,RELEASED,PART,FWD,PARTS/SOLIDS/,ECO-2025-001,J.Smith,Forward primary frame
```

## References

- Parent directory: [**../**](../)
- Main STEP README: [**../README.md**](../README.md)
- BOM management: `00-PROGRAM/CONFIG_MGMT/03-BOM_MGMT/`
- Part numbering: `00-PROGRAM/CONFIG_MGMT/02-PART_NUMBERING/`
