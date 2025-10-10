# router_honeycomb — Honeycomb Routing Programs

## Purpose
Panel core routing programs and depth control tables for honeycomb structures in radiator panels.

## Contents
- Routing programs for honeycomb core
- Depth control tables and parameters
- Core pocket machining operations
- Edge routing programs
- Honeycomb cell preservation strategies

## Related Directories
- **[../setup_sheets/](../setup_sheets/)** — Setup documentation
- **[../tool_libraries/](../tool_libraries/)** — Router tool specifications
- **[../simulation/](../simulation/)** — Verification results
- **[../fixtures/](../fixtures/)** — Panel holding fixtures

## Guidelines
- Follow naming convention: `21-10-CAM_<part>__opNN__rNN__{WIP|RVW|REL}.<ext>`
- Document depth control and Z-axis parameters
- Include honeycomb cell size and orientation
- Specify routing speeds and feeds for core material
- Verify vacuum holding and support adequacy
- Units: mm, mm/min, RPM

## File Formats
- `.nc` — Post-processed router programs
- `.tap` — Alternative G-code format
- `.xlsx` / `.csv` — Depth control tables
- `.pdf` — Routing procedures and parameters
