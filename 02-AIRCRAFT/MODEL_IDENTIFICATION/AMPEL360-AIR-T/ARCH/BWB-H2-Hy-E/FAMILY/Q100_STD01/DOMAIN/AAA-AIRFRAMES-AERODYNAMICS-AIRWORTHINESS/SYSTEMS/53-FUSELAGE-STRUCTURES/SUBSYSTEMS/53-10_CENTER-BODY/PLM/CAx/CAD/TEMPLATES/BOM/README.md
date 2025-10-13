# BOM — Bill of Materials Templates and Standards

## Purpose

Standardized Bill of Materials (BOM) structures, templates, and export formats for the 53-10 Center Body assemblies.

## BOM Structure Types

### Engineering BOM (EBOM)
- **Purpose**: Captures design intent and functional hierarchy
- **Structure**: Product-centric, as-designed
- **Content**: All parts, assemblies, and relationships
- **Usage**: Engineering, design reviews, change management

### Manufacturing BOM (MBOM)
- **Purpose**: Represents manufacturing process and sequence
- **Structure**: Process-centric, as-built
- **Content**: Raw materials, sub-assemblies, manufacturing steps
- **Usage**: Production planning, shop floor, quality

### Service BOM (SBOM)
- **Purpose**: Supports maintenance and spare parts
- **Structure**: As-maintained, replaceable units
- **Content**: Line-replaceable units (LRU), consumables
- **Usage**: Maintenance manuals, spare parts ordering

## EBOM Structure for 53-10 Center Body

### Top-Level Assembly
```
53-10_ASM_CENTER-BODY_COMPLETE_v01
├── 53-11_ASM_FRAME_SECTION_FWD_v01
│   ├── 53-11-001_PRT_FRAME_F01_v01
│   ├── 53-11-002_PRT_FRAME_F02_v01
│   ├── 53-11-003_PRT_FRAME_F03_v01
│   └── Standard Hardware (fasteners, etc.)
├── 53-12_ASM_FRAME_SECTION_AFT_v01
│   ├── 53-12-001_PRT_FRAME_F04_v01
│   ├── 53-12-002_PRT_FRAME_F05_v01
│   └── Standard Hardware
├── 53-13_ASM_SKIN_PANELS_v01
│   ├── 53-13-001_PRT_SKIN_PANEL_SP-001_v01
│   ├── 53-13-002_PRT_SKIN_PANEL_SP-002_v01
│   └── Fasteners
├── 53-14_ASM_STRINGERS_v01
│   ├── 53-14-001_PRT_STRINGER_ST-001_v01
│   ├── 53-14-002_PRT_STRINGER_ST-002_v01
│   └── Fasteners
└── 53-15_ASM_FITTINGS_v01
    ├── 53-15-001_PRT_FITTING_WING-ATTACH_LEFT_v01
    ├── 53-15-002_PRT_FITTING_WING-ATTACH_RIGHT_v01
    └── Hardware
```

## BOM Attributes

### Required Attributes (All Items)
- **Item Number**: Sequential item number in BOM
- **Part Number**: Unique identifier
- **Description**: Part/assembly description
- **Quantity**: Quantity per parent assembly
- **Unit of Measure**: EA (each), SET, M (meter), KG, etc.

### Design Attributes
- **Material**: Material specification
- **Finish**: Surface finish/coating
- **Mass (Unit)**: Individual part mass
- **Mass (Total)**: Quantity × unit mass
- **Source**: Make/Buy designation

### Manufacturing Attributes
- **Manufacturing Process**: Machined, formed, composite layup, etc.
- **Make/Buy**: Internal manufacture or purchased
- **Supplier**: Supplier name (if buy)
- **Lead Time**: Procurement/manufacturing lead time

### Configuration Attributes
- **Configuration**: Applicable configurations (LEFT, RIGHT, ALL, etc.)
- **Effectivity**: Serial number or date effectivity
- **Find Number**: Find number on drawing
- **Reference Designator**: Installation location

## BOM Templates

### Part-Level BOM Template
```csv
Item,Part Number,Description,Qty,UOM,Material,Mass (kg),Source,Notes
1,53-11-001,Frame F01 Upper Web,1,EA,AL 2024-T3,2.5,Make,Critical
2,53-11-002,Frame F01 Lower Web,1,EA,AL 2024-T3,2.3,Make,Critical
3,MS20470AD-5,Rivet 5/32" Universal Head,120,EA,AL 2117-T4,0.002,Buy,Per pattern
```

### Assembly-Level BOM Template
```csv
Item,Part Number,Description,Qty,UOM,Type,Mass (kg),Make/Buy,Notes
1,53-11-001,Frame F01 Complete,1,EA,ASSY,15.2,Make,Sub-assembly
1.1,53-11-001-01,Frame F01 Upper Web,1,EA,PART,2.5,Make,
1.2,53-11-001-02,Frame F01 Lower Web,1,EA,PART,2.3,Make,
1.3,53-11-001-03,Frame F01 Cap Strip,2,EA,PART,1.2,Make,
1.4,MS20470AD-5,Rivet 5/32",120,EA,STD,0.002,Buy,
```

### Standard Parts BOM Section
```csv
Item,Part Number,Description,Qty,UOM,Specification,Source
10,MS20470AD-4,Rivet 1/8" Universal Head,450,EA,MS20470,Buy
11,MS20470AD-5,Rivet 5/32" Universal Head,280,EA,MS20470,Buy
12,HL11V-8,Hi-Lok Pin 1/2" Grip,36,EA,HL11V,Buy
13,HL13V-8,Hi-Lok Collar,36,EA,HL13V,Buy
14,NAS6604-12,Bolt Hex Head 1/4",24,EA,NAS6604,Buy
15,MS21042-4,Nut Self-Locking 1/4",24,EA,MS21042,Buy
```

## BOM Levels and Indentation

### Single-Level BOM
Shows only immediate children of an assembly:
```
53-10_ASM_CENTER-BODY_COMPLETE
  ├── 53-11_ASM_FRAME_SECTION_FWD
  ├── 53-12_ASM_FRAME_SECTION_AFT
  ├── 53-13_ASM_SKIN_PANELS
  ├── 53-14_ASM_STRINGERS
  └── 53-15_ASM_FITTINGS
```

### Multi-Level BOM
Shows complete product hierarchy:
```
1.0   53-10_ASM_CENTER-BODY_COMPLETE
1.1     53-11_ASM_FRAME_SECTION_FWD
1.1.1     53-11-001_PRT_FRAME_F01
1.1.2     53-11-002_PRT_FRAME_F02
1.1.3     MS20470AD-5 (Rivets)
1.2     53-12_ASM_FRAME_SECTION_AFT
1.2.1     53-12-001_PRT_FRAME_F04
...
```

### Flattened BOM
All items at same level with quantity roll-up:
```
Part Number            Description                 Total Qty
53-11-001             Frame F01                    1
53-11-002             Frame F02                    1
53-13-001             Skin Panel SP-001            4
MS20470AD-4           Rivet 1/8"                   1,850
MS20470AD-5           Rivet 5/32"                  920
HL11V-8               Hi-Lok Pin                   156
```

## BOM Export Formats

### CSV Format
```csv
Level,Item,Part Number,Description,Qty,UOM,Material,Mass,Make/Buy
1,1,53-10_ASM_CENTER-BODY_COMPLETE,Center Body Assembly,1,EA,-,125.0,Make
2,1.1,53-11_ASM_FRAME_SECTION_FWD,Forward Frame Section,1,EA,-,35.0,Make
3,1.1.1,53-11-001,Frame F01,1,EA,AL 2024-T3,2.5,Make
```

### Excel Format
- Multiple tabs: Summary, Detailed BOM, Standard Parts, Custom Parts
- Formatted cells with colors for Make/Buy
- Formulas for mass roll-up
- Filters and sorting enabled

### PDF Format
- Formatted table with company header
- Revision block
- Approval signatures
- Cross-references to drawings

## BOM Generation from CAD

### Automated BOM Extraction
CAD systems can auto-generate BOMs from assembly structure:
- **CATIA**: Product Structure Tools → Generate BOM
- **NX**: Assemblies → Parts List
- **SOLIDWORKS**: Insert → Tables → Bill of Materials
- **Creo**: Table → BOM Table

### BOM Customization
- Select BOM type (indented, flattened, parts only)
- Choose attributes to display
- Set quantity display (per assembly, total)
- Apply filters (exclude reference parts, etc.)
- Format table (fonts, borders, column widths)

### Scripts for BOM Export
See [`../SCRIPTS_MACROS/`](../SCRIPTS_MACROS/) for:
- `export_bom_to_csv.py` — Export BOM to CSV format
- `generate_flattened_bom.py` — Create flattened BOM with totals
- `bom_comparison.py` — Compare BOMs between revisions
- `standard_parts_report.py` — Extract standard/catalog parts

## BOM Validation

### BOM Completeness Checks
- All parts have part numbers
- All parts have descriptions
- All quantities are valid (> 0)
- All materials are specified
- No duplicate item numbers
- No orphan parts (not in any assembly)

### BOM Consistency Checks
- Part numbers match naming convention
- Mass values are reasonable
- Unit of measure is appropriate
- Make/Buy designation is present
- Standard parts use correct specifications

## BOM Change Management

### BOM Revision Control
- Track BOM changes with each design revision
- Document added, removed, or changed items
- Maintain revision history
- Link to ECRs (Engineering Change Requests)

### BOM Comparison
Compare BOMs between revisions:
```
Revision A → Revision B:
+ ADDED: 53-13-005 Skin Panel SP-005 (1 EA)
- REMOVED: 53-13-003 Skin Panel SP-003 (1 EA)
Δ CHANGED: MS20470AD-5 Rivet Qty: 920 → 1050 (+130)
```

## Related Directories

- **Properties**: [`../PROPERTIES/`](../PROPERTIES/) — BOM attribute definitions
- **Scripts/Macros**: [`../SCRIPTS_MACROS/`](../SCRIPTS_MACROS/) — BOM automation scripts
- **Export**: [`../EXPORT/`](../EXPORT/) — CAD export standards
- **Main templates**: [`../README.md`](../README.md)

## References

- PLM/EBOM documentation: [`../../EBOM_LINKS.md`](../../EBOM_LINKS.md)
- Assembly standards: [`../../ASSEMBLIES/README.md`](../../ASSEMBLIES/README.md)
- Configuration management: [`/00-PROGRAM/CONFIG_MGMT/`](/00-PROGRAM/CONFIG_MGMT/)
- Part numbering: [`/00-PROGRAM/CONFIG_MGMT/02-PART_NUMBERING.md`](/00-PROGRAM/CONFIG_MGMT/02-PART_NUMBERING.md)
