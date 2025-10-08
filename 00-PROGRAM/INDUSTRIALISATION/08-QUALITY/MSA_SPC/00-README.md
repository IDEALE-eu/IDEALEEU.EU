# MSA_SPC

Measurement System Analysis and Statistical Process Control.

## Measurement System Analysis (MSA)

### Overview
MSA evaluates the measurement process to ensure data quality before using for process control or capability studies.

### Gage R&R (Repeatability & Reproducibility)
- **Repeatability:** Variation when same operator measures same part multiple times
- **Reproducibility:** Variation between different operators
- **Method:** 3 operators × 3 trials × 10 parts (typical)
- **Acceptance:** %GRR <10% excellent, <30% acceptable

### MSA Metrics
- **%GRR:** Gage variation as % of tolerance or total variation
- **ndc (Number of Distinct Categories):** ≥5 acceptable
- **P/T Ratio:** Precision-to-tolerance ratio <30%

### MSA Frequency
- New measurement equipment
- After gage repair or calibration
- Periodic (annual) for critical gages
- When measurement results questioned

## Statistical Process Control (SPC)

### Overview
SPC uses control charts to monitor process stability and capability, enabling early detection of problems.

### Control Chart Types
- **Variables Data:** X-bar & R, X & MR, X-bar & S
- **Attributes Data:** p-chart (proportion), c-chart (count)

### Control Limits
- **UCL/LCL:** ±3 sigma from centerline
- **Calculated from data:** Not the same as specification limits
- **Purpose:** Detect special cause variation

### Out-of-Control Rules
1. Point beyond control limits
2. 8 consecutive points one side of centerline (run)
3. 6 consecutive increasing/decreasing (trend)
4. 14 points alternating up/down (cycling)
5. 2 of 3 points beyond 2-sigma
6. 4 of 5 points beyond 1-sigma

### Process Capability

**Indices:**
- **Cp:** Process potential (spread)
  - Cp = (USL - LSL) / 6σ
- **Cpk:** Process capability (considers centering)
  - Cpk = min[(USL - μ)/3σ, (μ - LSL)/3σ]
- **Ppk:** Process performance (long-term)

**Acceptance Criteria:**
- Cpk ≥ 1.67: Highly capable
- Cpk ≥ 1.33: Capable (minimum for aerospace)
- Cpk < 1.33: Requires improvement or 100% inspection

### SPC Implementation
1. **Select characteristics:** Critical dimensions/parameters
2. **Collect baseline data:** 20-30 subgroups
3. **Calculate control limits:** From baseline
4. **Monitor ongoing:** Plot new data on charts
5. **React to signals:** Investigate and correct
6. **Improve:** Reduce variation over time

## Software Tools
- Minitab, JMP, or equivalent statistical software
- SPC modules in MES or QMS systems
- Real-time SPC at work centers

## Training
- Operators: How to plot and recognize signals
- Quality engineers: Chart setup and analysis
- Management: Interpretation and decision-making

## Links
- To **CONTROL_PLAN/** for SPC requirements
- To **05-TOOLING_JIGS_FIXTURES/GAUGE_CALIBRATION/** for gage management
- To **16-IT_INTEGRATION/QMS/** for SPC software
