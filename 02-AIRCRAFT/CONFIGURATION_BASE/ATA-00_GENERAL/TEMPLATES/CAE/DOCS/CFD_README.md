# CFD Best Practices and Guidelines

## Overview

This document provides detailed guidance for CFD simulations including solver setup, numerical schemes, turbulence modeling, and best practices.

## Solver Selection

### OpenFOAM
**Strengths**:
- Open source, customizable
- Wide range of solvers
- Active community
- Good parallel scaling

**Best for**:
- Complex geometries
- Custom physics
- Research applications
- Linux environments

**Limitations**:
- Steeper learning curve
- Less polished GUI
- Community support only

### ANSYS Fluent
**Strengths**:
- Mature, robust
- Excellent documentation
- Commercial support
- User-friendly interface

**Best for**:
- Production simulations
- Standard applications
- Quick turnaround
- Windows/Linux

**Limitations**:
- License costs
- Limited customization
- Black box algorithms

## Mesh Generation

### Quality Metrics

| Metric | Good | Acceptable | Poor |
|--------|------|------------|------|
| Skewness | < 0.25 | 0.25-0.85 | > 0.85 |
| Aspect ratio | < 10 | 10-100 | > 100 |
| Orthogonality | > 0.7 | 0.5-0.7 | < 0.5 |
| Growth rate | < 1.1 | 1.1-1.3 | > 1.3 |

### Boundary Layer Meshing

For wall-resolved simulations (y+ < 1):
- First cell height: y+ ≈ 1
- Growth rate: ≤ 1.2
- Minimum 15-20 layers in boundary layer

For wall-function simulations (30 < y+ < 300):
- First cell height: y+ ≈ 30-100
- Growth rate: ≤ 1.3
- At least 3-5 layers in boundary layer

### Mesh Independence

1. Start with coarse mesh
2. Refine by factor of ~1.5 in each direction
3. Compare key metrics
4. Continue until change < 2%
5. Use Richardson extrapolation if possible

## Turbulence Modeling

### Model Selection Guide

| Flow Type | Recommended Model | Alternative |
|-----------|------------------|-------------|
| External aero | k-ω SST | Spalart-Allmaras |
| Internal flows | k-ε realizable | k-ω SST |
| Separated flows | k-ω SST | LES (if resources permit) |
| Natural convection | k-ε with buoyancy | RSM |
| Swirling flows | RSM | k-ω SST |

### RANS Models

**k-ε Standard**
- Fast, robust
- Good for fully turbulent flows
- Poor for adverse pressure gradients
- Not recommended for separated flows

**k-ε Realizable**
- Better than standard k-ε
- Good for jets, mixing layers
- Better separation prediction
- Use for most internal flows

**k-ω SST**
- Best all-around model
- Excellent near-wall treatment
- Good for separated flows
- Recommended for external aero

**Spalart-Allmaras**
- One equation, fast
- Good for external aero
- Not for complex flows
- Good for attached boundary layers

**Reynolds Stress Model (RSM)**
- Most physics, most expensive
- For complex turbulence
- Swirl, rotation, strong streamline curvature
- Requires fine mesh

### LES/DES

Use when:
- Unsteady flow features critical
- Computational resources available
- High-quality mesh achievable
- Time-accurate solution needed

Requirements:
- Very fine mesh (LES: y+ < 1, Δx+ ≈ 50-100)
- Long simulation time (> 10 flow-through times)
- Small time step (CFL < 1)
- Substantial computational cost

## Numerical Schemes

### Discretization Schemes

**Gradient Schemes**:
- Gauss linear: 2nd order, most common
- Gauss leastSquares: For non-orthogonal meshes
- cellLimited Gauss linear 1.0: For stability

**Divergence Schemes** (convection):
- Gauss upwind: 1st order, stable, diffusive
- Gauss linearUpwind: 2nd order, good accuracy
- Gauss LUST: For LES
- Avoid bounded schemes in production

**Laplacian Schemes** (diffusion):
- Gauss linear corrected: Standard for orthogonal
- Gauss linear limited 0.5: For non-orthogonal

**Interpolation**:
- linear: 2nd order, standard
- upwind: 1st order, use only if unstable

### Time Discretization

**Steady-state**:
- steadyState: Pseudo time-stepping
- localEuler: Local time stepping for convergence

**Transient**:
- Euler: 1st order, implicit, stable
- backward: 2nd order, implicit, recommended
- CrankNicolson 0.9: 2nd order, less diffusive

### CFL Number

Recommended values:
- Steady SIMPLE: No CFL limit
- Transient PIMPLE: CFL < 5
- Transient PISO: CFL < 1
- LES: CFL < 1 (often < 0.5)

## Solution Procedures

### SIMPLE Algorithm (Steady)

```
simpleFoam controls:
- nNonOrthogonalCorrectors 1-3
- Pressure under-relaxation 0.3
- Velocity under-relaxation 0.7
- Other under-relaxation 0.5-0.7
```

### PIMPLE Algorithm (Transient)

```
pimpleFoam controls:
- nOuterCorrectors 2-5
- nCorrectors 2-3
- nNonOrthogonalCorrectors 1-2
```

## Boundary Conditions

### Inlet Conditions

**Velocity Inlet**:
```
U: fixedValue
p: zeroGradient
k: turbulentIntensityKineticEnergyInlet (I = 1-5%)
epsilon: turbulentMixingLengthDissipationRateInlet (l = 0.07*L)
```

**Mass Flow Inlet**:
```
U: flowRateInletVelocity
p: zeroGradient
```

### Outlet Conditions

**Pressure Outlet**:
```
U: zeroGradient (or inletOutlet)
p: fixedValue
k, epsilon: zeroGradient
```

### Wall Conditions

**No-slip Wall**:
```
U: noSlip (or fixedValue (0 0 0))
p: zeroGradient
k: kqRWallFunction (or fixedValue 1e-10 for y+ < 1)
epsilon: epsilonWallFunction
```

**Slip Wall**:
```
U: slip
p: zeroGradient
```

## Convergence Criteria

### Residuals

Target residuals:
- Continuity: < 1e-4
- Momentum: < 1e-4
- Energy: < 1e-6
- Turbulence: < 1e-4

### Monitor Points

Place monitors at:
- Inlet/outlet
- Points of interest
- Locations with experimental data

Convergence when:
- Residuals plateau
- Monitor values change < 1% over 100 iterations
- Mass balance error < 0.1%

## Post-Processing

### Standard Outputs

Always extract:
- Pressure coefficient (Cp)
- Skin friction coefficient (Cf)
- Heat transfer coefficient (h or Nu)
- Total forces and moments
- Flow rates and mass balance

### Visualization

Best practices:
- Use consistent color scales
- Include scale bars and legends
- Show mesh in critical regions
- Provide multiple views
- Highlight key features

## Troubleshooting

### Divergence

Try:
- Reduce time step
- Increase under-relaxation
- Use more robust schemes (1st order temporarily)
- Check boundary conditions
- Improve mesh quality

### Slow Convergence

Try:
- Increase under-relaxation (carefully)
- Better initial condition
- Mesh refinement in active regions
- Different turbulence model

### Non-physical Results

Check:
- Boundary conditions
- Material properties
- Units consistency
- Mesh quality
- Reference frames

## Quality Checklist

Before considering case complete:
- [ ] Mesh quality acceptable
- [ ] Residuals converged
- [ ] Monitor points stable
- [ ] Mass balance < 0.1%
- [ ] Results physically reasonable
- [ ] Boundary layer resolved correctly
- [ ] Mesh independence demonstrated
- [ ] Documentation complete

## References

- OpenFOAM User Guide
- ANSYS Fluent Theory Guide
- Versteeg & Malalasekera: CFD
- Pope: Turbulent Flows
- NASA CFD Resources

---

**Version:** 1.0  
**Last Updated:** 2025-10-23
