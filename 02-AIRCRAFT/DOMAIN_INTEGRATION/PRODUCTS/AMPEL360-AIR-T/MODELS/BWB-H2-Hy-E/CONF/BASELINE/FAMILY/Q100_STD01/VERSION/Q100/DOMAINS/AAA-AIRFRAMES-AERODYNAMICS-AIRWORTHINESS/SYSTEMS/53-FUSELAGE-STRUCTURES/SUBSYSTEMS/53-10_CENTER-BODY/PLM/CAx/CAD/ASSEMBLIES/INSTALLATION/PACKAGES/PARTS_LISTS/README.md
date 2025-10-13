# PARTS_LISTS — Installation Parts Lists

## Purpose

This directory contains detailed parts lists and bills of materials (BOMs) for installation operations, documenting all components required for center body installation.

## Content Types

- **Installation BOMs** — Complete parts lists for installation assemblies
- **Interface parts lists** — Components specific to each interface
- **Fastener schedules** — Detailed fastener requirements
- **Consumables lists** — Materials consumed during installation
- **Alternate parts lists** — Approved substitutions and alternates

## File Formats

- `.xlsx` / `.csv` — Tabular parts lists
- `.pdf` — Released documentation
- `.xml` — Structured BOM data for PLM/ERP systems

## Naming Convention

```
PARTS_53-10_INSTALL_<interface>_<type>_v<version>.<ext>
```

Examples:
- `PARTS_53-10_INSTALL_WING-ATTACH_BOM_v001.xlsx`
- `PARTS_53-10_INSTALL_DOOR-FRAME_FASTENERS_v002.csv`
- `PARTS_53-10_INSTALL_COMPLETE_MASTER-BOM_v001.pdf`

## Parts List Contents

Each parts list should include:
- Part number
- Part description
- Quantity required
- Unit of measure
- Specification/standard reference
- Source (make/buy)
- Cage code (if applicable)
- Notes and remarks

## List Types

### Installation BOM
Complete bill of materials for installation:
- All structural parts
- All fasteners
- All seals and gaskets
- All consumables
- Installation aids

### Fastener Schedule
Detailed fastener list by location:
- Fastener type and size
- Installation torque
- Quantity per location
- Total quantity required
- Special requirements

### Consumables List
Materials consumed during installation:
- Sealants and adhesives
- Cleaning materials
- Primers
- Protective coatings
- Disposable supplies

### Alternate Parts List
Approved substitutions:
- Primary part number
- Alternate part numbers
- Interchangeability notes
- Effectivity information

## Data Management

- Link to PLM/PDM system
- Maintain revision control
- Track effectivity
- Document change history
- Include supplier information

## Cross-References

- [Parent: Packages](../README.md)
- [Installation Kits](../KITS/README.md)
- [Fasteners](../../FASTENERS/README.md)
- [Installation Drawings](../../DRAWINGS/README.md)

## Integration

Parts lists should integrate with:
- PLM/PDM systems
- ERP/MRP systems
- Supply chain management
- Configuration management
- Change control processes

## Quality Requirements

- Accuracy verification
- Regular audits
- Traceability to design
- Change control compliance
- Approval signatures required
