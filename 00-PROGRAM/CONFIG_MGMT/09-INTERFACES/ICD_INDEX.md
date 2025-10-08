# Interface Control Document (ICD) Index

## Overview
Catalog of all ICDs for the IDEALE EU program. ICDs define and control interfaces between systems, subsystems, and external entities.

## Purpose
- Clear interface requirements
- Party coordination
- Configuration control
- Traceability of changes
- Mismatch prevention

## ICD Numbering
Format: **ICD-[XXXX]** (sequential 4-digit).  
Template: **[ICD-XXXX.md](./ICD-XXXX.md)**

## ICD Index

| ICD Number | Title | Version | Interface Parties | Status | Owner | Date |
|---|---|---|---|---|---|---|
| [ICD-0001](./ICD-0001.md) | Aircraft–Propulsion System Interface | 1.0 | Airframe ↔ Propulsion | Draft | J. Smith | 2024-01-15 |
| [ICD-0002](./ICD-0002.md) | Spacecraft–Ground Segment Interface | 1.0 | Spacecraft ↔ Ground Station | Draft | M. Johnson | 2024-01-20 |
| [ICD-0003](./ICD-0003.md) | Avionics–Flight Control Interface | 1.0 | Avionics ↔ Flight Control | Draft | K. Lee | 2024-01-25 |
| [ICD-0004](./ICD-0004.md) | Power System Interface | 1.0 | Power Gen ↔ Distribution | Draft | A. Chen | 2024-02-01 |
|  |  |  |  |  |  |  |

> Baselines: [SRR](../04-BASELINES/SRR/) · [PDR](../04-BASELINES/PDR/) · [CDR](../04-BASELINES/CDR/) · [TRR](../04-BASELINES/TRR/) · [PRR](../04-BASELINES/PRR/) · [ORR_EIS](../04-BASELINES/ORR_EIS/) · [FRR](../04-BASELINES/FRR/)

## Interface Categories

### Internal Aircraft
- Airframe ↔ Propulsion
- Airframe ↔ Landing Gear
- Avionics ↔ Flight Controls
- Power Generation ↔ Distribution
- Cabin ↔ Environmental Control
- Hydrogen System ↔ Propulsion
- Thermal Management ↔ Systems

### Internal Spacecraft
- Structures ↔ Propulsion
- Power ↔ Avionics
- GNC ↔ Propulsion
- Thermal ↔ Power
- Communications ↔ Avionics
- Solar Arrays ↔ Power System

### External
- Aircraft ↔ Ground Support Equipment
- Aircraft ↔ Airport Infrastructure
- Spacecraft ↔ Ground Segment
- Spacecraft ↔ Launch Vehicle
- Vehicle ↔ Test Equipment

### Cross-Program
- Aircraft ↔ Spacecraft (shared tech)
- Design ↔ Manufacturing
- Engineering ↔ Operations

## ICD Development Process
1. Identify interface (SE)  
2. Assign number (CM)  
3. Draft using template (**[ICD-XXXX.md](./ICD-XXXX.md)**)  
4. Review (stakeholders)  
5. Approve (CCB) → **[../05-CCB/](../05-CCB/)**  
6. Release (CM) under **[../04-BASELINES/](../04-BASELINES/)**  
7. Maintain via ECR/ECO: **[../06-CHANGES/ECR/](../06-CHANGES/ECR/)** · **[../06-CHANGES/ECO/](../06-CHANGES/ECO/)**

## Status Definitions
**Draft** · **Review** · **Approved** · **Active** · **Superseded** · **Obsolete**

## Traceability
- Requirements: **[../10-TRACEABILITY/REQ_ITEM.csv](../10-TRACEABILITY/REQ_ITEM.csv)**  
- Items: **[../08-ITEM_MASTER/](../08-ITEM_MASTER/)**  
- Test procedures: see each ICD Appendix D and **[../../INDUSTRIALISATION/10-TEST_INSPECTION/](../../INDUSTRIALISATION/10-TEST_INSPECTION/)**

## Documentation Storage
- Active ICDs: **this folder**  
- Superseded: **[./ARCHIVE/](./ARCHIVE/)** (create if missing)  
- Standards refs: **[../../STANDARDS/](../../STANDARDS/)**

## Metrics
Track in **[../11-AUDITS/](../11-AUDITS/)** and program KPIs:
- Active vs. draft ICDs
- Review cycle time
- Interface-related ECRs
- Discrepancies/issues

## Governance
- Authority: Systems Engineering + Configuration Management  
- Approval: **[CCB](../05-CCB/)**  
- Quarterly review of this index

## References
- **[01-CM_PLAN.md](../01-CM_PLAN.md)**  
- **[../06-CHANGES/](../06-CHANGES/)**  
- **[../10-TRACEABILITY/](../10-TRACEABILITY/)**
```
