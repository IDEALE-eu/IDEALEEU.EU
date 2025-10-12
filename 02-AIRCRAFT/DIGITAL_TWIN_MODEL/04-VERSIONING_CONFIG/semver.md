# Semantic Versioning

## Version Format
MAJOR.MINOR.PATCH

## Version Increment Rules

### MAJOR version
- Breaking changes to API or model interface
- Changes that require recalibration
- Incompatible state vector changes

### MINOR version
- New features (backward compatible)
- New model capabilities
- Additional outputs or sensors

### PATCH version
- Bug fixes
- Parameter tuning
- Documentation updates

## Version Tags
All versions are tagged in git with format: `v{MAJOR}.{MINOR}.{PATCH}`

## Release Notes
Each version must include:
- Change description
- Migration guide (if applicable)
- Validation results
- Known limitations
