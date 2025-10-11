# CHAMBER_RECIPES — TVAC Chamber Control Profiles

## Purpose

This directory contains thermal vacuum chamber control recipes, temperature profiles, and pressure schedules.

## Contents

- TVAC temperature profiles vs. time
- Pressure schedules and set points
- Thermal shroud temperatures
- Ramp rates and dwell times
- Control parameters and limits
- Chamber configuration files

## File Naming Convention

```
RECIPE_<test-type>_<profile>_<rev>.{yaml|csv}
```

Examples:
- `RECIPE_tvac_hot_survival__r01.yaml`
- `RECIPE_tvac_cold_operational__r02.csv`
- `RECIPE_tvac_thermal_cycle__r03.yaml`

## Recipe Format

### YAML Format (Preferred)
```yaml
recipe_name: "TVAC Hot Survival"
revision: "r01"
test_type: "thermal_vacuum"
pressure_setpoint: 1.0e-5  # Torr
phases:
  - name: "Pumpdown"
    duration: 120  # minutes
    target_pressure: 1.0e-5
  - name: "Hot Soak"
    duration: 240
    target_temp: 85.0  # °C
    ramp_rate: 5.0  # °C/min
```

### CSV Format
Time-based profile with columns:
- Time (minutes)
- Chamber_Temp (°C)
- Shroud_Temp (°C)
- Pressure (Torr)
- Notes

## Profile Types

### Hot Survival
- Maximum qualification temperature
- Extended dwell for thermal stabilization
- Margin demonstration

### Cold Survival
- Minimum qualification temperature
- Cold soak duration per requirements
- Operational verification at cold

### Thermal Cycling
- Hot-cold cycles
- Transition rates
- Dwell times at extremes
- Number of cycles

### Operational Performance
- Mission-representative conditions
- Steady-state performance points
- Transient response characterization

## Control Parameters

Document for each recipe:
- **Pressure**: Target and limits
- **Temperatures**: Chamber, shroud, test article zones
- **Ramp Rates**: Heating and cooling rates
- **Dwell Times**: Stabilization and soak durations
- **Alarms**: Out-of-limit trip points
- **Interlocks**: Safety shutdown conditions

## Chamber Configuration

Include chamber-specific settings:
- Shroud configuration (zones, panels)
- LN2 flow control parameters
- Heater power limits
- Pressure transducer ranges
- Thermocouple locations

## Validation

Before use, recipes must be:
- ✅ Reviewed against test plan
- ✅ Validated for chamber capability
- ✅ Approved by test engineer
- ✅ Safety review completed
- ✅ Dry-run tested (if first use)

## Related Directories

- **[../](../)** — Test setups overview
- **[../channel_maps/](../channel_maps/)** — DAQ configuration
- **[../../tvac/](../../tvac/)** — TVAC test data
- **[../../plans/](../../plans/)** — Test plans

---

**Last Updated**: 2025-10-10
