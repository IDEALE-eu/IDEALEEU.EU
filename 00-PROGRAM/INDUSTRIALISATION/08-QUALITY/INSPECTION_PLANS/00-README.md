# INSPECTION_PLANS

Inspection and test plans for manufacturing operations.

## Overview

Inspection plans define what to inspect, how to inspect, and acceptance criteria to ensure product conformance.

## Inspection Plan Contents

### Part Identification
- Part number and description
- Revision level
- Drawing reference

### Characteristics to Inspect
- Dimensions, features, attributes
- From drawing, specification, and control plan
- Critical characteristics highlighted

### Inspection Method
- Measurement technique (CMM, caliper, gage, visual)
- Equipment or gage identification
- Sample size and frequency (100%, sample, first-piece)

### Acceptance Criteria
- Tolerances from drawing
- Visual standards or limits
- Go/no-go criteria

### Reaction Plan
- Non-conformance procedure
- Quarantine and NCR process
- Responsible party notification

## Inspection Levels

### Receiving Inspection
- Verify supplier parts and materials
- Material certifications reviewed
- Dimensional and functional checks per risk
- Release or reject for production use

### In-Process Inspection
- First-piece checks after setup
- In-station inspections per control plan
- Roving inspections by quality
- SPC monitoring

### Final Inspection
- 100% inspection of critical characteristics
- Sample inspection of non-critical
- Functional testing
- Documentation review (travelers, certs, etc.)
- Accept or reject for delivery

## Inspection Methods

### Dimensional
- CMM (Coordinate Measuring Machine): High precision, complex geometry
- Optical comparators: Profile and 2D features
- Calipers, micrometers: General dimensions
- Height gages, surface plates: Setup and datum
- Custom gages: Go/no-go, templates

### Visual
- Magnification: Optical, microscope for small features
- Lighting: Proper illumination and angle
- Standards: Color chips, texture standards
- Criteria: Scratches, dents, finish quality

### Functional
- Performance testing: Verify operational requirements
- Pressure testing: Leak checks, proof tests
- Electrical testing: Continuity, hi-pot, functional
- Environmental: Temperature, humidity, vibration

### Non-Destructive Testing (NDT)
- See **03-PROCESS_PLANNING/SPECIAL_PROCESSES/NDT/**
- Ultrasonic, radiography, penetrant, magnetic particle

## Sampling Plans

### 100% Inspection
- Critical safety characteristics
- High-risk or unstable processes
- Customer requirement
- Cost-effective for low volume

### Statistical Sampling
- Stable, capable processes (Cpk ≥ 1.33)
- Sampling per ANSI/ASQC Z1.4 (formerly MIL-STD-105)
- AQL (Acceptable Quality Level) defined
- Sample size and accept/reject criteria

### First-Piece Inspection
- After setup or tool change
- Verifies setup correctness before production run
- All characteristics checked on first piece
- Periodic re-checks during run

## Inspection Records

### Documentation
- Inspection report or traveler
- Actual measurements or test results
- Inspector identification and date
- Stamp or signature for acceptance

### Record Retention
- **Flight-critical parts:** Permanent
- **Non-critical parts:** Minimum 10 years
- **Digital archival:** Secure backup

## Links
- To **03-PROCESS_PLANNING/CONTROL_PLAN/** for inspection requirements
- To **05-TOOLING_JIGS_FIXTURES/GAUGE_CALIBRATION/** for measurement equipment
- To **AS9102_FAI/** for first article inspection
- To **MSA_SPC/** for measurement system validation
