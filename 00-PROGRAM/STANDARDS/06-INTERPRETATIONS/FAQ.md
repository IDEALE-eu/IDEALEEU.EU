# STANDARDS FAQ

Frequently Asked Questions about standards application.

## General Questions

### Q1: Which standards apply to my project?

**A**: The applicable standards depend on:
- **Domain**: Aircraft or spacecraft?
- **Certification Basis**: What are you certifying to? (CS-25, Part 25, ECSS)
- **System Criticality**: Safety classification (DAL for aircraft, criticality for spacecraft)
- **Customer Requirements**: What does customer specify?

Start with the Standards Register (01-REGISTER/STANDARDS_REGISTER.csv) and consult with Systems Engineering and Certification leads.

### Q2: Do I need to purchase standards or are they free?

**A**: Depends on the standard:
- **Purchase Required**: SAE (ARP, AMS), RTCA/EUROCAE (DO-xxx), ISO, IEC, ASTM
- **Free**: ECSS (download from https://ecss.nl), FAA/EASA regulations (from agency websites)
- See 07-LINKS/OFFICIAL_SOURCES.md for where to obtain

### Q3: Can I tailor a standard (not follow it exactly)?

**A**: Depends on the standard and authority:
- **Aircraft (EASA/FAA)**: Very limited tailoring. Deviations require authority approval. See 01-REGISTER/DEVIATIONS_WAIVERS.csv
- **Spacecraft (ECSS, ESA)**: Tailoring allowed with justification. Document in Tailored Requirements List (TRL)
- **Always**: Get customer/authority agreement on tailoring before proceeding

### Q4: What if a standard conflicts with another standard?

**A**: 
1. Document the conflict
2. Consult with Certification Lead and customer
3. Obtain authority ruling/interpretation
4. Document resolution
5. Update compliance matrices

## Aircraft Standards (ARP4754A, DO-178C, DO-254, DO-160)

### Q5: Do I need DO-178C for all software?

**A**: Only for **airborne software** (software executing on the aircraft). Ground software (development tools, test equipment, ground stations) does not require DO-178C, but should follow good software engineering practices.

Exception: Tools used to eliminate/reduce/automate verification require DO-330 tool qualification.

### Q6: What's the difference between DAL A and DAL E?

**A**: Development Assurance Level (DAL) based on failure condition severity:
- **DAL A**: Catastrophic (loss of aircraft, multiple fatalities)
- **DAL B**: Hazardous (serious injury, significant distress)
- **DAL C**: Major (discomfort, minor injuries)
- **DAL D**: Minor (inconvenience)
- **DAL E**: No safety effect (no DO-178C/DO-254 required)

DAL determines rigor of development, verification, independence.

### Q7: Can I reuse DO-178B certified software under DO-178C?

**A**: Yes, with caveats:
- Existing software can remain under DO-178B (grandfathering)
- New or significantly changed software should be DO-178C
- See FAA AC 20-115D and EASA guidance for details
- Document approach in PSAC and get authority agreement

### Q8: Do I need DO-254 for all hardware?

**A**: DO-254 is for **complex electronic hardware**:
- **Yes**: FPGA, ASIC, PLD, complex analog/mixed-signal
- **No**: Simple hardware (resistors, capacitors, simple ICs with established reliability data)

Complexity determined by whether design errors could exist that cannot be detected by testing.

### Q9: What DO-160 categories apply to my equipment?

**A**: Depends on:
- **Aircraft Type**: Commercial, regional, helicopter
- **Installation Location**: Flight deck, cabin, avionics bay, external
- **Criticality**: Safety classification

Consult DO-160 and equipment installation specification. Coordinate with aircraft integrator.

### Q10: Can I skip DO-160 Section 22 (Lightning) if my equipment is in a protected location?

**A**: Maybe, but requires justification:
- Some locations less susceptible (shielded avionics bay)
- Must show lightning currents won't reach equipment
- Coordinate with aircraft integrator and certification authority
- Document in DO-160 test plan

## Spacecraft Standards (ECSS)

### Q11: Do I need to follow all ECSS standards?

**A**: ECSS standards are tailorable:
- Identify applicable standards
- Tailor requirements to project (document in TRL)
- Justify tailoring (cost, schedule, applicability)
- Obtain customer agreement on tailoring

### Q12: What's the difference between ECSS-E and ECSS-Q?

**A**:
- **ECSS-E**: Engineering standards (systems, electrical, mechanical, software, etc.)
- **ECSS-Q**: Product Assurance standards (quality, safety, reliability, materials, components)
- **ECSS-M**: Management standards (project management, configuration management)
- **ECSS-S**: Sustainability standards (space debris)

### Q13: How do I handle the ECSS software categories (A, B, C, D)?

**A**: Similar to DO-178C DAL:
- **Category A**: Critical software (loss of spacecraft or mission)
- **Category B**: Essential software (major mission degradation)
- **Category C**: Utility software (minor degradation)
- **Category D**: Support software (no mission impact)

Requirements rigor increases with criticality. Assign category based on failure consequences per ECSS-Q-ST-80C.

### Q14: Do spacecraft need DO-160 testing?

**A**: No, spacecraft use ECSS-E-ST-10-03C environmental testing:
- **Vibration**: Per launch vehicle requirements
- **Thermal Vacuum (TVAC)**: Simulate space environment
- **EMC**: Per ECSS-E-ST-20-07C
- **Radiation**: Per mission environment

DO-160 is for aircraft only.

## Cross-Cutting Standards

### Q15: Do I need MBSE or can I use documents?

**A**: Not mandated by most standards, but:
- **Benefits**: MBSE improves traceability, consistency, reuse
- **Standards**: ISO/IEC/IEEE 15288 supports model-based approach
- **Recommendation**: Use MBSE for complex programs
- **Acceptable**: Document-based for simple programs

Authority cares about meeting requirements, not the tools used.

### Q16: What's the difference between ISO 10007 and EIA-649C for CM?

**A**: Both cover configuration management:
- **ISO 10007**: International standard, broader industry
- **EIA-649C**: U.S. standard, more detailed, aerospace focus
- **Either acceptable**: Choose one and follow it consistently
- **Many programs**: Use ISO 10007 + tailoring from EIA-649C

### Q17: Do I need a digital twin?

**A**: Not required by standards (yet), but:
- **Benefits**: Simulation, optimization, predictive maintenance
- **Standards Emerging**: ISO 23247, AIAA working on aerospace standards
- **Customer Request**: Some customers require digital twin
- **Recommendation**: Consider for complex, long-lifecycle products

### Q18: What's the difference between REACH and RoHS?

**A**:
- **REACH**: Broader chemicals regulation, applies to most products
- **RoHS**: Specific to electrical/electronic equipment (EEE), 10 restricted substances
- **Aerospace Exemption**: RoHS Article 2(4)(c) exempts aerospace, but REACH still applies
- **Practical**: Suppliers may ask for RoHS compliance even if exempt (to simplify their processes)

## Certification and Compliance

### Q19: When should I engage the certification authority?

**A**: **Early and often**:
- **Phase A**: Discuss certification approach, applicable standards
- **PDR**: Present preliminary compliance approach
- **CDR**: Freeze certification basis, submit plans (PSAC, PHAC, etc.)
- **Throughout**: Regular meetings to discuss progress and issues
- **Don't wait**: Last-minute surprises lead to delays and cost

### Q20: What if I find a non-compliance late in the program?

**A**:
1. **Document**: Capture in non-conformance report (NCR)
2. **Assess**: Determine impact (safety, certification, schedule, cost)
3. **Options**:
   - Fix the non-compliance (design change, additional verification)
   - Request deviation/waiver from authority (see 01-REGISTER/DEVIATIONS_WAIVERS.csv)
   - Argue equivalent level of safety (ELOS)
4. **Get Approval**: Authority must approve before proceeding
5. **Lessons Learned**: Prevent recurrence on future projects

### Q21: Can I self-certify or does the authority inspect everything?

**A**: Depends on:
- **Aircraft**: Varies by authority and organization
  - **Part 21 POA**: Production Organization Approval allows self-release of conforming products
  - **Delegation**: Some organizations have Designated Engineering Representatives (DER) who can approve on behalf of FAA
  - **EASA**: Generally more authority involvement
- **Spacecraft**: Typically customer acceptance, not government certification (except export control, launch safety)

---

## Didn't Find Your Answer?

Contact the **Standards Manager** or **Certification Lead**. If the answer is useful to others, we'll add it to this FAQ.

---

**Maintenance**: This FAQ is updated quarterly or when new common questions identified. Suggest additions to Standards Manager.
