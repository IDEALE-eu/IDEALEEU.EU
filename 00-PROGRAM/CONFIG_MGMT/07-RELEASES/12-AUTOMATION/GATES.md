# Automated Gates

**Document Number:** CM-AUTO-GATES  
**Revision:** 1.0  
**Date:** 2025-01-01

## 1. Purpose

Defines automated quality gates that enforce release standards and prevent defective releases.

## 2. Gate Definitions

### Gate 1: Pre-Commit
**When:** Before code commit  
**Blocking:** Yes

Criteria:
- [ ] Code linting passes (no errors)
- [ ] Unit tests pass (100%)
- [ ] Code formatting complies
- [ ] No secrets detected

### Gate 2: Pre-Merge
**When:** Before merge to main branch  
**Blocking:** Yes

Criteria:
- [ ] All pre-commit gates pass
- [ ] Peer review approved (minimum 1 reviewer)
- [ ] Integration tests pass
- [ ] Code coverage ≥95%
- [ ] Static analysis passes (no critical issues)

### Gate 3: Pre-Release
**When:** Before creating release package  
**Blocking:** Yes

Criteria:
- [ ] All pre-merge gates pass
- [ ] System tests pass (100%)
- [ ] Regression tests pass (100%)
- [ ] Security scan complete (0 critical vulnerabilities)
- [ ] SBOM generated and valid
- [ ] Compliance evidence complete (≥99%)
- [ ] Documentation updated
- [ ] Release notes complete
- [ ] Conformity checklist ≥100%

### Gate 4: Distribution
**When:** Before distributing release  
**Blocking:** Yes

Criteria:
- [ ] All pre-release gates pass
- [ ] CCB approval obtained
- [ ] Package SHA256 verified
- [ ] Digital signature valid
- [ ] Export classification verified
- [ ] Distribution authorized

## 3. Gate Configuration

Example configuration:
```yaml
gates:
  pre_commit:
    blocking: true
    checks:
      - name: linting
        command: "pylint src/"
        threshold: "score >= 9.0"
      - name: unit_tests
        command: "pytest tests/unit/"
        threshold: "pass_rate = 100%"
  
  pre_release:
    blocking: true
    checks:
      - name: security_scan
        command: "trivy scan ."
        threshold: "critical = 0"
      - name: sbom_validation
        command: "cyclonedx-cli validate sbom.json"
        threshold: "valid = true"
```

## 4. Override Authority

Only Configuration Manager can override blocking gates with documented justification.

## 5. Related Documents

- [RELEASE_PIPELINE.md](./RELEASE_PIPELINE.md)
- [00-README.md](./00-README.md)

---

**For gate configuration, contact the Configuration Manager.**
