# SETUPS — Test Setup Configurations

## Purpose

This directory contains test setup configurations, fixture documentation, chamber recipes, and instrumentation channel maps.

## Contents

- **[fixtures/](fixtures/)** — Fixture IDs, clamp maps, photos
- **[chamber_recipes/](chamber_recipes/)** — TVAC profiles (YAML/CSV)
- **[channel_maps/](channel_maps/)** — DAQ assignments, scales, units

## Organization

### Fixtures
Documentation of mechanical fixtures and mounting hardware:
- Fixture identification and part numbers
- Clamp and bolt patterns
- Torque specifications
- Assembly photos and drawings
- Fixture calibration records

### Chamber Recipes
TVAC chamber control profiles:
- Temperature profiles vs. time
- Pressure set points
- Thermal shroud temperatures
- Ramp rates and dwell times
- Control parameters

### Channel Maps
Data acquisition channel assignments:
- Sensor-to-channel mapping
- Calibration factors and offsets
- Engineering units
- Alarm limits
- Sample rates

## File Organization

Organize by:
- Test campaign or serial number
- Test type (TVAC, vib, etc.)
- Date and configuration revision

## Setup Documentation

Each setup configuration should include:
- Test article serial number
- Fixture configuration and revision
- Instrumentation list
- Channel assignments
- Calibration data
- Setup photos
- As-run configuration notes

## Version Control

- Maintain revision history for all setups
- Document changes between configurations
- Link setups to specific test runs
- Archive obsolete configurations

## Related Directories

- **[../procedures/](../procedures/)** — Setup procedures
- **[../calibration/](../calibration/)** — Calibration certificates
- **[../tvac/](../tvac/)** — TVAC test data
- **[../plans/](../plans/)** — Test plans

---

**Last Updated**: 2025-10-10
