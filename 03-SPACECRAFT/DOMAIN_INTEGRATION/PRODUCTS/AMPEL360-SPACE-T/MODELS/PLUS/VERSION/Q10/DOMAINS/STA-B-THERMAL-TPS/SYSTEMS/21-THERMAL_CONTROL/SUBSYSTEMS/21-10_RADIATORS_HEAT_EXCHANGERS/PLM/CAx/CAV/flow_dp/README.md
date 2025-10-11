# FLOW_DP — Flow vs. Pressure Drop Testing

## Purpose

This directory contains flow rate vs. pressure drop characterization data, clog detection tests, and bleed/purge verification.

## Contents

- Flow rate vs. ∆P curves
- Hydraulic resistance data
- Clog detection test results
- Bleed and purge effectiveness tests
- Flow distribution measurements
- Contamination sensitivity testing

## File Naming Convention

```
FLOW_<test-type>_<serial>_<date>.<ext>
```

Examples:
- `FLOW_dp_vs_Q_CP-SN001_20251011.csv`
- `FLOW_clog_test_HX-SN005_20251012.xlsx`
- `FLOW_purge_effectiveness_RAD-123_20251015.pdf`

## Test Objectives

### Flow-Pressure Drop Characterization
- Measure ∆P vs. flow rate over full range
- Determine hydraulic resistance
- Verify laminar/turbulent transition
- Compare to design predictions

### Clog Detection
- Verify no manufacturing debris
- Check for contamination
- Detect partial blockages
- Ensure all channels open

### Bleed/Purge Testing
- Verify air can be purged from system
- Measure time to achieve bubble-free flow
- Check bleed port effectiveness
- Verify fill procedures adequate

## Test Conditions

### Flow Rates
Test from 0% to 110% of design flow:
- 0% (static head)
- 25% of nominal
- 50% of nominal
- 75% of nominal
- 100% of nominal (design point)
- 110% of nominal (margin)

### Fluids
Test with:
- Water (for development testing)
- Flight fluid (for qualification)
- Multiple viscosities (if applicable)

### Temperatures
Test at:
- Cold operational temperature
- Nominal temperature
- Hot operational temperature

## Data Collection

For each flow rate, record:
- Volumetric flow rate (L/min)
- Mass flow rate (kg/s)
- Inlet pressure (Pa)
- Outlet pressure (Pa)
- ∆P = P_in - P_out
- Fluid temperature (°C)
- Fluid properties (density, viscosity)

## Performance Metrics

Calculate:
- **Hydraulic Resistance**: R_h = ∆P / Q
- **Reynolds Number**: Re = ρVD/μ
- **Friction Factor**: f = ∆P / (0.5ρV²L/D)
- **K-Factor**: K = ∆P / (0.5ρV²)

## Acceptance Criteria

Flow test passes if:
- ✅ ∆P vs. Q curve matches predictions ± 20%
- ✅ No anomalous high ∆P indicating clogs
- ✅ Flow distribution uniform across channels
- ✅ Air can be purged in reasonable time
- ✅ Maximum ∆P below pump capability

## Clog Detection Methods

### Pressure Drop Method
- Elevated ∆P at given flow rate
- Compare to baseline or predictions
- >20% increase suggests clog

### Flow Uniformity
- IR thermography shows cold channels
- Unequal outlet temperatures
- Visual flow indication (if possible)

### Acoustic/Vibration
- Unusual noise or vibration
- Cavitation indicators
- Flow-induced resonances

## Bleed/Purge Verification

Verify:
- ✅ Bleed ports at high points functional
- ✅ Air bubbles can be expelled
- ✅ Fill procedure effective
- ✅ System fully wetted
- ✅ No trapped air pockets

## Data Presentation

Plot:
- ∆P vs. Q (log-log scale typical)
- Compare multiple test runs
- Overlay design predictions
- Annotate operating point

## Related Directories

- **[../thermal_perf/](../thermal_perf/)** — Thermal performance data
- **[../procedures/](../procedures/)** — Flow test procedures
- **[../anomalies/](../anomalies/)** — Clog/contamination records
- **[../reports/](../reports/)** — Flow test reports

---

**Last Updated**: 2025-10-10
