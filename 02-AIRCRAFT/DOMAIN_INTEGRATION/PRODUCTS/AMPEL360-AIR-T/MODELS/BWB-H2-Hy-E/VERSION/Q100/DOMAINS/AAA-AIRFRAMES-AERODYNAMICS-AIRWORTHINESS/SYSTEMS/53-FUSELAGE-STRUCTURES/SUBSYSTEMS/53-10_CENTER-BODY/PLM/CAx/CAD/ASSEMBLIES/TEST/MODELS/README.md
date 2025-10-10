# MODELS — Test Article CAD Models

## Purpose

This directory contains CAD models specifically created for test articles, including simplified geometries, instrumentation provisions, and fixture attachment points.

## Contents

### Model Types
- **Test article assemblies**: Complete test specimen models
- **Instrumented configurations**: Models with sensor mounting provisions
- **Simplified test articles**: Reduced-scope models for specific tests
- **Interface test specimens**: Models for interface verification testing

## Naming Convention

Use the following pattern:
```
53-10_TEST_MODEL_<test-type>_<identifier>_<version>.<ext>
```

Examples:
- `53-10_TEST_MODEL_STATIC_FRAME-F05_v01.CATProduct`
- `53-10_TEST_MODEL_FATIGUE_WING-ATTACH_v02.SLDPRT`
- `53-10_TEST_MODEL_PRESSURE_FULL-SECTION_v01.STEP`

## Model Requirements

Test models should include:
- Accurate geometry matching production intent
- Instrumentation mounting locations
- Load introduction points
- Boundary condition features
- Fixture attachment provisions
- Sensor/gauge installation features

## Documentation

Each test model should be accompanied by:
- Model history and revision notes
- Deviations from production design
- Instrumentation layout drawings
- Assembly sequence documentation
- Material specifications

## Related Directories

- **Drawings**: [`../DRAWINGS/`](../DRAWINGS/)
- **Test procedures**: [`../../../CAV/PROCEDURES/`](../../../CAV/PROCEDURES/)
- **Production models**: [`../../TOP_LEVEL/`](../../TOP_LEVEL/)
- **Fixtures**: [`../../FIXTURES/`](../../FIXTURES/)
