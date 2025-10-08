# AIRCRAFT_TWIN

Aircraft digital twin models and instances.

## Purpose

This directory contains the digital twin models specific to the aircraft program, including physics-based models, behavioral models, data-driven ML models, and per-serial twin instances.

## Contents

- **README.md** - This file
- **PHYSICS_MODELS/** - FEM, CFD, thermal, H2 systems (CAE exports)
- **BEHAVIORAL_MODELS/** - Control logic, state machines (SysML/Modelica)
- **DATA_DRIVEN_MODELS/** - ML surrogates, anomaly detectors (ONNX/Python)
- **TWIN_INSTANCE/** - Per-serial twin instances (e.g., ACFT-001, ACFT-002)
- **TWIN_API_SPEC.yaml** - Standardized API interface for operations/MRO

## Model Organization

### Physics Models
- Aerodynamics (CFD)
- Structures (FEM)
- Propulsion (H2 systems, combustion)
- Thermal management
- Electromagnetics (EMI/EMC)

### Behavioral Models
- Flight control logic
- System mode management
- Fault detection and isolation
- Power management

### Data-Driven Models
- Anomaly detection
- Predictive maintenance
- Performance optimization
- Surrogate models for real-time operation

## Per-Serial Instances

Each aircraft has a dedicated twin instance:
- ACFT-001: First production aircraft
- ACFT-002: Second production aircraft
- ...

Each instance includes:
- As-built configuration
- As-maintained configuration
- Flight history and usage data
- Maintenance events
- Performance trends

## Related Documents

- **05-DIGITAL_TWIN/TWIN_DEFINITION.md** - Digital twin strategy and fidelity levels
- **05-DIGITAL_TWIN/TWIN_VALIDATION/** - Validation methodology
- **02-AIRCRAFT/DIGITAL_TWIN_MODEL/** - Aircraft-specific twin implementation
