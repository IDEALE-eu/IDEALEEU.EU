# FORMATS — BOM File Formats

## Purpose

This directory organizes BOMs by file format, facilitating format-specific processing, integration, and distribution.

## Directory Structure

```
FORMATS/
├── CSV/    — Comma-separated values (machine-readable)
├── XLSX/   — Excel spreadsheets (formatted with calculations)
├── XML/    — Extensible markup language (PLM integration)
└── JSON/   — JavaScript object notation (API/web integration)
```

## Format Selection

### CSV Format
- **Use for**: Version control, scripting, data processing
- **Advantages**: Simple, universal, diff-friendly
- **Best for**: Automated workflows, git tracking

### XLSX Format
- **Use for**: Review, analysis, reporting
- **Advantages**: Formatting, calculations, readability
- **Best for**: Engineering review, manual editing

### XML Format
- **Use for**: PLM system integration
- **Advantages**: Structured, validated, industry standard
- **Best for**: System-to-system data exchange

### JSON Format
- **Use for**: Web applications, APIs
- **Advantages**: Lightweight, modern, web-friendly
- **Best for**: Digital tools, dashboards, web services

## Format Synchronization

All formats should contain equivalent data:
- Same BOM content across formats
- Synchronized revisions
- Consistent naming conventions
- Maintained in parallel

## File Naming Convention

Maintain consistent naming across formats:
```
53-10_BOM_<assembly-id>_<bom-type>_<revision>.<ext>
```

## Format Conversion

### Conversion Guidelines
- Convert from authoritative source format
- Validate after conversion
- Maintain data integrity
- Document conversion process

### Authoritative Format
- Define one format as source of truth (typically CSV)
- Generate other formats from authoritative source
- Ensure consistency across formats

## Integration

### PLM Systems
- XML/JSON for PLM import/export
- Maintain PLM system synchronization
- Track PLM item references

### ERP Systems
- CSV/Excel for ERP integration
- Material requirements planning
- Procurement automation

### Version Control
- CSV preferred for git repositories
- Human-readable diffs
- Merge-friendly format

## Related Directories

- **Revisions**: [../REVISIONS/](../REVISIONS/) — BOM lifecycle management
- **Templates**: [../TEMPLATES/](../TEMPLATES/) — Format templates
- **Checks**: [../CHECKS/](../CHECKS/) — Format validation
