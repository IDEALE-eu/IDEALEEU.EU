# CONFIG — Optimization Configuration

## Purpose
Store optimization configuration files, parameters, and random seeds for reproducibility.

## Subdirectories

### PARAMS/ — Parameter Files
Optimization algorithm parameters:
- Solver settings (tolerance, max iterations, etc.)
- Algorithm-specific parameters (population size, mutation rate)
- Constraint penalty weights
- Objective function weights
- Design space bounds
- Convergence criteria

**Format**: JSON, YAML, XML, or solver-specific formats

### SEEDS/ — Random Seeds
Random number generator seeds for reproducibility:
- Initial population seeds (genetic algorithms, PSO)
- Monte Carlo simulation seeds
- Stochastic solver seeds
- Design of experiments (DOE) seeds

**Purpose**: Ensure reproducibility of optimization runs

## Configuration Management
- Version control all configuration files
- Document parameter selection rationale
- Archive configurations with run results
- Maintain baseline configurations
- Track parameter sensitivity

## Example Configuration Structure
```json
{
  "algorithm": "NSGA-II",
  "population_size": 100,
  "max_generations": 200,
  "mutation_rate": 0.1,
  "crossover_rate": 0.9,
  "seed": 42,
  "objectives": ["mass", "stiffness"],
  "constraints": ["strength", "buckling"]
}
```

## Guidelines
- Use human-readable formats when possible
- Include units in parameter definitions
- Document parameter ranges and defaults
- Test sensitivity to parameter changes
- Archive successful configurations as templates
