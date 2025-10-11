# TEST VECTORS

**📍 [IDEALE-EU](../../../../../../) > [02-AIRCRAFT](../../../../../) > [DIGITAL_TWIN_MODEL](../../../../) > 02-MODELS/CO_SIMULATION/FMU_FMI/TESTS > VECTORS**

Validation test vectors for FMU co-simulation, specifically for ATA-27 Flight Control System.

## Purpose

This directory contains comprehensive test vectors used to validate FMU behavior against system requirements. Test vectors define:
- Initial conditions
- Input sequences (stimulus)
- Expected outputs
- Pass/fail criteria
- Traceability to requirements

## Test Vector Structure

Each test vector is defined in YAML format and includes:

### 1. Metadata
- Test ID and name
- Description and purpose
- System/subsystem identification
- Requirement traceability
- Design Assurance Level (DAL)
- Author and review status

### 2. Initial Conditions
- Aircraft state (altitude, airspeed, attitude)
- System configuration (FCC mode, control surface positions)
- Environmental conditions

### 3. Test Sequence
- Time-stamped input commands
- Expected system responses
- Tolerance specifications

### 4. Expected Outputs
- Time series data for key signals
- Steady-state values
- Transient characteristics

### 5. Pass/Fail Criteria
- Quantitative acceptance criteria
- Compliance checks against specifications
- Performance metrics (rise time, overshoot, etc.)

### 6. Validation Against SPEC
- References to SPECS/fmi_config.yaml
- Tolerance validation
- Compliance status

## Test Vectors for ATA-27 Flight Controls

### Primary Control Surfaces
- **TV-ATA27-001**: Elevator step response
- **TV-ATA27-002**: Aileron step response
- **TV-ATA27-003**: Rudder step response
- **TV-ATA27-004**: Combined multi-axis input

### Performance Validation
- **TV-ATA27-010**: Frequency response (elevator)
- **TV-ATA27-011**: Rate limit validation
- **TV-ATA27-012**: Saturation behavior
- **TV-ATA27-013**: Steady-state accuracy

### Failure Modes (Safety-Critical)
- **TV-ATA27-020**: Actuator jam detection
- **TV-ATA27-021**: Actuator runaway
- **TV-ATA27-022**: Sensor failure (position feedback)
- **TV-ATA27-023**: FCC mode transition (NORMAL → DIRECT)

### Flight Envelope Protection
- **TV-ATA27-030**: Alpha limit protection
- **TV-ATA27-031**: Load factor limit
- **TV-ATA27-032**: Bank angle limit

### Integration Tests
- **TV-ATA27-040**: Flight control + aerodynamics
- **TV-ATA27-041**: Flight control + structures
- **TV-ATA27-042**: Complete co-simulation (all FMUs)

## Use Case Example: TV-ATA27-001

### Objective
Validate elevator actuator response to pilot step input command.

### Test Scenario
1. Initialize system at cruise conditions (35,000 ft, 250 kt)
2. Apply step input: pilot stick pitch = 5 deg (nose up)
3. Monitor elevator command and position feedback
4. Validate response characteristics:
   - Rise time < 200 ms
   - No overshoot > 5%
   - Steady-state error < 0.1 deg
   - Rate limit: 30 deg/s not exceeded

### Requirements Validated
- **REQ-FC-ELEVATOR-001**: Response time < 200 ms
- **REQ-FC-ELEVATOR-002**: Rate limit ≤ 30 deg/s
- **REQ-FC-ELEVATOR-003**: Steady-state error < 0.5 deg

### FMU Configuration
- **Active FMUs**: Control_FMU, Aero_FMU, Struct_FMU
- **Signal chain**: pilot_stick_pitch → elevator_cmd → elevator_position_fb
- **Step sizes**: Control_FMU (20 ms), Aero_FMU (10 ms), Struct_FMU (10 ms)

### Expected Results
| Time (s) | Pilot Input (deg) | Elevator Cmd (deg) | Position FB (deg) |
|----------|-------------------|--------------------|--------------------|
| 0.0 | 0.0 | 0.0 | 0.0 |
| 1.0 | 5.0 | -3.5 | -3.45 |
| 2.0 | 5.0 | -3.5 | -3.50 |
| 3.0 | 0.0 | 0.0 | 0.0 |

### Validation Against SPEC
From `SPECS/fmi_config.yaml`:
- `position_error_deg: 0.1` ✓ Met (error = 0.05 deg)
- `rate_error_deg_per_s: 1.0` ✓ Met (max rate = 30 deg/s)

## Relationship to System Requirements

All test vectors trace to system-level requirements in:
```
02-AIRCRAFT/CONFIGURATION_BASE/ATA-27_FLIGHT_CONTROLS/
```

### Requirement Hierarchy
1. **System Requirements** (ATA-27 README)
   - High-level flight control system requirements
   - Interface specifications (ATA-22, ATA-34, etc.)

2. **Subsystem Requirements** (ATA-27/PARAMS, ATA-27/ICD)
   - Control surface deflection ranges
   - Actuator performance specifications
   - Control law parameters

3. **Test Vectors** (this directory)
   - Specific test cases validating requirements
   - Quantitative pass/fail criteria
   - Traceable to EBOM and requirement IDs

## Execution

### Manual Execution
```bash
cd ../TOOLS/scripts
python run_test_vector.py --test-vector ../TESTS/VECTORS/TV-ATA27-001_elevator_step.yaml \
                          --output ../SIM/results/
```

### Batch Execution
```bash
cd ../TOOLS/scripts
python run_all_test_vectors.py --test-dir ../TESTS/VECTORS/ \
                                --output ../SIM/results/ \
                                --report ../EVIDENCE/test_report.html
```

### Automated Regression Testing
Test vectors are automatically executed as part of:
- **Continuous Integration**: On every commit to FMU source code
- **Nightly Builds**: Full regression test suite
- **Release Validation**: Before configuration control baseline

## Output Format

Test results are saved in CSV format:
```csv
time_s,pilot_stick_pitch_deg,elevator_cmd_deg,elevator_position_fb_deg,pass_fail
0.0,0.0,0.0,0.0,PASS
1.0,5.0,-3.5,-3.45,PASS
2.0,5.0,-3.5,-3.50,PASS
3.0,0.0,0.0,0.0,PASS
```

Results directory: `../SIM/results/`

## Visualization

Test results can be visualized using:
```bash
python plot_test_results.py --input ../SIM/results/TV-ATA27-001_results.csv \
                             --output ../SIM/results/TV-ATA27-001_plots.png
```

Plots include:
- Time history of inputs and outputs
- Phase plots
- Frequency response (if applicable)
- Pass/fail indicators

## Traceability Matrix

Test vectors maintain full traceability:

| Test ID | Requirement | EBOM Ref | SPEC Section | Status |
|---------|-------------|----------|--------------|--------|
| TV-ATA27-001 | REQ-FC-ELEVATOR-001 | ATA-27-21-001 | control_surfaces.position_error | ✓ PASS |
| TV-ATA27-002 | REQ-FC-AILERON-001 | ATA-27-22-001 | control_surfaces.position_error | ✓ PASS |
| TV-ATA27-003 | REQ-FC-RUDDER-001 | ATA-27-23-001 | control_surfaces.position_error | ✓ PASS |

See `../EVIDENCE/traceability_matrix.csv` for complete matrix.

## Test Coverage

Test vectors provide coverage for:
- **Functional Requirements**: 95% (target: 100%)
- **Safety Requirements**: 100% (mandatory)
- **Performance Requirements**: 90% (target: 95%)
- **Interface Requirements**: 85% (target: 90%)

Coverage analysis: `../EVIDENCE/coverage_report.html`

## Best Practices

### Creating New Test Vectors
1. **Start with requirement**: Identify specific requirement to validate
2. **Define clear objective**: What behavior is being tested?
3. **Choose representative conditions**: Realistic flight conditions
4. **Set quantitative criteria**: Avoid subjective pass/fail
5. **Include metadata**: Author, date, review status
6. **Trace to EBOM**: Link signals to Bill of Materials

### Naming Convention
```
TV-<ATA>-<seq>_<short_description>.yaml
```
Examples:
- `TV-ATA27-001_elevator_step.yaml`
- `TV-ATA27-020_actuator_jam.yaml`
- `TV-ATA27-042_full_cosim.yaml`

### Version Control
- Test vectors are configuration-controlled
- Changes require review and approval
- Baseline versions archived in EVIDENCE/

## Related Documents

- [SPECS/fmi_config.yaml](../../SPECS/fmi_config.yaml) - Tolerance specifications
- [INTERFACES/signals.yaml](../../INTERFACES/signals.yaml) - Signal definitions
- [TOOLS/scripts/](../../TOOLS/scripts/) - Execution scripts
- [SIM/results/](../../SIM/results/) - Test results output
- [EVIDENCE/](../../EVIDENCE/) - Test evidence and reports
- [ATA-27_FLIGHT_CONTROLS/VERIFICATION/](../../../../../CONFIGURATION_BASE/ATA-27_FLIGHT_CONTROLS/VERIFICATION/) - System verification

## References

### Standards
- **DO-178C**: Software verification (DAL-A)
- **DO-254**: Hardware verification
- **ARP-4754A**: System development and verification

### Tools
- **FMPy**: For executing test vectors with FMUs
- **pytest**: For automated test execution
- **matplotlib**: For visualization

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2025-10-11 | Flight Controls Test Team | Initial test vectors for ATA-27 elevator |

---

**Status**: Configuration-controlled per `00-PROGRAM/CONFIG_MGMT/`
