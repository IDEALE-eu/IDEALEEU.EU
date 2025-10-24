# COUPLING — Multi-Physics Coupling

## Purpose

This directory contains configurations and examples for multi-physics coupling simulations including:
- CFD-FEA coupling (Fluid-Structure Interaction)
- Thermal-structural coupling
- Co-simulation frameworks
- FMU (Functional Mock-up Unit) wrappers

## Directory Structure

```
COUPLING/
├─ README.md                    # This file
├─ precice/                     # preCICE configurations and adapters
│  ├─ configs/                  # preCICE XML configurations
│  └─ adapters/                 # Custom adapter implementations
├─ fmu/                         # FMU wrappers and tests
│  ├─ models/                   # FMU model files
│  └─ tests/                    # FMU integration tests
└─ examples/                    # Example co-simulation scenarios
   ├─ fsi_wing/                 # Example: wing FSI
   └─ thermal_structural/       # Example: thermal-structural coupling
```

## preCICE Integration

preCICE is the primary coupling framework for partitioned multi-physics simulations.

### Configuration Files
- `precice-config.xml`: Main coupling configuration
- `precice-adapter-config.xml`: Adapter-specific settings

### Supported Couplings
- OpenFOAM ↔ Calculix
- OpenFOAM ↔ FEniCS
- Custom solver adapters

## FMU Co-Simulation

Functional Mock-up Units (FMUs) enable tool-independent co-simulation.

### FMU Development
1. Create model in source tool (Simulink, Modelica, etc.)
2. Export as FMU 2.0 for Co-Simulation
3. Validate FMU with PyFMI or FMPy
4. Document interface variables

### FMU Testing
```python
from fmpy import simulate_fmu

result = simulate_fmu('model.fmu', 
                      start_time=0.0,
                      stop_time=10.0,
                      output_interval=0.1)
```

## Example Scenarios

Each example should include:
- README with problem description
- All necessary configuration files
- Scripts to run the coupled simulation
- Baseline results for validation

## Running Coupled Simulations

### preCICE Example
```bash
cd examples/fsi_wing

# Terminal 1: Start fluid solver
cd fluid
./Allrun-parallel &

# Terminal 2: Start structure solver
cd structure
calculix -i model &

# Both solvers will couple through preCICE
```

### FMU Example
```bash
cd fmu/tests
python3 run_cosim.py --master master.fmu --slave slave.fmu
```

## Best Practices

1. **Synchronization**: Ensure consistent time stepping
2. **Data Mapping**: Document interpolation schemes
3. **Convergence**: Use appropriate coupling schemes (serial, parallel, implicit)
4. **Stability**: Check sub-cycling and relaxation parameters
5. **Validation**: Compare against monolithic solutions when possible

## Coupling Schemes

### Explicit (Serial)
- Fast, but may be unstable
- Suitable for loosely coupled problems

### Implicit (Parallel with iterations)
- Stable, but computationally expensive
- Required for strongly coupled problems

### Quasi-Newton
- Accelerates implicit coupling
- Reduces number of iterations

## Data Exchange

Document exchanged quantities:
- Forces and displacements (FSI)
- Heat flux and temperature (CHT)
- Custom field variables

## Troubleshooting

Common issues:
- **Mapping errors**: Check mesh matching and tolerance
- **Divergence**: Reduce time step or add relaxation
- **Communication**: Verify network/socket configuration

## References

- preCICE Documentation: https://precice.org/
- FMI Standard: https://fmi-standard.org/
- Best Practices: See DOCS/COUPLING_README.md

---

**Last Updated:** 2025-10-23
