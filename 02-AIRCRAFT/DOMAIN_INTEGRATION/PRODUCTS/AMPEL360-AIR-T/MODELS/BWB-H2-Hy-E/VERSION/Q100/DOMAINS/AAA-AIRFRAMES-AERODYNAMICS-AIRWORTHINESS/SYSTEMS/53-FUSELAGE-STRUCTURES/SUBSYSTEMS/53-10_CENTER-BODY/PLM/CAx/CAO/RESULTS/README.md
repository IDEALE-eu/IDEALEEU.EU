# RESULTS — Optimization Results

## Purpose
Store and document optimization results, including Pareto fronts, plots, and formal reports.

## Subdirectories

### PARETO/ — Pareto Frontier Results
Multi-objective optimization Pareto sets:
- Pareto-optimal design points
- Trade-off curves (mass vs. stiffness, mass vs. cost)
- Non-dominated solution sets
- Decision-making data
- Sensitivity to weights
- Comparison across studies

**Format**: CSV data files, JSON design vectors, visualization plots

### PLOTS/ — Visualization and Plots
Graphical results and visualizations:
- Convergence plots
- Objective function histories
- Constraint violation plots
- Design variable evolution
- Response surface visualizations
- Trade-off charts
- Comparison bar charts

**Format**: PNG, PDF, SVG; matplotlib, Tecplot, or commercial tool outputs

### REPORTS/ — Formal Reports
Comprehensive optimization study reports:
- Executive summaries
- Problem formulation documentation
- Results analysis and interpretation
- Design recommendations
- Lessons learned
- Sensitivity studies
- Verification and validation

**Format**: PDF, Markdown, LaTeX sources

## Result Organization
```
STUDY_[NUMBER]_RESULTS/
  ├─ optimal_design.csv
  ├─ pareto_front.csv
  ├─ convergence.png
  └─ final_report.pdf
```

## Guidelines
- Archive raw result data in addition to plots
- Include metadata (date, solver, versions)
- Document post-processing procedures
- Maintain traceability to run inputs
- Compare with baseline designs
- Highlight key findings and recommendations
- Link results to design decisions
