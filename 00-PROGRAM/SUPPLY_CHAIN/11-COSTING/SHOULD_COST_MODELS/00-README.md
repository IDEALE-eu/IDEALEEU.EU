# Should-Cost Models

## Overview

Should-cost modeling estimates the theoretical cost to produce an item based on analysis of materials, labor, overhead, and profit.

## Should-Cost Components

### 1. Direct Material Costs
**Raw Materials:**
- Material type and specification
- Material quantity (with scrap factor)
- Material unit cost (market price)
- Material yield and waste

**Purchased Components:**
- Off-the-shelf parts and sub-assemblies
- Market pricing or supplier quotes
- Volume discounts

### 2. Direct Labor Costs
**Manufacturing Labor:**
- Operations and process steps
- Standard hours per operation
- Labor rate by skill level
- Learning curve (for new products)

**Assembly Labor:**
- Assembly sequence and time
- Skilled vs. semi-skilled requirements
- Testing and inspection labor

### 3. Manufacturing Overhead
**Variable Overhead:**
- Utilities, consumables, supplies
- Tooling amortization
- Scrap and rework allowance

**Fixed Overhead:**
- Facility costs (rent, depreciation)
- Supervision and support labor
- Quality assurance
- Maintenance
- Applied as overhead rate (% of direct labor or cost driver)

### 4. Engineering and NRE (Non-Recurring Engineering)
**Development Costs:**
- Engineering design hours
- Prototyping and testing
- Qualification and certification
- Amortization over production quantity

**Tooling:**
- Tool design and fabrication
- Fixtures and test equipment
- Amortization period or per-unit cost

### 5. General and Administrative (G&A)
**Corporate Overhead:**
- Management and administration
- Sales and marketing
- Finance and legal
- IT and facilities
- Applied as percentage of cost base (typically 10-25%)

### 6. Profit Margin
**Target Margin:**
- Industry standard margins
- Supplier financial requirements
- Competitive positioning
- Risk and complexity factors
- Typical: 10-20% for production, 15-30% for development

## Should-Cost Methodology

### Step 1: Define Scope
- Part or assembly to be analyzed
- Production quantity assumptions
- Time period (current or future)
- Level of detail (rough order of magnitude vs. detailed)

### Step 2: Gather Data
- Technical drawings and specifications
- Bill of materials (BOM)
- Process routing and cycle times
- Material prices (market data or quotes)
- Labor rates (by geography and skill)
- Overhead rates (industry benchmarks or supplier data)

### Step 3: Build Model
- Spreadsheet or specialized software
- Calculate direct material costs
- Calculate direct labor costs (operation by operation)
- Apply overhead rates
- Add G&A and profit
- Summarize total cost

### Step 4: Validate
- Compare to supplier quote or current pricing
- Sensitivity analysis (key cost drivers)
- Sanity check with subject matter experts
- Review assumptions and adjust if needed

### Step 5: Use in Negotiation
- Identify cost gaps and opportunities
- Focus negotiation on specific elements
- Challenge supplier's costs with data
- Collaborate on cost reduction opportunities

## Example Should-Cost Structure

```
Part: Titanium Bracket
Quantity: 1,000 units/year

Direct Material:
  Titanium sheet (2 kg @ $35/kg)                     $70.00
  Fasteners and hardware                              $8.00
Direct Material Total                                $78.00

Direct Labor:
  Cutting (0.5 hr @ $25/hr)                          $12.50
  Forming (0.3 hr @ $30/hr)                           $9.00
  Machining (0.4 hr @ $35/hr)                        $14.00
  Inspection (0.1 hr @ $28/hr)                        $2.80
Direct Labor Total                                   $38.30

Manufacturing Overhead (150% of direct labor)        $57.45

Subtotal (Direct Material + Labor + Overhead)       $173.75

G&A (15% of subtotal)                                $26.06

Engineering NRE (amortized)                          $10.00

Total Cost                                          $209.81

Profit (15%)                                         $31.47

Target Price                                        $241.28
```

## Cost Drivers Analysis

### Material Cost Drivers
- Material specification (can lower grade be used?)
- Material form (bar, sheet, forging - which is most efficient?)
- Scrap rate (can design reduce waste?)
- Volume leverage (higher quantities = lower unit cost)

### Labor Cost Drivers
- Process selection (machining vs. forming vs. additive manufacturing)
- Automation opportunities
- Cycle time reduction
- Geographic location (labor rates vary)
- Learning curve and volume

### Overhead Cost Drivers
- Facility utilization (fixed costs spread over more units)
- Capacity investment (depreciation and amortization)
- Quality costs (high reject rate increases overhead)

## Applications

### Sourcing and RFQ
- Set target prices for RFQs
- Evaluate reasonableness of quotes
- Identify suppliers significantly out of line
- Focus negotiation discussions

### Make vs. Buy
- Compare internal manufacturing cost to supplier quotes
- Inform strategic sourcing decisions
- Identify when outsourcing is cost-effective

### Cost Reduction Projects
- Identify highest cost contributors
- Prioritize improvement efforts
- Quantify savings opportunities
- Design changes, process improvements, material substitution

### Supplier Negotiations
- Data-driven negotiation approach
- Challenge cost elements with facts
- Collaborative cost reduction dialogue
- Long-term pricing discussions

## Tools and Resources

### Software Options
- Excel with custom templates (most common)
- aPriori (automated should-cost software)
- CostTrack
- Seer Manufacturing

### Data Sources
- Material price indices (CRU, Platts, MEPS)
- Labor rate surveys
- Industry benchmarking studies
- Supplier cost breakdowns (when available)
- Internal historical data

## Best Practices

### Accuracy and Detail
- Level of detail appropriate for decision importance
- Validate assumptions with subject matter experts
- Update models with actual data when available
- Sensitivity analysis on key assumptions

### Collaboration
- Involve engineering, manufacturing, quality in model development
- Share models with suppliers (selective, in partnership approach)
- Joint cost reduction workshops using should-cost analysis

### Continuous Improvement
- Refine models over time with experience
- Build library of cost models for reference
- Learn from variances between modeled and actual costs
- Incorporate new processes and technologies

### Ethical Use
- Should-cost is an estimate, not absolute truth
- Respect supplier proprietary information
- Use as negotiation tool, not bludgeon
- Fair profit for supplier is important for long-term partnership
