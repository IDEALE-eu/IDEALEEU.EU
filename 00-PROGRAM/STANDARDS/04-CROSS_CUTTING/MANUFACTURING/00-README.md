# MANUFACTURING

Manufacturing quality and process standards.

## Overview

This directory contains standards for manufacturing quality, cleanroom environments, testing laboratories, and occupational health and safety.

## Applicable Standards

### ISO 14644 - Cleanrooms and Associated Controlled Environments
- **Scope**: Classification, design, operation of cleanrooms
- **Parts**: 9 parts covering classification, monitoring, design, operations
- **Applicability**: Spacecraft AIT, precision manufacturing, semiconductor fabrication

### ISO/IEC 17025 - General Requirements for the Competence of Testing and Calibration Laboratories
- **Scope**: Quality and technical competence requirements for labs
- **Coverage**: Management, technical requirements, accreditation
- **Applicability**: Test labs, calibration labs, metrology

### ISO 45001 - Occupational Health and Safety Management Systems
- **Scope**: OH&S management framework
- **Coverage**: Hazard identification, risk assessment, worker participation
- **Applicability**: All manufacturing and test facilities

### AS9100 - Quality Management Systems - Requirements for Aviation, Space and Defense Organizations
- **Scope**: QMS for aerospace industry (based on ISO 9001)
- **Revision**: AS9100D (current)
- **Applicability**: Aircraft and spacecraft manufacturing, suppliers

### ISO 9001 - Quality Management Systems - Requirements
- **Scope**: General QMS requirements
- **Applicability**: All organizations, baseline for AS9100

## Cleanroom Standards (ISO 14644)

### Cleanroom Classification

Cleanliness by particle count per cubic meter:
- **ISO Class 1**: ≤ 10 particles ≥ 0.1 µm (ultra-clean, semiconductor)
- **ISO Class 3**: ≤ 1,000 particles ≥ 0.1 µm
- **ISO Class 5**: ≤ 100,000 particles ≥ 0.1 µm (old Class 100)
- **ISO Class 7**: ≤ 10⁶ particles ≥ 0.5 µm (old Class 10,000)
- **ISO Class 8**: ≤ 10⁷ particles ≥ 0.5 µm (old Class 100,000)

### Spacecraft AIT Cleanrooms
- **ISO Class 7 or 8** typical for spacecraft assembly
- **ISO Class 5** for critical operations (optical surfaces, propulsion)
- **Airflow**: HEPA-filtered, laminar or turbulent
- **Pressure**: Positive relative to surroundings

### Cleanroom Practices
- **Garments**: Coveralls, hoods, gloves, shoe covers
- **Entry**: Air showers, sticky mats
- **Materials**: Low-particulating, low-outgassing
- **Monitoring**: Particle counters, environmental sensors
- **Cleaning**: Regular cleaning and disinfection

## Laboratory Standards (ISO/IEC 17025)

### Management Requirements
- Organization and management structure
- Quality management system
- Document and data control
- Impartiality and confidentiality
- Complaints and appeals

### Technical Requirements
- Personnel competence and training
- Facilities and environmental conditions
- Equipment (calibration, maintenance, handling)
- Measurement traceability
- Sampling and test methods
- Validation of methods
- Uncertainty of measurement
- Data integrity and reporting

### Accreditation
- **Accreditation Bodies**: NVLAP (US), UKAS (UK), COFRAC (France), DAkkS (Germany)
- **Scope**: Specific test methods and calibrations accredited
- **Audits**: Initial assessment, surveillance, re-assessment (4-5 years)

## Occupational Health and Safety (ISO 45001)

### OH&S Management System
- **Leadership**: Top management commitment
- **Planning**: Hazard identification, risk assessment
- **Support**: Resources, competence, awareness, communication
- **Operation**: Operational controls, emergency preparedness
- **Performance Evaluation**: Monitoring, audits, management review
- **Improvement**: Incident investigation, corrective actions

### Hazard Types
- **Physical**: Noise, vibration, radiation, temperature
- **Chemical**: Solvents, adhesives, propellants, acids
- **Biological**: Pathogens, allergens
- **Ergonomic**: Repetitive motion, lifting, workstation design
- **Psychosocial**: Stress, workload, work hours

### Risk Assessment
- Identify hazards
- Assess risk (likelihood × severity)
- Determine controls (elimination, substitution, engineering, administrative, PPE)
- Monitor effectiveness

## Quality Management (AS9100 / ISO 9001)

### AS9100 Enhancements over ISO 9001
- **Product Safety**: Safety-critical items, FOD prevention
- **Configuration Management**: Design and process changes
- **Risk Management**: Risk-based thinking throughout lifecycle
- **Counterfeit Prevention**: Parts and materials authenticity
- **Special Processes**: Welding, heat treatment, NDT, etc.
- **First Article Inspection (FAI)**: AS9102 procedures
- **Key Characteristics**: Critical features requiring verification

### Quality Management Principles
1. Customer focus
2. Leadership
3. Engagement of people
4. Process approach
5. Improvement
6. Evidence-based decision making
7. Relationship management

### QMS Processes
- **Management**: Quality policy, objectives, planning, review
- **Resources**: People, infrastructure, environment, monitoring equipment
- **Realization**: Design, purchasing, production, service
- **Measurement**: Monitoring, audits, nonconformities, improvement

## Manufacturing Processes

### Special Processes (AS9100)
Processes where output cannot be fully verified by inspection:
- **Welding**: TIG, MIG, electron beam, laser
- **Heat Treatment**: Annealing, hardening, stress relief
- **Surface Treatment**: Anodizing, plating, coating
- **Non-Destructive Testing (NDT)**: X-ray, ultrasound, dye penetrant, eddy current
- **Composite Layup**: Hand layup, automated fiber placement (AFP)
- **Brazing and Soldering**: Joining processes

Requirements:
- Qualified procedures
- Qualified equipment
- Qualified personnel
- Process monitoring and control
- Records

### Foreign Object Debris (FOD)
- **Definition**: Any object that can cause damage or malfunction
- **Prevention**: Tool control, cleaning, inspections, barriers
- **Detection**: Visual inspection, X-ray, borescope
- **Critical for**: Aircraft engines, spacecraft mechanisms, propulsion

## Key Deliverables

1. **Quality Management System Manual** - QMS description per AS9100/ISO 9001
2. **Cleanroom Qualification** - Particle counts, airflow, pressure
3. **Laboratory Accreditation** - ISO/IEC 17025 scope and certificate
4. **OH&S Management System** - ISO 45001 compliance
5. **Special Process Procedures** - Qualified processes (welding, NDT, etc.)
6. **First Article Inspection Report (FAIR)** - AS9102 verification
7. **Calibration Certificates** - Test equipment calibration per ISO/IEC 17025

## Compliance Requirements

- Manufacturing per AS9100D or ISO 9001:2015
- Cleanrooms per ISO 14644
- Laboratories per ISO/IEC 17025 (if accreditation required)
- OH&S per ISO 45001 or local regulations (OSHA, etc.)
- Special processes qualified and controlled
- Personnel trained and qualified

## Integration with Other Standards

### Aircraft
- AS9100 required for Part 21 Production Certificate
- Manufacturing supports DO-178C/DO-254 development
- FOD critical for aircraft safety

### Spacecraft
- Cleanrooms per ECSS-Q-ST-70C and ISO 14644
- Manufacturing quality per ECSS-Q-ST-20C
- AIT facilities support ECSS-E-ST-10-06C

## Best Practices

- Establish QMS early (before production)
- Seek AS9100 certification
- Maintain cleanroom discipline
- Accredit test labs where customer requires
- Regular OH&S training and drills
- FOD prevention culture
- Lessons learned from nonconformities

## Common Pitfalls

- QMS too bureaucratic (slows work)
- Cleanroom practices not followed (contamination)
- Equipment not calibrated (invalid test results)
- OH&S ignored (accidents, injuries)
- Special processes not qualified (quality issues)
- FOD not controlled (damage to equipment)

## References

- 01-REGISTER/STANDARDS_REGISTER.csv - STD-023 (AS9100D)
- ISO 14644 series (purchase from ISO)
- ISO/IEC 17025 (purchase from ISO)
- ISO 45001 (purchase from ISO)
- AS9100D (purchase from SAE/IAQG)
- 00-PROGRAM/QUALITY_QMS/ - Program QMS implementation

---

**Status**: Configuration-controlled per 00-PROGRAM/CONFIG_MGMT/
