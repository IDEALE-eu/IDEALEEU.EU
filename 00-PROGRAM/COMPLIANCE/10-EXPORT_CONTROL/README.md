---
area: "00-PROGRAM/COMPLIANCE/10-EXPORT_CONTROL"
owner: "Export Control Officer"
status: "Active"
utcs_anchor: "utcs://PROGRAM/COMPLIANCE/EXPORT"
confidentiality: "Controlled"
---

# 10-EXPORT_CONTROL

Export control compliance including ITAR/EAR classification, technology transfer controls, and screening procedures.

## Purpose

Ensure compliance with International Traffic in Arms Regulations (ITAR), Export Administration Regulations (EAR), and EU dual-use regulations to prevent unauthorized technology transfer and avoid civil/criminal penalties.

## Contents

### Regulatory Framework

#### United States
- **ITAR** (International Traffic in Arms Regulations) - State Department
- **EAR** (Export Administration Regulations) - Commerce Department
- **OFAC** Sanctions - Treasury Department

#### European Union
- **EU Dual-Use Regulation** (2021/821)
- **EU Military List**
- **Member State National Controls**

#### Other Jurisdictions
- UK Export Control
- Canadian Controlled Goods Program
- Australian Defense Trade Controls

### Classification Determinations

#### ITAR Classification
Aircraft/spacecraft items typically ITAR if:
- Military aircraft or space systems
- Specifically designed military components
- Technical data related to defense articles

Categories most relevant:
- **Category VIII**: Aircraft and related articles
- **Category XV**: Spacecraft and related articles
- **Category XXI**: Miscellaneous articles

#### EAR Classification
Commercial items under EAR if:
- Not on US Munitions List (USML)
- Assigned Export Control Classification Number (ECCN)
- May require license depending on destination/end-use

Common ECCNs:
- **9A991**: Aircraft not controlled by 9A001-9A990
- **9D991**: Software for 9A991
- **9E991**: Technology for 9A991

#### EU Dual-Use
Items with both civilian and military applications:
- Annex I items (licensing required)
- Catch-all provisions for weapons of mass destruction
- Torture equipment prohibitions

### Technology Transfer Controls

**Defense Services** (ITAR):
- Technical assistance
- Training
- Engineering support
- Consulting

Require:
- Technical Assistance Agreement (TAA)
- Manufacturing License Agreement (MLA)
- State Department approval

**Deemed Exports**:
- Release of technical data to foreign nationals
- Even in US/EU, requires authorization
- Background checks required

### Screening Procedures

#### Personnel Screening
- Citizenship verification
- Need-to-know determination
- Non-Disclosure Agreements (NDAs)
- Training on export control obligations

#### Visitor Control
- Pre-visit authorization
- Escort requirements
- Controlled area access restrictions
- Technical discussion limitations

#### Partner/Supplier Screening
- Denied Parties List (DPL) check
- Unverified List (UVL) check
- Entity List check
- Specially Designated Nationals (SDN) check

Automated screening via:
- OFAC screening tools
- Bureau of Industry and Security (BIS) tools
- EU sanctions database

## Licensing

### ITAR Licenses
- **DSP-5**: Permanent Export License
- **DSP-61**: Temporary Import License
- **DSP-73**: Temporary Export License
- **TAA/MLA**: Technology transfer agreements

### EAR Licenses
- **License Exception**: Specific exceptions (STA, CIV, etc.)
- **Export License**: Required for controlled items to restricted destinations
- **Re-export Authorization**: For items already exported

### Processing Times
- ITAR: 60-90 days typical, up to 180 days
- EAR: 30-60 days typical
- Plan accordingly in project schedules

## Compliance Program Elements

### Written Program
- Export compliance manual
- Procedures for classification, screening, licensing
- Training requirements
- Audit procedures
- Violation reporting

### Organizational Structure
- Export Control Officer (Empowered Official)
- Deputy ECO
- Regional/functional coordinators
- Engineering liaisons

### Record Keeping
Maintain for 5+ years:
- Classification determinations
- License applications and approvals
- Shipping documents
- Technical assistance records
- Training records
- Screening logs

### Technology Control Plans

For ITAR programs:
- Identify defense articles and technical data
- Physical security measures
- Electronic security measures
- Personnel access controls
- Visitor procedures
- Subcontractor flow-down
- Audits and oversight

## Key Artifacts

### EXPORT_CLASSIFICATION_LIST.xlsx
Master list of program items:
- Part Number/Drawing Number
- Description
- ITAR Category or ECCN
- Rationale/Determination
- Classification Date, Reviewed By
- License Requirements by Destination

### TECHNOLOGY_CONTROL_PLAN.md
Program-specific TCP defining:
- Scope (what articles/data controlled)
- Physical security measures
- Electronic security (encryption, access controls)
- Personnel controls (screening, training)
- Visitor procedures
- Subcontractor requirements
- Audit plan

### FOREIGN_NATIONAL_REGISTER.csv
Personnel with foreign national status:
- Name, Citizenship
- Position, Department
- Access Authorization (approved/denied)
- Approval Authority, Date
- Access Restrictions
- Training Completion

### EXPORT_LICENSE_LOG.csv
Track all licenses:
- License Number, Type (ITAR/EAR)
- Applicant, Recipient, Destination
- Items Covered, Quantity, Value
- Application Date, Approval Date, Expiration
- Status (Pending/Approved/Denied/Expired)
- Shipments Against License

### SCREENING_LOGS/
Document all screening checks:
- Partner/supplier screening results
- Visitor screening results
- Personnel screening results
- Automated screening reports
- Manual review decisions

## Training Requirements

### Initial Training
All personnel:
- Export control overview (ITAR/EAR/EU)
- Company export control policy
- Consequences of violations
- Reporting obligations

Role-specific:
- **Engineers**: Technical data identification, deemed exports
- **Procurement**: Supplier screening, flow-down clauses
- **Shipping**: Licensing, destination control statements
- **HR**: Foreign national hiring procedures

### Refresher Training
- Annual for all personnel with access to controlled technology
- Quarterly for Export Control Officers
- Upon significant regulation changes

## Violations and Voluntary Disclosure

### Potential Violation Indicators
- Shipment to unauthorized destination
- Technology discussion with uncleared foreign national
- Missing license or authorization
- Inadequate screening or record-keeping

### Response Process
1. Immediately stop further violations
2. Notify Export Control Officer
3. Investigate and document facts
4. Assess harm (what was released, to whom)
5. Implement corrective actions
6. Consider Voluntary Self-Disclosure (VSD) to authorities

### Voluntary Self-Disclosure
Benefits of VSD:
- Mitigating factor in penalties
- Demonstrates good faith compliance culture
- Reduces liability exposure

VSD submitted to:
- State Department (ITAR violations)
- Commerce Department (EAR violations)
- EU Member State authority (EU violations)

## Penalties

### Civil Penalties
- ITAR: Up to $1M per violation
- EAR: Up to $300K per violation (adjusted for inflation)
- EU: Varies by member state, can be substantial

### Criminal Penalties
Willful violations:
- Imprisonment up to 20 years
- Fines up to $1M (individuals)
- Corporate criminal liability

### Administrative Sanctions
- Denial of export privileges
- Debarment from government contracts
- Consent agreements with restrictions

## International Collaboration

### Export License Requirements
When collaborating with foreign entities:
- Technical data sharing requires approval
- Hardware shipments require licenses
- Services agreements require authorization
- Joint development needs special arrangements

### Approved Destinations
Licensing easier for allies:
- NATO countries (with caveats)
- Australia, Japan, South Korea (closer security ties)
- Individual agreements (TAA/MLA) case-by-case

### Third-Country Nationals
Special care with:
- Chinese, Russian, Iranian, North Korean nationals
- Technology of concern (space, aviation, AI)
- Enhanced screening and authorization

## Integration Points

- **Security**: [`../../SECURITY/`](../../SECURITY/)
- **Human Resources**: Personnel screening, foreign national hiring
- **Procurement**: Supplier screening, contract flow-down
- **Legal**: Licensing strategy, violation response
- **IT Security**: Electronic data controls

## Related Documents

- Compliance Policies: [`../02-POLICIES/`](../02-POLICIES/)
- Security Program: [`../../SECURITY/`](../../SECURITY/)
- Data Protection: [`../11-DATA_PROTECTION/`](../11-DATA_PROTECTION/)
- Risk Register: [`../09-RISK_COMPLIANCE/`](../09-RISK_COMPLIANCE/)

## Metrics

- Classification determinations (count, backlog)
- License applications (count, approval rate, cycle time)
- Screening hits (count, false positives)
- Training completion rate
- Audit findings (count, severity)
- Violation reports (count, corrective actions)

---

**Owner**: Export Control Officer (Empowered Official)  
**Review**: Continuous for classifications/licenses, Annual program review  
**Approval**: General Counsel, Chief Security Officer

**⚠️ WARNING**: Export control compliance is legally mandated. Violations carry severe civil and criminal penalties including imprisonment. When in doubt, consult Export Control Officer before any international activity.
