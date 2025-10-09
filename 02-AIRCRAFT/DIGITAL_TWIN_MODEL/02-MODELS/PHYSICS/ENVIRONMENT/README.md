# ENVIRONMENT

**📍 [IDEALE-EU](../../../../) > [02-AIRCRAFT](../../../) > [DIGITAL_TWIN_MODEL](../../) > 02-MODELS/PHYSICS > ENVIRONMENT**

Atmospheric models and mission profile definitions.

## Purpose

Environmental models for atmospheric conditions and mission profiles.

## Contents

- **ATMOSPHERE/** - Atmospheric models (ISA, non-standard atmosphere, winds)
- **MISSION_PROFILES/** - Typical mission profiles (climb, cruise, descent)

## Fidelity Levels

- **Level 5 (Real-Time)**: ISA lookup, <1ms
- **Level 3 (Detailed)**: Weather data integration, seconds

## Validation Requirements

- Correlation with METAR/TAF weather data: Temperature within ±2K, pressure within ±1 hPa

---

**Status**: Configuration-controlled per `00-PROGRAM/CONFIG_MGMT/`
