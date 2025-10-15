# NSGA-II Configuration for Q100 Center Body Optimization

## Algorithm
Non-dominated Sorting Genetic Algorithm II (NSGA-II)

## Purpose
Multi-objective optimization with 2 objectives:
1. Minimize structural mass
2. Minimize maximum deflection

## Configuration

### Population Settings
```yaml
population_size: 32
n_generations: 20
n_offsprings: 32
```

### Genetic Operators

#### Crossover
- **Type**: Simulated Binary Crossover (SBX)
- **Probability**: 0.9
- **Distribution index (η_c)**: 15
- **Purpose**: Exploit solution space around parents

#### Mutation
- **Type**: Polynomial Mutation
- **Probability**: 0.1 (per variable)
- **Distribution index (η_m)**: 20
- **Purpose**: Explore new regions

### Selection
- **Method**: Binary tournament selection
- **Crowding distance**: Yes (diversity preservation)
- **Elitism**: Yes (non-dominated solutions preserved)

### Termination Criteria
- Maximum generations: 20
- Maximum evaluations: 500 (whichever comes first)
- Convergence tolerance: 1e-6 (optional, rarely triggered)

## Expected Performance

### Computational Budget
- Population × Generations: 32 × 20 = 640 evaluations
- With caching and initial sampling: ~200-300 unique evaluations
- Time per evaluation: 10-20 minutes (FEA)
- Total runtime: 40-100 hours

### Convergence
- Pareto front typically forms by generation 10-15
- Refinement continues to generation 20
- Expect 10-20 non-dominated solutions

## Implementation

### Python (pymoo)
```python
from pymoo.algorithms.moo.nsga2 import NSGA2
from pymoo.operators.crossover.sbx import SBX
from pymoo.operators.mutation.pm import PM
from pymoo.optimize import minimize

algorithm = NSGA2(
    pop_size=32,
    n_offsprings=32,
    crossover=SBX(eta=15, prob=0.9),
    mutation=PM(eta=20),
    eliminate_duplicates=True
)

result = minimize(
    problem,
    algorithm,
    ('n_gen', 20),
    seed=42,
    verbose=True,
    save_history=True
)
```

### Key Parameters Rationale

**Population Size (32)**
- Small enough for fast iterations
- Large enough for diversity
- Standard for 18 design variables

**Generation Count (20)**
- Balance between quality and time
- Sufficient for convergence
- Can extend if time permits

**SBX η=15**
- Moderate exploitation
- Balances exploration/exploitation

**PM η=20**
- Controlled mutation
- Prevents excessive jumps

## Output Files
- `pareto_front.csv` - Final non-dominated solutions
- `population_history.pkl` - All populations per generation
- `convergence_metrics.csv` - Hypervolume, IGD per generation
- `final_population.csv` - Last generation population

## Validation
Compare with:
- Random search baseline
- Single-objective GA (mass only)
- Classical gradient-based (if surrogate available)

## References
- Deb et al. (2002). "A fast and elitist multiobjective genetic algorithm: NSGA-II"
- pymoo documentation: https://pymoo.org/algorithms/moo/nsga2.html

---
**Created**: 2025-10-09
**Version**: 1.0.0
**Status**: Active
