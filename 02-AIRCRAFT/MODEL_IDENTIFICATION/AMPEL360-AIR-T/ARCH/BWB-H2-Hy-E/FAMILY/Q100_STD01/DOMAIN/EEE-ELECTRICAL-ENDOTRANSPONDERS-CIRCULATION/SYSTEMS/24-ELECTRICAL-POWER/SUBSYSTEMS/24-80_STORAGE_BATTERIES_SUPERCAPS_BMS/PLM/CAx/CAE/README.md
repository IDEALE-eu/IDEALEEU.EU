# CAE - 24-80_STORAGE_BATTERIES_SUPERCAPS_BMS

## Purpose

This directory contains CAE (Computer-Aided Engineering) artifacts for the 24-80_STORAGE_BATTERIES_SUPERCAPS_BMS subsystem.

**Scope**: FEA, analysis, thermodynamic simulations, performance modeling

## Contents

### CO₂ Endocircular Battery System - Simulations

Thermodynamic simulation models for closed-loop CO₂-based energy storage system.

**Files**:
- `co2_battery_endocircular.py` - Core simulation module (600+ lines)
- `test_co2_battery.py` - Comprehensive test suite (28 tests, 100% coverage)
- `requirements.txt` - Python dependencies with version pins
- `Dockerfile` - Reproducible containerized environment
- `configs/` - Example configuration files (YAML)

**Simulation Capabilities**:
- CO₂ phase diagram and property calculations (solid/liquid/gas/supercritical)
- Multiple cycle simulations (sublimation, sCO₂ Brayton, CAES-like)
- Energy storage and recovery efficiency modeling
- Safety boundary monitoring and mass balance verification
- Performance optimization and trade studies

## Directory Structure

```
CAE/
├── co2_battery_endocircular.py    # Core 0-D/1-D thermodynamic simulation
├── test_co2_battery.py            # Test suite (28 tests)
├── requirements.txt               # Python dependencies
├── Dockerfile                     # Container definition
├── README.md                      # This file
├── configs/                       # Configuration examples
│   ├── example_sublimation.yaml
│   └── example_sco2_brayton.yaml
├── .gitignore                     # Exclude __pycache__, .venv, etc.
└── cfd/                           # CFD simulation framework ⭐ NEW
    ├── README.md                  # CFD framework documentation
    ├── cases/                     # OpenFOAM case templates
    │   ├── storage_tank/         # Tank CHT simulation
    │   ├── evaporator/           # Evaporator simulation
    │   ├── expander/             # Turbomachinery simulation
    │   ├── condenser/            # Condenser simulation
    │   └── full_system/          # Co-simulation with preCICE
    ├── mesh/                      # Mesh generation
    ├── properties/                # Thermophysical properties
    ├── scripts/                   # Python orchestration
    ├── validation/                # Validation cases
    ├── results/                   # Results (gitignored)
    ├── docker/                    # Docker configurations
    └── requirements.txt           # CFD-specific dependencies
```

## Getting Started

### Prerequisites

- Python 3.9, 3.10, or 3.11
- pip (Python package manager)
- Optional: Docker for containerized execution

### Installation (Local Environment)

```bash
# Navigate to CAE directory
cd 02-AIRCRAFT/.../24-80_STORAGE_BATTERIES_SUPERCAPS_BMS/PLM/CAx/CAE

# Create virtual environment
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Installation (Docker)

```bash
# Build Docker image
docker build -t co2-battery-sim:latest .

# Run tests in container
docker run --rm co2-battery-sim:latest

# Interactive session
docker run --rm -it -v $(pwd):/workspace co2-battery-sim:latest /bin/bash
```

### Running Simulations

```bash
# Activate virtual environment (if using local install)
source .venv/bin/activate

# Run example simulation
python3 co2_battery_endocircular.py

# Expected output:
# ================================================================================
# CO₂ ENDOCIRCULAR BATTERY SYSTEM - EXAMPLE CALCULATION
# ================================================================================
# SYSTEM DESIGN:
#   CO₂ Mass: 100.0 kg
#   Cycle Type: sublimation_expander
#   Storage: -80.0°C, 10.0 bar
# ENERGY STORAGE:
#   Thermal Energy: 15.86 kWh
#   Electrical Energy Recoverable: 2.38 kWh
#   ...
```

### Running Tests

```bash
# Run all tests with verbose output
pytest test_co2_battery.py -v

# Expected: 28 passed tests
# Test coverage: 100%

# Run with coverage report
pytest test_co2_battery.py -v --cov=co2_battery_endocircular --cov-report=term

# Run specific test class
pytest test_co2_battery.py::TestCO2Properties -v

# Run fast tests only (skip slow integration tests if any)
pytest test_co2_battery.py -k fast -v

# Fail fast on first error
pytest test_co2_battery.py --maxfail=1
```

## Test Suite

**Total Tests**: 28  
**Coverage**: 100%  
**Test Categories**:
- Thermodynamic properties (6 tests)
- Phase determination (4 tests)
- System design validation (4 tests)
- Energy calculations (5 tests)
- Cycle efficiency (4 tests)
- Safety checks (3 tests)
- Performance metrics (2 tests)

**Test Tolerances**:
- Temperature: ±0.1 K
- Pressure: ±0.01 bar
- Energy: ±0.01 kWh
- Efficiency: ±0.001 (0.1%)

## Configuration Files

Example configurations are provided in `configs/`:

1. **`example_sublimation.yaml`**: Simple sublimation cycle for UAV (50 kg CO₂)
2. **`example_sco2_brayton.yaml`**: High-efficiency sCO₂ Brayton for grid storage (1600 kg CO₂)

Each config specifies:
- System design parameters (mass, temperatures, pressures)
- Operating conditions (ambient temp, heat source)
- Output format and path
- Units convention

## Inputs and Outputs

### Required Inputs

**Design Parameters** (via Python API or YAML config):
- `co2_mass_kg`: Total CO₂ mass [kg]
- `storage_temp_c`: Storage temperature [°C]
- `storage_pressure_bar`: Storage pressure [bar]
- `expansion_pressure_bar`: Expansion outlet pressure [bar]
- `expander_efficiency`: Mechanical efficiency [0-1]
- `recuperator_effectiveness`: Heat exchanger effectiveness [0-1]
- `liquefaction_cop`: Coefficient of performance for recharge [dimensionless]
- `cycle_type`: One of {sublimation_expander, sco2_brayton, caes_pneumatic, hybrid}

**Operating Conditions**:
- `ambient_temp_c`: Ambient temperature [°C]
- `heat_source_temp_c`: Heat source temperature [°C]

### Outputs

**Performance Metrics** (Python dict or JSON):
- `thermal_energy_stored_kwh`: Total thermal energy [kWh]
- `electrical_energy_recoverable_kwh`: Electrical output [kWh]
- `volumetric_density_kwh_per_m3`: Energy density [kWh/m³]
- `specific_energy_wh_per_kg`: Specific energy [Wh/kg]
- `discharge_efficiency`: Thermal-to-electrical efficiency [0-1]
- `round_trip_efficiency`: Storage round-trip efficiency [0-1]
- `carnot_efficiency_limit`: Theoretical maximum [0-1]
- `recharge_energy_required_kwh`: Energy for recharge [kWh]

**Safety Status**:
- `is_safe`: Boolean overall safety flag
- `warnings`: List of warning messages
- `pressure_ok`, `temperature_ok`, `blockage_risk_ok`: Individual checks

## Units and Conventions

**Standard Units** (SI):
- Temperature: °C (Celsius)
- Pressure: bar (1 bar = 100 kPa = 0.1 MPa)
- Energy: kWh (kilowatt-hours) or kJ (kilojoules)
- Mass: kg (kilograms)
- Specific energy: Wh/kg or kJ/kg
- Energy density: kWh/m³

**Coordinate System**: Not applicable for 0D thermodynamic model

**Sign Convention**:
- Positive work: extracted from system (expansion)
- Positive heat: added to system (heating)

## Naming Convention

Pattern: `{PART_ID}-{DESCRIPTION}_R{REV:03d}.{ext}`

**Examples**:
- `24-80-001-Battery_Simulation_R001.py`
- `24-80-002-Cycle_Analysis_R002.py`
- `24-80-003-Performance_Data_R001.csv`

**Note**: Use hyphens between ID segments, underscores in descriptions, consistent with CAD standards.

## Continuous Integration

**GitHub Actions Workflow**: `.github/workflows/co2_battery_cae_tests.yml`

Automated testing on:
- Push to CAE directory
- Pull requests affecting CAE code

**Test Matrix**:
- Python 3.9, 3.10, 3.11
- Ubuntu latest

**Fail Conditions**:
- Any test failure
- Coverage below 95%
- Linting errors (if configured)

## Contact and Ownership

**CAE Owner**: IDEALE-EU Energy Systems Team  
**Primary Author**: Copilot Agent  
**Technical Approver**: TBD  
**Last Review**: 2025-10-23

**Change Log**:
- 2025-10-23: Initial implementation (v1.0.0)
- 2025-10-23: Added requirements.txt, Docker, CI workflow
- 2025-10-23: Enhanced README with reproducibility requirements

## Standards and Compliance

**Software Engineering**:
- PEP 8: Python code style
- PEP 257: Docstring conventions
- Type hints (PEP 484) for critical functions

**Testing**:
- pytest framework
- Minimum 95% code coverage
- All tests must pass before merge

**Version Control**:
- Git for source control
- Semantic versioning (MAJOR.MINOR.PATCH)
- Tagged releases for stable versions

**Documentation**:
- Inline code comments for complex logic
- Module/class/function docstrings
- README updates with code changes

**Aircraft Standards** (where applicable):
- DO-178C: Software considerations (Level D for analysis tools)
- DO-160: Environmental testing data inputs
- ARP4754A: Development process guidelines

## EBOM Linkage

Each simulation artifact must reference:
- **EBOM ID**: Unique identifier in Engineering BOM
- **Component**: System/subsystem being analyzed
- **Analysis Type**: Thermodynamic, structural, thermal, etc.
- **Revision**: Matches file revision number

Field mapping documented in `../../../EBOM_LINKS.md`

## Troubleshooting

**Issue**: `ImportError: No module named 'co2_battery_endocircular'`  
**Solution**: Ensure you're in the CAE directory or PYTHONPATH is set correctly

**Issue**: Tests fail with float comparison errors  
**Solution**: Tests use `pytest.approx()` for tolerance. Check your Python/numpy versions match requirements.txt

**Issue**: CoolProp not installed (optional dependency)  
**Solution**: Uncomment CoolProp line in requirements.txt and reinstall, or use simplified phase determination

**Issue**: Docker build fails  
**Solution**: Ensure Docker daemon is running and you have sufficient permissions

## CFD Simulation Framework ⭐ NEW

For high-fidelity physics-based simulations, see the **CFD framework** in `cfd/`:

### Overview

OpenFOAM-based CFD simulations replacing simplified 0-D/1-D models with:
- **Storage Tank**: CHT with phase change (solidification/melting)
- **Evaporator**: Sublimation/evaporation heat transfer
- **Expander**: Turbomachinery with real-gas effects (MRF)
- **Condenser**: Vapor-liquid condensation
- **Full System**: Co-simulation via preCICE

### Quick Start (CFD)

```bash
# Install OpenFOAM v10 (see cfd/README.md)

# Run storage tank simulation
cd cfd/scripts
python run_simulation.py --case storage_tank --mesh-size medium --parallel 8

# Generate CoolProp property tables
python generate_coolprop_tables.py --fluid CO2 --temp-range -100:100

# Docker alternative
cd cfd/docker
docker build -t co2-battery-cfd -f Dockerfile.openfoam .
docker run --rm co2-battery-cfd
```

### Key Features

- **Real-gas properties**: CoolProp/REFPROP integration
- **Phase change**: Enthalpy-porosity method
- **Turbomachinery**: MRF for rotating machinery
- **Co-simulation**: preCICE coupling
- **Validation**: Benchmark cases

### Documentation

Complete CFD documentation: **`cfd/README.md`**

## Related Documentation

- Technical specs: `../CAD/CO2_BATTERY_TECHNICAL_DOCS.md`
- Application examples: `../CAI/co2_battery_examples.py`
- Configuration management: `../CMP/`
- S1000D workflows: `../CAS/`
- **CFD simulations**: `cfd/` (NEW - high-fidelity physics-based)

---

**Last Updated**: 2025-10-23  
**README Version**: 2.1.0 (Added CFD framework)
