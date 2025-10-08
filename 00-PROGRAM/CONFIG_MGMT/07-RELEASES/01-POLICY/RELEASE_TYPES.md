# Release Types

**Document Number:** CM-POL-RELTYPE  
**Revision:** 1.0  
**Date:** 2025-01-01

## 1. Purpose

Defines the types of releases used throughout the product lifecycle, their characteristics, approval requirements, and use cases.

## 2. Release Type Overview

| Type | Version Pattern | Baseline Gate | Authority | Distribution |
|------|----------------|---------------|-----------|--------------|
| Engineering | 0.x.y or x.y.z-alpha | CDR draft | Engineering Manager | Internal only |
| Certification | x.y.z-beta or x.y.z-rc | PRR/FRR | CCB + Cert Authority | Limited external |
| Production | x.y.z | ORR/EIS | CCB + Cert Authority | Authorized customers |
| Operational | x.y.z | Post-delivery | CCB | Operators/maintainers |
| Emergency Patch | x.y.z+1 | Any | Fast-track CCB | Targeted urgent |

## 3. Engineering Release

### 3.1 Purpose

Early-stage development and validation releases for internal engineering use.

### 3.2 Characteristics

- **Version:** `0.x.y` or `x.y.z-alpha.n`
- **Baseline:** CDR draft or interim engineering baseline
- **Approval:** Engineering Manager or Domain Lead
- **Distribution:** Internal program team only
- **Compliance:** Design verification evidence (partial)
- **Frequency:** As needed, often weekly or bi-weekly

### 3.3 Package Contents

Minimum contents:
- Release notes (engineering focus)
- Design documentation (may be incomplete)
- EBOM (preliminary)
- Test results (unit/integration tests)
- Known issues list
- Next steps/roadmap

Optional:
- Preliminary SBOM
- Partial compliance evidence

### 3.4 Use Cases

- Design validation testing
- Integration testing
- Proof-of-concept demonstrations
- Early supplier evaluation
- Internal design reviews

### 3.5 Restrictions

- **Not for certification** — No regulatory approval
- **Not for production** — Manufacturing not authorized
- **Not for flight/space** — Safety case incomplete
- **Internal use only** — No external distribution without explicit waiver

## 4. Certification Release

### 4.1 Purpose

Formal releases for certification authority review and approval, supporting type certification or flight clearance.

### 4.2 Characteristics

- **Version:** `x.y.z-beta.n` or `x.y.z-rc.n`
- **Baseline:** PRR (aircraft) or FRR (spacecraft)
- **Approval:** CCB + Certification Authority engagement
- **Distribution:** Internal + certification authorities + selected partners
- **Compliance:** Full certification evidence required
- **Frequency:** Per certification plan milestones

### 4.3 Package Contents

Complete certification evidence:
- Release notes (compliance-focused)
- Design documentation (frozen)
- EBOM (finalized)
- MBOM (preliminary or final)
- SBOM (complete, CycloneDX format)
- Compliance matrices:
  - Aircraft: DO-178C, DO-254, DO-160, AS9100, ARP4754A
  - Spacecraft: ECSS-Q-ST-80, ECSS-Q-ST-70, ESA PSS standards
- Test reports (all verification complete)
- Safety case and hazard analysis
- Interface Control Documents (frozen versions)
- Certification plans and reports
- CCB approval package
- Provenance attestations

### 4.4 Sub-Types

#### 4.4.1 Beta Release (x.y.z-beta.n)

- Feature-complete
- All compliance activities in progress
- Certification authority engagement active
- Finding resolution ongoing

#### 4.4.2 Release Candidate (x.y.z-rc.n)

- All findings closed or accepted
- Certification authority pre-approval
- Production-ready pending final signature
- No further changes expected

### 4.5 Use Cases

- Type certificate application (aircraft)
- Flight permit application (spacecraft)
- DO-178C software approval
- DO-254 hardware approval
- Production organization approval (POA)

### 4.6 Restrictions

- **Limited production only** — As authorized by authority
- **Controlled distribution** — Per certification agreement
- **No operational deployment** — Until final approval

## 5. Production Release

### 5.1 Purpose

Formal releases authorized for full-scale production and delivery to customers.

### 5.2 Characteristics

- **Version:** `x.y.z` (stable, no prerelease suffix)
- **Baseline:** ORR (aircraft) or EIS (aircraft entry-into-service)
- **Approval:** CCB + Full certification authority approval
- **Distribution:** Authorized production sites and customers
- **Compliance:** Type certificate or equivalent obtained
- **Frequency:** Per production schedule, typically quarterly or less

### 5.3 Package Contents

Complete production data package:
- Release notes (customer-facing)
- Design documentation (released for production)
- EBOM (configuration-controlled)
- MBOM (released to manufacturing)
- SBOM (signed, verified)
- All compliance evidence (archived)
- Manufacturing work instructions
- Inspection procedures
- Test procedures (acceptance/qualification)
- ICD frozen versions
- Effectivity data (serial number applicability)
- Distribution package with SHA256 verification
- Rollback kit and procedures
- Baseline reference
- Provenance attestations (signed)

### 5.4 Use Cases

- Serial production authorization
- Customer delivery
- Spare parts manufacturing
- Retrofit kits
- Service bulletins

### 5.5 Effectivity

Each production release defines effectivity:
- **Embodied** — Incorporated at factory
- **Mandatory** — Retrofit required by date
- **Optional** — Customer choice

See EFFECTIVITY.csv in release package.

## 6. Operational Release

### 6.1 Purpose

Post-delivery updates for operational aircraft/spacecraft, including software updates, service bulletins, and modifications.

### 6.2 Characteristics

- **Version:** Continues production version sequence (x.y.z)
- **Baseline:** Post-delivery configuration
- **Approval:** CCB + Certification authority (if airworthiness-impacting)
- **Distribution:** Operators, maintenance organizations, MROs
- **Compliance:** Airworthiness directive compliance if applicable
- **Frequency:** As needed for fleet support

### 6.3 Package Contents

Operator-focused:
- Service bulletin or technical directive
- Release notes (operational impact focus)
- Updated SBOM (if software changes)
- Installation instructions
- Inspection/test procedures
- Effectivity (fleet applicability)
- Compliance documentation (AD compliance if applicable)
- Rollback procedures
- Troubleshooting guide

### 6.4 Sub-Types

#### 6.4.1 Scheduled Update

- Planned improvements
- Performance enhancements
- Feature additions
- Standard change control

#### 6.4.2 Service Bulletin

- Non-urgent issue resolution
- Recommended or mandatory compliance
- Standard approval process

#### 6.4.3 Airworthiness Directive (AD) Compliance

- Urgent safety issue
- Mandatory compliance
- Regulatory authority issued
- Expedited approval

### 6.5 Use Cases

- Software updates (avionics, flight control)
- Firmware updates
- Configuration changes
- Inspection interval adjustments
- Parts obsolescence mitigation

## 7. Emergency Patch

### 7.1 Purpose

Urgent fixes for critical safety, security, or operational issues requiring immediate deployment.

### 7.2 Characteristics

- **Version:** Increments PATCH (x.y.z+1)
- **Baseline:** Current operational baseline
- **Approval:** Fast-track CCB per [EMERGENCY_PATCH_WORKFLOW.md](../02-WORKFLOW/EMERGENCY_PATCH_WORKFLOW.md)
- **Distribution:** Targeted urgent deployment
- **Compliance:** Minimum required evidence, full documentation follows
- **Frequency:** Rare, only when critical issue identified

### 7.3 Package Contents

Minimum viable:
- Emergency release notice (severity, impact, required action)
- Patch files with SHA256 verification
- Installation instructions (step-by-step)
- Rollback procedure (must be tested)
- Risk assessment
- Interim approval documentation
- Test results (focused on fix)

Follow-up package (within 30 days):
- Complete compliance documentation
- Full regression test results
- Updated SBOM
- Formal CCB approval
- Lessons learned

### 7.4 Severity Levels

#### 7.4.1 Critical (Deploy within 24 hours)

- Immediate safety hazard
- Security vulnerability actively exploited
- Loss of essential function

#### 7.4.2 High (Deploy within 72 hours)

- Potential safety issue
- Security vulnerability disclosed
- Major operational impact

#### 7.4.3 Medium (Deploy within 7 days)

- Degraded safety margin
- Security risk (not actively exploited)
- Significant operational limitation

### 7.5 Workflow

See [02-WORKFLOW/EMERGENCY_PATCH_WORKFLOW.md](../02-WORKFLOW/EMERGENCY_PATCH_WORKFLOW.md) for detailed process.

### 7.6 Restrictions

- **Targeted deployment only** — Only affected systems/serials
- **Temporary approval** — Full approval required within 30 days
- **Rollback ready** — Must be able to revert if issues arise
- **Monitoring required** — Enhanced surveillance post-deployment

## 8. Special Release Types

### 8.1 Qualification Release

For qualification testing of new designs or suppliers:
- Version: `x.y.z-qual`
- Approval: Engineering Manager + Quality
- Distribution: Test labs, qualification facilities
- Not for production or operation

### 8.2 Retrofit Kit Release

For field modifications of existing units:
- Version: New minor version (x.y+1.0) or patch (x.y.z+1)
- Approval: CCB + Certification (if airworthiness-related)
- Distribution: MROs, operators, field service
- Includes compatibility matrix

### 8.3 Development Kit / SDK Release

For third-party developers (if applicable):
- Version: Separate from product version
- Approval: Engineering Manager + Legal
- Distribution: Authorized developers under NDA
- Includes APIs, documentation, sample code

## 9. Release Type Selection

### 9.1 Decision Tree

```
Is it for production? → NO → Engineering or Certification
                     ↓ YES
Is certification complete? → NO → Certification
                           ↓ YES
Is it in operation? → NO → Production
                    ↓ YES
Is it urgent? → YES → Emergency Patch
              ↓ NO
              → Operational
```

### 9.2 Checklist

Use [04-TEMPLATES/CONFORMITY_CHECKLIST.md](../04-TEMPLATES/CONFORMITY_CHECKLIST.md) to verify release type requirements.

## 10. Related Documents

- [RELEASE_POLICY.md](./RELEASE_POLICY.md) — Governance framework
- [VERSIONING_SCHEME.md](./VERSIONING_SCHEME.md) — Version numbering rules
- [02-WORKFLOW/RELEASE_WORKFLOW.md](../02-WORKFLOW/RELEASE_WORKFLOW.md) — Standard process
- [02-WORKFLOW/EMERGENCY_PATCH_WORKFLOW.md](../02-WORKFLOW/EMERGENCY_PATCH_WORKFLOW.md) — Expedited process

## 11. Revision History

| Rev | Date | Description | Approved By |
|-----|------|-------------|-------------|
| 1.0 | 2025-01-01 | Initial release | Configuration Manager |
