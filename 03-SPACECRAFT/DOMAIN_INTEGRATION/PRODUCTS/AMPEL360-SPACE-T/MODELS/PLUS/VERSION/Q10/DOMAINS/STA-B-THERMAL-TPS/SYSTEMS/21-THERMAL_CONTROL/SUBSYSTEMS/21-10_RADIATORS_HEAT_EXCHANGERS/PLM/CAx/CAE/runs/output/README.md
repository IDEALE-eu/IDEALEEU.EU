# OUTPUT — Raw Analysis Results

## Purpose
Raw solver output files, result databases, and analysis logs. Results are archived by content hash for long-term storage.

## Contents
- Solver output files
- Results databases (binary formats)
- Log files and convergence histories
- Checkpoint and restart files
- Error logs and warnings
- Time-step or iteration data

## File Organization
- Hash-based archival system
- One directory per analysis run
- Include all solver-generated outputs
- Store convergence diagnostics

## Naming Convention
```
21-10-CAE_output_<case>_<YYYYMMDD>__r<NN>__<STATUS>/
  └─ <content_hash>/ (e.g., sha256 hash)
```

Example: `21-10-CAE_output_thermal_balance_20251010__r01__REL/abc123.../`

## Output File Types
- **Thermal**: Temperature distributions, heat flows
- **Structural**: Displacement, stress, strain
- **CFD**: Velocity, pressure, temperature fields
- **Logs**: Convergence history, iteration counts
- **Diagnostics**: Error messages, warnings

## Result Database Formats
- **Nastran**: .op2, .f06
- **ANSYS**: .rst, .rth
- **Abaqus**: .odb
- **Fluent**: .cas.h5, .dat.h5
- **Generic**: HDF5, NetCDF

## Hash-Based Archival
Results are stored by content hash to:
- Prevent duplication
- Enable efficient storage
- Maintain data integrity
- Support version control

## Guidelines
- Archive complete output files
- Maintain link to input files
- Document solver version
- Preserve convergence diagnostics
- Do not post-process results in this directory

---

**Last Updated**: 2025-10-10
