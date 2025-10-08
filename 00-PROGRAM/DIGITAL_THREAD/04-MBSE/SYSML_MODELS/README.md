# SYSML_MODELS

Central SysML model repository or links to external MBSE tools.

## Purpose

This directory contains the SysML models or references to external MBSE tool repositories (Cameo Systems Modeler, Capella, etc.).

## Organization

### Option 1: Centralized File-Based Models
If using file-based SysML tools, models are stored here:
```
SYSML_MODELS/
├─ AIRCRAFT/
│  ├─ SYSTEM_ARCHITECTURE.sysml
│  ├─ AIRFRAMES/
│  ├─ PROPULSION/
│  ├─ AVIONICS/
│  └─ ...
├─ SPACECRAFT/
│  ├─ SYSTEM_ARCHITECTURE.sysml
│  ├─ GNC/
│  ├─ POWER_THERMAL/
│  ├─ PROPULSION/
│  └─ ...
└─ SHARED/
   ├─ COMMON_INTERFACES.sysml
   └─ REUSABLE_COMPONENTS.sysml
```

### Option 2: Links to External Repository
If using centralized MBSE tool (e.g., Cameo Cloud, 3DEXPERIENCE):
- **REPOSITORY_LINKS.md** - URLs and access instructions for external MBSE repositories
- **MODEL_EXPORTS/** - Periodic exports (XMI format) for backup and analysis

## Model Access

### Tool Access
- **Tool**: [Specify tool name and version]
- **Repository URL**: [Provide URL]
- **Authentication**: Role-based access per 09-GOVERNANCE/ACCESS_CONTROL_POLICY.md
- **License**: [License information]

### Export Formats
- **XMI (XML Metadata Interchange)**: For tool interoperability
- **ReqIF**: For requirements interchange
- **SVG/PNG**: Diagram exports for documentation
- **JSON/YAML**: For automated processing

## Version Control

### Model Versioning
- Models follow semantic versioning: MAJOR.MINOR.PATCH
- Version tags aligned with configuration baselines
- Git or tool-native version control

### Branching Strategy
- **main**: Production baseline (PDR, CDR baselines)
- **develop**: Integration branch for ongoing development
- **feature/**: Feature development branches
- **release/**: Release preparation branches

## Quality Assurance

### Model Validation
- Automated syntax checking
- Consistency validation
- Completeness checks
- Requirements allocation verification

### Review Process
- Peer review required for all model changes
- Architecture review for structural changes
- Stakeholder review at major milestones

## Related Documents

- **04-MBSE/00-README.md** - MBSE overview
- **04-MBSE/MODEL_BASELINES/** - Configuration baselines
- **04-MBSE/REQUIREMENTS_ALLOCATION.csv** - Requirements traceability
