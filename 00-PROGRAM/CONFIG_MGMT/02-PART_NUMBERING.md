# 02-PART_NUMBERING.md

Defines the part numbering scheme for all configuration items. Ensures unique ID, traceability, and control.

## 1. Overview
Scope: aircraft, spacecraft, GSE, software/firmware, documents, test equipment. Item Master lives at **[08-ITEM_MASTER/ITEMS.csv](./08-ITEM_MASTER/ITEMS.csv)**.

## 2. Objectives
Unique IDs · classification · interchangeability · inventory/procurement · consistency across domains.

## 3. Structure

### 3.1 Format
**[PROGRAM]-[CATEGORY]-[SEQUENCE]-[VARIANT]**  
Example: `ACFT-AIRF-10234-A`

- **PROGRAM**: 4–6 chars  
- **CATEGORY**: 4 chars  
- **SEQUENCE**: 5 digits (zero-padded)  
- **VARIANT**: 1–2 chars (optional)

### 3.2 Program Identifiers
| Code | Description |
|---|---|
| IDEALE | Common shared items |
| ACFT | Aircraft program |
| SCFT | Spacecraft program |
| GSE | Ground Support Equipment |
| TEST | Test equipment and fixtures |

### 3.3 Category Codes

**Aircraft (when PROGRAM = ACFT)**
| Code | Description |
|---|---|
| AIRF | Airframe structures |
| PROP | Propulsion systems |
| AVNX | Avionics and electronics |
| HYDR | Hydraulic systems |
| ELEC | Electrical systems |
| FCTL | Flight controls |
| LDGR | Landing gear |
| FUEL | Fuel systems |
| H2SY | Hydrogen systems |
| THRM | Thermal management |
| CABN | Cabin and interior |
| CRGO | Cargo systems |

**Spacecraft (when PROGRAM = SCFT)**
| Code | Description |
|---|---|
| STRC | Structures |
| PROP | Propulsion |
| PWER | Power |
| GNCE | Guidance/Nav/Control |
| COMM | Communications |
| THRM | Thermal control |
| AVIO | Avionics |
| SWRE | Software |
| PYRO | Pyrotechnics |
| MECH | Mechanisms |

**Common**
| Code | Description |
|---|---|
| PROC | Processes/specs |
| TOOL | Tooling |
| GSEE | Ground support equipment |
| TEST | Test equipment |
| DOCS | Documentation |
| SOFT | Software/firmware |

### 3.4 Sequence Numbers
00001–99999. Assigned per **PROGRAM–CATEGORY**. Never reused. Controlled by CM. Logged in **[ITEMS.csv](./08-ITEM_MASTER/ITEMS.csv)**.

### 3.5 Variants
Single letter A–Z (or 2 chars) for non-interchangeable design variants.

## 4. Revisions

Design revs: A→Z (form/fit/function).  
Process revs: 1→N (manufacturing only).  
Format: `PN Rev [Design][Process]` → `ACFT-AIRF-10234 Rev C2`.

Pre-release tags: `PRELIM`, `PROTO`, `ALPHA`, `BETA` (e.g., `ACFT-AIRF-10234 PRELIM`).

## 5. Dash Numbers
Components within an assembly: `[Parent PN]-[dash]`  
Example:  
- `ACFT-AIRF-00001` — wing assembly  
- `ACFT-AIRF-00001-1` — spar  
- `ACFT-AIRF-00001-2` — skin

## 6. Special Cases

### 6.1 COTS
`COTS-[MFR_CODE]-[MFR_PN]` → `COTS-HONW-IMU5000`  
Registry in **[ITEMS.csv](./08-ITEM_MASTER/ITEMS.csv)** and supply data: **[SUPPLY_CHAIN/13-DATA_MODELS/AML_APPROVED_MFR_LIST.csv](../SUPPLY_CHAIN/13-DATA_MODELS/AML_APPROVED_MFR_LIST.csv)**, **[.../AVL_APPROVED_VENDOR_LIST.csv](../SUPPLY_CHAIN/13-DATA_MODELS/AVL_APPROVED_VENDOR_LIST.csv)**.

### 6.2 Standards Hardware
Use native IDs (MS, AN, NAS, AS): e.g., `MS21042-3`.

### 6.3 Raw Materials
`MAT-[Spec]-[Size]` → `MAT-AL7075-T6-SHEET-2MM`.

## 7. Assignment Process
1. Request to CM.  
2. Classify PROGRAM–CATEGORY.  
3. Assign next SEQUENCE.  
4. Register in **[ITEMS.csv](./08-ITEM_MASTER/ITEMS.csv)**.  
5. Notify requester.

## 8. Interchangeability

Codes in Item Master:
| Code | Meaning |
|---|---|
| I | Fully interchangeable |
| F | Fit only |
| N | Not interchangeable |

Source status: Source-Controlled / Source-Restricted / Multiple Source. See AML/AVL in **[SUPPLY_CHAIN/13-DATA_MODELS/](../SUPPLY_CHAIN/13-DATA_MODELS/)**.

## 9. Effectivity
Serial, date, or modification effectivity recorded in **[ITEMS.csv](./08-ITEM_MASTER/ITEMS.csv)**.

## 10. Obsolescence
Mark **OBSOLETE**, add “superseded by”, never reuse PN. Keep records.

## 11. Registry
Master at **[08-ITEM_MASTER/ITEMS.csv](./08-ITEM_MASTER/ITEMS.csv)** with PN, description, category, status (PRELIM/ACTIVE/OBSOLETE), rev, interchangeability, superseded-by, owner, date.

## 12. Examples (corrected to scheme)
| Part Number | Description |
|---|---|
| ACFT-AIRF-00001 Rev A | Aircraft wing assembly |
| ACFT-AIRF-00001-1 | Wing spar |
| ACFT-AIRF-00001-2 | Wing skin |
| SCFT-STRC-00001 Rev B1 | Spacecraft primary structure |
| ACFT-PROP-00100 Rev A | Hybrid propulsion module |
| GSE-TEST-00050 | Hydraulic test fixture |
| COTS-HONW-IMU5000 | Inertial measurement unit |
| MAT-AL7075-T6-SHEET-2MM | Sheet material |

## 13. Governance
Numbering authority: Configuration Manager. Changes require **[CCB](./05-CCB/)** approval. Annual effectiveness review. Serialization rules: **[03-SERIALIZATION.md](./03-SERIALIZATION.md)**. Changes managed in **[06-CHANGES/](./06-CHANGES/)**.

