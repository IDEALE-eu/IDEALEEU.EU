# exports_rel — Release Exports

## Purpose
Signed release bundles containing verified NC programs, setup sheets, and supporting documentation with checksums for production release.

## Contents
- Release bundle ZIP files
- SHA256 checksum files
- Signed NC programs
- Complete setup documentation packages
- Tool lists and specifications
- Simulation verification reports

## Related Directories
- **[../cnc_3axis/](../cnc_3axis/)** — Released programs
- **[../cnc_5axis/](../cnc_5axis/)** — Released programs
- **[../mill_turn/](../mill_turn/)** — Released programs
- **[../setup_sheets/](../setup_sheets/)** — Setup documentation
- **[../simulation/](../simulation/)** — Verification reports

## Guidelines
- Bundle includes all files needed for production
- Generate SHA256 checksums for verification
- Include version/revision information
- Sign releases with authorized credentials
- NC programs must be in REL (Released) state
- Include simulation verification report
- Document drawing revision and CAD source
- Maintain traceability to CAD geometry

## Naming Convention
```
21-10-CAM_<part>__opNN__rNN__REL_YYYYMMDD.zip
21-10-CAM_<part>__opNN__rNN__REL_YYYYMMDD.sha256
```

## File Formats
- `.zip` — Release bundle archives
- `.sha256` — Checksum verification files
- `.pdf` — Release documentation and signatures
