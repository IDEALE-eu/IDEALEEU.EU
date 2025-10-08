# DATA_SHARING_AGREEMENT.md

Data Sharing Agreement between IDEALE Consortium and [Partner Name]

## Agreement Information
Agreement ID: DSA-YYYY-XXXX
Effective Date: YYYY-MM-DD
Expiration Date: YYYY-MM-DD (or "Indefinite")
Version: 1.0

## Parties

### Data Provider
**Organization**: IDEALE Consortium
**Representative**: [Name, Title]
**Contact**: [Email, Phone]
**Address**: [Full Address]

### Data Recipient
**Organization**: [Partner Organization Name]
**Representative**: [Name, Title]
**Contact**: [Email, Phone]
**Address**: [Full Address]

## Purpose and Scope

### Purpose of Data Sharing
Description of why data is being shared and intended use cases:
- Use case 1
- Use case 2
- Use case 3

### Data to be Shared
Specific datasets and data products covered by this agreement:

| Data Product | Description | Refresh Frequency | Format | Classification |
|--------------|-------------|-------------------|--------|----------------|
| Product 1 | Description | Daily | Parquet | INTERNAL |
| Product 2 | Description | Real-time | JSON | CONFIDENTIAL |

### Data Not Included
Explicitly excluded data:
- Excluded data type 1
- Excluded data type 2

## Terms and Conditions

### 1. Permitted Use
The Data Recipient may use the shared data for:
- [ ] Research and development
- [ ] Product development
- [ ] Performance analysis
- [ ] Regulatory compliance
- [ ] Other (specify): _______________

### 2. Prohibited Use
The Data Recipient shall NOT:
- [ ] Share data with third parties without written consent
- [ ] Use data for competitive purposes
- [ ] Reverse-engineer source systems
- [ ] Combine data with other datasets without approval
- [ ] Use data beyond the stated purpose

### 3. Data Classification and Security

**Classification Level**: PUBLIC | INTERNAL | CONFIDENTIAL | RESTRICTED

**Security Requirements**:
- [ ] Encryption at rest (AES-256)
- [ ] Encryption in transit (TLS 1.3)
- [ ] Access control (RBAC/ABAC)
- [ ] Multi-factor authentication
- [ ] Audit logging (7-year retention)
- [ ] Annual security audit

### 4. Export Control
Export Control Classification: NONE | EAR99 | ITAR

**Restrictions** (if applicable):
- Data Recipient must comply with [Export Control Regulations]
- Data may only be accessed from [Approved Countries]
- Personnel with access must have [Clearance Level]

### 5. Privacy and GDPR Compliance

**PII Handling**:
- Data is pseudonymized/anonymized: YES | NO
- GDPR compliance required: YES | NO
- Data Protection Officer contact: [Email]

**Data Subject Rights**:
- Right to erasure process: [Description]
- Right to access process: [Description]

### 6. Data Quality and SLA

**Quality Guarantees**:
- Completeness: > XX%
- Accuracy: [Description]
- Timeliness: Data available within XX hours

**Availability**:
- Target: XX.X% uptime
- Downtime window: [Schedule]

**Support**:
- Support contact: [Email/Phone]
- Response time: [SLA]

## Data Transfer Mechanism

### Transfer Method
- [ ] S3 bucket (read-only access)
- [ ] SFTP server
- [ ] API (RESTful)
- [ ] Kafka stream
- [ ] Other (specify): _______________

### Access Credentials
- Credentials provided by: [Data Provider Contact]
- Credential rotation frequency: [e.g., Quarterly]
- Access revocation process: [Description]

### Transfer Schedule
- Frequency: Real-time | Hourly | Daily | Weekly | Monthly
- Transfer window: [Time range]

## Intellectual Property

### Ownership
- Data Provider retains ownership of all shared data
- Data Recipient may create derivative works (subject to restrictions)
- Derivative work ownership: [To be negotiated]

### Attribution
Data Recipient shall attribute data source as:
"Data provided by IDEALE Consortium under Data Sharing Agreement DSA-YYYY-XXXX"

## Liability and Indemnification

### Limitation of Liability
- Data provided "as is" without warranty
- Data Provider not liable for decisions made using data
- Data Recipient assumes all risk of data use

### Indemnification
Data Recipient shall indemnify Data Provider against:
- Unauthorized disclosure of data
- Misuse of data
- Breach of agreement terms

## Compliance and Audit

### Audit Rights
- Data Provider may audit Data Recipient's use of data annually
- Data Recipient must provide audit cooperation
- Audit notice period: 30 days

### Compliance Reporting
Data Recipient shall report:
- Data breach incidents: Within 24 hours
- Unauthorized access attempts: Within 72 hours
- Compliance status: Quarterly report

## Term and Termination

### Term
This agreement is effective from [Effective Date] and remains in effect until:
- [ ] Expiration date: [Date]
- [ ] Terminated by either party with 90-day notice
- [ ] Indefinite (until terminated)

### Termination Conditions
Agreement may be terminated immediately if:
- Material breach of agreement
- Security incident or data breach
- Change in export control status
- Bankruptcy or insolvency of either party

### Post-Termination Obligations
Upon termination, Data Recipient shall:
- Cease all use of shared data
- Delete or return all data copies within 30 days
- Certify data deletion in writing
- Destroy all derivative works (if required)

## Amendments
- Amendments must be in writing and signed by both parties
- Minor updates (e.g., contact changes) may be made via email

## Dispute Resolution
- Disputes shall be resolved through good-faith negotiation
- Escalation: Senior management meeting within 30 days
- Arbitration: [Jurisdiction and governing law]

## Notices
All notices under this agreement shall be sent to:

**Data Provider**:
[Contact Name]
[Email]
[Phone]

**Data Recipient**:
[Contact Name]
[Email]
[Phone]

## Signatures

### Data Provider
Name: ______________________________
Title: ______________________________
Signature: __________________________
Date: _______________________________

### Data Recipient
Name: ______________________________
Title: ______________________________
Signature: __________________________
Date: _______________________________

## Attachments
- Attachment A: Detailed data product specifications
- Attachment B: Technical integration guide
- Attachment C: Security requirements checklist
- Attachment D: Data classification matrix

## Document Control
| Version | Date       | Changes                        | Author      |
|---------|------------|--------------------------------|-------------|
| 1.0     | YYYY-MM-DD | Initial agreement              | Legal Team  |

---

**CONFIDENTIAL**: This agreement contains confidential information and shall not be disclosed to third parties without written consent.
