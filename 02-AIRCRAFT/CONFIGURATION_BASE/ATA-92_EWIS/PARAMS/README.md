# Wire Specifications and Parameters

This directory contains wire gauge specifications, shielding requirements, zone definitions, and environmental ratings for all aircraft wiring.

## Overview

Per EWIS rules, ALL wire specifications for the entire aircraft are centralized here.

## Contents

### Wire Specifications
- `WIRE_GAUGE_SPECS.csv` - Wire gauge specifications (AWG/mm²)
- `WIRE_DERATING.csv` - Current derating factors by environment
- `ENVIRONMENTAL_RATINGS.csv` - Temperature and environmental ratings

### Shielding and Protection
- `SHIELDING_SPECS.csv` - Shielding requirements by circuit type
- `GROUNDING_SPECS.csv` - Grounding and bonding requirements
- `WIRE_SEPARATION_RULES.csv` - Separation requirements (power vs. signal)

### Zone Definitions
- `ZONE_DEFINITIONS.csv` - Aircraft zone definitions for wire routing
- `ZONE_ENVIRONMENTAL_CONDITIONS.csv` - Environmental conditions by zone

## Wire Marking Standards

All wires marked per ARINC 622:
- System code (ATA chapter)
- Wire number
- Segment identifier
- Gauge designation

Example: `27-1234-A-20` (ATA-27, wire 1234, segment A, 20 AWG)

## Regulatory Compliance

EWIS specifications must comply with:
- FAA SFAR 88
- EASA CS-25 Amendment 15
- DO-160 environmental testing
- MIL-W-5088 wire specifications
- SAE AS50881 wiring standards

## Related Directories

- `../BASELINE/` - Harness assemblies and wire lists
- `../HW_CONFIG/` - Connectors, splices, terminations
- System ATA chapters - For signal definitions (stored in ICD/)

## Validation

Wire specifications validated for:
- Current carrying capacity with derating
- Voltage drop calculations
- Environmental suitability
- EMI/EMC compliance
- Safety margins

---

**Last Updated**: 2024-01-15

**Note**: All personnel working with EWIS data must complete EWIS training.
