# VARIANCE — BOM Variance Reports

## Purpose

This directory contains variance reports analyzing changes, differences, and deviations in BOMs across revisions, configurations, and actual vs. planned states.

## Report Types

### BOM Change Reports
- Changes between revisions
- Added/deleted/modified parts
- Quantity changes
- Specification changes
- Impact analysis

### As-Designed vs. As-Built Reports
- Design intent vs. actual production
- Configuration differences
- Substitutions and deviations
- Field changes
- Non-conformances

### Supplier Deviation Reports
- Supplier-proposed changes
- Material substitutions
- Process variations
- Dimensional deviations
- Impact assessments

### Configuration Variance Reports
- Aircraft-to-aircraft differences
- Option variations
- Customer-specific configurations
- Effectivity tracking

## File Naming Convention

```
53-10_VAR_<variance-type>_<comparison>_<date>.<ext>
```

Examples:
- `53-10_VAR_BOM-CHANGES_r001-to-r002_20240315.pdf`
- `53-10_VAR_AS-BUILT_S001_20240320.xlsx`
- `53-10_VAR_SUPPLIER-DEV_ACME-MFG_20240322.pdf`
- `53-10_VAR_CONFIG_OPT-A-vs-OPT-B_20240325.xlsx`

## BOM Change Report

### Report Sections
1. **Summary**: Overview of changes
2. **Added Parts**: New components
3. **Deleted Parts**: Removed components
4. **Modified Parts**: Changed specifications or quantities
5. **Impact Analysis**: Downstream effects

### Change Categories
- **Design changes**: Engineering modifications
- **Substitutions**: Alternative parts
- **Corrections**: Error fixes
- **Updates**: Specification updates

### Change Details
For each change, document:
- Part number and description
- Type of change (add/delete/modify)
- Old vs. new values
- Reason for change
- Engineering change reference
- Impact assessment
- Effectivity

## As-Designed vs. As-Built Report

### Comparison Sections
1. **Configuration Baseline**: Design intent BOM
2. **Actual Configuration**: As-built BOM
3. **Variances**: Differences identified
4. **Root Cause**: Reasons for variances
5. **Disposition**: Resolution actions

### Variance Categories
- **Approved deviations**: Authorized changes
- **Field changes**: Production modifications
- **Substitutions**: Alternative parts used
- **Errors**: Unintended differences
- **Non-conformances**: Quality issues

### Traceability
Link variances to:
- Engineering changes
- Deviation approvals
- Non-conformance reports
- Field service bulletins
- Configuration records

## Supplier Deviation Report

### Report Content
1. **Deviation Description**: Proposed change details
2. **Technical Impact**: Engineering assessment
3. **Quality Impact**: Quality considerations
4. **Schedule Impact**: Delivery effects
5. **Cost Impact**: Financial implications
6. **Recommendation**: Approve/reject decision

### Review Process
1. Receive supplier deviation request
2. Technical evaluation
3. Impact assessment
4. Decision and approval
5. BOM update (if approved)
6. Documentation

## Configuration Variance Report

### Comparison Scope
- Standard vs. optional configurations
- Customer-specific variations
- Production sequence changes
- Obsolescence replacements

### Report Elements
- Configuration identifiers
- Part differences
- Effectivity tracking
- Interchangeability analysis
- Maintenance implications

## Variance Metrics

Standard variance metrics:
- Number of changes
- Change frequency
- Most changed parts
- Change impact severity
- Time to resolve variances

## Impact Analysis

Assess impact of variances on:
- Performance
- Weight and balance
- Cost
- Schedule
- Certification
- Maintainability
- Interchangeability

## Disposition

For each variance:
- Accept as-is
- Rework to design
- Request design change
- Obtain deviation approval
- Update documentation

## Usage

Variance reports support:
- Change control
- Configuration management
- Quality assurance
- Supplier management
- Certification compliance
- Audit traceability

## Related Directories

- **Summary**: [../SUMMARY/](../SUMMARY/) — Summary reports
- **Revisions**: [../../REVISIONS/](../../REVISIONS/) — BOM revisions
- **Checks**: [../../CHECKS/](../../CHECKS/) — Validation procedures
