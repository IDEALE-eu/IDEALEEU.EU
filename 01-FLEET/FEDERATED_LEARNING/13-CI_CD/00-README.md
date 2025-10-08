# 13-CI_CD

CI/CD pipelines, quality gates, and automation for FL models.

## Purpose

Define continuous integration and continuous deployment (CI/CD) pipelines for FL model training, validation, and deployment.

## Contents

- **00-README.md** - This file
- **GATES.md** - Quality gates (reproducibility, DP check, SBOM scan)
- **PIPELINES/** - GitLab/Jenkins pipelines (air-gapped compatible)

## CI/CD Stages

### Stage 1: Build

- **Trigger**: Code commit to FL repository
- **Actions**: Lint, unit tests, build Docker image
- **Gates**: 90%+ test coverage, no lint errors

### Stage 2: Test

- **Trigger**: Build stage passed
- **Actions**: Integration tests, HIL/SIL validation
- **Gates**: All tests passed, no regressions

### Stage 3: Security

- **Trigger**: Test stage passed
- **Actions**: SBOM scan, vulnerability scan, DP-SGD check
- **Gates**: No critical vulnerabilities, DP budget within limits

### Stage 4: Deploy (Canary)

- **Trigger**: Security stage passed + CCB approval
- **Actions**: Deploy to canary clients (5 aircraft)
- **Gates**: Canary KPIs passed (see ../../09-DEPLOYMENT/CANARY_ROLLOUTS.md)

### Stage 5: Deploy (Full)

- **Trigger**: Canary stage passed
- **Actions**: Progressive rollout (10% → 25% → 50% → 100%)
- **Gates**: No drift alerts, performance within targets

## Related Documents

- **GATES.md** - Quality gate definitions
- **PIPELINES/** - Pipeline configurations
- **../../09-DEPLOYMENT/** - Deployment procedures
