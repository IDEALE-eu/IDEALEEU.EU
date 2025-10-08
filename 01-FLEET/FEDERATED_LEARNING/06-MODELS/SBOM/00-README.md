# SBOM

Software Bill of Materials (SBOM) for ML dependencies (CycloneDX format).

## Purpose

Track all software dependencies for FL models, including ML frameworks, libraries, and toolchains, for security auditing and compliance.

## Format

CycloneDX SBOM (JSON or XML)

## Contents

- [**00-README.md**](00-README.md) - This file
- (SBOMs generated per model deployment)

## Generation

```bash
# Example: Generate SBOM for PyTorch model
pip install cyclonedx-bom
cyclonedx-bom -o model_sbom.json
```

## Related Documents

- [**../REGISTRY.md**](../REGISTRY.md) - Model versioning
- [**../../13-CI_CD/GATES.md**](../../13-CI_CD/GATES.md) - SBOM checks in CI/CD
