# UTCS Registry
Purpose: immutable linkage of artifacts to UTCS passports.

## Layout
- RECORDS/: signed JSON passports
- SCHEMAS/: JSON Schema for validation
- INDEX/utcs-index.csv: summary table

## Minimal record fields
passport_id, artifact_path, sha256, owner, issued_at, evidence_refs

## CI
Run `../../12-CI/validate-utcs.py`.
