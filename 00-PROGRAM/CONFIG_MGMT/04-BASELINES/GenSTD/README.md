# GenSTD – Generalized Standardization Directive

## Overview

**GenSTD** is the formal consolidation framework that converts dynamic OtC (Open to Change) reproducible baselines into governed, compliance-ready, auditable standards.

## Purpose

GenSTD provides the stabilization and dissemination layer built on the OtC foundation:
- Converts prototype baselines into canonical standards
- Provides CM-compliant, policy-driven baselines with embedded OtC logic
- Ensures regulatory and compliance alignment
- Maintains full provenance from OtC source

## Policy Statement

> **OtC remains the generative layer. GenSTD is the stabilization and dissemination layer. Compliance derives from GenSTD, adaptability from OtC.**

## Hierarchy

| Tier | Description | Location |
|------|-------------|----------|
| **OtC-α→β→γ→δ→Ω** | Prototype flow (creative, adaptive, open) | Pre-GenSTD development |
| **GenSTD-I** | Frozen OtC snapshot validated by CAB | [I_core/](./I_core/) |
| **GenSTD-II** | Multi-domain standard (CM + QA + Security) | [II_multidomain/](./II_multidomain/) |
| **GenSTD-III** | Regulatory and compliance-aligned reference baseline | [III_regulatory/](./III_regulatory/) |
| **GenSTD-IV** | Industry-wide harmonized standard under CSDB control | [IV_harmonized/](./IV_harmonized/) |

## Conversion Rule

```
OtC[x] + CAB approval + CSA trace → GenSTD[y]
```

Each GenSTD entry inherits provenance metadata from its OtC source:
- Hash (SHA-256)
- Manifest
- RFC ID
- Audit references
- CAB approval date and minutes

## EHC Compliance

**Embedded in Human Comprehensivity (EHC)** is mandatory for all GenSTD artifacts.

### EHC Requirements

Every GenSTD baseline must be understandable by a qualified human without toolchains or insider context:

1. **Plain-language summary** ≤150 words answering: what, why, impact, risk
2. **One diagram** explaining flow or structure
3. **Glossary links** resolve all non-common acronyms on first use
4. **Decision log** lists alternatives rejected and reasoning
5. **Reproduction steps** run from clean machine in ≤15 minutes
6. **Readability target**: CEFR B2–C1 or Flesch-Kincaid 10–12

### Required Artifacts per Baseline

Each GenSTD baseline must include:

- **`SUMMARY.md`** - Executive 150-word brief
- **`DECISIONS.md`** - ADR bullets, timestamps, owners
- **`GLOSSARY.md`** - Local terms mapped to Org Glossary
- **`RUNBOOK.md`** - Setup, run, rollback, verification
- **`DIAGRAM.(png|svg)`** - Single-page system view
- **`MANIFEST.json`** - Provenance metadata (see schema)
- **`RISKS.md`** - Top 5 risks, mitigations, residual

### Policy Line

> **EHC is mandatory. No GenSTD artifact passes without a self-contained summary, glossary resolution, runnable steps, and a single explanatory diagram.**

## Templates

Standard templates for GenSTD baselines are available in [TEMPLATES/](./TEMPLATES/):

- **[MANIFEST.schema.json](./TEMPLATES/MANIFEST.schema.json)** - JSON schema for GenSTD manifests
- **[MANIFEST.example.json](./TEMPLATES/MANIFEST.example.json)** - Example manifest
- **[SUMMARY.md](./TEMPLATES/SUMMARY.md)** - Summary template
- **[DECISIONS.md](./TEMPLATES/DECISIONS.md)** - Decision log template
- **[GLOSSARY.md](./TEMPLATES/GLOSSARY.md)** - Local glossary template
- **[RUNBOOK.md](./TEMPLATES/RUNBOOK.md)** - Runbook template
- **[RISKS.md](./TEMPLATES/RISKS.md)** - Risk assessment template

## Validation

GenSTD baselines must pass EHC validation before approval. See [TEMPLATES/validate_ehc.py](./TEMPLATES/validate_ehc.py) for the validation script.

### Verification Checklist (Gate in CI)

- [ ] Lint docs: headings present, word count ≤150 in `SUMMARY.md`
- [ ] Spellcheck + acronym resolver against Org Glossary
- [ ] Diagram file exists and is referenced in `SUMMARY.md`
- [ ] `RUNBOOK.md` verified by scripted dry-run
- [ ] `MANIFEST.json` schema-valid and cross-links resolve
- [ ] Readability score within target (FK 10–12)

## Usage

### Creating a New GenSTD Baseline

1. **Select OtC source**: Identify the OtC baseline to convert
2. **Copy templates**: Use templates from [TEMPLATES/](./TEMPLATES/)
3. **Complete all required artifacts**:
   - Write 150-word `SUMMARY.md`
   - Document decisions in `DECISIONS.md`
   - Create local `GLOSSARY.md` mapping to org terms
   - Write executable `RUNBOOK.md`
   - Create single-page `DIAGRAM.svg` or `DIAGRAM.png`
   - Fill out `MANIFEST.json` with full provenance
   - Document top 5 risks in `RISKS.md`
4. **Validate**: Run `validate_ehc.py` to check compliance
5. **Submit for CAB approval**: Include all artifacts
6. **Place in appropriate tier**: I, II, III, or IV based on maturity

### Validation Command

```bash
python TEMPLATES/validate_ehc.py path/to/baseline/
```

## Directory Structure

```
GenSTD/
├── README.md                 # This file
├── I_core/                   # GenSTD-I: Frozen OtC snapshots
│   └── [baseline-dirs]/
├── II_multidomain/           # GenSTD-II: Multi-domain standards
│   └── [baseline-dirs]/
├── III_regulatory/           # GenSTD-III: Regulatory baselines
│   └── [baseline-dirs]/
├── IV_harmonized/            # GenSTD-IV: Industry-wide standards
│   └── [baseline-dirs]/
└── TEMPLATES/                # Templates and validation tools
    ├── MANIFEST.schema.json
    ├── MANIFEST.example.json
    ├── SUMMARY.md
    ├── DECISIONS.md
    ├── GLOSSARY.md
    ├── RUNBOOK.md
    ├── RISKS.md
    └── validate_ehc.py
```

## Integration with Configuration Management

GenSTD baselines integrate with the broader CM process:

- **CCB Approval**: Required for all GenSTD-I and above ([../05-CCB/](../05-CCB/))
- **Change Management**: Changes to GenSTD baselines via ECR/ECO ([../06-CHANGES/](../06-CHANGES/))
- **Traceability**: MANIFEST.json links to UTCS ([../10-TRACEABILITY/](../10-TRACEABILITY/))
- **Audit Trail**: CSA records maintained ([../11-AUDITS/](../11-AUDITS/))
- **Release Process**: GenSTD baselines tagged and released ([../07-RELEASES/](../07-RELEASES/))

## References

- **OtC Methodology**: See program governance documentation
- **CAB Process**: [../05-CCB/README.md](../05-CCB/README.md)
- **Change Management**: [../06-CHANGES/00-README.md](../06-CHANGES/00-README.md)
- **Org Glossary**: [/docs/glossary.md](/docs/glossary.md)
- **EHC Specification**: This document, EHC Compliance section

---

*Last Updated: 2025-10-15 | Version: 1.0*
