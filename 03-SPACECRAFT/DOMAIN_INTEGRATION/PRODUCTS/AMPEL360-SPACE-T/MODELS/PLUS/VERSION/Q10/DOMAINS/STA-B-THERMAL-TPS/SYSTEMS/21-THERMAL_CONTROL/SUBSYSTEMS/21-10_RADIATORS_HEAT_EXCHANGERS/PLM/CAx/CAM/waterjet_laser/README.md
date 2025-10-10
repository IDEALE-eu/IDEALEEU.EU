# waterjet_laser — Waterjet & Laser Cutting

## Purpose
DXF/DWG files and NC programs for blanks, masks, gaskets, and sheet cutting using waterjet or laser cutting processes.

## Contents
- DXF/DWG geometry files for cutting
- NC programs for waterjet cutting
- Laser cutting programs
- Blank cutting patterns
- Mask and gasket templates
- Nesting layouts for material optimization

## Related Directories
- **[../setup_sheets/](../setup_sheets/)** — Material and setup specifications
- **[../templates/](../templates/)** — Standard cutting templates
- **[../simulation/](../simulation/)** — Cut path verification

## Guidelines
- Follow naming convention: `21-10-CAM_<part>__opNN__rNN__{WIP|RVW|REL}.<ext>`
- Include material specification and thickness
- Document cutting parameters (pressure, speed, gas type)
- Optimize nesting for material efficiency
- Include lead-in/lead-out strategies
- Verify kerf compensation
- Units: mm, mm/min

## File Formats
- `.dxf` — 2D cutting geometry
- `.dwg` — Alternative CAD format
- `.nc` — Post-processed cutting programs
- `.tap` — Alternative G-code format
- `.pdf` — Cutting specifications and nesting layouts
