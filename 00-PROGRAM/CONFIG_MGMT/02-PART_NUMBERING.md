# Part Numbering System

## 1. Overview

This document defines the part numbering scheme for all configuration items in the IDEALE EU aerospace program. The numbering system ensures unique identification, traceability, and proper configuration control.

## 2. Objectives

- Provide unique identification for every configuration item
- Enable classification and categorization
- Support interchangeability analysis
- Facilitate inventory and procurement
- Maintain consistency across aircraft and spacecraft programs

## 3. Part Number Structure

### 3.1 Format

**[PROGRAM]-[CATEGORY]-[SEQUENCE]-[VARIANT]**

**Example:** `IDEALE-ACFT-10234-A`

Where:
- **PROGRAM** - Program identifier (4-6 characters)
- **CATEGORY** - Item category code (4 characters)
- **SEQUENCE** - Sequential number (5 digits, zero-padded)
- **VARIANT** - Variant identifier (1-2 characters, optional)

### 3.2 Program Identifiers

| Code | Description |
|------|-------------|
| IDEALE | Common items shared between aircraft and spacecraft |
| ACFT | Aircraft-specific items |
| SCFT | Spacecraft-specific items |
| GSE | Ground Support Equipment |
| TEST | Test equipment and fixtures |

### 3.3 Category Codes

#### Aircraft Categories (ACFT)
| Code | Description |
|------|-------------|
| AIRF | Airframe structures |
| PROP | Propulsion systems |
| AVNX | Avionics and electronics |
| HYDR | Hydraulic systems |
| ELEC | Electrical systems |
| FCTL | Flight control systems |
| LDGR | Landing gear |
| FUEL | Fuel systems |
| H2SY | Hydrogen systems |
| THRM | Thermal management |
| CABN | Cabin and interior |
| CRGO | Cargo systems |

#### Spacecraft Categories (SCFT)
| Code | Description |
|------|-------------|
| STRC | Structures |
| PROP | Propulsion |
| PWER | Power systems |
| GNCE | Guidance, Navigation, Control |
| COMM | Communications |
| THRM | Thermal control |
| AVIO | Avionics |
| SWRE | Software |
| PYRO | Pyrotechnics |
| MECH | Mechanisms and deployables |

#### Common Categories
| Code | Description |
|------|-------------|
| PROC | Processes and specifications |
| TOOL | Tooling |
| GSEE | Ground support equipment |
| TEST | Test equipment |
| DOCS | Documentation |
| SOFT | Software and firmware |

### 3.4 Sequence Numbers

- 5-digit sequential number: 00001 to 99999
- Assigned sequentially within each PROGRAM-CATEGORY combination
- Never reused, even for obsolete parts
- Managed by Configuration Management

### 3.5 Variant Identifiers

- Single letter (A-Z) for design variants
- Used when parts are similar but not interchangeable
- Examples:
  - `IDEALE-ACFT-10234-A` - Standard version
  - `IDEALE-ACFT-10234-B` - Enhanced version
  - `IDEALE-ACFT-10234-C` - Lightweight version

## 4. Revision Control

### 4.1 Revision Codes

Revisions are tracked separately from part numbers using a dual system:

**Design Revisions:** Letters (A, B, C, ... Z)
- Used for design changes that affect form, fit, or function
- Start at 'A' for released design
- Increment for each design change

**Process Revisions:** Numbers (1, 2, 3, ...)
- Used for manufacturing process changes
- Do not affect form, fit, or function
- Examples: material substitutions, tooling changes

**Format:** Part Number Rev [Design][Process]
- Example: `IDEALE-ACFT-10234 Rev C2`

### 4.2 Pre-Release Designations

During development, use preliminary designations:
- **PRELIM** - Preliminary design
- **PROTO** - Prototype
- **ALPHA** - Alpha test version
- **BETA** - Beta test version

Example: `IDEALE-ACFT-10234 PRELIM`

## 5. Dash Numbers

Dash numbers identify components within an assembly:

**Format:** [Parent Part Number]-[Dash Number]

**Example:**
- `IDEALE-ACFT-10234` - Main assembly
- `IDEALE-ACFT-10234-1` - Component 1
- `IDEALE-ACFT-10234-2` - Component 2

Dash numbers are used for:
- Components of an assembly
- Hardware kits
- Drawing sheets

## 6. Special Cases

### 6.1 Commercial Off-The-Shelf (COTS)

Format: **COTS-[Manufacturer Code]-[Manufacturer Part Number]**

Example: `COTS-HONW-ABC123`

Maintain COTS registry with:
- Manufacturer name and code
- Manufacturer part number
- Description
- Qualification status

### 6.2 Standard Hardware

Use industry-standard identifiers:
- **MS** - Military Standard
- **AN** - Air Force-Navy
- **NAS** - National Aerospace Standard
- **AS** - Aerospace Standard

Example: `MS21042-3` (locknut)

### 6.3 Raw Materials

Format: **MAT-[Material Spec]-[Size]**

Example: `MAT-AL7075-T6-SHEET-2MM`

## 7. Part Number Assignment Process

1. **Request** - Engineer submits part number request to CM
2. **Classification** - CM determines appropriate PROGRAM-CATEGORY
3. **Assignment** - CM assigns next sequential number
4. **Registration** - Part number added to Item Master (08-ITEM_MASTER/ITEMS.csv)
5. **Communication** - CM notifies requester of assigned number

## 8. Interchangeability

### 8.1 Interchangeability Codes

| Code | Description |
|------|-------------|
| I | Fully interchangeable (form, fit, function) |
| F | Fit interchangeable only |
| N | Not interchangeable |

Documented in item master attributes.

### 8.2 Source Control

For critical items, specify:
- **Source Controlled** - Must be from approved source
- **Source Restricted** - Single source only
- **Multiple Source** - Any qualified supplier

## 9. Effectivity

Track when part numbers become effective:
- **Serial Number Effectivity** - Applies to specific serial numbers
- **Date Effectivity** - Applies from specific date
- **Mod Effectivity** - Applies with specific modification

Example: "Effective S/N 1001 and subsequent"

## 10. Obsolescence

When parts become obsolete:
1. Mark as OBSOLETE in item master
2. Document superseding part (if any)
3. Never reuse part number
4. Maintain obsolete part data for historical reference

## 11. Part Number Registry

All part numbers maintained in **08-ITEM_MASTER/ITEMS.csv** with:
- Part number
- Description
- Category
- Status (PRELIM, ACTIVE, OBSOLETE)
- Revision
- Interchangeability
- Superseded by (if obsolete)
- Owner
- Date created

## 12. Examples

| Part Number | Description |
|-------------|-------------|
| IDEALE-ACFT-00001 Rev A | Aircraft main wing assembly |
| IDEALE-ACFT-00001-1 | Wing spar |
| IDEALE-ACFT-00001-2 | Wing skin |
| IDEALE-SCFT-00001 Rev B1 | Spacecraft primary structure |
| IDEALE-PROP-00100 Rev A | Hybrid propulsion module |
| GSE-TEST-00050 | Hydraulic test fixture |
| COTS-HONW-IMU5000 | Inertial measurement unit |
| MAT-AL7075-T6-SHEET-2MM | Aluminum sheet material |

## 13. Governance

- Part numbering authority: Configuration Manager
- Changes to numbering scheme require CCB approval
- Annual review of numbering system effectiveness
