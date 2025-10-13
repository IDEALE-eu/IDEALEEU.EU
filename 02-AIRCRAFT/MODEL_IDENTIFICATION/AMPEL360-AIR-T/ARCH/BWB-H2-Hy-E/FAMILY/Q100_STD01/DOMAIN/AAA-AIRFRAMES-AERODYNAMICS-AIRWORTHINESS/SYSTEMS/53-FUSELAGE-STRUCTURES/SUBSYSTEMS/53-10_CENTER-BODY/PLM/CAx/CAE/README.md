# CAE — Computer-Aided Engineering

## Purpose
Analysis models and structural validation for the center body fuselage structure, including finite element analysis (FEA), computational fluid dynamics (CFD), and multi-physics coupling.

## Structure

### FEA/
Finite Element Analysis workflows for structural analysis.
- **PRE/**: Pre-processing (geometry, materials, loads, boundary conditions, mesh, templates)
- **RUN/**: Analysis cases (linear, nonlinear, buckling, dynamic, fatigue, pressurization)
- **POST/**: Post-processing (results, plots, reports)

### CFD/
Computational Fluid Dynamics for aerodynamic and thermal analysis.
- **PRE/**: Pre-processing (geometry, mesh, boundary conditions, templates)
- **RUN/**: Analysis cases (external aero, internal flow, venting, heat transfer, cryogenic)
- **POST/**: Post-processing (results, plots, reports)

### COUPLING/
Multi-physics coupling analyses.
- **FSI/**: Fluid-Structure Interaction
- **THERMO-STRUCTURAL/**: Thermal-structural coupling
- **AEROELASTICITY/**: Aeroelastic analysis

### DATA/
Engineering databases.
- **LOADS_DB/**: Loads cases and load distributions
- **MATERIALS_DB/**: Material properties and allowables

### SCRIPTS/
Automation and post-processing scripts.
- **PRE/**: Pre-processing automation
- **POST/**: Post-processing and reporting

### QA/
Quality assurance and validation.
- **VERIFICATION/**: Verification cases and benchmarks
- **VALIDATION/**: Validation against test data

## Guidelines
- Document solver version and analysis assumptions
- Include material cards with A/B-basis references
- Link results to verification evidence and acceptance criteria
- Commit large binaries via Git LFS
- Provide README.md per analysis with inputs/outputs/solver/tool version
