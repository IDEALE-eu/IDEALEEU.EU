# 06-SPACECRAFT

Spacecraft release packages following ECSS standards and ESA production assurance requirements.

## Purpose

This directory contains all formal releases for spacecraft configurations, including complete mission assurance evidence, manufacturing data, and operational support packages.

## Directory Structure

Each spacecraft release is stored in its own directory following the naming convention:

```
REL-SC-[VERSION]/
```

For example:
- `REL-SC-0.1.0/` — Engineering release
- `REL-SC-1.0.0-beta.1/` — Certification/qualification release
- `REL-SC-1.0.0/` — Flight release
- `REL-SC-1.1.0/` — Mission update

## Release Package Structure

Each release directory contains the following standardized structure:

```
REL-SC-x.y.z/
├── RELEASE_NOTES.md
├── MANIFEST.yaml
├── EFFECTIVITY.csv
├── EBOM/
├── MBOM/
├── SBOM/
├── COMPLIANCE/
│   ├── ECSS-Q-ST-80/
│   ├── ECSS-Q-ST-70/
│   ├── RADIATION_TEST/
│   └── ESA_PROD_ASSURANCE/
├── INTERFACES/ICDs/
├── SIGNOFF/
├── DISTRIBUTION/
├── ROLLBACK_KIT/
├── BASELINE_REF/
└── PROVENANCE/
```

## Directory Descriptions

### RELEASE_NOTES.md
Comprehensive release notes documenting changes, features, issues resolved, known limitations, effectivity, and compliance status. Created from [04-TEMPLATES/RELEASE_NOTES_TEMPLATE.md](../04-TEMPLATES/RELEASE_NOTES_TEMPLATE.md).

### MANIFEST.yaml
Complete manifest listing all files, SHA256 hashes, approvals, dependencies, and metadata. Created from [04-TEMPLATES/RELEASE_PACKAGE_MANIFEST.yaml](../04-TEMPLATES/RELEASE_PACKAGE_MANIFEST.yaml).

### EFFECTIVITY.csv
Serial number effectivity mapping showing which spacecraft this release applies to, effective dates, and modification status.

Format:
```csv
serial_number,effective_date,mod_status,notes
SC-FM-001,2025-02-01,embodied,"Flight model - factory configuration"
SC-EM-001,2025-01-15,optional,"Engineering model - test only"
```

### EBOM/
Engineering Bill of Materials - as-designed configuration including all parts, assemblies, documents, and specifications with revisions.

### MBOM/
Manufacturing Bill of Materials - manufacturing-specific BOM with assembly integration sequences, tooling, procedures, and specifications.

### SBOM/
Software Bill of Materials in CycloneDX format:
- `sbom.json` — Complete SBOM listing all software components, versions, dependencies, and licenses
- `sbom.json.sig` — Digital signature
- `vulnerabilities.txt` — Vulnerability scan results

### COMPLIANCE/

#### ECSS-Q-ST-80/
Software product assurance per ECSS-Q-ST-80:
- Software management plan
- Software requirements specification
- Software design specification
- Software validation plan
- Software verification plan
- Software configuration management plan
- Test specifications and reports
- Software user manual
- Software product file

Categories:
- **Category A** — Critical (e.g., flight control, life support)
- **Category B** — Essential (e.g., mission success)
- **Category C** — Useful (e.g., housekeeping)
- **Category D** — Desirable (e.g., ground support)

#### ECSS-Q-ST-70/
Materials, mechanical parts, and processes:
- Material selection and approval
- Parts list and qualification
- Process specifications
- Cleanliness requirements
- EEE parts management
- Mechanical parts management
- Material and process test results

#### RADIATION_TEST/
Radiation testing and qualification:
- Total Ionizing Dose (TID) testing
- Single Event Effects (SEE) testing
- Displacement Damage Dose (DDD) testing
- Radiation environment specification
- Test plans and procedures
- Test reports and qualification certificates
- Radiation analysis and margins

#### ESA_PROD_ASSURANCE/
ESA production assurance evidence per PSS standards:
- Product assurance plan
- Reliability analysis (FMECA, FTA)
- Safety data package
- Software product assurance
- EEE component management
- Inspection and test records
- Non-conformance reports
- Review board minutes (PDR, CDR, QR, AR)

### INTERFACES/ICDs/
Frozen copies of all Interface Control Documents used in this release. Cross-referenced in [03-REGISTERS/RELEASE_ICD_INDEX.csv](../03-REGISTERS/RELEASE_ICD_INDEX.csv).

### SIGNOFF/
- `CCB_APPROVAL.pdf` — Configuration Control Board approval package
- `SIGNATURES.json` — Digital signatures from all approvers
- `HASH_LIST.txt` — Complete list of SHA256 hashes for verification
- `FRR_APPROVAL.pdf` — Flight Readiness Review approval (if applicable)

### DISTRIBUTION/
- `REL-SC-x.y.z.zip` — Complete distribution package
- `SHA256SUMS.txt` — Hash file for distribution package
- `SHA256SUMS.txt.sig` — Signed hash file
- `README.txt` — Extraction and verification instructions

### ROLLBACK_KIT/
- `rollback_procedure.md` — Step-by-step rollback instructions
- `scripts/` — Automated rollback scripts (if applicable)
- Previous version artifacts (if needed for rollback)
- Verification procedures post-rollback
- Ground segment coordination requirements

### BASELINE_REF/
Symlink to the associated baseline in [04-BASELINES/](../../04-BASELINES/):
- Engineering releases → [04-BASELINES/CDR/](../../04-BASELINES/CDR/)
- Flight releases → [04-BASELINES/FRR/](../../04-BASELINES/FRR/)

### PROVENANCE/
In-toto/SLSA provenance attestations:
- `build.intoto.jsonl` — Build provenance (who built, when, where, how)
- `materials.intoto.jsonl` — Material provenance (source code, dependencies)
- `review.intoto.jsonl` — Review provenance (code reviews, approvals)

## Compliance Standards

### ECSS (European Cooperation for Space Standardization)

#### ECSS-E-ST-10C - System Engineering
Space system engineering processes and requirements.

#### ECSS-E-ST-40C - Software
Software engineering for space systems.

#### ECSS-Q-ST-80C - Software Product Assurance
Software product assurance requirements including:
- Software criticality categories (A/B/C/D)
- Verification and validation
- Configuration management
- Problem reporting
- Software quality assurance

#### ECSS-Q-ST-70C - Materials, Mechanical Parts and Processes
Requirements for materials selection, qualification, and control.

#### ECSS-Q-ST-60C - Electrical, Electronic and Electromechanical (EEE) Components
EEE parts selection, procurement, and control.

#### ECSS-M-ST-40C - Configuration and Information Management
Configuration management for space projects.

### ESA PSS Standards (legacy but still referenced)

- **PSS-05-0** — Software engineering standards
- **PSS-01-60** — Software dependability and safety
- **PSS-01-20** — Configuration management

### NASA Standards (if applicable for international cooperation)

- **NASA-STD-8739.8** — Software assurance and software safety
- **NPR 7150.2** — NASA software engineering requirements

### ISO Standards

- **ISO 9001** — Quality management systems
- **ISO/IEC 12207** — Software lifecycle processes

## Release Types for Spacecraft

### Engineering Release (0.x.y)
- Internal validation and testing
- Engineering model (EM) or breadboard testing
- Incomplete qualification evidence
- Not for flight
- Stored in engineering baseline

### Qualification Release (x.y.z-beta.n)
- Qualification model (QM) testing
- Complete qualification evidence
- Environmental testing complete
- Radiation testing complete
- ESA/Agency review in progress

### Flight Release (x.y.z)
- Flight Readiness Review (FRR) passed
- Flight model (FM) qualified and delivered
- Authorized for launch and operations
- Complete mission assurance documentation

### Mission Update (x.y.z)
- In-flight software updates
- Ground segment updates
- Operational procedure changes
- Mission phase transitions

## Spacecraft Model Designations

### Engineering Models (EM)
- Early prototypes
- Design verification
- Software/firmware development
- Interface testing

### Qualification Models (QM)
- Environmental qualification
- Radiation qualification
- Mechanical qualification
- Thermal qualification

### Flight Models (FM)
- Flight-qualified hardware
- Flight software baseline
- Delivered for integration and launch

### Flight Spare (FS)
- Backup flight-qualified unit
- Same configuration as FM

### Protoflight Model (PFM)
- Combined qualification and flight model
- Used when cost/schedule requires single unit

## Effectivity

Spacecraft releases use effectivity to define which models are affected:

- **Embodied** — Incorporated during assembly
- **Mandatory** — Must be updated before launch or mission phase
- **Optional** — Enhanced capability (e.g., science mode optimization)

## Mission Phases

Release effectivity often tied to mission phases:
- **Pre-launch** — Ground integration and testing
- **Launch** — Launch configuration baseline
- **Early Operations (LEOP)** — Launch and Early Orbit Phase
- **Commissioning** — System checkout and calibration
- **Nominal Operations** — Primary mission
- **Extended Mission** — Beyond primary mission
- **End of Life** — Decommissioning

## Space Agencies and Authorities

- **ESA** — European Space Agency
- **NASA** — National Aeronautics and Space Administration (USA)
- **JAXA** — Japan Aerospace Exploration Agency
- **Roscosmos** — Russian space agency
- **CNES** — French space agency (Centre National d'Études Spatiales)
- **DLR** — German space agency (Deutsches Zentrum für Luft- und Raumfahrt)
- **ASI** — Italian space agency (Agenzia Spaziale Italiana)
- **National space agencies** — As applicable for international cooperation

## Radiation Environment

Releases must document radiation qualification:
- **LEO** (Low Earth Orbit) — Van Allen belts, South Atlantic Anomaly
- **GEO** (Geostationary Orbit) — Trapped radiation
- **Deep Space** — Galactic Cosmic Rays (GCR), Solar Particle Events (SPE)
- **Planetary** — Specific environments (e.g., Jupiter radiation belts)

## Access Control

- **Engineering releases** — Internal program team only
- **Qualification releases** — Program team + agencies + selected partners
- **Flight releases** — Authorized integration facilities + mission operations
- **Mission updates** — Mission operations center + approved personnel

Access logged per [09-DISTRIBUTION/](../09-DISTRIBUTION/).

## Export Control Considerations

Space technology often subject to export control:
- **ITAR** (International Traffic in Arms Regulations) — US
- **EAR** (Export Administration Regulations) — US dual-use
- **EU Dual-Use Regulation** — European Union
- **National export control** — Per country

All releases must have export classification documented in [09-DISTRIBUTION/EXPORT_CLASSIFICATION.md](../09-DISTRIBUTION/EXPORT_CLASSIFICATION.md).

## Related Documents

- [01-POLICY/RELEASE_POLICY.md](../01-POLICY/RELEASE_POLICY.md)
- [01-POLICY/VERSIONING_SCHEME.md](../01-POLICY/VERSIONING_SCHEME.md)
- [01-POLICY/RELEASE_TYPES.md](../01-POLICY/RELEASE_TYPES.md)
- [02-WORKFLOW/RELEASE_WORKFLOW.md](../02-WORKFLOW/RELEASE_WORKFLOW.md)
- [04-TEMPLATES/](../04-TEMPLATES/)
- [../../04-BASELINES/](../../04-BASELINES/)
- [../../STANDARDS/03-SPACECRAFT/](../../STANDARDS/03-SPACECRAFT/)

## Example Releases

See subdirectories for actual release packages. Each follows the structure defined above.

---

**For questions about spacecraft releases, contact the Spacecraft Configuration Manager.**
