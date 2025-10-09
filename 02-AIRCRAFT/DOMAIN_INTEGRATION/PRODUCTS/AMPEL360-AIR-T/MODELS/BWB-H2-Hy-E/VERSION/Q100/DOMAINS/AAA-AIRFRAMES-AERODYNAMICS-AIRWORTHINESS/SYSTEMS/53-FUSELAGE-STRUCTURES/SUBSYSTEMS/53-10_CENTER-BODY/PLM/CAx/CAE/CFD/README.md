# CFD — Computational Fluid Dynamics

## Purpose
Aerodynamic and thermal analysis of the center body fuselage using computational fluid dynamics.

## Structure

### PRE/ — Pre-processing
- **GEOMETRY/**: Surface geometry and fluid domain
- **MESH/**: Volume mesh files and mesh generation parameters
- **BCS/**: Boundary conditions (inlets, outlets, walls, symmetry)
- **TEMPLATES/**: Solver setup templates and configuration files

### RUN/ — Analysis Execution
- **EXTERNAL_AERO/**: External aerodynamics and pressure distributions
- **INTERNAL_FLOW/**: Internal flow patterns (cabin, equipment bays)
- **VENTING/**: Venting and pressure relief systems
- **HEAT_TRANSFER/**: Thermal analysis and heat transfer
- **CRYO/**: Cryogenic cooling and thermal protection

### POST/ — Post-processing
- **RESULTS/**: Raw CFD solution files
- **PLOTS/**: Flow visualizations, contours, streamlines
- **REPORTS/**: CFD analysis reports and summaries

## Supported Solvers
- ANSYS Fluent
- Star-CCM+
- OpenFOAM
- CFX

## Guidelines
- Document turbulence models and solver settings
- Include mesh independence studies
- Report y+ values for wall-bounded flows
- Reference flight conditions and Reynolds numbers
- Archive solver versions with solution files
