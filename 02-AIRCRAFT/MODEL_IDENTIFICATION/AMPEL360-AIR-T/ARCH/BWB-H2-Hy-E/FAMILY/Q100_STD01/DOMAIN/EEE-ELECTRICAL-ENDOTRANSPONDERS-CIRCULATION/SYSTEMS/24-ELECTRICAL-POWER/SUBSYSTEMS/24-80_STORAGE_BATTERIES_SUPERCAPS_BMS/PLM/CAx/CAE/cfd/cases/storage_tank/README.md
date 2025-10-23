# Storage Tank CFD Case

## Overview

CHT simulation of solid/liquid CO₂ storage tank with phase change.

## Physics

- **Solver**: chtMultiRegionFoam with enthalpy-porosity phase change
- **Regions**:
  - CO2: Phase-changing fluid (solid/liquid)
  - tank: Stainless steel 316L walls
  - insulation: Vacuum + MLI layer
- **Phase Change**: Enthalpy-porosity method for solidification/melting
- **Natural Convection**: Boussinesq approximation in liquid region

## Geometry

- Tank volume: 100 L (400 mm diameter × 800 mm height)
- Wall thickness: 5 mm
- Insulation thickness: 50 mm (equivalent vacuum + MLI)

## Boundary Conditions

### CO2 Region
- **Initial**: T = -60°C (liquid), P = 20 bar
- **Top**: Symmetry (closed tank)
- **Bottom**: No-slip wall, coupled to tank

### Tank Walls
- **Inner**: Coupled to CO2
- **Outer**: Coupled to insulation

### Insulation
- **Inner**: Coupled to tank
- **Outer**: Fixed temperature (ambient = 25°C) or convection

## Mesh

- **Coarse**: 50k cells (prototype)
- **Medium**: 200k cells (standard)
- **Fine**: 800k cells (production)

## Expected Runtime

- Coarse: 2 hours (4 cores)
- Medium: 6 hours (8 cores)
- Fine: 20 hours (16 cores)

## Key Outputs

- Solid fraction vs. time
- Temperature distribution
- Heat leak rate
- Charging/discharging energy

## Running the Case

```bash
# From cfd/scripts
python run_simulation.py --case storage_tank --mesh-size medium --parallel 8

# Manual OpenFOAM workflow
cd cases/storage_tank
blockMesh
snappyHexMesh -overwrite
splitMeshRegions -cellZones -overwrite
decomposePar -allRegions
mpirun -np 8 chtMultiRegionFoam -parallel
reconstructPar -allRegions
```

## Post-Processing

```bash
# Extract solid fraction
postProcess -func 'components(alpha.CO2)' -latestTime

# Extract temperature field
paraFoam

# Generate time-series plots
python ../scripts/postprocess.py --case storage_tank
```

## Notes

- Ensure CoolProp tables cover the operating range (-80°C to +30°C, 1-60 bar)
- Monitor solid fraction to avoid complete solidification (numerical instability)
- Adjust time step for phase change regions (CFL < 0.5 recommended)
