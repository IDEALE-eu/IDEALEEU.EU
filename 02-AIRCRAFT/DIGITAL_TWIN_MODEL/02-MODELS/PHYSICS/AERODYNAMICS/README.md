# AERODYNAMICS

**📍 [IDEALE-EU](../../../../) > [02-AIRCRAFT](../../../) > [DIGITAL_TWIN_MODEL](../../) > 02-MODELS/PHYSICS > AERODYNAMICS**

CFD surrogates, aerodynamic polars, and load predictions for the aircraft.

## Purpose

This directory contains aerodynamic models including CFD-based reduced-order models (ROM), aerodynamic polar databases, and load prediction tools.

## Contents

- **CFD_SURROGATES/** - Reduced-order models (GPR, POD, neural networks) for real-time aerodynamic predictions
- **POLARS/** - Lift, drag, and moment coefficient databases (CL, CD, CM vs. α, β, δ)
- **LOADS/** - Aerodynamic load distributions for structural analysis
- **VALIDATION_DATA/** - Wind tunnel and flight test correlation data

## ATA Chapter Links

- **ATA-27** - Flight Controls (control surface aerodynamics)
- **ATA-57** - Wings (wing aerodynamics, high-lift devices)

## Model Types

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
