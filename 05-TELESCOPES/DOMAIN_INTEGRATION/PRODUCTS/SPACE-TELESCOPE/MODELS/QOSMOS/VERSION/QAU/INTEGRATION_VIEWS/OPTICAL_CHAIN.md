# Optical Chain Integration View

**Systems:** 70 ↔ 76 ↔ 77 ↔ 71

## Overview

This integration view describes the end-to-end optical chain from the primary mirror through to the science instruments, including:
- Primary/secondary/tertiary optical elements (System 70)
- Mirror control and actuation (System 76)
- Alignment sensing and wavefront measurement (System 77)
- Focal plane instruments (System 71)

## Interface Summary

| From System | To System | Interface Type | Description |
|-------------|-----------|----------------|-------------|
| 70-OPTICAL_SUBSYSTEMS | 76-MIRROR_CONTROL | Mechanical/Electrical | Mirror positioning actuators |
| 70-OPTICAL_SUBSYSTEMS | 77-ALIGNMENT_SENSING | Optical | Wavefront sensing optical paths |
| 77-ALIGNMENT_SENSING | 76-MIRROR_CONTROL | Data/Control | Alignment feedback loop |
| 70-OPTICAL_SUBSYSTEMS | 71-INSTRUMENTS_PAYLOADS | Optical | Focal plane illumination |

## Design Notes

TBD - To be populated during system design phase.

## References

- Interface matrices in `/INTERFACE_MATRIX/`
- ICDs: `../../../../../../00-PROGRAM/CONFIG_MGMT/09-INTERFACES/`
