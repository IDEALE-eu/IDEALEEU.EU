# RUNS — Analysis Execution

## Purpose
This directory contains analysis execution files including solver input decks and raw output results.

## Subdirectories

### [input/](input/) — Solver Input Decks
Solver input files and run configurations:
- Thermal solver decks (TMM)
- FEM solver decks (Nastran, ANSYS, Abaqus)
- CFD solver input files
- Job submission scripts
- Solver configuration files

**Format**: Native solver input formats, batch scripts

### [output/](output/) — Raw Results
Analysis output files:
- Solver output files
- Result databases
- Log files and convergence histories
- Checkpoint files
- Archive by content hash

**Format**: Native solver output formats, HDF5, results databases

## Run Organization
```
<case_name>_<date>/
  ├─ input/
  │  ├─ solver_deck.inp
  │  ├─ run_config.json
  │  └─ submit_job.sh
  └─ output/
     ├─ solver_output.out
     ├─ results.rst
     └─ convergence.log
```

## Naming Convention
```
21-10-CAE_run_<case>_<YYYYMMDD>__r<NN>__<STATUS>/
```

Example: `21-10-CAE_run_thermal_balance_hot_20251010__r01__REL/`

## Guidelines
- Archive complete run configurations
- Document solver version and settings
- Maintain reproducibility
- Hash-based result archival in output/
- Link runs to specific cases and models

---

**Last Updated**: 2025-10-10
