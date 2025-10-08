# EXPORT

ITAR/EAR export control screening for FL model weights and algorithms.

## Export Control Classification

### ITAR (International Traffic in Arms Regulations)

**Applicability**: TBD (depends on military use of aircraft)

- **Category VIII**: Aircraft and related articles
- **Exemption**: Advisory systems (non-critical)

### EAR (Export Administration Regulations)

**Classification**: ECCN 4E001 (software for aircraft)

- **Export License**: Required for certain jurisdictions
- **Approved Jurisdictions**: EU, US, UK, Canada, Australia, Japan

## Screening Process

### Step 1: Classification Request

- **Submitter**: AI/ML Team
- **Document**: Model architecture, training data provenance, use case
- **Reviewer**: Export Control Officer

### Step 2: Jurisdiction Review

- **Approved**: EU, US, UK (default)
- **Restricted**: China, Russia, Iran, North Korea (case-by-case)

### Step 3: License Application (if required)

- **Timeline**: 4-8 weeks
- **Documentation**: Model technical specs, end-user statement

## Model Weight Export

- **Encryption**: Model weights encrypted in transit and at rest
- **Distribution**: Only to approved jurisdictions (configured in ../../02-ORCHESTRATION/)

## Related Documents

- [**../../01-ARCHITECTURE/FL_TOPOLOGY.md**](../../01-ARCHITECTURE/FL_TOPOLOGY.md) - Geographic distribution
- [**../../02-ORCHESTRATION/CLIENT_SELECTION.md**](../../02-ORCHESTRATION/CLIENT_SELECTION.md) - Jurisdiction filtering
