# PARTS_LISTS — Assembly Parts Lists

## Purpose

This directory contains detailed parts lists organized by kit for assembly operations of the 53-10 Center Body.

## Contents

### Parts List Types
- Operation parts lists
- Sub-assembly parts lists
- Kit parts lists with quantities
- Consumables lists

## Parts List Format

### Information to Include
- Part number
- Part description
- Quantity per kit
- Unit of measure
- Material specification
- Source (stock, fabricated, purchased)
- Storage location
- Special handling requirements

### Example Format
```
Kit: K001 - Frame F05 Installation
Part No.        Description              Qty  UOM  Location
53-10-100-001   Frame F05               1    EA   Assy-A-001
53-10-200-005   Stringer Assy           4    EA   Assy-A-002
NAS1097-6       Rivet, 6mm              48   EA   Hardware-H-010
PR-1422-B2      Sealant                 1    Tube Chemical-C-005
```

## Naming Convention

Use the following pattern:
```
53-10_PARTS-LIST_<kit-id>_<description>_<version>.<ext>
```

Examples:
- `53-10_PARTS-LIST_K001_FRAME-F05_v01.xlsx`
- `53-10_PARTS-LIST_K002_FASTENERS_v02.xlsx`
- `53-10_PARTS-LIST_K003_CONSUMABLES_v01.xlsx`

## Parts List Management

### Creation
- Extract from BOM
- Organize by operation/kit
- Add storage locations
- Include special handling
- Validate quantities

### Maintenance
- Update with design changes
- Track revisions
- Maintain effectivity
- Link to BOM changes
- Version control

## Integration

### With BOM
- Linked to master BOM
- Synchronized with EBOM/MBOM
- Updated with ECOs
- Maintain traceability

### With Inventory
- Reference storage locations
- Track part availability
- Support pull lists
- Enable replenishment

## Related Directories

- **Layouts**: [`../LAYOUTS/`](../LAYOUTS/) — Kit layout drawings
- **BOM**: [`../../BOM/`](../../BOM/) — Master bills of materials
