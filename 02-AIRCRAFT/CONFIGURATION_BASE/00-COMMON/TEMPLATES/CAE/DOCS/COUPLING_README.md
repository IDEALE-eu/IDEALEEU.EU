# Multi-Physics Coupling Guidelines

## Overview

This document provides guidance for setting up and running coupled multi-physics simulations using preCICE and other coupling frameworks.

## Coupling Approaches

### Monolithic
**Definition**: Solve all physics in one code  
**Pros**: Strong coupling, stable  
**Cons**: Limited solver choice, less flexible  

### Partitioned
**Definition**: Separate solvers coupled through interface  
**Pros**: Use best solver for each physics, modular  
**Cons**: Stability challenges, communication overhead  

## preCICE Framework

preCICE is the recommended tool for partitioned multi-physics coupling.

### Supported Couplings

- **FSI**: Fluid-Structure Interaction
- **CHT**: Conjugate Heat Transfer  
- **CFD-CFD**: Domain decomposition
- **Custom**: Any field exchange

### Architecture

```
Solver 1 (e.g., OpenFOAM)
    ↓ (adapter)
  preCICE
    ↑ (adapter)
Solver 2 (e.g., Calculix)
```

## Configuration

### preCICE Config (XML)

Key elements:
```xml
<precice-configuration>
  <solver-interface dimensions="3">
    
    <!-- Participants -->
    <participant name="Fluid">
      <use-mesh name="FluidMesh" provide="yes"/>
      <write-data name="Force" mesh="FluidMesh"/>
      <read-data name="Displacement" mesh="FluidMesh"/>
    </participant>
    
    <participant name="Solid">
      <use-mesh name="SolidMesh" provide="yes"/>
      <write-data name="Displacement" mesh="SolidMesh"/>
      <read-data name="Force" mesh="SolidMesh"/>
    </participant>
    
    <!-- Coupling scheme -->
    <coupling-scheme:parallel-implicit>
      <participants first="Fluid" second="Solid"/>
      <max-time-windows value="1000"/>
      <time-window-size value="0.01"/>
      <max-iterations value="50"/>
      <relative-convergence-measure data="Displacement" 
                                    mesh="SolidMesh" 
                                    limit="1e-4"/>
    </coupling-scheme:parallel-implicit>
    
    <!-- Data mapping -->
    <mapping:nearest-projection 
             constraint="consistent" 
             from="FluidMesh" 
             to="SolidMesh" 
             direction="write"/>
             
  </solver-interface>
</precice-configuration>
```

### Coupling Schemes

**Serial Explicit (Weak)**:
- Each solver runs once per time step
- Fast but potentially unstable
- Use for loosely coupled problems

**Parallel Implicit (Strong)**:
- Iterate until convergence each time step
- Stable but expensive
- Use for strongly coupled problems
- Add acceleration (see below)

**Multi-rate**:
- Different time step sizes
- Sub-cycling in fast solver

## FSI - Fluid-Structure Interaction

### Problem Setup

**Fluid side**:
- Moving mesh (ALE)
- Interface as moving wall
- Apply structural displacement

**Structure side**:
- Interface nodes
- Apply fluid forces
- Compute displacement

### Critical Parameters

- **Added mass**: ρfluid / ρsolid
  - High ratio → stability issues
  - Use strong coupling if > 0.1

- **Time step**: Δt ≤ min(Δtfluid, Δtsolid)

- **Convergence**: Monitor displacement/force

### Common Applications

- Wing flutter
- Valve dynamics
- Pipe vibration
- Hemodynamics

## CHT - Conjugate Heat Transfer

### Problem Setup

**Fluid side**:
- Interface as wall
- Apply wall temperature
- Compute heat flux

**Solid side**:
- Interface as boundary
- Apply heat flux
- Compute temperature

### Interface Conditions

Continuity:
- T_fluid = T_solid (at interface)
- q_fluid = -q_solid (heat flux balance)

### Critical Parameters

- **Thermal time scales**: τ = ρcpL²/k
- **Biot number**: Bi = hL/k
- **Time step**: Based on slowest process

### Applications

- Heat exchangers
- Electronic cooling
- Turbine blade cooling
- Insulation systems

## Stability and Acceleration

### Under-relaxation

Simple but effective:
```
x^{n+1} = ω x^{n+1}_computed + (1-ω) x^n
```
- ω = 0.1-0.5 for stability
- Slows convergence

### Aitken Relaxation

Adaptive under-relaxation:
- Automatically adjusts ω
- Better than fixed relaxation
- Use as default

### Quasi-Newton (IQN-ILS)

Most efficient:
- Accelerates based on history
- Requires more memory
- Recommended for production

Configuration:
```xml
<acceleration:IQN-ILS>
  <initial-relaxation value="0.5"/>
  <max-used-iterations value="50"/>
  <time-windows-reused value="10"/>
</acceleration:IQN-ILS>
```

## Data Mapping

### Nearest Projection

Fastest, least accurate:
- Projects to nearest point
- Use for similar meshes

### Nearest Neighbor

Simple:
- Uses closest element
- Conservative option exists

### Radial Basis Functions (RBF)

Most accurate:
- Smooth interpolation
- Handles non-matching meshes
- More expensive
- Use for production

Types:
- Thin-plate-splines: Good general purpose
- Gaussian: Tunable support
- Compact: Sparse matrices

## Convergence Criteria

### Relative Measure
```
||x^{n+1} - x^n|| / ||x^{n+1}|| < ε
```
Typical: ε = 1e-4

### Absolute Measure
```
||x^{n+1} - x^n|| < ε
```
Use when relative doesn't work

### Energy-based
For FSI:
```
|E^{n+1} - E^n| / E^{n+1} < ε
```

## Time Stepping

### Synchronization

All solvers must:
- Use same time window
- Agree on time step
- Synchronize at checkpoints

### Adaptive Time Stepping

preCICE doesn't handle directly:
- Use fixed time step
- Or implement in solvers
- Communicate through preCICE

## Parallel Execution

### Domain Decomposition

Each solver can run in parallel:
```bash
# Terminal 1: Fluid (8 cores)
mpirun -np 8 pimpleFoam -parallel

# Terminal 2: Solid (4 cores)
mpirun -np 4 calculix
```

### Communication

preCICE handles:
- MPI within solvers
- Socket/MPI between solvers
- Automatic load balancing

## Debugging

### Check Files

preCICE generates:
- `precice-Participant-events.json`: Timing
- `precice-Participant-convergence.txt`: Convergence history
- `precice-Participant-iterations.txt`: Iteration counts

### Visualization

Export coupling data:
```xml
<export:vtk directory="precice-output" every-n-time-windows="1"/>
```

### Common Issues

**No convergence**:
- Reduce time step
- Increase max iterations
- Try stronger acceleration
- Check boundary conditions

**Instability**:
- Use implicit coupling
- Reduce under-relaxation
- Check added mass effect

**Slow coupling**:
- Increase acceleration
- Reduce mapping tolerance
- Optimize mesh at interface

## Performance Optimization

### Mesh Interface

Keep small:
- Only couple needed surfaces
- Refine only where necessary
- Coarsen away from interface

### Mapping

- Use compact RBF for large cases
- Adjust support radius
- Precompute mappings when possible

### Checkpointing

Enable for robustness:
- Implicit schemes need checkpointing
- Coordinate with solver checkpoints

## Validation

### Sanity Checks

- [ ] Energy conservation (if applicable)
- [ ] Mass conservation
- [ ] Force/flux balance at interface
- [ ] Reasonable convergence rates

### Comparison

- Monolithic solution (if available)
- Analytical solution (simple cases)
- Experimental data
- Literature benchmarks

## Best Practices

1. **Start simple**: Test each solver separately first
2. **Weak → Strong**: Try explicit before implicit
3. **Document**: Record all coupling parameters
4. **Monitor**: Watch convergence and timing
5. **Validate**: Check conservation properties
6. **Version control**: Track preCICE configs with solvers

## Example Cases

### FSI: Elastic Flap
- Simple 2D case
- Good for testing setup
- Available in preCICE tutorials

### CHT: Heat Exchanger
- Periodic boundary conditions
- Turbulent flow
- Temperature-dependent properties

### FSI: Turbine Blade
- Complex geometry
- High-speed flow
- Thermal loads

## References

- preCICE Documentation: https://precice.org/docs.html
- preCICE Tutorials: https://precice.org/tutorials.html
- Coupling FSI paper: Bungartz et al., 2016
- CHT best practices: Errera & Duchaine, 2016

---

**Version:** 1.0  
**Last Updated:** 2025-10-23
