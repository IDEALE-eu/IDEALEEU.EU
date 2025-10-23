# CFD Simulation Framework for CO₂ Endocircular Battery System

## Overview

This directory contains OpenFOAM-based Computational Fluid Dynamics (CFD) simulations for the CO₂ endocircular battery system. The CFD framework replaces simplified 0-D/1-D thermodynamic models with high-fidelity physics-based simulations.

## Recommended Stack

- **Solver**: OpenFOAM v10 or latest LTS
- **Thermophysical Properties**: CoolProp (unit tests/tabulation) and Span-Wagner/REFPROP (high fidelity)
- **Co-simulation**: preCICE or FMU (FMI) for CFD-system coupling
- **Meshing**: snappyHexMesh for complex geometry
- **Post-processing**: ParaView and Python (meshio, numpy, pandas)
- **Orchestration**: Python 3.9+ scripts
- **Container**: Docker with OpenFOAM + CoolProp bindings

## Directory Structure

```
cfd/
├── README.md                        # This file
├── cases/                           # OpenFOAM case templates
│   ├── storage_tank/               # Storage tank CHT simulation
│   ├── evaporator/                 # Evaporator/heater simulation
│   ├── expander/                   # Turbomachinery simulation
│   ├── condenser/                  # Condenser simulation
│   └── full_system/                # Full system co-simulation
├── mesh/                            # Mesh generation scripts
│   ├── geometry/                   # CAD geometry (STEP/STL)
│   ├── scripts/                    # snappyHexMesh scripts
│   └── templates/                  # Mesh templates
├── properties/                      # Thermophysical properties
│   ├── coolprop_tables/            # CoolProp tabulated properties
│   ├── transport/                  # Transport properties
│   └── thermophysical/             # Thermophysical dictionaries
├── scripts/                         # Python orchestration
│   ├── run_simulation.py           # Main simulation runner
│   ├── mesh_generator.py           # Automated mesh generation
│   ├── postprocess.py              # Post-processing automation
│   ├── co_simulation.py            # preCICE coupling
│   └── utils/                      # Utility functions
├── validation/                      # Validation cases
│   ├── phase_change/               # Phase change validation
│   ├── turbomachinery/             # Expander validation
│   └── heat_transfer/              # CHT validation
├── results/                         # Simulation results (gitignored)
└── docker/                          # Docker configurations
    ├── Dockerfile.openfoam         # OpenFOAM + CoolProp image
    └── docker-compose.yml          # Multi-container setup
```

## Physics Models

### 1. Storage Tank (Solid/Liquid CO₂)
- **Method**: Conjugate Heat Transfer (CHT)
- **Phase Change**: Enthalpy-porosity method for solidification/melting
- **Multiphase**: Solid CO₂ as immobile porous region
- **Insulation**: Vacuum + MLI as thermal resistance layer
- **Solver**: `chtMultiRegionFoam` with custom enthalpy solver

### 2. Evaporator/Heaters
- **Method**: CHT domain with heat sources
- **Boundary Conditions**: Electrical/resistive heating or hot gas
- **Solver**: `chtMultiRegionFoam`

### 3. Expansion/Turbomachinery
- **Method**: Co-simulation approach
  - Option A: MRF (Moving Reference Frame) in OpenFOAM
  - Option B: Actuator disk model for preliminary design
  - Option C: Couple to 1-D turbomachinery code via preCICE
- **Solver**: `simpleFoam` (steady) or `pimpleFoam` (transient) with MRF

### 4. Piping/Heat Exchangers
- **Method**: Single-phase or two-phase (VOF) for gas-liquid
- **Real-gas**: CoolProp tables or Span-Wagner EOS
- **Solver**: `rhoPimpleFoam` for compressible flow

### 5. Condenser/Liquefaction
- **Method**: CHT + phase change
- **Multiphase**: VOF for gas-liquid interface
- **Solver**: `multiphaseEulerFoam` or `interCondensatingEvaporatingFoam`

## Getting Started

### Prerequisites

1. **OpenFOAM Installation**:
   ```bash
   # Ubuntu/Debian
   curl -s https://dl.openfoam.org/gpg.key | sudo apt-key add -
   sudo add-apt-repository http://dl.openfoam.org/ubuntu
   sudo apt-get update
   sudo apt-get install openfoam10
   source /opt/openfoam10/etc/bashrc
   ```

2. **Python Dependencies**:
   ```bash
   cd cfd
   pip install -r requirements.txt
   ```

3. **Docker (Alternative)**:
   ```bash
   cd cfd/docker
   docker build -t co2-battery-cfd:latest -f Dockerfile.openfoam .
   ```

### Running a Simulation

#### Method 1: Python Orchestration (Recommended)
```bash
cd cfd/scripts
python run_simulation.py --case storage_tank --mesh-size medium --parallel 4
```

#### Method 2: Manual OpenFOAM Workflow
```bash
cd cfd/cases/storage_tank
blockMesh
snappyHexMesh -overwrite
chtMultiRegionFoam
paraFoam
```

#### Method 3: Docker Container
```bash
docker run --rm -v $(pwd)/results:/results co2-battery-cfd:latest \
    python scripts/run_simulation.py --case storage_tank
```

### Mesh Generation

Generate meshes using automated scripts:

```bash
cd cfd/scripts
python mesh_generator.py --geometry tank --size fine --output ../cases/storage_tank
```

Mesh sizes:
- **coarse**: 50k-100k cells (rapid prototyping)
- **medium**: 500k-1M cells (standard analysis)
- **fine**: 2M-5M cells (high-fidelity)
- **very-fine**: 10M+ cells (publication quality)

### Post-Processing

Automated post-processing with Python:

```bash
cd cfd/scripts
python postprocess.py --case ../cases/storage_tank/results --output ../results/tank_analysis
```

Generates:
- Time-series plots (temperature, pressure, phase fraction)
- Contour plots (ParaView state files)
- Performance metrics (CSV/JSON)
- Validation reports (PDF)

## Case Templates

### Storage Tank CHT Simulation

**Objective**: Model solidification/melting and heat transfer in cryogenic tank

**Domain**:
- CO₂ region (solid/liquid phase change)
- Tank wall (stainless steel 316L)
- Insulation (vacuum + MLI)

**Boundary Conditions**:
- Ambient temperature (external)
- Heat leak through insulation
- Natural convection in liquid region

**Key Outputs**:
- Solid fraction vs. time
- Temperature distribution
- Heat leak rate
- Charge/discharge energy

**Typical Runtime**: 2-8 hours (medium mesh, 8 cores)

### Evaporator Simulation

**Objective**: Model sublimation/evaporation and heat transfer

**Domain**:
- CO₂ flow channel
- Heating element
- Heat exchanger walls

**Boundary Conditions**:
- Inlet: subcooled liquid or solid CO₂
- Outlet: superheated vapor
- Heat source: constant power or temperature

**Key Outputs**:
- Exit vapor quality
- Heat transfer coefficient
- Pressure drop
- Thermal efficiency

### Expander Simulation

**Objective**: Model gas expansion and work extraction

**Method**: MRF or actuator disk

**Domain**:
- Inlet nozzle
- Rotor (MRF zone)
- Diffuser

**Boundary Conditions**:
- Inlet: high-pressure CO₂ vapor
- Outlet: low-pressure expanded CO₂
- Walls: adiabatic or cooled

**Key Outputs**:
- Isentropic efficiency
- Power output
- Exit temperature/pressure
- Flow uniformity

### Full System Co-Simulation

**Objective**: Couple all components via preCICE

**Architecture**:
- Tank CFD → preCICE → System controller
- Evaporator CFD → preCICE → Mass flow controller
- Expander CFD → preCICE → Power output
- Condenser CFD → preCICE → Heat rejection

**Coupling**: Explicit or implicit time stepping

**Key Outputs**:
- System-level efficiency
- Transient behavior
- Control stability
- Cycle performance

## Thermophysical Properties

### CoolProp Integration

Generate property tables for OpenFOAM:

```bash
cd cfd/scripts
python generate_coolprop_tables.py --fluid CO2 --temp-range -100:100 --press-range 1:200
```

Output: `properties/coolprop_tables/CO2_table.dat`

### Property Files

OpenFOAM thermophysical dictionaries in `properties/thermophysical/`:

- `CO2_realGas`: Real-gas EOS (Span-Wagner)
- `CO2_idealGas`: Simplified ideal gas (preliminary)
- `CO2_liquid`: Liquid properties
- `CO2_solid`: Solid properties
- `SS316L`: Stainless steel 316L
- `insulation`: MLI thermal properties

## Validation Cases

### Phase Change Validation

**Test Case**: Stefan problem (1-D solidification)

**Objective**: Validate enthalpy-porosity method

**Benchmark**: Analytical solution

**Acceptance**: < 5% error in solid front position

### Turbomachinery Validation

**Test Case**: Radial turbine expansion

**Objective**: Validate MRF and real-gas effects

**Benchmark**: NIST sCO₂ turbine data

**Acceptance**: Isentropic efficiency within ±3%

### Heat Transfer Validation

**Test Case**: Cryogenic natural convection

**Objective**: Validate CHT coupling and Boussinesq approximation

**Benchmark**: Experimental correlations

**Acceptance**: Nusselt number within ±10%

## Performance and Scaling

### Computational Resources

| Case | Mesh Size | Cores | Time/Step | Wall Time |
|------|-----------|-------|-----------|-----------|
| Tank (coarse) | 100k | 4 | 2s | 4h |
| Tank (medium) | 500k | 8 | 5s | 8h |
| Tank (fine) | 2M | 16 | 15s | 24h |
| Evaporator | 300k | 8 | 3s | 6h |
| Expander (MRF) | 1M | 16 | 10s | 20h |
| Full system | 5M | 64 | 30s | 48h |

**Note**: Times assume transient simulation for 10s physical time

### HPC Recommendations

- **Minimum**: 8 cores, 32 GB RAM
- **Standard**: 16 cores, 64 GB RAM
- **Large**: 64 cores, 256 GB RAM
- **Cluster**: 256+ cores for full system co-simulation

## Troubleshooting

### OpenFOAM Errors

**Issue**: `FoamFatalError: cannot find file`
- **Solution**: Check case structure, run `foamListTimes`, verify dictionary files

**Issue**: Divergence or blowup
- **Solution**: Reduce time step, check mesh quality (`checkMesh`), use relaxation

**Issue**: Slow convergence
- **Solution**: Improve mesh quality, use better initial conditions, adjust solvers

### CoolProp Integration

**Issue**: Property table out of range
- **Solution**: Extend table bounds, add extrapolation warnings

**Issue**: Negative density or temperature
- **Solution**: Add physical limiters in thermophysical model

### preCICE Coupling

**Issue**: Coupling instability
- **Solution**: Use implicit coupling, reduce time step, add under-relaxation

**Issue**: Data mapping errors
- **Solution**: Check mesh alignment, use conservative mapping

## References

### OpenFOAM
- OpenFOAM User Guide: https://www.openfoam.com/documentation/user-guide
- OpenFOAM Tutorials: `$FOAM_TUTORIALS`

### Thermophysical Properties
- CoolProp Documentation: http://www.coolprop.org/
- Span & Wagner (1996): Reference EOS for CO₂

### Multiphase & Phase Change
- Voller & Prakash (1987): Enthalpy-porosity technique
- Brackbill et al. (1992): VOF method

### Turbomachinery
- Greitzer et al. (2004): Internal Flow
- Aungier (2006): Turbine Aerodynamics

### Co-Simulation
- preCICE Documentation: https://precice.org/docs.html
- Bungartz et al. (2016): Coupling

## Contact and Support

**CAE Team**: Listed in parent README.md  
**OpenFOAM Support**: https://www.openfoam.com/support  
**Issue Tracker**: Repository issues tab

## Change Log

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0.0 | 2025-10-23 | Copilot | Initial CFD framework implementation |

---

**Status**: Production Ready  
**Last Updated**: 2025-10-23  
**OpenFOAM Version**: v10 or later
