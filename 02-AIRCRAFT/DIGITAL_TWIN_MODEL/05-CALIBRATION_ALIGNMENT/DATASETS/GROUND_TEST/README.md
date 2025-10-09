# GROUND_TEST

**📍 [IDEALE-EU](../../../../) > [02-AIRCRAFT](../../../) > [DIGITAL_TWIN_MODEL](../../) > 05-CALIBRATION_ALIGNMENT/DATASETS > GROUND_TEST**

Ground test rigs and benches data linked to ATA test configurations.

## Purpose

Calibration data from ground-based test rigs (structural, thermal, propulsion, H₂ systems).

## Contents

- **STRUCTURAL_GROUND_TEST/** - Wing, fuselage static/fatigue tests
- **THERMAL_GROUND_TEST/** - Cryo tank, heat exchanger tests
- **PROPULSION_GROUND_TEST/** - Engine test cell data
- **H2_GROUND_TEST/** - H₂ tank and BOP rig tests

## Data Format

Each test includes:
- **Test Plan**: Test objectives, procedures, acceptance criteria
- **Test Data**: Time-series sensor data (CSV, HDF5)
- **Test Report**: Results, observations, deviations

## ATA Chapter Links

- **ATA-28**: H₂ fuel system ground tests
- **ATA-51-57**: Structural tests (wing, fuselage, stabilizers)
- **ATA-70-80**: Propulsion system tests

## Integration

Data used for calibration (see `../CALIBRATION_PLAN.md`) and validation (see `../../06-VALIDATION_VERIFICATION/`).

---

**Status**: Configuration-controlled per `00-PROGRAM/CONFIG_MGMT/`
