# PIPELINES

CI/CD pipeline configurations for FL model development and deployment.

## Purpose

Define pipeline configurations for GitLab CI, Jenkins, or other CI/CD tools (air-gapped compatible).

## Contents

- [**00-README.md**](00-README.md) - This file
- (Pipeline YAML files added as needed, e.g., `.gitlab-ci.yml`, `Jenkinsfile`)

## Example Pipeline Structure

```yaml
stages:
  - build
  - test
  - security
  - deploy_canary
  - deploy_full

build:
  stage: build
  script:
    - docker build -t fl-client:latest .
    - pytest tests/unit --cov=fl_client --cov-report=xml
  coverage: '/TOTAL.*\s+(\d+%)$/'

test:
  stage: test
  script:
    - pytest tests/integration

security:
  stage: security
  script:
    - cyclonedx-bom -o sbom.json
    - trivy image fl-client:latest

deploy_canary:
  stage: deploy_canary
  when: manual  # CCB approval required
  script:
    - ./deploy_canary.sh

deploy_full:
  stage: deploy_full
  when: manual
  script:
    - ./deploy_progressive.sh
```

## Related Documents

- [**../GATES.md**](../GATES.md) - Quality gate definitions
- [**../../09-DEPLOYMENT/**](../../09-DEPLOYMENT/) -  Deployment procedures
