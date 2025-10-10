# ATP/ATR — 21-10_RADIATORS_HEAT_EXCHANGERS

## Purpose

Acceptance Test Procedures (ATP) and Acceptance Test Reports (ATR) for radiator, LPHX, and coldplate installations. These documents define and record functional testing, leak checks, and performance verification after integration.

## Content Types

- **Acceptance Test Procedures (ATP)** — Test methods and acceptance criteria
- **Acceptance Test Reports (ATR)** — Test results and data
- **Leak Test Procedures** — Pressure/helium leak test methods
- **Functional Test Procedures** — Continuity, resistance, flow checks

## File Formats

- `.pdf` — Controlled ATP documents and completed ATR reports
- `.xlsx` — Test data templates and logs

## Naming Convention

```
ATP-21-10-{identifier}__{revision}.pdf
ATR-21-10-{identifier}__SN{serial}__{date}.pdf
```

**Examples:**
- `ATP-21-10-radiator_leak_test__r01.pdf`
- `ATP-21-10-lphx_flow_check__r02.pdf`
- `ATP-21-10-coldplate_continuity__r01.pdf`
- `ATR-21-10-radiator_leak_test__SN042__20250315.pdf`

## ATP Requirements

Each ATP must include:
- **Scope** — Hardware and tests covered
- **Prerequisites** — Required completed steps, hardware configuration
- **Test Equipment** — Required instruments, calibration requirements
- **Test Setup** — Configuration, connections, instrumentation
- **Test Procedures** — Step-by-step test methods
- **Acceptance Criteria** — Pass/fail limits, tolerances
- **Data Recording** — Tables for measured data
- **Safety** — Hazards, precautions, PPE
- **Sign-offs** — Test engineer, QA witness, approval

## Test Types

### Leak Tests
- **Method:** Pressure decay or helium mass spectrometer
- **Pressure:** Per specification (e.g., 200 psi for fluid systems)
- **Duration:** Stabilization + measurement (e.g., 1 hour min)
- **Acceptance:** Leak rate <1×10⁻⁶ scc/s helium (typical)
- **Documentation:** Leak rate, temperature, serial numbers

### Continuity Tests
- **Method:** Ohmmeter or multimeter
- **Application:** Heater circuits, sensors, electrical bonding
- **Acceptance:** <1 Ω for power circuits, <0.1 Ω for bonding
- **Documentation:** Measured resistance per circuit

### Flow Tests (LPHX, Coldplates)
- **Method:** Flow meter, pressure gauges
- **Application:** Verify no blockage, proper flow distribution
- **Acceptance:** Flow within design range, pressure drop within limits
- **Documentation:** Flow rate, inlet/outlet pressure, temperature

### Functional Tests
- **Method:** Power-up, sensor read-back, actuator operation
- **Application:** Heaters, temperature sensors, valves
- **Acceptance:** All functions operational, readings within range
- **Documentation:** Functional status, readings, performance

## ATR Requirements

Each ATR must include:
- **Test Identification** — ATP reference, hardware serial
- **Test Date/Time** — Complete chronology
- **Test Personnel** — Test engineer, inspector, witnesses
- **Test Equipment** — Instrument serials and calibration dates
- **Test Data** — All measured values recorded
- **Deviations** — Any non-conformances or anomalies
- **Disposition** — Accept, reject, or use-as-is with rationale
- **Sign-offs** — Test engineer, QA, approval authority

## Test Sequence (Typical)

1. **Pre-test Inspection:** Visual, configuration verification
2. **Instrumentation Setup:** Install sensors, gages, leak test fixtures
3. **Initial Readings:** Baseline measurements
4. **Execute Test:** Perform per ATP steps
5. **Record Data:** Populate ATR with all measurements
6. **Evaluate:** Compare results to acceptance criteria
7. **Disconnect:** Remove test equipment
8. **Post-test Inspection:** Verify no damage or contamination
9. **Disposition:** Accept or reject hardware
10. **Documentation:** Complete ATR, approvals, archive

## Cross-References

- [Parent: CAI](../README.md)
- [Work Instructions](../work_instructions/README.md)
- [Travelers](../travelers/README.md)
- [As-Run Records](../as_run_records/README.md)
- [CAV Validation](../../CAV/README.md)
- [CMP Compliance](../../CMP/README.md)

## Standards & Constraints

- **Units:** Standard SI units; pressure in psi or Pa, flow in LPM
- **Calibration:** All test equipment must have valid cal certs
- **Traceability:** Hardware serials, test equipment serials
- **Environment:** Record ambient temperature, humidity
- **Leak Rate:** Typical spacecraft requirement <1×10⁻⁶ scc/s He

## Handoff to Test

After CAI operations complete:
- [ ] All work instructions executed and signed
- [ ] Travelers complete with as-built data
- [ ] Inspection checklists passed
- [ ] ATP/ATR executed and approved
- [ ] As-run records archived
- [ ] Hardware ready for handoff to CAV for TVAC/leak/proof testing

## Revision Control

- ATP documents maintained under configuration control
- ATR reports are archived records (read-only after approval)
- ATP changes require engineering review and approval
- ATR cannot be modified; use addendum for corrections
