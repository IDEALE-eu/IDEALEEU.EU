# NC_PROGRAMS — Numerical Control Programs

## Purpose
Numerical control (NC) programs for CNC machining operations on the center body fuselage structure.

## Contents
- **[MILLING_3AX/](MILLING_3AX/)** — 3-axis milling programs
- **[MILLING_5AX/](MILLING_5AX/)** — 5-axis milling programs
- **[DRILLING/](DRILLING/)** — Drilling and hole-making programs
- **[TRIMMING_ROUTING/](TRIMMING_ROUTING/)** — Trimming and routing operations
- **[POST/](POST/)** — Post-processor configurations
- **[TEMPLATES/](TEMPLATES/)** — NC program templates and standards

## Related Directories
- **[../PROCESS_PLANS/](../PROCESS_PLANS/)** — Process planning and routings
- **[../SIMULATION/](../SIMULATION/)** — NC program simulation and verification
- **[../VERIFICATION/](../VERIFICATION/)** — NC verification and toolpath QA
- **[../EXPORTS/](../EXPORTS/)** — Production-ready NC exports

## Guidelines
- Use consistent naming conventions
- Include program headers with metadata
- Document tool lists and parameters
- Verify programs before release

## Formats
- G-code (.nc, .gcode)
- APT language (.apt)
- Native CAM formats (Mastercam, NX, etc.)
