# Q100 Center Body Optimization Driver

## Purpose
Master script orchestrating the generative design workflow for center body structural optimization.

## Usage

### Installation
```bash
# Install required Python packages
pip install pymoo numpy pyyaml scipy matplotlib

# Optional: FEA integration libraries
pip install meshio h5py
```

### Running the Optimization
```bash
cd CAO/SCRIPTS/DRIVERS/
python driver.py
```

### With Custom Configuration
```bash
python driver.py --config ../../PROBLEMS/q100_cb_custom.yaml
```

## Workflow

The driver executes the following steps:

1. **Load Configuration**
   - Read problem definition from `PROBLEMS/q100_cb.yaml`
   - Load parameter bounds from `CAD/MODELS/MASTER/SKELETON/params.json`

2. **Initialize Optimizer**
   - Setup NSGA-II with configured parameters
   - Initialize population (LHS or Sobol sampling)
   - Setup evaluation cache

3. **Optimization Loop**
   For each candidate design:
   - Update CAD parameters → regenerate geometry
   - Update FEA mesh → run structural analysis
   - Extract objectives (mass, deflection)
   - Extract constraint values (stress, buckling)
   - Evaluate fitness and feasibility
   - Apply genetic operators (selection, crossover, mutation)

4. **Export Results**
   - Pareto front → `RESULTS/PARETO/q100_cb_pareto.csv`
   - All candidates → `RUNS/study_001/candidates.csv`
   - Convergence history → `RUNS/study_001/convergence.csv`
   - Execution logs → `RUNS/study_001/logs.txt`
   - Top designs → `CAD/EXPORTS/STEP/.../*.stp`

## Configuration

Key parameters in `q100_cb.yaml`:
- `population_size`: 32 (NSGA-II population)
- `n_generations`: 20 (stopping criterion)
- `n_samples`: 64 (initial DOE)
- `seed`: 42 (reproducibility)

## Outputs

### RESULTS/PARETO/q100_cb_pareto.csv
Non-dominated solutions (Pareto front):
```csv
cb_length,cb_width,...,mass,deflection,g1,g2,g3
8000,12000,...,3200,15.2,-10.5,-0.15,-2.3
7500,11500,...,3100,16.8,-5.2,-0.08,-1.1
...
```

### RUNS/study_001/candidates.csv
All evaluated designs with metadata:
```csv
eval_id,timestamp,x1,x2,...,f1,f2,g1,g2,g3,feasible
1,2025-10-09T10:30:00,8000,...,3200,15.2,-10,-0.1,-2,True
2,2025-10-09T10:50:00,7500,...,3100,16.8,-5,-0.05,-1,True
...
```

### RUNS/study_001/logs.txt
Detailed execution log:
```
2025-10-09 10:30:00 [INFO] Configuration loaded
2025-10-09 10:30:05 [INFO] Problem initialized: 18 vars, 2 objs, 3 constrs
2025-10-09 10:30:10 [INFO] Starting NSGA-II optimization...
2025-10-09 10:30:15 [INFO] Evaluation 1: mass=3200.0 kg, deflection=15.2 mm
...
```

## Performance

### Computational Requirements
- RAM: 4-8 GB
- CPU: 4+ cores recommended
- Disk: 10 GB for results
- Runtime: 40-100 hours (200-500 evaluations @ 10-20 min each)

### Parallelization
To enable parallel evaluations (if FEA solver supports):
```yaml
optimization:
  parallelization:
    enabled: true
    n_workers: 4
```

## Extending the Driver

### Custom CAD/CAE Integration
Replace `_synthetic_evaluation()` with:
```python
def _real_evaluation(self, x):
    # Update CAD
    update_cad_parameters(x)
    regenerate_geometry()
    export_geometry('temp_geometry.stp')
    
    # Run FEA
    update_mesh('temp_geometry.stp')
    run_static_analysis()
    run_buckling_analysis()
    
    # Extract results
    mass = extract_mass()
    deflection = extract_max_deflection()
    stress = extract_max_stress()
    buckling_rf = extract_buckling_rf()
    
    # Compute constraints
    g1 = stress - 230.0  # stress limit
    g2 = 1.1 - buckling_rf  # buckling limit
    g3 = deflection - (x[0] / 500.0)  # deflection limit
    
    return mass, deflection, [g1, g2, g3]
```

### Custom Objectives
Add new objectives in `q100_cb.yaml` and update problem definition:
```python
n_obj = len(config['objectives'])  # Auto-detects from config
```

### Custom Constraints
Add constraint definitions to configuration and evaluation function.

## Troubleshooting

### Issue: CAD regeneration fails
- Check parameter bounds are physically valid
- Verify CAD model robustness to parameter changes
- Add geometry validation checks

### Issue: FEA convergence failures
- Check mesh quality (aspect ratio, warping)
- Verify boundary conditions
- Adjust solver tolerances

### Issue: Optimization stagnates
- Increase population size
- Increase mutation rate
- Restart with different seed

### Issue: All designs infeasible
- Relax constraints or expand design space
- Check constraint formulation
- Use constraint handling techniques (epsilon-constraint, repair)

## References
- NSGA-II algorithm: Deb et al. (2002)
- pymoo documentation: https://pymoo.org
- Problem definition: `PROBLEMS/q100_cb.md`

---
**Version**: 1.0.0  
**Created**: 2025-10-09  
**Status**: Active  
**Maintainer**: Design Automation Team
