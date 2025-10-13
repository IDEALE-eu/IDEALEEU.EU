# LASER_TRACKER — Laser Tracker Measurement Data

## Purpose

This directory contains laser tracker measurement files, target configurations, and reports for large-scale check fixture operations.

## Contents

### Subdirectories
- **[TARGETS/](./TARGETS/)** — Target definitions and configurations
- **[LAYOUTS/](./LAYOUTS/)** — Measurement layout files
- **[REPORTS/](./REPORTS/)** — Measurement reports and results

## Laser Tracker Operations

### Measurement Process
1. Set up laser tracker and reference targets
2. Define coordinate system using reference points
3. Measure target locations on fixture and part
4. Compare measurements to nominal CAD data
5. Generate deviation reports
6. Document results

### Application Areas
- Large structure measurements
- Assembly alignment verification
- Fixture positioning and setup
- Interface verification
- Tooling certification

## Equipment

### Laser Tracker Systems
- Leica AT960/AT402
- FARO Vantage
- API Radian series
- Hexagon Absolute Tracker

### Measurement Accuracy
- Typical accuracy: ±0.010 mm + 5 µm/m
- Range: Up to 80 meters
- Sphere-mounted retroreflectors (SMR)
- 6DOF probes for additional measurements

## Quality Standards

Follow:
- **ASME B89.4.19**: Laser tracker performance evaluation
- **ISO 10360-10**: Laser tracker acceptance and reverification tests
- **Internal calibration procedures**: Site-specific requirements

## Related Directories

- **Setup procedures**: [`../SETUP/`](../SETUP/)
- **Check points**: [`../CHECK_POINTS/`](../CHECK_POINTS/)
- **Reports**: [`../REPORTS/`](../REPORTS/)
