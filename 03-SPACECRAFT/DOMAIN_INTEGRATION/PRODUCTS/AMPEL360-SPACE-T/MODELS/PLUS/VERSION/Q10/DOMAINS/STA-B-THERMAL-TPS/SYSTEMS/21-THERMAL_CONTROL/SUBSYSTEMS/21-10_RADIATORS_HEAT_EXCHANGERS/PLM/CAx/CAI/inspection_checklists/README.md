# Inspection Checklists — 21-10_RADIATORS_HEAT_EXCHANGERS

## Purpose

Inspection checklists define acceptance criteria and measurement procedures for radiator, LPHX, and coldplate installations, including flatness, shim selection, hole patterns, port sizes/threads, and TIM thickness verification.

## Content Types

- **Flatness Checks** — Surface flatness measurements and tolerances
- **Port Inspections** — Thread verification, port sizes, cleanliness
- **Hole Pattern Verification** — Hole location and size checks
- **TIM Thickness Inspection** — Post-clamp thickness measurements
- **Shim Selection Logs** — Gap measurements and shim sizing

## File Formats

- `.xlsx` — Checklist templates with data entry fields
- `.pdf` — Completed and signed inspection records

## Naming Convention

```
CHK-21-10-{type}__{revision}.xlsx
```

**Examples:**
- `CHK-21-10-flatness__r01.xlsx`
- `CHK-21-10-ports__r02.xlsx`
- `CHK-21-10-threads__r01.xlsx`
- `CHK-21-10-hole_pattern__r00.xlsx`
- `CHK-21-10-tim_thickness__r01.xlsx`

## Inspection Checklist Requirements

Each checklist must include:
- **Inspection Criteria** — Acceptance limits and tolerances
- **Measurement Method** — Tools, procedures, standards
- **Data Recording** — Fields for measured values
- **Accept/Reject** — Pass/fail decision logic
- **Inspector Sign-off** — QA stamp and date
- **Traceability** — Hardware serial, location, date
- **Reference Documents** — Drawings, specifications, work instructions
- **Non-conformance Process** — Steps if acceptance not met

## Inspection Types

### Flatness Inspection
- **Method:** Dial indicator or CMM scan
- **Tolerance:** Per drawing (typical ±0.05 mm over 300 mm span)
- **Frequency:** Each radiator panel before installation
- **Recording:** Min, max, deviation map

### Port Inspection
- **Method:** Thread gauge, bore gauge
- **Checks:** Thread class, depth, cleanliness, damage
- **Frequency:** 100% of leak ports and fluid connections
- **Recording:** Pass/fail per port, serial traced

### Thread Inspection
- **Method:** Go/no-go thread gauges
- **Tolerance:** Per ASME B1.1 or drawing callout
- **Frequency:** Critical fastener holes, leak ports
- **Recording:** Gauge ID, pass/fail, corrective action

### Hole Pattern Verification
- **Method:** CMM or optical comparator
- **Tolerance:** Per drawing (typical ±0.1 mm location)
- **Frequency:** First article, suspect conditions
- **Recording:** Measured vs. nominal, deviation report

### TIM Thickness Inspection
- **Method:** Caliper or ultrasonic gauge
- **Tolerance:** Per drawing (typical 0.05-0.15 mm)
- **Frequency:** Each coldplate after torque
- **Recording:** Multiple points, average, min, max

## Cross-References

- [Parent: CAI](../README.md)
- [Work Instructions](../work_instructions/README.md)
- [Travelers](../travelers/README.md)
- [Torque Tables](../torque_tables/README.md)
- [As-Run Records](../as_run_records/README.md)

## Standards & Constraints

- **Units:** mm, N·m, °C
- **Calibration:** All gages must have valid cal certs
- **Traceability:** Inspection data linked to hardware serial
- **Documentation:** Signed hard copy or electronic with PKI
- **Non-conformance:** MRB process for out-of-spec conditions

## Revision Control

- Checklists maintained under configuration control
- Revisions coordinated with drawings and work instructions
- Previous versions archived
- Changes require engineering and QA approval
