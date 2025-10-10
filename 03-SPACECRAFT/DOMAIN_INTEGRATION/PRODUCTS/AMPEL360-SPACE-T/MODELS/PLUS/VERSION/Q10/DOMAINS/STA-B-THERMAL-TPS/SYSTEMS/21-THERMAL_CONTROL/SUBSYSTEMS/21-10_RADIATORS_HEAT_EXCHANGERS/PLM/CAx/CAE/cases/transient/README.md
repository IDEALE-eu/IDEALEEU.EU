# TRANSIENT — Transient Analysis Cases

## Purpose
Time-dependent thermal analysis for operational mode transitions, eclipse cycles, and thermal cycling.

## Contents
- Operational mode transition analysis
- Eclipse entry and exit transients
- Survival heating profiles
- Power-on thermal transients
- Thermal cycling and fatigue assessment
- Heater control simulation

## File Organization
- One subdirectory per transient scenario
- Include timeline and sequence definition
- Store time-dependent boundary conditions
- Document initial conditions

## Naming Convention
```
21-10-CAE_transient_<scenario>__r<NN>__<STATUS>/
```

Example: `21-10-CAE_transient_eclipse_cycle__r01__RVW/`

## Case Requirements
- Define time-dependent heat loads
- Specify eclipse durations and frequencies
- Document initial thermal state
- Include heater control logic
- Reference operational timelines

## Analysis Outputs
- Temperature evolution over time
- Peak and minimum temperatures
- Thermal cycling amplitude
- Heater duty cycle
- Time to thermal equilibrium

## Typical Scenarios
- Single orbit thermal cycle
- Extended mission operations
- Safe mode survival
- Post-launch commissioning
- End-of-life degraded performance

## Standards
- Follow transient analysis best practices
- Verify thermal rate requirements
- Document time step convergence

---

**Last Updated**: 2025-10-10
