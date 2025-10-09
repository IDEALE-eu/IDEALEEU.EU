# STATE_MACHINES

**📍 [IDEALE-EU](../../../../) > [02-AIRCRAFT](../../../) > [DIGITAL_TWIN_MODEL](../../) > 02-MODELS/BEHAVIORAL > STATE_MACHINES**

SysML state charts and Stateflow models for system behavior (e.g., IMA health, fuel sequencing).

## Purpose

Behavioral models using finite state machines for discrete system modes and transitions.

## Contents

- **IMA_HEALTH/** - Integrated Modular Avionics health monitoring state machines
- **FUEL_SEQUENCING/** - H₂ fuel system sequencing logic
- **SYSTEM_MODES/** - Aircraft-level mode management (startup, normal ops, degraded, emergency)

## Model Formats

- **SysML**: State machine diagrams from MBSE tool
- **Stateflow**: MATLAB/Simulink Stateflow charts
- **Executable**: C/C++ code generation for runtime

## Fidelity Level

- **Level 5 (Real-Time)**: State machine execution, <1ms per transition

## Validation Requirements

- Functional validation: 100% state/transition coverage
- Integration testing: HIL/SIL rig validation

---

**Status**: Configuration-controlled per `00-PROGRAM/CONFIG_MGMT/`
