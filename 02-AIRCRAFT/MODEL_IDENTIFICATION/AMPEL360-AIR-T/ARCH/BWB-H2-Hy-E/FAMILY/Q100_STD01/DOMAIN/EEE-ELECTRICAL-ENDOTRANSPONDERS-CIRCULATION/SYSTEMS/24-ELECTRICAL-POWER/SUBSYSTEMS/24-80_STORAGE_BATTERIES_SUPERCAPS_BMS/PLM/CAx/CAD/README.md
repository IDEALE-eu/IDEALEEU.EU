# CAD - 24-80_STORAGE_BATTERIES_SUPERCAPS_BMS

## Purpose

This directory contains CAD artifacts for the 24-80_STORAGE_BATTERIES_SUPERCAPS_BMS subsystem.

Computer-Aided Design (3D models, drawings, design specifications)

## Scope

CAD deliverables for this subsystem include:
- Native CAD files (SolidWorks, Creo, Siemens NX)
- Neutral formats with PMI (STEP AP242, IGES)
- 2D manufacturing drawings (PDF/DWG)
- Assembly and subassembly models
- Design specifications and technical documentation

## Contents

### CO₂ Endocircular Battery System - Design Specifications

Complete technical design documentation for the closed-loop CO₂-based energy storage system.

**Files**:
- `CO2_BATTERY_TECHNICAL_DOCS.md` - Complete technical reference documentation (13KB)

**Documentation Includes**:
- System architecture and component specifications
- Operating cycles with detailed performance analysis (sublimation, sCO₂ Brayton, CAES-like)
- Thermodynamic background and phase diagrams
- Safety considerations and materials selection
- Integration guidelines for aircraft systems
- Comparison with other storage technologies

**Related Files**:
- Simulation models: `../CAE/co2_battery_endocircular.py` and `test_co2_battery.py`
- Application examples: `../CAI/co2_battery_examples.py`

**Performance Summary**:
- Energy density: ~247 kWh/m³ (thermal)
- Specific energy: 20-70 Wh/kg (electrical, cycle-dependent)
- Discharge efficiency: 15-55% (cycle-dependent)
- Round-trip efficiency: 20-70% (with heat recovery)

## File Organization

- Use clear, descriptive filenames with canonical spelling
- Include revision/version in filename
- Maintain neutral formats alongside native files
- Document file relationships in parent README
- Include preview images (JPEG/PNG thumbnails, exploded views for assemblies)

## Naming Convention

**Pattern**: `{PART_ID}-{DESCRIPTION}_R{REV:03d}.{ext}`

Where:
- `PART_ID`: ATA chapter + subsystem (e.g., `24-80-001`)
- `DESCRIPTION`: Component name with underscores (e.g., `Battery_Assembly`)
- `REV`: 3-digit revision number (e.g., `001`, `002`)
- `ext`: File extension

**Examples**:
- `24-80-001-Battery_Assembly_R001.step`
- `24-80-002-Storage_Tank_R001.sldprt`
- `24-80-003-Pressure_Vessel_Drawing_R001.pdf`

## Required File Formats

| Format | Purpose | Requirements |
|--------|---------|--------------|
| Native CAD | Design intent, editability | SolidWorks/Creo/NX with mass properties |
| STEP AP242 | Neutral exchange with PMI | Include geometric and product manufacturing information |
| IGES | Legacy compatibility | Surfaces and wireframe |
| Parasolid | Kernel-level exchange | Binary format (.x_t) |
| PDF (2D) | Manufacturing drawings | ISO 128/129 compliant, readable at A3 |
| STL | Rapid prototyping | Mesh resolution ≤ 0.1 mm |

## Technical Conventions

- **Units**: SI (mm for length, kg for mass)
- **Coordinate System**: Right-handed, Z-axis vertical
- **Datum Reference**: As per ASME Y14.5-2018
- **Mass Properties**: Required in native file metadata (mass, center of gravity, moments of inertia)
- **Bounding Box**: Document max dimensions (X × Y × Z)

## EBOM Linkage

Each CAD file must reference:
- **EBOM ID**: Unique identifier in Engineering BOM
- **Part Number**: Matches PLM system
- **Assembly Level**: Top, subassembly, or component
- **Configuration**: If part has multiple variants

Field mapping documented in `../../../EBOM_LINKS.md`

## Revision Control

- **Branch Policy**: Feature branches for design iterations
- **Tag Pattern**: `CAD-{PART_ID}-R{REV}` (e.g., `CAD-24-80-001-R001`)
- **Sign-off**: Design engineer + lead engineer approval required
- **Change Management**: ECN required for released parts (see `../CMP/`)

## Standards

**Mandatory Compliance**:
- ASME Y14.5-2018: Geometric Dimensioning and Tolerancing
- ISO 128: Technical drawings - General principles
- ISO 129: Technical drawings - Dimensioning
- ISO 1101: Geometrical Product Specifications (GPS)
- ISO 10303 (STEP): Industrial automation systems and integration
- ASME BPVC Section VIII: Pressure vessel design
- SAE ARP1476: Cryogenic fluid storage systems

**Aircraft-Specific**:
- ATA iSpec 2200: Information Standards for Aviation Maintenance
- SAE AS9100: Quality Management Systems for Aviation
- DO-160: Environmental conditions for airborne equipment

## CAD Data Management

- **Check-in Procedure**: All files via PLM system
- **Metadata Required**: Part number, revision, author, approval status
- **Preview Required**: 
  - One thumbnail image (512×512 px JPEG)
  - One exploded view for assemblies
- **File Size Limits**: Native CAD < 100 MB, STEP < 50 MB

---

**Last Updated**: 2025-10-23
