# AFT — Aft Zone Components

## Purpose

This directory contains STEP files for components located in the **aft zone** of the center body structure (53-10).

## What to Store

- Aft fuselage frames and bulkheads
- Aft skin panels and doublers
- Tail cone structures
- Aft pressure bulkhead
- Empennage attachment structures
- APU mounting structures (if applicable)

## Zone Definition

The aft zone typically includes:
- Aft of center bulkhead/frame reference
- Empennage attachment region
- Coordinates: [Define specific station/frame numbers]
- Interfaces with tail/empennage systems

## File Organization

Organize by component type within aft zone:
- Parts: Individual aft zone components
- Assemblies: Aft zone sub-assemblies
- Installations: APU, empennage attachments

## Related Directories

- [**../FWD/**](../FWD/) — Forward zone components
- [**../CTR/**](../CTR/) — Center zone components
- [**../../PARTS/**](../../PARTS/) — All parts (zone-agnostic)
- [**../../ASSEMBLIES/**](../../ASSEMBLIES/) — All assemblies
- [**../../INSTALLATION/INTERFACES/**](../../INSTALLATION/INTERFACES/) — Zone interfaces with empennage

## Cross-References

- Zone definition: `00-PROGRAM/CONFIG_MGMT/08-ZONES/`
- Empennage interfaces: `55-EMPENNAGE/` system directory
- APU interfaces: `49-APU/` system directory

## References

- Parent directory: [**../**](../)
- Main STEP README: [**../../README.md**](../../README.md)
