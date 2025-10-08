# REGISTRY

Federated learning model registry with versioning and metadata.

## Registry Structure

| model_id | version | fl_round | hash (SHA256) | owner | created_at | status |
|----------|---------|----------|---------------|-------|------------|--------|
| pm-engine-bearing | 1.0.0 | 10 | a3f5b8c1... | AI/ML Team | 2024-11-01 | active |
| ad-sensor-drift | 1.0.0 | 15 | d4e6f7a8... | AI/ML Team | 2024-11-05 | canary |

## Versioning

- **Major.Minor.Patch** (Semantic versioning)
- **Major**: Breaking changes (input schema, output format)
- **Minor**: New features (additional inputs, improved accuracy)
- **Patch**: Bug fixes, retraining with same architecture

## Metadata Fields

- **model_id**: Unique identifier (use case + model type)
- **version**: Semantic version (Major.Minor.Patch)
- **fl_round**: Training round number
- **hash**: SHA256 checksum (model weights file)
- **owner**: Team responsible for model
- **created_at**: Timestamp (ISO 8601)
- **status**: draft | canary | active | archived

## Related Documents

- **MODEL_CARDS/** - Model documentation
- **DATASETS_INDEX.md** - Training data provenance
