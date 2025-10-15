# CAM - Computer-Aided Manufacturing

[↑ Up to 10-02_STAND_GEOMETRY_MARKINGS](../../../README.md)

Computer-Aided Manufacturing artifacts for airport stand geometry and ground marking standards.

## Purpose

Manufacturing processes, NC programming, tooling, and production planning supporting the development, verification, and deployment of airport stand geometry and ground marking standards.

## Structure

- **NC_PROGRAMS/** - CNC programs and tool paths
- **TOOLING/** - Tool designs and specifications
- **FIXTURES/** - Manufacturing fixtures and jigs
- **PROCESSES/** - Manufacturing process definitions
- **SETUP_SHEETS/** - Machine setup instructions
- **INSPECTION/** - Manufacturing inspection plans
- **REPORTS/** - Manufacturing feasibility studies

## Key Artifacts

- CNC programs (G-code, APT)
- Tool path visualizations
- Manufacturing process sheets
- Tooling and fixture designs
- Machining time estimates

## Naming Convention

```
10-02_{CAX}_{DESCRIPTION}_v{VER}.{ext}
```

## Standards

- Follow applicable CAM standards and best practices
- Ensure traceability to EBOM items
- Maintain configuration control per CM plan
- Document assumptions and validation basis
- Include metadata and revision history

## File Formats

- **NC Programs:** G-code, APT, CLDATA
- **CAM:** Native CAM files (NX, Mastercam, etc.)
- **Tooling:** STEP, PDF drawings
- **Reports:** PDF, Excel

## Traceability

All CAM artifacts must:
- Link to EBOM items in [PLM/EBOM_LINKS.md](../EBOM_LINKS.md)
- Reference requirements and specifications
- Include verification and validation evidence
- Maintain audit trail of changes
- Support configuration management

## References

- [Parent Subsystem README](../../../README.md)
- [EBOM Links](../EBOM_LINKS.md)
- [Configuration Management](../../../../../../../../../../../../../00-PROGRAM/CONFIG_MGMT/)
- [CAM Standards](../../../../../../../../../../../../../00-PROGRAM/STANDARDS/CAM/)

## Related CAx Areas

- [CAD](../CAD/) - Source models for manufacturing
- [CAP](../CAP/) - Manufacturing process planning
- [CAV](../CAV/) - First article inspection
- [CMP](../CMP/) - Manufacturing governance

## Version Control

- Use Git LFS for large binary files
- Include metadata in file headers/properties
- Tag releases with version numbers
- Maintain change logs for major revisions
- Document tool versions and dependencies

---

**Status**: Ready for artifact population  
**Owner**: TBD - Assign CAM lead  
**Last Updated**: 2025-10-11
