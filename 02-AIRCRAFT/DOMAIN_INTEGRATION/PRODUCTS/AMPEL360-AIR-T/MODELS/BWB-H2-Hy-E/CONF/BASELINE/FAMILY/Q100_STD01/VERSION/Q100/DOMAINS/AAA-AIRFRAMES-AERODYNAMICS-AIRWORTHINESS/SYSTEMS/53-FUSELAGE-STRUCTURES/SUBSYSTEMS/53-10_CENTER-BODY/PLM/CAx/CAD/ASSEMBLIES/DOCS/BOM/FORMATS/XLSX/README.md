# XLSX — Excel Spreadsheet BOMs

## Purpose

This directory contains BOMs in Microsoft Excel format (XLSX), optimized for human readability, formatting, and interactive analysis.

## Format Characteristics

### Advantages
- **Human-readable**: Clear formatting and layout
- **Calculations**: Built-in formulas and totals
- **Formatting**: Colors, borders, conditional formatting
- **Charts**: Visual data representation
- **Familiar**: Widely used and understood

### Use Cases
- Engineering review and approval
- Manual data entry and editing
- Financial analysis and costing
- Presentation and reporting
- Stakeholder communication

## Spreadsheet Structure

### Typical Layout
- **Header rows**: Title, assembly info, revision
- **Column headers**: Part number, description, qty, etc.
- **Data rows**: BOM line items
- **Summary rows**: Totals, mass rollup
- **Additional sheets**: Notes, revision history, approvals

### Standard Sheets
1. **BOM**: Main bill of materials
2. **Summary**: Totals and statistics
3. **Revision History**: Change log
4. **Notes**: Additional information
5. **Approvals**: Sign-off documentation

## File Naming Convention

```
53-10_BOM_<assembly-id>_<bom-type>_<revision>.xlsx
```

Examples:
- `53-10_BOM_CENTER-BODY_EBOM_r002.xlsx`
- `53-10_BOM_FRAME-F05_MBOM_r003.xlsx`
- `53-10_BOM_WING-ATTACH_AS-BUILT_S001_r001.xlsx`

## Best Practices

### Formatting
- Use table formatting for BOM data
- Apply consistent cell styles
- Lock header rows
- Use freeze panes
- Conditional formatting for status

### Formulas
- Calculate subtotals and totals
- Mass rollup calculations
- Quantity validations
- Cost calculations
- Part count summaries

### Data Validation
- Dropdown lists for source (MAKE/BUY)
- Restricted input for critical fields
- Data validation rules
- Protected cells for calculated values

## Quality Features

### Built-in Validation
- Formula-based checks
- Conditional formatting for errors
- Data validation constraints
- Protected calculation cells

### Traceability
- Revision history sheet
- Change tracking
- Author and date stamps
- Approval signatures

## Export Guidelines

### Converting to CSV
- Export main BOM sheet only
- Remove formatting
- Validate data integrity
- Check for formula errors

## Compatibility

### Excel Versions
- Save in XLSX format (not XLS)
- Avoid Excel-specific features
- Test in Excel and LibreOffice
- Document any macro usage

## Related Directories

- **CSV**: [../CSV/](../CSV/) — CSV format BOMs
- **Templates**: [../../TEMPLATES/](../../TEMPLATES/) — Excel BOM templates
- **Checks**: [../../CHECKS/](../../CHECKS/) — Validation procedures
