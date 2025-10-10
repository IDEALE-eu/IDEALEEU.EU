# PLOTS — Result Plots and Visualizations

## Purpose
Visual representations of analysis results for reporting and communication.

## Contents
- Temperature distribution contour plots
- Stress and strain field visualizations
- Flow field and streamline plots
- Time history and transient plots
- Convergence and residual plots
- Comparison and validation plots

## File Organization
- One subdirectory per analysis case or report
- Include plot metadata (case, date, units)
- Store high-resolution versions
- Maintain consistent formatting

## Naming Convention
```
21-10-CAE_plot_<case>_<parameter>__r<NN>__<STATUS>.{png|pdf|svg}
```

Example: `21-10-CAE_plot_thermal_balance_temp_distribution__r01__REL.png`

## Plot Requirements
- Include title and case identification
- Show units for all quantities
- Include color bar/legend
- Display min/max values
- Add timestamp and revision
- Use consistent color schemes

## Typical Plots
- **Thermal**: Temperature contours, heat flow arrows
- **Structural**: Von Mises stress, displacement magnitude
- **CFD**: Velocity magnitude, pressure contours, streamlines
- **Transient**: Temperature vs time, heating/cooling curves

## Format Guidelines
- **PNG**: For presentations and web (300 dpi)
- **PDF**: For reports and documentation (vector)
- **SVG**: For editable graphics (vector)

## Plot Formatting Standards
```python
# Example formatting guidelines
- Font size: 12-14 pt for axis labels
- Title: 16-18 pt bold
- Color map: Jet, Viridis, or custom thermal scale
- Aspect ratio: Maintain physical geometry
- Grid: Optional, subtle if used
```

## Guidelines
- Maintain traceability to analysis case
- Document plot generation method
- Use consistent formatting across reports
- Archive scripts used to generate plots

---

**Last Updated**: 2025-10-10
