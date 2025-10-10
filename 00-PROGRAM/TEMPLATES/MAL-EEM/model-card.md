# Model Card Template

**Model Name**: [Name]  
**Version**: [Version]  
**UTCS ID**: [UTCS-XXX]  
**Date**: YYYY-MM-DD  
**Owner**: [ML Lead Name]

---

## 1. Model Details

### Basic Information
- **Developed By**: [Team/Organization]
- **Model Type**: [Classification, Regression, Generation, etc.]
- **Model Architecture**: [e.g., Neural Network, Decision Tree, etc.]
- **Framework**: [TensorFlow, PyTorch, Scikit-learn, etc.]
- **License**: [License type]

### Model Purpose
[Describe what the model is designed to do]

### Intended Use
- **Primary Use Case**: [Description]
- **Intended Users**: [Who should use this model]
- **Operational Context**: [Where/how it will be deployed]

---

## 2. Model Scope

### In Scope
- [Task 1]
- [Task 2]

### Out of Scope
- [What the model should NOT be used for]
- [Known limitations]

---

## 3. Training Data

### Data Sources
- [Source 1]: [Description, size]
- [Source 2]: [Description, size]

**Data Sheet**: [Link to data sheet documentation]

### Data Characteristics
- **Size**: [Number of samples]
- **Features**: [Number and types of features]
- **Labels**: [Label types and distribution]
- **Time Period**: [When data was collected]
- **Geographic Coverage**: [If applicable]

### Preprocessing
[Describe data preprocessing steps]

---

## 4. Evaluation

### Metrics
| Metric | Train | Validation | Test | Threshold |
|--------|-------|------------|------|-----------|
| Accuracy | [Value] | [Value] | [Value] | ≥ [Threshold] |
| Precision | [Value] | [Value] | [Value] | ≥ [Threshold] |
| Recall | [Value] | [Value] | [Value] | ≥ [Threshold] |
| F1 Score | [Value] | [Value] | [Value] | ≥ [Threshold] |

### Evaluation Approach
[Describe evaluation methodology]

### Test Dataset
- **Size**: [Number of samples]
- **Characteristics**: [Description]
- **Representativeness**: [How well it represents real-world data]

---

## 5. Performance by Slice

### Demographic Slices
| Slice | Metric | Value | Parity Δ | Status |
|-------|--------|-------|----------|--------|
| [Group 1] | Accuracy | [Value] | [Δ%] | Pass/Fail |
| [Group 2] | Accuracy | [Value] | [Δ%] | Pass/Fail |

**Bias/Fairness Report**: [Link to bias_fairness/ documentation]

### Other Slices
[Performance by other relevant slices: geography, time, input type, etc.]

---

## 6. Limitations

### Known Limitations
- [Limitation 1]
- [Limitation 2]

### Edge Cases
- [Edge case 1 and behavior]
- [Edge case 2 and behavior]

### Failure Modes
- [Failure mode 1 and indicators]
- [Failure mode 2 and indicators]

---

## 7. Uncertainty Specification

### Confidence Intervals
[Describe how uncertainty is quantified]

### Calibration
- **Calibration Metric**: [ECE, Brier Score, etc.]
- **Calibration Value**: [Value]
- **Interpretation**: [What this means]

### Handling Low-Confidence Predictions
[Describe what happens when confidence is below threshold]

---

## 8. Safety and Ethics

### Hazard Links
- [Link to hazard analysis]
- [Link to safety case]

**Risk Assessment**: [Link to risk_assessments/ documentation]

### Ethical Considerations
- [Privacy concerns]
- [Fairness considerations]
- [Potential for misuse]

**Ethics Review**: [Link to ethics review documentation]

---

## 9. Human Factors

### Cognitive Load
[Assessment of cognitive load on users]

### User Interface
[How results are presented to users]

### Interpretability
[How model decisions can be explained]

**Human Factors Review**: [Link to review documentation]

---

## 10. Monitoring and Maintenance

### Performance Monitoring
- **Metrics Tracked**: [List]
- **Monitoring Frequency**: [Frequency]
- **Alert Thresholds**: [Thresholds for intervention]

### Retraining Policy
- **Retraining Trigger**: [When to retrain]
- **Retraining Frequency**: [If scheduled]
- **Data Refresh**: [How training data is updated]

### Model Drift Detection
[How distribution shift and drift are detected]

---

## 11. Rollback and Kill-Switch

### Rollback Procedure
[Steps to revert to previous model version]

**Target MTTR**: [Time target for rollback]

### Kill-Switch
- **Activation Criteria**: [When to deactivate model]
- **Kill-Switch Owner**: [Role responsible]
- **Runbook**: [Link to kill-switch runbook]

---

## 12. Compliance

### Standards
- [ ] MAL-EEM P2 Gate passed
- [ ] Safety case approved
- [ ] Ethics review approved
- [ ] DPIA completed (if applicable)

**Gate Decisions**: [Links to review board decisions]

---

## 13. Version History

| Version | Date | Changes | Approved By |
|---------|------|---------|-------------|
| 1.0 | YYYY-MM-DD | Initial model | [Name] |

---

## 14. Approvals

**ML Lead**: [Name, Date]  
**Safety Lead**: [Name, Date]  
**Ethics Officer**: [Name, Date]  
**CCB**: [Name, Date]

**Decision Record**: Store in `REVIEW_BOARDS/CCB/decisions/`

---

## Attachments

- [Training logs]
- [Evaluation reports]
- [Bias analysis]
- [Model artifacts]
