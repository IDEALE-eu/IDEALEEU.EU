# ATA-05 — Time Limits and Maintenance Checks  
**Configuration Baseline**

This baseline defines the reference configuration for all **time-limited tasks, periodic maintenance checks, and service intervals** under ATA Chapter 05.

---

## Scope
Covers all airframe, propulsion, electrical, and systems items requiring:
- Calendar- or flight-time-based maintenance actions  
- A/B/C/D-check scheduling logic  
- Integration with S1000D data modules for maintenance procedures  
- ESG (environmental, social, governance) impact reporting per task

---

## Directory Overview

| Folder | Purpose |
|---------|----------|
| `01-MAINTENANCE_TASKS/` | Executable S1000D XML work packages (CAS-owned). |
| `02-DATA_MODULES/` | Source Data Modules (DMCs) defining individual requirements. |
| `03-IDENTIFICATION/` | Baseline identification, ESG declaration, CMP references. |
| `04-REVISIONS/` | Controlled change history and Engineering Change Notices. |

---

## Configuration Items
| CI ID | Description | Owner | Source |
|-------|--------------|--------|---------|
| `ATA-05/BL-2025.10` | Time Limits and Maintenance Checks baseline | CMP | `03-IDENTIFICATION/IDENTIFICATION_CARD.json` |
| `ECN-2025-05123` | Initial baseline creation | CMP | `04-REVISIONS/ECN-2025-05123.json` |

---

## Compliance References
- **S1000D Issue 5.0** — Data Module coding and publication structure  
- **EASA CS-25 / FAA Part 25.1529** — Instructions for Continued Airworthiness  
- **IDEALE-EU CMP-STD-1001** — Configuration and Maintenance Planning Standard  
- **ISO 14001:2015** — Environmental management reference for ESG declaration

---

## Version Control
All modifications follow CMP change governance.  
Each revision must update:
- `REVISION_HISTORY.yaml`
- Linked ECN record
- Updated `baselineId` in `IDENTIFICATION_CARD.json`

---

**Baseline Owner:** `CMP Lead — ATA-05`  
**Date:** 2025-10-24  
**Status:** Active (Baseline 1.0)
