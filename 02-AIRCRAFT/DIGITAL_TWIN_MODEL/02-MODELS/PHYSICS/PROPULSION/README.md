# PROPULSION

**📍 [IDEALE-EU](../../../../) > [02-AIRCRAFT](../../../) > [DIGITAL_TWIN_MODEL](../../) > 02-MODELS/PHYSICS > PROPULSION**

Engine and electric motor performance models, FADEC (Full Authority Digital Engine Control) plants.

## Purpose

Propulsion system models for thrust, fuel consumption, and engine health monitoring.

## Contents

- **ENGINE_MODELS/** - Thermodynamic cycle models (0D, 1D)
- **ELECTRIC_MOTOR/** - EM performance models (if applicable)
- **FADEC_PLANTS/** - Engine control system models
- **DEGRADATION/** - Performance degradation models (time/cycle-based)

## ATA Chapter Links

- **ATA-70** - Engine (General)
- **ATA-71-79** - Engine systems (fuel, ignition, exhaust, oil, etc.)
- **ATA-76** - Engine Controls
- **ATA-80** - Starting

## Fidelity Levels

- **Level 5 (Real-Time)**: Map lookup, <1ms
- **Level 4 (High-Fidelity)**: 1D cycle analysis, seconds
- **Level 3 (Detailed)**: 2D CFD (compressor, turbine), hours

## Validation Requirements

- Ground test correlation: Thrust within ±2%, fuel flow within ±3%
- Flight test correlation: Thrust within ±3%, EGT within ±20°C

---

**Status**: Configuration-controlled per `00-PROGRAM/CONFIG_MGMT/`
