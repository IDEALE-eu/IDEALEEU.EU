# GenSTD-I: Core Baselines

## Overview

**GenSTD-I** represents frozen OtC snapshots validated by the Change Advisory Board (CAB). This is the first tier of GenSTD standardization.

## Purpose

GenSTD-I baselines are:
- Frozen snapshots from OtC development phases (α, β, γ, δ, or Ω)
- Validated and approved by CAB
- Ready for use but not yet multi-domain integrated
- The foundation for higher-tier GenSTD baselines

## Characteristics

- **Source**: OtC-[phase]-YYYY-NNNN baselines
- **Approval**: CAB validation required
- **Scope**: Single domain or focused application
- **Stability**: Frozen, changes require new ECR/ECO
- **EHC**: Full compliance mandatory

## Placement Criteria

A baseline qualifies for GenSTD-I when:
- [ ] OtC source identified and documented
- [ ] CAB approval obtained
- [ ] CSA trace complete
- [ ] All EHC artifacts present and validated
- [ ] Provenance metadata complete (hash, RFC, etc.)
- [ ] Baseline frozen (no further OtC changes)

## Usage

GenSTD-I baselines are used for:
- Early adoption by pilot programs
- Foundation for GenSTD-II development
- Reference implementations
- Proof-of-concept validation

## Directory Structure

```
I_core/
├── GenSTD-I-2025-0001/
│   ├── MANIFEST.json
│   ├── SUMMARY.md
│   ├── DECISIONS.md
│   ├── GLOSSARY.md
│   ├── RUNBOOK.md
│   ├── RISKS.md
│   ├── DIAGRAM.svg
│   └── [baseline artifacts]
├── GenSTD-I-2025-0002/
│   └── ...
```

## Transition Path

GenSTD-I baselines can progress to GenSTD-II through:
1. Multi-domain integration
2. Additional QA and Security validation
3. Broader stakeholder review
4. Enhanced compliance documentation

## References

- [GenSTD Overview](../README.md)
- [CAB Process](../../05-CCB/README.md)
- [OtC Methodology](../../GOVERNANCE.md)

---

*GenSTD-I baselines are the first step in formal standardization. They represent validated, frozen configurations ready for controlled deployment.*
