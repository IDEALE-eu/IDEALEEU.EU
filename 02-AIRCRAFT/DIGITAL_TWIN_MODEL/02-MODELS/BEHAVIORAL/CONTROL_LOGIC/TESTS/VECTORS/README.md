# TESTS/VECTORS

Test vectors for validating control logic requirements.

## Contents

### [cases/](cases/)
Nominal test cases for functional validation:
- **[pitch_response_test.yaml](cases/pitch_response_test.yaml)** - Validates REQ-FCC-070 (pitch step response)
- Additional test cases to be added for roll, yaw, and other control modes

### [corner_cases/](corner_cases/)
Edge cases and limit testing:
- **[alpha_protection_test.yaml](corner_cases/alpha_protection_test.yaml)** - Validates REQ-FCC-041 (angle of attack protection)
- Additional corner cases for load factor limits, overspeed protection, etc.

## Purpose

Test vectors provide structured test definitions that:

- **Validate requirements**: Each test traces to specific requirements in [../SPEC/](../SPEC/)
- **Define inputs**: Time-based signal profiles using IDs from [../INTERFACES/signals.yaml](../INTERFACES/signals.yaml)
- **Specify expected outputs**: Performance metrics and acceptance criteria
- **Enable automation**: YAML format suitable for automated test execution
- **Provide traceability**: Links requirements → signals → tests → evidence

## Test Vector Structure

Each test vector YAML file contains:

```yaml
test_metadata:
  test_id: UNIQUE-ID-001
  requirement: REQ-FCC-XXX
  description: What is being tested
  
configuration:
  flight_condition: Initial conditions
  
inputs:
  - signal: signal_name
    profile: Time-based input sequence
    
expected_outputs:
  - signal: signal_name
    requirements: Expected behavior
    
performance_metrics:
  metric_name:
    requirement: Performance target
    limit: Pass/fail threshold
    
acceptance_criteria:
  - Pass/fail criteria
```

## Test Types

### Functional Tests (cases/)
- Validate normal operation
- Performance verification
- Mode transitions
- Example: Step response, frequency response, tracking

### Corner Cases (corner_cases/)
- Boundary conditions
- Envelope protection
- Failure scenarios
- Example: Maximum AoA, load factor limits, sensor failures

## Usage

### Creating a New Test Vector

1. **Identify the requirement** from [../SPEC/control_modes.md](../SPEC/control_modes.md)
2. **Select signal IDs** from [../INTERFACES/signals.yaml](../INTERFACES/signals.yaml)
3. **Define flight condition**: Altitude, speed, weight, CG, configuration
4. **Specify input profile**: Time-based sequence of input signals
5. **Define expected outputs**: What should happen and when
6. **Set acceptance criteria**: Pass/fail thresholds
7. **Add traceability**: Link to requirements and related tests

### Executing Test Vectors

```bash
# Software-in-the-Loop (SIL)
python ../SIM/harness/fcc_sil_harness.py --test cases/pitch_response_test.yaml

# Hardware-in-the-Loop (HIL)
python ../SIM/harness/fcc_hil_harness.py --test corner_cases/alpha_protection_test.yaml
```

Results are logged to [../EVIDENCE/test_results/](../EVIDENCE/test_results/)

## Test Coverage

Test vectors should provide:
- **Requirements coverage**: Every requirement has at least one test
- **Signal coverage**: All critical signals exercised
- **Condition coverage**: Various flight conditions (altitude, speed, configuration)
- **Failure coverage**: Sensor failures, actuator faults, mode transitions

## Related Documents

- [Requirements Specification](../SPEC/control_modes.md) - What to test
- [Signal Definitions](../INTERFACES/signals.yaml) - Signal IDs and properties
- [Control Parameters](../PARAMS/gains.yaml) - Gains used in tests
- [Test Evidence](../EVIDENCE/) - Test results and reports

---

**Status**: Configuration-controlled per `00-PROGRAM/CONFIG_MGMT/`
