# 06-MODELS

Model registry, model cards, datasets, and Software Bill of Materials (SBOM).

## Purpose

Centralized registry for FL models with versioning, provenance, model cards, and dependency tracking.

## Contents

- **00-README.md** - This file
- **REGISTRY.md** - Model versioning (model_id, hash, FL round, owner)
- **MODEL_CARDS/** - Model cards (intended use, limits, safety disclaimers)
- **DATASETS_INDEX.md** - Dataset provenance, retention, consent
- **SBOM/** - Software Bill of Materials (CycloneDX for ML dependencies)

## Model Lifecycle

1. **Training**: FL rounds produce candidate models
2. **Validation**: Test on holdout dataset (see ../08-VALIDATION_VVP/)
3. **Registration**: Add to REGISTRY.md with metadata
4. **Deployment**: CCB approval, rollout (see ../09-DEPLOYMENT/)
5. **Monitoring**: Drift detection, performance tracking
6. **Retirement**: Archive after 2 years

## Related Documents

- **REGISTRY.md** - Model versioning and metadata
- **MODEL_CARDS/** - Model documentation
- **../09-DEPLOYMENT/** - Deployment procedures
