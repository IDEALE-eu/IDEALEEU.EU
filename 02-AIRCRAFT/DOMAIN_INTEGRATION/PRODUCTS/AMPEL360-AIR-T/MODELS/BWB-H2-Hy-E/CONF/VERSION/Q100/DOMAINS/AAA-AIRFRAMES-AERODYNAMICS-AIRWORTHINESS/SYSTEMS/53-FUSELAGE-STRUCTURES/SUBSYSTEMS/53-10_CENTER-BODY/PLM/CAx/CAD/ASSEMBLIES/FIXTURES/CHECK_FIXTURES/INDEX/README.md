# INDEX — Check Fixture Index and Registry

## Purpose

This directory contains master index files and registries for all check fixtures, documentation, and related records.

## Contents

### Index Types
- **Fixture registry**: Master list of all check fixtures
- **Document index**: Index of all procedures, drawings, programs
- **Equipment index**: List of inspection equipment
- **Part-to-fixture cross-reference**: Links parts to fixtures
- **Calibration index**: List of calibration requirements and status

## Naming Convention

Use the following pattern:
```
INDEX_<index-type>_<date>.xlsx
```

Examples:
- `INDEX_FIXTURE-REGISTRY_2024-01-15.xlsx`
- `INDEX_DOCUMENT-MASTER_2024-02-20.xlsx`
- `INDEX_PART-XREF_2024-03-10.xlsx`

## Fixture Registry

### Registry Contents
Master list of all check fixtures with:
- **Fixture ID**: Unique identifier
- **Description**: Fixture name and purpose
- **Part numbers**: Parts inspected with this fixture
- **Drawing number**: Reference drawing
- **CAD file location**: Path to CAD models
- **Calibration frequency**: How often calibrated
- **Last calibration date**: Most recent calibration
- **Next due date**: When next calibration required
- **Status**: Active, inactive, in repair, obsolete
- **Location**: Where fixture is stored
- **Owner**: Responsible engineer/department
- **Notes**: Special information

## Document Index

### Master Document List
Index of all fixture-related documents:
- **Document number**: Unique identifier
- **Title**: Document name
- **Type**: Drawing, procedure, program, etc.
- **Revision**: Current revision level
- **Date**: Issue or revision date
- **File location**: Path to file
- **Applies to**: Which fixtures/parts
- **Status**: Released, draft, obsolete

## Equipment Index

### Inspection Equipment List
All equipment used with check fixtures:
- **Equipment ID**: Unique identifier
- **Description**: Equipment type and model
- **Manufacturer**: Maker and model number
- **Serial number**: Unique serial
- **Calibration frequency**: Interval
- **Calibration due date**: Next due
- **Location**: Where stored
- **Condition**: Operational status

## Part-to-Fixture Cross-Reference

### Cross-Reference Matrix
Links part numbers to check fixtures:
| Part Number | Description | Check Fixture(s) | CMM Program | Inspection Frequency |
|-------------|-------------|------------------|-------------|---------------------|
| FRAME-F05 | Frame 5 | FIX-CHECK-F05 | CMM_F05.dmis | First Article + 10% sample |
| WING-INT | Wing Interface | FIX-CHECK-WING-INT | CMM_WING.dmis | 100% |

### Usage
- Find which fixture to use for a part
- Identify all parts using a fixture
- Plan fixture usage and capacity
- Schedule maintenance windows

## Calibration Index

### Calibration Schedule Summary
- List all items requiring calibration
- Show current calibration status
- Highlight items due soon or overdue
- Track calibration compliance rate

## Index Maintenance

### Update Frequency
- Update monthly or as changes occur
- Review quarterly for accuracy
- Audit annually
- Distribute updated indexes

### Index Management
- Keep current version readily accessible
- Archive previous versions
- Maintain change history
- Ensure accuracy and completeness

## Index Reports

### Summary Reports
- Active fixtures count
- Calibration compliance rate
- Inactive/obsolete fixtures
- Missing documents
- Overdue calibrations

### Status Dashboards
- Visual status indicators
- Trend charts
- Compliance metrics
- Alert notifications

## Related Directories

- **All subdirectories**: Index references all content
- **Calibration schedule**: [`../CALIBRATION/SCHEDULE/`](../CALIBRATION/SCHEDULE/)
- **Models**: [`../MODELS/`](../MODELS/)
- **Reports**: [`../REPORTS/`](../REPORTS/)
