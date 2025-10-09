# THERMAL

**📍 [IDEALE-EU](../../../../) > [02-AIRCRAFT](../../../) > [DIGITAL_TWIN_MODEL](../../) > 02-MODELS/PHYSICS > THERMAL**

Thermal models for cryogenic H₂ tanks, heat exchangers, and aircraft thermal management.

## Purpose

Thermal analysis for H₂ fuel system, cabin conditioning, and avionics cooling.

## Contents

- **CRYO_TANK/** - Liquid H₂ tank thermal models (boil-off, heat leak)
- **HEAT_EXCHANGERS/** - HX effectiveness models (counter-flow, cross-flow)
- **CABIN/** - Cabin thermal balance (HVAC, insulation)
- **AVIONICS_COOLING/** - Avionics bay thermal management

## ATA Chapter Links

- **ATA-21** - Air Conditioning
- **ATA-28** - Fuel (H₂ thermal management)
- **ATA-36** - Pneumatic

## Fidelity Levels

- **Level 5 (Real-Time)**: Lumped-parameter, <10ms
- **Level 4 (High-Fidelity)**: 3D CFD, hours
- **Level 3 (Detailed)**: 1D network, seconds

## Validation Requirements

- Ground test correlation: Temperature within ±2K, heat leak within ±10%

---

**Status**: Configuration-controlled per `00-PROGRAM/CONFIG_MGMT/`
