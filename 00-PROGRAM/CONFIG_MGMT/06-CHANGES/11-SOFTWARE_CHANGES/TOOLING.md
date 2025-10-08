# Software Tooling

> Location: `CONFIG_MGMT/06-CHANGES/11-SOFTWARE_CHANGES/TOOLING.md`

## Purpose

Track software development tools, qualification status, and impact of tool changes per DO-178C requirements.

## Tool Qualification

Per DO-178C Section 12.2, tools are classified and qualified:

### Tool Qualification Levels

**TQL-1:** Tool output is part of airborne software (e.g., compiler, linker)  
**TQL-2:** Tool automates verification (e.g., test tools)  
**TQL-3:** Tool cannot introduce errors  
**TQL-4:** Tool output is verified  
**TQL-5:** Tool cannot introduce errors that are undetected

## Development Tools

| Tool | Version | Purpose | TQL | Qualification Status |
|------|---------|---------|-----|---------------------|
| GCC | 12.2.0 | Compiler | TQL-1 | Qualified |
| LDRA | 10.5 | Static Analysis | TQL-5 | Qualified |

## Change Impact

Changes to qualified tools require:
- Re-qualification or qualification credit
- Impact analysis on existing software
- ECR/ECO if tool affects baseline

## SBOM (Software Bill of Materials)

Software dependencies tracked for security and configuration management.
