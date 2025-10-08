# 09-DISTRIBUTION

Internal and external distribution management with security and export classification controls.

## Purpose

This directory manages the controlled distribution of releases, ensuring proper authorization, access control, export compliance, and audit trail for all release distributions.

## Directory Structure

```
09-DISTRIBUTION/
├── 00-README.md (this file)
├── SECURITY.md
├── EXPORT_CLASSIFICATION.md
├── INTERNAL/
│   └── [Internal distribution records and access logs]
└── EXTERNAL/
    └── [External distribution records and export documentation]
```

## Distribution Types

### Internal Distribution
Releases distributed within the program organization:
- Program team members
- Internal engineering teams
- Manufacturing facilities (same company)
- Internal test facilities
- Quality assurance teams

**Authorization:** Configuration Manager or Release Manager  
**Tracking:** INTERNAL/ directory

### External Distribution
Releases distributed outside the organization:
- Customers
- Partners and suppliers
- Certification authorities
- External test facilities
- Maintenance organizations
- Operators

**Authorization:** Configuration Control Board (CCB)  
**Tracking:** EXTERNAL/ directory

## SECURITY.md

### Purpose
Defines security requirements and controls for release distribution.

### Contents
1. **Security Classification** — Classification levels and handling requirements
2. **Access Control** — Authorization and authentication requirements
3. **Distribution Channels** — Approved methods for distribution
4. **Encryption** — Encryption requirements for data at rest and in transit
5. **Integrity Verification** — Hash verification and signature requirements
6. **Audit Logging** — Distribution activity logging requirements
7. **Incident Response** — Procedures for security incidents
8. **Training** — Security awareness requirements

### Security Classifications

#### Internal Only
- Engineering releases
- Pre-certification packages
- Internal test results
- Proprietary design data

**Controls:**
- Accessible only on internal networks
- No external distribution permitted
- Digital Rights Management (DRM) if applicable
- Watermarking for printed copies

#### Controlled Distribution
- Certification releases
- Partner-shared data
- Customer deliverables (non-export controlled)

**Controls:**
- Authorized recipient list (CCB approved)
- Distribution agreement required
- Encrypted transmission
- Acknowledgment of receipt required
- Non-disclosure agreements (NDAs) in place

#### Export Restricted
- Releases containing export-controlled technology
- Dual-use items
- ITAR or EAR restricted content

**Controls:**
- Export license verification before distribution
- Destination country verification
- End-user certification
- Foreign national access control
- Special handling and marking
- Legal review for each distribution

### Distribution Channels

#### Approved Methods
1. **Secure File Transfer** — SFTP, FTPS, encrypted cloud storage
2. **Physical Media** — Encrypted USB, sealed packages with tracking
3. **Configuration Management System** — Role-based access control
4. **Secure Collaboration Platform** — Encrypted, access-controlled

#### Prohibited Methods
- Unencrypted email attachments
- Public file sharing services
- Unencrypted cloud storage
- Untracked physical media
- Personal devices

### Integrity Verification

All distributed releases must include:
1. **SHA256 hash** — For every file and complete package
2. **Digital signature** — Signed with release key
3. **Verification instructions** — Step-by-step verification procedure
4. **Chain of custody** — Documentation from creation to distribution

## EXPORT_CLASSIFICATION.md

### Purpose
Documents export control classification for all releases, ensuring compliance with international trade regulations.

### Contents
1. **Export Control Determination** — ECCN/USML classification
2. **Dual-Use Assessment** — Civilian and military use evaluation
3. **Destination Control** — Authorized countries and end-users
4. **License Requirements** — Export licenses needed
5. **Compliance Procedures** — How to comply with restrictions
6. **Review History** — Classification reviews and updates

### Export Control Regimes

#### United States
- **ITAR** — International Traffic in Arms Regulations
  - USML (US Munitions List) items
  - Defense articles and services
  - State Department jurisdiction
- **EAR** — Export Administration Regulations
  - Dual-use items
  - Commerce Control List (CCL)
  - Commerce Department jurisdiction

#### European Union
- **EU Dual-Use Regulation** — (EC) No 428/2009
- **Common Military List** — Council Common Position 2008/944/CFSP
- **Member State Controls** — National export control laws

#### Wassenaar Arrangement
Multilateral export control regime for conventional arms and dual-use goods and technologies.

### Export Control Classification Number (ECCN)

Format: `XYZ99[.A-E]`
- **X** — Category (0-9)
- **Y** — Product group (A-E)
- **Z** — Type of control (0-9)
- **99** — Specific item
- **[.A-E]** — Sub-category

Examples:
- **9A991** — Aircraft and related items (not ITAR)
- **9D004** — Software for flight control systems
- **7A994** — Integrated circuits

### Classification Process

1. **Technical Review** — Engineering describes technology
2. **Legal Review** — Export compliance attorney determines classification
3. **Justification** — Document rationale for classification
4. **Management Approval** — Configuration Manager and Legal approve
5. **Documentation** — Record in EXPORT_CLASSIFICATION.md
6. **Annual Review** — Re-evaluate classification

### Template for Export Classification

```markdown
## Release: REL-ACFT-1.0.0

### Classification
- **ECCN:** 9A991.a
- **USML:** Not applicable
- **Dual-Use:** Yes
- **Determination Date:** 2025-01-15
- **Reviewed By:** J. Smith, Export Compliance Attorney

### Justification
This release contains aircraft components controlled under ECCN 9A991.a 
for technology related to civil aircraft...

### License Requirements
- **License Exception:** ENC available for most destinations
- **License Required:** Countries in Country Group E:1, E:2

### Authorized Destinations
- EU member states
- NATO countries
- Australia, Japan, South Korea (with Technology Control Plan)

### Restricted Destinations
- Country Group E (embargo countries)
- Denied parties per Consolidated Screening List

### Compliance Notes
- End-user certification required
- Technology Control Plan required for certain destinations
- Annual compliance audit
```

## INTERNAL/ Directory

### Purpose
Tracks internal distributions with access logs.

### Contents
- **ACCESS_LOG.csv** — Who accessed what and when
- **AUTHORIZATION_LIST.csv** — Authorized internal users
- **DISTRIBUTION_RECORDS/** — Records by release
- **ACCESS_REVIEWS/** — Periodic access reviews

### Access Log Format
```csv
timestamp,user_id,user_name,release_id,action,ip_address,notes
2025-01-15T10:30:00Z,user123,John Doe,REL-ACFT-1.0.0,download,192.168.1.100,"Engineering review"
```

### Access Control
- Role-based access control (RBAC)
- Principle of least privilege
- Quarterly access reviews
- Immediate revocation for departing personnel

## EXTERNAL/ Directory

### Purpose
Tracks external distributions with export documentation.

### Contents
- **EXTERNAL_DISTRIBUTION_LOG.csv** — External distributions
- **EXPORT_LICENSES/** — Copy of export licenses
- **END_USER_CERTIFICATES/** — End-user certifications
- **DISTRIBUTION_AGREEMENTS/** — NDAs, licenses, contracts
- **ACKNOWLEDGMENTS/** — Signed receipts

### External Distribution Log Format
```csv
distribution_id,release_id,recipient_org,recipient_country,distribution_date,export_license,acknowledgment_received,notes
EXT-2025-001,REL-ACFT-1.0.0,Airline XYZ,France,2025-01-20,License-Free,2025-01-22,"Customer delivery"
```

### External Distribution Process

1. **Request** — External party requests release
2. **Authorization Check** — Verify authority to receive
3. **Export Check** — Verify export compliance
   - Check destination country
   - Check end-user against denied parties list
   - Verify export license (if required)
   - Obtain end-user certificate (if required)
4. **Agreement** — Execute distribution agreement (NDA, license)
5. **Package Preparation** — Encrypt, sign, verify
6. **Distribution** — Transfer via approved channel
7. **Acknowledgment** — Obtain signed receipt
8. **Logging** — Record in EXTERNAL_DISTRIBUTION_LOG.csv
9. **Follow-up** — Periodic check for compliance

### Required Documentation (External)
- Export license (if required)
- End-user certificate
- Import permit (if required by destination)
- Distribution agreement
- Acknowledgment of receipt
- Handling instructions

## Distribution Approval Authority

### Internal Distribution
- **Engineering releases** — Release Manager
- **Test packages** — Engineering Manager
- **Manufacturing packages** — Manufacturing Manager
- **All internal** — Configuration Manager has override authority

### External Distribution
- **All external distributions** — CCB approval required
- **Export-controlled** — CCB + Legal + Export Compliance
- **Customer deliveries** — CCB + Program Manager
- **Certification authorities** — CCB + Certification Lead

## Compliance and Audit

### Distribution Audits
- Monthly review of distribution logs
- Quarterly access reviews
- Annual export compliance audit
- Immediate review for security incidents

### Metrics
Tracked in [10-METRICS/](../10-METRICS/):
- Number of distributions (internal/external)
- Average authorization time
- Export compliance rate
- Acknowledgment receipt rate
- Security incidents

### Violations
Export control violations are serious and may result in:
- Civil penalties (fines)
- Criminal penalties (imprisonment)
- Debarment from export privileges
- Loss of government contracts
- Reputational damage

**Report immediately to Legal and Export Compliance.**

## Training Requirements

All personnel involved in distribution must complete:
- **Export Control Training** — Annual, mandatory
- **Security Awareness** — Annual, mandatory
- **Distribution Procedures** — Role-specific, annual
- **Incident Response** — As needed

## Emergency Distribution

For emergency patches (see [02-WORKFLOW/EMERGENCY_PATCH_WORKFLOW.md](../02-WORKFLOW/EMERGENCY_PATCH_WORKFLOW.md)):
- Expedited approval process
- Export compliance review still required (cannot be waived)
- Enhanced logging and follow-up
- Retroactive documentation within 30 days

## Related Documents

- [01-POLICY/RELEASE_POLICY.md](../01-POLICY/RELEASE_POLICY.md) — Section 8 on distribution control
- [02-WORKFLOW/RELEASE_WORKFLOW.md](../02-WORKFLOW/RELEASE_WORKFLOW.md) — Phase 5 on distribution
- [03-REGISTERS/DISTRIBUTION_LOG.csv](../03-REGISTERS/DISTRIBUTION_LOG.csv) — Master distribution log
- Export Control Compliance Plan (Legal department)
- Information Security Policy (IT Security)

## Contact

- **Release Manager** — Distribution operations
- **Security Officer** — Security controls and classification
- **Export Compliance** — Export control and licensing
- **Legal** — Agreements and compliance
- **Configuration Manager** — Overall policy and approval

---

**For distribution requests or export questions, contact the Release Manager or Export Compliance Officer.**
