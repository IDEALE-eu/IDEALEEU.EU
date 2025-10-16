---
area: "00-PROGRAM/COMPLIANCE/02-POLICIES/REGIONAL_REGULATIONS/EU"
regulation: "EU AI Act (EU 2024/1689)"
owner: "AI Ethics & Compliance Officer"
status: "Active"
effective_date: "2024-08-01"
full_application: "2026-08-02"
last_review: "2025-01"
confidentiality: "Internal"
---

# EU Artificial Intelligence Act Compliance Framework

## Overview

The EU Artificial Intelligence Act (Regulation (EU) 2024/1689) establishes the first comprehensive legal framework for AI in the world, taking a risk-based approach to AI regulation with the goal of ensuring AI systems are safe, transparent, traceable, non-discriminatory, and environmentally friendly.

## Key Dates and Phased Implementation

| Phase | Date | Requirements |
|-------|------|--------------|
| Entry into Force | August 1, 2024 | Regulation officially enacted |
| Prohibited AI Bans | February 2, 2025 | 6 months - Prohibited AI systems banned |
| Codes of Practice | August 2, 2025 | 12 months - General-purpose AI codes of practice |
| Governance | August 2, 2025 | 12 months - AI Office and governance structures |
| High-Risk AI | August 2, 2026 | 24 months - High-risk AI requirements apply |
| Full Application | August 2, 2027 | 36 months - All requirements fully applicable |

## Scope and Definitions

### Territorial Scope (Art. 2)
- **Providers**: Placing AI systems on EU market or putting into service
- **Deployers**: Using AI systems under their authority in EU
- **Importers/Distributors**: Making AI systems available in EU
- **Product Manufacturers**: Integrating AI into products covered by EU harmonized legislation
- **Extra-territorial**: Output used in EU affects scope

### Key Definitions (Art. 3)

#### AI System
A machine-based system designed to operate with varying levels of autonomy that may exhibit adaptiveness after deployment and that, for explicit or implicit objectives, infers from input how to generate outputs such as predictions, content, recommendations, or decisions that can influence physical or virtual environments.

#### Provider
A natural or legal person, public authority, agency, or other body that develops an AI system or that has an AI system developed and places it on the market or puts it into service under its own name or trademark, whether for payment or free of charge.

#### Deployer
A natural or legal person, public authority, agency, or other body using an AI system under its authority, except where the AI system is used in the course of a personal non-professional activity.

#### High-Risk AI System
AI systems identified as high-risk based on their intended purpose and classification under Annex III or as safety components under EU harmonized legislation.

## Risk Classification Framework

### Prohibited AI Practices (Art. 5)

#### Absolute Prohibitions
1. **Subliminal Manipulation**: Techniques beyond person's consciousness causing harm
2. **Exploitation of Vulnerabilities**: Exploiting age, disability, or socioeconomic situation
3. **Social Scoring**: Evaluation/classification by public authorities leading to detrimental treatment
4. **Risk Assessment for Crime**: Predicting likelihood of offenses based solely on profiling or personality traits
5. **Facial Recognition Databases**: Untargeted scraping from internet or CCTV
6. **Emotion Recognition**: In workplace or education (with exceptions for medical/safety)
7. **Biometric Categorization**: Inferring race, political opinions, trade union membership, religion, sex life, or sexual orientation (with exceptions for law enforcement)
8. **Real-Time Remote Biometric Identification**: In public spaces for law enforcement (with narrow exceptions for serious crimes)

#### Exceptions and Safeguards
- Narrow exceptions for law enforcement with judicial authorization
- Strict necessity and proportionality requirements
- Transparent use with human oversight
- Retroactively reviewable

### High-Risk AI Systems (Art. 6 & Annex III)

#### Categories

**1. Biometric Identification and Categorization**
- Remote biometric identification systems
- Biometric categorization systems (according to sensitive attributes)
- Emotion recognition systems

**2. Critical Infrastructure**
- Safety components of critical infrastructure (energy, water, transport)
- Management and operation systems

**3. Education and Vocational Training**
- Systems for determining access or admission to education
- Assessment of learning outcomes
- Evaluation of appropriate education level
- Monitoring and detection of prohibited behavior (e.g., cheating)
- Proctoring of exams

**4. Employment, Workers Management, and Access to Self-Employment**
- Recruitment and selection systems
- Promotion and termination decisions
- Task allocation and performance monitoring
- Access to self-employment and services (e.g., credit scoring for starting business)

**5. Essential Private and Public Services**
- Creditworthiness assessment and credit scoring
- Risk assessment and pricing for life and health insurance
- Evaluation of eligibility for public assistance and benefits
- Emergency dispatch and prioritization systems

**6. Law Enforcement**
- Individual risk assessment for crime victims
- Polygraph and similar tools
- Evaluation of reliability of evidence
- Crime prediction and analytics (profiling, location, time)
- Profiling during detection, investigation, prosecution

**7. Migration, Asylum, and Border Control**
- Polygraph and similar tools
- Risk assessments (security, irregular immigration, health)
- Examination of applications (visa, asylum, residence permits)
- Detection of false documents and identities
- Complaint verification

**8. Administration of Justice and Democratic Processes**
- Assisting judicial authorities in research and interpretation of facts and law
- Application of law to concrete facts
- Influencing elections or referendums
- Influencing voting behavior

#### Exemptions from High-Risk Classification
- Limited to narrow procedural tasks
- Not replacing human assessment
- Improving result of previously completed human activity
- Detecting decision-making patterns
- Under supervision and not binding

### Limited-Risk AI Systems (Transparency Obligations)

#### General-Purpose AI Models (Art. 52)
- **Chatbots**: Users must be informed they're interacting with AI
- **Emotion Recognition/Biometric Categorization**: Inform users of system operation
- **Deep Fakes**: Clear disclosure that content is artificially generated/manipulated
- **AI-Generated Content**: Labeling and detectability (e.g., watermarking)

#### General-Purpose AI (GPAI) (Art. 51-55)
**Standard GPAI Models:**
- Technical documentation
- Information and documentation for downstream providers
- Copyright compliance (summary of training data)
- Transparency regarding EU content use

**GPAI with Systemic Risk:**
- Additional requirements when model training with >10^25 FLOPs
- Model evaluation
- Adversarial testing
- Incident reporting
- Cybersecurity protection
- Energy consumption reporting

### Minimal Risk AI Systems
- No specific requirements beyond general law
- Voluntary codes of conduct encouraged
- Examples: AI-enabled video games, spam filters, inventory management

## Requirements for High-Risk AI Systems

### Risk Management System (Art. 9)
- **Continuous Process**: Throughout entire lifecycle
- **Risk Identification**: Known and foreseeable risks
- **Risk Estimation**: Probability and severity
- **Risk Evaluation**: Against benefit and state of the art
- **Risk Reduction**: Elimination or mitigation measures
- **Residual Risk**: Acceptable level determination
- **Testing**: Validation of risk mitigation measures
- **Post-Market Monitoring**: Ongoing risk assessment

### Data and Data Governance (Art. 10)
- **Training, Validation, Testing Data**:
  - Relevant, representative, error-free, complete
  - Appropriate statistical properties
  - Consideration of intended geographic, behavioral, functional setting
  - GDPR compliance for personal data
- **Data Governance**:
  - Data design choices documented
  - Examination for biases
  - Mitigation measures for biases
  - Data gaps identification
  - Special measures for sensitive attributes
- **Input Data Quality**:
  - Specifications for input data quality and relevance
  - Instructions for data preparation and formatting

### Technical Documentation (Art. 11 & Annex IV)
**Must Include:**
- General description of AI system
- Detailed description of elements and development process
- Detailed information on monitoring, functioning, control
- Description of risk management system
- Changes to the system throughout its lifecycle
- Description of testing and validation
- Cybersecurity measures
- Compliance assessment procedure followed
- Copy of conformity declaration
- Detailed description of system performance

### Record-Keeping (Art. 12)
- **Automatic Logging**: Technical capability for automatic event logs
- **Duration**: As appropriate for intended purpose and legal obligations
- **Content**:
  - Period of AI system use
  - Reference database
  - Input data leading to decision
  - Identification of deployer
  - Identification of natural persons subject to decision
- **Protection**: Against tampering and unauthorized access
- **GDPR Compliance**: Logging of personal data must comply with data protection rules

### Transparency and Information for Deployers (Art. 13)
- **Instructions for Use**:
  - Identity and contact details of provider
  - Characteristics, capabilities, and limitations
  - Changes to system and performance over time
  - Performance metrics and limitations
  - Level of accuracy, robustness, cybersecurity
  - Known or foreseeable circumstances of failures
  - Reasonably foreseeable misuse
  - Human oversight measures
  - Expected lifetime and maintenance
  - Changes determined by provider

### Human Oversight (Art. 14)
- **Oversight Measures**:
  - Understand system capabilities and limitations
  - Be aware of automation bias
  - Interpret outputs correctly
  - Decide not to use or override decision
  - Intervene or interrupt operation (stop button)
- **Technical Design**:
  - Identified and built into system
  - Assigned to natural persons with necessary competence and authority
  - Appropriate frequency of human intervention

### Accuracy, Robustness, and Cybersecurity (Art. 15)
- **Accuracy**: Achieve appropriate level consistent with intended purpose
- **Robustness**: Resilient against errors, faults, inconsistencies, third-party attempts
- **Cybersecurity**: Resilient against unauthorized third parties
- **Technical Solutions**:
  - Redundancy measures
  - Backup or fail-safe plans
  - Protection against adversarial examples
  - Measures to handle model drift
  - Secure software development practices

## Obligations of Providers (Art. 16-23)

### Quality Management System (Art. 17)
- **Documented and Maintained**:
  - Compliance strategy for regulatory requirements
  - Design, development, and testing procedures
  - Pre- and post-market validation procedures
  - Technical specifications and standards applied
  - Data management system
  - Risk management system
  - Post-market monitoring system
  - Incident and corrective action procedures
  - Communication with authorities, notified bodies, operators
  - Record-keeping systems
  - Resource management
  - Accountability framework

### Conformity Assessment (Art. 43)
#### Internal Control (Annex VI)
- For most high-risk AI systems
- Technical documentation compilation
- Compliance verification by provider
- EU declaration of conformity issuance
- Registration in EU database

#### Third-Party Assessment (Annex VII)
- For AI systems used in law enforcement, migration, or as safety components under specific regulations
- Notified body assessment
- More rigorous evaluation
- Certification issuance

### EU Declaration of Conformity (Art. 47)
- Provider confirms compliance with AI Act
- Continuously updated
- Available to authorities for 10 years
- Accompanied by technical documentation

### CE Marking (Art. 48)
- Affixed visibly, legibly, indelibly
- Or on packaging or accompanying documentation
- Indicates conformity with AI Act requirements
- Other markings allowed if don't reduce visibility/legibility

### Registration (Art. 49 & Art. 71)
#### EU Database for High-Risk AI Systems
**Providers Must Register:**
- Name, address, contact details
- AI system trade name and additional description
- Intended purpose
- Status (on market, in service, recalled, withdrawn)
- Type of conformity assessment
- Authority or notified body involved
- Instructions for use
- EU declaration of conformity
- Link to website for further information

**Deployers Must Register (for certain systems):**
- Public authorities and EU institutions
- Private deployers of remote biometric identification and emotion recognition systems

### Post-Market Monitoring (Art. 72)
- **Plan and Documentation**:
  - Active and systematic collection of data on performance
  - Analysis of AI system in use
  - Review of safety, performance, compliance
- **Reporting**:
  - Serious incidents to market surveillance authorities
  - Timeline: Immediately after awareness, full report within 15 days
  - Malfunctions and deviations impacting compliance
- **Corrective Actions**:
  - Recall, withdrawal, modification, service termination
  - Immediate action for serious incidents
  - Documentation and communication

## Obligations of Deployers (Art. 26)

### General Obligations
- Use AI systems according to instructions for use
- Assign human oversight to competent persons
- Monitor operation based on instructions
- Maintain automatically generated logs (where applicable)
- Inform provider of serious incidents and malfunctions

### Specific Obligations for Certain Deployers
- **Data Protection Impact Assessment**: If high-risk AI involves personal data processing
- **Fundamental Rights Impact Assessment**: Public authorities and certain private deployers
- **Registration**: Public authorities, EU institutions, specific private deployers
- **Inform Individuals**: When subject to decisions based on high-risk AI outputs
- **Additional Transparency**: For emotion recognition and biometric categorization

### Becoming a Provider
Deployer becomes provider if:
- Puts own name/trademark on high-risk AI system
- Modifies intended purpose of high-risk AI system
- Makes substantial modification to high-risk AI system

## General-Purpose AI Models (GPAI) (Art. 51-55)

### Standard GPAI Requirements
1. **Technical Documentation** (Art. 53(1)(a))
   - Training and testing process
   - Data used
   - Compute resources
   - Model architecture
   - Performance metrics
   - Limitations and mitigation measures

2. **Information for Downstream Providers** (Art. 53(1)(b))
   - Capabilities and limitations
   - Appropriate use conditions
   - Integration guidance
   - Technical specifications

3. **Copyright Compliance** (Art. 53(1)(c))
   - Summary of training data
   - Copyright compliance measures
   - Available upon request to authority and copyright holders

4. **Transparency** (Art. 53(1)(d))
   - Public summary of content used for training
   - Sufficiently detailed for rights holders to assert rights

### GPAI with Systemic Risk
**Designation Criteria** (Art. 51(1)):
- Cumulative amount of compute > 10^25 FLOPs
- Or Commission decision based on capabilities/impact

**Additional Requirements** (Art. 55):
1. **Model Evaluation** (Art. 55(1)(a))
   - Standardized protocols and tools
   - Assessment of systemic risks
   - Including cybersecurity, AI safety

2. **Adversarial Testing** (Art. 55(1)(b))
   - Red-teaming
   - Testing for vulnerabilities
   - Documentation of results

3. **Serious Incident Reporting** (Art. 55(1)(c))
   - To AI Office
   - Format and procedures defined by Commission

4. **Cybersecurity Protection** (Art. 55(1)(d))
   - State-of-the-art measures
   - Protection of model and infrastructure
   - Against unauthorized access and manipulation

5. **Energy Consumption** (Art. 55(1)(e))
   - Track and document
   - Report to AI Office

### Codes of Practice (Art. 56)
- Voluntary adherence demonstrating compliance
- Developed by providers with stakeholder involvement
- Approved by AI Office
- Open participation, transparency, adaptability
- Regularly updated

## Governance and Enforcement

### AI Office (Art. 64)
- **European Level**: Part of European Commission
- **Functions**:
  - Monitor and supervise general-purpose AI
  - Scientific research and analysis
  - Coordinate with national authorities
  - Maintain EU AI database
  - Develop codes of practice and guidelines
  - International cooperation

### National Competent Authorities (Art. 65-66)
- **Market Surveillance Authorities**: Enforce AI Act in Member States
- **Notifying Authorities**: Designate and monitor notified bodies
- **Powers**:
  - Access to data, documentation, code
  - Testing and examination
  - Request information from providers/deployers
  - Order corrective measures, withdrawal, recall
  - Restrict or prohibit making available
  - Impose administrative fines

### European Artificial Intelligence Board (Art. 65)
- **Composition**: Representatives from Member States, European Data Protection Supervisor, Commission
- **Functions**:
  - Advise and assist Commission and national authorities
  - Contribute to consistent application
  - Coordinate between market surveillance authorities
  - Collect and share best practices
  - Provide opinions and recommendations

### Notified Bodies (Art. 39-41)
- **Designation**: By Member States
- **Requirements**:
  - Independence and impartiality
  - Competence and expertise
  - Documented procedures
  - Sufficient resources
- **Functions**:
  - Third-party conformity assessment
  - Certificate issuance
  - Post-market surveillance
  - Information to authorities

## Penalties and Enforcement (Art. 99)

### Administrative Fines
**Maximum Amounts:**
- **€35 million or 7% global turnover** (higher amount): Non-compliance with prohibited AI practices
- **€15 million or 3% global turnover**: Non-compliance with high-risk AI requirements, obligations of operators, notified bodies
- **€7.5 million or 1.5% global turnover**: Supplying incorrect information to authorities

**For SMEs and Startups:**
- Lower percentages apply
- Fines proportionate to size and market position

**Factors Considered:**
- Nature, gravity, duration of infringement
- Intentional or negligent
- Actions to mitigate harm
- Financial benefits gained or losses avoided
- Cooperation with authorities
- Previous infringements
- How authorities became aware
- Compliance with corrective measures
- Other aggravating or mitigating factors

## Aviation Industry Specific Applications

### Flight Operations
- **Automated Flight Planning**: High-risk if safety-critical
- **Predictive Maintenance**: High-risk classification likely
- **Collision Avoidance**: Safety component of critical infrastructure
- **Air Traffic Management AI**: Critical infrastructure application

### Crew and Personnel
- **Pilot Training Assessment**: High-risk (education/training)
- **Crew Scheduling**: High-risk (employment management)
- **Fatigue Detection**: Emotion recognition - transparency obligations
- **Performance Evaluation**: High-risk (employment decisions)

### Passenger Services
- **Dynamic Pricing**: Potentially high-risk if discriminatory
- **Customer Service Chatbots**: Transparency obligations
- **Biometric Boarding**: High-risk biometric identification
- **Behavior Monitoring**: Potentially prohibited depending on implementation

### Safety and Security
- **Baggage Screening**: High-risk if used for security risk assessment
- **Passenger Risk Assessment**: High-risk law enforcement application
- **Anomaly Detection**: Classification depends on use case
- **Cybersecurity Systems**: High-risk if protecting critical infrastructure

## Space Industry Specific Applications

### Mission Operations
- **Autonomous Navigation**: High-risk if crew safety impact
- **Collision Avoidance**: Critical infrastructure safety component
- **Anomaly Detection**: Classification depends on criticality
- **Resource Optimization**: Minimal risk if no safety impact

### Crew and Ground Personnel
- **Crew Selection**: High-risk employment decision
- **Training and Assessment**: High-risk education application
- **Health Monitoring**: High-risk if used for crew decisions
- **Performance Evaluation**: High-risk employment management

### Payload and Science
- **Data Analysis**: Generally minimal risk
- **Autonomous Experiments**: Risk depends on safety implications
- **Mission Planning**: High-risk if crew safety involved
- **Decision Support**: Classification depends on role and autonomy

### Safety and Security
- **Fault Detection and Diagnosis**: High-risk for critical systems
- **ECLSS Management**: High-risk critical infrastructure
- **Security Threat Assessment**: Potentially prohibited or high-risk
- **Emergency Response**: High-risk if automated decisions

## Defense Industry Specific Considerations

### Scope and Exemptions (Art. 2(3))
- **National Security**: AI for national security purposes exempt
- **Military, Defense, National Security**: Exempt from AI Act
- **BUT**: Export control implications
- **Dual-Use**: Civilian applications must comply

### Dual-Use Applications
- **Supply Chain**: AI in civilian supply chain must comply
- **Testing and Validation**: Civilian facilities must comply
- **Personnel Systems**: HR systems for civilian staff must comply
- **Research**: Non-military research must comply

### Export Considerations
- **Regulation (EU) 2021/821**: Dual-use items export control
- **AI Act Compliance**: May become export criterion
- **International Sales**: Compliance may be competitive advantage
- **Third Country Requirements**: May align with or differ from EU

## Compliance Implementation Roadmap

### Phase 1: Immediate Actions (Completed by Feb 2025)
- [ ] **AI Inventory**: Catalog all AI systems in use and development
- [ ] **Prohibited AI Check**: Ensure no prohibited practices
- [ ] **Governance Structure**: Establish AI Ethics & Compliance function
- [ ] **Awareness Training**: Executive and management briefings
- [ ] **Initial Risk Assessment**: High-level classification of AI systems

### Phase 2: Preparation for GPAI (Feb 2025 - Aug 2025)
- [ ] **GPAI Assessment**: Determine if any models qualify as GPAI
- [ ] **Technical Documentation**: Prepare for GPAI requirements
- [ ] **Copyright Compliance**: Review training data provenance
- [ ] **Transparency Measures**: Prepare public summaries
- [ ] **Monitoring Setup**: Systems for ongoing compliance

### Phase 3: High-Risk AI Compliance (Aug 2025 - Aug 2026)
- [ ] **Detailed Risk Classification**: Complete classification of all AI systems
- [ ] **Requirements Mapping**: Map requirements to each high-risk system
- [ ] **Risk Management**: Implement risk management for each system
- [ ] **Data Governance**: Establish data quality and bias mitigation
- [ ] **Technical Documentation**: Complete documentation per Annex IV
- [ ] **Logging and Record-Keeping**: Implement automatic logging
- [ ] **Human Oversight**: Design and implement oversight measures
- [ ] **Accuracy and Robustness**: Testing and validation programs
- [ ] **Quality Management System**: Establish QMS per Art. 17
- [ ] **Conformity Assessment**: Prepare for and complete assessments
- [ ] **CE Marking**: Obtain and affix where required
- [ ] **Registration**: Register in EU database

### Phase 4: Deployment and Monitoring (Aug 2026 onwards)
- [ ] **Deployer Compliance**: Instructions for deployers
- [ ] **Post-Market Monitoring**: Continuous monitoring systems
- [ ] **Incident Response**: Reporting and corrective action procedures
- [ ] **Ongoing Training**: Staff training and competency maintenance
- [ ] **Continuous Improvement**: Lessons learned and updates
- [ ] **Authority Cooperation**: Respond to information requests

## Integration with IDEALEEU.EU Framework

### Governance Integration
- **AI Ethics Board**: Part of [`../../REVIEW_BOARDS/ETHICS/`](../../../REVIEW_BOARDS/ETHICS/)
- **Risk Management**: Integrated with [`../../COMPLIANCE/09-RISK_COMPLIANCE/`](../../../COMPLIANCE/09-RISK_COMPLIANCE/)
- **Quality Management**: QMS for AI systems in [`../../QUALITY_QMS/`](../../../QUALITY_QMS/)
- **Data Protection**: Coordination with [`../../COMPLIANCE/11-DATA_PROTECTION/`](../../../COMPLIANCE/11-DATA_PROTECTION/)

### Technical Integration
- **MAL-EEM Framework**: Model Cards and Risk Assessments in [`../../GOVERNANCE/MAL-EEM/`](../../../GOVERNANCE/MAL-EEM/)
- **Digital Thread**: AI system lifecycle tracking
- **UTCS Anchoring**: AI Act compliance evidence
- **Version Control**: AI system versioning and change management

### Documentation Links
- **Model Cards**: [`../../GOVERNANCE/MAL-EEM/model_cards/`](../../../GOVERNANCE/MAL-EEM/model_cards/)
- **Risk Assessments**: [`../../GOVERNANCE/MAL-EEM/risk_assessments/`](../../../GOVERNANCE/MAL-EEM/risk_assessments/)
- **Bias and Fairness**: [`../../GOVERNANCE/MAL-EEM/bias_fairness/`](../../../GOVERNANCE/MAL-EEM/bias_fairness/)
- **Safety Cases**: [`../../GOVERNANCE/MAL-EEM/safety_case/`](../../../GOVERNANCE/MAL-EEM/safety_case/)

## References

### Primary Legislation
- **Regulation (EU) 2024/1689**: Artificial Intelligence Act
- **Commission Delegated Regulations**: To be adopted (technical standards, conformity assessment)
- **Commission Implementing Regulations**: To be adopted (detailed rules)

### Supporting Documents
- **Recitals**: Context and intent of provisions
- **Annexes**: Detailed requirements and lists
- **Guidelines**: AI Office and Board guidelines (to be developed)

### Related EU Legislation
- **GDPR**: Data protection compliance
- **Product Safety Regulations**: Harmonized legislation integration
- **Digital Services Act**: Online platform responsibilities
- **Machinery Regulation**: Safety of machinery with AI
- **Medical Devices Regulation**: AI as medical device

### Standards (In Development)
- **ISO/IEC 42001**: AI Management System
- **ISO/IEC 23894**: AI Risk Management
- **ISO/IEC 5338**: AI System Life Cycle Process
- **ISO/IEC TR 24027**: Bias in AI systems
- **IEEE 7000**: Ethics by Design

## Version Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2025-01 | AI Ethics & Compliance Office | Initial comprehensive AI Act framework |

---

**Owner**: AI Ethics & Compliance Officer  
**Review Frequency**: Quarterly during implementation phase, then annual  
**Next Review**: 2025-04  
**Classification**: Internal Use Only
