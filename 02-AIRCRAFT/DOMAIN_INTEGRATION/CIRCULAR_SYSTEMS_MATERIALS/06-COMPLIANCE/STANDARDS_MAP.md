# Standards Map - Circular Systems Domain

## Overview

This document maps applicable standards to the CIRCULAR_SYSTEMS_MATERIALS domain systems and provides compliance requirements.

## Airworthiness Standards

### CS-25 (EASA) / FAR 25 (FAA)
Certification Specifications and Acceptable Means of Compliance for Large Aeroplanes

| Standard | Title | Applicable to | Compliance Method |
|----------|-------|---------------|-------------------|
| CS-25.831 | Ventilation | ATA-21 | Test + Analysis |
| CS-25.832 | Cabin ozone concentration | ATA-21 | Test |
| CS-25.841 | Pressurized cabins | ATA-21 | Test + Analysis |
| CS-25.863 | Flammable fluid fire protection | ATA-28 | Analysis + Inspection |
| CS-25.981 | Fuel tank ignition prevention | ATA-28 | Analysis + Test |
| CS-25.1447 | Equipment standards for oxygen | ATA-38 (water quality) | Test |

## Environmental Standards

### REACH (Registration, Evaluation, Authorization of Chemicals)
| Requirement | Applicable to | Compliance Method |
|-------------|---------------|-------------------|
| Substance registration | All materials | Material passports (MTL) |
| Authorization for SVHCs | All materials | Supplier certification |
| Restriction compliance | All materials | Design review + Inspection |

### RoHS (Restriction of Hazardous Substances)
| Requirement | Applicable to | Compliance Method |
|-------------|---------------|-------------------|
| Lead-free electronics | ATA-21, ATA-28, ATA-38 controllers | Supplier certification |
| Mercury-free devices | ATA-38 (UV lamps) | Design specification |
| Cadmium-free materials | All systems | Material passports (MTL) |

### WEEE (Waste Electrical and Electronic Equipment)
| Requirement | Applicable to | Compliance Method |
|-------------|---------------|-------------------|
| Design for disassembly | All electronic systems | Design review (MTL) |
| Material recovery targets | All systems | LCA/LCC models (MTL) |
| Recycling documentation | All systems | Material passports (MTL) |

## System Development Standards

### ARP4754A - Development of Civil Aircraft and Systems
| Section | Requirement | Applicable to | Compliance Evidence |
|---------|-------------|---------------|---------------------|
| 5.1 | Requirements capture | All systems | MBSE model, requirements docs |
| 5.2 | System architecture | All systems | Integration views, MBSE |
| 5.3 | Interface management | All systems | Interface matrix, ICDs |
| 5.4 | Verification planning | All systems | VVP plan |

### ARP4761 - Safety Assessment Process
| Section | Requirement | Applicable to | Compliance Evidence |
|---------|-------------|---------------|---------------------|
| 3.2 | Functional Hazard Assessment | All systems | FHA documents |
| 3.3 | Preliminary System Safety Assessment | Critical systems | PSSA documents |
| 3.4 | System Safety Assessment | All systems | SSA documents |
| 3.5 | Common Cause Analysis | All systems | CCA documents |

## Environmental Testing

### DO-160 - Environmental Conditions and Test Procedures for Airborne Equipment
| Category | Test | Applicable to | Compliance Evidence |
|----------|------|---------------|---------------------|
| Section 4 | Temperature and altitude | All LRUs | Test reports |
| Section 5 | Temperature variation | All LRUs | Test reports |
| Section 8 | Vibration | All LRUs | Test reports |
| Section 10 | Operational shocks | All LRUs | Test reports |
| Section 16 | Power input | All electrical LRUs | Test reports |
| Section 21 | Emission of RF energy | All LRUs | Test reports |

## Software Standards

### DO-178C - Software Considerations in Airborne Systems and Equipment Certification
| Level | Applicable to | Objectives | Compliance Evidence |
|-------|---------------|------------|---------------------|
| DAL B | ATA-28 BOP Controller | High-level requirements through testing | Software docs, test results |
| DAL C | ATA-21 Controllers | High-level requirements through testing | Software docs, test results |
| DAL D | ATA-38 Water Controller | High-level requirements verification | Software docs, test results |

## Hydrogen-Specific Standards

### ISO 16901 - Gaseous hydrogen - Land vehicles - Fuel system
| Section | Requirement | Applicable to | Compliance Evidence |
|---------|-------------|---------------|---------------------|
| 5 | General requirements | ATA-28 H₂ system | Design docs, analysis |
| 6 | Container requirements | ATA-28 LH₂ tank | Test reports, certification |
| 7 | Pressure relief devices | ATA-28 valves | Test reports |
| 8 | Leak tightness | ATA-28 all components | Test reports |

### SAE J2579 - Hydrogen fuel systems safety
| Section | Requirement | Applicable to | Compliance Evidence |
|---------|-------------|---------------|---------------------|
| 4 | System design | ATA-28 H₂ system | Design review, FHA |
| 5 | Leak prevention | ATA-28 all components | Analysis, test reports |
| 6 | Ventilation | ATA-28 compartments | Analysis, test reports |
| 7 | Fire detection | ATA-28 compartments | Test reports |

## Water Quality Standards

### WHO - Guidelines for Drinking-water Quality
| Parameter | Limit | Applicable to | Compliance Method |
|-----------|-------|---------------|-------------------|
| Turbidity | < 5 NTU | ATA-38 potable water | Continuous monitoring |
| pH | 6.5 - 8.5 | ATA-38 potable water | Continuous monitoring |
| Coliform bacteria | 0 CFU/100mL | ATA-38 potable water | Periodic sampling |

### NSF/ANSI 55 - Ultraviolet Microbiological Water Treatment Systems
| Requirement | Applicable to | Compliance Evidence |
|-------------|---------------|---------------------|
| UV dose > 40 mJ/cm² | ATA-38 UV sterilizer | Component certification |
| Intensity monitoring | ATA-38 UV sterilizer | Continuous monitoring |

## Lifecycle Assessment Standards

### ISO 14040/14044 - Life Cycle Assessment
| Section | Requirement | Applicable to | Compliance Evidence |
|---------|-------------|---------------|---------------------|
| Goal and scope definition | LCA studies | MTL LCA models | LCA reports |
| Inventory analysis | LCA studies | MTL LCA models | Material data |
| Impact assessment | LCA studies | MTL LCA models | Impact results |
| Interpretation | LCA studies | MTL LCA models | LCA reports |

### ISO 14067 - Carbon footprint of products
| Requirement | Applicable to | Compliance Evidence |
|-------------|---------------|---------------------|
| Carbon footprint calculation | All systems | MTL LCC models |
| Reporting requirements | All systems | LCA reports |

## Material Identification Standards

### ISO 11469 - Marking of plastics products for identification
| Requirement | Applicable to | Compliance Evidence |
|-------------|---------------|---------------------|
| Material marking | All plastic components | Design specification |
| Marking location | All plastic components | Design drawings |

### ISO 1043 - Symbols and abbreviated terms
| Requirement | Applicable to | Compliance Evidence |
|-------------|---------------|---------------------|
| Polymer abbreviations | All plastic components | Material passports |
| Additive abbreviations | All plastic components | Material passports |

## Compliance Matrix Summary

| System | Critical Standards | Compliance Status |
|--------|-------------------|-------------------|
| ATA-21 Air Conditioning | CS-25.831, CS-25.841, DO-160, DO-178C | In progress |
| ATA-28 Fuel/H₂ | CS-25.863, CS-25.981, ISO 16901, SAE J2579, DO-160, DO-178C | In progress |
| ATA-38 Water/Waste | FAR 25.1447, WHO, NSF/ANSI 55, DO-160, DO-178C | In progress |
| MTL-CIRCULARITY | REACH, RoHS, WEEE, ISO 14040/14044, ISO 14067, ISO 11469 | In progress |

## References

- [EVIDENCE_LINKS.md](EVIDENCE_LINKS.md) - Links to compliance evidence
- [00-PROGRAM/CONFIG_MGMT/07-RELEASES/](../../../00-PROGRAM/CONFIG_MGMT/07-RELEASES/) - Release baselines with compliance packages
- [00-README.md](../00-README.md) - Domain overview

## Revision History

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2024-12-XX | Domain Integration Team | Initial standards map |
