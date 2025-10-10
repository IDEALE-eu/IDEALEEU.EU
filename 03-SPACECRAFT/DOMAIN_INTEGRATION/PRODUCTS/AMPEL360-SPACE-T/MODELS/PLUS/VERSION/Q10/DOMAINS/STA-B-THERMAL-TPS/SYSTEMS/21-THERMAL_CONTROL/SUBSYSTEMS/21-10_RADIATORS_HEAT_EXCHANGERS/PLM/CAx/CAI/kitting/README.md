# Kitting — 21-10_RADIATORS_HEAT_EXCHANGERS

## Purpose

Kitting packages define parts lists, material requirements, staging procedures, and readiness verification for radiator, LPHX, and coldplate integration operations.

## Content Types

- **Kitting Lists** — Complete parts and materials inventory
- **Staging Procedures** — Parts preparation and storage
- **Readiness Checklists** — Pre-integration verification
- **Material Certs** — Traceability documentation requirements

## File Formats

- `.xlsx` — Kitting lists with part numbers and quantities
- `.pdf` — Printed kitting packages and checklists

## Naming Convention

```
KIT-21-10-{identifier}__{revision}.xlsx
```

**Examples:**
- `KIT-21-10-radiator_panel__r01.xlsx`
- `KIT-21-10-lphx_integration__r02.xlsx`
- `KIT-21-10-coldplate_assy__r01.xlsx`

## Kitting List Requirements

Each kitting list must include:
- **Part Numbers** — Drawing numbers, vendor part numbers
- **Descriptions** — Clear part identification
- **Quantities** — Required quantity per assembly
- **Material Specs** — Material type, grade, specification
- **Traceability** — Serial numbers, lot codes, batch numbers
- **Expiration Dates** — For adhesives, TIM, perishables
- **Storage Requirements** — Temperature, humidity, cleanliness
- **Inspection Status** — Receiving inspection, QA acceptance
- **Supplier/Source** — Vendor, stock location, cage code

## Typical Kitting Contents

### Hardware
- Radiator panels with serials
- LPHX units with serials
- Coldplates with serials
- Mounting brackets and fittings
- Fasteners (bolts, nuts, washers) per torque table

### Consumables
- Adhesives with batch numbers and expiration dates
- Thermal interface materials (TIM)
- Shims (various thicknesses)
- Cleaning solvents (IPA, acetone)
- Wipes and swabs

### Tools & MGSE
- Torque wrenches (calibrated)
- Fixtures and alignment tools
- Dispensing equipment for adhesive/TIM
- Measurement tools (calipers, micrometers, dial indicators)

### Documentation
- Work instructions
- Travelers (blank, ready for data entry)
- Torque tables
- Bondline specifications
- Inspection checklists

## Kitting Process

1. **Pull Parts:** Retrieve from stock per kitting list
2. **Verify Traceability:** Check serials, lot codes, certs
3. **Inspect:** Visual inspection, damage check
4. **Verify Expiration:** Adhesives, TIM within shelf life
5. **Stage:** Organize in cleanroom or controlled area
6. **Document:** Record pulled items, serials, batch numbers
7. **Sign-off:** QA approval before release to production

## Readiness Verification

Before integration, verify:
- [ ] All parts present and accounted for
- [ ] Correct part numbers and revisions
- [ ] Serials match traveler
- [ ] Material certs available and valid
- [ ] Adhesives/TIM within shelf life
- [ ] Tools calibrated and available
- [ ] Work instructions and travelers ready
- [ ] Personnel trained and qualified
- [ ] Facility conditions acceptable (temp, humidity, cleanliness)

## Cross-References

- [Parent: CAI](../README.md)
- [Work Instructions](../work_instructions/README.md)
- [Assembly Plans](../assembly_plans/README.md)
- [Travelers](../travelers/README.md)
- [Bondline](../bondline/README.md)
- [Torque Tables](../torque_tables/README.md)

## Standards & Constraints

- **Traceability:** All flight hardware serials tracked
- **Shelf Life:** Verify before issue to production
- **Storage:** Per material datasheet (e.g., refrigerated adhesives)
- **Cleanliness:** Clean parts in controlled environment
- **ESD:** ESD protection for electronics and heaters

## Revision Control

- Kitting lists tied to work instruction and assembly plan revisions
- Changes require engineering review
- Material substitutions require approval and ECO
- Previous revisions archived
