# SUMMARY — BOM Summary Reports

## Purpose

This directory contains summary reports providing high-level BOM analysis, statistics, and key metrics for management review and decision-making.

## Report Types

### Mass Rollup Reports
- Assembly total mass
- Mass by subsystem
- Mass distribution analysis
- Center of gravity calculations
- Mass budget tracking

### Cost Summary Reports
- Total assembly cost estimate
- Cost by subsystem
- Make vs. Buy cost breakdown
- Material cost analysis
- Supplier cost distribution

### Part Count Reports
- Total part count
- Unique part count
- Parts by category
- Make vs. Buy distribution
- Common parts analysis

### Material Summary Reports
- Material types and quantities
- Material cost breakdown
- Material supplier analysis
- Material certifications required
- Special material handling

### Supplier Summary Reports
- Supplier count and distribution
- Parts by supplier
- Supplier criticality analysis
- Lead time summary
- Supplier quality metrics

## File Naming Convention

```
53-10_SUM_<summary-type>_<revision>_<date>.<ext>
```

Examples:
- `53-10_SUM_MASS-ROLLUP_r002_20240315.pdf`
- `53-10_SUM_COST-ESTIMATE_r002_20240315.xlsx`
- `53-10_SUM_PART-COUNT_r002_20240315.pdf`
- `53-10_SUM_SUPPLIER-LIST_r002_20240320.xlsx`

## Report Content

### Executive Summary
- Key metrics at a glance
- Significant findings
- Trends and observations
- Recommendations

### Detailed Analysis
- Breakdown by category
- Comparative analysis
- Historical trends
- Variance from targets

### Supporting Data
- Source BOM references
- Calculation methodology
- Assumptions and exclusions
- Data quality notes

## Mass Rollup Report

### Standard Sections
1. **Total Mass**: Assembly and sub-assemblies
2. **Mass Distribution**: By subsystem and component type
3. **Mass Budget**: Target vs. actual comparison
4. **Critical Items**: Heaviest components
5. **Trends**: Mass evolution over revisions

### Metrics to Include
- Total assembly mass
- Sub-assembly masses
- Component masses
- Percentage distribution
- Mass growth tracking
- Center of gravity

## Cost Summary Report

### Standard Sections
1. **Total Cost**: Assembly cost estimate
2. **Cost Breakdown**: By subsystem and category
3. **Make vs. Buy**: Manufacturing vs. procurement
4. **Material Costs**: Raw material expenses
5. **Trends**: Cost evolution

### Metrics to Include
- Total estimated cost
- Recurring costs
- Non-recurring costs
- Material costs
- Labor costs
- Tooling costs

## Part Count Report

### Standard Sections
1. **Part Counts**: Total and unique parts
2. **Category Breakdown**: Parts by type
3. **Commonality**: Shared parts analysis
4. **Complexity**: Assembly complexity metrics

### Metrics to Include
- Total part count
- Unique part count
- Parts per assembly
- Common parts percentage
- Standard vs. custom parts

## Usage

Summary reports are used for:
- Program management reviews
- Design review presentations
- Cost review meetings
- Supplier negotiations
- Customer reporting
- Regulatory submissions

## Update Frequency

Reports should be generated:
- At each major BOM revision
- Before design reviews
- Monthly for active programs
- On-demand for special needs

## Related Directories

- **Variance**: [../VARIANCE/](../VARIANCE/) — Variance analysis reports
- **Templates**: [../../TEMPLATES/](../../TEMPLATES/) — Report templates
- **Revisions**: [../../REVISIONS/RELEASED/](../../REVISIONS/RELEASED/) — Source BOMs
