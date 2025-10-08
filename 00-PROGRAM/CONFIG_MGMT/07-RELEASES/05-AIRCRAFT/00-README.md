# 05-AIRCRAFT

Aircraft release packages following ARP4754A, DO-178C, DO-254, DO-160, and AS9100 standards.

## Purpose

This directory contains all formal releases for aircraft configurations, including complete certification evidence, manufacturing data, and operational support packages.

## Directory Structure

Each aircraft release is stored in its own directory following the naming convention:

```
REL-ACFT-[VERSION]/
```

For example:
- `REL-ACFT-0.1.0/` — Engineering release
- `REL-ACFT-1.0.0-rc.1/` — Certification release candidate
- `REL-ACFT-1.0.0/` — Production release
- `REL-ACFT-1.0.1/` — Production patch release

## Release Package Structure

Each release directory contains the following standardized structure:

```
REL-ACFT-x.y.z/
├── RELEASE_NOTES.md
├── MANIFEST.yaml
├── EFFECTIVITY.csv
├── EBOM/
├── MBOM/
├── SBOM/
├── COMPLIANCE/
│   ├── DO-178C/
│   ├── DO-254/
│   ├── DO-160/
│   └── AS9100/
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
Serial number effectivity mapping showing which aircraft this release applies to, effective dates, and modification status (embodied/mandatory/optional).

Format:
```csv
serial_number,effective_date,mod_status,notes
ACFT-001,2025-02-01,embodied,"Factory incorporation"
ACFT-002,2025-03-15,mandatory,"Retrofit required by 2025-03-15"
```

### EBOM/
Engineering Bill of Materials - as-designed configuration including all parts, assemblies, documents, and specifications with revisions.

### MBOM/
Manufacturing Bill of Materials - manufacturing-specific BOM with process routings, tooling, work instructions, and manufacturing specifications.

### SBOM/
Software Bill of Materials in CycloneDX format:
- `sbom.json` — Complete SBOM listing all software components, versions, dependencies, and licenses
- `sbom.json.sig` — Digital signature
- `vulnerabilities.txt` — Vulnerability scan results

### COMPLIANCE/

#### DO-178C/
Software lifecycle data per DO-178C:
- Software plans (PSAC, SDP, SVP, SQAP, SCM Plan)
- Software requirements (SRS)
- Software design (SDD)
- Source code
- Test procedures and results
- Verification and validation reports
- Configuration management records
- Problem reports
- Software accomplishment summary (SAS)
- Software conformity review (SCR) checklist

#### DO-254/
Complex electronic hardware lifecycle data per DO-254:
- Hardware plans (PHAC, HDP, HVP, HQAP, HCM Plan)
- Hardware requirements (HRS)
- Hardware design data
- Verification procedures and results
- Problem reports
- Hardware accomplishment summary (HAS)
- Hardware conformity review (HCR) checklist

#### DO-160/
Environmental qualification per DO-160:
- Test plans
- Test procedures
- Test reports per category (temperature, vibration, EMI, etc.)
- Qualification certificates

#### AS9100/
Quality management system evidence:
- Quality plans
- Work instructions
- Inspection procedures
- First article inspection (FAI) reports
- Process control records
- Supplier quality records
- Non-conformance reports and dispositions

### INTERFACES/ICDs/
Frozen copies of all Interface Control Documents used in this release. Cross-referenced in [03-REGISTERS/RELEASE_ICD_INDEX.csv](../03-REGISTERS/RELEASE_ICD_INDEX.csv).

### SIGNOFF/
- `CCB_APPROVAL.pdf` — Configuration Control Board approval package
- `SIGNATURES.json` — Digital signatures from all approvers
- `HASH_LIST.txt` — Complete list of SHA256 hashes for verification

### DISTRIBUTION/
- `REL-ACFT-x.y.z.zip` — Complete distribution package
- `SHA256SUMS.txt` — Hash file for distribution package
- `SHA256SUMS.txt.sig` — Signed hash file
- `README.txt` — Extraction and verification instructions

### ROLLBACK_KIT/
- `rollback_procedure.md` — Step-by-step rollback instructions
- `scripts/` — Automated rollback scripts (if applicable)
- Previous version artifacts (if needed for rollback)
- Verification procedures post-rollback

### BASELINE_REF/
Symlink to the associated baseline in [04-BASELINES/](../../04-BASELINES/):
- Engineering releases → [04-BASELINES/CDR/](../../04-BASELINES/CDR/)
- Certification releases → [04-BASELINES/PRR/](../../04-BASELINES/PRR/)
- Production releases → [04-BASELINES/ORR/](../../04-BASELINES/ORR/) or [04-BASELINES/EIS/](../../04-BASELINES/EIS/)

### PROVENANCE/
In-toto/SLSA provenance attestations:
- `build.intoto.jsonl` — Build provenance (who built, when, where, how)
- `materials.intoto.jsonl` — Material provenance (source code, dependencies)
- `review.intoto.jsonl` — Review provenance (code reviews, approvals)

## Compliance Standards

### ARP4754A - Aircraft System Development
Guidelines for development of civil aircraft and systems, including:
- Requirements capture and management
- Functional hazard assessment (FHA)
- Safety assessment process
- Verification and validation
- Configuration management

### DO-178C - Software Considerations in Airborne Systems
Software lifecycle requirements per Design Assurance Level (DAL):
- **DAL A** (Catastrophic) — Most rigorous
- **DAL B** (Hazardous)
- **DAL C** (Major)
- **DAL D** (Minor)
- **DAL E** (No Effect) — Minimal requirements

### DO-254 - Hardware Design Assurance
Complex electronic hardware lifecycle requirements per Design Assurance Level.

### DO-160 - Environmental Conditions and Test Procedures
Environmental qualification categories:
- Temperature and altitude
- Temperature variation
- Humidity
- Operational shocks and crash safety
- Vibration
- Waterproofness
- Fluids susceptibility
- Sand and dust
- Fungus
- Salt spray
- Magnetic effect
- Power input
- Voltage spike
- Audio frequency conducted susceptibility
- Induced signal susceptibility
- Radio frequency susceptibility
- Emission of radio frequency energy

### AS9100 - Quality Management Systems
Aerospace QMS requirements building on ISO 9001.

## Release Types for Aircraft

### Engineering Release (0.x.y)
- Internal validation and testing
- Incomplete certification evidence
- Not for flight operations
- Stored in engineering baseline

### Certification Release (x.y.z-rc.n)
- Complete certification evidence
- FAA/EASA engagement active
- Type certificate application submitted
- Limited production authorized

### Production Release (x.y.z)
- Type certificate obtained
- Full production authorized
- Certified for flight operations
- Deliverable to customers

### Operational Release (x.y.z)
- Service bulletins
- Software updates
- Modifications
- Retrofit kits

## Effectivity

Aircraft releases use effectivity to define which tail numbers (serial numbers) are affected:

- **Embodied** — Incorporated during manufacturing
- **Mandatory** — Must be retrofitted by specified date (often driven by Airworthiness Directive)
- **Optional** — Customer discretion

## Certification Authorities

- **FAA** — Federal Aviation Administration (United States)
- **EASA** — European Union Aviation Safety Agency
- **Transport Canada**
- **Other NAAs** — National Aviation Authorities as applicable

## Access Control

- **Engineering releases** — Internal program team only
- **Certification releases** — Program team + certification authorities + selected partners
- **Production releases** — Authorized production sites + customers
- **Operational releases** — Operators + maintenance organizations + MROs

Access logged per [09-DISTRIBUTION/](../09-DISTRIBUTION/).

## Related Documents

- [01-POLICY/RELEASE_POLICY.md](../01-POLICY/RELEASE_POLICY.md)
- [01-POLICY/VERSIONING_SCHEME.md](../01-POLICY/VERSIONING_SCHEME.md)
- [01-POLICY/RELEASE_TYPES.md](../01-POLICY/RELEASE_TYPES.md)
- [02-WORKFLOW/RELEASE_WORKFLOW.md](../02-WORKFLOW/RELEASE_WORKFLOW.md)
- [04-TEMPLATES/](../04-TEMPLATES/)
- [../../04-BASELINES/](../../04-BASELINES/)

## Example Releases

See subdirectories for actual release packages. Each follows the structure defined above.

---

**For questions about aircraft releases, contact the Aircraft Configuration Manager.**
