# mill_turn — Mill-Turn Programs

## Purpose
NC programs for fittings, ports, and LPHX (Loop Heat Pipe eXchanger) components requiring combined milling and turning operations.

## Contents
- NC files (`.nc`, `.tap`) for mill-turn operations
- Source CAM operation files
- Programs for fittings machining
- Port manufacturing programs
- LPHX component operations

## Related Directories
- **[../setup_sheets/](../setup_sheets/)** — Setup documentation for these programs
- **[../tool_libraries/](../tool_libraries/)** — Tool definitions used in programs
- **[../simulation/](../simulation/)** — Simulation and verification results
- **[../fixtures/](../fixtures/)** — Fixture and work holding documentation

## Guidelines
- Follow naming convention: `21-10-CAM_<part>__opNN__rNN__{WIP|RVW|REL}.<ext>`
- Document spindle and sub-spindle operations
- Coordinate systems must match CAD datums
- Verify tool clearances in both milling and turning modes
- Mandatory simulation before first cut
- Units: mm, mm/min, RPM

## File Formats
- `.nc` — Post-processed G-code for mill-turn controllers
- `.tap` — Alternative G-code format
- CAM native formats
- `.pdf` — Operation and setup documentation
