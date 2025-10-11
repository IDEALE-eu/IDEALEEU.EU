# THERMAL_PERF — Thermal Performance Testing

## Purpose

This directory contains thermal performance characterization data for coldplates, liquid plate heat exchangers (LPHX), and radiators.

## Contents

- Heat load vs. temperature (∆T-Q) curves
- Flow rate vs. pressure drop (∆P-Q) data
- System Effectiveness Ratio (SER) calculations
- Flow uniformity testing
- Channel performance data
- Thermal resistance measurements

## File Naming Convention

```
PERF_<test-type>_<serial>_<date>.<ext>
```

Examples:
- `PERF_deltaT-Q_CP-SN001_20251011.csv`
- `PERF_SER_HX-SN005_20251012.xlsx`
- `PERF_flow_uniformity_RAD-123_20251015.pdf`

## Test Objectives

### ∆T-Q Mapping
Characterize thermal performance:
- Vary heat load (Q) from min to max
- Measure inlet/outlet temperature difference (∆T)
- Measure flow rate and pressure drop
- Calculate thermal resistance

### System Effectiveness Ratio (SER)
```
SER = Q / (A × ∆T)
```
Where:
- Q = Heat transfer rate (W)
- A = Heat transfer area (m²)
- ∆T = Temperature difference (K)

Higher SER indicates better performance.

### Flow Uniformity
Verify all channels active:
- IR thermography of surface
- Outlet temperature uniformity
- Detect clogs or blockages
- Verify flow distribution

## Test Conditions

### Heat Loads
Vary from 0% to 110% of design load:
- Minimum operational load
- Nominal design load
- Maximum operational load
- Margin verification (110%)

### Flow Rates
Test at multiple flow rates:
- Minimum flow rate
- Nominal flow rate
- Maximum flow rate
- Verify performance across range

### Fluid Temperatures
Test at relevant fluid temperatures:
- Cold survival temperature
- Nominal operational temperature
- Hot survival temperature

## Data Collection

For each test point, record:
- Heat load applied (W)
- Fluid flow rate (kg/s or L/min)
- Inlet temperature (°C)
- Outlet temperature (°C)
- ∆T = T_out - T_in
- Pressure drop inlet to outlet (Pa)
- Surface temperatures (IR or thermocouples)
- Ambient conditions

## Performance Metrics

Calculate and report:
- **Thermal Resistance**: R = ∆T / Q (K/W)
- **Heat Transfer Coefficient**: h = Q / (A × ∆T) (W/m²K)
- **SER**: Q / (A × ∆T) (W/m²K)
- **Effectiveness**: ε = Q_actual / Q_max
- **Pressure Drop**: ∆P vs. flow rate

## Acceptance Criteria

Performance test passes if:
- ✅ Thermal resistance ≤ design prediction + margin
- ✅ SER ≥ design requirement
- ✅ No clogs or flow maldistribution detected
- ✅ Pressure drop within acceptable range
- ✅ Performance meets or exceeds specification

## Test-to-Analysis Correlation

Compare test results to CAE predictions:
- Plot test vs. analysis curves
- Calculate deltas and %errors
- Update thermal models if needed
- Document any discrepancies

## Related Directories

- **[../plans/](../plans/)** — Thermal performance test plans
- **[../procedures/](../procedures/)** — Test procedures
- **[../flow_dp/](../flow_dp/)** — Flow-pressure drop data
- **[../reports/](../reports/)** — Performance reports
- **[../../CAE/](../../CAE/)** — Thermal analysis models

---

**Last Updated**: 2025-10-10
