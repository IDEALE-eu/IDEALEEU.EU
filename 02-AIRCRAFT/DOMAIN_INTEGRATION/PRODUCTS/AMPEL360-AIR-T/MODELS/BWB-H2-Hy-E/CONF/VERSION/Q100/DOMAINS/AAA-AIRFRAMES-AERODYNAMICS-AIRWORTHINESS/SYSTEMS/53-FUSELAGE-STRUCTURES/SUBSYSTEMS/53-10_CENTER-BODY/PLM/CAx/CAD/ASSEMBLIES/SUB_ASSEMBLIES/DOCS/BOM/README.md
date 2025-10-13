# BOM — Bills of Materials

## Purpose

This directory contains Bills of Materials (BOMs) for all 53-10 Center Body sub-assemblies. BOMs provide complete part lists with quantities, descriptions, and associated metadata for manufacturing, procurement, and assembly.

## BOM Types

### Engineering BOM (EBOM)
- **Design structure**: As-designed part hierarchy
- **Engineering parts**: All components in the design
- **Reference designators**: Part identifiers in assembly
- **Design attributes**: Engineering specifications

### Manufacturing BOM (MBOM)
- **Production structure**: As-built part hierarchy
- **Manufacturing parts**: Parts as procured or fabricated
- **Process steps**: Manufacturing operations
- **Tooling references**: Required manufacturing aids

### As-Maintained BOM
- **Maintenance structure**: Serviceable assemblies and components
- **Spare parts**: Replaceable items
- **Maintenance procedures**: Service instructions
- **Part interchangeability**: Alternate parts and substitutions

## BOM Format

Standard BOM format (CSV or Excel):

| Level | Item | Part Number | Description | Quantity | Unit | Material | Weight | Source | Notes |
|-------|------|-------------|-------------|----------|------|----------|--------|--------|-------|
| 1 | 1 | 53-10-ASM-F05 | Frame Section F05 | 1 | EA | Assembly | 45.2 kg | Internal | Top assembly |
| 2 | 1.1 | 53-10-FRM-F05 | Frame F05 | 1 | EA | 7075-T6 | 12.5 kg | Machined | Primary frame |
| 2 | 1.2 | 53-10-STR-L01 | Stringer L01 | 4 | EA | 7075-T6 | 2.8 kg | Extrusion | Upper stringers |

## Naming Convention

Use the following pattern for BOM files:
```
53-10_BOM_<assembly>_v<version>.<ext>
```

Examples:
- `53-10_BOM_FRAME-SECTION-F05_v01.xlsx`
- `53-10_BOM_STRINGER-BAY-L01_v02.csv`
- `53-10_BOM_COMPLETE-CENTER-BODY_v01.pdf`

## BOM Content Requirements

### Mandatory Fields
- **Part number**: Unique identifier for each part
- **Description**: Clear part description
- **Quantity**: Number required in assembly
- **Unit of measure**: EA (each), M (meter), KG (kilogram), etc.
- **Material**: Material specification
- **Source**: Manufactured, purchased, or standard part

### Recommended Fields
- **Weight**: Individual part weight and total weight
- **Drawing reference**: Engineering drawing number
- **Specification**: Material or process specifications
- **Supplier**: Preferred supplier or manufacturer
- **Lead time**: Procurement or manufacturing lead time
- **Cost**: Unit cost and extended cost (if available)
- **Notes**: Special requirements or instructions

## BOM Levels

### Level 0 - Top Assembly
- Complete aircraft or major assembly
- Highest level in structure

### Level 1 - Major Sub-Assemblies
- Frame sections, floor modules, bulkheads
- Main assemblies in product structure

### Level 2 - Detail Assemblies
- Frame with clips, skin panel with doublers
- Lower-level assemblies

### Level 3+ - Components
- Individual parts: frames, skins, fasteners
- Lowest level detail parts

## BOM Rollup

BOM rollup provides totals:
- **Total part count**: Number of unique parts
- **Total quantity**: Sum of all quantities
- **Total weight**: Rolled-up assembly weight
- **Total cost**: Rolled-up assembly cost (if available)

## Related Directories

- **Frame sections**: [`../../FRAME_SECTIONS/`](../../FRAME_SECTIONS/)
- **All sub-assembly directories**: BOMs for each assembly type
- **Component models**: [`../../../../MODELS/`](../../../../MODELS/)
- **Engineering drawings**: [`../../../../DRAWINGS/`](../../../../DRAWINGS/)
- **Top-level assembly**: [`../../../TOP_LEVEL/`](../../../TOP_LEVEL/)

## BOM Management

### Version Control
- Track BOM revisions with version numbers
- Document changes in revision history
- Maintain change notices for BOM updates
- Coordinate BOM changes with configuration management

### Configuration Management
- Link BOMs to specific assembly configurations
- Document effectivity (serial numbers, dates)
- Track configuration options and variants
- Maintain as-built BOMs for each aircraft

### Data Validation
- Verify part numbers are valid
- Check quantities match assembly model
- Validate material specifications
- Ensure weight calculations are accurate
- Verify supplier information

## BOM Extraction

BOMs can be extracted from:
- **CAD assemblies**: Automated BOM extraction from 3D models
- **PDM/PLM systems**: Enterprise BOM management
- **ERP systems**: Manufacturing and procurement BOMs
- **Spreadsheets**: Manual BOM creation and maintenance

## Multi-Level BOM (MBOM)

Multi-level BOMs show:
- Complete product structure hierarchy
- Parent-child relationships
- Where-used information
- Assembly levels and indentation

Example:
```
1.0 Center Body Assembly
  1.1 Frame Section F05
    1.1.1 Frame F05
    1.1.2 Stringer L01 (Qty 4)
    1.1.3 Skin Panel SP-001
    1.1.4 Fasteners (Qty 200)
  1.2 Frame Section F06
    1.2.1 Frame F06
    ...
```

## Single-Level BOM (SBOM)

Single-level BOMs show:
- Immediate children only
- No sub-assembly detail
- Simplified view for procurement

## BOM Formats

### Spreadsheet (Excel/CSV)
- Most common format
- Easy to edit and share
- Good for manual updates
- Can include formulas and calculations

### PDF
- Read-only format for distribution
- Maintains formatting
- Good for formal releases
- Cannot be easily edited

### XML/JSON
- Machine-readable format
- Good for system integration
- Supports automated processing
- Structured data exchange

## Procurement Integration

BOMs support:
- **Purchase requisitions**: Parts to order
- **Supplier quotes**: RFQ (Request for Quote) packages
- **Material planning**: MRP (Material Requirements Planning)
- **Inventory management**: Stock levels and reorder points
- **Cost estimation**: Product cost roll-up

## Manufacturing Integration

BOMs support:
- **Production planning**: Manufacturing schedules
- **Work orders**: Shop floor job packets
- **Material kitting**: Assembly kits for production
- **Quality control**: Inspection and test requirements
- **As-built documentation**: Actual parts installed

## Metadata Requirements

Each BOM should include:
- **Assembly reference**: Associated assembly part number
- **BOM type**: EBOM, MBOM, or As-Maintained
- **BOM version**: Revision level
- **Effectivity**: Applicable serial numbers or dates
- **Date**: BOM creation or revision date
- **Author**: Responsible engineer or planner
- **Approval**: Authorized approver
- **Status**: Draft, released, or obsolete

## Quality Assurance

BOM quality checks:
- Part number validity (exist in system)
- Quantity accuracy (matches assembly)
- Weight accuracy (matches part data)
- Material specification completeness
- Source information correctness
- No duplicate entries
- Proper indentation and levels

## Version Control

- Track BOM changes in revision history
- Document reason for each change
- Maintain previous BOM versions
- Coordinate changes with ECO (Engineering Change Order)
- Update related documents when BOM changes
