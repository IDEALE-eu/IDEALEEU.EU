# Data Sheet Template

**Dataset Name**: [Name]  
**Version**: [Version]  
**UTCS ID**: [UTCS-XXX]  
**Date**: YYYY-MM-DD  
**Owner**: [Data Owner Name]

---

## 1. Motivation

### Purpose
**For what purpose was the dataset created?**
[Describe the purpose]

**Who created the dataset and on behalf of which entity?**
- **Creator**: [Team/Organization]
- **Funding**: [Funding source, if applicable]

**Who funded the creation of the dataset?**
[Funding details]

---

## 2. Composition

### Dataset Characteristics
- **Size**: [Number of instances]
- **Features**: [Number and description]
- **Data Types**: [Numerical, categorical, text, image, etc.]
- **Time Period**: [When data was collected]
- **Update Frequency**: [If applicable]

### Instances
**What do the instances represent?**
[e.g., individual people, events, documents]

**How many instances are there in total?**
[Number]

**Does the dataset contain all possible instances or a sample?**
[Complete census or sample? If sample, describe sampling strategy]

### Data Content
**What data does each instance consist of?**
[List and describe features/fields]

| Field Name | Type | Description | Example |
|-----------|------|-------------|---------|
| [Field] | [Type] | [Description] | [Example] |

**Is there a label or target associated with each instance?**
[If supervised learning, describe labels]

---

## 3. Provenance and Consent

### Data Collection
**How was the data collected?**
- [ ] Direct observation/measurement
- [ ] Survey/questionnaire
- [ ] Existing database/records
- [ ] Web scraping
- [ ] Sensor data
- [ ] User-generated
- [ ] Other: [Specify]

**Who was involved in the data collection?**
[Teams, contractors, etc.]

**Over what timeframe was the data collected?**
- **Start Date**: YYYY-MM-DD
- **End Date**: YYYY-MM-DD

### Consent and Privacy
**Were data subjects informed about data collection?**
[ ] Yes [ ] No [ ] N/A

**What consent mechanism was used?**
- [ ] Explicit opt-in consent
- [ ] Implicit consent (terms of service)
- [ ] No consent required (public data)
- [ ] Other: [Specify]

**DPIA Required?**
[ ] Yes [ ] No

**DPIA Status**: [Link to DPIA if applicable]

---

## 4. Personal Data

### PII Content
**Does the dataset contain personal data?**
[ ] Yes [ ] No

**If yes, what types of personal data?**
- [ ] Names
- [ ] Email addresses
- [ ] Phone numbers
- [ ] Addresses
- [ ] Biometric data
- [ ] Financial information
- [ ] Health information
- [ ] Other: [Specify]

### Anonymization/Pseudonymization
**Has the data been anonymized or pseudonymized?**
[ ] Anonymized [ ] Pseudonymized [ ] Raw

**Method**: [Describe anonymization/pseudonymization technique]

**Re-identification Risk**: [Low/Medium/High and justification]

---

## 5. Legal Basis and License

### Legal Basis (GDPR)
- [ ] Consent
- [ ] Contract
- [ ] Legal obligation
- [ ] Vital interests
- [ ] Public interest
- [ ] Legitimate interest
- [ ] N/A (not personal data)

**Justification**: [Explain legal basis]

### License
**What license governs the dataset?**
[License type: MIT, CC-BY, Proprietary, etc.]

**Can the dataset be redistributed?**
[ ] Yes [ ] No [ ] With restrictions

**Restrictions**: [Any usage restrictions]

---

## 6. Data Quality

### Completeness
**Is the data complete or are there missing values?**
- **Missing Data**: [Percentage or description]
- **Handling**: [How missing data is handled]

### Accuracy
**How accurate is the data?**
[Assessment of data accuracy]

**Validation Performed**: [Describe validation steps]

### Errors and Noise
**Does the dataset contain errors?**
[Known errors or noise in the data]

**Error Rate**: [If quantifiable]

---

## 7. Preprocessing

### Preprocessing Steps
[List preprocessing steps applied]

1. [Step 1]
2. [Step 2]

### Raw Data Availability
**Is raw, unprocessed data available?**
[ ] Yes [ ] No

**Raw Data Location**: [If available]

---

## 8. Distribution and Representation

### Population Coverage
**Does the dataset represent a specific population?**
[Describe target population]

**Sampling Method**: [Random, stratified, convenience, etc.]

### Demographic Representation
| Demographic | Representation | Notes |
|-------------|---------------|-------|
| [Group] | [Percentage] | [Notes on representation] |

### Geographic Coverage
- **Countries/Regions**: [List]
- **Urban/Rural**: [Distribution]

### Temporal Coverage
- **Time Period**: [Covered period]
- **Seasonality**: [Any seasonal patterns]

---

## 9. Biases and Limitations

### Known Biases
- [Bias 1]: [Description and impact]
- [Bias 2]: [Description and impact]

**Bias Analysis**: [Link to bias_fairness/ documentation]

### Selection Bias
[Describe any selection bias in data collection]

### Representation Bias
[Describe groups that may be under- or over-represented]

### Limitations
- [Limitation 1]
- [Limitation 2]

---

## 10. Data Retention and Deletion

### Retention Policy
**How long will the data be retained?**
[Retention period]

**Retention Justification**: [Why this period is necessary]

### Deletion Procedure
**How is data deleted?**
[Describe deletion process]

**Deletion Verification**: [How deletion is verified]

### Subject Rights
**Can data subjects request deletion?**
[ ] Yes [ ] No

**Request Process**: [How to request deletion]

---

## 11. Updates and Maintenance

### Update Schedule
**Will the dataset be updated?**
[ ] Yes, regularly [ ] Yes, as needed [ ] No

**Update Frequency**: [If regular updates]

### Versioning
**How are dataset versions managed?**
[Versioning scheme]

**Version History**: [Link to version history]

### Notification
**How are users notified of updates?**
[Notification mechanism]

---

## 12. Ethical Review

### Ethics Assessment
**Has the dataset undergone ethical review?**
[ ] Yes [ ] No

**Reviewer**: [Ethics officer/committee]  
**Review Date**: YYYY-MM-DD

### Ethical Concerns
[List any ethical concerns and mitigations]

**Ethics Approval**: [Link to approval documentation]

---

## 13. Security

### Access Control
**Who has access to the data?**
[Roles with access]

**Access Control Mechanism**: [How access is controlled]

### Security Measures
- [ ] Encryption at rest
- [ ] Encryption in transit
- [ ] Access logging
- [ ] Audit trail
- [ ] Other: [Specify]

---

## 14. Approvals

**Data Owner**: [Name, Date]  
**DPO**: [Name, Date]  
**Ethics Officer**: [Name, Date]  
**Security Lead**: [Name, Date]

**Decision Record**: Store in `REVIEW_BOARDS/DATA_PROTECTION/decisions/`

---

## Attachments

- [Data dictionary]
- [Sample data]
- [Collection protocols]
- [Consent forms]
