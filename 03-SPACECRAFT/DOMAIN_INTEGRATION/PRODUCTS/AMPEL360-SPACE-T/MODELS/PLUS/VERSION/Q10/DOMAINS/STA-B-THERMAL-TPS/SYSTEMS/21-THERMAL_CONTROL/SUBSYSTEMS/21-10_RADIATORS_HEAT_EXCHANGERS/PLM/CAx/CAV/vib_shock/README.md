# VIB_SHOCK — Vibration and Shock Testing

## Purpose

This directory contains vibration and shock test data for radiators, heat exchangers, and thermal hardware.

## Contents

- Sine sweep test results
- Random vibration test data
- Shock test results
- Response spectra and transfer functions
- Resonance identification
- Pre/post-test inspection records
- Accelerometer data and PSD plots

## File Naming Convention

```
VIB_<test-type>_<serial>_<axis>_<date>.<ext>
```

Examples:
- `VIB_sine_RAD-SN001_X-axis_20251011.csv`
- `VIB_random_HX-SN005_Z-axis_20251012.txt`
- `SHOCK_pyro_CP123_Y-axis_20251015.tdms`

## Test Types

### Sine Sweep
- Identify structural resonances
- Verify no resonances in critical bands
- Measure transmissibility and Q-factors
- Check for structural yielding

### Random Vibration
- Qualification or acceptance level testing
- Duration per mission profile
- Monitor response at critical locations
- Verify survival without damage

### Shock
- Pyroshock simulation (if applicable)
- Separation shock events
- Verify survival of shock environment
- Check for damage or loosening

## Test Levels

Typical qualification levels:
- **Sine Sweep**: 0.5-2000 Hz, 0.5-2.0 g
- **Random**: Per mission PSD, 1-3 minutes per axis
- **Shock**: Per shock response spectrum (SRS)

## Data Collection

### Accelerometer Data
- Control accelerometer on fixture
- Response accelerometers on test article
- Sample rate: 5-10× highest frequency
- Record full time history

### Derived Data
- Power spectral density (PSD)
- Shock response spectrum (SRS)
- Transmissibility (response/input)
- Resonance frequencies and Q-factors

## Acceptance Criteria

Test passes if:
- ✅ No structural damage observed
- ✅ No functional failures
- ✅ Resonances within predicted ranges
- ✅ No hardware loosening or fatigue
- ✅ Post-test inspection clean

## Safety Requirements

- ⚠️ Secure fixture and test article properly
- 🔊 Hearing protection required in test area
- 📹 Remote monitoring during high-level tests
- 🛑 Abort criteria defined (overload, anomalies)

## Test Documentation

For each test, include:
- Test setup photos and drawings
- Fixture configuration
- Accelerometer locations
- Control parameters and tolerances
- Test duration and levels achieved
- Response data and analysis

## Related Directories

- **[../plans/](../plans/)** — Vibration test plans
- **[../procedures/](../procedures/)** — Test procedures
- **[../setups/](../setups/)** — Fixture configurations
- **[../reports/](../reports/)** — Test reports

---

**Last Updated**: 2025-10-10
