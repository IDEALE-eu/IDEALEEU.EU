# CO_SIMULATION ORCHESTRATION

**📍 [IDEALE-EU](../../../) > [02-AIRCRAFT](../../) > [DIGITAL_TWIN_MODEL](../) > 02-MODELS/CO_SIMULATION > ORCHESTRATION**

Master algorithm, step sizes, and error control for co-simulation.

## Purpose

Orchestrate co-simulation of multiple FMUs (Functional Mock-up Units) using FMI 3.0 standard.

## Co-Simulation Master Algorithm

### Fixed-Step Integration
- **Step Size**: 0.01s - 1.0s (dependent on system dynamics)
- **Solver**: Forward Euler, Heun (2nd order), RK4 (4th order)
- **Use Case**: Real-time models, deterministic execution time

### Adaptive-Step Integration
- **Solver**: CVODE, DOPRI5 (adaptive Runge-Kutta)
- **Error Control**: Local truncation error <1e-6
- **Use Case**: Batch analysis, high-fidelity simulations

## FMU Communication

### Gauss-Seidel (Sequential)
- Execute FMUs in sequence: FMU1 → FMU2 → ... → FMUn
- **Advantage**: Simple, deterministic
- **Disadvantage**: May introduce numerical damping

### Jacobi (Parallel)
- Execute all FMUs in parallel at each time step
- **Advantage**: True parallelism, faster for independent subsystems
- **Disadvantage**: May require smaller time steps for stability

## Error Control

### Local Error
- **Truncation Error**: Estimated from Richardson extrapolation
- **Coupling Error**: Difference between Gauss-Seidel and Jacobi (if computed)

### Global Error
- **Drift Detection**: Compare co-simulation result with monolithic model (if available)
- **Acceptance Criterion**: Global error <1% over mission duration (e.g., 3-hour flight)

## Step Size Selection

| System | Fastest Dynamic | Recommended Δt | Solver |
|--------|----------------|----------------|--------|
| **Aerodynamics** | Flutter (~10 Hz) | 0.01s | Fixed |
| **Structures** | Vibration (~50 Hz) | 0.005s | Fixed |
| **Thermal** | Thermal time constant (~100s) | 1.0s | Adaptive |
| **Propulsion** | Engine response (~1s) | 0.1s | Fixed |
| **H₂ Energy** | Tank dynamics (~10s) | 1.0s | Adaptive |
| **Control Logic** | Control loop (10-50 Hz) | 0.02s | Fixed |

## Initialization

1. **FMU Loading**: Load all FMUs, verify FMI version (3.0)
2. **Parameter Setting**: Set initial conditions, parameters from `../../04-VERSIONING_CONFIG/`
3. **Variable Mapping**: Map outputs of FMUi to inputs of FMUj (see FMU_FMI/CONNECTION_MATRIX.csv)
4. **Initialization Mode**: Enter initialization mode, solve algebraic loops
5. **Simulation Start**: Exit initialization, begin time stepping

## Termination

### Normal Termination
- Reach end time: t_end (e.g., 3 hours for cruise mission)
- All FMUs report success

### Abnormal Termination
- FMU error: Numerical instability, constraint violation
- Error budget exceeded: Global error >1%
- User interrupt: Manual stop from operator

## Monitoring

- **Performance**: Step execution time, FMU load time
- **Accuracy**: Local/global error estimates
- **Stability**: Eigenvalues of Jacobian (if computed)

## Related Documents

- **FMU_FMI/README.md** - FMU specifications and connections
- **../../03-INTERFACES_APIS/** - FMU I/O mapping
- **../../06-VALIDATION_VERIFICATION/** - Co-simulation validation test cases

---

**Status**: Configuration-controlled per `00-PROGRAM/CONFIG_MGMT/`
