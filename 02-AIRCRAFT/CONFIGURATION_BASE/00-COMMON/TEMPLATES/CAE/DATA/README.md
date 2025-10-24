# DATA — Experimental and Baseline Data

## Purpose

This directory contains:
- Experimental validation data
- Regression test baselines
- Historical simulation results
- Archived data for comparison

## Directory Structure

```
DATA/
├─ README.md                    # This file
├─ experimental/                # Measured validation data
│  ├─ wind_tunnel/              # Wind tunnel test data
│  ├─ bench_tests/              # Bench test measurements
│  └─ flight_tests/             # Flight test data
├─ regression_baselines/        # Large baseline outputs (use LFS)
│  ├─ cfd/                      # CFD regression baselines
│  └─ fea/                      # FEA regression baselines
└─ results_archive/             # Historical results for reference
   └─ by_date/                  # Organized by date
```

## Experimental Data

### Format Requirements
- **CSV**: Tabular time-series or spatial data
- **HDF5**: Large multi-dimensional datasets
- **JSON**: Metadata and test conditions

### Documentation
Each experimental dataset must include:
- Test conditions (temperature, pressure, etc.)
- Instrumentation details
- Uncertainty estimates
- Calibration information

### Example Structure
```
experimental/wind_tunnel/test_2024_10_15/
├─ README.md                    # Test description
├─ conditions.json              # Test conditions
├─ pressure_taps.csv            # Measured pressures
├─ force_balance.csv            # Force/moment data
└─ uncertainty.json             # Uncertainty analysis
```

## Regression Baselines

Regression baselines are reference solutions used for continuous validation.

### Storage
- Use Git LFS for large binary files (> 10 MB)
- Store compressed archives (.tar.gz) for field data
- Keep metadata separate in JSON files

### Naming Convention
```
{CASE_ID}_{SOLVER}_{VERSION}_{DATE}_{HASH}.{ext}

Example: CFD-TANK-001_OpenFOAM_v10_20251023_a3f5b2.tar.gz
```

### Baseline Contents
- Full field data (optional, for detailed comparison)
- Extracted metrics (required, in metrics.json)
- Convergence history
- Solver log files

## Results Archive

Historical results for long-term reference.

### Organization
```
results_archive/
└─ by_date/
   └─ 2025/
      └─ 2025-10/
         └─ CFD-TANK-001_R001/
            ├─ metadata.json
            ├─ metrics.json
            └─ results.tar.gz
```

### Retention Policy
- Keep all results for active projects
- Archive older results (> 2 years) to cold storage
- Maintain metadata even if full results are archived

## Data Quality

### Validation Checklist
- [ ] Data format consistent with standards
- [ ] Metadata complete and accurate
- [ ] Units clearly specified
- [ ] Uncertainty documented
- [ ] Calibration current (< 1 year old)
- [ ] Traceability to source

## Using Experimental Data

### Comparison Scripts
```python
import pandas as pd
import matplotlib.pyplot as plt

# Load experimental data
exp_data = pd.read_csv('experimental/wind_tunnel/test_001/pressure.csv')

# Load simulation results
sim_data = pd.read_csv('CFD/cases/wing/results/pressure.csv')

# Compare
plt.plot(exp_data['x'], exp_data['Cp'], 'o', label='Experiment')
plt.plot(sim_data['x'], sim_data['Cp'], '-', label='Simulation')
plt.legend()
plt.savefig('comparison.png')
```

### Correlation Metrics
- R² coefficient
- Root mean square error (RMSE)
- Mean absolute percentage error (MAPE)

## Git LFS Configuration

Add to `.gitattributes`:
```
*.odb filter=lfs diff=lfs merge=lfs -text
*.rst filter=lfs diff=lfs merge=lfs -text
*.op2 filter=lfs diff=lfs merge=lfs -text
*.tar.gz filter=lfs diff=lfs merge=lfs -text
*.h5 filter=lfs diff=lfs merge=lfs -text
*.hdf5 filter=lfs diff=lfs merge=lfs -text
```

## Best Practices

1. **Immutability**: Never modify experimental data
2. **Documentation**: Document data provenance
3. **Versioning**: Use Git LFS for version control
4. **Access**: Restrict access to sensitive data
5. **Backup**: Maintain off-site backups

## References

- Data Management Plan: See 00-PROGRAM/CONFIG_MGMT/
- UTCS Traceability: Link data to UTCS URIs
- Git LFS Documentation: https://git-lfs.github.com/

---

**Last Updated:** 2025-10-23
