# INDEX — BOM Catalog and Index

## Purpose

This directory contains master indexes, catalogs, and cross-reference tables that provide comprehensive tracking and quick access to all BOMs in the 53-10 Center Body system.

## Contents

### Master BOM Index
- Complete catalog of all BOMs
- BOM identification and location
- Revision tracking
- Status tracking
- Cross-reference tables

### Index Types
- **By Part Number**: Find BOMs containing specific parts
- **By Assembly**: Locate assembly-specific BOMs
- **By Revision**: Track BOM revision history
- **By Status**: Filter by DRAFT/RELEASED/OBSOLETE
- **By Date**: Chronological listing

## Master Index Structure

### Standard Index Columns
```csv
bom_id,assembly_name,revision,status,type,date,location,author,approver,notes
```

### Example Index Entry
```csv
53-10-CB-001,Center Body Assembly,r002,RELEASED,EBOM,2024-03-15,ASSEMBLIES/,J.Smith,M.Jones,Complete EBOM
53-10-FB-001,Forward Bulkhead,r001,RELEASED,EBOM,2024-03-10,PARTS/,A.Brown,M.Jones,Single part BOM
53-10-HW-001,Wing Attach Hardware,r003,RELEASED,INSTALL,2024-03-20,INSTALLATION/,K.Wilson,M.Jones,Installation BOM
```

## File Naming Convention

```
INDEX_<index-type>_<date>.<ext>
```

Examples:
- `INDEX_MASTER_20240315.csv`
- `INDEX_BY-PART-NUMBER_20240315.xlsx`
- `INDEX_REVISION-HISTORY_20240320.xlsx`
- `INDEX_STATUS-TRACKING_20240325.csv`

## Index Types

### Master BOM Index
Complete listing of all BOMs:
- BOM identifier
- Assembly/part name
- Current revision
- Status (DRAFT/RELEASED/OBSOLETE)
- BOM type (EBOM/MBOM/etc.)
- Release date
- File location
- Responsible engineer
- Approver

### Part Number Cross-Reference
Find BOMs containing specific parts:
- Part number
- Part description
- BOMs using this part
- Quantity per BOM
- Revision of BOM
- Status

### Assembly Hierarchy Index
BOM structure and relationships:
- Parent assembly
- Sub-assemblies
- Component parts
- Hierarchy level
- BOM references

### Revision History Index
Track BOM changes over time:
- BOM identifier
- Revision sequence
- Date of each revision
- Change description
- Status of each revision
- Superseded by

### Status Tracking Index
Current status of all BOMs:
- Active BOMs (RELEASED)
- BOMs in development (DRAFT)
- Obsolete BOMs
- Status change dates
- Reason for status

## Index Maintenance

### Update Frequency
- Update when new BOM created
- Update when BOM revised
- Update when status changes
- Monthly verification
- Annual audit

### Update Process
1. Identify new or changed BOM
2. Update master index
3. Update relevant cross-references
4. Verify completeness
5. Publish updated index
6. Archive previous version

## Index Usage

### Finding BOMs
- Search by part number
- Search by assembly name
- Filter by status
- Filter by revision
- Sort by date

### Tracking Changes
- Monitor revision history
- Track status changes
- Identify obsolete BOMs
- Find current revisions

### Reporting
- Generate BOM lists
- Create status reports
- Analyze BOM metrics
- Support audits

## Cross-Reference Tables

### Part Usage Table
Shows which BOMs use each part:
```csv
part_number,part_description,bom_count,bom_list
53-10-001,Center Frame,3,"CB-001,FB-001,WA-001"
```

### BOM Relationship Table
Shows BOM dependencies:
```csv
parent_bom,child_bom,relationship_type
53-10-CB-001,53-10-FB-001,CONTAINS
53-10-CB-001,53-10-HW-001,REQUIRES
```

## Metadata Tracking

Each index entry should track:
- Creation date
- Last modification date
- Author/owner
- Approver
- Change history
- Effectivity
- Configuration applicability

## Quality Assurance

Index quality requirements:
- Complete and accurate
- Updated promptly
- No duplicate entries
- Valid references
- Synchronized with actual BOMs
- Regularly audited

## Automated Index Generation

### Script-Based Indexing
- Scan BOM directories
- Extract metadata
- Generate index files
- Validate completeness
- Update cross-references

### Index Validation
- Check for missing BOMs
- Verify status consistency
- Validate file locations
- Check for duplicates
- Confirm revision sequence

## Index Formats

### CSV Format
- Machine-readable
- Import to databases
- Easy to search and sort
- Version control friendly

### Excel Format
- Human-readable
- Filtered views
- Pivot tables
- Dashboard reports

## Archive Index

Track obsolete and archived BOMs:
- Original release date
- Obsolescence date
- Reason for obsolescence
- Superseding BOM
- Archive location
- Retention requirements

## Usage Examples

### Finding Current BOM
1. Open master index
2. Search for assembly name
3. Filter by RELEASED status
4. Identify highest revision
5. Navigate to file location

### Finding Part Usage
1. Open part number cross-reference
2. Search for part number
3. Review list of BOMs
4. Check quantities and revisions
5. Access specific BOMs

### Tracking Revisions
1. Open revision history index
2. Search for BOM identifier
3. Review revision sequence
4. Compare changes
5. Identify current baseline

## Related Directories

- **Revisions**: [../REVISIONS/](../REVISIONS/) — BOM lifecycle states
- **Reports**: [../REPORTS/](../REPORTS/) — BOM analysis reports
- **All BOM directories**: Index references all BOM locations
