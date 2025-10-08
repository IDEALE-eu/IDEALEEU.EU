# REGULATORY

Regulatory standards and certification requirements for aircraft.

## Overview

This directory contains regulatory standards and certification specifications for aircraft development, type certification, and continued airworthiness.

## Applicable Regulations

### EASA CS-23 - Certification Specifications for Normal, Utility, Aerobatic, and Commuter Category Aeroplanes
- **Scope**: Small aircraft (≤ 8,600 kg / 19,000 lbs, ≤ 19 passengers)
- **Categories**: Normal, Utility, Aerobatic, Commuter
- **Structure**: Subparts A-H covering flight, structure, design, systems, equipment, etc.

### EASA CS-25 - Certification Specifications for Large Aeroplanes
- **Scope**: Large aircraft (> 5,700 kg / 12,500 lbs or > 19 passengers)
- **Structure**: Subparts A-H similar to CS-23, more stringent requirements
- **Amendment Level**: Important to track (e.g., Amendment 27)

### FAA 14 CFR Part 21 - Certification Procedures for Products and Articles
- **Subpart A**: General
- **Subpart B**: Type Certificates
- **Subpart C**: Provisional Type Certificates
- **Subpart D**: Changes to Type Certificates
- **Subpart E**: Supplemental Type Certificates (STC)
- **Subpart F**: Production Certificates
- **Subpart G**: Production Certificates
- **Subpart H**: Airworthiness Certificates
- **Subpart K**: Parts Manufacturer Approvals (PMA)
- **Subpart O**: Technical Standard Order Authorizations (TSOA)

### FAA 14 CFR Part 23 - Airworthiness Standards: Normal Category Airplanes
- **Scope**: Small aircraft, recently revised (performance-based)
- **Structure**: Subparts A-G covering flight, structures, design, systems, etc.

### FAA 14 CFR Part 25 - Airworthiness Standards: Transport Category Airplanes
- **Scope**: Large transport aircraft
- **Structure**: Subparts A-H parallel to EASA CS-25
- **Compliance**: Often used in conjunction with CS-25 for bilateral agreements

### FAA 14 CFR Part 33 - Airworthiness Standards: Aircraft Engines
- **Scope**: Engine type certification
- **Requirements**: Design, construction, performance, endurance testing

### FAA 14 CFR Part 35 - Airworthiness Standards: Propellers
- **Scope**: Propeller type certification
- **Requirements**: Design, construction, tests

## Certification Process

### Type Certificate (TC)
1. **Application** - Submit to EASA or FAA
2. **Certification Basis** - Establish applicable regulations and special conditions
3. **Certification Plan** - Define compliance methods
4. **Design Compliance** - Demonstrate compliance with regulations
5. **Type Inspection Authorization (TIA)** - Authority inspection and tests
6. **Type Certificate Issued** - Approval to manufacture and operate

### Supplemental Type Certificate (STC)
- Modification to existing type certificate
- Must comply with original certification basis + new requirements if applicable
- Examples: Avionics upgrades, cargo conversions, engine changes

### Production Certificate
- Authorization to manufacture aircraft per type design
- Quality system approval (AS9100 or equivalent)
- Conformity inspection at production facilities

### Airworthiness Certificate
- Individual aircraft certificate of airworthiness
- Standard (commercial, transport)
- Special (experimental, restricted, limited)

## Bilateral Agreements

### EASA-FAA Bilateral Aviation Safety Agreement (BASA)
- Mutual recognition of certifications
- Streamlined approval process
- Technical Implementation Procedures (TIPs)

### Other Bilateral Agreements
- Transport Canada
- Brazil (ANAC)
- China (CAAC)
- Japan (JCAB)

## Special Conditions and Exemptions

### Special Conditions
- When regulations don't address novel or unusual design features
- Authority issues special conditions with additional requirements
- Examples: Fly-by-wire, composite structures, advanced avionics

### Exemptions
- Relief from specific regulation requirements
- Must demonstrate equivalent level of safety
- Authority approval required

## Equivalent Level of Safety (ELOS)

- Alternative means of compliance when literal compliance impractical
- Demonstrate equivalent or better safety
- Examples: Different test methods, alternative materials, novel designs

## Key Regulatory Areas

### Flight Performance
- Takeoff, climb, cruise, descent, landing
- One-engine-inoperative (OEI) performance
- Stall characteristics and handling

### Structures
- Flight loads, ground loads, fatigue, damage tolerance
- Static tests, fatigue tests, flutter tests
- Material qualification

### Systems and Equipment
- Redundancy, failure modes, emergency systems
- Electrical, hydraulic, pneumatic, fuel systems
- Avionics, communication, navigation

### Powerplant
- Engine installation, controls, fuel system
- Propeller installation (if applicable)
- Fire protection, ice protection

### Flight Deck and Human Factors
- Control layout, display design
- Pilot workload, situation awareness
- See HUMAN_FACTORS/ for detailed standards

## Certification Documentation

1. **Type Certificate Data Sheet (TCDS)** - Approved configuration and limitations
2. **Airplane Flight Manual (AFM)** - Operating procedures and limitations
3. **Certification Plans** (PSCP, PSAC, PHAC, etc.)
4. **Compliance Reports** - Demonstration of compliance with regulations
5. **Type Inspection Report (TIR)** - Authority findings

## Continued Airworthiness

### Maintenance Program
- Maintenance planning document
- Airworthiness limitations
- Instructions for continued airworthiness (ICA)

### Service Bulletins (SB)
- Manufacturer-issued maintenance/modification instructions
- May be mandatory (via Airworthiness Directive)

### Airworthiness Directives (AD)
- Mandatory actions to maintain airworthiness
- Issued by authorities (EASA, FAA)
- Must be complied with per schedule

## Key Deliverables

1. **Certification Plan** - Overall strategy and schedule
2. **Type Certificate Application** - Formal application
3. **Compliance Checklist** - All regulations and compliance methods
4. **Compliance Reports** - Evidence of compliance for each regulation
5. **Type Certificate Data Sheet (TCDS)** - Approved design configuration
6. **Airplane Flight Manual (AFM)** - Operating limitations and procedures

## Compliance Requirements

- All applicable regulations must be complied with
- Certification basis established before design freeze (CDR)
- Compliance demonstration witnessed by authorities
- Documentation maintained per Part 21.48

## Integration with Other Standards

- **ARP4754A** - Systems engineering supports regulatory compliance
- **ARP4761** - Safety assessment per 25.1309
- **DO-178C/DO-254** - Software/hardware certification per 25.1301, 25.1309
- **DO-160** - Environmental qualification per installation requirements

## Tools and Templates

- Compliance checklists (CS-23, CS-25, Part 23, Part 25)
- Certification plan templates
- Compliance report templates

## References

- 01-REGISTER/STANDARDS_REGISTER.csv - STD-010 (CS-25), STD-011 (Part 25)
- EASA regulations: https://www.easa.europa.eu/regulations
- FAA regulations: https://www.ecfr.gov (Title 14 CFR)
- 06-INTERPRETATIONS/AUTHORITY_POSITION_PAPERS/ - Regulatory guidance

---

**Status**: Configuration-controlled per 00-PROGRAM/CONFIG_MGMT/
