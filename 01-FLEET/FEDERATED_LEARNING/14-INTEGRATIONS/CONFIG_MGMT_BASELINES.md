# CONFIG_MGMT_BASELINES

How FL models join system baseline (integration with CONFIG_MGMT).

## FL Model as Configuration Item (CI)

FL models are software CIs managed by CONFIG_MGMT:

- **CI Type**: Software (embedded model)
- **CI ID**: FL-MODEL-{use_case}-{version}
- **Baseline**: Aircraft system baseline (e.g., BASELINE-AIRCRAFT-2024Q4)

## Baseline Integration Process

### Step 1: Model Registration

- FL model registered in `../../06-MODELS/REGISTRY.md`
- CI entry created in `00-PROGRAM/CONFIG_MGMT/08-ITEM_MASTER/ITEMS.csv`

### Step 2: ECR/ECO

- ECR submitted to CCB (see [../../10-GOVERNANCE/CCB_HANDOFF.md](../../10-GOVERNANCE/CCB_HANDOFF.md))
- Impact assessment on system baseline
- ECO issued if approved

### Step 3: Baseline Release

- FL model added to system baseline
- Versioned in `00-PROGRAM/CONFIG_MGMT/07-RELEASES/AIRCRAFT/`
- Traceability links updated

## Baseline Contents

**FL Model Baseline Includes:**
- Model architecture and weights (versioned file)
- Training configuration (FL algorithm, hyperparameters)
- Data contracts (input/output schemas)
- Certification evidence (DO-178C, DO-326A)

## Related Documents

- [**../../10-GOVERNANCE/MAL-CB/POLICY.md**](../../10-GOVERNANCE/MAL-CB/POLICY.md) - Baseline control policy
- [**../../../00-PROGRAM/CONFIG_MGMT/**](../../../00-PROGRAM/CONFIG_MGMT/) -  CONFIG_MGMT framework
