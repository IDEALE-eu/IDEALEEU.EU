# BOM — Bills of Materials

## Purpose

This directory contains Bills of Materials (BOMs) extracted from CAD assembly models, listing all components, quantities, and specifications for the 53-10 Center Body.

## Contents

### BOM Types
- **Engineering BOM (EBOM)**: Design intent component list
- **Manufacturing BOM (MBOM)**: Production component list with process steps
- **As-Designed BOM**: Current design configuration
- **As-Built BOM**: Actual manufactured configuration

## BOM Structure

### Hierarchical BOM
- Top-level assembly
- Sub-assemblies (indented)
- Components and parts
- Raw materials and stock

### BOM Information

Each BOM entry should include:
- Part number
- Part name/description
- Quantity required
- Unit of measure
- Material specification
- Reference designator
- Find number
- Source (make/buy)
- Mass (individual and total)

## File Formats

### Supported Formats
- **CSV**: Machine-readable, version control friendly
- **Excel**: Formatted with calculations
- **PDF**: Approved documentation
- **XML/PLM**: Integration with PLM systems

## Naming Convention

Use the following pattern:
```
53-10_BOM_<assembly-id>_<bom-type>_<version>.<ext>
```

Examples:
- `53-10_BOM_CENTER-BODY_EBOM_v01.csv`
- `53-10_BOM_FRAME-SECTION-F05_MBOM_v02.xlsx`
- `53-10_BOM_WING-ATTACH_AS-BUILT_S001_v01.pdf`

## BOM Generation

BOMs should be:
- Extracted directly from CAD assemblies
- Validated against component models
- Cross-referenced with part master data
- Synchronized with assembly versions

## BOM Maintenance

### Configuration Control
- Track BOM revisions
- Document changes from previous version
- Obtain approval for changes
- Maintain effectivity tracking

### Quality Checks
- Verify part numbers are valid
- Confirm quantities are accurate
- Check material specifications
- Validate mass properties
- Ensure completeness

## BOM Usage

### Design
- Component tracking
- Mass budget management
- Cost estimation
- Supplier selection

### Manufacturing
- Material procurement
- Production planning
- Kitting and staging
- Work order generation

### Maintenance
- Spare parts identification
- Repair procedures
- Configuration management
- Traceability

## Integration

### PLM Integration
- Link to PLM part master
- Synchronize with EBOM structure
- Track engineering changes
- Maintain configuration baselines

### ERP Integration
- Material requirements planning
- Procurement automation
- Inventory management
- Cost accounting

## Standards Compliance

Follow:
- **ISO 16792**: Digital product definition
- **AS9102**: First Article Inspection BOM requirements
- **Internal PLM procedures**: Company BOM standards

## Related Directories

- **Assembly models**: [`../../TOP_LEVEL/`](../../TOP_LEVEL/)
- **Sub-assemblies**: [`../../SUB_ASSEMBLIES/`](../../SUB_ASSEMBLIES/)
- **Component models**: [`../../../MODELS/`](../../../MODELS/)
- **PLM EBOM links**: [`../../../../EBOM_LINKS.md`](../../../../EBOM_LINKS.md)
