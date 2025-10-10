# INDEX — Simplified Configuration Index and Registry

## Purpose

This directory contains index files and registries that track all simplified configurations, their versions, approval status, and relationships to detailed baselines.

## Contents

### Index Files
- **Master index**: Complete listing of all simplified configurations
- **Version registry**: Version tracking for simplified models
- **Approval registry**: Approval status and records
- **Usage matrix**: Use case to model mapping

## Master Index

### Index File Format

The master index should be maintained as a CSV file:

**File**: `SIMPLIFIED_INDEX.csv`

```csv
model_id,model_name,lod_level,version,baseline_ref,file_path,status,approved_date,approved_by,use_cases,notes
53-10-001,CENTER-BODY_COMPLETE,1,v01,53-10_ASM_CB_v05.CATPart,../ASM/53-10_ASM_CENTER-BODY_SIMP_LOD1_v01.CATProduct,Approved,2025-01-15,J.Smith,"Executive review, Space claim",Envelope only
53-10-002,FRAME-SECTION-F01-F05,2,v01,53-10_ASM_FS_v03.asm,../ASM/53-10_ASM_FRAME-SECTION_SIMP_LOD2_v01.asm,Approved,2025-01-20,M.Jones,"Design review, Presentation",Major components simplified
...
```

### Column Definitions

- **model_id**: Unique identifier for simplified model
- **model_name**: Descriptive name
- **lod_level**: Level of detail (1-4)
- **version**: Current version number
- **baseline_ref**: Reference to detailed baseline model
- **file_path**: Relative path to model file
- **status**: Current status (Draft, Under Review, Approved, Superseded, Obsolete)
- **approved_date**: Date of approval (YYYY-MM-DD)
- **approved_by**: Name of approver
- **use_cases**: Comma-separated list of approved use cases
- **notes**: Additional information

## Version Registry

### Version Tracking File

**File**: `VERSION_HISTORY.csv`

```csv
model_id,version,date_created,created_by,changes,baseline_version,validation_status,approval_ref
53-10-001,v01,2025-01-10,J.Smith,Initial creation,v05,Validated,APPR-2025-001
53-10-001,v02,2025-02-15,J.Smith,Updated for new baseline,v06,Validated,APPR-2025-015
53-10-002,v01,2025-01-15,M.Jones,Initial creation,v03,Validated,APPR-2025-002
...
```

### Version Information

Track for each version:
- Creation date and creator
- Changes made from previous version
- Baseline model version reference
- Validation status
- Approval reference number

## Approval Registry

### Approval Tracking File

**File**: `APPROVAL_REGISTRY.csv`

```csv
approval_id,model_id,version,approval_date,creator,reviewer,approver,use_cases,restrictions,expiry_date,status
APPR-2025-001,53-10-001,v01,2025-01-15,J.Smith,K.Lee,R.Brown,"Executive review, Space claim",Not for detailed analysis,2026-01-15,Active
APPR-2025-002,53-10-002,v01,2025-01-20,M.Jones,K.Lee,R.Brown,"Design review, Presentation",Internal use only,2026-01-20,Active
...
```

### Approval Information

Document for each approval:
- Approval ID and date
- Creator, reviewer, and approver names
- Approved use cases
- Usage restrictions
- Expiry date (if applicable)
- Current status

## Usage Matrix

### Use Case Mapping File

**File**: `USAGE_MATRIX.csv`

Map simplified models to approved use cases:

```csv
model_id,model_name,lod_level,executive_review,design_review,stakeholder_presentation,preliminary_analysis,space_claim,manufacturing_planning,notes
53-10-001,CENTER-BODY_COMPLETE,1,Yes,No,Yes,No,Yes,No,Envelope only
53-10-002,FRAME-SECTION-F01-F05,2,Yes,Yes,Yes,No,Yes,No,Major components
53-10-003,WING-ATTACH-INTERFACE,3,No,Yes,Yes,Yes,No,Yes,Moderate detail
...
```

### Use Case Columns

- **executive_review**: Approved for executive reviews
- **design_review**: Approved for technical design reviews
- **stakeholder_presentation**: Approved for stakeholder presentations
- **preliminary_analysis**: Approved for preliminary analysis
- **space_claim**: Approved for space claim studies
- **manufacturing_planning**: Approved for manufacturing planning
- **notes**: Additional use case information

## LOD Level Definitions

### Level of Detail Registry

**File**: `LOD_DEFINITIONS.csv`

```csv
lod_level,name,description,typical_file_size_reduction,typical_use_cases,approval_required
1,Envelope Only,Outer boundary representation only,90-95%,"Executive review, Space claim, High-level layout",Chief Engineer
2,Major Components,Simplified major subassemblies,70-85%,"Design review, Stakeholder presentation, Early analysis",Senior Engineer
3,Moderate Detail,Reduced detail for technical reviews,40-60%,"Technical review, Interface coordination, Assembly planning",Team Lead
4,Full Detail Reference,Full detail retained (reference),0-20%,"Detailed analysis, Manufacturing, As-designed documentation",Not Required
```

## Baseline Mapping

### Baseline Reference File

**File**: `BASELINE_MAPPING.csv`

Track relationship between simplified models and detailed baselines:

```csv
simplified_id,simplified_version,baseline_id,baseline_version,sync_status,last_sync_date,delta_description
53-10-001,v01,53-10_ASM_CB,v05,Synchronized,2025-01-15,None
53-10-001,v02,53-10_ASM_CB,v06,Synchronized,2025-02-15,Updated interfaces
53-10-002,v01,53-10_ASM_FS,v03,Synchronized,2025-01-20,None
53-10-003,v01,53-10_ASM_WI,v04,Out of sync,2025-01-18,Baseline updated v05 on 2025-02-01
...
```

### Synchronization Status

- **Synchronized**: Simplified model current with baseline
- **Out of sync**: Baseline has been updated
- **Under review**: Sync update in progress
- **Superseded**: Simplified model obsolete

## Statistics and Metrics

### Performance Metrics File

**File**: `PERFORMANCE_METRICS.csv`

Track performance improvements:

```csv
model_id,lod_level,detailed_file_size_mb,simplified_file_size_mb,size_reduction_pct,detailed_load_time_s,simplified_load_time_s,load_time_improvement_pct
53-10-001,1,245.3,12.5,94.9,45.2,2.1,95.4
53-10-002,2,156.8,31.4,80.0,32.5,7.8,76.0
53-10-003,3,89.4,44.7,50.0,18.3,9.1,50.3
...
```

### Quality Metrics File

**File**: `QUALITY_METRICS.csv`

Track quality metrics:

```csv
model_id,lod_level,mass_delta_pct,cog_shift_mm,interface_validation,geometry_quality,validation_date,validator
53-10-001,1,2.3,15.5,Pass,Pass,2025-01-14,K.Lee
53-10-002,2,3.1,22.3,Pass,Pass,2025-01-19,K.Lee
53-10-003,3,1.8,8.7,Pass,Pass,2025-01-25,M.Chen
...
```

## Index Maintenance

### Update Procedures

Update indexes when:
- New simplified model created
- Model version updated
- Approval status changes
- Baseline model updated
- Model superseded or obsoleted

### Maintenance Schedule

- **Weekly**: Review for new entries
- **Monthly**: Audit for accuracy
- **Quarterly**: Archive superseded versions
- **Annually**: Purge obsolete entries

## Search and Query

### Finding Models

To find simplified models:
1. Check `SIMPLIFIED_INDEX.csv` for model list
2. Filter by LOD level, use case, or status
3. Review `VERSION_HISTORY.csv` for version details
4. Check `APPROVAL_REGISTRY.csv` for approval status
5. Consult `USAGE_MATRIX.csv` for use case suitability

### Query Examples

**Find all LOD1 models**:
```bash
grep ",1," SIMPLIFIED_INDEX.csv
```

**Find models approved for design review**:
```bash
grep "Design review" SIMPLIFIED_INDEX.csv
```

**Find models needing baseline sync**:
```bash
grep "Out of sync" BASELINE_MAPPING.csv
```

## Reporting

### Monthly Reports

Generate monthly reports containing:
- New simplified models created
- Models approved/updated
- Models needing baseline synchronization
- Performance metrics summary
- Quality metrics summary

### Quarterly Reviews

Conduct quarterly reviews to:
- Validate index accuracy
- Audit approval status
- Review usage patterns
- Identify obsolete models
- Update LOD definitions if needed

## Quality Requirements

Index files must:
- Be maintained under version control
- Be updated within 24 hours of model changes
- Pass CSV validation (no syntax errors)
- Include complete required information
- Cross-reference correctly to other indexes

## Backup and Recovery

- Commit index files to Git
- Tag with major releases
- Maintain backup copies
- Document recovery procedures

## Related Directories

- **Assemblies**: [`../ASM/`](../ASM/) — Simplified model files
- **Documentation**: [`../DOCS/`](../DOCS/) — Approval and validation documents
- **Rules**: [`../RULES/`](../RULES/) — Simplification rules and standards
- **Configuration management**: [`../../../../../../00-PROGRAM/CONFIG_MGMT/`](../../../../../../00-PROGRAM/CONFIG_MGMT/)

## Tools

### Recommended Tools
- **Excel/LibreOffice Calc**: For editing CSV files
- **csvkit**: Command-line CSV tools
- **Python pandas**: For automated processing
- **Git**: For version control
