# Radiation Data

## Overview

Radiation test data and qualification for space-grade EEE components.

## Radiation Environment

### Sources of Radiation in Space
- **Galactic Cosmic Rays (GCR):** High-energy particles (protons, heavy ions)
- **Solar Particle Events (SPE):** Solar flares producing energetic protons
- **Trapped Radiation Belts:** Van Allen belts (electrons and protons)
- **Secondary Radiation:** Neutrons and other particles from interactions

### Mission Orbits
- **Low Earth Orbit (LEO):** Moderate radiation, South Atlantic Anomaly (SAA)
- **Medium Earth Orbit (MEO):** GPS orbit, higher radiation exposure
- **Geostationary Orbit (GEO):** High radiation, trapped electrons
- **Interplanetary:** Deep space, GCR dominant, no trapped radiation

## Radiation Effects

### Total Ionizing Dose (TID)
**Mechanism:**
- Accumulation of charge in oxides (gate oxide, field oxide)
- Threshold voltage shifts in MOSFETs
- Increased leakage currents
- Parametric degradation over time

**Units:** rad or Gray (1 Gray = 100 rad)

**Typical Mission Doses:**
- LEO (5 years): 10-30 krad
- GEO (15 years): 100-300 krad
- Interplanetary (10 years): 50-100 krad (depends on shielding)

**Testing:**
- Co-60 gamma rays or X-rays
- Per MIL-STD-883 Method 1019 or ESCC 22900
- Dose rate: 50-300 rad/min (low dose rate more representative)
- Bias conditions during irradiation
- Electrical parameter monitoring

### Single Event Effects (SEE)
**Types:**
- **SEU (Single Event Upset):** Bit flip in memory or register
- **SEL (Single Event Latchup):** High current state, potentially destructive
- **SEFI (Single Event Functional Interrupt):** Temporary loss of function
- **SEB (Single Event Burnout):** Destructive failure of power device
- **SEGR (Single Event Gate Rupture):** Gate oxide rupture

**Mechanism:**
- Heavy ion or high-energy proton strikes sensitive node
- Charge collection causes transient or state change

**Characterization:**
- **LET (Linear Energy Transfer):** MeV·cm²/mg
- **Cross-section:** cm²/device (probability of SEE)
- **Threshold LET:** Minimum LET to cause effect

**Testing:**
- Heavy ion accelerator facility
- Ion species: Fe, Kr, Xe, etc.
- LET range: 1-100+ MeV·cm²/mg
- Fluence: ions/cm²
- Electrical monitoring during exposure
- Per ESCC 25100 or similar

### Displacement Damage
**Mechanism:**
- Displacement of atoms in crystal lattice
- Affects optoelectronics (LEDs, photodetectors, solar cells)
- Degrades gain in bipolar transistors

**Units:** Non-Ionizing Energy Loss (NIEL)

**Testing:**
- Proton or neutron irradiation
- Energy spectrum representative of environment
- Performance degradation measurement

## Radiation Testing

### Test Standards
- **MIL-STD-883 Method 1019:** TID testing
- **ESCC 22900:** TID for space
- **ESCC 25100:** SEE testing
- **NASA EEE-INST-002:** Part selection and testing guidelines

### Test Facilities
- NASA facilities
- European facilities (CERN, PSI, etc.)
- University accelerators
- Commercial radiation test services

### Test Costs
- TID testing: $5k-$20k per part type
- SEE testing: $20k-$100k per part type (accelerator time expensive)
- Can share costs across programs or with other companies

## Radiation Data Management

### Data Sources
- **Manufacturer data:** Some manufacturers provide radiation data
- **NASA Radiation Effects Database:** Public data for many parts
- **ESA Radiation Database:** European data
- **JPL REAG:** Jet Propulsion Laboratory Radiation Effects and Analysis Group
- **Company internal database:** Accumulate data from own testing

### Data Requirements
- Part manufacturer and part number
- Test conditions (dose rate, bias, LET, energy)
- Failure modes and mechanisms
- Statistical data (multiple samples)
- Lot-to-lot variability
- Derating guidelines based on data

### Data Sharing
- Industry collaboration on testing
- Conference presentations (RADECS, NSREC, SEE)
- Technical papers
- Data sharing agreements

## Part Selection for Radiation

### Radiation-Hardened Parts
- Designed and manufactured for radiation environment
- Expensive and limited selection
- Long lead times
- Used for critical functions

### Radiation-Tolerant Commercial Parts
- Commercial parts with acceptable radiation performance
- Much broader selection
- Lower cost
- Testing required for qualification

### Selection Process
1. Define mission radiation environment
2. Identify critical functions and acceptable failure rates
3. Search radiation databases for candidate parts
4. Review radiation test data
5. Test additional parts if data unavailable
6. Select part with margin for uncertainties
7. Implement mitigation (shielding, redundancy, error correction)

## Mitigation Strategies

### Shielding
- Aluminum or tantalum shielding around sensitive devices
- PCB layer stackup for shielding
- Enclosure shielding
- Diminishing returns (weight, secondary radiation)

### Redundancy
- Triple Modular Redundancy (TMR) for logic
- Spare channels for critical functions
- Voting circuits

### Error Detection and Correction
- EDAC (Error Detection and Correction) for memory
- Parity checking
- CRC (Cyclic Redundancy Check) for data
- Watchdog timers for SEFIs

### Design Techniques
- Avoid sensitive devices in critical paths
- Latch-up protection circuits (current limiting)
- Periodic scrubbing of memory (rewrite correct data)
- Soft reset capabilities

### Derating
- Operate parts at lower stress (voltage, current, temperature)
- Reduces SEE cross-section
- Improves TID tolerance

## Documentation

### Radiation Test Report
- Part identification
- Test facility and date
- Test conditions and procedures
- Test results (TID, SEE)
- Failure modes observed
- Statistical analysis
- Recommendations for use

### Radiation Analysis Report
- Mission radiation environment
- Part radiation tolerance
- Margin analysis
- Mitigation strategies
- Risk assessment
- Compliance with requirements
