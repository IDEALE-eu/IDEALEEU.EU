# Travelers — 21-10_RADIATORS_HEAT_EXCHANGERS

## Purpose

Serialized travelers track individual hardware units through integration, capturing as-built data, sign-offs, torque records, and bond cure logs for each flight article.

## Content Types

- **Integration Travelers** — Per-serial tracking documents
- **Torque Records** — Fastener installation logs
- **Bond Cure Logs** — Adhesive/TIM application records
- **Sign-off Sheets** — Quality approval checkpoints

## File Formats

- `.xlsx` — Traveler templates and active documents
- `.pdf` — Completed and signed travelers (archived)
- `.csv` — Data export for database entry

## Naming Convention

```
TRV-21-10-{identifier}__{serial}.xlsx
```

**Examples:**
- `TRV-21-10-radiator_panel__SN001.xlsx`
- `TRV-21-10-lphx_unit__SN042.xlsx`
- `TRV-21-10-coldplate_assy__SN015.xlsx`

## Traveler Requirements

Each traveler must include:
- **Hardware Identification** — Part number, serial number, lot codes
- **Traceability** — Component serials, material certs, batch numbers
- **Operation Log** — Date, time, operator, inspector for each step
- **Measured Data** — Gaps, shims, TIM thickness, flatness
- **Torque Records** — Target, actual, witness, re-torque values
- **Bond Records** — Adhesive batch, mix ratio, cure time/temp
- **Inspection Results** — Pass/fail, measurements, photos
- **Deviations** — Non-conformances, MRB actions, waivers
- **Sign-offs** — Mechanic, inspector, engineer approvals
- **Final Configuration** — As-built part list and configuration

## Data Recording Standards

- **Torque Values:** Record in N·m with ±0.1 N·m precision
- **Gaps/Shims:** Measure in mm to ±0.01 mm
- **TIM Thickness:** Measure in mm to ±0.01 mm after clamp
- **Cure Times:** Log start time, end time, ambient temp
- **Operator ID:** Badge number or initials
- **Inspector Stamp:** QA stamp and date

## Cross-References

- [Parent: CAI](../README.md)
- [Work Instructions](../work_instructions/README.md)
- [Assembly Plans](../assembly_plans/README.md)
- [Torque Tables](../torque_tables/README.md)
- [Bondline](../bondline/README.md)
- [Inspection Checklists](../inspection_checklists/README.md)
- [As-Run Records](../as_run_records/README.md)

## Standards & Constraints

- **Units:** mm, N·m, °C
- **Traceability:** All components traced to material certs
- **Signatures:** Wet signature or electronic with PKI
- **Archival:** PDF/A format for long-term storage
- **Data Integrity:** No erasures; strikethrough and initial corrections

## Traveler Lifecycle

1. **Issue:** Blank traveler issued with hardware serial
2. **Active:** Populated during integration operations
3. **Review:** Engineering review of completed traveler
4. **Approve:** QA approval and sign-off
5. **Archive:** Scanned to PDF and stored in document control
6. **Database:** Key data extracted to configuration database

## Change Control

- Traveler template changes require engineering approval
- Active travelers cannot be modified; use deviation process
- Completed travelers are read-only records
- Any post-completion changes via ECO and traveler addendum
