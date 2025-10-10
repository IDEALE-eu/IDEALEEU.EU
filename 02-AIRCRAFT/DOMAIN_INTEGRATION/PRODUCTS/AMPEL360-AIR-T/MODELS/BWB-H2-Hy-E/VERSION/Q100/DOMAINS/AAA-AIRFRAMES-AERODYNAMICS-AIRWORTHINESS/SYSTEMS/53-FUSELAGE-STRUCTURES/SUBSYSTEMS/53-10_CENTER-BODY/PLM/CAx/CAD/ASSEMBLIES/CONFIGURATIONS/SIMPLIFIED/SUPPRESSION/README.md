# SUPPRESSION — Feature Suppression Records

## Purpose

This directory contains records and documentation of feature suppression applied to create simplified models.

## Contents

### Suppression Records
- **Suppression lists**: Features suppressed in each model
- **Suppression rules**: Criteria for feature suppression
- **Impact assessments**: Effects of suppression on model behavior
- **Validation records**: Testing results for suppressed configurations

## What to Document

### For Each Simplified Model
Document the following suppression details:

#### Suppressed Features
- List of features suppressed by name/ID
- Reason for suppression
- Impact on mass properties
- Impact on external interfaces
- Visual impact

#### Suppression Method
- CAD system suppression function used
- Manual deletion vs. parametric suppression
- Reversibility of suppression
- Dependencies affected

## Suppression Categories

### Geometry Features
**Typically Suppressed**:
- Small fillets and chamfers
- Cosmetic features
- Mounting boss details
- Non-structural ribs
- Threaded holes
- Text/engravings

**Never Suppress**:
- External interfaces
- Mounting datums
- Critical dimensions
- Load-bearing features

### Components
**Typically Suppressed**:
- Fasteners (screws, rivets, clips)
- O-rings and seals
- Labels and placards
- Non-structural brackets
- Cable routing clips
- Inspection covers

**Never Suppress**:
- Primary structure
- Interface fittings
- Load paths
- Major assemblies

### Assembly Features
**Typically Suppressed**:
- Mating constraints (simplified)
- Pattern instances (reduced)
- Reference geometry
- Construction planes/axes

**Maintain**:
- Assembly structure
- Component relationships
- Interface definitions

## Suppression Levels by LOD

### LOD1 (Envelope Only)
Suppress everything except:
- Outer bounding envelope
- Interface mounting points
- Coordinate system

### LOD2 (Major Components)
Suppress:
- All internal features
- Fastener details
- Small features < 10mm
- Non-critical components

### LOD3 (Moderate Detail)
Suppress:
- Features < 5mm
- Fastener thread details
- Cosmetic features
- Hidden internal components

### LOD4 (Full Detail)
Minimal suppression:
- Only for performance if needed
- Document any suppressions
- Justify necessity

## File Naming Convention

Use the following pattern:
```
53-10_SUPP_<model-id>_LOD<level>_<version>.csv
```

Examples:
- `53-10_SUPP_CENTER-BODY_LOD1_v01.csv`
- `53-10_SUPP_FRAME-F01_LOD2_v02.csv`

## CSV Format

Suppression records should be in CSV format with the following columns:

```csv
feature_id,feature_name,feature_type,suppression_reason,mass_impact_kg,interface_impact,notes
F001,Fillet_R2,Fillet,LOD1_cosmetic,0.001,None,Small corner fillet
C012,Screw_M6,Fastener,LOD1_detail,0.012,None,Mounting screw
...
```

### Column Definitions
- **feature_id**: Unique feature identifier from CAD system
- **feature_name**: Descriptive feature name
- **feature_type**: Category (fillet, hole, component, etc.)
- **suppression_reason**: Why suppressed (LOD level, type)
- **mass_impact_kg**: Mass change in kilograms
- **interface_impact**: Effect on interfaces (None, Minor, Critical)
- **notes**: Additional comments

## Mass Property Tracking

### Before vs. After Comparison
Document for each simplified model:
- **Original mass**: From detailed model
- **Suppressed mass**: After suppression
- **Delta**: Difference in kg and %
- **COG shift**: Center of gravity change (mm)
- **MOI change**: Moment of inertia change (if relevant)

### Acceptance Criteria
- Mass delta < 5% for LOD2-3
- Mass delta < 10% for LOD1
- COG shift < 50mm
- No impact on external interfaces

## Validation Records

### Suppression Validation
For each suppressed configuration:
- [ ] Model loads without errors
- [ ] External interfaces unchanged
- [ ] Mass properties within tolerance
- [ ] Performance improvement achieved
- [ ] Visual quality acceptable
- [ ] Approved for intended use case

### Test Results
Document:
- Load time improvement (%)
- File size reduction (MB)
- Memory usage reduction (MB)
- Display performance improvement

## Change Control

### Suppression Changes
When modifying suppression:
1. Document changes in new version
2. Re-validate model
3. Update mass property comparison
4. Re-approve for use cases
5. Update this documentation

### Baseline Updates
When detailed baseline changes:
1. Review suppression list
2. Identify new features to suppress
3. Re-apply suppression rules
4. Validate results
5. Update records

## Quality Requirements

### Documentation Quality
- Complete suppression records for all simplified models
- CSV files validated and error-free
- Mass property deltas calculated accurately
- Approval signatures on file

### Traceability
- Link to detailed baseline model
- Reference simplified model version
- Cross-reference to approval documentation
- Maintain change history

## Related Directories

- **Assemblies**: [`../ASM/`](../ASM/) — Simplified models
- **Rules**: [`../RULES/`](../RULES/) — Suppression rules and guidelines
- **Documentation**: [`../DOCS/`](../DOCS/) — Approval documentation
- **View states**: [`../VIEW_STATES/`](../VIEW_STATES/) — Display configurations
