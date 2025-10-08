# CONTROL_PLAN

Process control plans defining parameters, inspection methods, and reaction plans.

## Overview

Control plans document the systematic approach to controlling manufacturing processes, including critical parameters, inspection methods, sample sizes, and reaction plans for out-of-control conditions.

## Control Plan Structure

### Header Information
- Part number and name
- Process/assembly name
- Supplier/location
- Key contact
- Revision date and level
- Approval signatures

### Control Plan Columns

1. **Control Number** - Unique identifier
2. **Process Step / Operation** - From process flow
3. **Process/Product Characteristic** - What is being controlled
4. **Specification / Tolerance** - Acceptance criteria
5. **Evaluation / Measurement Technique** - How to measure
6. **Sample Size** - Quantity inspected
7. **Sample Frequency** - How often to inspect
8. **Control Method** - Prevention or detection
9. **Reaction Plan** - Response to out-of-control situation
10. **Responsible** - Department/person

## Control Plan Types

### Prototype Control Plan
- Used during design validation
- Enhanced inspection and monitoring
- Data collection for process capability

### Pre-Launch Control Plan
- Used during pilot production
- Validate manufacturing processes
- Establish baseline capability

### Production Control Plan
- Ongoing production control
- Based on demonstrated process capability
- Balance of prevention and detection

## Control Methods

### Prevention Controls
- **Mistake-Proofing (Poka-Yoke):** Design prevents errors
- **Process Capability (Cpk ≥ 1.33):** Stable, capable process
- **Standard Work:** Documented procedures
- **Training:** Certified operators
- **Preventive Maintenance:** Equipment reliability

### Detection Controls
- **100% Inspection:** All parts checked (critical characteristics)
- **Statistical Process Control (SPC):** Control charts, trend analysis
- **Sample Inspection:** Periodic checks based on risk
- **First Article Inspection (FAI):** Setup verification
- **Gage R&R:** Measurement system validation

## Inspection Levels

### Level 1: 100% Inspection
**When to use:**
- Critical safety characteristics
- High severity PFMEA items (S = 9-10)
- New or unstable processes
- Customer requirement

**Example:** Torque on safety-critical fasteners

### Level 2: Statistical Process Control (SPC)
**When to use:**
- Capable processes (Cpk ≥ 1.33)
- High-volume operations
- Continuous improvement focus

**Example:** Dimensions on machined parts

### Level 3: Sample Inspection
**When to use:**
- Stable, capable processes
- Lower-risk characteristics
- Cost-effective approach

**Example:** Visual checks on non-critical features

### Level 4: First Piece / Setup Check
**When to use:**
- Stable processes
- Setup-sensitive operations
- Low-risk characteristics

**Example:** First piece after tool change

## Example Control Plans

### Aircraft Wing Spar - Hole Drilling

| # | Operation | Characteristic | Spec | Method | Size | Freq | Control | Reaction |
|---|-----------|----------------|------|--------|------|------|---------|----------|
| 1.1 | CNC drilling | Hole diameter | 6.35 ±0.05mm | CMM | 5 | Every 50 | SPC | Stop, adjust, re-verify |
| 1.2 | CNC drilling | Hole position | ±0.1mm | CMM | 5 | Every 50 | SPC | Stop, adjust, re-verify |
| 1.3 | CNC drilling | Surface finish | 63 Ra max | Visual comp | 1 | First piece | Detection | Rework if needed |
| 1.4 | CNC drilling | Burr removal | No burrs | Visual | 100% | Each part | Detection | Deburr before next op |

### Spacecraft Bus - Harness Installation

| # | Operation | Characteristic | Spec | Method | Size | Freq | Control | Reaction |
|---|-----------|----------------|------|--------|------|---------|---------|----------|
| 2.1 | Harness routing | Route per drawing | DWG-XXX | Visual check | 100% | Each | Prevention | Correct and re-inspect |
| 2.2 | Connector mating | Torque | 0.5-0.7 Nm | Torque wrench | 100% | Each | Prevention | Re-torque if out of spec |
| 2.3 | Connector mating | Pins intact | No damage | Visual | 100% | Each | Detection | Replace connector |
| 2.4 | Continuity | Continuity OK | Per schematic | Multimeter | 100% | Each | Detection | Troubleshoot and repair |

## Reaction Plans

### Typical Reaction Plan Components
1. **Immediate Action:** Stop production, contain suspect parts
2. **Investigation:** Determine root cause (5 Whys, fishbone)
3. **Corrective Action:** Fix the problem
4. **Verification:** Confirm fix is effective
5. **Prevention:** Update process/training to prevent recurrence

### Example Reaction Plan: Out-of-Tolerance Dimension

**Immediate:**
- Tag and quarantine last 10 parts produced
- Stop production on affected operation
- Notify supervisor and quality

**Investigation:**
- Check tool wear and condition
- Verify CMM calibration
- Review process parameters

**Corrective Action:**
- Replace worn tool
- Adjust machine offsets
- Verify first piece in tolerance

**Verification:**
- Measure 5 consecutive pieces
- Resume production if all in specification

**Prevention:**
- Reduce tool life or implement predictive maintenance
- Update tool change schedule

## Statistical Process Control (SPC)

### Control Chart Types
- **X-bar and R Chart:** Variable data, small subgroups
- **X and MR Chart:** Individual measurements
- **p Chart:** Proportion defective (attribute data)
- **c Chart:** Count of defects (attribute data)

### Control Limits
- **UCL/LCL:** Upper/Lower Control Limits (±3 sigma)
- **Specification Limits:** Customer requirements (different from control limits)

### Out-of-Control Rules
1. **Single point outside control limits**
2. **Run of 8 points on one side of centerline**
3. **Trend of 6+ points increasing or decreasing**
4. **Cycling pattern (14 points alternating)**

## Process Capability

### Capability Indices
- **Cp:** Process capability (specification width / process width)
- **Cpk:** Process capability accounting for centering
- **Ppk:** Process performance (includes long-term variation)

### Acceptance Criteria
- **Cpk ≥ 1.67:** Preferred (highly capable)
- **Cpk ≥ 1.33:** Acceptable (capable)
- **Cpk < 1.33:** Requires improvement or enhanced control

## Documentation and Maintenance

### Document Control
- Unique control plan number
- Revision level and history
- Approval signatures (manufacturing, quality, engineering)
- Distribution list

### Review and Update
- **Annual review:** Minimum frequency
- **Triggered reviews:** Process changes, quality issues, customer feedback
- **Continuous improvement:** Update based on Kaizen activities

## Integration Points

- Link to **PFMEA/** for risk-based control decisions
- Link to **PROCESS_FLOW.md** for process steps
- Link to **08-QUALITY/INSPECTION_PLANS/** for detailed inspection procedures
- Link to **08-QUALITY/MSA_SPC/** for measurement and statistical methods
- Link to **06-WORK_INSTRUCTIONS/** for operator procedures
- Link to **18-TEMPLATES** for control plan template

## References

- AIAG APQP manual
- AS9145 (APQP/PPAP for aerospace)
- ISO 9001 requirements for process control
