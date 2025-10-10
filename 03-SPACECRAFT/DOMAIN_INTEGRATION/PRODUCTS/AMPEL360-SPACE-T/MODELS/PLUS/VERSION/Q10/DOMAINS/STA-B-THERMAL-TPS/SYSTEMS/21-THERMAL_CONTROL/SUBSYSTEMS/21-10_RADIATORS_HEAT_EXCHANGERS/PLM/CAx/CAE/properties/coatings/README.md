# COATINGS — Coating Optical Properties

## Purpose
Surface coating optical and thermal properties for radiative heat transfer analysis.

## Contents
- Solar absorptance α (0.3-2.5 µm)
- Infrared emissivity ε (5-50 µm)
- Temperature dependence α(T), ε(T)
- Angular dependence (if significant)
- Beginning-of-life (BOL) and end-of-life (EOL) values
- Degradation factors

## File Organization
- One file per coating type or product
- Include BOL and EOL data
- Document test data sources
- Store vendor specifications

## Naming Convention
```
21-10-CAE_coatings_<coating_name>__r<NN>__<STATUS>.{csv|xlsx}
```

Example: `21-10-CAE_coatings_white_paint_z93__r01__REL.csv`

## Data Requirements
- Coating identification and manufacturer
- Solar absorptance α (BOL/EOL)
- Infrared emissivity ε (BOL/EOL)
- Temperature range
- Degradation model (UV, particle radiation)
- Test method reference

## Common Coatings
- **White paints**: Z93, YB71, S13GLO
- **Black paints**: Cat-a-lac black, Aeroglaze Z306
- **Silver Teflon**: Ag-FEP
- **Kapton**: Aluminized, black
- **Anodize**: Black, clear
- **Polished metal**: Aluminum, stainless steel

## Property Table Format
```
Coating     | α (BOL) | ε (BOL) | α (EOL) | ε (EOL) | Degradation
------------|---------|---------|---------|---------|-------------
Z93 White   | 0.18    | 0.91    | 0.25    | 0.89    | UV + particle
Black Paint | 0.96    | 0.88    | 0.98    | 0.88    | Minimal
Ag-FEP      | 0.08    | 0.81    | 0.12    | 0.81    | UV + particle
```

## Guidelines
- Reference test data per ASTM E903, E408
- Include mission duration for EOL
- Document environmental exposure
- Maintain traceability to coating batch

---

**Last Updated**: 2025-10-10
