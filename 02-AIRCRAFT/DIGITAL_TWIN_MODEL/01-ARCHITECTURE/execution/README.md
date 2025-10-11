# execution

**📍 [IDEALE-EU](../../../../) > [02-AIRCRAFT](../../../) > [DIGITAL_TWIN_MODEL](../../) > [01-ARCHITECTURE](../) > execution**

Docker containers and orchestration for digital twin deployment.

## Purpose

This directory contains deployment artifacts for running the digital twin in various environments.

## Contents

- **[docker/](docker/)** - Docker containerization
  - **[Dockerfile](docker/Dockerfile)** - Twin runtime container
  - **[compose.yml](docker/compose.yml)** - Multi-container orchestration
- **[orchestration/](orchestration/)** - Execution workflows
  - **[run_local.yaml](orchestration/run_local.yaml)** - Local development execution
  - **[run_hil.yaml](orchestration/run_hil.yaml)** - Hardware-in-the-loop execution

## Deployment Modes

- **Local**: Development and testing on workstation
- **HIL**: Hardware-in-the-loop with real avionics
- **Cloud**: Production deployment in operations center

## Related Documents

- **[../../07-RUNTIME_DEPLOYMENT/](../../07-RUNTIME_DEPLOYMENT/)** - Deployment architecture
- **[../../12-CODE/](../../12-CODE/)** - Implementation code

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2025-01-XX | DevOps Team | Initial execution artifacts |

---

**Status**: Configuration-controlled per `00-PROGRAM/CONFIG_MGMT/`
