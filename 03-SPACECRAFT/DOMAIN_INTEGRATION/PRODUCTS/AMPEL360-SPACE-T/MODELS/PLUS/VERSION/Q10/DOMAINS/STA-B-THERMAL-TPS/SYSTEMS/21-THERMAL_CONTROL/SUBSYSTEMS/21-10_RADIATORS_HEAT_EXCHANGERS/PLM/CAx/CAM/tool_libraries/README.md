# tool_libraries — Tool Libraries

## Purpose
Centralized cutter database, tool holder specifications, and tool assembly definitions for all machining operations.

## Contents
- Tool database files (`.json`, `.xml`)
- Cutter specifications and geometry
- Tool holder definitions
- Tool assembly documentation
- Cutting parameter recommendations
- Tool life and replacement schedules

## Related Directories
- **[../cnc_3axis/](../cnc_3axis/)** — Programs using tools
- **[../cnc_5axis/](../cnc_5axis/)** — Programs using tools
- **[../mill_turn/](../mill_turn/)** — Programs using tools
- **[../setup_sheets/](../setup_sheets/)** — Tool setup documentation

## Guidelines
- Use centralized tool library - no ad-hoc tool edits in NC
- Document tool number, description, and geometry
- Include manufacturer part numbers
- Specify cutting parameters (speed, feed, DOC)
- Document tool holder and stick-out lengths
- Track tool life and replacement intervals
- Maintain version control of tool library

## File Formats
- `.json` — Tool library database
- `.xml` — Alternative tool database format
- `.xlsx` / `.csv` — Tool lists and parameters
- `.pdf` — Tool specifications and documentation
