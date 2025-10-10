# As-Run Records — 21-10_RADIATORS_HEAT_EXCHANGERS

## Purpose

As-run records capture serialized installation data, measured gaps, shim selections, torque values, leak test IDs, and other as-built information for radiator, LPHX, and coldplate installations. These records provide traceability and configuration history for each flight unit.

## Content Types

- **Installation Logs** — Serial-specific operation records
- **Measured Data** — Gaps, shims, TIM thickness, flatness
- **Torque Logs** — Fastener installation records
- **Leak Test IDs** — Test dates, leak rates, disposition
- **Configuration Records** — As-built part lists and serials

## File Formats

- `.csv` — Structured data for database import
- `.xlsx` — Human-readable logs and summaries
- `.pdf` — Archived, signed records

## Naming Convention

```
RUN-21-10-{identifier}_logs__{date}.csv
RUN-21-10-SN{serial}_assy_data__{date}.xlsx
```

**Examples:**
- `RUN-21-10-serial_logs__20250315.csv`
- `RUN-21-10-SN042_assy_data__20250316.xlsx`
- `RUN-21-10-leak_test_summary__20250320.pdf`

## As-Run Data Requirements

Each record must include:
- **Hardware Identification** — Part number, serial number
- **Operation Date** — Date and time of installation
- **Personnel** — Mechanic, inspector, engineer
- **Configuration** — Installed components with serials
- **Measured Values** — Gaps, shims, TIM thickness, torques
- **Inspection Results** — Pass/fail status, deviations
- **Test Results** — Leak test, continuity, functional test
- **Deviations** — Non-conformances, waivers, MRB actions
- **Approvals** — Sign-offs and acceptance

## Data Fields (Typical CSV Format)

```csv
serial_number,part_number,operation,date,time,operator_id,inspector_id,parameter,measured_value,units,acceptance_limit,status,notes
SN042,21-10-001-RAD,gap_measurement,2025-03-15,14:30,JD123,QA456,gap_top_left,0.08,mm,0.05-0.15,PASS,
SN042,21-10-001-RAD,shim_selection,2025-03-15,14:35,JD123,QA456,shim_thickness,0.10,mm,N/A,ACCEPT,0.10mm shim installed
SN042,21-10-001-RAD,torque_install,2025-03-15,15:00,JD123,QA456,fastener_M6_01,9.2,Nm,9.0±0.8,PASS,
SN042,21-10-001-RAD,leak_test,2025-03-16,09:00,TEST789,QA456,leak_rate,5.0E-07,scc/s,<1.0E-06,PASS,He mass spec
```

## Record Types

### Gap Measurements
- **Location:** Identify by datum or grid reference
- **Tool:** Feeler gage, caliper, dial indicator
- **Data:** Measured gap in mm
- **Shim:** Selected shim thickness
- **Status:** Within tolerance or use-as-is with justification

### Torque Logs
- **Fastener ID:** Location per drawing or torque table
- **Target Torque:** Per torque table (N·m)
- **Actual Torque:** Measured value (N·m)
- **Re-torque:** If applicable, after cure or thermal cycle
- **Status:** Pass/fail based on tolerance
- **Witness:** QA inspector stamp

### TIM Thickness
- **Location:** Interface or measurement point
- **Pre-clamp:** Gap before assembly
- **Post-clamp:** Measured thickness after torque
- **Target:** Per drawing specification
- **Status:** Within tolerance or disposition

### Leak Test Results
- **Test ID:** Unique test number
- **Serial Number:** Hardware tested
- **Date/Time:** Test execution
- **Method:** Pressure decay or helium leak test
- **Result:** Leak rate or pass/fail
- **Disposition:** Accept, reject, retest

## Data Management

### Collection
- Record data in real-time during operations
- Use traveler templates for structured data entry
- Verify data with inspector before sign-off

### Validation
- Check for completeness and accuracy
- Verify serials and traceability
- Confirm acceptance criteria met

### Archival
- Export to CSV for database import
- Archive signed PDF copies
- Store in configuration management system
- Maintain backups per data retention policy

### Access
- Configuration management system
- Read-only access for historical data
- Authorized personnel for current operations

## Cross-References

- [Parent: CAI](../README.md)
- [Travelers](../travelers/README.md)
- [Inspection Checklists](../inspection_checklists/README.md)
- [ATP/ATR](../atp_atr/README.md)
- [Work Instructions](../work_instructions/README.md)

## Standards & Constraints

- **Units:** Standard SI units (mm, N·m, °C, scc/s)
- **Traceability:** All data linked to hardware serial
- **Data Integrity:** No erasures; corrections signed and dated
- **Retention:** Maintain for life of hardware
- **Security:** Controlled access, backup, disaster recovery

## Database Schema

As-run data should be structured for import to configuration database:
- **Hardware Table:** Serials, part numbers, configuration
- **Operations Table:** Date, time, operator, operation type
- **Measurements Table:** Parameter, value, units, status
- **Tests Table:** Test type, result, disposition
- **Deviations Table:** Non-conformances, MRB, waivers

## Revision Control

- As-run records are immutable once approved
- Corrections via addendum, not modification
- Version control for data schemas and templates
- Changes to data fields require database schema update
