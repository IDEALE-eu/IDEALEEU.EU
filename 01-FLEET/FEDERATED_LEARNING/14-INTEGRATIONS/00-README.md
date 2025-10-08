# 14-INTEGRATIONS

Digital thread links, config management baselines, and MRO feedback loops.

## Purpose

Define integration points between FL system and broader program infrastructure (digital thread, config management, MRO).

## Contents

- [**00-README.md**](00-README.md) - This file
- [**DIGITAL_THREAD_LINKS.md**](DIGITAL_THREAD_LINKS.md) - UTCS anchors, graph IDs
- [**CONFIG_MGMT_BASELINES.md**](CONFIG_MGMT_BASELINES.md) - How FL models join system baseline
- [**MRO_FEEDBACK_LOOP.md**](MRO_FEEDBACK_LOOP.md) - Anomaly → ECR → SCAR → retrain

## Integration Architecture

```
FL System ←→ Digital Thread ←→ CONFIG_MGMT ←→ MRO
```

## Key Integration Points

1. **Digital Thread**: FL models tracked as digital artifacts with UTCS IDs
2. **CONFIG_MGMT**: FL models are configuration items (CIs) in baseline
3. **MRO**: Maintenance feedback informs retraining (fault patterns, NCRs)

## Related Documents

- [**DIGITAL_THREAD_LINKS.md**](DIGITAL_THREAD_LINKS.md) - Digital thread integration
- [**CONFIG_MGMT_BASELINES.md**](CONFIG_MGMT_BASELINES.md) - Baseline integration
- [**MRO_FEEDBACK_LOOP.md**](MRO_FEEDBACK_LOOP.md) - Maintenance feedback
