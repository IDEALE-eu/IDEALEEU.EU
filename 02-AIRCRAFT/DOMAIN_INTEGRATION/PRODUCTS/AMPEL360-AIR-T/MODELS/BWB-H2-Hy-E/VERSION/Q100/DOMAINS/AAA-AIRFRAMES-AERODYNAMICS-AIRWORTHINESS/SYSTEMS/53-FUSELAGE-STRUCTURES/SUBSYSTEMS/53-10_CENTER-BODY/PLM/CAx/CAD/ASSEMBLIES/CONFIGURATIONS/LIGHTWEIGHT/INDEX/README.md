# INDEX — Configuration Index and Catalog

## Purpose

This directory contains index files and catalogs that track all lightweight configurations, their versions, and relationships.

## Contents

### Index Types
- **Master index**: Complete catalog of all lightweight configurations
- **Version history**: Tracking of configuration evolution
- **Dependency map**: Relationships between files and configurations
- **Usage matrix**: Which configurations are used where
- **Status tracking**: Active, deprecated, or archived configurations

## Naming Convention

Use the following pattern:
```
53-10_INDEX_<index-type>_<date>.<ext>
```

Examples:
- `53-10_INDEX_master_2024-10-09.csv`
- `53-10_INDEX_version-history_2024-10-09.xlsx`
- `53-10_INDEX_dependencies_2024-10-09.json`

## Master Index Structure

### CSV Format
```csv
ConfigID,Name,Version,Date,Author,Status,FileLocation,Purpose
LW-001,Center Body LW,v01,2024-10-09,J.Smith,Active,ASM/53-10_ASM_CENTER-BODY_LW_v01.CATProduct,General use
LW-002,Frame Section LW,v01,2024-10-09,M.Johnson,Active,ASM/53-10_ASM_FRAME-SECTION_LW_v01.asm,Reviews
LW-003,Skin Panel LW,v01,2024-10-09,K.Lee,Active,ASM/53-10_ASM_SKIN-PANEL_LW_v01.sldasm,Collaboration
```

### JSON Format
```json
{
  "configurations": [
    {
      "id": "LW-001",
      "name": "Center Body Lightweight",
      "version": "v01",
      "created": "2024-10-09",
      "author": "J.Smith",
      "status": "active",
      "files": {
        "assembly": "ASM/53-10_ASM_CENTER-BODY_LW_v01.CATProduct",
        "suppression": "SUPPRESSION/53-10_SUPP_CENTER-BODY_fasteners_v01.txt",
        "viewState": "VIEW_STATES/53-10_VIEW_CENTER-BODY_low-detail_v01.catview"
      },
      "performance": {
        "fileSize": "45MB",
        "loadTime": "12s",
        "memory": "2.1GB"
      },
      "purpose": "General design work and collaboration"
    }
  ]
}
```

## Version History Tracking

Track configuration evolution:
- **Version number**: Incremental version tracking
- **Date created**: When version was created
- **Author**: Who created the version
- **Changes**: What changed from previous version
- **Baseline**: Link to full-detail baseline
- **Status**: Active, superseded, deprecated, archived

## Dependency Mapping

Document relationships:
- **Assembly to parts**: Which parts are in which assemblies
- **Rules to configs**: Which rules define which configurations
- **Exports to sources**: Which exports came from which native files
- **Views to assemblies**: Which view states apply to which assemblies

## Usage Matrix

Track where configurations are used:
- **Design activities**: Which teams use which configs
- **Reviews**: Which configs are used in design reviews
- **Collaboration**: Which configs are shared externally
- **Analysis**: Which configs are used for specific analyses

## Status Categories

### Active
- Currently in use
- Up to date with baseline
- Maintained and supported
- Available for use

### Deprecated
- Superseded by newer version
- No longer recommended
- Maintained for legacy support
- Scheduled for archival

### Archived
- No longer in active use
- Preserved for historical reference
- Read-only access
- Not maintained

## Maintenance Schedule

### Weekly
- Update master index with new configurations
- Verify file locations and availability
- Check for orphaned or missing files

### Monthly
- Review configuration usage
- Identify candidates for deprecation
- Update performance benchmarks
- Validate dependency maps

### Quarterly
- Audit all configurations
- Archive obsolete versions
- Update documentation
- Review and optimize catalog structure

## Index Reports

Generate reports such as:
- **Configuration summary**: Count by status, age, usage
- **Storage analysis**: Total file sizes, growth trends
- **Usage statistics**: Most/least used configurations
- **Quality metrics**: Validation status, approval dates

## Best Practices

### Index Management
- Keep index files current (update weekly)
- Use consistent naming conventions
- Document all relationships
- Automate index updates where possible
- Backup index files regularly

### Configuration Tracking
- Assign unique IDs to each configuration
- Link to source baseline models
- Document optimization applied
- Track approval and validation status
- Maintain complete history

## Related Directories

- **Assembly files**: [`../ASM/`](../ASM/)
- **Part files**: [`../PARTS/`](../PARTS/)
- **Documentation**: [`../DOCS/`](../DOCS/)
- **Exports**: [`../EXPORTS/`](../EXPORTS/)
- **All other subdirectories**: Reference complete structure
