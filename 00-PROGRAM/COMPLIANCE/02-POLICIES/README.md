---
area: "00-PROGRAM/COMPLIANCE/02-POLICIES"
owner: "Compliance Office"
status: "Active"
utcs_anchor: "utcs://PROGRAM/COMPLIANCE/POLICIES"
confidentiality: "Internal"
---

# 02-POLICIES

Program policies, Standard Operating Procedures (SOPs), and Work Instruction (WI) links for compliance management.

## Purpose

Establish and maintain the policy framework that governs compliance activities across the IDEALEEU.EU program, ensuring consistent interpretation and application of regulatory requirements.

## Contents

### Compliance Policies

#### Aviation Compliance Policy
- DO-178C software development approach
- DO-254 hardware assurance strategy
- ARP4754A systems engineering process
- Certification basis definition
- Relationship with certification authorities (EASA, FAA)

#### Space Compliance Policy
- ECSS tailoring philosophy
- Mission assurance approach
- Safety and reliability requirements
- Planetary protection (if applicable)

#### Quality Management Policy
- AS9100/ISO 9001 implementation
- Non-conformance handling
- CAPA process
- Supplier quality requirements

#### Security & Data Protection Policy
- ISO 27001 implementation
- GDPR compliance approach (see [`REGIONAL_REGULATIONS/EU/GDPR_COMPLIANCE.md`](REGIONAL_REGULATIONS/EU/GDPR_COMPLIANCE.md))
- Cybersecurity for aviation (DO-326A/355A)
- Data classification and handling

#### AI Governance & Ethics Policy
- EU AI Act compliance framework (see [`REGIONAL_REGULATIONS/EU/AI_ACT_COMPLIANCE.md`](REGIONAL_REGULATIONS/EU/AI_ACT_COMPLIANCE.md))
- Risk-based AI classification and management
- Human oversight and transparency requirements
- Ethical AI principles and responsible innovation
- Model governance and bias mitigation

#### Export Control Policy
- ITAR/EAR screening procedures
- Technology transfer controls
- International collaboration guidelines
- Controlled unclassified information (CUI) handling

#### Regional Regulatory Compliance
- **European Union**: GDPR, AI Act, Product Safety, CE marking
- **United States**: NIST frameworks, sector-specific regulations
- **United Kingdom**: UK GDPR, Data Protection Act 2018
- **Asia-Pacific**: China PIPL, Japan APPI, others
- **International**: OECD principles, ISO standards

### Standard Operating Procedures (SOPs)

Links to relevant procedures in `../../QUALITY_QMS/02-PROCEDURES/`:
- **PRO-001**: Document Control
- **PRO-003**: Risk Management and Safety Assessment
- **PRO-004**: Non-Conformance Management
- **PRO-005**: Corrective and Preventive Action (CAPA)
- **PRO-006**: Internal Audit Program
- **PRO-007**: Management Review
- **PRO-010**: Configuration Management
- **PRO-015**: Design Assurance for Complex Hardware
- **PRO-020**: Supplier Quality Management

### Work Instructions (WIs)

Detailed instructions for compliance tasks:
- WI-COMP-001: How to complete compliance matrix entries
- WI-COMP-002: Evidence collection and indexing
- WI-COMP-003: CAPA initiation and closure
- WI-COMP-004: Audit preparation and response
- WI-COMP-005: Deviation and waiver requests
- WI-COMP-006: Export control screening

## Global Regulatory Frameworks

### European Union

#### GDPR - General Data Protection Regulation (EU 2016/679)
**Location**: [`REGIONAL_REGULATIONS/EU/GDPR_COMPLIANCE.md`](REGIONAL_REGULATIONS/EU/GDPR_COMPLIANCE.md)

**Key Requirements**:
- Lawful basis for personal data processing
- Data subject rights (access, rectification, erasure, portability)
- Data Protection Impact Assessments (DPIA) for high-risk processing
- Data breach notification (72 hours to supervisory authority)
- Data Protection Officer (DPO) appointment where required
- Records of Processing Activities (RoPA)
- International data transfer safeguards (SCCs, adequacy decisions)
- Privacy by design and by default

**Penalties**: Up to €20 million or 4% of global annual turnover

**Application to IDEALEEU.EU**:
- Employee data processing
- Customer and partner data
- Aviation passenger data (PNR considerations)
- Space mission crew data
- Research participant data
- Telemetry and operational data containing personal information

#### EU AI Act - Artificial Intelligence Act (EU 2024/1689)
**Location**: [`REGIONAL_REGULATIONS/EU/AI_ACT_COMPLIANCE.md`](REGIONAL_REGULATIONS/EU/AI_ACT_COMPLIANCE.md)

**Key Requirements**:
- **Prohibited AI**: Subliminal manipulation, social scoring, certain biometric uses
- **High-Risk AI**: Conformity assessment, risk management, data governance, transparency, human oversight, accuracy, robustness
- **Limited Risk**: Transparency obligations (chatbots, deepfakes, emotion recognition)
- **General-Purpose AI**: Documentation, copyright compliance, transparency
- **GPAI with Systemic Risk**: Model evaluation, adversarial testing, incident reporting

**Penalties**: Up to €35 million or 7% of global annual turnover (prohibited AI)

**Application to IDEALEEU.EU**:
- Automated flight planning and operations
- Predictive maintenance systems
- Crew assessment and training systems
- Passenger risk assessment and biometric systems
- Autonomous spacecraft navigation
- Decision support systems
- Employment and HR AI systems

#### Other EU Regulations
- **ePrivacy Directive (2002/58/EC)**: Electronic communications privacy
- **NIS2 Directive (EU 2022/2555)**: Network and information security
- **Machinery Regulation (EU 2023/1230)**: Safety of machinery including AI
- **Product Safety Regulation**: General product safety requirements
- **Digital Services Act (EU 2022/2065)**: Online platforms and digital services
- **Cyber Resilience Act (proposed)**: Cybersecurity of products with digital elements

### United States

#### NIST Privacy Framework
**Key Components**:
- Identify: Understanding privacy risks
- Govern: Privacy governance and risk management
- Control: Managing data processing
- Communicate: Transparency and individual participation
- Protect: Data security and resilience

#### NIST AI Risk Management Framework
**Core Functions**:
- **Govern**: Culture, processes, structures for AI risk management
- **Map**: Context understanding and risk identification
- **Measure**: AI system performance and impacts
- **Manage**: Risk prioritization and response

#### Sector-Specific Regulations
- **FAA Regulations**: Aviation safety and certification (14 CFR)
- **ITAR**: International Traffic in Arms Regulations
- **EAR**: Export Administration Regulations
- **FTC Act**: Consumer protection and unfair practices
- **State Privacy Laws**: California CCPA/CPRA, Virginia CDPA, Colorado CPA, etc.
- **NASA Requirements**: Space systems and mission requirements

### United Kingdom

#### UK GDPR and Data Protection Act 2018
**Key Features**:
- Similar to EU GDPR with UK-specific modifications
- Information Commissioner's Office (ICO) as supervisory authority
- Separate adequacy decisions for international transfers
- UK-specific guidance and codes of practice

#### UK AI Regulation Approach
**Principles-Based Framework**:
- Safety, security, and robustness
- Appropriate transparency and explainability
- Fairness
- Accountability and governance
- Contestability and redress

**Sector Regulators**: Existing regulators (CAA, FCA, etc.) apply AI principles

### China

#### Personal Information Protection Law (PIPL)
**Effective**: November 1, 2021

**Key Requirements**:
- Consent as primary legal basis
- Sensitive personal information protections
- Data localization and cross-border transfer restrictions
- Personal information impact assessments
- Individual rights (access, correction, deletion, portability)
- Data protection officer (DPO) appointment

**Application**: Processing of Chinese residents' personal information

#### Other Chinese Regulations
- **Cybersecurity Law (2017)**: Critical information infrastructure protection
- **Data Security Law (2021)**: Data classification and security
- **Algorithm Recommendation Regulations (2022)**: AI recommendation systems
- **Deep Synthesis Regulations (2023)**: Deepfakes and synthetic media

### Japan

#### Act on the Protection of Personal Information (APPI)
**Amended**: 2020, effective 2022

**Key Requirements**:
- Similar structure to GDPR but differences in scope and rights
- Notification and publication requirements
- Individual rights (disclosure, correction, suspension of use)
- Cross-border transfer restrictions
- Security management measures

**Personal Information Protection Commission (PPC)**: Supervisory authority

### Canada

#### Personal Information Protection and Electronic Documents Act (PIPEDA)
**Key Principles**:
- Accountability
- Identifying purposes
- Consent
- Limiting collection, use, disclosure, retention
- Accuracy
- Safeguards
- Openness
- Individual access
- Challenging compliance

#### Artificial Intelligence and Data Act (AIDA)
**Status**: Proposed as part of Bill C-27

**Key Features**:
- Risk-based approach to AI regulation
- High-impact AI systems assessment
- Transparency and explainability
- Human oversight requirements
- Mitigation of bias and harm

### Australia

#### Privacy Act 1988 (with amendments)
**Australian Privacy Principles (APPs)**:
- Open and transparent management of personal information
- Anonymity and pseudonymity
- Collection, use, and disclosure requirements
- Data quality and security
- Individual access and correction rights
- Cross-border disclosure restrictions

#### AI Ethics Framework
**Principles**:
- Human, societal and environmental wellbeing
- Human-centered values
- Fairness
- Privacy protection and security
- Reliability and safety
- Transparency and explainability
- Contestability
- Accountability

### International Frameworks

#### OECD AI Principles
1. Inclusive growth, sustainable development and well-being
2. Human-centered values and fairness
3. Transparency and explainability
4. Robustness, security and safety
5. Accountability

#### ISO/IEC Standards
- **ISO/IEC 27001**: Information Security Management
- **ISO/IEC 27701**: Privacy Information Management
- **ISO/IEC 42001**: AI Management System (in development)
- **ISO/IEC 23894**: AI Risk Management
- **ISO/IEC 27562**: Cybersecurity for AI systems

#### Aviation-Specific International Standards
- **ICAO Annex 6**: Operation of Aircraft
- **ICAO Annex 8**: Airworthiness of Aircraft
- **ICAO Doc 9859**: Safety Management Manual
- **EASA Certification Specifications**: CS-25, CS-E
- **DO-178C**: Software for Airborne Systems
- **DO-254**: Hardware for Airborne Systems
- **ARP4754A**: Development of Civil Aircraft and Systems

#### Space-Specific International Standards
- **ECSS Standards**: European Cooperation for Space Standardization
- **NASA Standards**: NPR 7150.2, NPR 8705.2, etc.
- **ISO 14300**: Space Systems Program Management
- **ISO 17770**: Space Systems Quality Management
- **CCSDS Standards**: Consultative Committee for Space Data Systems

## Regulatory Compliance Matrix

### Cross-Regional Comparison

| Aspect | EU | US | UK | China | Japan | Canada |
|--------|----|----|----|----|----|----|
| **Data Protection** | GDPR | State laws, FTC | UK GDPR | PIPL | APPI | PIPEDA |
| **AI Regulation** | AI Act | NIST Framework | Principles | Multiple laws | Guidelines | AIDA (proposed) |
| **Enforcement** | High fines | Civil/criminal | High fines | High fines | Moderate | Moderate |
| **Extraterritoriality** | Strong | Limited | Strong | Strong | Limited | Limited |
| **DPO Required** | Often | Rare | Often | Often | No | No |
| **DPIA/PIA** | Yes (GDPR) | Recommended | Yes | Yes | Recommended | Recommended |
| **Breach Notification** | 72 hours | Varies by state | 72 hours | Immediately | Without delay | Feasible soon as possible |
| **Data Localization** | No | No | No | Yes | No | No |
| **AI Risk Classification** | 4 tiers | Risk-based | Sector-based | Use-based | Sector-based | Risk-based |

### Industry-Specific Considerations

#### Aviation Industry
**Regulatory Stack**:
1. **Aviation Safety**: EASA CS-25, FAA 14 CFR Part 25, ICAO Annexes
2. **Software/Hardware**: DO-178C, DO-254, DO-160
3. **Cybersecurity**: DO-326A/ED-202A, DO-355/ED-203
4. **Data Protection**: GDPR, UK GDPR, PIPEDA (passenger data)
5. **AI Systems**: EU AI Act (automated systems), NIST AI RMF
6. **PNR Data**: EU PNR Directive, national PNR requirements

**Key Challenges**:
- Safety-critical AI systems classification (High-Risk under AI Act)
- Balancing safety data retention vs. data minimization
- Crew privacy vs. flight data monitoring
- International data transfers for global operations
- Biometric boarding systems compliance

#### Space Industry
**Regulatory Stack**:
1. **Mission Assurance**: ECSS-Q, NASA NPR 7120.5
2. **Systems Engineering**: ECSS-E, ISO 14300 series
3. **Software**: ECSS-Q-ST-80C, DO-178C (adapted)
4. **Data Protection**: GDPR (crew data), multinational considerations
5. **AI Systems**: EU AI Act (autonomous systems), NIST AI RMF
6. **Export Control**: ITAR, EAR, Wassenaar Arrangement

**Key Challenges**:
- Autonomous decision-making in deep space
- Multi-national crew data protection harmonization
- Limited human oversight feasibility
- Long-duration mission data retention
- Export control for international collaboration

#### Defense Industry
**Regulatory Stack**:
1. **National Security**: National security exemptions apply
2. **Dual-Use**: Civilian applications must comply
3. **Export Control**: ITAR, EAR, national export regulations
4. **Cybersecurity**: NIST 800-171, CMMC, national requirements
5. **Data Protection**: GDPR (civilian aspects), national laws
6. **AI Systems**: EU AI Act (limited applicability), ethical frameworks

**Key Challenges**:
- Determining national security exemption boundaries
- Dual-use AI system compliance
- Export control and international AI collaboration
- Classified data handling and privacy rights
- Autonomous weapons systems ethics and regulation

## Policy Structure

Each policy document includes:
- **Scope**: What and whom it applies to
- **Purpose**: Why the policy exists
- **Definitions**: Key terms and acronyms
- **Policy Statement**: The actual requirements
- **Roles & Responsibilities**: Who does what
- **References**: Related standards and procedures
- **Approval**: Signature authority
- **Revision History**: Version control

## Policy Approval Authority

- **Program Policies**: Chief Engineer + Quality Manager
- **Functional Policies**: Functional Manager + Compliance Officer
- **Work Instructions**: Subject Matter Expert + Compliance Officer

## Policy Lifecycle

1. **Draft**: Policy author creates draft
2. **Review**: SME review and stakeholder input
3. **Approval**: Management signature
4. **Release**: Controlled distribution via document management system
5. **Training**: Affected personnel trained on new/updated policy
6. **Review**: Periodic review (annual or upon regulatory change)
7. **Revision**: Updates processed through change control
8. **Archive**: Superseded versions retained for historical reference

## Policy Compliance

All personnel must:
- Read and acknowledge applicable policies
- Follow policy requirements in their work
- Report policy violations or gaps
- Suggest improvements based on lessons learned

## Training Requirements

- New employee onboarding: Core compliance policies
- Role-specific training: Policies relevant to job function
- Annual refresher: Critical policies (export control, data protection)
- Update training: When policies significantly change

## Integration Points

- **Standards**: Policies implement standard requirements (see `../01-STANDARDS/`)
- **Procedures**: Policies are executed through SOPs (see `../../QUALITY_QMS/02-PROCEDURES/`)
- **Evidence**: Policy compliance demonstrated through objective evidence (see `../06-EVIDENCE/`)
- **Audits**: Policies audited for effectiveness (see `../04-AUDITS/`)

## Key Artifacts

### POLICY_REGISTER.csv
Master list of all compliance policies:
- Policy ID, Title, Version, Effective Date
- Owner, Approval Authority
- Next Review Date
- Related Standards, Related Procedures
- Training Required (Y/N)

### PROCEDURE_LINKS.md
Quick reference to relevant SOPs and WIs with:
- Procedure number and title
- Brief description
- Link to document in PLM/QMS
- Applicability (aviation/space/both)

### TRAINING_MATRIX.xlsx
Maps policies to:
- Job roles requiring training
- Training completion status
- Refresh frequency
- Last completion date

## Deviations from Policy

Temporary deviations require:
1. Written justification
2. Risk assessment
3. Approval by policy owner
4. Time-limited duration
5. Tracking in deviation register
6. Review for permanent policy change

## Directory Structure

```
02-POLICIES/
├── README.md (this file)
├── REGIONAL_REGULATIONS/
│   ├── EU/
│   │   ├── GDPR_COMPLIANCE.md
│   │   ├── AI_ACT_COMPLIANCE.md
│   │   ├── ePrivacy_Directive.md
│   │   ├── NIS2_Directive.md
│   │   └── Product_Safety.md
│   ├── US/
│   │   ├── NIST_Privacy_Framework.md
│   │   ├── NIST_AI_RMF.md
│   │   ├── State_Privacy_Laws.md
│   │   ├── FAA_Regulations.md
│   │   └── Export_Control.md
│   ├── UK/
│   │   ├── UK_GDPR.md
│   │   ├── Data_Protection_Act_2018.md
│   │   └── AI_Regulation.md
│   ├── CHINA/
│   │   ├── PIPL.md
│   │   ├── Cybersecurity_Law.md
│   │   ├── Data_Security_Law.md
│   │   └── AI_Regulations.md
│   ├── JAPAN/
│   │   ├── APPI.md
│   │   └── AI_Guidelines.md
│   ├── CANADA/
│   │   ├── PIPEDA.md
│   │   └── AIDA.md
│   ├── AUSTRALIA/
│   │   ├── Privacy_Act.md
│   │   └── AI_Ethics_Framework.md
│   └── INTERNATIONAL/
│       ├── OECD_Principles.md
│       ├── ISO_Standards.md
│       └── UN_Guidelines.md
├── AI_GOVERNANCE/
│   ├── AI_Ethics_Policy.md
│   ├── Risk_Classification.md
│   ├── Model_Governance.md
│   ├── Bias_Mitigation.md
│   ├── Human_Oversight.md
│   └── Transparency_Requirements.md
├── SECTOR_SPECIFIC/
│   ├── AVIATION/
│   │   ├── Aviation_Safety_Compliance.md
│   │   ├── DO_178C_Policy.md
│   │   ├── PNR_Data_Policy.md
│   │   └── Crew_Data_Privacy.md
│   ├── SPACE/
│   │   ├── Mission_Assurance_Policy.md
│   │   ├── ECSS_Compliance.md
│   │   ├── Crew_Privacy_Policy.md
│   │   └── Export_Control_Space.md
│   └── DEFENSE/
│       ├── Dual_Use_Policy.md
│       ├── National_Security_Exemptions.md
│       └── Classified_Data_Handling.md
├── POLICY_REGISTER.csv
├── PROCEDURE_LINKS.md
└── TRAINING_MATRIX.xlsx
```

## Related Documents

- Quality Management System: [`../../QUALITY_QMS/`](../../QUALITY_QMS/)
- Governance Framework: [`../../GOVERNANCE/`](../../GOVERNANCE/)
- Standards Library: [`../01-STANDARDS/`](../01-STANDARDS/)
- Audit Program: [`../04-AUDITS/`](../04-AUDITS/)

## Metrics

- Policy review currency (% on-time reviews)
- Training completion rate (% personnel trained)
- Policy deviations (count, closure rate)
- Policy effectiveness (audit findings related to policy gaps)

---

**Owner**: Compliance Office  
**Review**: Annual or upon regulatory change  
**Approval**: Chief Engineer, Quality Manager
