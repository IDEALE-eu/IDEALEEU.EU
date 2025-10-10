# Study 001 - Initial Q100 Center Body Optimization

## Study Information
- **Study ID**: study_001
- **Problem**: q100_cb (Q100 Center Body Multi-Objective Optimization)
- **Started**: 2025-10-09
- **Status**: Ready to run

## Objective
Initial generative design study to establish Pareto front between structural mass and stiffness for the Q100 center body.

## Configuration
- Algorithm: NSGA-II
- Population: 32
- Generations: 20
- Design variables: 18
- Objectives: 2 (minimize mass, minimize deflection)
- Constraints: 3 (stress, buckling, deflection ratio)

## Expected Outputs
This directory will contain:
- `candidates.csv` - All evaluated designs
- `convergence.csv` - Convergence metrics per generation
- `logs.txt` - Detailed execution log
- `eval_cache.pkl` - Cached evaluations for reuse
- `metadata.json` - Study metadata and summary
- `config.yaml` - Copy of problem configuration

## Execution
Run from SCRIPTS/DRIVERS/:
```bash
python driver.py
```

## Success Criteria
- ✓ ≥200 unique candidates evaluated
- ✓ ≥10 non-dominated solutions in Pareto front
- ✓ All evaluations logged and traceable
- ✓ Results reproducible from config + seed

## Notes
- First run may take 40-100 hours depending on FEA evaluation time
- Cached evaluations will speed up subsequent runs
- Study can be resumed if interrupted (cache persists)

---
**Created**: 2025-10-09  
**Status**: Initialized  
