# QA — Quality Assurance

## Purpose

This directory contains quality assurance artifacts for CAE including:
- Test plans and procedures
- Acceptance criteria
- Regression test suites
- Quality reports

## Directory Structure

```
QA/
├─ README.md                    # This file
├─ test_plan.md                 # Overall QA test plan
├─ acceptance_criteria.md       # Acceptance criteria for cases
├─ regression_tests/            # Automated regression tests
│  ├─ compare_metrics.py        # Metric comparison script
│  ├─ test_cfd_cases.py         # CFD regression tests
│  └─ test_fea_cases.py         # FEA regression tests
└─ reports/                     # QA reports and results
   ├─ weekly/                   # Weekly regression reports
   └─ release/                  # Release qualification reports
```

## Test Plan

See `test_plan.md` for the complete test plan covering:
- Smoke tests (fast, coarse cases for CI)
- Regression tests (compare against baselines)
- Validation tests (compare against experimental data)
- Performance tests (runtime and scalability)

## Acceptance Criteria

See `acceptance_criteria.md` for criteria including:
- Convergence requirements
- Mesh quality thresholds
- Metric tolerances
- Documentation completeness

## Regression Testing

### Automated Tests

Regression tests run automatically in CI and compare results against baselines.

```bash
# Run all regression tests
python3 regression_tests/compare_metrics.py --all

# Run specific test
python3 regression_tests/test_cfd_cases.py --case tank_solidification
```

### Comparison Tolerance

Default tolerances for metric comparison:
- Mass: ±1%
- Energy: ±2%
- Temperature: ±2°C
- Flow rate: ±3%
- Runtime: Not checked (varies by machine)

### Test Results

Results are saved to `reports/` with timestamp:
```
reports/
└─ 2025-10-23_regression_results.json
```

## CI Integration

### Pipeline Steps
1. **Checkout**: Clone repository
2. **Setup**: Install dependencies
3. **Metadata Check**: Validate all metadata files
4. **Smoke Tests**: Run fast coarse cases
5. **Regression Tests**: Compare against baselines
6. **Report**: Generate and upload test report

### Success Criteria
- All metadata valid
- All smoke tests pass
- Regression metrics within tolerance
- Total CI time < 10 minutes

## Quality Metrics

Track these metrics over time:
- Smoke test pass rate
- Regression test pass rate
- Average convergence iterations
- Solver runtime trends
- Code coverage (for scripts)

## Reporting

### Weekly Reports
Generate weekly regression reports:
```bash
python3 regression_tests/generate_report.py --week 2025-W43
```

Report includes:
- Test summary (pass/fail counts)
- Failed cases with details
- Performance trends
- Action items

### Release Reports
Before each release, generate qualification report:
```bash
python3 regression_tests/generate_report.py --release v2.0
```

Release report includes:
- All regression test results
- Validation against experimental data
- Performance benchmarks
- Known issues and limitations

## Test Development

### Adding New Tests

1. Create test case in appropriate directory
2. Run case and generate baseline metrics
3. Add test to regression suite
4. Document test purpose and expected behavior

### Test Template

```python
import unittest
from pathlib import Path
from compare_metrics import compare_metrics

class TestCFDCase(unittest.TestCase):
    def test_tank_solidification(self):
        case_path = Path("CFD/cases/tank_solidification")
        baseline_path = case_path / "baseline/metrics.json"
        result_path = case_path / "case/metrics.json"
        
        passed, differences = compare_metrics(
            baseline_path, 
            result_path,
            tolerance=0.02
        )
        
        self.assertTrue(passed, f"Metrics differ: {differences}")
```

## Best Practices

1. **Automation**: Automate all tests that can be automated
2. **Fast Feedback**: Keep smoke tests fast (< 5 min each)
3. **Clear Failures**: Provide clear error messages
4. **Traceability**: Link tests to requirements
5. **Documentation**: Document test purpose and setup

## Troubleshooting

### Common Issues

**Smoke test failure**
- Check solver installation
- Verify input files
- Review error logs

**Regression metric mismatch**
- Check solver version
- Verify mesh files
- Review boundary conditions

**CI timeout**
- Reduce smoke case size
- Parallelize independent tests
- Optimize solver settings

## References

- CI Configuration: .github/workflows/
- Test Standards: See test_plan.md
- Metrics Definition: See acceptance_criteria.md

---

**Last Updated:** 2025-10-23
