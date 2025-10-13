# INDEX — Assembly Index and Catalog

## Purpose

This directory contains index files, catalogs, and navigation aids for the top-level assembly structure.

## Index Files

### Master Index
- **File inventory**: Complete list of all files
- **Directory structure**: Organization overview
- **File relationships**: Dependencies and links
- **Version tracking**: Current versions of all files

### Component Index
- **Part numbers**: Catalog of all parts
- **Descriptions**: Brief description of each component
- **Locations**: Where files are stored
- **Status**: Draft, released, obsolete

## Index Types

### By Category
- **Assemblies**: All assembly files
- **Models**: All component models
- **Drawings**: All drawing files
- **Documentation**: All supporting documents
- **Exports**: All neutral format files

### By Status
- **Current**: Active files in use
- **Released**: Formally approved versions
- **Obsolete**: Superseded files
- **Draft**: Work in progress

## File Formats

- `.xlsx` — Excel spreadsheet index
- `.csv` — CSV data export
- `.html` — Web-based index
- `.pdf` — Printable catalog
- `.xml` — Structured data index

## Naming Convention

```
53-10_INDEX_<type>_<date>.<ext>
```

Examples:
- `53-10_INDEX_MASTER_2024-01-15.xlsx`
- `53-10_INDEX_COMPONENTS_2024-01-15.csv`
- `53-10_INDEX_DRAWINGS_2024-01-15.pdf`

## Index Contents

### File Index Fields
- **File name**: Full file name with extension
- **Path**: Relative path from TOP_LEVEL
- **Type**: Assembly, model, drawing, document, export
- **Version**: Current version number
- **Revision**: Revision letter if released
- **Date**: Last modified date
- **Author**: File creator
- **Status**: Draft, released, obsolete
- **Description**: Brief description
- **Size**: File size
- **Checksum**: File integrity check (MD5, SHA)

### Component Index Fields
- **Part number**: Unique identifier
- **Description**: Component name/description
- **Type**: Frame, stringer, skin, fitting, etc.
- **Quantity**: Number in assembly
- **Material**: Material specification
- **Mass**: Component mass (kg)
- **File name**: CAD file name
- **Drawing**: Associated drawing number
- **Status**: Design status

## Index Generation

### Automated Index
- Script-generated file lists
- Automated metadata extraction
- Scheduled updates (nightly/weekly)
- Change detection and reporting

### Manual Index
- Curated component lists
- Design intent documentation
- Interface descriptions
- Special notes and warnings

## Navigation Aids

### Quick Reference
- **File location map**: Visual directory tree
- **Component hierarchy**: Assembly structure diagram
- **Interface map**: System interface locations
- **Change log**: Recent modifications

### Search Tools
- **Find by part number**: Locate files quickly
- **Find by type**: Filter by file type
- **Find by status**: Show only released/draft/obsolete
- **Find by date**: Recent changes

## Index Maintenance

### Update Frequency
- **Automated**: Daily or on-commit
- **Manual review**: Weekly
- **Full audit**: Monthly
- **Archive**: Quarterly snapshots

### Validation
- [ ] All files accounted for
- [ ] No broken links
- [ ] Versions accurate
- [ ] Status correct
- [ ] No duplicates
- [ ] Checksums valid

## Reports

### Standard Reports
- **File inventory**: Complete file list
- **Version report**: Current versions of all files
- **Status report**: Files by status (draft/released/obsolete)
- **Change report**: Recent modifications
- **Dependency report**: File relationships

## Integration

### PLM Integration
- Sync with PLM system
- Export BOM to PLM
- Import release status
- Track change orders

### Version Control
- Git repository mapping
- Branch and tag references
- Commit history links
- Merge tracking

## Documentation

- **Index usage guide**: How to use index files
- **Update procedures**: How to maintain index
- **Field definitions**: Description of all fields
- **Examples**: Sample queries and reports

## Tools

### Index Tools
- **Index generator scripts**: Python/PowerShell scripts
- **Search utilities**: Command-line or GUI tools
- **Report generators**: Automated report creation
- **Validation scripts**: Index validation tools

## Related Directories

This index covers all directories under TOP_LEVEL:
- [`../ASM/`](../ASM/)
- [`../MODELS/`](../MODELS/)
- [`../DRAWINGS/`](../DRAWINGS/)
- [`../DOCS/`](../DOCS/)
- [`../EXPORTS/`](../EXPORTS/)
- [`../CHECKS/`](../CHECKS/)
- [`../REVISIONS/`](../REVISIONS/)
- And all subdirectories
