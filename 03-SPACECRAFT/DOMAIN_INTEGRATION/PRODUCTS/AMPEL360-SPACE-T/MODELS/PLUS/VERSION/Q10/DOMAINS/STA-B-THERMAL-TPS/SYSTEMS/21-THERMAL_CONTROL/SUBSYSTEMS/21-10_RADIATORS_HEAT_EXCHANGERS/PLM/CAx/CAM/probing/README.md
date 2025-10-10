# probing — Probing & Verification

## Purpose
WCS (Work Coordinate System) macros, datum probing programs, and part verification procedures.

## Contents
- Work offset probing macros
- Datum location programs
- Part setup verification cycles
- In-process measurement programs
- Feature location and verification
- Surface probing routines

## Related Directories
- **[../setup_sheets/](../setup_sheets/)** — Setup and probing procedures
- **[../fixtures/](../fixtures/)** — Fixture datum references
- **[../drilling/](../drilling/)** — Hole verification programs

## Guidelines
- Follow naming convention: `21-10-CAM_<part>__opNN__rNN__{WIP|RVW|REL}.<ext>`
- Document probe tip diameter and calibration
- Include expected nominal values and tolerances
- Specify coordinate system relationships (G54-G59)
- Document probe approach and retract distances
- Include probe error handling procedures
- Units: mm

## File Formats
- `.nc` — Probing cycle programs
- `.tap` — Alternative G-code format
- `.xlsx` / `.csv` — Measurement tables and nominal values
- `.pdf` — Probing procedures and documentation
