# CHECKS — BOM Validation and Quality Checks

## Purpose

This directory contains validation checklists, quality check procedures, and automated validation scripts to ensure BOM accuracy, completeness, and compliance.

## Contents

### Validation Checklists
- **Completeness checks**: Required field verification
- **Accuracy checks**: Data validation procedures
- **Consistency checks**: Cross-reference validation
- **Compliance checks**: Standards verification

### Automated Checks
- **Validation scripts**: Automated BOM validation
- **Format checkers**: File format verification
- **Schema validators**: XML/JSON validation
- **Data quality tools**: Anomaly detection

## Check Categories

### Data Completeness
- All required fields populated
- No missing part numbers
- Descriptions provided
- Quantities specified
- Units of measure included
- Material specifications complete

### Data Accuracy
- Valid part numbers
- Correct quantities
- Accurate mass values
- Proper material codes
- Valid supplier references
- Correct drawing references

### Data Consistency
- Quantities match CAD model
- Mass values match specifications
- Part numbers match PLM system
- Drawing references are valid
- Revisions are current

### Format Compliance
- File format correct
- Naming convention followed
- Required columns present
- Data types correct
- Encoding proper (UTF-8)

## Validation Checklist

### Pre-Release BOM Checklist

```
□ All required fields completed
□ Part numbers validated against PLM
□ Quantities verified against CAD model
□ Mass values calculated and reviewed
□ Material specifications confirmed
□ Source (MAKE/BUY) specified for all parts
□ Drawing references checked and valid
□ Supplier information complete (for BUY parts)
□ Revision level correct
□ No duplicate part numbers
□ Hierarchical structure correct
□ Find numbers sequential
□ Total mass calculated and reasonable
□ Cost estimates reviewed (if applicable)
□ Technical review completed
□ Approval signatures obtained
```

## File Naming Convention

```
CHECK_<check-type>_<version>.<ext>
```

Examples:
- `CHECK_COMPLETENESS_v01.xlsx`
- `CHECK_VALIDATION-SCRIPT_v02.py`
- `CHECK_PRE-RELEASE_v01.pdf`

## Automated Validation

### Validation Scripts

Example Python validation script structure:
```python
def validate_bom(bom_file):
    checks = {
        'completeness': check_completeness(bom_file),
        'part_numbers': validate_part_numbers(bom_file),
        'quantities': validate_quantities(bom_file),
        'materials': validate_materials(bom_file),
        'references': validate_references(bom_file)
    }
    return generate_report(checks)
```

### Validation Rules

#### Part Number Validation
- Follows company numbering scheme
- No duplicates in BOM
- Exists in PLM system
- Not obsolete

#### Quantity Validation
- Positive integer values
- Reasonable quantities
- Matches CAD model count
- Consistent with usage

#### Material Validation
- Valid material code
- From approved materials list
- Specifications complete
- Certifications available

#### Mass Validation
- Positive numeric values
- Reasonable for part type
- Total mass within budget
- Consistent with CAD properties

## Quality Metrics

Track BOM quality metrics:
- **Completeness**: Percentage of required fields populated
- **Accuracy**: Error rate in validation
- **Timeliness**: Time to complete checks
- **First-time quality**: BOMs passing first review

## Check Procedures

### Step 1: Initial Validation
- Run automated validation scripts
- Check file format and naming
- Verify required fields present
- Identify obvious errors

### Step 2: Detailed Review
- Verify part number validity
- Check quantities against design
- Validate material specifications
- Review drawing references
- Confirm supplier information

### Step 3: Cross-Reference Checks
- Compare to CAD model
- Verify against PLM data
- Check drawing consistency
- Validate interface BOMs

### Step 4: Final Approval
- Complete checklist
- Resolve all issues
- Obtain technical approval
- Document check results

## Error Resolution

Common errors and resolutions:
- **Missing data**: Request from design team
- **Invalid part numbers**: Correct or create new parts
- **Quantity mismatches**: Verify with CAD model
- **Material errors**: Update with correct specifications
- **Format issues**: Reformat per template

## Documentation

For each validation check:
- Document check date
- Record checker name
- List findings
- Track resolution
- Obtain approval

## Integration

### PLM Integration
- Validate against PLM part master
- Check part lifecycle status
- Verify BOM structure
- Confirm revision levels

### CAD Integration
- Compare quantities with CAD
- Validate mass properties
- Check assembly structure
- Verify part references

## Continuous Improvement

### Process Enhancement
- Track common errors
- Update checklists
- Improve automation
- Enhance validation rules
- Train personnel

## Related Directories

- **Templates**: [../TEMPLATES/](../TEMPLATES/) — BOM templates with validation
- **Revisions**: [../REVISIONS/DRAFT/](../REVISIONS/DRAFT/) — BOMs requiring validation
- **Reports**: [../REPORTS/](../REPORTS/) — Validation results
