# MASS_PROPERTIES — Mass and Inertia Calculations

## Purpose

Mass property calculations including weight, center of gravity, and moments of inertia.

## Content

- Component mass (individual parts)
- Assembly mass (subassembly and total weights)
- Center of gravity (CG location)
- Moments of inertia (Ixx, Iyy, Izz, Ixy, Ixz, Iyz)
- Mass tracking (weight vs. allocation)
- Material breakdown summaries

## File Formats

- `.pdf` — Mass property reports
- `.csv` — Mass property tables
- `.xlsx` — Detailed mass tracking
- CG travel envelopes
- Weight tracking dashboards

## Naming Convention

```
53-10_CHECK_MASS_PROPS_<MODEL-ID>_<DATE>_v<VERSION>.<ext>
```

Examples:
- `53-10_CHECK_MASS_PROPS_FRAME-FR001_20240115_v01.pdf`
- `53-10_CHECK_MASS_PROPS_ASSY-COMPLETE_20240120_v02.csv`

## Accuracy Requirements

- Part mass within ±0.5% of actual
- Assembly mass rollup verified
- CG location within ±5mm
- Material densities from approved specifications
