# Software Bill of Materials (SBOM)

## Purpose

This directory contains Software Bill of Materials (SBOM) documents for all artifacts in ECR-AMP360-QPL-001. SBOMs provide transparency, security, and supply chain traceability for quantum pipeline integration components.

## SBOM Standards

All SBOMs must comply with:

- **SPDX 2.3+** - Software Package Data Exchange format
- **CycloneDX 1.4+** - Lightweight SBOM standard
- **NTIA Minimum Elements** - Required fields per NTIA guidelines

## Required for Each Artifact

### Firmware Components
- Quantum algorithm libraries (QAOA, VQE)
- Propulsion control firmware modules
- Real-time operating system (RTOS)
- Device drivers and HAL components
- Cryptographic libraries

### Container Images
- Base image and layers
- Runtime dependencies
- Quantum computing frameworks
- Orchestration tools
- Monitoring and logging agents

### Models
- Training frameworks (e.g., TensorFlow, PyTorch)
- Quantum simulation libraries
- Data preprocessing tools
- Model optimization libraries
- Inference engines

## SBOM Minimum Elements (NTIA)

Each SBOM must include:

1. **Supplier Name** - Component vendor/maintainer
2. **Component Name** - Software component identifier
3. **Version** - Specific version/release
4. **Other Unique Identifiers** - Package URLs (purl), CPE, SWID
5. **Dependency Relationships** - Component dependencies
6. **Author of SBOM Data** - Who generated the SBOM
7. **Timestamp** - When SBOM was created

## File Organization

```
sbom/
├── firmware/
│   ├── qpl-ctrl-1.0.0.spdx.json
│   ├── qpl-ctrl-1.0.0.cyclonedx.json
│   └── fallback-logic-1.0.0.spdx.json
├── containers/
│   ├── qaoa-optimizer-1.2.3.spdx.json
│   ├── qaoa-optimizer-1.2.3.cyclonedx.json
│   └── vqe-engine-2.0.1.spdx.json
├── models/
│   ├── thrust-predictor-2.1.0.spdx.json
│   └── energy-optimizer-1.5.2.spdx.json
└── aggregated/
    └── ECR-AMP360-QPL-001-complete.spdx.json
```

## Naming Convention

```
{COMPONENT_NAME}-{VERSION}.{FORMAT}.json
```

**Formats:**
- `spdx.json` - SPDX JSON format
- `cyclonedx.json` - CycloneDX JSON format
- `spdx.xml` - SPDX XML format (optional)

## Generation

SBOMs are automatically generated via CI/CD:

### Build-time Generation
```bash
# SPDX format
syft packages <artifact> -o spdx-json > sbom/component.spdx.json

# CycloneDX format
syft packages <artifact> -o cyclonedx-json > sbom/component.cyclonedx.json
```

### Container Images
```bash
# Scan container and generate SBOM
syft <image>:<tag> -o spdx-json > sbom/container.spdx.json
```

### Firmware
```bash
# Binary analysis for firmware
syft file:<binary> -o spdx-json > sbom/firmware.spdx.json
```

## Validation

SBOMs must be validated before release:

```bash
# Validate SPDX
spdx-tools validate sbom/component.spdx.json

# Check NTIA minimum elements
sbom-tool validate sbom/component.spdx.json --ntia
```

## Vulnerability Scanning

SBOMs are used for continuous vulnerability scanning:

```bash
# Scan SBOM for known vulnerabilities
grype sbom:sbom/component.spdx.json

# Generate vulnerability report
grype sbom:sbom/component.spdx.json -o json > vuln-report.json
```

## SLSA Integration

SBOMs are part of SLSA Level 3 attestations:

1. **Generate SBOM** during artifact build
2. **Sign SBOM** with build provenance
3. **Attach to attestation** in `../attestations/`
4. **Verify** SBOM integrity at deployment

## Supply Chain Security

### Dependency Analysis
- Direct and transitive dependencies
- License compliance (avoid copyleft conflicts)
- Known vulnerability exposure
- End-of-life (EOL) component tracking

### Risk Assessment
- Critical vulnerabilities (CVSS > 7.0)
- Unmaintained components
- Supply chain attacks (e.g., typosquatting)
- Malicious packages

## UTCS Anchoring

Each SBOM is anchored to UTCS:
- **UTCS Reference**: `UTCS-AMP360-AIR-T-PROP-QPL-001@1.0.0`
- **Anchor**: `AMP360-AIR-T/PROP/QPL`
- **Badge**: `QPL-PROP-OPT`
- **Registry**: HUELLΔ digital passport

## Compliance

### Regulatory Requirements
- **CS-25.1309**: Software component traceability
- **EASA**: Software lifecycle documentation
- **FAA**: Configuration management records

### Industry Standards
- **ISO/IEC 5962**: SPDX standard
- **NTIA**: SBOM minimum elements
- **OpenSSF**: Supply chain security best practices

## Aggregated SBOM

An aggregated SBOM combines all component SBOMs:
- Provides complete ECR software inventory
- Used for certification and compliance
- Referenced in digital passport
- Maintained for lifecycle support

## CI/CD Pipeline Integration

```yaml
# .github/workflows/ci.yml
- name: Generate SBOM
  run: syft packages . -o spdx-json > sbom/component.spdx.json

- name: Validate SBOM
  run: sbom-tool validate sbom/component.spdx.json --ntia

- name: Scan Vulnerabilities
  run: grype sbom:sbom/component.spdx.json

- name: Sign SBOM
  run: cosign sign-blob sbom/component.spdx.json
```

## References

- **Artifacts**: [../artifacts/](../artifacts/)
- **Attestations**: [../attestations/](../attestations/)
- **UTCS Schema**: [../UTCS.yaml](../UTCS.yaml)
- **CI/CD Pipeline**: [../../../../../../.github/workflows/ci.yml](../../../../../../.github/workflows/ci.yml)
- **SPDX Specification**: https://spdx.dev/
- **CycloneDX Specification**: https://cyclonedx.org/
- **NTIA Guidelines**: https://www.ntia.gov/sbom
