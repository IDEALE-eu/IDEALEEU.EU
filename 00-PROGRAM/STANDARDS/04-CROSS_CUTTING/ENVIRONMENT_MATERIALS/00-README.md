# ENVIRONMENT_MATERIALS

Environmental compliance and materials standards.

## Overview

This directory contains standards for environmental compliance (REACH, RoHS) and aerospace materials specifications (ASTM, AMS, etc.).

## Applicable Standards

### REACH - Registration, Evaluation, Authorization and Restriction of Chemicals (EU)
- **Regulation**: EC 1907/2006
- **Scope**: Chemical substances manufactured or imported into EU
- **Purpose**: Protect human health and environment from hazardous chemicals
- **Requirements**: Registration, safety data sheets, restrictions on certain substances

### RoHS - Restriction of Hazardous Substances (EU)
- **Directive**: 2011/65/EU (RoHS 2), amended by 2015/863 (RoHS 3)
- **Scope**: Electrical and electronic equipment (EEE)
- **Restricted Substances**: Lead, mercury, cadmium, hexavalent chromium, PBB, PBDE, DEHP, BBP, DBP, DIBP
- **Exemptions**: Aerospace and defense equipment (Article 2(4)(c))

### ISO 14001 - Environmental Management Systems
- **Scope**: EMS framework and requirements
- **Coverage**: Environmental policy, planning, implementation, checking, review
- **Benefits**: Reduce environmental impact, improve compliance, cost savings

### ASTM Standards - American Society for Testing and Materials
- **Scope**: Material specifications, test methods, practices
- **Examples**:
  - **ASTM E8**: Tensile testing of metallic materials
  - **ASTM E595**: Outgassing test for space materials
  - **ASTM D3359**: Adhesion testing of coatings
- **Applicability**: All materials used in aerospace

### AMS (SAE Aerospace Material Specifications)
- **Scope**: Material and process specifications for aerospace
- **Examples**:
  - **AMS 4911**: Titanium alloy (Ti-6Al-4V) sheet/plate
  - **AMS 5659**: Stainless steel (17-4 PH) bars/forgings
  - **AMS 2700**: Passivation of stainless steel
- **Use**: Specify materials in drawings and BOMs

## REACH Compliance

### Substances of Very High Concern (SVHC)
- **Candidate List**: ~230 substances (growing)
- **Authorization List (Annex XIV)**: Restricted unless authorized
- **Restriction List (Annex XVII)**: Prohibited or limited use
- **Examples**: Certain phthalates, chromium compounds, lead compounds

### REACH Requirements
- **Registration**: Manufacturers/importers register substances > 1 ton/year
- **Communication**: Notify customers if articles contain SVHC > 0.1% w/w
- **Authorization**: Apply for authorization if substance on Annex XIV
- **Restriction**: Comply with restrictions in Annex XVII

### REACH in Aerospace
- Aerospace generally not exempt (unlike RoHS)
- Must comply with SVHC communication and restrictions
- Challenge: Long product lifecycles, legacy designs

## RoHS Compliance

### Restricted Substances (RoHS 3)
- **Lead (Pb)**: < 0.1% by weight
- **Mercury (Hg)**: < 0.1% by weight
- **Cadmium (Cd)**: < 0.01% by weight
- **Hexavalent Chromium (Cr6+)**: < 0.1% by weight
- **Polybrominated Biphenyls (PBB)**: < 0.1% by weight
- **Polybrominated Diphenyl Ethers (PBDE)**: < 0.1% by weight
- **Bis(2-ethylhexyl) Phthalate (DEHP)**: < 0.1% by weight
- **Butyl Benzyl Phthalate (BBP)**: < 0.1% by weight
- **Dibutyl Phthalate (DBP)**: < 0.1% by weight
- **Diisobutyl Phthalate (DIBP)**: < 0.1% by weight

### RoHS Exemption for Aerospace
- **Article 2(4)(c)**: Equipment designed for use in air or space
- **Interpretation**: Aircraft and spacecraft generally exempt
- **Caution**: Ground equipment, test equipment may not be exempt
- **Supply Chain**: Suppliers may ask for RoHS compliance even if exempt

## Environmental Management (ISO 14001)

### EMS Components
- **Environmental Policy**: Commitment to environmental protection
- **Planning**: Environmental aspects, legal requirements, objectives
- **Implementation**: Resources, competence, communication, documentation, operational control
- **Checking**: Monitoring, corrective actions, audits
- **Management Review**: Top management review of EMS

### Environmental Aspects
- Emissions to air (VOC, CO2, dust)
- Discharges to water (chemicals, wastewater)
- Waste generation (hazardous, non-hazardous)
- Use of resources (energy, water, materials)
- Noise, vibration, odor

### Benefits
- Regulatory compliance
- Reduced environmental impact
- Cost savings (energy, waste)
- Improved reputation
- Competitive advantage (customers require ISO 14001)

## Materials Standards

### ASTM Standards

#### Material Specifications
- **ASTM B21**: Naval brass rod, bar, shapes
- **ASTM B26**: Aluminum alloy sand castings
- **ASTM A564**: Stainless steel bars for aerospace
- **ASTM D3039**: Tensile properties of fiber-resin composites

#### Test Methods
- **ASTM E8/E8M**: Tensile testing of metallic materials
- **ASTM E290**: Bend testing of metallic materials
- **ASTM E595**: Outgassing for spacecraft materials
- **ASTM D3359**: Adhesion testing (cross-cut or tape test)

### AMS Specifications

#### Metals
- **AMS 4911**: Ti-6Al-4V titanium alloy sheet/plate
- **AMS 5662**: Stainless steel (A286) bars/forgings
- **AMS 6414**: 4340 steel (high-strength alloy)
- **AMS 7725**: Aluminum 6061-T6 extrusions

#### Processes
- **AMS 2700**: Passivation of stainless steel
- **AMS 2759**: Heat treatment of steel
- **AMS 2770**: Cadmium plating
- **AMS-QQ-A-250**: Anodizing of aluminum alloys

#### Composites
- **AMS 3819**: Carbon fiber prepreg
- **AMS 3841**: Epoxy resin
- **AMS 3850**: Aramid fiber (Kevlar)

### Material Selection Criteria

- **Mechanical Properties**: Strength, stiffness, fatigue, fracture toughness
- **Physical Properties**: Density, thermal expansion, conductivity
- **Environmental Resistance**: Corrosion, UV, temperature extremes
- **Flammability**: Fire resistance (especially for cabin materials)
- **Outgassing**: Low outgassing for spacecraft (ASTM E595)
- **Cost and Availability**: Balance performance and cost
- **Heritage**: Flight-proven materials preferred

## Outgassing (Spacecraft Materials)

### ASTM E595 Test
- **Conditions**: 24 hours at 125°C in vacuum (10⁻⁵ torr)
- **Measurements**:
  - **Total Mass Loss (TML)**: Mass lost during test
  - **Collected Volatile Condensable Materials (CVCM)**: Condensed on cold plate
- **Acceptance Criteria** (NASA):
  - TML ≤ 1.0%
  - CVCM ≤ 0.1%

### Low-Outgassing Materials
- Select materials meeting ASTM E595
- NASA outgassing database: https://outgassing.nasa.gov
- Test new materials if not in database

## Conflict Minerals

### Dodd-Frank Act Section 1502 (US)
- **Conflict Minerals**: Tin, tantalum, tungsten, gold (3TG)
- **Scope**: Minerals originating from Democratic Republic of Congo (DRC) and adjoining countries
- **Requirement**: Publicly traded companies must report use of conflict minerals
- **Supply Chain**: Suppliers provide Conflict Minerals Reporting Template (CMRT)

### EU Conflict Minerals Regulation
- **Regulation**: EU 2017/821
- **Scope**: Importers of 3TG into EU
- **Due Diligence**: Supply chain due diligence per OECD guidelines

## Key Deliverables

1. **REACH Declaration**: List of articles and SVHC content
2. **RoHS Declaration**: Compliance statement (or exemption claim)
3. **ISO 14001 Certification**: EMS certificate (if pursuing)
4. **Material Specifications**: BOMs referencing ASTM/AMS specs
5. **Material Test Reports**: Certification of material properties
6. **Outgassing Test Data**: ASTM E595 results for spacecraft materials
7. **Conflict Minerals Report**: CMRT for supply chain

## Compliance Requirements

- REACH compliance for EU market (SVHC communication, restrictions)
- RoHS compliance or exemption justification
- ISO 14001 certification (optional, but beneficial)
- Materials per ASTM/AMS specifications
- Outgassing per ASTM E595 for spacecraft
- Conflict minerals due diligence

## Integration with Other Standards

### Aircraft
- Materials per AMS specifications
- Flammability per FAA/EASA requirements
- Environmental impact considered in design

### Spacecraft
- Outgassing per ASTM E595 and ECSS-Q-ST-70C
- Materials qualification per ECSS
- Environmental disposal per IADC guidelines

## Best Practices

- Maintain approved materials list (AML)
- Monitor REACH/RoHS updates (new substances, exemptions)
- Test materials early (outgassing, flammability)
- Use flight-proven materials when possible
- Engage suppliers on compliance (REACH, RoHS, conflict minerals)
- Consider lifecycle environmental impact (design for recycling)

## Common Pitfalls

- Late discovery of non-compliant materials (redesign required)
- Supplier non-compliance (supply chain disruption)
- Inadequate outgassing data (launch delays)
- Exemption misunderstood (RoHS not applicable but supplier asks for compliance)
- Legacy designs with restricted substances

## References

- REACH Regulation: https://echa.europa.eu/regulations/reach
- RoHS Directive: https://ec.europa.eu/environment/topics/waste-and-recycling/rohs-directive_en
- ISO 14001 (purchase from ISO)
- ASTM standards: https://www.astm.org
- AMS standards (purchase from SAE)
- NASA outgassing database: https://outgassing.nasa.gov
- CMRT template: https://www.responsiblemineralsinitiative.org/

---

**Status**: Configuration-controlled per 00-PROGRAM/CONFIG_MGMT/
