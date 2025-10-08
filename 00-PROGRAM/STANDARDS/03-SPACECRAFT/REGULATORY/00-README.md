# REGULATORY

Spacecraft regulatory standards and launch safety requirements.

## Overview

This directory contains regulatory requirements for spacecraft, including ESA production assurance, national space agency requirements, and launch range safety.

## Applicable Regulations

### ESA Production Assurance
- **ESA PSS standards**: Product Assurance and Safety Standards (older, being replaced by ECSS)
- **ECSS-Q series**: Quality assurance, reliability, safety
- **Independent Product Assurance (IPA)**: ESA oversight of contractor quality

### National Regulatory Bodies
- **ESA**: European Space Agency (European cooperation)
- **NASA**: National Aeronautics and Space Administration (United States)
- **CNES**: Centre National d'Études Spatiales (France)
- **DLR**: Deutsches Zentrum für Luft- und Raumfahrt (Germany)
- **ASI**: Agenzia Spaziale Italiana (Italy)
- **UKSA**: UK Space Agency (United Kingdom)

### Launch Range Safety
- **Range Safety Requirements**: Specific to launch site (Kourou, Cape Canaveral, Vandenberg, etc.)
- **Flight Termination System (FTS)**: For expendable launch vehicles
- **Debris Analysis**: Ensure no harm to populated areas
- **Toxic Materials**: Handling of hazardous propellants

## ESA Requirements

### ESA Project Phases
- **Phase 0**: Mission Analysis / Needs Identification
- **Phase A**: Feasibility
- **Phase B**: Preliminary Definition
- **Phase C**: Detailed Definition
- **Phase D**: Qualification and Production
- **Phase E**: Utilization (Operations)
- **Phase F**: Disposal

### ESA Reviews
- **Mission Definition Review (MDR)**: End of Phase A
- **Preliminary Design Review (PDR)**: During Phase B
- **Critical Design Review (CDR)**: End of Phase C/D
- **Qualification Review (QR)**: During Phase D
- **Acceptance Review (AR)**: End of Phase D
- **Flight Readiness Review (FRR)**: Before launch
- **Operational Readiness Review (ORR)**: Operations preparedness

### ESA Product Assurance
- **IPA (Independent Product Assurance)**: ESA representatives oversee contractor
- **Quality Assurance**: ISO 9001, AS9100, ECSS-Q-ST-20C
- **Reliability**: ECSS-Q-ST-30C (FMECA, reliability prediction)
- **Safety**: ECSS-Q-ST-40C (hazard analysis, safety verification)
- **EEE Components**: ECSS-Q-ST-60C (parts selection, screening)
- **Materials and Processes**: ECSS-Q-ST-70C (material qualification)

## NASA Requirements

### NASA Standards
- **NPR 7120.5**: NASA Space Flight Program and Project Management Requirements
- **NPR 7123.1**: NASA Systems Engineering Processes and Requirements
- **NASA-STD-8739**: Workmanship standards (soldering, crimping, etc.)
- **NASA-HDBK-4002A**: Mitigating In-Space Charging Effects

### NASA Reviews
- **SRR**: System Requirements Review
- **MDR**: Mission Definition Review
- **SRR/SDR**: System Requirements / System Design Review
- **PDR**: Preliminary Design Review
- **CDR**: Critical Design Review
- **TRR**: Test Readiness Review
- **FRR**: Flight Readiness Review
- **ORR**: Operational Readiness Review

### NASA Safety
- **NASA Safety Manual**: NPR 8715.3 (General Safety Program)
- **Range Safety**: KSC, VAFB, Wallops requirements
- **Payload Safety**: ISS payloads have additional requirements

## Launch Vehicle Interface

### Interface Control Document (ICD)
- **Mechanical Interface**: Attach fitting dimensions, bolt pattern
- **Electrical Interface**: Separation signals, umbilicals
- **Mass and CG**: Mass limits, center of gravity envelope
- **Stiffness**: Natural frequency requirements (avoid coupled loads)
- **Environments**: Loads, vibration, acoustic, shock, thermal

### Common Launch Vehicles
- **Ariane 6**: ESA heavy-lift (payload up to 11.5 tons to GTO)
- **Vega-C**: ESA small-lift (payload up to 2.3 tons to LEO)
- **Falcon 9**: SpaceX medium-to-heavy lift
- **Electron**: Rocket Lab small-lift
- **Soyuz**: Roscosmos (launched from Baikonur or Kourou)

### Launch Vehicle User Manuals
- Define requirements for payload
- Mechanical, electrical, environmental interfaces
- Analysis and verification requirements
- Launch site operations

## Launch Range Safety

### Range Safety Objectives
- Protect public and property
- Prevent debris from impacting populated areas
- Ensure controlled re-entry or orbit
- Handle hazardous materials safely

### Safety Analyses
- **Debris Analysis**: Predict debris footprint for failures
- **Toxic Plume Modeling**: Dispersion of propellants
- **Collision Avoidance**: Orbital debris and active satellites
- **Flight Termination**: Destruct system for controlled failure

### Hazardous Materials
- **Propellants**: Hydrazine, MMH, NTO (toxic, corrosive)
- **Batteries**: Lithium batteries (fire hazard)
- **Radioactive**: RTG (radioisotope thermoelectric generator)
- **Pressurized Systems**: High-pressure vessels

### Safety Documentation
- **Range Safety Data Package**: Flight termination, debris analysis
- **Hazard Analysis**: All hazards and mitigations
- **Safety Review**: Range safety approval before launch

## Planetary Protection

### COSPAR Planetary Protection Policy
- **Objective**: Prevent biological contamination of planets and Earth
- **Categories**: I-V based on mission type and destination
  - **Category I**: No protection (e.g., Venus flyby)
  - **Category II**: Simple documentation (e.g., Mars flyby)
  - **Category III**: Bioburden control (e.g., Mars orbiter)
  - **Category IV**: Stringent bioburden control (e.g., Mars lander)
  - **Category V**: Containment (sample return from life-bearing body)

### Bioburden Control
- **Cleaning**: Remove organic and microbial contamination
- **Bioassay**: Measure microbial counts (spores/m²)
- **Sterilization**: Heat (dry heat microbial reduction) or other methods
- **Documentation**: Bioburden reports, cleaning logs

## Space Debris Mitigation

### IADC Guidelines (Inter-Agency Space Debris Coordination Committee)
- **Passivation**: Deplete energy sources at end-of-life
- **De-orbit**: Remove from orbit within 25 years (LEO)
- **GEO Disposal**: Raise to graveyard orbit (300 km above GEO)
- **Breakup Prevention**: Avoid explosions and collisions

### ECSS Standards
- **ECSS-U-AS-10C**: Adoption of ISO 24113 (space debris mitigation)

## Export Control

### ITAR (International Traffic in Arms Regulations)
- **Applicability**: U.S. defense articles and services
- **Space Items**: Many spacecraft components are ITAR-controlled
- **Compliance**: Export licenses, secure facilities, U.S. person restrictions

### EAR (Export Administration Regulations)
- **Applicability**: U.S. commercial items not on USML (ITAR)
- **Dual-Use**: Items with both commercial and military applications

### European Export Control
- **EU Dual-Use Regulation**: EC Regulation 428/2009
- **National Controls**: Each EU member state implements controls

## Key Deliverables

1. **Regulatory Compliance Matrix** - All applicable regulations and compliance status
2. **Launch Vehicle ICD Compliance** - Mechanical, electrical, environmental compliance
3. **Range Safety Data Package** - Debris analysis, flight termination, hazards
4. **Planetary Protection Plan** - Bioburden control, sterilization (if applicable)
5. **Space Debris Mitigation Plan** - Passivation, de-orbit/disposal strategy
6. **Hazardous Materials Handling** - Safety procedures for propellants, batteries
7. **Export Control Plan** - ITAR/EAR compliance (if applicable)
8. **Independent Product Assurance Reports** - IPA findings and closure

## Compliance Requirements

- Spacecraft shall comply with ESA/NASA/agency requirements
- Launch vehicle ICD requirements met
- Range safety approval obtained
- Planetary protection category assigned and requirements met
- Space debris mitigation per IADC guidelines
- Export control compliance (if applicable)

## Integration with Other Standards

- **ECSS-E-ST-10C** - Systems engineering defines regulatory requirements
- **ECSS-Q series** - Quality, reliability, safety assurance
- **Launch vehicle user manuals** - Interface requirements

## Tools and Templates

- Regulatory compliance matrix
- Hazard analysis templates
- Range safety analysis tools
- Planetary protection procedures

## References

- 01-REGISTER/STANDARDS_REGISTER.csv - ESA and regulatory standards
- ECSS Portal: https://ecss.nl
- ESA website: https://www.esa.int
- NASA standards: https://standards.nasa.gov
- Launch vehicle user manuals (Ariane, Vega, Falcon, etc.)
- IADC: https://www.iadc-home.org

---

**Status**: Configuration-controlled per 00-PROGRAM/CONFIG_MGMT/
