# ZONES — Zone-Based Organization

## Purpose

This directory organizes JT files by aircraft zones (forward, center, aft). Zone-based organization aligns with aircraft structural divisions and work packages.

## What to Store

- Zone-specific assemblies and parts
- Section-level models
- Zone interface definitions
- Work package deliverables

## Subdirectories

- [`FWD/`](./FWD/) — Forward zone (front section)
- [`CTR/`](./CTR/) — Center zone (mid section)
- [`AFT/`](./AFT/) — Aft zone (rear section)

## Zone Definitions

### Forward Zone (FWD)
- Front frames and structure
- Forward interfaces
- Nose section components

### Center Zone (CTR)
- Mid-fuselage structure
- Main load-bearing frames
- Primary interfaces (wing, landing gear)

### Aft Zone (AFT)
- Rear fuselage structure
- Tail interfaces
- Empennage attachments

## Usage

Use zone organization for:
- Work package management
- Manufacturing sequences
- Subcontractor coordination
- Assembly planning
- Zonal safety analysis
- Maintenance documentation

## Related Directories

- [`../ASSEMBLIES/SUB_ASSEMBLIES/`](../ASSEMBLIES/SUB_ASSEMBLIES/) — Sub-assembly files
- [`../PARTS/`](../PARTS/) — Individual parts
- [`../REVISIONS/`](../REVISIONS/) — Revision management
- [`../README.md`](../README.md) — JT format overview

## Best Practices

- Align zone boundaries with work packages
- Define clear zone interfaces
- Coordinate with manufacturing plan
- Use for progressive build sequences
- Maintain zone-specific BOMs
