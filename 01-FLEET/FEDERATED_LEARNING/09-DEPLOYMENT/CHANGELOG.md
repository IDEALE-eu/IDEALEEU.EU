# CHANGELOG

FL model deployment changelog (semantic versioning: v1.2.0-fl).

## Version Format

**Major.Minor.Patch-fl**

- **Major**: Breaking changes (input schema, output format)
- **Minor**: New features, improvements (backward-compatible)
- **Patch**: Bug fixes, retraining

## Changelog Entries

### v1.1.0-fl (2024-11-15)

**Added:**
- Engine oil pressure anomaly detection model
- DP-SGD with ε=1.0 for privacy

**Changed:**
- Updated FedAvg to FedProx for heterogeneous clients
- Increased local epochs from 3 to 5

**Fixed:**
- Drift detection false positives (adjusted PSI threshold)

### v1.0.0-fl (2024-11-01)

**Initial Release:**
- Predictive maintenance model for engine bearing wear
- FedAvg algorithm with 30 clients per round
- Weekly training schedule

## Related Documents

- [**../06-MODELS/REGISTRY.md**](../06-MODELS/REGISTRY.md) - Model registry
- [**ROLLOUT_STRATEGY.md**](ROLLOUT_STRATEGY.md) - Deployment procedures
