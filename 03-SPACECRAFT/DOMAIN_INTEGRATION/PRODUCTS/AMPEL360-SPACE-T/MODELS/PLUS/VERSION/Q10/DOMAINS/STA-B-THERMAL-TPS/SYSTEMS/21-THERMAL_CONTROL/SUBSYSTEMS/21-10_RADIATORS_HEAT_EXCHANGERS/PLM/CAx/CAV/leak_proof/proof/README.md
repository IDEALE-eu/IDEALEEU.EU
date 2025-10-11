# PROOF — Proof Pressure Testing

## Purpose

This directory contains proof pressure test data demonstrating structural integrity at 1.5× Maximum Expected Operating Pressure (MEOP).

## Contents

- Pressure vs. time traces
- Hold duration verification
- Strain gauge data (if installed)
- Deformation measurements
- Pre/post-test inspection photos
- Test certificates

## File Naming Convention

```
PROOF_<serial>_<meop>_<date>.<ext>
```

Examples:
- `PROOF_RAD-SN001_150psi_20251011.csv`
- `PROOF_HX-SN005_225psi_20251012.pdf`
- `PROOF_CP123_300psi_20251015_cert.pdf`

## Test Requirements

### Proof Pressure
- Pressure = 1.5 × MEOP
- Hold duration: 5 minutes minimum (or per requirement)
- Pressure stability: ±2% of setpoint

### Acceptance Criteria
- ✅ No pressure drop during hold
- ✅ No permanent deformation
- ✅ No leaks initiated
- ✅ No structural damage

## Test Procedure

### Pre-Test
1. Visual inspection and photos
2. Dimensional measurements (if required)
3. Helium leak test (baseline)
4. Install pressure monitoring

### Pressurization
1. Pressurize gradually to proof pressure
2. Ramp rate: typically 10-50 psi/min
3. Monitor for anomalies
4. All personnel clear of test area

### Hold Period
1. Maintain pressure for required duration
2. Monitor pressure continuously
3. Record any pressure decay
4. Visual inspection (remote cameras)

### Depressurization
1. Depressurize gradually
2. Monitor for damage indicators
3. Return to ambient pressure

### Post-Test
1. Visual inspection and photos
2. Dimensional measurements (verify no permanent set)
3. Helium leak test (verify no new leaks)
4. Document test results

## Data Collection

Record continuously:
- Time (elapsed from test start)
- Pressure (psi or bar)
- Temperature (if temperature-sensitive)
- Strain (if gauges installed)

Document:
- Pressurization rate achieved
- Peak pressure reached
- Hold duration achieved
- Any pressure decay observed
- Post-test inspection findings

## Safety Requirements

During proof testing:
- ⚠️ **Blast shield** or pressure containment
- 🚫 **No personnel** in test area
- 📹 **Remote monitoring** only
- 🔴 **Overpressure relief** set at 1.6× MEOP
- 🛑 **Abort criteria** defined

## Test Certification

Upon successful proof test:
- Issue proof test certificate
- Include test date, serial, pressures
- Test engineer signature
- QA witness signature
- Include pressure trace plot

## Related Directories

- **[../sniffer/](../sniffer/)** — Pre/post leak testing
- **[../burst/](../burst/)** — Burst test data
- **[../../procedures/](../../procedures/)** — Proof test procedures
- **[../../reports/](../../reports/)** — Test reports

---

**Last Updated**: 2025-10-10
