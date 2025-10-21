# Attestations

## Purpose

This directory contains digital attestations and provenance records for all artifacts in ECR-AMP360-QPL-001. Attestations provide cryptographic proof of artifact integrity, build provenance, and supply chain security.

## Attestation Framework

### SLSA (Supply-chain Levels for Software Artifacts)

ECR-AMP360-QPL-001 targets **SLSA Level 3**:

- **L1**: Build process is fully scripted/automated
- **L2**: Signed provenance with hosted build service
- **L3**: Hardened builds with non-falsifiable provenance
- **L4**: Two-party review + hermetic builds (future goal)

## Attestation Types

### Build Provenance
Records the complete build process:
- Build platform and environment
- Source repository and commit SHA
- Build command and parameters
- Builder identity and timestamp
- Material inputs (dependencies, tools)

### SBOM Attestation
Links SBOMs to artifacts:
- SBOM hash and signature
- Artifact hash
- Attestation of completeness
- Supply chain transparency

### Vulnerability Scan Attestation
Security scan results:
- Scanner identity and version
- Scan timestamp
- Vulnerability count and severity
- Scan provenance

### Test Attestation
Verification results:
- Test suite execution
- Pass/fail status
- Coverage metrics
- Test environment details

### Code Review Attestation
Human review evidence:
- Reviewer identity
- Review timestamp
- Approval status
- Review scope and findings

## File Organization

```
attestations/
├── build-provenance/
│   ├── qpl-ctrl-1.0.0.intoto.jsonl
│   ├── qaoa-optimizer-1.2.3.intoto.jsonl
│   └── vqe-engine-2.0.1.intoto.jsonl
├── sbom-attestations/
│   ├── qpl-ctrl-1.0.0-sbom.att
│   └── qaoa-optimizer-1.2.3-sbom.att
├── vulnerability-scans/
│   ├── qpl-ctrl-1.0.0-vuln.att
│   └── qaoa-optimizer-1.2.3-vuln.att
├── test-results/
│   ├── qpl-ctrl-1.0.0-tests.att
│   └── integration-tests.att
└── code-reviews/
    ├── pr-123-review.att
    └── pre-release-review.att
```

## Attestation Format

### in-toto Attestation
Standard format for SLSA provenance:

```json
{
  "_type": "https://in-toto.io/Statement/v0.1",
  "subject": [
    {
      "name": "qpl-ctrl-firmware",
      "digest": {
        "sha256": "abc123..."
      }
    }
  ],
  "predicateType": "https://slsa.dev/provenance/v0.2",
  "predicate": {
    "builder": {
      "id": "https://github.com/IDEALE-eu/IDEALEEU.EU/.github/workflows/ci.yml"
    },
    "buildType": "https://github.com/Attestations/GitHubActionsWorkflow@v1",
    "invocation": {
      "configSource": {
        "uri": "git+https://github.com/IDEALE-eu/IDEALEEU.EU@refs/heads/main",
        "digest": {
          "sha1": "def456..."
        }
      }
    },
    "metadata": {
      "buildStartedOn": "2025-10-18T00:00:00Z",
      "buildFinishedOn": "2025-10-18T00:15:00Z"
    },
    "materials": [...]
  }
}
```

## Signing

### Keyless Signing (Cosign + Fulcio)
Preferred method using OIDC identity:

```bash
# Sign artifact with keyless cosign
cosign sign --oidc-issuer=https://token.actions.githubusercontent.com \
  ghcr.io/ideale-eu/qpl-ctrl:1.0.0

# Generate attestation
cosign attest --type slsaprovenance \
  --predicate provenance.json \
  ghcr.io/ideale-eu/qpl-ctrl:1.0.0
```

### Key-based Signing
For critical artifacts requiring long-term verification:

```bash
# Generate key pair (one-time)
cosign generate-key-pair

# Sign with private key
cosign sign --key cosign.key \
  ghcr.io/ideale-eu/qpl-ctrl:1.0.0

# Attest with key
cosign attest --key cosign.key \
  --type slsaprovenance \
  --predicate provenance.json \
  ghcr.io/ideale-eu/qpl-ctrl:1.0.0
```

## Verification

### Verify Signature
```bash
# Verify with public key
cosign verify --key cosign.pub \
  ghcr.io/ideale-eu/qpl-ctrl:1.0.0

# Verify keyless signature
cosign verify \
  --certificate-identity-regexp="https://github.com/IDEALE-eu/*" \
  --certificate-oidc-issuer=https://token.actions.githubusercontent.com \
  ghcr.io/ideale-eu/qpl-ctrl:1.0.0
```

### Verify Attestation
```bash
# Verify and display attestation
cosign verify-attestation \
  --type slsaprovenance \
  --key cosign.pub \
  ghcr.io/ideale-eu/qpl-ctrl:1.0.0 | jq
```

### Policy Enforcement
```bash
# Verify against policy (OPA/Rego)
cosign verify-attestation \
  --type slsaprovenance \
  --policy policy.rego \
  ghcr.io/ideale-eu/qpl-ctrl:1.0.0
```

## CI/CD Integration

Attestations are generated automatically:

```yaml
# .github/workflows/ci.yml
- name: Build Artifact
  run: make build

- name: Generate Provenance
  uses: slsa-framework/slsa-github-generator@v1.9.0

- name: Sign Artifact
  run: cosign sign --oidc-issuer=https://token.actions.githubusercontent.com $IMAGE

- name: Generate SBOM Attestation
  run: cosign attest --type spdxjson --predicate sbom.spdx.json $IMAGE

- name: Scan and Attest
  run: |
    grype $IMAGE -o json > vuln-report.json
    cosign attest --type vuln --predicate vuln-report.json $IMAGE
```

## UTCS Anchoring

Attestations are linked to UTCS:
- **UTCS Reference**: `UTCS-AMP360-AIR-T-PROP-QPL-001@1.0.0`
- **Anchor**: `AMP360-AIR-T/PROP/QPL`
- **Signer**: Recorded in UTCS.yaml
- **Timestamp**: ISO 8601 format

## Digital Passport Integration

Attestations are registered in HUELLΔ digital passport:
- **Badge**: `QPL-PROP-OPT`
- **Registry**: Immutable record in digital passport
- **Audit Trail**: Full provenance chain
- **Lifecycle**: Maintained through product lifetime

## Compliance

### Regulatory
- **CS-25.1309**: Traceability and integrity verification
- **EASA**: Software configuration control
- **FAA**: Configuration management evidence

### Industry Standards
- **SLSA**: Supply chain security levels
- **in-toto**: Attestation framework
- **Sigstore**: Transparency and signing infrastructure
- **OpenSSF**: Best practices scorecard

## Attestation Policy

### Build Environment
- Builds must run in GitHub Actions or approved CI
- Build environment must be ephemeral
- No secrets in build logs or artifacts

### Signing Requirements
- All artifacts must be signed
- Keyless signing for automated builds
- Key-based signing for release artifacts
- Signatures must be verifiable via Rekor

### Retention
- Attestations retained for product lifetime
- Transparency logs (Rekor) provide tamper-evidence
- Archive attestations with artifacts

## Security Considerations

### Threat Model
- **Supply chain attacks**: Prevented by SLSA provenance
- **Artifact tampering**: Detected by signature verification
- **Build compromise**: Mitigated by hardened build environment
- **Key compromise**: Limited impact with keyless signing

### Incident Response
1. Identify compromised artifact via attestation
2. Trace provenance to source commit
3. Assess impact scope using SBOM
4. Revoke compromised artifacts
5. Re-issue clean artifacts with new attestations

## Tools

### Required
- **cosign**: Signing and verification
- **in-toto**: Attestation generation
- **rekor-cli**: Transparency log interaction
- **slsa-verifier**: SLSA provenance verification

### Optional
- **kyverno**: Policy enforcement
- **OPA/Rego**: Custom policy engine
- **syft**: SBOM generation
- **grype**: Vulnerability scanning

## References

- **Artifacts**: [../artifacts/](../artifacts/)
- **SBOM**: [../sbom/](../sbom/)
- **UTCS Schema**: [../UTCS.yaml](../UTCS.yaml)
- **CI/CD Pipeline**: [../../../../../../.github/workflows/ci.yml](../../../../../../.github/workflows/ci.yml)
- **SLSA**: https://slsa.dev/
- **in-toto**: https://in-toto.io/
- **Sigstore**: https://www.sigstore.dev/
- **Cosign**: https://github.com/sigstore/cosign
