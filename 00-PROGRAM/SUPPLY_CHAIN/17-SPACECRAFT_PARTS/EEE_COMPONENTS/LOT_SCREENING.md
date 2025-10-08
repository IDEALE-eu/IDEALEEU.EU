# Lot Screening Procedures

## Overview

Lot acceptance and screening to ensure quality and reliability of EEE components for space.

## Lot Acceptance Criteria

### Certificate of Conformance (COC)
- Manufacturer name and part number
- Lot date code or traceability code
- Quantity in lot
- Inspection and test results
- Compliance with specifications
- Authorized signature

### Lot Date Code
- Manufacturing date code
- Traceability to manufacturing lot
- Age limits (typically <2 years for semiconductors)
- Homogeneous lot (same manufacturing run)

### Visual Inspection
- External visual per MIL-STD-883 Method 2009
- Markings legible and correct
- No physical damage
- Package integrity

## Screening Flow

### Level 1: Basic Screening (All Lots)
1. **Incoming Inspection:**
   - COC review
   - Visual inspection
   - Package integrity
   - Marking verification

2. **Electrical Testing:**
   - 100% electrical screening per datasheet parameters
   - Parametric limits per specification
   - Temperature testing if required

### Level 2: Environmental Screening (Flight Critical)
1. **Pre-Burn-In Electrical:**
   - Baseline electrical parameters

2. **Burn-In:**
   - Temperature: Per MIL-STD-883 Method 1015 (125°C typical, 168-240 hours)
   - Bias conditions: Worst-case or power-on
   - Monitoring for failures

3. **Post-Burn-In Electrical:**
   - Re-test electrical parameters
   - Accept/reject based on drift and limits

4. **Temperature Cycling:**
   - Per MIL-STD-883 Method 1010
   - Typically -55°C to +125°C
   - 10-20 cycles
   - Electrical testing before/after

5. **Constant Acceleration (Centrifuge):**
   - Per MIL-STD-883 Method 2001
   - 30,000 G for 1 minute (small parts)
   - Detects internal defects

6. **Fine and Gross Leak:**
   - Hermetic packages only
   - Per MIL-STD-883 Methods 1014 (fine) and 1014 (gross)
   - Helium leak detection

7. **X-Ray (Radiography):**
   - Per MIL-STD-883 Method 2012
   - 100% X-ray for bondwire and die attach inspection
   - Identify voids, shorts, foreign material

8. **Destructive Physical Analysis (DPA):**
   - Performed on sample (typically 3-5 units per lot)
   - Cross-sectioning and microscopy
   - Bondwire pull, die shear tests
   - Internal visual inspection
   - Per MIL-STD-1580 or NASA-STD-8739.1

## Screening Test Matrix

| Part Type | Level 1 | Level 2 | DPA Sample |
|-----------|---------|---------|------------|
| Resistors | 100% Electrical | Temperature Cycling, Constant Accel | 3 units |
| Capacitors | 100% Electrical | Temperature Cycling, Constant Accel, Leak Test (if hermetic) | 3 units |
| Diodes | 100% Electrical | Burn-In, Temperature Cycling, Constant Accel | 3 units |
| Transistors | 100% Electrical | Burn-In, Temperature Cycling, Constant Accel, X-Ray | 5 units |
| ICs (Digital) | 100% Electrical | Burn-In, Temperature Cycling, Constant Accel, X-Ray | 5 units |
| ICs (Analog) | 100% Electrical | Burn-In, Temperature Cycling, Constant Accel, X-Ray | 5 units |
| Power Devices | 100% Electrical | Burn-In, Temperature Cycling, X-Ray | 5 units |
| Optoelectronics | 100% Electrical | Burn-In, Temperature Cycling | 3 units |
| Connectors | Visual, Mating Test | Temperature Cycling, Vibration | 3 units |
| Relays | Functional Test | Temperature Cycling, Vibration, Life Test | 3 units |

## Acceptance Criteria

### Electrical Parameters
- All parameters within datasheet limits
- No parametric drift beyond allowed percentage after stress
- No infant mortality failures during burn-in

### Visual and X-Ray
- No defects (voids, cracks, foreign material, shorts)
- Bondwires intact and properly placed
- Die attach adequate

### DPA
- Internal construction per specification
- No workmanship defects
- Pull and shear tests meet minimums

## Lot Rejection

### Criteria for Rejection
- COC incomplete or non-compliant
- Electrical failures exceed acceptable quality level (AQL)
- Physical or internal defects found
- DPA reveals workmanship or material issues
- Counterfeit or suspect

### Process
1. Quarantine lot immediately
2. Document nonconformance
3. Notify manufacturer and procurement
4. Disposition (return, scrap, use-as-is with waiver)
5. Investigate root cause
6. SCAR to manufacturer if applicable

## Documentation

### Screening Report
- Lot identification and traceability
- Quantity screened
- Test procedures and standards used
- Test results (pass/fail, data)
- Defects and failures noted
- DPA summary
- Accept/reject recommendation
- Signed and dated

### Records Retention
- Lifetime of program
- Electronic and physical copies
- Linked to flight hardware traceability
- Available for audits and reviews

## Screening Facilities

### Internal Lab
- Company-owned screening facility
- Controlled environment
- Qualified personnel
- Equipment calibrated and maintained
- ECSS or NASA-compliant

### Third-Party Lab
- Accredited screening laboratory
- NADCAP or similar accreditation
- Approved by customer (if required)
- Audit and oversight by company

## Continuous Improvement

- Monitor screening effectiveness (escape rate)
- Feedback to manufacturers
- Adjust screening based on part performance
- Industry best practices
- Technology advancements in screening
