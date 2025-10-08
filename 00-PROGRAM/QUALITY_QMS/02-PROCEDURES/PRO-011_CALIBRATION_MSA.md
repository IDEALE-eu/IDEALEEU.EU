# PRO-011: Calibration and Measurement System Analysis

**Procedure Number:** PRO-011  
**Revision:** 1.0  
**Effective Date:** 2025-01-01  
**Owner:** Quality Manager

## 1. Purpose

Ensure measurement and test equipment is properly calibrated, maintained, and validated to provide reliable measurement data.

## 2. Scope

All measurement and test equipment used for:
- Inspection and testing
- Process control
- Verification and validation
- Calibration of other equipment

## 3. Responsibilities

- **Quality Manager:** Calibration program oversight
- **Calibration Coordinator:** Schedule, track, maintain records
- **Metrology Lab:** Perform calibrations (internal or external)
- **Equipment Users:** Proper use, storage, handling

## 4. Equipment Register

**Contents (EQUIPMENT_REGISTER.csv):**
- Equipment ID number
- Description and manufacturer
- Serial number
- Location/owner
- Calibration frequency
- Last calibration date
- Next calibration due date
- Calibration standard/procedure
- Status (In Service, Out of Service, Calibration Due)

## 5. Calibration Requirements

### 5.1 Calibration Standards

**Traceability:**
- NIST (National Institute of Standards and Technology)
- Equivalent national standards (NPL, PTB, etc.)
- Industry-accepted reference standards

**Hierarchy:**
- Primary standards (reference)
- Transfer standards
- Working standards
- Production equipment

### 5.2 Calibration Frequency

**Based on:**
- Manufacturer recommendations
- Usage frequency
- Historical stability
- Criticality of measurements
- Environmental conditions

**Typical Frequencies:**
- Micrometers, calipers: 12 months
- CMM, vision systems: 12 months
- Torque wrenches: 12 months or 5,000 cycles
- Thermocouples: 6 months
- Pressure/vacuum: 12 months
- Multimeters: 12 months
- Weights, standards: 24 months

### 5.3 Calibration Methods

**Internal Calibration:**
- Simple equipment
- Qualified metrology personnel
- Traceable standards
- Documented procedures

**External Calibration:**
- Complex equipment
- Specialized equipment
- ISO/IEC 17025 accredited lab preferred
- Certificate with traceability

## 6. Calibration Procedures

### 6.1 Calibration Process

1. Remove equipment from service
2. Clean and inspect for damage
3. Perform calibration per procedure
4. Record as-found and as-left data
5. Adjust if out of tolerance
6. Apply calibration label
7. Update calibration records
8. Return to service or repair if failed

### 6.2 Calibration Labels

**Information:**
- Equipment ID
- Calibration date
- Next calibration due date
- Calibrated by
- Status (Pass, Limited Use, Fail)

**Colors (optional):**
- Green: Current calibration
- Yellow: Due soon
- Red: Out of calibration

### 6.3 Out-of-Tolerance Handling

**Actions:**
1. Remove equipment from service immediately
2. Assess measurements since last calibration
3. Determine impact on product quality
4. Evaluate affected products (recall if needed)
5. Issue NCRs as appropriate (PRO-004)
6. Repair or replace equipment
7. Re-calibrate after repair
8. Document investigation and actions

## 7. Measurement System Analysis (MSA)

### 7.1 MSA Purpose

Quantify measurement system variation including:
- Repeatability (equipment variation)
- Reproducibility (operator variation)
- Bias (accuracy)
- Linearity (across range)
- Stability (over time)

### 7.2 Gage R&R Study

**Method:** ANOVA or Range method

**Acceptance Criteria:**
- **< 10%:** Acceptable
- **10-30%:** Marginal (may be acceptable depending on application)
- **> 30%:** Unacceptable (improve or replace)

**Study Design:**
- 3 operators minimum
- 10 parts spanning range
- 3 measurements per part per operator
- Random order

**Calculation:**
- %R&R = (Gage R&R / Total Variation) × 100%
- Or: %R&R = (Gage R&R / Tolerance) × 100%

### 7.3 Bias and Linearity

**Bias Study:**
- Compare measurements to known standard
- Bias = Measured - True value
- Acceptable if bias < 5% of tolerance

**Linearity Study:**
- Measure standards across operating range
- Plot bias vs. reference value
- Linear regression analysis
- Acceptable if slope ≈ 0

### 7.4 Attribute Gage Study

For Go/No-Go gages:
- 30 samples spanning accept/reject boundary
- 3 operators
- 3 trials each
- Calculate % agreement
- Target: > 90% agreement

## 8. Equipment Control

### 8.1 Identification

- Unique ID number
- Calibration label
- Equipment log

### 8.2 Storage and Handling

- Clean, dry environment
- Protective cases
- No exposure to excessive shock/vibration
- Temperature/humidity control

### 8.3 Calibration Alerts

- 30-day advance notice
- Weekly overdue report
- Automatic removal from service when overdue

### 8.4 Equipment Loans

- Check out system
- Verify calibration current
- Inspect upon return
- Re-calibrate if suspect damage

## 9. Environmental Conditions

**Metrology Lab:**
- Temperature: 20°C ± 1°C (68°F ± 2°F)
- Humidity: 45% ± 10% RH
- Vibration isolation
- Cleanliness control
- Environmental monitoring and recording

## 10. Records

- Equipment register (EQUIPMENT_REGISTER.csv)
- Calibration schedule (CAL_SCHEDULE.csv)
- Calibration certificates (CERTIFICATES/)
- MSA studies
- Out-of-tolerance investigations
- Equipment maintenance logs

**Retention:** Equipment lifetime + 10 years

## 11. Related Documents

- ISO/IEC 17025 (Calibration laboratories)
- ANSI/NCSL Z540.3 (Calibration systems)
- PRO-004_NONCONFORMANCE
- Section 08-CALIBRATION_METROLOGY/

## 12. Revision History

| Rev | Date | Description | Approved By |
|-----|------|-------------|-------------|
| 1.0 | 2025-01-01 | Initial release | Quality Manager |
