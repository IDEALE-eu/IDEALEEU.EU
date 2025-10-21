# Security Policy

## Supported Versions
Only the latest minor of each active release line receives security fixes.

| Version | Supported |
|--------:|:---------:|
| 0.1.x   | ✅        |
| < 0.1   | ❌        |

## Report a Vulnerability
- Email: security@ideale-eu.org
- GPG: `0xDEADBEEF` (append key to your report or request ours)
- Please provide: affected version, PoC, impact, environment, and suggested fix if known.
- Do not open public issues for vulnerabilities.

## Coordinated Disclosure
- We confirm receipt within 2 business days.
- We provide a status update within 7 days.
- We target a fix and release within 30 days for High/Critical issues, 90 days for others.
- We credit reporters by handle (opt-out available).

## Scope
- This repository’s code and build/release pipeline.
- Security of dependencies is in scope when our usage creates exploitable risk.

Out of scope: unrelated third-party services and end-user misconfiguration.

## Severity
We use CVSS v3.1. Critical and High severities are prioritized. We may assign CVE IDs for confirmed issues.

## Fix and Release Process
1. Reproduce and triage.
2. Patch in a private branch.
3. Add tests covering the issue.
4. Run security checks (CodeQL, static analysis).
5. Publish a patched release and changelog entry.
6. Notify reporter and, when applicable, ecosystem security channels.

## Dependency and Supply Chain
- Lock and review dependencies.
- Automated alerts: Dependabot + `pip-audit`.
- Signed releases and checksums are attached to GitHub Releases.
- SBOM (when available) is published with each release.

## Safe Reporting Guidelines
- Minimize data exposure. Do not include secrets or personal data.
- Use PoCs that avoid service disruption.

## Security Contacts
- Primary: security@ideale-eu.org
- Backup: maintainers@ideale-eu.org

## Hardening Checklist (maintainers)
- CodeQL enabled for default branch.
- 2FA required for org and maintainers.
- Protected branches with required reviews.
- Release artifacts built from tagged commits in CI.
- Secrets stored in GitHub Actions secrets with least privilege.

## Hall of Fame
We thank researchers who follow this policy. Add your preferred handle in your report to be credited.
```

