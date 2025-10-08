# Derating Rules for Reliability

## Overview

Derating guidelines to improve reliability by operating components below maximum ratings.

## General Derating Philosophy

### Purpose
- Reduce stress and failure rates
- Improve reliability and mission life
- Margin for uncertainties and variations
- Graceful degradation under off-nominal conditions

### Derating Factors
- Voltage, current, power
- Temperature (junction, case, ambient)
- Frequency, speed
- Mechanical stress
- Environmental factors

## Derating Guidelines by Component

### Resistors

**Power Derating:**
- Derating Factor: 50-70% of rated power at maximum operating temperature
- Lower derating for higher reliability (50% for space)

**Temperature:**
- Maximum hotspot temperature: 125°C (film resistors)
- Derate power linearly above rated ambient temperature

**Example:**
- 1/4 W resistor at 70°C ambient and 50% derating
- Allowable power: 0.125 W maximum

**Voltage:**
- Voltage across resistor < 70% of maximum rated voltage
- Important for high-value resistors where voltage rating may be limiting

### Capacitors

**Voltage Derating:**
- Ceramic (Class II): 50-60% of rated voltage
- Tantalum: 50-60% of rated voltage (lower for higher reliability)
- Aluminum electrolytic: 60-80% of rated voltage
- Film: 60-70% of rated voltage

**Temperature:**
- Maximum case temperature: 85-105°C depending on type and voltage derating
- Tantalum: Avoid temperatures >85°C at high voltage stress

**Ripple Current:**
- Electrolytic capacitors: Keep ripple current <70% of rated ripple current
- ESR (Equivalent Series Resistance) causes heating; thermal analysis required

**Tantalum Special Considerations:**
- Voltage surge protection recommended (series resistor or inrush limiting)
- Avoid applications with voltage transients or reverse bias
- Lower derating (40-50%) for higher risk applications

### Inductors and Transformers

**Current Derating:**
- DC current: <80% of rated current
- AC current: Consider RMS and peak currents

**Temperature:**
- Maximum hotspot: 125-140°C
- Core material temperature limits (ferrite: 100-125°C)

**Frequency:**
- Operate below SRF (Self-Resonant Frequency)
- Core losses increase with frequency; thermal analysis needed

### Diodes

**Current Derating:**
- Average forward current: 50-70% of maximum rated
- Peak current: <80% of peak forward current rating

**Voltage Derating:**
- Reverse voltage (PIV): 50-60% of maximum rating
- Zener diodes: 60-80% of rated power and voltage

**Temperature:**
- Junction temperature: <125°C (preferably <100°C for space)
- Calculate junction temperature: Tj = Ta + (Pd × θja)

**Example:**
- 1N4148 diode: VR = 100V, IF = 300mA, Tj = 175°C max
- Derated: VR < 50V, IF < 150mA, Tj < 125°C

### Transistors (Bipolar)

**Power Derating:**
- Power dissipation: 50-60% of maximum rating at case temperature
- Derating curve above 25°C

**Voltage Derating:**
- VCE: 60-70% of VCEO or VCBO (whichever applicable)
- Ensure operation in safe operating area (SOA)

**Current Derating:**
- IC: 70% of maximum rated collector current

**Temperature:**
- Junction temperature: <125°C (space), <150°C (other)
- Calculate Tj from power dissipation and thermal resistance

**Example:**
- 2N2222: VCE = 40V, IC = 800mA, Pd = 1.8W (at 25°C)
- Derated: VCE < 28V, IC < 560mA, Pd < 0.9W at 70°C case temp, Tj < 125°C

### MOSFETs

**Voltage Derating:**
- VDS: 60-70% of rated drain-source voltage
- VGS: 60-80% of gate-source voltage rating

**Current Derating:**
- ID: 60-80% of rated drain current at operating temperature
- Consider RDSon increase with temperature

**Power Derating:**
- Power dissipation: 50-60% at case temperature
- Thermal analysis critical for switching applications

**Temperature:**
- Junction temperature: <125°C (space), <150°C (other)
- Gate oxide reliability concerns at high temperature and voltage stress

**Radiation Considerations:**
- Threshold voltage shift with TID
- SEE susceptibility (SEB, SEGR)
- Derate VDS to 50% or lower for high-radiation environments

### Integrated Circuits (ICs)

**Voltage Derating:**
- Supply voltage: 80-90% of maximum rating
- Input/output voltages: Within absolute maximum ratings with margin

**Current Derating:**
- Output current: 70-80% of maximum rating per pin
- Total device current: <80% of maximum

**Power Derating:**
- Power dissipation: 50-60% at case or ambient temperature
- Consider junction temperature limit

**Temperature:**
- Junction temperature: <100°C (commercial), <125°C (space)
- Military-grade parts: -55°C to +125°C operation

**Speed and Timing:**
- Clock frequency: <80% of maximum rated frequency
- Setup and hold times: Meet timing with margin

**Radiation (for space ICs):**
- SEE sensitivity: Operate below threshold LET if possible
- TID tolerance: Select parts with margin above mission dose

### Power Devices (MOSFETs, IGBTs)

**Voltage Derating:**
- VDS or VCE: 50-60% of rated voltage (lower for higher reliability and radiation)

**Current Derating:**
- Continuous current: 50-70% of maximum rating at case temperature

**Power and Temperature:**
- Junction temperature: <125°C (preferably <100°C for space)
- Thermal cycling stress reduction
- Safe Operating Area (SOA) compliance with margin

**Switching:**
- dV/dt and dI/dt: Within safe operating area
- Gate drive voltage: Within safe limits
- Turn-on/turn-off losses considered in thermal analysis

### Optoelectronics

**LEDs:**
- Forward current: 50-70% of maximum rated current
- Power dissipation: 50% of maximum
- Consider radiation-induced output degradation

**Photodetectors:**
- Reverse voltage: 50-70% of maximum rating
- Power dissipation: 50% of rating
- Radiation darkening and sensitivity degradation in space

**Optocouplers:**
- Forward current (LED): 50-70% of maximum
- CTR (Current Transfer Ratio) degradation with radiation
- Derate CTR to account for radiation-induced reduction

### Connectors

**Current Derating:**
- Contact current: 50-70% of maximum rated current per contact
- Derating for multiple contacts carrying current in same connector

**Voltage Derating:**
- Voltage: 70-80% of rated voltage
- Altitude derating if applicable

**Mating Cycles:**
- Limit mating cycles to 50-70% of rated cycles
- Critical for ground operations and testing

**Temperature:**
- Operate within connector temperature rating
- Thermal analysis for high current contacts

### Relays

**Contact Current and Voltage:**
- Current: 50-70% of rated contact current
- Voltage: 70-80% of rated voltage
- Lower derating for inductive loads (arcing)

**Switching Life:**
- Number of operations: <50% of rated electrical life
- Higher for resistive loads

**Coil:**
- Coil voltage: 80-90% of rated voltage
- Coil power: <80% of rated power
- Temperature rise considered

**Environment:**
- Avoid operation near maximum temperature rating
- Vibration and shock well within rating

## Temperature Considerations

### Junction Temperature Calculation

**Formula:**
Tj = Ta + (Pd × θja)

Where:
- Tj = Junction temperature (°C)
- Ta = Ambient temperature (°C)
- Pd = Power dissipation (W)
- θja = Thermal resistance, junction-to-ambient (°C/W)

For packages with heat sinks:
Tj = Ta + (Pd × θjc) + (Pd × θcs) + (Pd × θsa)

Where:
- θjc = Junction-to-case
- θcs = Case-to-sink
- θsa = Sink-to-ambient

### Worst-Case Temperatures
- Maximum ambient or case temperature
- Highest power dissipation
- Thermal analysis accounting for enclosure, altitude, mission phases
- Margin for uncertainties (±10°C typical)

## Derating Verification

### Analysis
- Worst-case analysis (WCA)
- Component stress analysis
- Thermal analysis
- Reliability prediction (MIL-HDBK-217, FIDES)

### Testing
- Thermal vacuum testing
- Worst-case environmental testing
- Temperature measurement (thermocouples, IR imaging)
- Correlation to analysis

### Documentation
- Derating analysis report
- Part stress summary tables
- Thermal analysis results
- Compliance matrix

## Exceptions and Waivers

### When Derating Cannot Be Met
- Document justification
- Assess risk and reliability impact
- Mitigation measures (redundancy, screening, monitoring)
- Approval by appropriate authority
- Acceptance by customer if required

### Waiver Process
- Formal waiver request
- Technical justification
- Risk assessment
- Alternative analysis (e.g., FMEA)
- Approval and documentation

## Standards and References

- MIL-HDBK-217: Reliability Prediction of Electronic Equipment
- MIL-STD-975: NASA Standard Electrical, Electronic, and Electromechanical (EEE) Parts List
- ECSS-Q-ST-30-11: Derating and end-of-life parameter drifts - EEE components
- NASA-STD-8739.11: Parts and Materials Selection List (PMSL)
- IPC-9592: Requirements for Power Conversion Devices for the Computer and Telecommunications Industries
