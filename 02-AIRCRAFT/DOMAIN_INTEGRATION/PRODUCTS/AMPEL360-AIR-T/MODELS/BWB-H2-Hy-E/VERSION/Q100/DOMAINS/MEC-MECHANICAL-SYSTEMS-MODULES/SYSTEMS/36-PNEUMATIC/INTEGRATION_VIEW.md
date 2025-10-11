# System: 36-PNEUMATIC

## Overview

This document provides an integration view for the 36-PNEUMATIC system within the MEC-MECHANICAL-SYSTEMS-MODULES domain.

## Purpose

Defines the mechanical system interfaces, subsystem integration, and coordination with other ATA chapters.

## System Interfaces

See [Interface Matrix](./INTERFACE_MATRIX/) directory for detailed CSV files defining interfaces with other systems.

## Subsystems

All subsystems are located in the [SUBSYSTEMS/](./SUBSYSTEMS/) directory. Each subsystem contains:
- README.md with detailed documentation
- PLM/CAx/ with engineering artifacts (CAD, CAE, CAO, CAM, CAI, CAV, CAP, CAS, CMP)
- PLM/EBOM_LINKS.md for BOM references
- META.json and inherit.json for configuration

## Integration Process

1. Review subsystem requirements in respective README files
2. Coordinate interfaces via Interface Matrix
3. Update PLM artifacts in subsystem CAx directories
4. Maintain traceability through EBOM_LINKS

## References

- Main domain: [MEC-MECHANICAL-SYSTEMS-MODULES](../../README.md)
- Program governance: [00-PROGRAM/GOVERNANCE](../../../../../../../../../../../../00-PROGRAM/GOVERNANCE/)
