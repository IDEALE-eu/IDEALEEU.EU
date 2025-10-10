# CAx — Engineering Artifacts

## Engineering Files Layout

- **CAD**: Mechanical design models and drawings
- **CAE**: Engineering analysis (FEA, CFD, etc.)
- **CAO**: Optimization studies
- **CAM**: Manufacturing data (NC paths, tooling)
- **CAI**: Installation drawings and procedures
- **CAV**: Validation models and test results
- **CAS**: Simulation models and scripts
- **CMP**: Composite materials data

## Rules
- Use neutral formats (STEP / JT / glTF) alongside native where possible
- Commit large binaries via LFS
- Include SBOM / BOM exports in EBOM_LINKS.md
- Provide README per model with inputs/outputs/solver/tool version
