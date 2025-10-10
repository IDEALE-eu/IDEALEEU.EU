# S1000D CSDB — 21-10 Radiators & Heat Exchangers

## Purpose

This is the **Common Source Database (CSDB)** for S1000D-compliant technical publications for the 21-10 Radiators & Heat Exchangers subsystem of AMPEL360-SPACE-T.

## Directory Structure

```
S1000D/
├── README.md                      # This file
├── brex/                          # Business Rules Exchange
│   └── BREX-AMPEL360-21-10.xml
├── dmrl/                          # Data Module Requirements List
│   └── DMRL-AMPEL360-21-10.xml
├── dm/                            # Data Modules (XML)
│   ├── 000-general/               # System descriptions, principles
│   ├── 200-fault-isolation/       # Troubleshooting procedures
│   ├── 400-scheduled-maintenance/ # Maintenance intervals, inspections
│   ├── 500-removal-installation/  # R&I procedures
│   ├── 600-repair/                # Repair procedures
│   ├── 700-overhaul/              # Depot-level overhaul
│   ├── 800-ipd/                   # Illustrated Parts Data
│   └── 900-tools-consumables/     # Tools & consumables lists
├── pm/                            # Publication Modules
│   ├── AMM/                       # Aircraft/Spacecraft Maintenance Manual
│   │   └── PM-AMM-AMPEL360-21-10-Q10.xml
│   ├── CMM/                       # Component Maintenance Manual
│   │   └── PM-CMM-AMPEL360-21-10-Q10.xml
│   └── IPC/                       # Illustrated Parts Catalog
│       └── PM-IPC-AMPEL360-21-10-Q10.xml
├── icn/                           # Illustrations (Illustration Control Numbers)
│   ├── vector/                    # SVG/CGM vector graphics
│   └── raster/                    # PNG/JPG raster graphics
├── res/                           # Resources (CSS/XSL/Schematron)
├── qc/                            # Quality Control / Validation logs
└── delivery/                      # IETP/PDF delivery packages
```

## Standards

- **S1000D Issue 6.0**: XML-based technical publications
- **ATA iSpec 2200**: Chapter 21 (Thermal Control)
- **ASD-STE-100**: Simplified Technical English

## Data Module Naming Convention

Data Modules follow the S1000D DMC (Data Module Code) format:

```
DMC-<ModelIdent>-<SystemCode>-<SubSystem>-<SubSubSystem>-<Disassy>-<DisassyVar>-<InfoCode>-<InfoVar>-<ItemLoc>
```

Example:
```
DMC-AMPEL360-2110-00-00-00-00A-040A-A_en-US_001-00.xml
```

Where:
- `AMPEL360`: Model Identification Code
- `2110`: System Code (21 = Thermal Control, 10 = Radiators)
- `00-00-00`: SubSystem/SubSubSystem/Disassy codes
- `00A`: Disassembly Code Variant
- `040A`: Info Code (040 = Scheduled Maintenance)
- `A`: Info Code Variant
- `en-US`: Language and country code
- `001-00`: Issue number and in-work

## Workflow

1. **Author Data Modules**: Create XML files per S1000D schema
2. **Validate**: Run BREX and Schematron validation
3. **Illustrate**: Create ICNs and link to DMs
4. **Assemble Publications**: Create Publication Modules
5. **Quality Control**: Log validation results in qc/
6. **Publish**: Generate IETP and PDF in delivery/

## Tools

- **XML Editors**: oXygen XML Editor, Arbortext Editor
- **BREX Validation**: Python scripts or commercial tools
- **Schematron**: Schema validation
- **XSL-FO**: PDF transformation
- **IETP Viewer**: S1000D-compliant viewer

## References

- S1000D Issue 6.0 Specification: http://www.s1000d.org
- ATA iSpec 2200: Chapter 21 structure
- AMPEL360 System Breakdown: STA-B domain
