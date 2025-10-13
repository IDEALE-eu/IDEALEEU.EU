# Q100 Center Body - Quick Start Guide for Generative Design

## Overview
This guide helps you start the generative design phase for the Q100 Center Body (53-10).

---

## Prerequisites

### 1. System Requirements
- Python 3.8+ installed
- 4+ GB RAM available
- 10 GB disk space for results
- (Optional) FEA solver integration

### 2. Software Installation
```bash
# Navigate to driver scripts directory
cd 02-AIRCRAFT/DOMAIN_INTEGRATION/PRODUCTS/AMPEL360-AIR-T/MODELS/BWB-H2-Hy-E/CONF/BASELINE/FAMILY/Q100_STD01/VERSION/Q100/DOMAINS/AAA-AIRFRAMES-AERODYNAMICS-AIRWORTHINESS/SYSTEMS/53-FUSELAGE-STRUCTURES/SUBSYSTEMS/53-10_CENTER-BODY/PLM/CAx/CAO/SCRIPTS/DRIVERS/

# Install dependencies
pip install -r requirements.txt
```

---

## Quick Start (Synthetic Evaluation)

The driver includes synthetic evaluation for testing the optimization loop without real CAE.

### Run the Optimization
```bash
python driver.py
```

### What Happens
1. Loads configuration from `PROBLEMS/q100_cb.yaml`
2. Initializes NSGA-II with 32 population, 20 generations
3. Evaluates designs using synthetic functions
4. Exports results to `RESULTS/PARETO/`

### Expected Output
```
======================================================================
Q100 CENTER BODY OPTIMIZATION - GENERATIVE DESIGN PHASE
======================================================================

2025-10-09 10:30:00 [INFO] Configuration loaded
2025-10-09 10:30:05 [INFO] Problem initialized: 18 vars, 2 objs, 3 constrs
2025-10-09 10:30:10 [INFO] Starting NSGA-II optimization...
...
======================================================================
OPTIMIZATION COMPLETE
======================================================================
Total evaluations: 640
Pareto solutions: 15
Results directory: RESULTS/PARETO/
Run logs: RUNS/study_001/logs.txt

GENERATIVE DESIGN CRITERIA:
  ✓ Automated loop: CAD → CAE → eval → update
  ✓ ≥200 candidates evaluated (640)
  ✓ ≥1 Pareto front with ≥10 solutions (15)
  ✓ Reproducible from single script
  ✓ Results traceable and versioned

STATUS: READY FOR GENERATIVE DESIGN PHASE ✓
```

---

## Integrating Real CAE

### Step 1: Implement CAE Evaluator
Edit `driver.py`, replace `_synthetic_evaluation()` method:

```python
def _real_evaluation(self, x):
    """Real CAE evaluation - replace synthetic version."""
    
    # 1. Update CAD parameters
    param_dict = self._array_to_params(x)
    update_cad_model(param_dict)
    regenerate_geometry()
    
    # 2. Export geometry
    export_step("temp_geometry.stp")
    
    # 3. Update FEA mesh
    update_mesh("temp_geometry.stp", mesh_size=50.0)
    
    # 4. Run structural analyses
    run_static_analysis(load_cases=['LC1', 'LC2', 'LC3'])
    run_buckling_analysis()
    
    # 5. Extract results
    mass = extract_structural_mass()
    deflection = extract_max_deflection()
    stress = extract_max_von_mises_stress()
    buckling_rf = extract_min_buckling_rf()
    
    # 6. Compute constraints
    material_yield = 345.0  # MPa for AL 2024-T3
    cb_length = param_dict['cb_length']
    
    g1 = stress - (material_yield / 1.5)  # stress constraint
    g2 = 1.1 - buckling_rf                 # buckling constraint
    g3 = deflection - (cb_length / 500.0)  # deflection constraint
    
    return mass, deflection, np.array([g1, g2, g3])
```

### Step 2: Implement CAD/CAE Functions
Create helper functions for your specific tools:

```python
def update_cad_model(params):
    """Update parametric CAD model (CATIA, NX, SolidWorks API)."""
    # Tool-specific implementation
    pass

def run_static_analysis(load_cases):
    """Run FEA static analysis (Nastran, Abaqus, ANSYS)."""
    # Tool-specific implementation
    pass
```

### Step 3: Test Single Evaluation
Before running full optimization:

```python
# Test single evaluation
problem = Q100CenterBodyProblem(config)
x_test = np.array([...])  # Sample design
f, g = problem._real_evaluation(x_test)
print(f"Mass: {f[0]} kg, Deflection: {f[1]} mm")
print(f"Constraints: {g}")
```

---

## Monitoring Progress

### Check Logs in Real-Time
```bash
tail -f RUNS/study_001/logs.txt
```

### Check Pareto Front Size
```bash
wc -l RESULTS/PARETO/q100_cb_pareto.csv
```

### Check Evaluation Count
```bash
grep "Evaluation" RUNS/study_001/logs.txt | wc -l
```

---

## Configuration Tuning

### Adjust Population Size
Edit `PROBLEMS/q100_cb.yaml`:
```yaml
optimization:
  algorithm_params:
    population_size: 64  # Increase for better exploration
    n_generations: 15    # Reduce if time-constrained
```

### Adjust Mesh Density
```yaml
cae_settings:
  mesh_size: 75.0  # Coarser mesh for faster evaluation
  target_element_count: 30000
```

### Enable Caching
Caching is enabled by default in config:
```yaml
optimization:
  caching:
    enabled: true
    cache_file: RUNS/study_001/eval_cache.pkl
```

---

## Results Analysis

### Pareto Front CSV
```bash
# View Pareto solutions
head RESULTS/PARETO/q100_cb_pareto.csv
```

### Plot Trade-off Curve
```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('RESULTS/PARETO/q100_cb_pareto.csv', 
                 names=['design_vars...', 'mass', 'deflection', 'constraints...'])

plt.scatter(df['mass'], df['deflection'])
plt.xlabel('Structural Mass (kg)')
plt.ylabel('Max Deflection (mm)')
plt.title('Pareto Front: Mass vs Stiffness')
plt.grid(True)
plt.savefig('RESULTS/PLOTS/pareto_front.png')
```

### Select Reference Designs
1. **Minimum mass**: Lightest design
2. **Minimum deflection**: Stiffest design
3. **Balanced**: Middle of curve
4. **2 intermediate**: Span the trade-off space

---

## Troubleshooting

### Issue: "pymoo not installed"
```bash
pip install pymoo
```

### Issue: Optimization runs but no feasible solutions
- Check constraint limits in `q100_cb.yaml`
- Expand design space bounds
- Review constraint formulation in `CONSTRAINTS/`

### Issue: Evaluation taking too long
- Reduce mesh density in config
- Use coarser analysis settings
- Enable parallel evaluations (if supported)

### Issue: Python import errors
```bash
pip install --upgrade pymoo numpy scipy pyyaml matplotlib pandas
```

---

## Next Steps After First Run

1. **Validate Results**
   - Check Pareto front makes physical sense
   - Verify constraint satisfaction
   - Review convergence history

2. **Export Reference Designs**
   - Select 5 designs from Pareto front
   - Export to STEP format
   - Store in `CAD/EXPORTS/STEP/ASSEMBLIES/TOP_LEVEL/`

3. **Detailed Analysis**
   - Run refined FEA on selected designs
   - Perform stress analysis at critical points
   - Check manufacturing feasibility

4. **Documentation**
   - Update `RESULTS/PARETO/README.md` with findings
   - Create design trade study report
   - Link to requirements traceability

---

## Support Resources

### Documentation
- **Problem Definition**: `CAO/PROBLEMS/q100_cb.md`
- **Driver README**: `CAO/SCRIPTS/DRIVERS/README.md`
- **Generative Status**: `CAO/GENERATIVE_DESIGN_STATUS.md`

### Configuration Files
- **Problem Config**: `CAO/PROBLEMS/q100_cb.yaml`
- **Parameters**: `CAD/MODELS/MASTER/SKELETON/params.json`
- **Traceability**: `TRACE/REQ2TEST.csv`

### External References
- pymoo docs: https://pymoo.org
- NSGA-II paper: Deb et al. (2002)

---

**Version**: 1.0.0  
**Updated**: 2025-10-09  
**Status**: Ready for execution
