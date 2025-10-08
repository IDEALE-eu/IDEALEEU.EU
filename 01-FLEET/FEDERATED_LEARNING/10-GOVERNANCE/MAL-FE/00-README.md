# MAL-FE

MAL-FE (Fleet Experiments) approval workflow for FL experiments and A/B tests.

## Purpose

Define approval process for FL experiments, A/B tests, and shadow deployments that do not affect production operations.

## Contents

- [**00-README.md**](00-README.md) - This file
- [**POLICY.md**](POLICY.md) - MAL-FE policy and approval workflow

## Scope

MAL-FE applies to:
- New FL algorithms (FedProx, FedOpt, etc.)
- Hyperparameter tuning experiments
- A/B tests (treatment vs. control)
- Shadow deployments (parallel inference, no actuation)

## Approval Authority

- **AI/ML Team Lead**: Technical approval
- **Fleet Operations Manager**: Operational approval (resource impact)
- **Safety Engineering**: Safety review (if applicable)

## Related Documents

- [**POLICY.md**](POLICY.md) - Detailed approval workflow
- [**../../07-EXPERIMENTS/**](../../07-EXPERIMENTS/) -  Experiment tracking and A/B tests
