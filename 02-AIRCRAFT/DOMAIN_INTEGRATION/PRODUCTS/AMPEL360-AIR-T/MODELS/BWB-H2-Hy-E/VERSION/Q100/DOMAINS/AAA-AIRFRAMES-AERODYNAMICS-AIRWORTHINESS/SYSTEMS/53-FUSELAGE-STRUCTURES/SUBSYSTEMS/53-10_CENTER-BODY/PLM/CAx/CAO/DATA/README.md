# DATA — Engineering Databases

## Purpose
Centralized engineering data repositories for materials and loads used in optimization.

## Subdirectories

### [MATERIALS_DB/](MATERIALS_DB/) — Materials Database
Material properties and allowables:
- Composite material properties (CFRP per Q100 config)
- Aluminum alloy properties (secondary structure)
- Temperature-dependent properties
- A-basis and B-basis allowables
- Fatigue data (S-N curves)
- Fracture toughness
- Composite layup definitions
- Material specifications and certifications

**Format**: JSON, XML, CSV, or solver-specific material libraries

### [LOADS_DB/](LOADS_DB/) — Loads Database
Structural loads and load cases:
- Flight loads (limit and ultimate, per Q100 envelope)
- Ground loads (landing, taxiing, towing)
- Pressurization loads (8.6 psi differential per Q100 config)
- Emergency loads (crash, ditching)
- Combined load cases
- Load distributions
- Safety factors per CS-25

**Format**: CSV, HDF5, or solver-specific formats

## Guidelines
- Maintain version control for database entries
- Include source references and traceability
- Document applicable conditions (temperature, moisture)
- Use consistent unit systems (SI preferred)
- Archive test reports supporting data
- Update when new test data available
- Link to certification documents
- Validate data before use in optimization

## Traceability
- Materials data: Link to [Q100/00-CONFIG/RULES.md](../../../../../../../00-CONFIG/RULES.md)
- Loads data: Link to loads analysis reports
- Certifications: Reference [00-PROGRAM/CONFIG_MGMT/](../../../../../../../../../../../../00-PROGRAM/CONFIG_MGMT/)
