# cnc_5axis — 5-Axis CNC Programs

## Purpose
NC programs for manifolds, complex panels, and parts requiring simultaneous 5-axis machining capabilities.

## Contents
- NC files (`.nc`, `.tap`) for 5-axis mill operations
- Source CAM operation files
- Complex toolpath documentation
- Manifold machining programs
- Complex panel operations

## Related Directories
- **[../setup_sheets/](../setup_sheets/)** — Setup documentation for these programs
- **[../tool_libraries/](../tool_libraries/)** — Tool definitions used in programs
- **[../simulation/](../simulation/)** — Simulation and verification results
- **[../fixtures/](../fixtures/)** — Fixture documentation

## Guidelines
- Follow naming convention: `21-10-CAM_<part>__opNN__rNN__{WIP|RVW|REL}.<ext>`
- Coordinate systems must match CAD datums (A/B/C)
- Mandatory collision-free simulation before release
- Document rotary axis setup and work offsets
- Verify tool reach and clearances
- Units: mm, mm/min, RPM

## File Formats
- `.nc` — Post-processed G-code for specific controllers
- `.tap` — Alternative G-code format
- CAM native formats
- `.pdf` — Operation and setup documentation
