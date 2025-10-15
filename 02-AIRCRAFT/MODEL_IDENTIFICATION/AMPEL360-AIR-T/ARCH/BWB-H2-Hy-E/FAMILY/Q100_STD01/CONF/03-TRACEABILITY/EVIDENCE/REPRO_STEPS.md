<!-- UTCS: utcs://AMPEL360-AIR-T/BWB-H2-Hy-E/Q100_STD01 -->

# Reproducibility Steps for Evidence Artifacts

## Purpose

This document provides the steps necessary to reproduce all evidence artifacts in this directory, ensuring scientific reproducibility and regulatory acceptance.

---

## Environment Setup

### Software Versions
```
Python: 3.11.5
NumPy: 1.24.3
SciPy: 1.11.1
Pandas: 2.0.3
OpenFOAM: v2306
ANSYS Mechanical: 2023 R2
MATLAB: R2023a
```

### Hardware Requirements
- CPU: 32+ cores recommended
- RAM: 64 GB minimum
- Storage: 500 GB for intermediate files
- GPU: NVIDIA A100 (for ML/federated learning runs)

---

## Artifact Reproduction

### 1. H₂ Leak Test Report (REQ-AMPEL-001)
**File**: `H2_LEAK_TEST_REPORT_v2.3.pdf`

**Steps**:
1. Physical test conducted at TRL-6 facility (IDEALE-EU Lab, Munich)
2. Test setup: LH₂ tank prototype with instrumentation
3. Measurement equipment: Pfeiffer Vacuum HLT 560 leak detector
4. Test conditions: 20K, 5 bar internal pressure
5. Duration: 72 hours continuous monitoring
6. Data logged at 1 Hz sampling rate
7. Report generated using LaTeX template: `templates/test_report.tex`

**Reproduction**: Requires physical test facility access; contact `cqh-steward@idealeeu.eu`

---

### 2. Boil-off Analysis (REQ-AMPEL-002)
**File**: `BOILOFF_ANALYSIS_v2.3.xlsx`

**Steps**:
```bash
cd /home/runner/work/IDEALEEU.EU/IDEALEEU.EU/tools/thermal_analysis
python boiloff_calculator.py \
  --tank-config ../CONF/propulsion/tank_geometry.yaml \
  --ambient-temp 288.15 \
  --duration 86400 \
  --insulation MLI \
  --output BOILOFF_ANALYSIS_v2.3.xlsx
```

**Seeds/Parameters**:
- Random seed: 42
- Monte Carlo iterations: 10,000
- Ambient temperature: 288.15 K (15°C)
- Initial H₂ mass: 6,800 kg

---

### 3. Fuel System Validation (REQ-AMPEL-003)
**File**: `FUEL_SYSTEM_VALIDATION_v2.3.pdf`

**Steps**:
1. Design review conducted 2025-09-20
2. Reviewers: 5 domain experts (AAA, CQH, PPP)
3. Checklist: ATA-28 compliance matrix
4. Tool: PlantUML for P&ID diagrams
5. Report generation: Markdown → Pandoc → PDF

```bash
pandoc fuel_system_review_notes.md \
  -o FUEL_SYSTEM_VALIDATION_v2.3.pdf \
  --template=ideale_report.latex \
  --metadata-file=metadata.yaml
```

---

### 4. Power Distribution Test (REQ-AMPEL-004)
**File**: `POWER_DISTRIBUTION_TEST_v2.3.csv`

**Steps**:
```bash
cd /home/runner/work/IDEALEEU.EU/IDEALEEU.EU/tools/electrical_sim
python power_loss_calculator.py \
  --topology ../CONF/propulsion/power_distribution.yaml \
  --load-profile mission_cycle_v2.3.csv \
  --output POWER_DISTRIBUTION_TEST_v2.3.csv
```

**Parameters**:
- Cable resistivity: 1.68×10⁻⁸ Ω·m (copper, 20°C)
- Voltage: 800 VDC
- Load profiles: 10 flight cycles

---

### 5. Propulsion Integration (REQ-AMPEL-005)
**File**: `PROPULSION_INTEGRATION_v2.3.pdf`

**Steps**:
1. Structural loads analysis using ANSYS Mechanical
2. Input: `propulsion_mount_loads.csv`
3. FE model: `BWB_propulsion_mounts.wbpj`
4. Material properties: Ti-6Al-4V (Titanium alloy)
5. Mesh: 0.5 mm elements at critical regions
6. Solver: Static structural + harmonic response
7. Post-processing: Python script `extract_stress_margins.py`

---

### 6. Emissions Calculation (REQ-AMPEL-006)
**File**: `EMISSIONS_CALC_v2.3.xlsx`

**Steps**:
```bash
python tools/emissions_calculator.py \
  --mission performance/mission_profile.yaml \
  --fuel-type LH2 \
  --baseline-aircraft A320neo \
  --output EMISSIONS_CALC_v2.3.xlsx
```

**Assumptions**:
- H₂ combustion: H₂ + 0.5O₂ → H₂O (no CO₂)
- Electricity: 30% renewable grid mix
- LCA boundaries: tank-to-wake

---

### 7. Battery Safety Test (REQ-AMPEL-007)
**File**: `BATTERY_SAFETY_TEST_v2.3.pdf`

**Steps**:
1. Thermal runaway test per UN 38.3
2. Test facility: IDEALE-EU Battery Lab (Stuttgart)
3. Cell type: Li-S prototype (400 Ah)
4. Abuse conditions: overcharge to 150% SOC, nail penetration
5. Monitoring: thermal cameras, pressure sensors, gas detectors
6. Duration: 12 hours post-trigger

**Reproduction**: Requires certified test facility

---

### 8. Mission Profile Simulation (REQ-AMPEL-008)
**File**: `MISSION_PROFILE_SIM_v2.3.dat`

**Steps**:
```bash
cd /home/runner/work/IDEALEEU.EU/IDEALEEU.EU/tools/mission_sim
matlab -batch "run_mission_sim('mission_profile.yaml', 'v2.3')"
```

**Inputs**:
- Route: Frankfurt → New York (6,200 km)
- Reserves: 45 min + 200 km alternate
- Weather: ISA conditions
- Random seed: 12345

---

### 9. Cryogenic Insulation Test (REQ-AMPEL-009)
**File**: `CRYOGENIC_INSULATION_TEST_v2.3.pdf`

**Steps**:
1. Physical test of MLI panel samples
2. Test chamber: Vacuum < 10⁻⁶ mbar
3. Temperature gradient: 20K (inner) to 288K (outer)
4. Measurement: heat flux sensors
5. Duration: 168 hours (1 week)
6. Data acquisition: LabVIEW DAQ system

---

### 10. Structural Analysis (REQ-AMPEL-010)
**File**: `STRUCTURAL_ANALYSIS_FEM_v2.3.res`

**Steps**:
```bash
# OpenFOAM structural solver
cd /home/runner/work/IDEALEEU.EU/IDEALEEU.EU/simulations/structural
./run_fem_analysis.sh --config BWB_wing_loads.yaml --mesh fine
```

**Parameters**:
- Load case: 2.5g pullup maneuver
- Material: CFRP (Carbon Fiber Reinforced Polymer)
- Elements: 2.4M tetrahedral elements
- Solver: conjugateGradient

---

## Verification

To verify checksums:
```bash
cd 03-TRACEABILITY/EVIDENCE
sha256sum -c checksums.sha256
```

All checksums must match for evidence acceptance.

---

**Maintained By**: Verification & Validation Team  
**Last Updated**: 2025-10-15  
**Review Frequency**: Every baseline release
