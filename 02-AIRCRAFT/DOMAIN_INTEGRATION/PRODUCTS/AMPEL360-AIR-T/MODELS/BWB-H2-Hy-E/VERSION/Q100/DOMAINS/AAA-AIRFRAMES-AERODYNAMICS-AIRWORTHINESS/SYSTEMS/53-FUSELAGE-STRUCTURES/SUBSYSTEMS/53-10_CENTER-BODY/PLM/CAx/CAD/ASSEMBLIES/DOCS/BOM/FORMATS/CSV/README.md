# CSV — Comma-Separated Values BOMs

## Purpose

This directory contains BOMs in CSV (Comma-Separated Values) format, optimized for version control, automated processing, and data exchange.

## Format Characteristics

### Advantages
- **Machine-readable**: Easy to parse and process
- **Version control friendly**: Clean diffs in git
- **Universal**: Supported by all tools
- **Scriptable**: Simple to automate
- **Portable**: Platform-independent

### Use Cases
- Version control tracking
- Automated validation scripts
- Data import/export
- Batch processing
- Integration pipelines

## CSV Structure

### Standard BOM Columns
```csv
part_number,description,quantity,uom,material,mass_kg,source,find_number,reference
```

### Example
```csv
part_number,description,quantity,uom,material,mass_kg,source,find_number,reference
53-10-001,Center Frame Assembly,1,EA,AL7075-T6,125.5,MAKE,1,DWG-53-10-001
53-10-002,Bulkhead Forward,2,EA,AL2024-T3,45.2,MAKE,2,DWG-53-10-002
HW-B-001,Bolt M8x30,48,EA,STEEL,0.025,BUY,3,AN3-5A
```

## File Naming Convention

```
53-10_BOM_<assembly-id>_<bom-type>_<revision>.csv
```

Examples:
- `53-10_BOM_CENTER-BODY_EBOM_r002.csv`
- `53-10_BOM_FRAME-F05_MBOM_r003.csv`

## Best Practices

### Formatting
- Use standard comma delimiter
- Quote fields containing commas
- UTF-8 encoding
- Unix line endings (LF)
- No trailing whitespace

### Data Integrity
- Consistent column order
- Required fields always populated
- Valid part numbers
- Numeric values without units in data
- Units specified in column headers

## Validation

CSV files should be validated for:
- Valid CSV syntax
- Required columns present
- Data type correctness
- No duplicate part numbers
- Referential integrity

## Processing

### Reading CSV BOMs
```python
import csv

with open('53-10_BOM_CENTER-BODY_EBOM_r002.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        part_number = row['part_number']
        quantity = int(row['quantity'])
        # Process BOM data
```

## Related Directories

- **XLSX**: [../XLSX/](../XLSX/) — Excel format BOMs
- **XML**: [../XML/](../XML/) — XML format BOMs
- **Templates**: [../../TEMPLATES/](../../TEMPLATES/) — CSV BOM templates
