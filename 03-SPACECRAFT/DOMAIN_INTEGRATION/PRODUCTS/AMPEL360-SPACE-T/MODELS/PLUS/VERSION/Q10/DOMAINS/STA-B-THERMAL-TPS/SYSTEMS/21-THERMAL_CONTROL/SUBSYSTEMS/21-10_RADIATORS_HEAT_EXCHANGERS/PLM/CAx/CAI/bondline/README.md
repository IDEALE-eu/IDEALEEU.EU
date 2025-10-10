# Bondline — 21-10_RADIATORS_HEAT_EXCHANGERS

## Purpose

Bondline packages define adhesive and thermal interface material (TIM) specifications, application procedures, cure parameters, bead size requirements, and witness coupon testing for radiator, LPHX, and coldplate installations.

## Content Types

- **Adhesive Specifications** — Material datasheets, properties, shelf life
- **Cure Parameters** — Temperature, time, humidity requirements
- **Application Procedures** — Bead size, pattern, surface prep
- **Witness Coupon Procedures** — Sample testing and acceptance criteria
- **TIM Specifications** — Thermal conductivity, thickness, application

## File Formats

- `.pdf` — Controlled bondline specification documents
- `.xlsx` — Cure log templates and data sheets

## Naming Convention

```
BOND-21-10-{type}__{revision}.pdf
```

**Examples:**
- `BOND-21-10-adhesive__r01.pdf`
- `BOND-21-10-cure__r02.pdf`
- `BOND-21-10-tim_application__r01.pdf`
- `BOND-21-10-witness_coupon__r00.pdf`

## Bondline Package Requirements

Each package must include:
- **Material Identification** — Manufacturer, part number, specification
- **Material Properties** — Strength, thermal conductivity, outgassing data
- **Shelf Life** — Expiration date, storage requirements
- **Surface Preparation** — Cleaning, priming, masking
- **Application Method** — Bead size, pattern, dispensing tool
- **Cure Schedule** — Time, temperature, humidity profile
- **Inspection Criteria** — Visual, fillet size, coverage
- **Witness Coupon** — Sample preparation and testing
- **Safety** — Hazards, PPE, ventilation requirements

## Adhesive Types

### Structural Adhesives
- **Application:** Radiator panel bonding, mount attachment
- **Typical Materials:** Epoxy, acrylic, polyurethane
- **Cure:** Ambient or elevated temperature
- **Properties:** High strength, low outgassing
- **Witness Test:** Pull test or shear test on coupons

### Thermal Interface Materials (TIM)
- **Application:** Coldplate interfaces, gap filling
- **Typical Materials:** Phase change, gap filler, grease, pad
- **Conductivity:** >1 W/m·K typical
- **Thickness:** 0.05-0.15 mm target
- **Cure:** None or low-temp phase change

## Cure Parameters

### Typical Adhesive Cure
- **Ambient Cure:** 20-25°C, 24-48 hours
- **Elevated Cure:** 60-80°C, 2-4 hours
- **Post-cure:** Optional 100-120°C, 1-2 hours
- **Humidity:** <60% RH during cure
- **Monitoring:** Temperature logged every 15 minutes

### TIM Application
- **Pre-application:** Surface clean, dry, free of oils
- **Thickness Control:** Shims or spacers if required
- **Clamp Pressure:** Per specification (e.g., 50 psi)
- **Cure/Set Time:** Per datasheet (minutes to hours)

## Witness Coupon Testing

- **Purpose:** Verify adhesive batch quality and cure
- **Quantity:** Minimum 3 coupons per batch/cure cycle
- **Geometry:** Per ASTM D1002 (lap shear) or equivalent
- **Testing:** Pull/shear test to failure
- **Acceptance:** ≥80% of datasheet strength, cohesive failure mode
- **Documentation:** Test results in cure log and traveler

## Application Procedures

### Bead Size and Pattern
- **Continuous Bead:** Width per drawing (e.g., 3-5 mm)
- **Dot Pattern:** Spacing and size per drawing
- **Fillet Verification:** Visual after clamp, fillet visible but not excessive
- **Coverage:** 100% of bonded area or per drawing

### Surface Preparation
- **Cleaning:** Solvent wipe (IPA, acetone per contamination plan)
- **Drying:** Air dry, verify no residue
- **Priming:** If required per adhesive datasheet
- **Masking:** Adjacent areas to prevent contamination

## Cross-References

- [Parent: CAI](../README.md)
- [Work Instructions](../work_instructions/README.md)
- [Travelers](../travelers/README.md)
- [Inspection Checklists](../inspection_checklists/README.md)
- [As-Run Records](../as_run_records/README.md)
- [CMP Materials & Process](../../CMP/README.md)

## Standards & Constraints

- **Units:** mm for dimensions, W/m·K for thermal conductivity, °C for temperature
- **Outgassing:** CVCM ≤ 0.1%, TML ≤ 1.0% per ASTM E595
- **Cleanliness:** NVR/particle per 21 cleanliness plan
- **Traceability:** Batch numbers, lot codes, cure logs
- **Shelf Life:** Verify not expired at time of use

## Revision Control

- Bondline specs maintained under configuration control
- Material changes require engineering and materials approval
- Coordinate with CAP process specifications
- Previous revisions archived
