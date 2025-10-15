# UTCS Registry
Purpose: immutable linkage of artifacts to UTCS passports.

## Layout
- RECORDS/: signed JSON passports
- SCHEMAS/: JSON Schema for validation
- INDEX/utcs-index.csv: summary table
- INDEX/subsystem-registry.csv: subsystem UTCS URI registry

## Minimal record fields
passport_id, artifact_path, sha256, owner, issued_at, evidence_refs

## Subsystem Registry
The subsystem-registry.csv provides UTCS URI mappings for subsystems across products.

### Fields
- UTCS_URI: Universal traceability URI (utcs://AMPEL360/{ATA_CHAPTER}/{SUBSYSTEM_ID}/{VERSION})
- PRODUCT: Product identifier (e.g., AMPEL360-AIR-T, AMPEL360-SPACE-T)
- ATA_CHAPTER: ATA chapter or STA domain
- SUBSYSTEM_ID: Subsystem identifier
- VERSION: Configuration version
- PATH: Relative path to subsystem directory
- FILENAME: Primary IEF (Interface Exchange File) JSON descriptor
- STATUS: active, deprecated, or archived

## CI
Run `../../12-CI/validate-utcs.py`.
