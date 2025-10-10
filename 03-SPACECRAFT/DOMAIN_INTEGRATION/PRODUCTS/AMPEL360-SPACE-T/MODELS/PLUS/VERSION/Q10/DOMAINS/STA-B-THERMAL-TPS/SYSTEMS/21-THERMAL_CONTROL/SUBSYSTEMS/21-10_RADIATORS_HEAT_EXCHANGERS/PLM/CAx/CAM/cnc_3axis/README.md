# cnc_3axis — 3-Axis CNC Programs

## Purpose
NC programs and source operations for flat plates, coldplates, and other parts that can be machined using 3-axis milling.

## Contents
- NC files (`.nc`, `.tap`) for 3-axis mill operations
- Source CAM operation files (CAM software native formats)
- Toolpath documentation
- Operation sheets for flat plate machining
- Coldplate milling programs

## Related Directories
- **[../setup_sheets/](../setup_sheets/)** — Setup documentation for these programs
- **[../tool_libraries/](../tool_libraries/)** — Tool definitions used in programs
- **[../simulation/](../simulation/)** — Simulation and verification results
- **[../fixtures/](../fixtures/)** — Fixture documentation

## Guidelines
- Follow naming convention: `21-10-CAM_<part>__opNN__rNN__{WIP|RVW|REL}.<ext>`
- Coordinate systems must match CAD datums (A/B/C)
- All programs must be simulated before release
- Document tool requirements in setup sheets
- Units: mm, mm/min, RPM

## File Formats
- `.nc` — Post-processed G-code for specific controllers
- `.tap` — Alternative G-code format
- CAM native formats (e.g., `.prt`, `.CAMPart`)
- `.pdf` — Operation documentation
