# CHANNEL_MAPS — DAQ Channel Assignments

## Purpose

This directory contains data acquisition channel maps, sensor assignments, calibration factors, and engineering unit conversions.

## Contents

- Sensor-to-channel mapping tables
- Calibration factors and offsets
- Engineering unit specifications
- Alarm limits and ranges
- Sample rate configurations
- Channel naming conventions

## File Naming Convention

```
CHMAP_<test-id>_<serial>_<rev>.{yaml|csv|xlsx}
```

Examples:
- `CHMAP_tvac_RAD-SN001__r01.yaml`
- `CHMAP_vib_HX-SN005__r02.csv`
- `CHMAP_thermal_perf_CP123__r01.xlsx`

## Channel Map Format

### YAML Format (Preferred)
```yaml
channel_map:
  version: "r01"
  test_article: "RAD-SN001"
  test_type: "TVAC"
  channels:
    - id: "TC001"
      name: "Radiator_Inlet_Temp"
      sensor_type: "T-Type Thermocouple"
      cal_factor: 1.0
      offset: 0.0
      units: "degC"
      range: [-50, 100]
      alarm_hi: 95.0
      alarm_lo: -45.0
      sample_rate: 1.0  # Hz
```

### CSV/Excel Format
Columns:
- Channel_ID
- Sensor_Name
- Sensor_Type
- Cal_Factor
- Offset
- Units
- Range_Min
- Range_Max
- Alarm_Hi
- Alarm_Lo
- Sample_Rate

## Sensor Types

### Temperature Sensors
- Thermocouples (T, K, J types)
- RTDs (PT100, PT1000)
- Thermistors
- IR sensors

### Pressure Sensors
- Absolute pressure transducers
- Differential pressure transducers
- Vacuum gauges

### Flow Sensors
- Mass flow meters
- Volumetric flow meters
- Flow switches

### Power/Voltage
- Heater power channels
- Voltage monitors
- Current sensors

### Strain/Displacement
- Strain gauges
- LVDTs
- Position sensors

## Calibration Information

For each channel, document:
- **Cal Factor**: Slope (eng units per volt)
- **Offset**: Zero offset (eng units)
- **Cal Date**: When last calibrated
- **Cal Cert**: Reference to calibration certificate
- **Uncertainty**: Measurement uncertainty (±)

## Naming Conventions

Use descriptive, consistent channel names:
```
<Location>_<Parameter>_<Sensor>
```

Examples:
- `Radiator_Inlet_Temp_TC01`
- `Coldplate_Center_Temp_RTD05`
- `FluidLoop_FlowRate_FM02`
- `Chamber_Pressure_PT01`

## Data Acquisition Settings

Document DAQ configuration:
- **Sample Rates**: Hz per channel or channel group
- **Filters**: Low-pass, anti-aliasing settings
- **Trigger**: Trigger source and conditions
- **Storage**: Data file format and location
- **Buffering**: Buffer size and memory allocation

## Quality Checks

Before test execution:
- ✅ Verify all channels respond
- ✅ Check calibration factors loaded
- ✅ Confirm engineering units correct
- ✅ Test alarm limits
- ✅ Verify sample rates adequate
- ✅ Check data storage path

## Related Directories

- **[../](../)** — Test setups overview
- **[../../calibration/](../../calibration/)** — Calibration certificates
- **[../../tvac/raw/](../../tvac/raw/)** — Raw data files
- **[../../procedures/](../../procedures/)** — Test procedures

---

**Last Updated**: 2025-10-10
