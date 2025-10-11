# AERODYNAMICS

**📍 [IDEALE-EU](../../../../) > [02-AIRCRAFT](../../../) > [DIGITAL_TWIN_MODEL](../../) > 02-MODELS/PHYSICS > AERODYNAMICS**

CFD surrogates, aerodynamic polars, and load predictions for the aircraft.

## Purpose

This directory contains aerodynamic models including CFD-based reduced-order models (ROM), aerodynamic polar databases, and load prediction tools.

**Goal**: Compute aerodynamic coefficients and loads at 200 Hz using α–Mach tables plus linear terms. Contract in `INTERFACES/`. Parameters in `PARAMS/`. Validation in `VALIDATION/` and `TESTS/`. Backward-incompatible changes → MAJOR bump.

## Contents

- **INTERFACES/** - I/O contracts and signal definitions (signals.yaml)
- **PARAMS/** - Model parameters and lookup tables
  - `coeffs_airframe.yaml` - Baseline coefficients and linear derivatives
  - `control_effectiveness.yaml` - Control surface effectiveness parameters
  - `tables/` - α–Mach lookup tables (CL, CD, Cm)
- **MODELS/** - Model documentation and API specifications
  - `api.md` - Runtime API and computation flow
  - `coefficient_build_up.md` - Mathematical formulation
- **VALIDATION/** - Validation test cases and reference data
  - `cases.yaml` - Validation test cases with expected values
  - `wind_tunnel_ref.csv` - Wind tunnel reference data
- **TESTS/** - Unit tests and golden test data
  - `test_aero_interp.py` - Interpolation and coefficient tests
  - `golden_inputs.npz` / `golden_outputs.npz` - Regression test data
- **SCRIPTS/** - Utility scripts
  - `gen_tables.py` - Generate coefficient tables from CFD/DATCOM
- **CFD_SURROGATES/** - Reduced-order models (GPR, POD, neural networks) for real-time aerodynamic predictions
- **POLARS/** - Lift, drag, and moment coefficient databases (CL, CD, CM vs. α, β, δ)
- **LOADS/** - Aerodynamic load distributions for structural analysis
- **VALIDATION_DATA/** - Wind tunnel and flight test correlation data

## ATA Chapter Links

- **ATA-27** - Flight Controls (control surface aerodynamics)
- **ATA-57** - Wings (wing aerodynamics, high-lift devices)

## Model Types

### Real-Time Coefficient Model (200 Hz)

The primary model for real-time simulation uses lookup tables with bilinear interpolation:

**Execution Flow:**
1. **Input**: Receive flight state (α, β, Mach, etc.) and control surface commands
2. **Base Coefficients**: Bilinear interpolation on CSV tables (e.g., `CL_alpha_mach.csv`)
3. **Coefficient Build-Up**: Add linear derivatives (`coeffs_airframe.yaml`) and control effectiveness (`control_effectiveness.yaml`)
4. **Calculate Forces/Moments**: Apply dynamic pressure and reference geometry
5. **Output**: Send forces and moments to Equations of Motion block

See `MODELS/api.md` for detailed execution flow and `MODELS/coefficient_build_up.md` for mathematical formulation.

### CFD Surrogates
- **Gaussian Process Regression (GPR)**: For smooth interpolation in flight envelope
- **Proper Orthogonal Decomposition (POD)**: For flow field reconstruction
- **Neural Network Surrogates**: For fast inference (<10ms)

### Polar Databases
- **Lookup Tables**: CL, CD, CM vs. α (angle of attack), β (sideslip), Mach, Re (Reynolds number)
- **Configuration States**: Clean, flaps 0°-40°, landing gear up/down

### Load Predictions
- **Distributed Loads**: Spanwise and chordwise pressure distributions
- **Integrated Loads**: Total lift, drag, pitching moment, rolling moment, yawing moment

## Fidelity Levels

- **Level 5 (Real-Time)**: Polar lookup, <1ms
- **Level 4 (High-Fidelity)**: GPR surrogate, 10-100ms
- **Level 3 (Detailed)**: POD reconstruction, 1-10s
- **Level 2 (Preliminary)**: Handbook methods (e.g., DATCOM), <1s

## Validation Requirements

- Wind tunnel correlation: RMSE <5% for CL, <10% for CD
- Flight test correlation: RMSE <3% for CL, <8% for CD

## Related Documents

- **../../01-ARCHITECTURE/ASSUMPTIONS_LIMITATIONS.md** - Validity envelope (Mach 0.1-0.82, AoA -5° to +15°)
- **../../05-CALIBRATION_ALIGNMENT/** - Calibration with wind tunnel and flight test data
- **../../06-VALIDATION_VERIFICATION/** - Validation test cases
- **../../../CONFIGURATION_BASE/ATA-27_FLIGHT_CONTROLS/** - Flight control system configuration
- **../../../CONFIGURATION_BASE/ATA-57_WINGS/** - Wing configuration

---

**Status**: Configuration-controlled per `00-PROGRAM/CONFIG_MGMT/`
