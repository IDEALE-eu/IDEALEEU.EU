# SCRIPTS — Automation Scripts

## Purpose
Automation and workflow scripts for optimization processes.

## Subdirectories

### [PRE/](PRE/) — Pre-processing Scripts
Scripts for optimization setup:
- Problem definition parsers
- Design space initialization
- Initial population generation
- Constraint function builders
- Objective function setup
- Input file generation
- Model validation checks

**Languages**: Python, MATLAB, Bash

### [POST/](POST/) — Post-processing Scripts
Scripts for result analysis:
- Result extraction and parsing
- Pareto front generation
- Trade study analysis
- Visualization automation
- Report generation
- Statistical analysis
- Data export for Digital Twin

**Languages**: Python, MATLAB, R

### [DRIVERS/](DRIVERS/) — Optimization Drivers
Master scripts coordinating optimization workflow:
- End-to-end optimization drivers
- CAD/CAE/Optimizer coupling
- Parallel execution management
- Batch job submission
- Workflow orchestration
- Error handling and recovery

**Languages**: Python, Bash, workflow tools (Airflow, Luigi)

## Script Organization
```
script_name.py
  ├─ README.md (usage, inputs, outputs)
  ├─ requirements.txt (dependencies)
  └─ examples/ (test cases)
```

## Guidelines
- Include clear documentation in headers
- Use version control for all scripts
- Test with representative problems
- Include error handling and logging
- Provide usage examples
- Use standard libraries (NumPy, Pandas, SciPy)
- Maintain compatibility with solver APIs
- Archive scripts with results they generate
