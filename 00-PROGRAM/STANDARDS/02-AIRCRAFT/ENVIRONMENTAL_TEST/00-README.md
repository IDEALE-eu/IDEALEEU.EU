# ENVIRONMENTAL_TEST

Environmental testing standards for airborne equipment.

## Overview

This directory contains standards for environmental testing of aircraft equipment, primarily DO-160.

## Applicable Standards

### DO-160G - Environmental Conditions and Test Procedures for Airborne Equipment
- **Current Revision**: DO-160G (latest), also known as EUROCAE ED-14G
- **Scope**: Environmental qualification of airborne equipment
- **Purpose**: Ensure equipment operates reliably in aircraft environment

## Test Categories

DO-160 defines environmental test categories for various installation locations and aircraft types:

### Section 4 - Temperature and Altitude
- Operating temperature ranges (A1-A5, B1-B3, C1-C3)
- Storage temperature
- Altitude performance
- Decompression

### Section 5 - Temperature Variation
- Temperature shock and gradient testing

### Section 6 - Humidity
- Humidity exposure testing (95% RH)

### Section 7 - Operational Shocks and Crash Safety
- Shock pulses simulating hard landing, arrested landing
- Crash safety requirements

### Section 8 - Vibration
- Vibration categories by installation location
- Sinusoidal, random, intermittent vibration
- Curve 1-10 (propeller), 11-20 (jet), 21-30 (helicopter)

### Section 9 - Explosive Atmosphere
- Flammability and explosion protection

### Section 10 - Waterproofness
- Drip, spray, immersion testing

### Section 11 - Fluids Susceptibility
- Resistance to aircraft fluids (fuel, hydraulic, oil)

### Section 12 - Sand and Dust
- Sand and dust exposure

### Section 13 - Fungus Resistance
- Fungus growth resistance

### Section 14 - Salt Spray
- Corrosion resistance

### Section 15 - Magnetic Effect
- Magnetic field emissions

### Section 16 - Power Input
- AC/DC power quality, frequency, voltage variation
- Ripple, transients, interruptions

### Section 17 - Voltage Spike
- Transient voltage protection

### Section 18 - Audio Frequency Conducted Susceptibility
- Immunity to conducted audio frequencies

### Section 19 - Induced Signal Susceptibility
- Immunity to induced signals

### Section 20 - Radio Frequency Susceptibility (Radiated)
- Radiated EMI immunity (10 kHz - 40 GHz)
- Field strengths by category

### Section 21 - Emission of Radio Frequency Energy
- Conducted and radiated EMI emissions
- Compatibility with aircraft systems and external receivers

### Section 22 - Lightning Induced Transient Susceptibility
- Direct and indirect lightning effects
- Waveforms A, B, C, D, H, multiple stroke
- Pin injection and cable bundle testing

### Section 23 - Lightning Direct Effects
- Direct attachment zones 1A, 1B, 1C, 2A, 2B, 3
- Current waveforms and action integrals

### Section 24 - Icing
- Icing conditions for external equipment

### Section 25 - Electrostatic Discharge
- ESD immunity testing

### Section 26 - Fire, Flammability
- Fire resistance, smoke, toxicity

## Test Category Selection

Equipment category assignment based on:
- Aircraft type (commercial transport, regional, helicopter, military)
- Installation location (flight deck, cabin, avionics bay, wheel well, external)
- Criticality and safety classification

## Compliance Approach

1. **Test Plan**: Define applicable sections and categories
2. **Equipment Qualification**: Test per DO-160 procedures
3. **Test Report**: Document results and compliance
4. **Installation Considerations**: Verify installation matches test assumptions
5. **Certification Credit**: Submit to EASA/FAA as part of ETSOA or STC

## Key Deliverables

1. **DO-160 Test Plan** - Sections and categories applicable
2. **DO-160 Test Procedures** - Detailed test setups and methods
3. **DO-160 Test Report** - Results, deviations, compliance statement
4. **Installation Conditions** - Environmental assumptions verified

## Integration with Other Standards

- **ARP4754A** - System requirements define environmental conditions
- **DO-178C/DO-254** - Software/hardware tested in DO-160 environment
- **CS-25/Part 25** - Environmental requirements flow from certification specifications

## Test Facilities

- Accredited labs required for certification credit
- Witness testing by certification authorities
- Calibration and quality requirements per ISO/IEC 17025

## Tools and Templates

- See 05-MAPPINGS/ for DO-160 compliance matrices
- Test plan and report templates
- Category selection guidance

## References

- 01-REGISTER/STANDARDS_REGISTER.csv - STD-005 (DO-160G)
- 06-INTERPRETATIONS/FAQ.md - DO-160 testing questions
- RTCA DO-160G document (purchase required)

---

**Status**: Configuration-controlled per 00-PROGRAM/CONFIG_MGMT/
