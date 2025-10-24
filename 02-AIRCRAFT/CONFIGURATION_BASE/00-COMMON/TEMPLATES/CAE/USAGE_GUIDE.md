# CAE Template Usage Guide

## Quick Start

This guide helps you use the CAE template structure for your subsystem.

## Copy the Template

To use this template for a subsystem CAE directory:

```bash
# From your subsystem's PLM/CAx directory
cp -r /path/to/TEMPLATES/CAE ./CAE
cd CAE
```

## Initial Setup

### 1. Update META.json

Edit `META.json` with your team information:

```json
{
  "owner": "Your Name",
  "cae_owner": "CAE Lead Name",
  "approver": "Approver Name",
  "contact_email": "your-team@example.com",
  "last_updated": "2025-10-23"
}
```

### 2. Review Directory Structure

The template includes:
- `CFD/` - Computational Fluid Dynamics cases
- `FEA/` - Finite Element Analysis cases
- `COUPLING/` - Multi-physics coupling
- `DATA/` - Experimental and baseline data
- `QA/` - Quality assurance and testing
- `VALIDATION/` - Validation reports
- `DOCS/` - Detailed documentation
- `SCRIPTS/` - Automation scripts

### 3. Remove Unused Sections (Optional)

If you don't need certain analysis types:

```bash
# Example: Remove FEA if only doing CFD
rm -rf FEA/

# Example: Remove COUPLING if no multi-physics
rm -rf COUPLING/
```

## Creating a New Case

### CFD Case

1. **Create case directory**:
```bash
cd CFD/cases
mkdir my_new_case
cd my_new_case
mkdir case smoke baseline
```

2. **Copy metadata template**:
```bash
cp ../../../TEMPLATE_METADATA.yaml case/metadata.yaml
```

3. **Edit metadata**:
```yaml
case_id: CFD-MYNEW-001
description: "Description of my analysis"
revision: R001
solver: OpenFOAM
solver_version: v10
# ... fill in remaining fields
```

4. **Set up simulation**:
- Add your solver input files to `case/`
- Create a coarse version in `smoke/` for CI

5. **Run and create baseline**:
```bash
cd case
# Run your simulation
./Allrun

# Extract metrics
python3 ../../../SCRIPTS/cfd_postprocess.py --case .

# Copy to baseline
cp metrics.json ../baseline/
```

### FEA Case

Similar process as CFD:

1. **Create case directory**:
```bash
cd FEA/cases
mkdir my_stress_analysis
cd my_stress_analysis
mkdir model mesh smoke baseline
```

2. **Follow similar steps** as CFD case above

## Running Scripts

### Check Metadata

Validate all metadata files:

```bash
cd CAE
python3 SCRIPTS/check_metadata.py --dir .
```

### Run a Case

CFD example:
```bash
python3 SCRIPTS/cfd_runner.py --case CFD/cases/my_case/case --timeout 3600
```

FEA example:
```bash
python3 SCRIPTS/fea_runner.py --case FEA/cases/my_case/model --timeout 3600
```

### Post-process Results

```bash
python3 SCRIPTS/cfd_postprocess.py --case CFD/cases/my_case/case
python3 SCRIPTS/export_metrics.py --case CFD/cases/my_case/case
```

### CI Smoke Tests

Run fast smoke tests for continuous integration:

```bash
cd CAE
./SCRIPTS/ci_smoke.sh
```

This script:
1. Checks all metadata
2. Runs CFD smoke cases
3. Runs FEA smoke cases
4. Exports metrics

## Quality Assurance

### Regression Testing

Compare new results against baseline:

```bash
python3 QA/regression_tests/compare_metrics.py \
  --baseline CFD/cases/my_case/baseline/metrics.json \
  --current CFD/cases/my_case/case/metrics.json
```

### Acceptance Criteria

Review `QA/acceptance_criteria.md` to ensure your cases meet:
- Mesh quality requirements
- Convergence criteria
- Results quality checks

### Test Plan

Follow `QA/test_plan.md` for:
- Smoke test setup
- Regression test procedures
- Validation activities

## Validation

### Plan Validation Activities

1. Review `VALIDATION/validation_plan.md`
2. Identify required validation cases
3. Acquire experimental data
4. Set up validation simulations
5. Document results in `VALIDATION/correlation_reports/`

### Validation Report Template

Use the template structure:
```
VALIDATION/correlation_reports/YYYY-MM-DD_case_name.md
```

Include:
- Experimental setup
- Simulation setup
- Comparison results
- Correlation metrics (R², RMSE, etc.)
- Uncertainty analysis

## Documentation

### Solver-Specific Guidance

Refer to detailed documentation:
- `DOCS/CFD_README.md` - CFD best practices
- `DOCS/FEA_README.md` - FEA best practices
- `DOCS/COUPLING_README.md` - Multi-physics coupling

### Case Documentation

Each case should have a README describing:
- Purpose and objectives
- Geometry and mesh
- Material properties
- Boundary conditions
- Solution settings
- Expected results

## Git LFS Setup

For large files (meshes, results databases):

1. **Install Git LFS**:
```bash
git lfs install
```

2. **Track large files** in `.gitattributes`:
```
*.odb filter=lfs diff=lfs merge=lfs -text
*.rst filter=lfs diff=lfs merge=lfs -text
*.op2 filter=lfs diff=lfs merge=lfs -text
*.msh filter=lfs diff=lfs merge=lfs -text
*.unv filter=lfs diff=lfs merge=lfs -text
*.tar.gz filter=lfs diff=lfs merge=lfs -text
```

3. **Add and commit**:
```bash
git add .gitattributes
git add large_file.msh
git commit -m "Add large mesh file with LFS"
```

## CI/CD Integration

### GitHub Actions Example

Create `.github/workflows/cae-tests.yml`:

```yaml
name: CAE Tests

on: [push, pull_request]

jobs:
  smoke-tests:
    runs-on: ubuntu-latest
    timeout-minutes: 10
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Setup Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.9'
    
    - name: Install dependencies
      run: |
        pip install numpy pandas pyyaml
    
    - name: Check metadata
      run: |
        python3 CAE/SCRIPTS/check_metadata.py --dir CAE/
    
    - name: Run smoke tests
      run: |
        cd CAE
        ./SCRIPTS/ci_smoke.sh
```

## Troubleshooting

### Script Fails to Run

Check:
- Python version (require 3.9+)
- Required packages installed
- File permissions (scripts executable?)

### Metadata Validation Fails

- Ensure all required fields filled
- Remove placeholder values like "string", "int"
- Check YAML syntax

### Smoke Test Timeout

- Reduce mesh size in smoke cases
- Simplify physics models
- Increase timeout in script

### Metrics Comparison Fails

- Check units consistency
- Verify baseline is current
- Review tolerance settings
- Check for numerical differences

## Best Practices Summary

1. **Document everything**: README, metadata, comments
2. **Version control**: Track all inputs, not just code
3. **Test early**: Run smoke tests frequently
4. **Validate**: Compare against experiments when possible
5. **Automate**: Use scripts for repeatability
6. **Review**: Peer review before finalizing
7. **Archive**: Keep baseline results safe

## Getting Help

- Review detailed documentation in `DOCS/`
- Check example cases in `CFD/cases/tank_solidification/` and `FEA/cases/static_stress/`
- Contact CAE team (see META.json for contact info)

## Maintenance

### Updating Baselines

When intentionally changing results:

1. Document reason for change
2. Run full test suite
3. Update baseline metrics
4. Update CHANGELOG
5. Get approval from CAE lead

### Adding New Cases

1. Follow case creation process above
2. Add to regression test suite
3. Document in README
4. Submit for peer review

### Template Updates

Check for template updates:
```bash
# Compare your version with latest template
diff -r CAE/ /path/to/TEMPLATES/CAE/
```

Merge updates carefully to preserve your customizations.

---

**Version:** 1.0  
**Last Updated:** 2025-10-23  
**Questions?** Contact CAE team
