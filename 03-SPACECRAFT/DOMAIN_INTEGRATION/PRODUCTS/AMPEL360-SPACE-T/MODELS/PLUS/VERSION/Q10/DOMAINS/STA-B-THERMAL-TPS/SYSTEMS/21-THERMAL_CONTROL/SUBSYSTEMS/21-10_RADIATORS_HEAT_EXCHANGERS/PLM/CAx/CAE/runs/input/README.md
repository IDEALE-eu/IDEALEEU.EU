# INPUT — Solver Input Decks

## Purpose
Solver input files, run configurations, and job submission scripts for thermal, structural, and CFD analysis.

## Contents
- Thermal solver input decks (TMM formats)
- FEM solver input files (Nastran, ANSYS, Abaqus)
- CFD solver input files (Fluent, Star-CCM+)
- Job submission scripts
- Solver configuration files
- Parameter files

## File Organization
- One subdirectory per analysis run
- Include all files needed to reproduce run
- Store solver configuration settings
- Document run parameters

## Naming Convention
```
21-10-CAE_input_<case>_<YYYYMMDD>__r<NN>__<STATUS>.{inp|bdf|dat}
```

Example: `21-10-CAE_input_thermal_balance_20251010__r01__REL.inp`

## Input File Requirements
- Complete solver deck (all dependencies)
- Material property references
- Boundary condition definitions
- Load definitions
- Solver control parameters
- Convergence criteria

## Job Submission Scripts
```bash
#!/bin/bash
# Analysis run script
SOLVER_VERSION="v2023.1"
INPUT_FILE="thermal_balance_hot.inp"
OUTPUT_DIR="./output/"

module load thermal_solver/${SOLVER_VERSION}
run_solver -i ${INPUT_FILE} -o ${OUTPUT_DIR}
```

## Guidelines
- Document solver version and settings
- Include all referenced external files
- Maintain reproducibility
- Archive with corresponding output

---

**Last Updated**: 2025-10-10
