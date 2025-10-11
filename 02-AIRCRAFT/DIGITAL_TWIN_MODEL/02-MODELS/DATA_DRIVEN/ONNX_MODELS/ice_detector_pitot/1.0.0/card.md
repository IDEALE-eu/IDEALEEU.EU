# Model Card - Ice Detector (Pitot Tube)

**Model ID**: ice_detector_pitot  
**Version**: 1.0.0  
**Date**: 2024-12-01  
**Owner**: AI/ML Team - Sensor Health  
**ATA Chapter**: ATA-34-12 (Pitot-Static System)

---

## Model Details

### Model Type
- [x] Data-Driven (ML)
- [ ] Physics-Based
- [ ] Behavioral
- [ ] Hybrid

### Algorithm
Autoencoder (neural network) for anomaly detection

### Framework/Library
TensorFlow 2.14, exported to ONNX 1.14 (opset 17)

### Model Architecture
- **Encoder**: 50 → 32 → 16 (ReLU activation)
- **Decoder**: 16 → 32 → 50 (ReLU activation)
- **Loss**: Mean Squared Error (MSE)
- **Training**: Adam optimizer, learning rate 0.001, 100 epochs

---

## Intended Use

### Primary Use Case
Detect ice formation on pitot tube sensors by identifying anomalous patterns in sensor readings.

### Target Environment
- **Deployment**: Aircraft edge compute unit (ECU)
- **Real-time**: Yes (10 Hz update rate)
- **Certification**: DO-178C Level D

### Intended Users
- Flight control systems (automated alerts)
- Flight crew (cockpit warnings)
- Maintenance personnel (post-flight analysis)

---

## Training Data

### Dataset
- **Source**: Fleet telemetry + simulation data
- **Size**: 125,000 labeled samples
- **Split**: 70% train, 15% validation, 15% test
- **Time period**: 2023-Q1 to 2024-Q3
- **Aircraft types**: BWB-H2-Hy-E (AMPEL360-AIR-T)

### Data Collection
- Normal operations: 95,000 samples
- Ice conditions (simulated): 20,000 samples
- Sensor faults: 10,000 samples

### Labeling
- Automated labels from simulator ground truth
- Manual validation of 10% of samples by domain experts
- Inter-annotator agreement: 95%

---

## Model Performance

### Metrics (Test Set)
- **Accuracy**: 94%
- **Precision**: 91%
- **Recall**: 89%
- **F1 Score**: 90%
- **False Positive Rate**: 5%
- **False Negative Rate**: 11%

### Quantized Variants
- **FP16**: 94% accuracy (< 1% degradation)
- **INT8**: 92% accuracy (~2% degradation, acceptable)

### Edge Cases
- Extreme temperatures (-60 to 50°C): 91% accuracy
- Rapid altitude changes: 93% accuracy
- Sensor noise (SNR < 15dB): 90% accuracy

---

## Limitations and Assumptions

### Assumptions
1. Sensor data quality: No systematic sensor faults
2. Training data representativeness: Covers 95% of operational envelope
3. Ice scenarios: Model trained on ice formation >10 ppm (smaller accumulations not detectable)

### Known Limitations
1. **False Positives**: ~5% false positive rate (alert when no ice)
2. **Novel Scenarios**: May not detect ice in conditions not in training data
3. **Latency**: 15ms inference time on baseline FP32 (may miss very fast transients)

### Out-of-Scope
- Ice localization (model only detects, does not localize)
- Other pitot sensor anomalies (focus is ice formation only)
- Multi-sensor fusion (single pitot tube only)

---

## Fairness and Bias

Not applicable - sensor data has no demographic dimensions.

---

## Ethical Considerations

### Safety-Critical Context
This model operates in a safety-critical aviation environment. False negatives could result in undetected ice formation, while false positives may cause unnecessary alerts.

### Mitigation Strategies
- Persistence logic (3 consecutive violations before alert)
- Human-in-the-loop for critical decisions
- Redundant ice detection methods (e.g., backup physical sensors)
- Regular retraining with new flight data

---

## Maintenance and Updates

### Monitoring
- **Drift Detection**: Population Stability Index (PSI) monitored daily (alert if >0.25)
- **Performance Tracking**: Accuracy tracked weekly on recent data

### Retraining Triggers
- Drift detected (PSI >0.25 for 7 consecutive days)
- Performance degradation (accuracy <90%)
- New ice scenarios identified
- Sensor hardware changes

### Update Policy
See `../../08-SYNCHRONISATION/UPDATE_POLICY.md` (Ring deployment, 30-day shadow mode)

---

## Explainability

### Model Interpretability
Partial interpretability via reconstruction error heatmap (shows which sensors contribute most to anomaly score).

### Feature Importance
Top 5 features for ice detection:
1. Differential pressure (pitot-static)
2. Pitot heater current
3. Outside air temperature
4. Pitot temperature
5. Airspeed indicated

---

## Compliance

### Aviation Standards
- **DO-178C**: Level D (Low risk - advisory alerts only)
- **DO-254**: Not applicable (software-only model)

### Data Privacy
No personally identifiable information (PII) in training data.

### Export Control
EAR99 (not subject to ITAR restrictions)

---

## Contact

**Owner**: AI/ML Team - Sensor Health  
**Email**: ml-sensor-health@ideale-eu.eu  
**Documentation**: [ONNX_MODELS/ice_detector_pitot/1.0.0/](.)  
**Issue Tracker**: JIRA project IDEALE-ML

---

## Change History

| Version | Date       | Changes                                    | Author          |
|---------|------------|--------------------------------------------|-----------------|
| 1.0.0   | 2024-12-01 | Initial production release                 | AI/ML Team      |
| 0.9.0   | 2024-10-15 | Beta release for field testing             | AI/ML Team      |
