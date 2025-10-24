# CAE Acceptance Criteria

## Overview

This document defines acceptance criteria for CAE simulations to ensure quality and reliability of results.

## General Criteria

All CAE cases must satisfy:

1. **Metadata Completeness**
   - All required fields in metadata.yaml filled
   - UTCS reference included (if applicable)
   - Revision tracking current

2. **Documentation**
   - Case purpose clearly stated
   - Assumptions documented
   - Boundary conditions described
   - Material properties specified

3. **Reproducibility**
   - All input files committed
   - Scripts and procedures documented
   - Random seeds specified (if applicable)
   - Environment documented

4. **Traceability**
   - Linked to requirements
   - Baseline reference provided
   - Version history maintained

## CFD-Specific Criteria

### Mesh Quality

| Metric | Threshold | Note |
|--------|-----------|------|
| Minimum cell volume | > 0 | No negative volumes |
| Maximum aspect ratio | < 100 | < 10 preferred |
| Maximum skewness | < 0.85 | < 0.5 preferred |
| Minimum orthogonality | > 0.1 | > 0.5 preferred |
| Growth ratio | < 1.3 | Between adjacent cells |

### Convergence

| Metric | Threshold | Note |
|--------|-----------|------|
| Residuals (continuity) | < 1e-4 | < 1e-5 preferred |
| Residuals (momentum) | < 1e-4 | < 1e-5 preferred |
| Residuals (energy) | < 1e-6 | For thermal cases |
| Monitor point stability | < 1% change over 100 iterations | Key metrics |
| Mass balance | < 0.1% error | Conservation |

### Results Quality

| Metric | Threshold | Note |
|--------|-----------|------|
| Negative pressure | None | Check BCs if present |
| Negative temperature | None | Physical impossibility |
| Velocity sanity | < 2× inlet velocity | Check for divergence |
| Temperature sanity | Within bounds | Check material properties |

## FEA-Specific Criteria

### Mesh Quality

| Metric | Threshold | Note |
|--------|-----------|------|
| Element distortion | < 0.7 | For hex elements |
| Aspect ratio | < 20 | < 5 preferred |
| Jacobian | > 0 | Must be positive |
| Warping | < 20° | For shell elements |
| Minimum edge length | > 0.01 mm | Problem-dependent |

### Solution Quality

| Metric | Threshold | Note |
|--------|-----------|------|
| Force balance error | < 0.1% | Equilibrium check |
| Energy balance error | < 1% | For thermal |
| Contact penetration | < 0.01 mm | Check contact settings |
| Unreasonable strain | < 10% | Linear elastic limit |

### Convergence

| Metric | Threshold | Note |
|--------|-----------|------|
| Force residual | < 0.5% | Static analysis |
| Displacement change | < 0.1% | Iteration to iteration |
| Energy error | < 0.1% | Thermal analysis |

### Results Quality

| Metric | Threshold | Note |
|--------|-----------|------|
| Stress singularities | Documented | At sharp corners |
| Deformation magnitude | < 10% span | Check if larger |
| Safety factor | > 1.5 | Design dependent |
| Negative eigenvalues | None | Modal analysis |

## Regression Test Tolerances

Acceptable deviation from baseline:

| Metric | Tolerance | Basis |
|--------|-----------|-------|
| Mass | ±1% | Conservation |
| Energy | ±2% | Accumulated error |
| Peak temperature | ±2°C | Sensor accuracy |
| Mass flow rate | ±3% | Typical variation |
| Maximum stress | ±5% | Mesh sensitivity |
| Displacement | ±3% | Numerical precision |

## Validation Criteria

When comparing against experimental data:

| Metric | Criterion | Note |
|--------|-----------|------|
| R² correlation | > 0.95 | Linear regression |
| RMSE | < 10% of range | Root mean square error |
| MAPE | < 15% | Mean absolute percent error |
| Bias | < 5% | Systematic offset |
| Trend match | Qualitative | Correct physics |

## Performance Criteria

### Runtime

| Case Type | Maximum Runtime | Note |
|-----------|----------------|------|
| Smoke test | 5 minutes | CI requirement |
| Regression test | 1 hour | Daily testing |
| Production case | 24 hours | Typical limit |

### Scalability

| Cores | Minimum Efficiency | Note |
|-------|-------------------|------|
| 1 → 4 | > 90% | Strong scaling |
| 1 → 8 | > 80% | Strong scaling |
| 1 → 16 | > 70% | Strong scaling |
| 1 → 32 | > 60% | Strong scaling |

### Resource Usage

| Resource | Limit | Note |
|----------|-------|------|
| Memory per core | < 4 GB | Typical allocation |
| Disk space | < 100 GB | Per case |
| I/O bandwidth | < 100 MB/s | Average |

## Documentation Requirements

### Minimum Documentation

Each case must include:
- [ ] README.md with case description
- [ ] metadata.yaml with complete fields
- [ ] baseline/metrics.json with required metrics
- [ ] Comments in setup files explaining choices

### Recommended Documentation

- [ ] Mesh independence study
- [ ] Sensitivity analysis
- [ ] Validation report (if experimental data available)
- [ ] User guide for running the case

## Review and Approval

### Peer Review Checklist

Before approval, verify:
- [ ] All acceptance criteria met
- [ ] Documentation complete
- [ ] Results physically reasonable
- [ ] Baseline established
- [ ] Tests pass in CI

### Approval Authority

| Case Criticality | Approver | Note |
|-----------------|----------|------|
| Low (preliminary) | Any CAE engineer | Informal review |
| Medium (design) | Senior CAE engineer | Peer review required |
| High (certification) | CAE lead + independent | Formal review process |

## Non-Conformance

If acceptance criteria not met:
1. Document specific failures
2. Investigate root cause
3. Implement corrective action
4. Re-verify against criteria
5. Update documentation

## Continuous Improvement

Review criteria annually or when:
- New solver versions released
- New analysis types added
- Failures not caught by current criteria
- Industry best practices updated

---

**Version:** 1.0  
**Last Updated:** 2025-10-23  
**Approved by:** CAE Lead
