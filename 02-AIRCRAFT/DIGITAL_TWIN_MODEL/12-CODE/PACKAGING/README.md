# PACKAGING

**📍 [IDEALE-EU](../../../) > [02-AIRCRAFT](../../) > [DIGITAL_TWIN_MODEL](../) > 12-CODE > PACKAGING**

OCI images, SBOMs (Software Bill of Materials), signing scripts.

## Purpose

Packaging artifacts for deployment (containers, SBOMs, signatures).

## Contents

- **Dockerfile.edge** - Dockerfile for edge runtime (lightweight, CPU-only)
- **Dockerfile.ground** - Dockerfile for ground runtime (full, GPU-enabled)
- **sbom/** - Software Bill of Materials (SPDX, CycloneDX)
- **signing/** - GPG signing scripts

## OCI Images

### Edge Runtime Image
- **Base**: Alpine Linux (minimal)
- **Runtime**: ONNX Runtime (CPU)
- **Size**: <500 MB
- **Security**: Distroless, non-root user

### Ground Runtime Image
- **Base**: Ubuntu 22.04
- **Runtime**: ONNX Runtime (GPU), Python 3.11
- **Size**: <2 GB
- **Security**: Regular security updates, vulnerability scanning

## SBOM (Software Bill of Materials)

- **Format**: SPDX 2.3, CycloneDX 1.4
- **Content**: All dependencies (Python packages, system libraries)
- **Tool**: syft, cyclonedx-cli

---

**Status**: Configuration-controlled per `00-PROGRAM/CONFIG_MGMT/`
