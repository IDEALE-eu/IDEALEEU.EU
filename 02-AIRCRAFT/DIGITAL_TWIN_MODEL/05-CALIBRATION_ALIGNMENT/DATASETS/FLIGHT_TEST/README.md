# FLIGHT_TEST

**📍 [IDEALE-EU](../../../../) > [02-AIRCRAFT](../../../) > [DIGITAL_TWIN_MODEL](../../) > 05-CALIBRATION_ALIGNMENT/DATASETS > FLIGHT_TEST**

Flight test sensor packs and maneuvers data for model calibration.

## Purpose

Calibration data from flight test campaigns (aerodynamics, performance, systems).

## Contents

- **AERO_FLIGHT_TEST/** - Stall tests, polars, control effectiveness
- **PERFORMANCE_FLIGHT_TEST/** - Cruise performance, range, fuel consumption
- **SYSTEMS_FLIGHT_TEST/** - H₂ system, thermal, propulsion in-flight data

## Flight Test Matrix

| Test ID | Objective | Maneuvers | Data Collected |
|---------|-----------|-----------|----------------|
| **FT-AERO-001** | Stall characteristics | 1g stalls, approach stalls | α, β, CL, CM, control positions |
| **FT-AERO-002** | Control effectiveness | Doublets, frequency sweeps | δ_elevator, δ_aileron, δ_rudder, response |
| **FT-PERF-001** | Cruise performance | Steady cruise at multiple altitudes/speeds | Thrust, fuel flow, TAS, altitude |
| **FT-H2-001** | H₂ boil-off in flight | Long cruise (3 hours) | Tank pressure, temperature, mass flow |

## Data Quality

- **Sensor Accuracy**: Per instrument specifications (see `../../03-INTERFACES_APIS/STREAMS/INPUTS/TELEMETRY_MAP.csv`)
- **Data Rate**: 10-100 Hz (depends on parameter)
- **Preprocessing**: Outlier removal, signal filtering (low-pass for noise reduction)

## Integration

Data used for:
1. **Calibration**: Tune model parameters (see `../CALIBRATION_PLAN.md`)
2. **Validation**: Verify model accuracy (see `../../06-VALIDATION_VERIFICATION/`)
3. **Model Refinement**: Identify model deficiencies, drive improvements

---

**Status**: Configuration-controlled per `00-PROGRAM/CONFIG_MGMT/`
