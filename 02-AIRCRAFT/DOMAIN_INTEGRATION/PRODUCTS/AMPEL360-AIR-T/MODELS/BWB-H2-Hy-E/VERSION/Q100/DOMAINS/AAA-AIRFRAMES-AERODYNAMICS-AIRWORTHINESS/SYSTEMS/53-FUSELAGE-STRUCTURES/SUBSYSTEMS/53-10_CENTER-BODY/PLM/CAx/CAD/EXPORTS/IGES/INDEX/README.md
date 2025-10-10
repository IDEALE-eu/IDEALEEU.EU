# INDEX — IGES File Catalog and Index

## Purpose

This directory contains index files, catalogs, and inventories of all IGES exports to enable quick searching, tracking, and management of geometry files.

## Content

Store index and catalog files:
- **Master index**: Complete listing of all IGES files
- **Part catalogs**: Organized part number listings
- **Revision matrices**: Tracking current and obsolete revisions
- **Distribution logs**: Records of supplier distributions
- **File manifests**: Contents of packages and directories
- **Search databases**: Searchable file databases (CSV, XLSX)

## Index File Types

### Master Index (CSV/XLSX)
Complete catalog of all IGES files with columns:
- Part Number
- Part Name
- Revision
- File Name
- File Location
- Date Created
- File Size
- Status (Draft/Released/Obsolete)
- Author
- Notes

### Revision Matrix (CSV/XLSX)
Track revisions across parts:
- Part Number
- Current Revision
- Current File
- Previous Revisions
- Obsolete Files
- ECR/ECO References
- Change Description

### Distribution Log (CSV/XLSX)
Track file distributions:
- Package ID
- Supplier
- Files Included
- Distribution Date
- Recipient
- Acknowledgment Status
- Notes

## File Naming Convention

```
INDEX_<index-type>_<date>.<ext>
```

**Examples:**
- `INDEX_MASTER_20250110.xlsx`
- `INDEX_REVISIONS_20250110.xlsx`
- `INDEX_DISTRIBUTIONS_20250110.xlsx`
- `INDEX_PARTS-CATALOG_20250110.csv`

## Master Index Structure

Example master index (CSV format):
```csv
part_number,part_name,revision,file_name,directory,date_created,file_size_mb,status,author,notes
PN-12345,FRAME-F01,RevA,53-10_FRAME-F01_PN-12345_RevA_20250110.igs,PARTS/SOLIDS/,2025-01-10,2.5,Released,J.Smith,Initial release
PN-12346,PANEL-01,RevB,53-10_PANEL-01_PN-12346_RevB_20250110.igs,PARTS/SURFACES/,2025-01-10,5.8,Released,M.Jones,Updated dimensions
PN-12347,BULKHEAD,RevA,53-10_BULKHEAD_PN-12347_RevA_20250110.igs,PARTS/SOLIDS/,2025-01-10,3.2,Draft,K.Lee,Work in progress
```

## Index Maintenance

Index files should be:
- **Updated regularly**: Add new files, update status
- **Version controlled**: Track index changes
- **Backed up**: Prevent data loss
- **Validated**: Verify accuracy against actual files
- **Consistent**: Use standard format and structure

Update frequency:
- Master index: Weekly or after significant changes
- Revision matrix: After each revision release
- Distribution log: After each distribution

## Search and Query

Use index files to:
- Find files by part number
- Locate specific revisions
- Track file status
- Search by author or date
- Identify obsolete files
- Generate reports

## Related Directories

- **Parent**: [`../`](../) — Root IGES directory
- **All subdirectories**: Index covers entire IGES structure
- **Parts**: [`../PARTS/`](../PARTS/) — Part files indexed
- **Assemblies**: [`../ASSEMBLIES/`](../ASSEMBLIES/) — Assembly files indexed
- **Revisions**: [`../REVISIONS/`](../REVISIONS/) — Revision tracking

## Index Tools

Tools for managing indexes:
- **Spreadsheet software**: Excel, Google Sheets
- **Database tools**: Access, SQLite
- **Python scripts**: Automated index generation
- **PLM systems**: Integration with PLM catalogs

## Automated Index Generation

Consider automating index generation:
```python
# Example: Scan directory and generate index
import os
import csv
from datetime import datetime

def generate_index(root_dir):
    index = []
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.igs') or file.endswith('.iges'):
                path = os.path.join(root, file)
                size_mb = os.path.getsize(path) / (1024*1024)
                mod_time = datetime.fromtimestamp(os.path.getmtime(path))
                index.append({
                    'file_name': file,
                    'directory': root,
                    'size_mb': f'{size_mb:.2f}',
                    'date_modified': mod_time.strftime('%Y-%m-%d'),
                })
    return index
```

## Index Views

Create different index views for different purposes:

### By Part Number
- Sorted alphabetically by part number
- Shows all revisions per part
- Highlights current vs. obsolete

### By Status
- Grouped by Draft/Released/Obsolete
- Useful for revision management
- Identifies work in progress

### By Zone
- Grouped by FWD/CTR/AFT
- Useful for assembly planning
- Zone-based reporting

### By Type
- Grouped by Parts/Assemblies/Tooling
- Useful for manufacturing planning
- Type-specific analysis

## Reporting

Generate reports from index:
- **File count by status**: Number of draft/released/obsolete files
- **File size summary**: Total storage usage
- **Revision summary**: Parts with multiple revisions
- **Distribution summary**: Packages sent to suppliers
- **Quality metrics**: Files passing QA checks

## Best Practices

- Maintain accurate, up-to-date index
- Use consistent data format
- Include all relevant metadata
- Cross-reference to PDM/PLM
- Validate index against actual files
- Archive previous index versions
- Document index structure
- Provide search capability
- Generate regular reports
- Integrate with workflow tools

## Integration with PLM

Index files should integrate with:
- PLM part master data
- Engineering drawings
- BOM structures
- Configuration management
- Approval workflows
- Distribution tracking

## Index Backup and Recovery

Protect index data:
- Regular backups (daily or weekly)
- Version control (Git)
- Multiple backup locations
- Disaster recovery plan
- Easy restoration process

## Usage Examples

### Find Current Revision
```
Filter: part_number = "PN-12345"
Filter: status = "Released"
Sort by: date_created DESC
Result: Most recent released revision
```

### List Files in Package
```
Filter: distribution_log.package_id = "PKG-001"
Join: master_index on file_name
Result: All files in package with metadata
```

### Identify Obsolete Files
```
Filter: status = "Obsolete"
Group by: part_number
Result: List of obsolete files to archive
```
