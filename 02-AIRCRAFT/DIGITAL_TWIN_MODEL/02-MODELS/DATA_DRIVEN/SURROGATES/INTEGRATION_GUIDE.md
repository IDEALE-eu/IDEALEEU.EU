# Integration Guide: Surrogates with Control Logic for Co-Simulation

**Version**: 1.0  
**Date**: 2024-11-20  
**Author**: Digital Twin Architecture Team

---

## Overview

This document describes how data-driven surrogate models integrate with behavioral control logic to enable closed-loop co-simulation in the aircraft digital twin.

## Architecture Context

```
Digital Twin Architecture (Layer 2 - Model Layer)
│
├── Physics Model Runtime
│   └── Surrogates (this directory)
│       ├── Aerodynamics → aero_wing_cl_cd
│       ├── Thermal → thermal_avionics_temp
│       └── Structures → struct_fatigue_cycles
│
├── Behavioral Model Runtime
│   └── Control Logic (02-MODELS/BEHAVIORAL/CONTROL_LOGIC/)
│       ├── Autopilot
│       ├── Engine Control
│       └── Thermal Management
│
└── Co-Simulation Orchestrator
    ├── FMU Manager (loads surrogate FMUs)
    └── Master Algorithm (coordinates time stepping)
```

See [../../01-ARCHITECTURE/REFERENCE_ARCHITECTURE.md](../../01-ARCHITECTURE/REFERENCE_ARCHITECTURE.md) for complete architecture.

## Use Case: Closed-Loop Thermal Management

### Scenario

Aircraft thermal management system uses:
1. **Surrogate Model**: `thermal_avionics_temp` predicts component temperature
2. **Control Logic**: PID controller adjusts cooling fan speed
3. **Co-Simulation**: Iterates at 10 Hz to maintain temperature setpoint

### Implementation

#### 1. Package Surrogate as FMU

```bash
cd SURROGATES/TOOLS
./pack_fmu.py --model-dir ../thermal_avionics_temp/1.0.0/ \
              --fmu-name thermal_avionics_temp \
              --fmi-version 2.0
```

This creates: `thermal_avionics_temp/1.0.0/runtime/fmu/thermal_avionics_temp.fmu`

#### 2. Load FMU in Co-Simulation Environment

```python
from fmpy import simulate_fmu
import numpy as np

# Load surrogate FMU
thermal_fmu = load_fmu("thermal_avionics_temp.fmu")

# Initialize
thermal_fmu.setup_experiment(start_time=0.0, stop_time=3600.0)
thermal_fmu.enter_initialization_mode()
thermal_fmu.exit_initialization_mode()
```

#### 3. Implement Control Logic

```python
class ThermalController:
    """PID controller for thermal management."""
    
    def __init__(self, setpoint=70.0, Kp=0.5, Ki=0.1, Kd=0.05):
        self.setpoint = setpoint  # Target temperature (°C)
        self.Kp, self.Ki, self.Kd = Kp, Ki, Kd
        self.integral = 0.0
        self.prev_error = 0.0
    
    def update(self, T_measured, dt):
        """Compute control action (airflow adjustment)."""
        error = self.setpoint - T_measured
        self.integral += error * dt
        derivative = (error - self.prev_error) / dt
        
        # PID output
        control = (self.Kp * error + 
                   self.Ki * self.integral + 
                   self.Kd * derivative)
        
        # Convert to airflow (m³/min)
        airflow = np.clip(3.0 + control, 0.5, 8.0)
        
        self.prev_error = error
        return airflow
```

#### 4. Co-Simulation Loop

```python
# Initialize
t = 0.0
dt = 0.1  # 10 Hz
T_ambient = 35.0  # °C
P_load = 65.0     # W

controller = ThermalController(setpoint=70.0)

# Simulation loop
while t < 3600.0:  # 1 hour
    # Get current airflow from controller
    # (In real system, this would be measured)
    
    # Set FMU inputs
    thermal_fmu.set_real(
        value_references=[0, 1, 2],  # [T_ambient, P_load, airflow]
        values=[T_ambient, P_load, airflow]
    )
    
    # Execute time step
    thermal_fmu.do_step(
        current_time=t,
        step_size=dt
    )
    
    # Get FMU output (predicted temperature)
    T_component = thermal_fmu.get_real(value_references=[3])[0]
    
    # Update controller
    airflow = controller.update(T_component, dt)
    
    # Log results
    print(f"t={t:6.1f}s  T={T_component:5.1f}°C  airflow={airflow:4.2f} m³/min")
    
    # Advance time
    t += dt

# Terminate
thermal_fmu.terminate()
```

### Results

The co-simulation demonstrates:
- **Closed-loop control** maintains temperature near 70°C setpoint
- **Fast execution** (~real-time on single core)
- **Accurate dynamics** matches high-fidelity FEM within 2-3°C
- **Seamless integration** FMU interfaces with any FMI-compliant tool

## Use Case: Flight Dynamics with Aerodynamic Surrogate

### Scenario

Flight dynamics simulation uses:
1. **Surrogate Model**: `aero_wing_cl_cd` predicts lift/drag coefficients
2. **Control Logic**: Autopilot computes elevator deflection
3. **Co-Simulation**: 6-DOF equations of motion + aerodynamics + control

### FMU Network

```
┌─────────────────────────┐
│  Flight Dynamics FMU    │
│  (6-DOF equations)      │
│                         │
│  Inputs:  CL, CD, δe    │
│  Outputs: α, M, V       │
└────────┬────────────────┘
         │
         │ α, M
         ↓
┌─────────────────────────┐
│  Aero Surrogate FMU     │
│  (aero_wing_cl_cd)      │
│                         │
│  Inputs:  α, M          │
│  Outputs: CL, CD        │
└────────┬────────────────┘
         │
         │ CL, CD
         ↓
┌─────────────────────────┐
│  Autopilot FMU          │
│  (PID controller)       │
│                         │
│  Inputs:  CL, altitude  │
│  Outputs: δe (elevator) │
└─────────────────────────┘
```

### Master Algorithm

The co-simulation orchestrator (master algorithm) coordinates FMU communication:

1. **Fixed-step Gauss-Seidel**:
   ```python
   for t in time_steps:
       # 1. Flight dynamics step
       flight_fmu.set_real([CL, CD, delta_e])
       flight_fmu.do_step(t, dt)
       alpha, Mach, V = flight_fmu.get_real([alpha_idx, Mach_idx, V_idx])
       
       # 2. Aero surrogate prediction
       aero_fmu.set_real([alpha, Mach])
       aero_fmu.do_step(t, dt)
       CL, CD = aero_fmu.get_real([CL_idx, CD_idx])
       
       # 3. Autopilot control
       autopilot_fmu.set_real([CL, altitude])
       autopilot_fmu.do_step(t, dt)
       delta_e = autopilot_fmu.get_real([delta_e_idx])
   ```

2. **Adaptive Step with Error Control**:
   - Monitor extrapolation distance
   - Reduce time step if surrogate uncertainty increases
   - Trigger high-fidelity evaluation if error exceeds tolerance

## Integration Patterns

### Pattern 1: Direct Replacement

Replace physics model with surrogate in existing simulation:

```
Before:  Sensor → Physics Model (slow) → Controller
After:   Sensor → Surrogate FMU (fast) → Controller
```

**Benefits**: Minimal code changes, immediate speedup

### Pattern 2: Hybrid Multi-Fidelity

Use surrogate for fast iterations, physics model for validation:

```
Optimization Loop:
├── Surrogate (1000 evaluations) → Candidate designs
└── Physics Model (10 evaluations) → Validate finalists
```

**Benefits**: Optimal trade-off between speed and accuracy

### Pattern 3: Hierarchical Decomposition

Different surrogates at different system levels:

```
System Level:       Surrogate (aircraft performance)
↓ Subsystem Level:  Surrogate (wing aerodynamics)
↓ Component Level:  Physics Model (airfoil CFD)
```

**Benefits**: Scalability to complex systems

## Best Practices

### 1. Interface Compatibility

Ensure FMU variable naming matches expectations:

```xml
<!-- modelDescription.xml -->
<ScalarVariable name="alpha" valueReference="1" causality="input" />
<ScalarVariable name="Mach" valueReference="2" causality="input" />
<ScalarVariable name="CL" valueReference="3" causality="output" />
<ScalarVariable name="CD" valueReference="4" causality="output" />
```

### 2. Time Step Selection

- **Surrogate inference time**: 5 ms
- **Controller dynamics**: 10 Hz (100 ms period)
- **Recommended time step**: 50-100 ms

Rule of thumb: `dt ≥ 10 × inference_time`

### 3. Uncertainty Propagation

Pass uncertainty from surrogate to controller:

```python
result = predict(inputs, return_std=True)
T_component = result['T_component']
T_uncertainty = result['uncertainty_95']

# Adjust control gains based on uncertainty
if T_uncertainty > 5.0:
    controller.increase_damping()  # More conservative
```

### 4. Domain Monitoring

Log out-of-domain queries for model retraining:

```python
if is_out_of_domain(inputs):
    log_ood_query(inputs, timestamp, context)
    trigger_alert("Surrogate OOD: consider retraining")
```

## Example: Full Co-Simulation Script

See [examples/thermal_management_cosim.py](examples/thermal_management_cosim.py) for complete working example.

## Tools and Libraries

### FMI Co-Simulation

- **FMPy**: Python FMU simulation
- **PyFMI**: Python FMI library (Modelon)
- **OpenModelica**: Open-source modeling environment
- **Dymola**: Commercial Modelica tool (Dassault)

### Co-Simulation Orchestration

- **IMAS**: Integrated Modeling and Simulation (ESA)
- **Open Simulation Platform (OSP)**: Maritime/offshore
- **Custom Master**: Python/C++ master algorithm

## Performance Considerations

### Surrogate Overhead

| Component | Time | Percentage |
|-----------|------|------------|
| FMI overhead | ~0.5 ms | ~10% |
| Surrogate inference | ~5 ms | ~90% |
| **Total** | **~5.5 ms** | **100%** |

### Optimization

1. **Batch predictions**: If evaluating N samples, use `predict_batch()`
2. **Caching**: Cache recent predictions for repeated queries
3. **Native C**: Use `export_c.py` for embedded systems

## Troubleshooting

### Issue: Surrogate diverges in closed-loop

**Cause**: Feedback loop drives inputs outside training domain

**Solution**:
- Add domain constraints to controller
- Use conservative control gains
- Monitor OOD rate

### Issue: Co-simulation is unstable

**Cause**: Algebraic loop or stiff coupling

**Solution**:
- Use smaller time step
- Add low-pass filter to surrogate output
- Use implicit coupling scheme

## References

- FMI Standard: https://fmi-standard.org/
- Co-Simulation Best Practices: https://github.com/modelica/fmi-guides
- Digital Twin Architecture: [../../01-ARCHITECTURE/REFERENCE_ARCHITECTURE.md](../../01-ARCHITECTURE/REFERENCE_ARCHITECTURE.md)

---

**Status**: Configuration-controlled per `00-PROGRAM/CONFIG_MGMT/`

**Contact**: Digital Twin Architecture Team
