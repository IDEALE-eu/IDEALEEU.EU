# GATES

CI/CD quality gates for FL model pipelines.

## Gate 1: Code Quality

**Checks:**
- [ ] Lint passed (flake8, pylint, mypy)
- [ ] Test coverage ≥ 90%
- [ ] No code smells (SonarQube)

**Enforcement**: Blocking (pipeline fails if not passed)

## Gate 2: Reproducibility

**Checks:**
- [ ] Model training deterministic (fixed random seed)
- [ ] Results reproducible across runs (< 1% variance)
- [ ] Environment pinned (requirements.txt or Dockerfile)

**Enforcement**: Blocking

## Gate 3: Privacy Check

**Checks:**
- [ ] DP-SGD enabled (if configured)
- [ ] ε ≤ ε_budget
- [ ] No PII in training data (automated scan)

**Enforcement**: Blocking

## Gate 4: SBOM Scan

**Checks:**
- [ ] SBOM generated (CycloneDX format)
- [ ] No critical vulnerabilities (CVE scan)
- [ ] All dependencies licensed (Apache, MIT, BSD)

**Enforcement**: Blocking for critical vulnerabilities

## Gate 5: Model Validation

**Checks:**
- [ ] Validation accuracy ≥ target (e.g., AUC ≥ 0.90)
- [ ] Fairness constraints met (bias < 10% gap)
- [ ] Performance within limits (latency, resource usage)

**Enforcement**: Blocking

## Gate 6: CCB Approval

**Checks:**
- [ ] ECR submitted and approved
- [ ] Safety gates passed (see [../../08-VALIDATION_VVP/SAFETY_GATES.md](../../08-VALIDATION_VVP/SAFETY_GATES.md))
- [ ] Traceability complete

**Enforcement**: Blocking (manual approval)

## Related Documents

- [**../../08-VALIDATION_VVP/**](../../08-VALIDATION_VVP/) -  Validation procedures
- [**../../10-GOVERNANCE/CCB_HANDOFF.md**](../../10-GOVERNANCE/CCB_HANDOFF.md) - CCB approval process
