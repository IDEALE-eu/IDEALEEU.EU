# INDEX — File Catalogs and Indexes

## Purpose

This directory contains index files, catalogs, and cross-reference documentation for all JT files in the directory structure.

## What to Store

- Master file catalogs
- Cross-reference indexes
- BOM extracts
- File location maps
- Metadata summaries
- Search indexes

## Index Types

### Master Catalog
Complete list of all JT files with key metadata:
- Filename
- Part number
- Revision
- Location path
- File size
- Export date
- Status (draft/released/obsolete)

### Cross-Reference Index
Links between related files:
- Part → Assembly relationships
- Source CAD → JT mappings
- STEP ↔ JT correspondence
- Revision history chains
- Supplier package contents

### BOM Index
Bill of Materials extracted from assemblies:
- Assembly structure
- Component list
- Quantities
- Part numbers
- Material specifications

### Metadata Index
Searchable metadata catalog:
- Properties summary
- Attribute values
- Classification codes
- Keywords and tags

## File Formats

Indexes typically stored as:
- CSV spreadsheets (for Excel compatibility)
- JSON catalogs (for automation)
- XML databases (for systems integration)
- Markdown tables (for documentation)
- SQLite databases (for complex queries)

## Usage

Use indexes for:
- Finding files quickly
- Verifying completeness
- Generating reports
- Automation scripts
- BOM validation
- Traceability verification
- PLM synchronization

## Example Index Structure

```csv
filename,part_number,revision,location,size_mb,date,status
53-10_FRAME-F01.jt,PN-12345,B,PARTS/LOD_MED,2.3,2025-01-10,RELEASED
53-10_ASM_COMPLETE.jt,PN-10000,A,ASSEMBLIES/TOP_LEVEL,45.7,2025-01-10,RELEASED
```

## Related Directories

- [`../METADATA/`](../METADATA/) — Detailed metadata
- [`../QA/CHECKS/`](../QA/CHECKS/) — Validation records
- [`../REVISIONS/`](../REVISIONS/) — Revision management
- [`../README.md`](../README.md) — JT format overview

## Best Practices

- Update indexes automatically
- Keep synchronized with file changes
- Include in release packages
- Use for validation checks
- Generate periodically
- Archive historical indexes
