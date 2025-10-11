# TVAC — Thermal Vacuum Testing

## Purpose

This directory contains thermal vacuum test data, analysis results, and performance plots for radiators and heat exchangers.

## Contents

- **[raw/](raw/)** — Raw data files (CSV/Parquet, chamber logs)
- **[reduced/](reduced/)** — Cleaned, synchronized datasets
- **[plots/](plots/)** — Time plots, stability analysis, thermal margins

## Test Objectives

TVAC testing demonstrates:
- Thermal performance at hot/cold survival temperatures
- Steady-state thermal balance
- Transient response characteristics
- Thermal margins to limits
- Functionality in vacuum environment

## Test Conditions

Typical TVAC conditions:
- **Pressure**: <1×10⁻⁵ Torr
- **Hot Survival**: +85°C (or per requirements)
- **Cold Survival**: -40°C (or per requirements)
- **Operational**: Mission-representative temperatures
- **Duration**: Per thermal stabilization criteria

## Data Collection

### Raw Data
- Time-series temperature data (all thermocouples/RTDs)
- Chamber pressure log
- Heater power profiles
- Thermal shroud temperatures
- Test article surface temperatures

### Derived Parameters
- Thermal balance (Q_in = Q_out)
- Temperature margins
- Thermal time constants
- Gradient across hardware
- Performance vs. predictions

## Success Criteria

TVAC test success requires:
- ✅ All temperatures within predicted ±5°C
- ✅ Adequate margin to limits (typically >10°C)
- ✅ Thermal stability achieved (<0.5°C/hr)
- ✅ No hardware damage or anomalies
- ✅ Functional verification passed

## File Organization

Organize by:
- Test article serial number
- Test phase (hot, cold, cycling)
- Test run number and date

## Related Directories

- **[../plans/](../plans/)** — TVAC test plans
- **[../procedures/](../procedures/)** — Test procedures
- **[../setups/chamber_recipes/](../setups/chamber_recipes/)** — Chamber profiles
- **[../reports/](../reports/)** — Test reports

---

**Last Updated**: 2025-10-10
