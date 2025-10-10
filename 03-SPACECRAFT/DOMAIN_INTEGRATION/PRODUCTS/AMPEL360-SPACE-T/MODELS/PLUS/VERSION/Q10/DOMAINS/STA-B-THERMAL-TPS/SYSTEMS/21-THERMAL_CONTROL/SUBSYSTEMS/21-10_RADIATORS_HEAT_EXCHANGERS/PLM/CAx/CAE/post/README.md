# POST — Post-Processing

## Purpose
This directory contains post-processed results including plots, tables, and post-processing scripts.

## Subdirectories

### [plots/](plots/) — Result Plots
Visualization of analysis results:
- Temperature distribution plots
- Stress/strain contour plots
- Flow field visualizations
- Time history plots
- Convergence plots

**Format**: PNG, PDF, SVG

### [tables/](tables/) — Result Tables
Tabulated analysis results:
- Temperature summary tables
- Stress and margin tables
- Heat flow summaries
- Performance metrics
- Comparison tables

**Format**: CSV, XLSX, markdown tables

### [scripts/](scripts/) — Post-Processing Scripts
Automation scripts for result extraction:
- Result extraction utilities
- Plot generation scripts
- Table formatting tools
- Report automation
- Data export for Digital Twin

**Format**: Python, MATLAB, shell scripts

## File Organization
- Organize by analysis case
- Include metadata (date, version, case)
- Link to source raw results
- Document processing methodology

## Naming Convention
```
21-10-CAE_post_<type>_<case>__r<NN>__<STATUS>.{png|csv|py}
```

Example: `21-10-CAE_post_plot_temp_distribution__r01__REL.png`

## Guidelines
- Maintain traceability to raw results
- Document post-processing steps
- Use consistent plot formatting
- Archive scripts with results
- Include legends and units

---

**Last Updated**: 2025-10-10
