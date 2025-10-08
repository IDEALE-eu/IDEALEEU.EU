# 10-GOVERNANCE

Governance policies for federated learning experiments, updates, and baseline control.

## Purpose

Define approval workflows, change control, and ethical review processes for FL experiments and model deployments.

## Contents

- [**00-README.md**](00-README.md) - This file
- [**MAL-FE/**](MAL-FE/) -  MAL-FE (Fleet Experiments) approval workflow
- [**MAL-UE/**](MAL-UE/) -  MAL-UE (Update & Enablement) rules
- [**MAL-CB/**](MAL-CB/) -  MAL-CB (Change & Baseline) → CONFIG_MGMT integration
- [**CCB_HANDOFF.md**](CCB_HANDOFF.md) - Configuration Control Board integration
- [**ETHICS_REVIEW.md**](ETHICS_REVIEW.md) - EU AI Act high-risk assessment

## Governance Framework

### Three-Layer Approval

1. **MAL-FE**: Fleet experiments (new algorithms, A/B tests)
2. **MAL-UE**: Model updates and enablement (production deployments)
3. **MAL-CB**: Baseline changes (integration with CONFIG_MGMT)

### Approvers

- **MAL-FE**: AI/ML Team Lead, Fleet Operations Manager
- **MAL-UE**: CCB, Safety Engineering
- **MAL-CB**: Configuration Control Board (CCB)

## Related Documents

- [**CCB_HANDOFF.md**](CCB_HANDOFF.md) - CCB approval process
- [**../09-DEPLOYMENT/**](../09-DEPLOYMENT/) -  Deployment procedures
- [**../../00-PROGRAM/CONFIG_MGMT/**](../../00-PROGRAM/CONFIG_MGMT/) -  Configuration management
