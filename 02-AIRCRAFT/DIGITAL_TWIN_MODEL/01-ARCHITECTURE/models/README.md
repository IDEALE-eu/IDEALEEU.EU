# models

**📍 [IDEALE-EU](../../../../) > [02-AIRCRAFT](../../../) > [DIGITAL_TWIN_MODEL](../../) > [01-ARCHITECTURE](../) > models**

Model artifacts for digital twin execution.

## Purpose

This directory contains compiled model artifacts ready for execution in the digital twin runtime.

## Contents

- **[fmu/](fmu/)** - Functional Mock-up Units (FMI 2.0/3.0)
  - **[placeholder.fmu](fmu/placeholder.fmu)** - Example FMU file
- **[simulink/](simulink/)** - Simulink model exports
- **[modelica/](modelica/)** - Modelica model files

## Model Types

### FMU Models
- Physics-based models (aerodynamics, propulsion, fuel system)
- Exported from Simulink, Modelica, or custom tools
- FMI 2.0 or 3.0 compliant

### Simulink Models
- Control logic, state machines
- Code generation for real-time execution

### Modelica Models
- Multi-domain physical systems
- Open-standard declarative modeling

## Usage

Models are loaded by the twin runtime:
```python
from twin.runtime import FMULoader
model = FMULoader.load('models/fmu/fuel_system.fmu')
model.initialize(parameters)
output = model.step(inputs, dt=0.01)
```

## Related Documents

- **[../../02-MODELS/](../../02-MODELS/)** - Model specifications and source
- **[../execution/](../execution/)** - Execution orchestration
- **[../packaging/](../packaging/)** - Model packaging tools

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2025-01-XX | Model Integration Team | Initial model artifacts |

---

**Status**: Configuration-controlled per `00-PROGRAM/CONFIG_MGMT/`
