# TOOLS

**📍 [IDEALE-EU](../../../../../) > [02-AIRCRAFT](../../../../) > [DIGITAL_TWIN_MODEL](../../../) > 02-MODELS/CO_SIMULATION/FMU_FMI > TOOLS**

Utility scripts, build tools, and helper programs for FMU development and testing.

## Purpose

This directory contains tools and scripts to support:
- FMU building and packaging
- Test vector execution
- Co-simulation orchestration
- Result analysis and visualization
- FMU compliance checking

## Directory Structure

```
TOOLS/
├── cmake/              # CMake build configuration for FMU compilation
├── scripts/            # Python/shell scripts for automation
│   ├── run_test_vector.py
│   ├── run_all_test_vectors.py
│   ├── pack_fmu.sh
│   ├── simulate.py
│   └── validate_signals.py
└── README.md
```

## Scripts

### run_test_vector.py
**Execute a single test vector with FMU co-simulation**

```bash
python run_test_vector.py --test-vector ../TESTS/VECTORS/TV-ATA27-001_elevator_step.yaml \
                          --output ../SIM/results/ \
                          --verbose
```

**Features:**
- Loads test vector from YAML
- Initializes FMUs with initial conditions
- Executes test sequence
- Validates results against pass/fail criteria
- Generates CSV results and text report

**Output:**
- `{test_id}_results.csv` - Time series data
- `{test_id}_report.txt` - Test execution report

### run_all_test_vectors.py (TODO)
**Execute all test vectors in a directory**

```bash
python run_all_test_vectors.py --test-dir ../TESTS/VECTORS/ \
                                --output ../SIM/results/ \
                                --report ../EVIDENCE/test_report.html
```

**Features:**
- Batch execution of multiple test vectors
- Parallel execution support
- Consolidated HTML report with pass/fail summary
- Traceability matrix generation

### pack_fmu.sh (TODO)
**Package FMU from source code**

```bash
./pack_fmu.sh --component Control_FMU \
              --version 1.0.0 \
              --fmi-version 3.0 \
              --type co-simulation
```

**Process:**
1. Compile C/C++/Modelica source
2. Generate modelDescription.xml
3. Package binaries and resources
4. Create .fmu ZIP archive
5. Validate with FMI Compliance Checker

### simulate.py (TODO)
**Interactive co-simulation runner**

```bash
python simulate.py --scenario ../SIM/scenarios/cruise_flight.yaml \
                   --duration 300 \
                   --real-time \
                   --visualize
```

**Features:**
- Load scenario configuration
- Initialize all FMUs
- Run co-simulation with master algorithm
- Real-time visualization (optional)
- Save results to CSV/MAT format

### validate_signals.py (TODO)
**Validate signal interface definitions**

```bash
python validate_signals.py --signals ../INTERFACES/signals.yaml \
                            --fmu-dir ../COMPONENTS/ \
                            --report validation_report.txt
```

**Checks:**
- Signal names match between YAML and FMU modelDescription.xml
- Units are consistent
- Ranges are within physical limits
- Sample rates meet requirements
- EBOM references are valid

## CMake Configuration

### Building FMUs with CMake
```bash
cd cmake/
mkdir build && cd build
cmake .. -DFMU_NAME=Control_FMU -DFMI_VERSION=3.0
make
make package
```

**CMake options:**
- `FMU_NAME`: Name of the FMU to build
- `FMI_VERSION`: 2.0 or 3.0
- `FMI_TYPE`: co-simulation or model-exchange
- `BUILD_TESTS`: Enable/disable unit tests

## Dependencies

### Python Packages
```bash
pip install -r requirements.txt
```

Required packages:
- `pyyaml` - YAML parsing
- `numpy` - Numerical operations
- `pandas` - Data manipulation
- `matplotlib` - Plotting
- `fmpy` - FMU simulation and validation
- `pytest` - Testing framework

### System Tools
- CMake 3.15+
- GCC/Clang compiler
- FMI Compliance Checker
- Git

## Usage Examples

### Example 1: Run Single Test Vector
```bash
cd TOOLS/scripts
python run_test_vector.py \
    --test-vector ../../TESTS/VECTORS/TV-ATA27-001_elevator_step.yaml \
    --output ../../SIM/results/ \
    --verbose
```

### Example 2: Batch Test Execution (TODO)
```bash
cd TOOLS/scripts
python run_all_test_vectors.py \
    --test-dir ../../TESTS/VECTORS/ \
    --output ../../SIM/results/ \
    --parallel 4 \
    --report ../../EVIDENCE/test_summary.html
```

### Example 3: Build and Package FMU (TODO)
```bash
cd TOOLS/scripts
./pack_fmu.sh \
    --component Control_FMU \
    --source ../../COMPONENTS/Control_FMU/src/ \
    --output ../../COMPONENTS/Control_FMU/fmu/ \
    --version 1.2.0 \
    --fmi-version 3.0
```

### Example 4: Interactive Simulation (TODO)
```bash
cd TOOLS/scripts
python simulate.py \
    --scenario ../../SIM/scenarios/01_cruise_flight.yaml \
    --duration 300 \
    --step-size 0.01 \
    --real-time \
    --visualize \
    --output ../../SIM/results/
```

## Integration with CI/CD

### Continuous Integration
Test vectors are automatically executed on:
- Every commit to FMU source code
- Pull request validation
- Nightly regression tests

**GitHub Actions workflow example:**
```yaml
name: FMU Test Vectors
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Setup Python
        uses: actions/setup-python@v2
      - name: Install dependencies
        run: pip install -r requirements.txt
      - name: Run test vectors
        run: python run_all_test_vectors.py --test-dir ../TESTS/VECTORS/
      - name: Upload results
        uses: actions/upload-artifact@v2
        with:
          name: test-results
          path: ../SIM/results/
```

## Best Practices

### Script Development
1. **Use argparse**: Clear command-line interfaces
2. **Logging**: Use Python logging module
3. **Error handling**: Graceful failure with informative messages
4. **Documentation**: Docstrings and inline comments
5. **Version control**: All scripts in Git

### Test Automation
1. **Deterministic**: Tests should be repeatable
2. **Independent**: No dependencies between test vectors
3. **Fast**: Optimize for quick execution
4. **Clear output**: Pass/fail with detailed diagnostics

### FMU Building
1. **Version control**: Track FMU versions
2. **Reproducible builds**: Same input → same output
3. **Validation**: Always run compliance checker
4. **Documentation**: Update README with each build

## Related Documents

- [run_test_vector.py](scripts/run_test_vector.py) - Test vector execution script
- [../TESTS/VECTORS/](../TESTS/VECTORS/) - Test vector definitions
- [../SIM/](../SIM/) - Simulation scenarios and results
- [../COMPONENTS/](../COMPONENTS/) - FMU source code and binaries

## Change History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2025-10-11 | Digital Twin Team | Initial tools and scripts |

---

**Status**: Configuration-controlled per `00-PROGRAM/CONFIG_MGMT/`
