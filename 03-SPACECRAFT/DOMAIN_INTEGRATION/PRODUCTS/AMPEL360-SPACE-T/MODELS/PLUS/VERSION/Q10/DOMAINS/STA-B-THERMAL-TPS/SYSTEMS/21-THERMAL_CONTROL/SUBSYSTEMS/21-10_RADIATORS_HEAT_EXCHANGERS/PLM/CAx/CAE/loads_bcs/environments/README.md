# ENVIRONMENTS — Thermal Environments

## Purpose
Orbital and environmental parameter definitions for thermal analysis boundary conditions.

## Contents
- Solar flux intensity and spectrum
- Earth albedo factors
- Earth IR heating
- Beta angle definitions and ranges
- Seasonal variations
- Deep space sink temperature
- Attitude and pointing scenarios

## File Organization
- One file per environment type or orbit
- Include parametric definitions
- Document calculation methodology
- Store reference standards

## Naming Convention
```
21-10-CAE_environments_<type>_<orbit>__r<NN>__<STATUS>.{csv|xlsx}
```

Example: `21-10-CAE_environments_solar_leo__r01__REL.csv`

## Data Requirements
- Solar constant (W/m²)
- Albedo factor (0-1)
- Earth IR flux (W/m²)
- Beta angle range (degrees)
- Orbital parameters
- Eclipse fraction

## Environmental Parameters
- **Solar Flux**: 1367 W/m² (at 1 AU, typical)
- **Albedo**: 0.0 to 0.35 (typical range)
- **Earth IR**: ~240 W/m² (Earth-facing)
- **Deep Space Sink**: 3-4 K
- **Beta Angle**: -90° to +90°

## Worst-Case Definitions
- Hot case: Maximum solar, maximum albedo, minimum sink
- Cold case: Eclipse, minimum heat load, maximum sink

## Guidelines
- Reference mission orbit parameters
- Document seasonal variations
- Include beta angle sweep methodology
- Maintain consistency with mission analysis

---

**Last Updated**: 2025-10-10
