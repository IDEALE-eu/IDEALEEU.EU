# 07-COMMON

Shared libraries and cross-domain interface components used by both aircraft and spacecraft.

## Purpose

This directory contains release packages for common components, libraries, and interfaces that are shared across aircraft and spacecraft domains to promote reuse, consistency, and reduce duplication.

## Directory Structure

```
07-COMMON/
├── 00-README.md (this file)
├── SHARED_LIBS/
│   └── [Library releases]
└── CROSS_DOMAIN_INTERFACES/
    └── [Interface releases]
```

## SHARED_LIBS/

### Purpose
Common software libraries, frameworks, and reusable components used by both aircraft and spacecraft systems.

### Contents
- Utility libraries (math, data structures, algorithms)
- Communication protocol implementations
- Data processing libraries
- Simulation frameworks
- Test harnesses and mocks
- Common UI components (if applicable)
- Middleware components

### Naming Convention
```
LIB-[NAME]-[VERSION]/
```

Examples:
- `LIB-MATH-1.2.0/` — Mathematical utilities library
- `LIB-COMMS-2.0.1/` — Communication protocol library
- `LIB-TELEMETRY-1.5.0/` — Telemetry processing library

### Each Library Release Contains
- Library source code or binaries
- API documentation
- Usage examples
- Test suite
- SBOM (dependencies)
- License information
- Release notes
- Integration guide

## CROSS_DOMAIN_INTERFACES/

### Purpose
Interface definitions, protocols, and standards that apply to both aircraft and spacecraft systems, enabling interoperability and commonality.

### Contents
- Common data formats and schemas
- Communication protocol specifications
- Standard message definitions
- API specifications
- Interface adapters and translators
- Validation tools
- Test vectors

### Naming Convention
```
INTF-[NAME]-[VERSION]/
```

Examples:
- `INTF-TELEMETRY-3.0.0/` — Common telemetry format
- `INTF-COMMAND-2.1.0/` — Command protocol
- `INTF-DATA-LINK-1.0.0/` — Data link layer interface

### Each Interface Release Contains
- Interface specification document
- Protocol definitions (schemas, message formats)
- Reference implementation
- Validation test suite
- Compliance checklist
- Release notes
- Migration guide (if interface changed)

## Use Cases

### Common Libraries
1. **Mathematical Operations** — Shared math libraries for navigation, control, simulation
2. **Data Processing** — Common algorithms for sensor fusion, filtering, estimation
3. **Communication** — Unified protocol implementations for ground-to-vehicle links
4. **Logging and Diagnostics** — Common logging formats and analysis tools
5. **Security** — Shared cryptographic libraries and authentication mechanisms

### Cross-Domain Interfaces
1. **Ground Station Interface** — Common ground station communication protocols
2. **Telemetry and Commanding** — Unified TM/TC formats
3. **Mission Planning** — Common mission planning data structures
4. **Health Monitoring** — Unified health and status reporting
5. **Data Archive** — Common data storage and retrieval formats

## Versioning

Common components follow semantic versioning:
- **MAJOR** — Breaking changes (non-backward compatible)
- **MINOR** — New features (backward compatible)
- **PATCH** — Bug fixes (backward compatible)

### Compatibility Matrix

Each release must document compatibility with aircraft and spacecraft releases:

```
LIB-MATH-1.2.0:
  Compatible with:
    - REL-ACFT-1.0.0 and later
    - REL-SC-2.0.0 and later
  Incompatible with:
    - REL-ACFT-0.x.x
    - REL-SC-1.x.x
```

## Release Process

Common components follow standard release workflow per [02-WORKFLOW/RELEASE_WORKFLOW.md](../02-WORKFLOW/RELEASE_WORKFLOW.md) with some adaptations:

### Additional Requirements
1. **Dual-domain verification** — Test with both aircraft and spacecraft systems
2. **Impact analysis** — Assess impact on both domains
3. **Coordinated releases** — Align with aircraft and spacecraft release schedules
4. **Documentation** — Clear usage guidelines for both domains

### Approval
- Configuration Manager
- Aircraft Engineering Lead
- Spacecraft Engineering Lead
- Quality Manager

## Benefits of Common Components

### Advantages
1. **Reduced development cost** — Write once, use in multiple programs
2. **Improved quality** — More testing, wider usage improves maturity
3. **Consistency** — Common behavior across systems
4. **Faster development** — Reuse proven components
5. **Easier maintenance** — Centralized bug fixes and improvements

### Challenges
1. **Dependency management** — Changes affect multiple systems
2. **Compatibility** — Must maintain backward compatibility
3. **Testing burden** — Must test in multiple contexts
4. **Coordination** — Requires cross-domain collaboration

## Configuration Management

### Change Control
Changes to common components require:
1. Impact assessment on both aircraft and spacecraft
2. Approval from both domain leads
3. Regression testing in both contexts
4. Coordinated deployment

### Baseline Control
Common components are baselined independently but referenced by:
- Aircraft releases in [05-AIRCRAFT/](../05-AIRCRAFT/)
- Spacecraft releases in [06-SPACECRAFT/](../06-SPACECRAFT/)

### Dependency Tracking
- Aircraft releases document common component versions in their SBOM
- Spacecraft releases document common component versions in their SBOM
- Dependency matrices maintained in release manifests

## Quality Standards

Common components must meet the most stringent requirements from both domains:
- If aircraft requires DO-178C DAL A and spacecraft requires ECSS Cat A, component must meet both
- Environmental qualification for both flight and space environments (if applicable)
- Security requirements from both domains

## Access Control

- **Development versions** — Internal development teams only
- **Released versions** — Available to both aircraft and spacecraft programs
- **External distribution** — Follows most restrictive export control classification

## Related Documents

- [01-POLICY/RELEASE_POLICY.md](../01-POLICY/RELEASE_POLICY.md)
- [02-WORKFLOW/RELEASE_WORKFLOW.md](../02-WORKFLOW/RELEASE_WORKFLOW.md)
- [05-AIRCRAFT/00-README.md](../05-AIRCRAFT/00-README.md)
- [06-SPACECRAFT/00-README.md](../06-SPACECRAFT/00-README.md)

---

**For questions about common components, contact the Chief Architect or Configuration Manager.**
