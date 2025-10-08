# Serialization Guidelines

## 1. Overview

This document defines the serialization system for trackable items in the IDEALE EU aerospace program. Serialization provides unique identification for individual units of a configuration item, enabling traceability throughout manufacturing, testing, and operational life.

## 2. Purpose

Serialization enables:
- Individual item tracking from manufacturing through disposal
- Traceability of materials, processes, and test results
- Fleet management and maintenance history
- Incident investigation and root cause analysis
- Warranty and reliability tracking
- Regulatory compliance (FAA, EASA, ESA)

## 3. Serialization Requirements

### 3.1 Items Requiring Serialization

All of the following require unique serial numbers:

#### Critical Flight Items
- Aircraft assemblies and major components
- Spacecraft assemblies and subsystems
- Propulsion systems
- Flight control systems
- Life-critical structures
- Avionics and computing systems

#### Controlled Items
- Test articles and prototypes
- Qualification hardware
- Certification test specimens
- Flight test vehicles
- Ground test equipment (critical)
- Calibrated measurement equipment

#### High-Value Items
- Items >$50,000 unit cost
- Long-lead items
- Limited production items

### 3.2 Items NOT Requiring Serialization

- Standard hardware (bolts, nuts, fasteners)
- Bulk materials
- Consumables
- Low-cost COTS items (<$1,000)
- Documentation

## 4. Serial Number Format

### 4.1 Standard Format

**[Part Number]/S/N [Sequential Number]-[Lot Code]**

**Example:** `IDEALE-ACFT-10234/S/N 0001-L2024A`

Where:
- **Part Number** - Full part number (see 02-PART_NUMBERING.md)
- **S/N** - Serial number designator
- **Sequential Number** - 4-digit sequential (0001-9999)
- **Lot Code** - Manufacturing lot identifier (optional)

### 4.2 Sequential Numbering

- Start at 0001 for each part number
- Increment sequentially
- Zero-padded to 4 digits
- Never skip or reuse numbers
- After 9999, use 5-digit format (10000, 10001, ...)

### 4.3 Lot Codes

Format: **L[YEAR][QUARTER/MONTH][BATCH]**

Examples:
- `L2024A` - Year 2024, Batch A
- `L2024Q1` - Year 2024, Quarter 1
- `L202401A` - Year 2024, January, Batch A

Used for:
- Grouping items from same manufacturing run
- Material lot traceability
- Quality investigation

## 5. Serialization Application

### 5.1 Physical Marking Methods

#### Permanent Marking (Preferred)
- **Laser engraving** - Metal and composite parts
- **Dot peen** - Metal parts
- **Chemical etching** - Metal parts
- **Stamping** - Non-critical areas only

#### Semi-Permanent Marking
- **Anodized engraving** - Aluminum parts
- **Ink stamping** - With protective coating
- **Engraved nameplates** - Bolted or riveted

#### Temporary Marking (Not Acceptable for Final)
- Adhesive labels - For in-process tracking only
- Paint markers - For in-process tracking only

### 5.2 Marking Location

- Visible and accessible without disassembly (preferred)
- Non-critical area (away from stress concentrations)
- Protected from wear and environmental exposure
- Documented in engineering drawings

### 5.3 Marking Requirements

- Character height: Minimum 2mm (larger if readable from distance required)
- Depth: 0.05mm - 0.15mm (laser/etch), per drawing
- Font: Sans-serif, OCR-readable
- Contrast: High contrast for machine vision/scanning

### 5.4 Multiple Marking

For critical items, provide redundant marking:
- Primary marking: Permanent, external
- Secondary marking: Internal or alternate location
- Data matrix code: 2D barcode with S/N encoded

## 6. Data Matrix Codes

### 6.1 Format

2D barcode (Data Matrix ECC200) containing:
- Part number
- Serial number
- Lot code (if applicable)
- Date of manufacture

**Example Encoded Data:**
```
[P]IDEALE-ACFT-10234[S]0001[L]L2024A[D]20240315
```

### 6.2 Placement

- Adjacent to human-readable serial number
- Minimum 5mm x 5mm size
- Scannable with handheld readers
- Protected from damage

## 7. Serialization Process

### 7.1 Serial Number Assignment

1. **Request** - Manufacturing requests S/N from CM
2. **Assignment** - CM assigns next sequential S/N
3. **Registration** - S/N recorded in tracking system
4. **Communication** - CM provides S/N to manufacturing

### 7.2 Physical Marking

1. **Preparation** - Clean and prepare marking surface
2. **Marking** - Apply marking per specification
3. **Inspection** - Verify marking quality and correctness
4. **Documentation** - Record marking completion in traveler

### 7.3 Data Capture

At serialization:
- Date of manufacture
- Manufacturing lot
- Operator ID
- Manufacturing location
- Inspection status

## 8. Serial Number Tracking

### 8.1 Lifecycle Tracking

Track serialized items through:
1. **Manufacturing** - Fabrication, assembly, inspection
2. **Testing** - Component, system, qualification, acceptance
3. **Integration** - Assembly into higher-level systems
4. **Delivery** - Shipment to customer or integration site
5. **Operations** - In-service use
6. **Maintenance** - Repairs, overhauls, modifications
7. **Retirement** - End of life, disposal, archival

### 8.2 Traceability Records

Maintain for each S/N:
- Material certifications and lot numbers
- Manufacturing process records
- Inspection and test results
- Modifications and repairs
- Usage history (hours, cycles, missions)
- Maintenance history
- Failure/incident reports
- Final disposition

### 8.3 Database System

Serial number database maintained in item master system with:
- Part number and S/N
- Current status and location
- Manufacturing data
- Test history
- Configuration (as-built vs. design)
- Current effectivity
- Parent assembly (if installed)

## 9. Special Cases

### 9.1 Prototypes

Format: **[Part Number]/PROTO-[Number]**

Example: `IDEALE-ACFT-10234/PROTO-001`

### 9.2 Test Articles

Format: **[Part Number]/TEST-[Number]**

Example: `IDEALE-ACFT-10234/TEST-001`

### 9.3 Flight Test Vehicles

Format: **FTV-[Number]**

Example: `FTV-001` (Flight Test Vehicle 1)

### 9.4 Qualification Units

Format: **QU-[Part Number]-[Number]**

Example: `QU-IDEALE-ACFT-10234-001`

### 9.5 Engineering Models

Format: **EM-[Part Number]-[Number]**

Example: `EM-IDEALE-SCFT-00100-001`

## 10. Serialization for Software/Firmware

### 10.1 Software Build Numbers

Format: **[Major].[Minor].[Patch]-[Build]**

Example: `1.2.3-20240315`

### 10.2 Firmware Serial/Version

Embedded firmware includes:
- Software version
- Compilation date/time
- Hardware S/N (when loaded)

## 11. Documentation

### 11.1 Serialization Drawing Notes

Engineering drawings include:
- "THIS PART REQUIRES SERIALIZATION"
- Marking location (with detail view)
- Marking method
- Character size and depth
- Data matrix code requirement

### 11.2 Traveler Requirements

Manufacturing traveler includes:
- Serial number assignment step
- Marking operation
- Marking inspection
- S/N registration in database

## 12. Quality Control

### 12.1 Marking Inspection

Verify:
- Correct part number
- Correct serial number
- Legibility
- Location per drawing
- Depth/quality acceptable
- Data matrix scannable

### 12.2 Nonconformance

If marking is incorrect:
- Do NOT obliterate or alter
- Note discrepancy in traveler
- Request disposition from engineering
- May require scrapping and remanufacturing

## 13. Rework and Repair

### 13.1 Serial Number Retention

- Serial numbers are NEVER changed or reused
- Reworked items retain original S/N
- Repaired items retain original S/N
- Record all rework/repairs in S/N history

### 13.2 Replacement Units

If item is replaced:
- Original S/N marked as REMOVED
- Replacement item receives new S/N
- Both S/N histories updated with replacement event

## 14. Examples

### 14.1 Aircraft Examples

| Item | Serial Number |
|------|---------------|
| Aircraft (tail number) | IDEALE-ACFT-00001/S/N 0001 |
| Main wing assembly | IDEALE-ACFT-00100/S/N 0015-L2024Q1 |
| Propulsion module | IDEALE-PROP-00050/S/N 0003-L202401A |
| Flight computer | IDEALE-AVNX-00200/S/N 0042 |

### 14.2 Spacecraft Examples

| Item | Serial Number |
|------|---------------|
| Spacecraft | IDEALE-SCFT-00001/S/N 0001 |
| Primary structure | IDEALE-STRC-00010/S/N 0001-L2024A |
| Solar array | IDEALE-PWER-00025/S/N 0002-L2024B |
| Reaction wheel | IDEALE-GNCE-00100/S/N 0008 |

### 14.3 Test Article Examples

| Item | Serial Number |
|------|---------------|
| Flight test vehicle | FTV-001 |
| Static test article | IDEALE-ACFT-00100/TEST-001 |
| Qualification unit | QU-IDEALE-SCFT-00050-001 |
| Engineering model | EM-IDEALE-PROP-00075-002 |

## 15. Governance

- Serialization authority: Configuration Manager
- Serial number assignment: Manufacturing Engineering with CM approval
- Database maintenance: Configuration Management
- Process audits: Quality Assurance (quarterly)
