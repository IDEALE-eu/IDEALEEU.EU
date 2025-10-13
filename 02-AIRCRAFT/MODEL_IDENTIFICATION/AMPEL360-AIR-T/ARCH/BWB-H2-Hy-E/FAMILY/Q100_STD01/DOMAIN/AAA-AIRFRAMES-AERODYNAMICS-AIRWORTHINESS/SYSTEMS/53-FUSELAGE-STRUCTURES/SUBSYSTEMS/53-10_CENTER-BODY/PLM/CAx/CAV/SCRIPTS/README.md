# SCRIPTS — Automation Scripts

## Purpose

This directory contains automation scripts for data acquisition and processing, improving efficiency and consistency in the validation program.

## Directory Structure

### ACQ/
Data acquisition scripts for automated test data collection.

**Script Types**:
- DAQ system configuration scripts
- Real-time data monitoring scripts
- Automated trigger and control scripts
- Sensor calibration scripts
- Video/image capture automation

### PROCESSING/
Data processing and analysis scripts for post-test data reduction.

**Script Types**:
- Data filtering and conditioning scripts
- Calibration application scripts
- Derived quantity calculation scripts
- Statistical analysis scripts
- Plotting and visualization scripts
- Report generation scripts

## Script Standards

### Code Quality

All scripts must follow these standards:

1. **Documentation**
   - Header with script purpose, author, date
   - Function/class documentation
   - Inline comments for complex logic
   - README.md in each script directory

2. **Version Control**
   - Scripts under Git version control
   - Version number in script header
   - Change log maintained

3. **Error Handling**
   - Robust error handling and validation
   - Meaningful error messages
   - Graceful failure modes
   - Log file generation

4. **Testing**
   - Test with sample data before use
   - Validation against known results
   - Edge case testing

5. **Portability**
   - Use relative paths, not absolute paths
   - Document dependencies and versions
   - Provide environment setup instructions

### Supported Languages

- **Python** 3.8+ (preferred for data processing)
- **MATLAB** R2020a+ (for legacy compatibility)
- **LabVIEW** 2020+ (for DAQ systems)
- **Bash/PowerShell** (for system automation)

### Dependencies

Document all dependencies:
- Programming language version
- Required libraries and versions
- Operating system requirements
- Hardware requirements (if any)

## Acquisition Scripts (ACQ/)

### DAQ Configuration

**Purpose**: Configure data acquisition systems for test

**Typical Scripts**:
- `daq_config_static_test.py` — Configure DAQ for static test
- `daq_config_fatigue_test.py` — Configure DAQ for fatigue test
- `daq_config_vibration_test.py` — Configure DAQ for vibration test

**Contents**:
- Channel definitions
- Sampling rates
- Trigger configuration
- File naming and storage

### Real-Time Monitoring

**Purpose**: Monitor data during test execution

**Typical Scripts**:
- `realtime_monitor.py` — Display live data streams
- `safety_monitor.py` — Monitor safety limits and alarm
- `data_quality_check.py` — Real-time data quality assessment

### Calibration

**Purpose**: Apply calibrations to sensors and instruments

**Typical Scripts**:
- `strain_gauge_calibration.py` — Strain gauge calibration and shunt check
- `load_cell_calibration.py` — Load cell calibration
- `thermocouple_calibration.py` — Thermocouple calibration

## Processing Scripts (PROCESSING/)

### Data Filtering

**Purpose**: Filter and condition raw data

**Typical Scripts**:
- `apply_lowpass_filter.py` — Low-pass filter for noise reduction
- `remove_baseline_drift.py` — Remove baseline drift from signals
- `spike_removal.py` — Remove data spikes and outliers

### Data Reduction

**Purpose**: Calculate derived quantities from raw data

**Typical Scripts**:
- `calculate_stress_strain.py` — Calculate stress/strain from loads/deflections
- `calculate_frequency_response.py` — FFT and frequency domain analysis
- `extract_peak_values.py` — Extract peak values and statistics

### Plotting and Visualization

**Purpose**: Generate plots and visualizations

**Typical Scripts**:
- `plot_time_history.py` — Time history plots
- `plot_stress_strain.py` — Stress-strain curves
- `plot_frequency_spectrum.py` — Frequency spectrum plots
- `generate_contour_plots.py` — Contour plots for DIC data

### Report Generation

**Purpose**: Automate report generation

**Typical Scripts**:
- `generate_data_sheet.py` — Populate data sheet template
- `generate_quick_look.py` — Generate quick look report
- `compile_test_report.py` — Compile full test report

## Script Organization

### Directory Structure

```
SCRIPTS/
├─ ACQ/
│  ├─ daq/
│  │  ├─ daq_config_static_test.py
│  │  └─ daq_config_fatigue_test.py
│  ├─ monitoring/
│  │  ├─ realtime_monitor.py
│  │  └─ safety_monitor.py
│  └─ calibration/
│     └─ strain_gauge_calibration.py
├─ PROCESSING/
│  ├─ filtering/
│  │  ├─ apply_lowpass_filter.py
│  │  └─ remove_baseline_drift.py
│  ├─ analysis/
│  │  ├─ calculate_stress_strain.py
│  │  └─ calculate_frequency_response.py
│  └─ visualization/
│     ├─ plot_time_history.py
│     └─ generate_contour_plots.py
└─ COMMON/
   ├─ utils.py (common utilities)
   ├─ config.py (configuration)
   └─ data_io.py (data input/output)
```

### Naming Conventions

- **Files**: lowercase_with_underscores.py
- **Functions**: lowercase_with_underscores()
- **Classes**: PascalCase
- **Constants**: UPPERCASE_WITH_UNDERSCORES

## Usage Examples

### Example: Acquire Static Test Data

```bash
python ACQ/daq/daq_config_static_test.py --test-id QTP-53-10-100 --output-dir ../../DATA/RAW/
```

### Example: Process Strain Gauge Data

```bash
python PROCESSING/analysis/calculate_stress_strain.py \
  --input ../../DATA/RAW/QTP-53-10-100/strain_data.csv \
  --calibration ../../DATA/METADATA/QTP-53-10-100/strain_calibration.json \
  --output ../../DATA/PROCESSED/QTP-53-10-100/stress_strain.csv
```

### Example: Generate Quick Look Report

```bash
python PROCESSING/visualization/generate_quick_look.py \
  --test-id QTP-53-10-100 \
  --data-dir ../../DATA/PROCESSED/QTP-53-10-100/ \
  --output ../../REPORTS/Quick_Look_QTP-53-10-100.pdf
```

## Script Validation

Before using script on critical data:
1. Test with sample/simulated data
2. Validate output against known results
3. Review by independent engineer
4. Document validation in script header

## Script Repository

- Scripts maintained in this Git repository
- Version tagged for each test campaign
- Script changes tracked with commit messages
- Critical scripts require peer review before use

## References

- Data standards: `../../DATA/README.md`
- Test procedures: `../../PROCEDURES/`
- Analysis methods: `../../CORRELATION/`

---

**Owner**: Test Engineering / Data Analysis Team  
**Language**: Python preferred, MATLAB/LabVIEW as needed  
**Review**: Peer review required for critical scripts  
**Testing**: All scripts tested before operational use
