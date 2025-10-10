# TABLES — Result Tables and Summaries

## Purpose
Tabulated analysis results, summary statistics, and performance metrics for reporting and verification.

## Contents
- Temperature summary tables
- Stress and margin of safety tables
- Heat flow and power budgets
- Performance metrics and KPIs
- Comparison and delta tables
- Requirement verification matrices

## File Organization
- One file per analysis case or summary
- Include table metadata (case, date, units)
- Store both raw and formatted versions
- Maintain consistent formatting

## Naming Convention
```
21-10-CAE_table_<case>_<parameter>__r<NN>__<STATUS>.{csv|xlsx}
```

Example: `21-10-CAE_table_thermal_balance_temp_summary__r01__REL.xlsx`

## Table Requirements
- Include column headers with units
- Document case identification
- Show uncertainty or margin
- Include min/max/avg values
- Reference requirement limits
- Add timestamp and revision

## Typical Tables
- **Temperature Summary**: Component temps (min/max/avg)
- **Stress/Margin**: Peak stress, margin of safety
- **Heat Flow**: Power dissipation, radiative exchange
- **Performance**: Heat rejection, pressure drop, efficiency
- **Verification**: Requirement vs analysis result

## Table Format Example
```
Component ID | Location | T_min (°C) | T_max (°C) | T_avg (°C) | Req (°C) | Margin (°C)
-------------|----------|------------|------------|------------|----------|-------------
RAD-001      | Panel 1  | -35.2      | +62.8      | +15.3      | -40/+70  | +4.8/+7.2
LPHX-001     | Core     | +10.5      | +25.3      | +18.2      | +5/+30   | +5.5/+4.7
```

## Format Guidelines
- **CSV**: For data exchange and scripting
- **XLSX**: For formatted reports with multiple sheets
- **Markdown**: For documentation and README files

## Guidelines
- Maintain traceability to analysis case
- Include requirement verification
- Document margin calculation method
- Use consistent units and precision
- Archive with supporting documentation

---

**Last Updated**: 2025-10-10
