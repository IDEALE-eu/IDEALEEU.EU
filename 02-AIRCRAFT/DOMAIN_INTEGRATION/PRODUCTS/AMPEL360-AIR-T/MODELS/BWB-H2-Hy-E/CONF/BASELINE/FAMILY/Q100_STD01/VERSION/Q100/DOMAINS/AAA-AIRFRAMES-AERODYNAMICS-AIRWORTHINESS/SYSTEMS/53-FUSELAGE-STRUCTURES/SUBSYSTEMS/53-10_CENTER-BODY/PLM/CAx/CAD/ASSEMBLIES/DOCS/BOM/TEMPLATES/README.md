# TEMPLATES — BOM Templates and Standards

## Purpose

This directory contains standardized BOM templates, formats, and guidelines to ensure consistency and completeness across all BOM documentation.

## Contents

### BOM Templates
- **CSV templates**: Standard CSV BOM format
- **Excel templates**: Formatted Excel workbooks
- **XML templates**: XML schema and examples
- **JSON templates**: JSON structure templates

### Document Templates
- **Cover sheets**: BOM package cover pages
- **Approval forms**: BOM approval documentation
- **Change forms**: BOM change request forms
- **Report templates**: Standard report formats

## Template Types

### Basic BOM Template
Standard columns and structure:
```csv
part_number,description,quantity,uom,material,mass_kg,source,find_number,reference,revision,notes
```

### Engineering BOM (EBOM) Template
Design-focused structure:
- Part hierarchy
- Design specifications
- Engineering notes
- Reference drawings

### Manufacturing BOM (MBOM) Template
Production-focused structure:
- Assembly sequence
- Work center assignments
- Process steps
- Tooling requirements

### As-Built BOM Template
Configuration documentation:
- Serial number applicability
- Actual part numbers used
- Deviations and substitutions
- Installation dates

## Excel Template Structure

### Standard Worksheets
1. **BOM**: Main bill of materials
2. **Summary**: Totals and statistics
3. **Revision History**: Change tracking
4. **Instructions**: Template usage guide
5. **Validation**: Data validation rules

### Template Features
- Protected cells for formulas
- Data validation dropdowns
- Conditional formatting
- Automatic calculations
- Print formatting

## File Naming Convention

```
TEMPLATE_BOM_<type>_<format>_<version>.<ext>
```

Examples:
- `TEMPLATE_BOM_EBOM_CSV_v01.csv`
- `TEMPLATE_BOM_MBOM_EXCEL_v02.xlsx`
- `TEMPLATE_BOM_STANDARD_XML_v01.xml`
- `TEMPLATE_BOM_STANDARD_JSON_v01.json`

## Template Usage

### Creating New BOM
1. Select appropriate template
2. Make a copy (do not edit template)
3. Rename with project-specific name
4. Fill in BOM data
5. Validate completeness
6. Save in appropriate directory

### Template Customization
- Modify for project-specific needs
- Maintain core structure
- Document customizations
- Get approval for significant changes
- Update template version

## Standard Fields

### Required Fields
- **Part number**: Unique identifier
- **Description**: Part name/description
- **Quantity**: Number required
- **UOM**: Unit of measure
- **Material**: Material specification
- **Source**: MAKE or BUY

### Optional Fields
- Mass/weight
- Cost
- Supplier
- Lead time
- Drawing reference
- Revision
- Notes

## Data Validation

Templates should include:
- Required field validation
- Data type checking
- Format validation
- Range checking
- Consistency rules

## Quality Standards

Templates must support:
- Complete information capture
- Consistent formatting
- Accurate calculations
- Traceability
- Change tracking
- Approval workflow

## Template Maintenance

### Version Control
- Track template versions
- Document changes
- Maintain backward compatibility
- Communicate updates

### Updates
Templates updated for:
- Process improvements
- New requirements
- User feedback
- Standards changes
- Tool compatibility

## Documentation

Each template should include:
- **Purpose**: Template intent and use
- **Instructions**: How to use template
- **Field definitions**: Explanation of each field
- **Validation rules**: Data quality requirements
- **Examples**: Sample completed BOM

## Validation Rules

Standard validation rules:
- Part numbers follow numbering scheme
- Quantities are positive integers
- Material codes from approved list
- Source is MAKE or BUY
- Mass values are numeric
- References link to valid documents

## Related Directories

- **Formats**: [../FORMATS/](../FORMATS/) — Format-specific BOMs
- **Checks**: [../CHECKS/](../CHECKS/) — Validation checklists
- **Examples**: Use [../PARTS/](../PARTS/) and [../ASSEMBLIES/](../ASSEMBLIES/) for reference examples

## Standards Reference

Templates comply with:
- ISO 16792: Digital product definition
- AS9102: First article inspection requirements
- Internal PLM standards
- Industry best practices
