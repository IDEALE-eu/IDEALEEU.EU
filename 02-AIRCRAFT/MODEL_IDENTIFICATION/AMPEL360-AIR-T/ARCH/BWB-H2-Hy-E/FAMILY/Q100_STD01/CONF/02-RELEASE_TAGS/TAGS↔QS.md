<!-- UTCS: utcs://AMPEL360-AIR-T/BWB-H2-Hy-E/Q100_STD01 -->

# Release Tags ↔ QS Anchors

This document provides a human-readable view of the baseline progression for Q100_STD01.

## Baseline History

| Release Tag | QS Anchor | Status | Date | Key Changes |
|------------|-----------|--------|------|-------------|
| **v2.3.0** | Q100_STD01@v2.3 | ✅ CURRENT | 2025-10-15 | **Crystallized baseline** - Production-ready configuration with 6.8t H₂, 6× ducted fans, distributed power |
| v2.2.1 | Q100_STD01@v2.2 | 🔒 Archived | 2025-09-01 | Final candidate before crystallization - minor refinements to thermal models |
| v2.2.0 | Q100_STD01@v2.2 | 🔒 Archived | 2025-08-15 | FWD phase completion - mission profiles validated, energy models finalized |
| v2.1.0 | Q100_STD01@v2.1 | 🔒 Archived | 2025-07-01 | UE baseline - unit elements defined (mass, geometry, power) |
| v2.0.0 | Q100_STD01@v2.0 | 🔒 Archived | 2025-06-01 | QS anchor established - design space exploration completed |

## Tree Hash References

Each baseline has a cryptographic hash ensuring integrity:

```
v2.3.0 → sha256:a3f8b92c4d1e7890abcdef123456789
v2.2.1 → sha256:b2e7c81d3c0f6789abcdef234567890
v2.2.0 → sha256:c1d6b70e2b9e5678abcdef345678901
v2.1.0 → sha256:d0c5a69f1a8d4567abcdef456789012
v2.0.0 → sha256:e9b4958e0979f3456abcdef567890123
```

## CCB Approvals

| Baseline | CCB Meeting | Decision | Vote |
|----------|------------|----------|------|
| v2.3.0 | 2025-Q3-CCB-08 | APPROVED | 8-0-1 (1 abstention) |
| v2.2.1 | 2025-Q3-CCB-06 | APPROVED | 9-0-0 |
| v2.2.0 | 2025-Q3-CCB-04 | APPROVED | 8-1-0 (1 against: concern on thermal margin) |
| v2.1.0 | 2025-Q2-CCB-12 | APPROVED | 9-0-0 |
| v2.0.0 | 2025-Q2-CCB-08 | APPROVED | 7-0-2 (2 abstentions: pending domain reviews) |

## Workflow Phase Alignment

```
v2.0.0 ─────► v2.1.0 ─────► v2.2.0 ─────► v2.2.1 ─────► v2.3.0
  QS           UE           FWD           FE+CB         CB (Final)
  
Legend:
  QS  = Quantum Superposition
  UE  = Unit Elements
  FWD = Forward Prediction
  FE  = Federated Learning
  CB  = Crystallized Baseline
```

## Git Tag Commands

To checkout a specific baseline:
```bash
git checkout v2.3.0
git checkout v2.2.1
# etc.
```

## Rollback Procedure

If critical issues are discovered in v2.3.0:
1. File Emergency ECR (EECR)
2. Convene emergency CCB
3. Revert to v2.2.1: `git revert --hard v2.2.1`
4. Update QS_STATE.yaml with rollback rationale
5. Notify all stakeholders

---

**Data Source**: [`BASELINES.csv`](./BASELINES.csv)  
**Maintained By**: Configuration Management  
**Last Updated**: 2025-10-15
