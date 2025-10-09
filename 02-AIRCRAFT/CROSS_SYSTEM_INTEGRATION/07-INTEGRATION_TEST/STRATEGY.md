# Integration Test Strategy

## Overview

Aircraft cross-system integration testing follows a staged approach from lab simulation to flight test.

## Test Stages

### Stage 1: Lab Testing
- Component-level testing
- Interface testing (two LRUs)
- Network switch testing
- Timing verification

### Stage 2: HIL (Hardware-in-the-Loop)
- Integrated system testing with hardware LRUs
- Simulated sensors and actuators
- Real-time execution
- Fault injection

### Stage 3: Iron Bird (Full System Rig)
- Complete aircraft systems on ground rig
- Real actuators and sensors
- Flight scenarios execution
- Crew-in-the-loop testing

### Stage 4: Ground Testing (Aircraft)
- Systems integrated on actual aircraft
- Ground power and support equipment
- Taxi tests
- Electromagnetic compatibility (EMC) testing

### Stage 5: Flight Testing
- First flight and envelope expansion
- Functional flight tests per test plan
- Certification flight tests
- Validation of all functional chains

## Test Coverage

- 100% of functional chains (FC-001 through FC-020)
- 100% of interface matrix entries
- All hazard mitigations verified
- All DAL A/B software verified per DO-178C

## Test Evidence

All test results documented in [EVIDENCE/](./EVIDENCE/) folder with traceability to requirements.

## References
- [TEST_SPECIFICATIONS/](./TEST_SPECIFICATIONS/) - Detailed test cases
- [RIGS_HILSILS/](./RIGS_HILSILS/) - HIL/SIL configuration
- [TRACEABILITY.csv](./TRACEABILITY.csv) - Requirements traceability
