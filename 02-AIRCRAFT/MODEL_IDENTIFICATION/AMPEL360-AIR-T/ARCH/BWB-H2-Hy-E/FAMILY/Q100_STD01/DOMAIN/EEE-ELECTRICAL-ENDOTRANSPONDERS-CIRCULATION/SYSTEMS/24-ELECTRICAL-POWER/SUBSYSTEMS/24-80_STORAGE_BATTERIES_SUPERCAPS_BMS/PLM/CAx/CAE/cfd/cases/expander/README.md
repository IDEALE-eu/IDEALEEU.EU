# Expander CFD Case

## Overview

Simulation of CO₂ expansion through radial turbine with real-gas effects.

## Physics

- **Solver**: pimpleFoam (transient) or simpleFoam (steady)
- **Turbulence**: k-omega SST
- **Rotating**: MRF (Moving Reference Frame) for rotor region
- **Real-gas**: CoolProp properties for sCO₂ expansion

## Geometry

- Inlet nozzle: Converging section
- Rotor: Radial turbine blades (12 blades)
- Diffuser: Expanding section for pressure recovery
- Tip clearance: 0.5 mm

## Boundary Conditions

### Inlet
- **Total Pressure**: 80-150 bar (sCO₂ Brayton)
- **Total Temperature**: 150-400°C
- **Turbulence**: 5% intensity, length scale = 0.01 m

### Outlet
- **Static Pressure**: 30-50 bar
- **Backflow**: Zero gradient temperature

### Walls
- **Stationary**: No-slip, adiabatic or fixed T
- **Rotating**: No-slip, rotating with rotor speed

### MRF Zone
- **Rotation Speed**: 10,000-30,000 RPM
- **Axis**: Z-axis

## Mesh

- **Coarse**: 200k cells
- **Medium**: 1M cells
- **Fine**: 3M cells
- **y+ target**: < 1 (resolve boundary layer)

## Expected Runtime

- Steady-state: 4-8 hours (16 cores)
- Transient: 20-40 hours (16-32 cores)

## Key Outputs

- Isentropic efficiency
- Power output [kW]
- Mass flow rate [kg/s]
- Exit temperature and pressure
- Velocity and pressure contours
- Blade loading distribution

## Running the Case

```bash
# Steady-state MRF
python run_simulation.py --case expander --mesh-size medium --parallel 16

# Transient
python run_simulation.py --case expander --mesh-size fine --parallel 32 --transient
```

## Post-Processing

```bash
# Calculate efficiency
postProcess -func 'turbinePerformance'

# Extract blade forces
postProcess -func 'forces(rotor)'

# Visualize
paraFoam
```

## Validation

- Compare against NIST sCO₂ turbine data
- Target isentropic efficiency: 75-85%
- Acceptance: within ±3% of experimental data

## Notes

- Use real-gas properties (CoolProp) for accurate sCO₂ expansion
- Monitor convergence of mass flow rate and pressure ratio
- Adjust under-relaxation factors for stability (0.3-0.7 recommended)
- For transient: use adaptive time stepping with max CFL = 1.0
