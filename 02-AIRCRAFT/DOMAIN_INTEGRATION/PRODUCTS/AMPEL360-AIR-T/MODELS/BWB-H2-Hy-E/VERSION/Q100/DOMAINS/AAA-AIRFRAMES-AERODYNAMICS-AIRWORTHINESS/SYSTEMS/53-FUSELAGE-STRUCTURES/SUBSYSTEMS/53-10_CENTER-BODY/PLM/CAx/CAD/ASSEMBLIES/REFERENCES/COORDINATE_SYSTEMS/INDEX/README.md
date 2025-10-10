# INDEX — Coordinate System Index

## Purpose

This directory contains index files and catalogs of all coordinate systems defined for the 53-10 Center Body, enabling quick lookup and cross-referencing.

## Contents

### Master Index
- **COORDINATE_SYSTEMS_MASTER_INDEX.csv** — Complete list of all coordinate systems
- **COORDINATE_SYSTEMS_MASTER_INDEX.json** — Machine-readable index
- **COORDINATE_SYSTEMS_HIERARCHY.yaml** — Parent-child relationships

### Category Indices
- **INDEX_GLOBAL.csv** — Global coordinate systems only
- **INDEX_STATIONS.csv** — Station coordinate systems (FS/WL/BL)
- **INDEX_LOCAL.csv** — Local component coordinate systems
- **INDEX_INTERFACES.csv** — Interface coordinate systems
- **INDEX_DATUMS.csv** — Primary datums (A, B, C)

### Cross-Reference Indices
- **INDEX_BY_COMPONENT.csv** — Indexed by component type
- **INDEX_BY_STATION.csv** — Indexed by fuselage station
- **INDEX_BY_INTERFACE.csv** — Indexed by interface designation
- **INDEX_BY_OWNER.csv** — Indexed by responsible engineer/team

## Master Index Structure

The master index includes the following fields:

| Field | Description | Example |
|-------|-------------|---------|
| `id` | Unique identifier | `CS-53-10-001` |
| `name` | Full coordinate system name | `53-10_REF_CS_GLOBAL_BODY` |
| `type` | Type classification | `global`, `station`, `local`, `interface` |
| `category` | Sub-category | `aircraft_body`, `FS`, `frame`, `wing_interface` |
| `origin_x` | X coordinate of origin (mm) | `0.0` |
| `origin_y` | Y coordinate of origin (mm) | `0.0` |
| `origin_z` | Z coordinate of origin (mm) | `0.0` |
| `parent` | Parent coordinate system ID | `CS-GLOBAL-001` |
| `file_path` | Location of definition file | `GLOBAL/AIRCRAFT_BODY/...` |
| `cad_file` | CAD model filename | `53-10_REF_CS_GLOBAL_BODY_v01.CATPart` |
| `owner` | Responsible person/team | `J. Smith / Integration` |
| `status` | Current status | `active`, `draft`, `obsolete` |
| `version` | Current version | `1.2` |
| `date_created` | Creation date | `2024-03-15` |
| `date_modified` | Last modification date | `2024-10-01` |
| `approval_date` | Approval date | `2024-03-20` |
| `description` | Brief description | `Primary aircraft body frame` |

## Index Maintenance

### Adding New Coordinate Systems
When creating a new coordinate system:
1. Assign next sequential ID from master index
2. Create coordinate system files (CAD, definition, transformation)
3. Add entry to master index (CSV and JSON)
4. Update appropriate category index
5. Update hierarchy diagram
6. Commit and push changes

### Updating Existing Coordinate Systems
When modifying a coordinate system:
1. Increment version number
2. Update modification date
3. Update all affected index entries
4. Update transformation definitions if needed
5. Document changes in revision history
6. Update dependent coordinate systems if needed

### Retiring Coordinate Systems
When a coordinate system becomes obsolete:
1. Change status to `obsolete`
2. Add obsolescence date
3. Document replacement coordinate system (if any)
4. Maintain entry in index for historical reference
5. Move CAD files to archive location
6. Update all references in documentation

## Index Usage

### Quick Lookup
Use the master index to quickly find:
- Coordinate system by name or ID
- All coordinate systems of a specific type
- All coordinate systems owned by a team
- All children of a parent coordinate system
- Transformation chains between systems

### Validation
Use the index to verify:
- No duplicate IDs or names
- All parent references exist
- No circular dependencies
- All coordinate systems have valid owners
- All files exist at specified paths

### Reporting
Generate reports from index:
- Active coordinate systems summary
- Coordinate systems by subsystem
- Coordinate systems pending approval
- Recently modified coordinate systems
- Interface coordination status

## Cross-References

- [Parent: COORDINATE_SYSTEMS](../README.md)
- [All Coordinate System Directories](../)
- [Validation Reports](../VALIDATION/REPORTS/)
- [CAI Integration Data](../../../../CAI/INTERFACE_MATRIX/README.md)

## Index Scripts

Automation scripts for index management:
- `generate_index.py` — Regenerate master index from files
- `validate_index.py` — Validate index consistency
- `export_index.py` — Export index to various formats
- `search_index.py` — Search and query index
- `update_index.py` — Update index entries

Location: [`../TRANSFORMS/SCRIPTS/`](../TRANSFORMS/SCRIPTS/)

## Change Control

Index changes follow standard configuration management:
- Minor updates (status, owner): Direct commit
- Structural changes: Review required
- Schema changes: Approval by configuration control board

---

**Owner**: 53-10 Configuration Management + Integration  
**Update frequency**: Continuous (automated nightly regeneration)  
**Validation**: Automated validation on every commit  
**Criticality**: High — Central reference for all coordinate systems
