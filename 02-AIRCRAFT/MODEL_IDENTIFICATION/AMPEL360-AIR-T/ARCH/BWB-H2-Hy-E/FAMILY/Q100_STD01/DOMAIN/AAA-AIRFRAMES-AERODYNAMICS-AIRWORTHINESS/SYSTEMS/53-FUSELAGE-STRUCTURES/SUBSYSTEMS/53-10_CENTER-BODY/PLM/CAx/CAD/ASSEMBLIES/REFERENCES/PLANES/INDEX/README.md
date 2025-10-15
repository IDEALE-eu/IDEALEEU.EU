# INDEX — Reference Plane Index and Catalog

## Purpose

This directory contains index files, catalogs, and cross-reference documents that provide quick lookup and navigation of all reference planes defined for the 53-10 Center Body.

## Contents

### Master Index Files

#### Reference Plane Master List
- **File**: `53-10_PLANES_MASTER_INDEX.xlsx`
- **Description**: Complete catalog of all reference planes
- **Columns**:
  - Plane ID
  - Plane Type (Global, Station, Local, Interface, etc.)
  - File Name
  - Version
  - Location/Coordinates
  - Status (Active, Superseded, Obsolete)
  - Related Documents
  - Last Updated

#### Quick Reference Guide
- **File**: `53-10_PLANES_QUICK_REFERENCE.pdf`
- **Description**: Visual guide to key reference planes
- **Contents**:
  - Coordinate system overview
  - Major station locations
  - Interface plane locations
  - Naming convention summary
  - Usage guidelines

### Index by Category

#### Global Planes Index
- **File**: `53-10_INDEX_GLOBAL_PLANES.csv`
- **Contents**: All global reference planes (XY, XZ, YZ)

#### Station Planes Index
- **File**: `53-10_INDEX_STATION_PLANES.csv`
- **Contents**: All station planes (FS, WL, BL)

#### Local Planes Index
- **File**: `53-10_INDEX_LOCAL_PLANES.csv`
- **Contents**: All component-specific local planes

#### Interface Planes Index
- **File**: `53-10_INDEX_INTERFACE_PLANES.csv`
- **Contents**: All structural interface planes

### Cross-Reference Indexes

#### Plane-to-Component Index
- **File**: `53-10_INDEX_PLANE_TO_COMPONENT.csv`
- **Description**: Links planes to components/assemblies that use them
- **Usage**: Find all components affected by a plane change

#### Component-to-Plane Index
- **File**: `53-10_INDEX_COMPONENT_TO_PLANE.csv`
- **Description**: Lists all planes used by each component
- **Usage**: Find all planes needed for a specific component design

#### Interface Control Index
- **File**: `53-10_INDEX_INTERFACE_CONTROL.csv`
- **Description**: Links interface planes to ICDs and related documents
- **Usage**: Navigate between geometry and interface requirements

## Index Structure

### Master Index Format

The master index spreadsheet contains:

| Column | Description | Example |
|--------|-------------|---------|
| Plane ID | Unique identifier | PLANE-001 |
| Name | Descriptive name | FS-1200 Fuselage Station |
| Type | Category | STATION |
| Subtype | Specific type | FS |
| File Name | CAD file name | 53-10_STATION_FS-1200_v02.CATPart |
| Version | Current version | v02 |
| Status | Current status | Active |
| Location X | X coordinate (mm) | 1200.0 |
| Location Y | Y coordinate (mm) | 0.0 |
| Location Z | Z coordinate (mm) | 0.0 |
| Normal X | Normal vector X | 0.0 |
| Normal Y | Normal vector Y | 0.0 |
| Normal Z | Normal vector Z | 1.0 |
| Created By | Author | J. Smith |
| Created Date | Creation date | 2025-01-15 |
| Modified By | Last modifier | A. Johnson |
| Modified Date | Last update | 2025-03-10 |
| Related Docs | Links to other docs | ICD-53-57-001 |
| Notes | Additional info | Updated for wing interface |

### CSV Index Format

Standard format for CSV index files:

```csv
PlaneID,Name,Type,Subtype,FileName,Version,Status,Location,Normal,CreatedDate
PLANE-001,FS-1200,STATION,FS,53-10_STATION_FS-1200_v02.CATPart,v02,Active,"(1200.0,0.0,0.0)","(1.0,0.0,0.0)",2025-01-15
PLANE-002,WL-1500,STATION,WL,53-10_STATION_WL-1500_v01.CATPart,v01,Active,"(0.0,0.0,1500.0)","(0.0,0.0,1.0)",2025-01-20
PLANE-003,BL-0,STATION,BL,53-10_STATION_BL-0_v01.CATPart,v01,Active,"(0.0,0.0,0.0)","(0.0,1.0,0.0)",2025-01-10
```

## Index Maintenance

### Update Frequency

- **Real-time**: PLM system automatically tracks file versions
- **Daily**: Automated script updates CSV indexes from PLM
- **Weekly**: Manual review and validation of indexes
- **Monthly**: Comprehensive index audit and cleanup

### Update Procedures

#### New Plane Addition

1. Create plane file in CAD system
2. Check into PLM with metadata
3. PLM system auto-updates index
4. Verify index entry correct
5. Add cross-references if needed

#### Plane Modification

1. Modify plane in CAD system
2. Increment version number
3. Check in new version to PLM
4. PLM updates index with new version
5. Previous version marked as superseded
6. Update related document links

#### Plane Obsolescence

1. Identify planes no longer needed
2. Review for dependencies
3. Update status to "Obsolete"
4. Archive file (don't delete)
5. Document reason for obsolescence
6. Notify affected users

### Index Validation

Regular validation checks:
- All active planes have valid files
- All files have index entries
- Coordinates match between file and index
- Version numbers sequential
- No duplicate IDs or names
- Cross-references valid

## Search and Navigation

### Finding a Plane

#### By Location

1. Open station planes index
2. Filter by coordinate range
3. Sort by distance from target location
4. Select closest plane

#### By Type

1. Open category index (Global, Station, Local, Interface)
2. Filter by subtype if needed
3. Review available planes
4. Select appropriate plane

#### By Component

1. Open component-to-plane index
2. Look up component ID
3. View list of associated planes
4. Access needed plane files

#### By Interface

1. Open interface planes index
2. Look up interface ID (e.g., 53_TO_57)
3. View interface plane set
4. Review related ICDs

### Index Files Available

```
INDEX/
├── 53-10_PLANES_MASTER_INDEX.xlsx
├── 53-10_PLANES_QUICK_REFERENCE.pdf
├── 53-10_INDEX_GLOBAL_PLANES.csv
├── 53-10_INDEX_STATION_PLANES.csv
├── 53-10_INDEX_LOCAL_PLANES.csv
├── 53-10_INDEX_INTERFACE_PLANES.csv
├── 53-10_INDEX_PLANE_TO_COMPONENT.csv
├── 53-10_INDEX_COMPONENT_TO_PLANE.csv
├── 53-10_INDEX_INTERFACE_CONTROL.csv
└── INDEX_MAINTENANCE_GUIDE.md
```

## Index Usage Examples

### Example 1: Find Frame F05 Reference Planes

1. Open `53-10_INDEX_LOCAL_PLANES.csv`
2. Filter `Name` column for "FRAME_F05"
3. Result shows all planes for Frame F05:
   - F05 web plane
   - F05 upper cap plane
   - F05 lower cap plane
   - F05 attachment planes

### Example 2: Find All Planes at Station FS-1200

1. Open `53-10_INDEX_STATION_PLANES.csv`
2. Filter `Location` column where X = 1200.0
3. Result shows:
   - FS-1200 primary station plane
   - Any WL planes at FS-1200
   - Any BL planes at FS-1200

### Example 3: Find Wing Interface Planes

1. Open `53-10_INDEX_INTERFACE_PLANES.csv`
2. Filter `Name` column for "53_TO_57"
3. Result shows all wing-to-body interface planes
4. Cross-reference to `53-10_INDEX_INTERFACE_CONTROL.csv`
5. Find related ICD documents

## Automated Index Generation

### PLM Integration

The PLM system automatically maintains indexes by:
- Monitoring file check-ins
- Extracting metadata
- Updating index databases
- Generating CSV exports
- Publishing updated indexes

### Custom Scripts

Additional automation available:
- **Validation Script**: Checks index integrity
- **Search Tool**: Command-line plane search
- **Report Generator**: Creates usage reports
- **Duplicate Checker**: Finds duplicate or near-duplicate planes

## Standards Compliance

Follow:
- **ISO 16792**: Digital product definition data practices
- **ATA iSpec 2200**: Data organization and indexing
- **Company PLM standards**: Configuration management and indexing

## Related Directories

- **All plane directories**: [`../`](../) (parent PLANES directory)
- **Validation**: [`../VALIDATION/`](../VALIDATION/)
- **Metadata**: [`../METADATA/`](../METADATA/)
- **Interface control**: [`../../../DOCS/INTERFACE_CONTROL/`](../../../DOCS/INTERFACE_CONTROL/)

## Support

For assistance with indexes:
- **PLM System Support**: Help with automated indexing
- **CAD Support**: Help finding or creating planes
- **Configuration Management**: Questions about versions and status
- **Documentation Team**: Help with cross-references and ICDs
