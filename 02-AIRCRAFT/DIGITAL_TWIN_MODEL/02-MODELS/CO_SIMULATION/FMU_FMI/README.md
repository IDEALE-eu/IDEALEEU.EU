# FMU_FMI

**📍 [IDEALE-EU](../../../../) > [02-AIRCRAFT](../../../) > [DIGITAL_TWIN_MODEL](../../) > 02-MODELS/CO_SIMULATION > FMU_FMI**

Functional Mock-up Units (FMUs) and FMI 3.0 configurations for co-simulation.

## Purpose

FMU library for co-simulation of aircraft subsystems.

## Contents

- **FMU_LIBRARY/** - Compiled FMUs for each subsystem
- **CONNECTION_MATRIX.csv** - Variable mapping between FMUs
- **FMI_CONFIG/** - FMI 3.0 configuration files

## FMU List

| FMU Name | Subsystem | Inputs | Outputs | Update Rate |
|----------|-----------|--------|---------|-------------|
| **Aero_FMU** | Aerodynamics | α, β, Mach, δ (control surfaces) | CL, CD, CM | 100 Hz |
| **Struct_FMU** | Structures | Loads (Fx, Fy, Fz, Mx, My, Mz) | Deflections, Stress | 100 Hz |
| **Thermal_FMU** | Thermal | Heat sources, ambient T | Component temps | 1 Hz |
| **Propulsion_FMU** | Propulsion | Throttle, altitude, Mach | Thrust, fuel flow, EGT | 10 Hz |
| **H2_FMU** | H₂ Energy | Fuel demand, ambient T | Tank pressure, boil-off | 1 Hz |
| **Control_FMU** | Control Logic | Sensors, pilot commands | Actuator commands | 50 Hz |

## FMI 3.0 Features

- **Co-Simulation**: Model exchange for subsystem simulation
- **Event Handling**: Discrete events (e.g., gear extension, mode changes)
- **Continuous Outputs**: Smooth interpolation between time steps

## Connection Matrix

Example (see `CONNECTION_MATRIX.csv` for full matrix):
```
Aero_FMU.CL → Struct_FMU.Lift
Aero_FMU.CD → Propulsion_FMU.Drag
Propulsion_FMU.Thrust → Aero_FMU.ThrustInput
H2_FMU.FuelFlow → Propulsion_FMU.FuelAvailable
```

---

**Status**: Configuration-controlled per `00-PROGRAM/CONFIG_MGMT/`
