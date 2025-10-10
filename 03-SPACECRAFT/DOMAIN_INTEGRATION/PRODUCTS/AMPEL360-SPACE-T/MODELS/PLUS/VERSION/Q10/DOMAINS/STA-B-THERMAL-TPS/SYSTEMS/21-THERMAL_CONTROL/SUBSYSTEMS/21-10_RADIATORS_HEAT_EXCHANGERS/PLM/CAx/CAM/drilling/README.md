# drilling — Drilling Operations

## Purpose
Pattern cycles, peck parameters, and hole tables for drilling operations in radiator components.

## Contents
- Drilling cycle programs
- Hole pattern definitions
- Peck drilling parameters
- Spot drilling operations
- Tap drilling specifications
- Hole location tables

## Related Directories
- **[../setup_sheets/](../setup_sheets/)** — Drill tool specifications
- **[../tool_libraries/](../tool_libraries/)** — Drill tool definitions
- **[../probing/](../probing/)** — Hole verification procedures
- **[../simulation/](../simulation/)** — Drilling simulation results

## Guidelines
- Follow naming convention: `21-10-CAM_<part>__opNN__rNN__{WIP|RVW|REL}.<ext>`
- Document peck depth and dwell times
- Include hole size, tolerance, and finish requirements
- Specify drill speed and feed rates
- Note coolant requirements
- Document break-edge and deburring cycles
- Units: mm, mm/min, RPM

## File Formats
- `.nc` — Post-processed drilling programs
- `.tap` — Alternative G-code format
- `.xlsx` / `.csv` — Hole tables and coordinates
- `.pdf` — Drilling specifications
