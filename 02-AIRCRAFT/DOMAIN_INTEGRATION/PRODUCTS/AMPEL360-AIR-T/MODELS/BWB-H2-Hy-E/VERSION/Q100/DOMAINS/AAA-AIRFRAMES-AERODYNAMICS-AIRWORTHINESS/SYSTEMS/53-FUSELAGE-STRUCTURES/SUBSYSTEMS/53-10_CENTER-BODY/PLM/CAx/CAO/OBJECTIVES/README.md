# OBJECTIVES — Optimization Objectives

## Purpose
Define optimization objective functions for center body design, supporting single-objective and multi-objective optimization.

## Subdirectories

### MASS/ — Mass Minimization
Structural mass objectives:
- Total structural mass
- Operating empty weight (OEW) contribution
- Mass per unit area/length
- Mass budget tracking
- Weight reduction targets
- Cumulative weight savings

**Priority**: Primary objective for most structural optimizations

### STIFFNESS/ — Stiffness Objectives
Structural stiffness targets:
- Global stiffness requirements
- Deflection limits under load
- Natural frequency requirements
- Flutter margin considerations
- Dynamic response characteristics

**Priority**: Often a constraint, sometimes co-optimized with mass

### COST/ — Cost Objectives
Lifecycle cost minimization:
- Manufacturing cost
- Material cost
- Assembly labor cost
- Tooling cost
- Recurring vs. non-recurring costs
- Maintenance cost impact

**Priority**: Secondary objective, often traded against performance

## Multi-Objective Optimization
- Pareto frontier generation (mass vs. stiffness, mass vs. cost)
- Weighted sum approaches
- ε-constraint methods
- Trade-off analysis and decision making
- Stakeholder preference integration

## Guidelines
- Normalize objective functions for multi-objective optimization
- Document weighting factors and rationale
- Maintain objective function evaluations with design history
- Link objectives to top-level requirements (Q100 MTOW, OEW targets)
- Conduct sensitivity analysis on objective weights
- Generate trade studies and Pareto fronts
