# RUNS — Optimization Execution

## Purpose
Manage optimization study execution, including run configurations and execution logs.

## Subdirectories

### [STUDIES/](STUDIES/) — Optimization Studies
Individual optimization study definitions:
- Study configuration files
- Initial design points
- Optimization run setups
- Batch job scripts
- Study objectives and scope
- Design of experiments (DOE)
- Sensitivity studies

**Organization**: One subdirectory per study (e.g., `STUDY_001_MASS_MIN/`, `STUDY_002_MULTIOBJECTIVE/`)

### [LOGS/](LOGS/) — Execution Logs
Runtime logs and diagnostics:
- Solver output logs
- Convergence histories
- Iteration summaries
- Error logs and warnings
- Resource usage (CPU, memory, walltime)
- Job submission records

**Format**: Text logs, CSV convergence data, HDF5 history files

## Study Naming Convention
```
STUDY_[NUMBER]_[OBJECTIVE]_[DATE]/
  ├─ config.json
  ├─ initial_design.csv
  ├─ run_script.sh
  └─ README.md
```

## Guidelines
- Document study purpose and scope in README
- Archive input files with each study
- Log all optimization parameters
- Track computational resources used
- Maintain run reproducibility
- Link studies to problem definitions
- Compare results across studies
