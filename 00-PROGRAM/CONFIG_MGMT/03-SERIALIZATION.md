# Serialization Guidelines

> Scope: aircraft, spacecraft, GSE, software/firmware.  
> References: **[02-PART_NUMBERING.md](./02-PART_NUMBERING.md)** · **[08-ITEM_MASTER/ITEMS.csv](./08-ITEM_MASTER/ITEMS.csv)** · **[QUALITY_QMS/08-CALIBRATION_METROLOGY/](../QUALITY_QMS/08-CALIBRATION_METROLOGY/)** · **[SUPPLY_CHAIN/13-DATA_MODELS/](../SUPPLY_CHAIN/13-DATA_MODELS/)**

## 1. Overview
Serialization gives each physical unit a unique identity for full-lifecycle traceability.

## 2. Purpose
Tracking, materials/process/test traceability, fleet maintenance history, incident RCA, warranty/reliability, regulatory compliance (EASA/FAA/ESA).

## 3. Requirements

### 3.1 Items requiring serialization
**Critical Flight Items:** major aircraft/spacecraft assemblies and subsystems, propulsion, flight controls, life-critical structures, avionics/computing.  
**Controlled Items:** test articles, qual hardware, certification specimens, FTVs, critical ground test equipment, calibrated instruments (**[QMS calibration](../QUALITY_QMS/08-CALIBRATION_METROLOGY/)**).  
**High-Value:** unit cost > \$50k, long-lead, limited production.

### 3.2 Items not serialized
Standard hardware, bulk materials, consumables, low-cost COTS (< \$1k), documentation.

## 4. Serial Number Format

### 4.1 Standard
**`[PartNumber]/S/N [Sequential]-[LotCode]`**  
Example (PN per **02-PART_NUMBERING.md**): `ACFT-AIRF-00100/S/N 0015-L2024Q1`

- **PartNumber:** as defined in **[02-PART_NUMBERING.md](./02-PART_NUMBERING.md)** (e.g., `ACFT-AIRF-00100`)  
- **Sequential:** 4 digits `0001–9999` (extend to 5+ after 9999)  
- **LotCode (optional):** run/material batch

### 4.2 Rules
Start at `0001` per PN. Increment without gaps. Never reuse.

### 4.3 Lot codes
`L[YEAR][Q/M][BATCH]` → `L2024A`, `L2024Q1`, `L202401A`.

## 5. Application

### 5.1 Marking methods
**Permanent (preferred):** laser, dot-peen, chem etch, stamping (non-critical areas).  
**Semi-permanent:** anodized engraving, ink + protective coat, nameplates.  
**Temporary (in-process only):** labels, paint markers.

### 5.2 Location
Visible without disassembly, non-critical zones, protected from wear/environment, defined on drawing.

### 5.3 Requirements
Min height 2 mm, depth 0.05–0.15 mm (per drawing), sans-serif OCR font, high contrast.

### 5.4 Redundancy
Primary external mark + secondary internal/alt location. Include 2D code for scan.

## 6. Data Matrix Codes
ECC200 containing PN, S/N, lot, DOM.

Encoded example:
```

[P]ACFT-AIRF-00100[S]0015[L]L2024Q1[D]20240315

```
Placement: adjacent to HRI, ≥5×5 mm, scannable, protected.

## 7. Process

### 7.1 Assignment
Manufacturing requests → CM assigns next S/N → record in tracking system (linked to **[ITEMS.csv](./08-ITEM_MASTER/ITEMS.csv)**) → notify requester.

### 7.2 Physical marking
Prep surface → mark per spec → inspect → record completion in traveler/WI (**[INDUSTRIALISATION/06-WORK_INSTRUCTIONS/](../INDUSTRIALISATION/06-WORK_INSTRUCTIONS/)**).

### 7.3 Data capture (at serialization)
DOM, lot, operator ID, site, inspection status.

## 8. Lifecycle Tracking
Manufacturing → Testing → Integration → Delivery → Operations → Maintenance → Retirement.  
Records per S/N: material certs/lots, process history, inspections/tests, mods/repairs, usage (hours/cycles/missions), maintenance, failures/incidents, disposition.

Database: item master / PLM, with PN, S/N, status/location, mfg/test history, as-built configuration, effectivity, parent assembly.

## 9. Special Cases
**Prototypes:** `[PN]/PROTO-[###]` → `ACFT-AIRF-00100/PROTO-001`  
**Test articles:** `[PN]/TEST-[###]` → `ACFT-AIRF-00100/TEST-001`  
**Flight Test Vehicles:** `FTV-[###]` → `FTV-001`  
**Qualification units:** `QU-[PN]-[###]` → `QU-SCFT-STRC-00050-001`  
**Engineering models:** `EM-[PN]-[###]` → `EM-ACFT-PROP-00075-002`

## 10. Software/Firmware
Build numbers: `Major.Minor.Patch-Build` → `1.2.3-20240315`.  
Firmware embeds SW version, build date/time, host hardware S/N when loaded.

## 11. Documentation

### 11.1 Drawing notes
“THIS PART REQUIRES SERIALIZATION”, mark location, method, size/depth, Data-Matrix requirement.

### 11.2 Traveler
Steps for S/N assignment, marking operation, inspection, DB registration.

## 12. Quality Control
Verify PN/SN correctness, legibility, location, depth/quality, barcode scan.  
Nonconformance: do not obliterate; record NCR; seek disposition (**[QUALITY_QMS/02-PROCEDURES/PRO-004_NONCONFORMANCE.md](../QUALITY_QMS/02-PROCEDURES/PRO-004_NONCONFORMANCE.md)**).

## 13. Rework and Repair
S/N never changes or reuses. Rework/repair retains S/N; record all actions.  
Replacements: mark original S/N “REMOVED”; new unit has new S/N; cross-reference both histories.

## 14. Examples

### 14.1 Aircraft
| Item | Serial Number |
|---|---|
| Wing assembly | `ACFT-AIRF-00100/S/N 0015-L2024Q1` |
| Propulsion module | `ACFT-PROP-00050/S/N 0003-L202401A` |
| Flight computer | `ACFT-AVNX-00200/S/N 0042` |

### 14.2 Spacecraft
| Item | Serial Number |
|---|---|
| Primary structure | `SCFT-STRC-00010/S/N 0001-L2024A` |
| Solar array | `SCFT-PWER-00025/S/N 0002-L2024B` |
| Reaction wheel | `SCFT-GNCE-00100/S/N 0008` |

### 14.3 Test/Qual
| Item | Serial Number |
|---|---|
| Flight Test Vehicle | `FTV-001` |
| Static test article | `ACFT-AIRF-00100/TEST-001` |
| Qualification unit | `QU-SCFT-STRC-00050-001` |
| Engineering model | `EM-ACFT-PROP-00075-002` |

## 15. Governance
Authority: Configuration Manager. Assignment: Manufacturing Eng with CM approval. DB maintenance: CM. Quarterly audits: Quality. AML/AVL and supplier links: **[SUPPLY_CHAIN/13-DATA_MODELS/AML_APPROVED_MFR_LIST.csv](../SUPPLY_CHAIN/13-DATA_MODELS/AML_APPROVED_MFR_LIST.csv)** · **[.../AVL_APPROVED_VENDOR_LIST.csv](../SUPPLY_CHAIN/13-DATA_MODELS/AVL_APPROVED_VENDOR_LIST.csv)**.
```
