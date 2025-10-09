# MODEL CARD TEMPLATE

**Model Name**: [e.g., Anomaly Detector for H₂ Leak Detection]

**Model ID**: [e.g., ANOMALY_DETECTOR_H2_LEAK_V1.2.3]

**Version**: [e.g., 1.2.3]

**Date**: [e.g., 2025-01-15]

**Owner**: [e.g., Data Science Team, Jane Smith]

---

## Model Details

### Model Type
- [ ] Physics-Based
- [ ] Behavioral
- [x] Data-Driven (ML)
- [ ] Hybrid

### Algorithm
[e.g., Autoencoder (neural network) for anomaly detection]

### Framework/Library
[e.g., TensorFlow 2.14, exported to ONNX 1.14]

### Model Architecture
[e.g., Encoder: 50 → 32 → 16, Decoder: 16 → 32 → 50, Activation: ReLU, Loss: MSE]

---

## Intended Use

### Primary Use Case
[e.g., Real-time detection of H₂ leaks in fuel system (UC-PRED-001)]

### Target Users
[e.g., Fleet operators, maintenance crews, pilots (alert display)]

### Deployment Environment
- [ ] Edge (on-aircraft)
- [x] Ground (operations center)
- [ ] Both

### Safety Criticality
- [x] Level A (Catastrophic)
- [ ] Level B (Hazardous)
- [ ] Level C (Major)
- [ ] Level D (Minor)

---

## Training Data

### Data Sources
[e.g., Flight test data (FY2024, 250 flights), Ground test data (120 tests)]

### Data Size
- **Training Set**: [e.g., 200,000 samples]
- **Validation Set**: [e.g., 50,000 samples]
- **Test Set**: [e.g., 50,000 samples]

### Data Labeling
[e.g., Expert-labeled (3 engineers), ground truth from sensor calibration]

### Data Characteristics
- **Features**: [e.g., 50 sensor signals (H₂ concentration, tank pressure, temperature, flow rates)]
- **Target**: [e.g., Binary classification: Normal (0) vs. Leak (1)]
- **Class Balance**: [e.g., 95% normal, 5% leak (handled with class weights)]

### Data Preprocessing
[e.g., Normalization (z-score), outlier removal (3σ), sliding window (10 seconds)]

---

## Model Performance

### Validation Metrics

| Metric | Value | Target | Status |
|--------|-------|--------|--------|
| **Accuracy** | 94.2% | >90% | ✅ Pass |
| **Precision** | 91.5% | >85% | ✅ Pass |
| **Recall (Sensitivity)** | 88.3% | >85% | ✅ Pass |
| **Specificity** | 95.8% | >95% | ✅ Pass |
| **AUC (ROC)** | 0.88 | >0.85 | ✅ Pass |
| **F1-Score** | 89.8% | >85% | ✅ Pass |

### Confusion Matrix (Test Set)
```
                Predicted
              Normal  Leak
Actual Normal  47,500   250
       Leak       300  1,950
```

### Performance by Subgroup
[e.g., Performance consistent across different flight phases: Ground (AUC=0.89), Cruise (AUC=0.87), Descent (AUC=0.88)]

---

## Limitations and Assumptions

### Assumptions
1. Sensor data quality: No systematic sensor faults
2. Training data representativeness: Covers 95% of operational envelope
3. Leak scenarios: Model trained on leaks >10 ppm (smaller leaks not detectable)

### Known Limitations
1. **False Positives**: ~5% false positive rate (alert when no leak)
2. **Novel Scenarios**: May not detect leaks in conditions not in training data
3. **Latency**: 25ms inference time (may miss very fast transients <25ms)

### Out-of-Scope
- Leak localization (model only detects, does not localize)
- Other fuel system anomalies (focus is H₂ leaks only)

---

## Fairness and Bias

### Fairness Considerations
[e.g., Model performance equal across all aircraft variants (PAX, CARGO, LONG_RANGE): AUC variance <0.02]

### Bias Mitigation
[e.g., Training data includes diverse operational conditions: high/low altitude, hot/cold weather, day/night]

---

## Ethical Considerations

### Potential Harms
[e.g., False negative (missed leak) → safety risk, False positive → unnecessary maintenance, downtime]

### Mitigation Strategies
[e.g., Dual validation with independent sensor (interlock), Human-in-the-loop for critical alerts]

---

## Maintenance and Updates

### Monitoring
- **Drift Detection**: PSI monitored daily (alert if >0.25)
- **Performance Tracking**: AUC tracked weekly on recent data

### Retraining Triggers
- Drift detected (PSI >0.25 for 7 days)
- Performance degradation (AUC <0.80)
- New leak scenarios identified

### Update Policy
See `../../08-SYNCHRONISATION/UPDATE_POLICY.md` (Ring deployment, 30-day shadow mode)

---

## Explainability

### Model Interpretability
[e.g., Partial interpretability via reconstruction error heatmap (shows which sensors contribute most to anomaly score)]

### Feature Importance
Top 5 features for leak detection:
1. H₂ concentration (sensor H2_CONC_01)
2. Tank pressure rate-of-change
3. Tank temperature
4. Valve position (unexpected open)
5. Flow rate

---

## Compliance

### Standards
- **ARP4754A**: Safety assessment (Level A)
- **DO-178C**: Software development (Level A)
- **DO-326A**: Cybersecurity (model signing, secure deployment)

### Certification Evidence
See `../../06-VALIDATION_VERIFICATION/CERT_EVIDENCE_LINKS.md`

---

## Contact

- **Model Owner**: [Name, email]
- **Data Science Lead**: [Name, email]
- **Safety Engineer**: [Name, email]

---

## Change History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0.0 | 2024-10-01 | Data Science Team | Initial release |
| 1.2.0 | 2024-12-15 | Data Science Team | Retrained with Q4 data, improved recall |
| 1.2.3 | 2025-01-15 | Data Science Team | Bug fix (memory leak), no model changes |

---

**Status**: Configuration-controlled per `00-PROGRAM/CONFIG_MGMT/`
