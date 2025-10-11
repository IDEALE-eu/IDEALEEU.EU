# PLOTS — TVAC Data Visualization

## Purpose

This directory contains plots, charts, and visualizations of TVAC test data for analysis and reporting.

## Contents

- Temperature vs. time plots
- Thermal stability plots
- Temperature distribution maps
- Margin assessments
- Transient response curves
- Thermal balance plots
- Performance comparison charts

## File Naming Convention

```
<test-id>_<serial>_<plot-type>_<date>.<ext>
```

Examples:
- `TVAC-001_RAD-SN001_temp_vs_time_20251011.png`
- `TVAC-002_HX-SN005_thermal_margins_20251012.pdf`
- `TVAC-003_CP123_stability_analysis_20251015.png`

## Plot Types

### Time History Plots
Temperature vs. time for all sensors:
- All thermocouples on radiator
- Chamber and shroud temperatures
- Heater power profile
- Pressure profile

### Thermal Stability
Assess thermal equilibrium:
- Temperature rate of change (dT/dt)
- Stability criteria verification
- Time to stabilization

### Thermal Margins
Visualize margins to limits:
- Bar charts showing T_measured vs. T_limit
- Margin values (T_limit - T_measured)
- Hot and cold cases

### Spatial Distribution
Temperature contours on hardware:
- 2D temperature maps
- Gradient visualization
- Hot/cold spot identification

### Test vs. Prediction
Comparison plots:
- Measured vs. predicted temperatures
- Delta (test - analysis)
- Correlation assessment

### Transient Response
Dynamic thermal behavior:
- Response to heater power changes
- Thermal time constants
- Heating/cooling rates

## Plot Standards

### Format Requirements
- **Title**: Test ID, serial, date
- **Axes**: Clear labels with units
- **Legend**: Sensor IDs and descriptions
- **Grid**: For readability
- **Annotations**: Key events, phases
- **Quality**: High resolution (300 dpi min)

### File Formats
- **PNG**: For reports and presentations
- **PDF**: For vector graphics, archival
- **SVG**: For editable vector graphics
- **MATLAB .fig**: For interactive analysis

## Plot Organization

Organize by:
- Test phase (hot, cold, cycling)
- Plot type (time history, stability, etc.)
- Test article serial number

## Automation

- Use scripted plotting for consistency
- Maintain plotting scripts with data
- Automate plot generation when possible
- Document plotting parameters

## Quality Checks

All plots should:
- ✅ Have clear, readable text
- ✅ Include units on all axes
- ✅ Show data source and date
- ✅ Be properly scaled
- ✅ Have informative titles
- ✅ Include legends when needed

## Related Directories

- **[../raw/](../raw/)** — Raw data source
- **[../reduced/](../reduced/)** — Processed data plotted
- **[../../reports/](../../reports/)** — Reports using these plots
- **[../../plans/](../../plans/)** — Requirements for plots

---

**Last Updated**: 2025-10-10
