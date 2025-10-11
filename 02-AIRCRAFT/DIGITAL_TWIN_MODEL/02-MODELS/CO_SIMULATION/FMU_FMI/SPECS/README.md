# SPECS

**📍 [IDEALE-EU](../../../../../) > [02-AIRCRAFT](../../../../) > [DIGITAL_TWIN_MODEL](../../../) > 02-MODELS/CO_SIMULATION/FMU_FMI > SPECS**

FMI 2.0/3.0 specifications, co-simulation parameters, tolerances, and step sizes.

## Purpose

This directory contains configuration specifications for the FMI (Functional Mock-up Interface) co-simulation environment. It defines:
- FMI version selection (2.0 vs 3.0)
- Co-simulation vs model exchange mode
- Time integration parameters and step sizes
- Numerical tolerances
- Event handling configuration
- Error handling strategies

## Files

### fmi_config.yaml
**Main FMI configuration specification**
- FMI version: 3.0 (with 2.0 fallback)
- Co-simulation type selection
- Master algorithm step size: 10 ms (100 Hz) default
- Individual FMU step sizes optimized for each subsystem
- Solver configuration (fixed-step, adaptive)
- Tolerances (relative: 1e-6, absolute: 1e-8)
- Event handling for discrete events (mode changes, faults)
- Continuous output interpolation
- Logging and debugging configuration

### Key Parameters

#### Time Integration
- **Master step**: 10 ms (100 Hz) - suitable for flight control dynamics
- **Control_FMU**: 20 ms (50 Hz) - control law update rate
- **Aero_FMU**: 10 ms (100 Hz) - aerodynamic updates
- **Struct_FMU**: 10 ms (100 Hz) - structural dynamics
- **Propulsion_FMU**: 100 ms (10 Hz) - slower propulsion dynamics
- **H2_FMU**: 1 s (1 Hz) - thermal/fuel system
- **Thermal_FMU**: 1 s (1 Hz) - thermal management

#### Solver Options
- **Fixed-step**: Forward Euler, Heun, RK4
- **Adaptive-step**: CVODE, DOPRI5 with error control
- **Communication**: Jacobi (parallel) or Gauss-Seidel (sequential)
- **Extrapolation**: Linear, constant, or quadratic

#### Tolerances

##### Numerical
- Relative tolerance: 1e-6
- Absolute tolerance: 1e-8
- Zero crossing: 1e-10

##### Signal-Specific
- Control surface position: ±0.1 deg
- Control surface rate: ±1.0 deg/s
- Lift coefficient: ±0.01
- Drag coefficient: ±0.001
- Angle of attack: ±0.5 deg
- Altitude: ±50 ft

## FMI 3.0 Features

### Enhanced Capabilities
1. **Event Handling**: Support for discrete events (mode changes, gear extension, actuator faults)
2. **Clocks**: Periodic and aperiodic clocks for hybrid co-simulation
3. **Continuous Outputs**: Smooth interpolation between time steps
4. **Terminals**: Enhanced interface definitions
5. **Improved Initialization**: Dedicated initialization mode

### Events Configured
- **mode_change**: FCC operating mode transitions
- **actuator_fault**: Actuator failure detection
- **gear_extension**: Landing gear state changes
- **flap_position_change**: Flap configuration changes

## Co-Simulation Strategy

### Communication Scheme
**Jacobi (Parallel)**: All FMUs evaluate simultaneously using inputs from previous time step
- Advantage: Better performance, natural parallelization
- Disadvantage: May require smaller step sizes for stability

Alternative: **Gauss-Seidel (Sequential)**: FMUs evaluated in order, using latest available outputs
- Advantage: Better numerical stability
- Disadvantage: No parallelization

### Algebraic Loop Handling
- Detection enabled
- Fixed-point iteration solver
- Max iterations: 10
- Convergence tolerance: 1e-6

## Error Handling

### Error Budget
- Maximum global error: 1.0%
- Maximum local error: 0.1%

### Actions on Error
- FMU error: Terminate simulation (log detailed error)
- Retry: Up to 3 attempts with exponential backoff
- Fallback: Option to continue with reduced fidelity

## Validation Requirements

### Pre-Simulation Checks
- Verify FMU versions match configuration
- Validate all signal connections
- Check for algebraic loops
- Verify causality (no circular dependencies)

### Runtime Checks
- Range checking (signal values within bounds)
- Rate-of-change checking (physical plausibility)
- Consistency checking (redundant signal agreement)

### Post-Simulation
- Generate simulation report
- Compare with reference data (if available)
- Log performance metrics

## Tool Compatibility

### Supported Tools
- **FMPy**: Python-based FMU simulation and validation
- **Simulink**: MATLAB/Simulink FMU import
- **OpenModelica**: Open-source Modelica FMU export
- **Dymola**: Commercial Modelica environment
- **CATIA Systems**: Systems engineering tool

### Adapters Available
See `../ADAPTERS/` directory for tool-specific wrappers and integration code.

## Performance Optimization

### Parallelization
- Parallel FMU evaluation: Enabled (4 threads)
- Suitable for Jacobi scheme with independent FMUs

### Caching
- Output caching: Enabled (1 GB max)
- Reduces redundant calculations

### Memory
- Preallocate buffers: 256 MB
- Reduces dynamic allocation overhead

## Logging Configuration

### Log Levels
- **Debug**: Detailed step-by-step execution
- **Info**: Major events (initialization, termination)
- **Warning**: Non-critical issues (tolerance violations)
- **Error**: Critical failures
- **Critical**: Fatal errors requiring termination

### Categories
- Initialization: Always logged
- Time stepping: Optional (debugging only)
- Event handling: Always logged
- Variable exchange: Optional (debugging only)
- Error conditions: Always logged

## Related Documents

- [fmi_config.yaml](fmi_config.yaml) - Complete FMI configuration specification
- [../INTERFACES/signals.yaml](../INTERFACES/signals.yaml) - Signal interface definitions
- [../ORCHESTRATION/](../ORCHESTRATION/) - Master algorithm implementation
- [../TESTS/compliance/](../TESTS/compliance/) - FMU compliance test results

## References

### Standards
- **FMI 3.0 Specification**: https://fmi-standard.org/docs/3.0/
- **FMI 2.0 Specification**: https://fmi-standard.org/docs/2.0.4/

### Tools
- **FMI Compliance Checker**: https://github.com/modelica-tools/FMUComplianceChecker
- **FMPy**: https://github.com/CATIA-Systems/FMPy

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2025-10-11 | Digital Twin Team | Initial FMI configuration specifications |

---

**Status**: Configuration-controlled per `00-PROGRAM/CONFIG_MGMT/`
