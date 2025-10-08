# RADIATION

Radiation effects and hardness assurance standards.

## Overview

This directory contains ECSS standards for radiation environment definition, effects analysis, and hardness assurance for spacecraft electronics and materials.

## Applicable Standards

### ECSS-Q-ST-60C - Electrical, Electronic and Electromechanical (EEE) Components
- **Radiation Coverage**: Component radiation tolerance and testing
- **Key Topics**:
  - Radiation environment specification
  - Total ionizing dose (TID) requirements
  - Single event effects (SEE) requirements
  - Displacement damage requirements
  - Radiation test methods

### ECSS-Q-ST-30C - Dependability (Radiation Section)
- **Scope**: Radiation effects on reliability
- **Key Topics**:
  - Radiation-induced failure modes
  - Radiation reliability prediction
  - Radiation testing for reliability

### Mission-Specific Standards
- **ECSS-E-ST-10-04C**: Space environment definition (radiation environments)
- **NASA standards**: NASA-HDBK-4002A (Mitigating In-Space Charging Effects)

## Space Radiation Environment

### Radiation Sources
- **Trapped Radiation**: Van Allen belts (protons, electrons)
- **Solar Particles**: Solar proton events (SPE), solar flares
- **Galactic Cosmic Rays (GCR)**: Heavy ions from outside solar system
- **Secondary Radiation**: Bremsstrahlung, neutrons from nuclear interactions

### Orbital Dependence
- **Low Earth Orbit (LEO)**: South Atlantic Anomaly (SAA), trapped protons/electrons
- **Medium Earth Orbit (MEO)**: High trapped radiation (e.g., GPS orbit)
- **Geostationary Orbit (GEO)**: Lower trapped radiation, solar particle events
- **Deep Space**: GCR dominant, solar particle events
- **Lunar/Planetary**: Surface radiation (no magnetic shielding)

## Radiation Effects

### Total Ionizing Dose (TID)
- **Mechanism**: Ionization creates electron-hole pairs in oxides
- **Effects**: Threshold voltage shifts, increased leakage current, parameter drift
- **Units**: rad(Si) or Gy(Si), 1 Gy = 100 rad
- **Typical Mission Doses**:
  - LEO: 1-100 krad over mission
  - GEO: 10-300 krad over mission
  - Interplanetary: Variable, up to several Mrad

### Displacement Damage (DD)
- **Mechanism**: Nuclear reactions displace atoms in crystal lattice
- **Effects**: Degradation of minority carrier lifetime, increased leakage
- **Components Affected**: Solar cells, photodetectors, LEDs, bipolar transistors
- **Metric**: Non-Ionizing Energy Loss (NIEL), fluence (particles/cm²)

### Single Event Effects (SEE)
- **Mechanism**: Single heavy ion or proton creates ionization track
- **Effect Types**:
  - **SEU** (Single Event Upset): Bit flip in memory or register
  - **SET** (Single Event Transient): Voltage spike in analog circuit
  - **SEL** (Single Event Latchup): Parasitic thyristor turns on, high current
  - **SEB** (Single Event Burnout): Permanent damage to power device
  - **SEGR** (Single Event Gate Rupture): Oxide breakdown
- **Units**: Events per bit-day, cross-section (cm²/device)

## Radiation Hardness Assurance

### Hardness Assurance Process
1. **Define Radiation Environment**: Mission orbit and duration
2. **Specify Radiation Requirements**: TID, DD, SEE limits per component
3. **Select Radiation-Tolerant Parts**: Radiation-hardened or radiation-tolerant
4. **Radiation Testing**: TID, DD, SEE testing of components
5. **Radiation Analysis**: Predict on-orbit performance
6. **Mitigation Design**: Shielding, redundancy, error correction
7. **Verification**: Demonstrate compliance with requirements

### Component Selection
- **Radiation-Hardened (rad-hard)**: Specially designed for radiation tolerance (military, space heritage)
- **Radiation-Tolerant (rad-tolerant)**: Commercial parts with demonstrated tolerance
- **Commercial Off-The-Shelf (COTS)**: Requires extensive testing

### Radiation Testing

#### TID Testing
- Expose component to gamma rays (Co-60) or X-rays
- Irradiate to mission dose + margin
- Measure parameters at dose intervals
- Typical dose rates: 50-300 rad(Si)/min (high) or 10 mrad(Si)/s (low)

#### SEE Testing
- Expose to heavy ion beam (accelerator) or proton beam
- Measure SEU cross-section vs. LET (Linear Energy Transfer)
- Determine SEL, SEB, SEGR thresholds
- Extrapolate to on-orbit rates

#### DD Testing
- Irradiate with protons or neutrons
- Measure degradation (e.g., solar cell output, detector noise)
- Determine damage coefficients

### Radiation Analysis

#### TID Analysis
- Calculate dose behind shielding (aluminum, PCB, encapsulation)
- Account for dose-rate effects (low dose-rate enhancement)
- Compare to component TID limits
- Verify positive margins

#### SEE Rate Prediction
- Heavy ion: Convolve SEU cross-section with GCR spectrum
- Protons: Direct ionization + indirect (nuclear reactions)
- Calculate event rates (upsets/device/day)
- Assess impact on mission (acceptable rate?)

#### DD Analysis
- Calculate particle fluence (protons, electrons)
- Apply damage coefficients
- Predict EOL performance (e.g., solar cell power, detector signal-to-noise)

## Mitigation Techniques

### Design Mitigation
- **Shielding**: Aluminum or tantalum around sensitive electronics (diminishing returns)
- **Redundancy**: Dual or triple modular redundancy (TMR)
- **Error Detection and Correction (EDAC)**: ECC memory, CRC on data
- **Watchdog Timers**: Reset on SEL or SEU-induced hang
- **Immune Technologies**: SOI (Silicon-On-Insulator), SiGe

### Operational Mitigation
- **SEL Detection and Recovery**: Current monitoring, power cycling
- **Memory Scrubbing**: Periodically read and correct memory
- **Safe Mode**: Reduce operations during SPE
- **Upset Filtering**: Ignore transient data errors

## Key Deliverables

1. **Radiation Environment Specification** - Mission orbit, duration, environment
2. **Radiation Requirements Document** - TID, DD, SEE limits
3. **Radiation Test Plan** - Test strategy, facilities, procedures
4. **Radiation Test Reports** - TID, DD, SEE test results per component
5. **Radiation Analysis Report** - TID, DD, SEE analysis and margins
6. **Radiation Mitigation Design** - Shielding, EDAC, redundancy
7. **Radiation Hardness Assurance Plan** - Overall RHA approach
8. **Lessons Learned** - Anomalies and improvements

## Compliance Requirements

- Radiation environment defined per mission profile
- Components selected with adequate radiation tolerance
- Radiation testing demonstrates margins
- Radiation analysis predicts on-orbit performance
- Mitigation techniques implemented as needed

## Integration with Other Standards

- **ECSS-E-ST-10C** - Systems engineering defines mission and environment
- **ECSS-Q-ST-60C** - EEE component selection includes radiation tolerance
- **ECSS-E-ST-20C** - Electrical design incorporates EDAC and redundancy

## Radiation Test Facilities

- **Heavy Ion Accelerators**: TAMU (Texas A&M), Brookhaven, GANIL, GSI, HIMAC
- **Proton Facilities**: PSI (Switzerland), iThemba (South Africa), UC Davis
- **TID Facilities**: Co-60 gamma sources, X-ray machines (many labs worldwide)

## Tools and Templates

- Radiation environment models: AP-8/AE-8, CREME96, SPENVIS, OMERE
- SEE rate calculators: CREME96, OMERE
- Radiation analysis templates

## References

- 01-REGISTER/STANDARDS_REGISTER.csv - STD-018 (ECSS-Q-ST-60C)
- ECSS Portal: https://ecss.nl
- NASA-HDBK-4002A - Mitigating In-Space Charging Effects
- SPENVIS: https://www.spenvis.oma.be (space environment tools)

---

**Status**: Configuration-controlled per 00-PROGRAM/CONFIG_MGMT/
