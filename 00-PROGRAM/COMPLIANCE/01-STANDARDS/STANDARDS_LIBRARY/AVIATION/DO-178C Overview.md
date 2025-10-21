# DO-178C Overview

DO-178C is the primary standard for planning, developing, verifying, and certifying airborne software.

## Software Levels
- **Level A**: Catastrophic failure; 71 objectives; highest rigor.
- **Level B**: Hazardous; significant oversight.
- **Level C**: Major; moderate oversight.
- **Level D**: Minor; minimal oversight.
- **Level E**: No effect; least oversight.

## Lifecycle Data Requirements
- **Planning**: Plan for Software Aspects of Certification (PSAC)
- **Development**: Software Requirements Specification (SRS), Software Design Description (SDD), source code
- **Verification**: Test cases, test results, structural coverage analysis
- **Configuration Management**: Records and baselines
- **Quality Assurance**: Audit and compliance records

## Verification Independence & Coverage
- **Level A/B**: Requires Modified Condition/Decision Coverage (MC/DC)
- **Level C**: Requires Decision Coverage
- **Levels D/E**: Reviews only (no structural coverage required)
- Independence required for verification activities increases with criticality level

## Supplements
- **DO-330**: Tool qualification
- **DO-331**: Model-based development
- **DO-332**: Object-oriented technology
- **DO-333**: Formal methods
