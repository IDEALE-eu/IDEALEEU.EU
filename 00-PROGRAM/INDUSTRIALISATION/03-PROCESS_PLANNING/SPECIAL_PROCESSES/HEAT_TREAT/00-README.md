# HEAT_TREAT

Heat treatment specifications and procedures for aerospace metals.

## Overview

Heat treatment process specifications per AMS standards for aluminum, steel, titanium, and other aerospace alloys.

## Heat Treatment Types

### Solution Heat Treatment
- **Purpose:** Dissolve alloying elements into solid solution
- **Materials:** Aluminum 2xxx, 6xxx, 7xxx series
- **Process:** Heat to solution temperature, rapid quench

### Aging (Precipitation Hardening)
- **Natural Aging (T4):** Room temperature aging after solution treatment
- **Artificial Aging (T6):** Elevated temperature aging for maximum strength
- **Overaging (T7):** Slight overaging for stress corrosion resistance

### Annealing
- **Full Anneal:** Maximum softness and ductility
- **Stress Relief Anneal:** Relieve residual stresses without full softening
- **Materials:** All metals as needed

### Hardening and Tempering (Steel)
- **Austenitizing:** Heat above transformation temperature
- **Quench:** Rapid cool for martensite formation
- **Tempering:** Reheat for toughness and stress relief

### Case Hardening
- **Carburizing:** Add carbon to surface
- **Nitriding:** Add nitrogen to surface
- **Purpose:** Hard wear surface, tough core

## Heat Treatment Standards

### AMS 2750: Pyrometry
- **Pyrometry:** Temperature measurement and control
- **Furnace classification:** Classes 1-6 based on instrumentation
- **Temperature uniformity surveys (TUS):** Verify furnace uniformity
- **System accuracy tests (SAT):** Verify sensor accuracy

### AMS 2759: Aluminum Heat Treatment
- **2759/1:** Castings
- **2759/2:** Consumable Electrode Melted Alloys
- **2759/3:** Wrought Aluminum Alloys (Solution/Precipitation)
- **2759/6:** Wrought Aluminum Alloys (Thermal Solution Treatment)
- **2759/7:** Stress Relieving

### AMS 2770: Steel Heat Treatment
- **2770A-F:** Various steel heat treatment specifications
- **2771:** Stress Relieving of Steel Parts

### AMS H-Series: Hardness Testing
- **AMS-H-6875:** Hardness and Conductivity Test Methods

## Pyrometry Requirements per AMS 2750

### Temperature Sensors
- **Thermocouples:** Type K, N, R, S (depending on temperature)
- **Placement:** Work zone, multiple locations
- **Calibration:** Per AMS 2750 frequency (daily, quarterly, annual)

### Furnace Instrumentation
- **Control Thermocouple:** Controls furnace temperature
- **Recording System:** Continuous recording (chart or digital)
- **Overtemperature Protection:** Independent high-limit cutoff

### Temperature Uniformity Survey (TUS)
- **Frequency:** Quarterly, semi-annual, or annual (depends on class)
- **Procedure:** 9-point survey in work zone
- **Acceptance:** ±15°F uniformity for most aerospace processes
- **Record:** TUS report with date, results, corrective actions

### System Accuracy Test (SAT)
- **Frequency:** Quarterly, semi-annual, or annual
- **Procedure:** Compare furnace sensors to calibrated reference
- **Acceptance:** Within ±5°F of reference
- **Corrective action:** Recalibrate or replace sensors

## Heat Treatment Processes

### Aluminum Solution + Aging (T6)

**Example: 7075-T6 Aluminum**

1. **Solution Heat Treatment**
   - Temperature: 860-890°F (460-477°C)
   - Time: Per thickness (1-2 hours typical)
   - Quench: Water or polymer quench, <15 seconds to 212°F

2. **Aging**
   - Temperature: 250°F (121°C)
   - Time: 24 hours
   - Cooling: Air cool to room temperature

**Critical Parameters:**
- Solution temperature: ±10°F
- Time at temperature: Per spec
- Quench delay: <15 seconds from furnace to quench
- Quench medium temperature: <100°F
- Aging temperature: ±5°F
- Aging time: ±15 minutes

### Steel Hardening and Tempering

**Example: 4340 Steel (200-220 ksi UTS)**

1. **Austenitizing**
   - Temperature: 1550-1600°F (843-871°C)
   - Time: 30-60 minutes (per section size)
   - Atmosphere: Protective (nitrogen or endogas)

2. **Quench**
   - Medium: Oil or polymer
   - Agitation: Moderate to vigorous
   - Cool to <150°F

3. **Tempering**
   - Temperature: 700-800°F (371-427°C) for 200 ksi
   - Time: 2 hours minimum
   - Multiple tempers: 2-3 cycles typical

**Critical Parameters:**
- Austenitizing temp: ±15°F
- Quench delay: <10 seconds
- Tempering temp: ±10°F
- Hardness verification: Test coupons or parts

## Quality Control

### Process Monitoring
- **Temperature recording:** Continuous chart or digital
- **Load tracking:** Part numbers, heat lot, furnace load ID
- **Quench conditions:** Medium, temperature, agitation
- **Time at temperature:** Start and end times

### Verification Testing
- **Hardness testing:** Per AMS-H-6875, sample or 100%
- **Conductivity (aluminum):** Eddy current per AMS 2658
- **Microstructure:** Metallographic examination (samples)
- **Tensile testing:** Mechanical properties (qualification)

### Acceptance Criteria
- **Hardness range:** Per material specification (e.g., 7075-T6: 82-87 HRB)
- **Conductivity:** Per AMS or company spec (e.g., 7075-T6: 33-37% IACS)
- **Microstructure:** Grain size, precipitate distribution (if specified)

## Lot Control

### Heat Treat Lot Definition
- **Same furnace load:** Parts processed together
- **Same material heat:** Same mill heat lot
- **Same process parameters:** Same recipe/cycle

### Lot Traceability
- **Heat treat lot number:** Unique identifier
- **Parts in lot:** Serial numbers or part numbers
- **Process parameters:** Temperature, time, quench
- **Test results:** Hardness, conductivity, any other tests

## Rework and Re-Heat Treatment

### Re-Heat Treatment Limits
- **Aluminum:** Typically 1-2 re-heat treatments allowed
- **Steel:** Multiple tempering allowed, limited re-hardening
- **Approval:** Engineering approval required for rework

### Process
1. Identify non-conforming condition (hardness, conductivity)
2. Engineering disposition (rework or scrap)
3. Strip coating if applicable
4. Re-heat treat per approved procedure
5. Re-test and verify conformance

## Distortion Control

### Minimize Distortion
- **Fixturing:** Support part during heat treatment
- **Quench technique:** Optimize quench rate and uniformity
- **Stress relief:** Before final machining if necessary
- **Design:** Avoid thin/thick section transitions

### Straightening
- **Press straightening:** Cold straightening within limits
- **Hot straightening:** Limited temperature and deformation
- **Limits:** Per specification (e.g., max 2% cold work)
- **Re-test:** Hardness/conductivity after straightening

## Documentation

### Heat Treatment Records
- Part number and serial number
- Material specification and heat lot
- Heat treatment specification (e.g., AMS 2759/3)
- Furnace identification
- Temperature and time (chart or data log)
- Quench details
- Test results (hardness, conductivity)
- Operator signature and date

### Record Retention
- **Flight-critical parts:** Permanent retention
- **Non-critical parts:** 10 years minimum

## Equipment Maintenance

### Preventive Maintenance
- Furnace heating elements and controls
- Quench system pumps and agitation
- Temperature sensors and instruments
- Furnace atmosphere systems (if used)

### Calibration
- **Thermocouples:** Per AMS 2750 (quarterly to annual)
- **Hardness testers:** Annual calibration
- **Conductivity meters:** Annual calibration

## Environmental, Health, and Safety

### Heat Treatment Hazards
- **Burns:** Hot furnaces and parts
- **Fumes:** Oil quench smoke, protective atmospheres
- **Fire:** Oil quench tanks

### Controls
- **PPE:** Heat-resistant gloves, face shield, long sleeves
- **Ventilation:** Local exhaust for quench tanks
- **Fire suppression:** Automatic systems for quench tanks
- **Training:** Safe handling of hot parts and equipment

## References

- AMS 2750: Pyrometry
- AMS 2759 series: Aluminum heat treatment
- AMS 2770 series: Steel heat treatment
- AMS-H-6875: Hardness testing
- Link to **CONTROL_PLAN/** for heat treatment controls
- Link to **08-QUALITY/** for inspection and testing
- Link to **13-TRAINING_COMPETENCY/** for heat treater certification
