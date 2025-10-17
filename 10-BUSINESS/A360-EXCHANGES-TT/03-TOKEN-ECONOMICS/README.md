# Token Economics Configuration

**Version:** 1.0  
**UTCS:** `utcs://BUSINESS/A360-EXCHANGES-TT/TOKEN-ECONOMICS`

## Overview

This directory contains the Teknia Token (TT) economic model configuration for the A360 exchanges platform.

## Token Specification

### Supply
- **Total Supply:** 1,000,000,000 TT (1 billion tokens)
- **Decimals:** 18 (standard ERC-20 compatibility)
- **Symbol:** TT
- **Type:** Utility + Staking

### Distribution

| Allocation | Percentage | Amount (TT) | Lock Period | Purpose |
|------------|-----------|-------------|-------------|---------|
| Ecosystem Reserve | 28% | 280,000,000 | Rolling 2yr | Long-term ecosystem development |
| Risk Fund | 18% | 180,000,000 | 4yr vest | Counterparty default coverage |
| Market Maker Reserve | 14% | 140,000,000 | 1yr | Liquidity provision |
| Incentives Pool | 22% | 220,000,000 | 3yr vest | User rewards and growth |
| Team & Contributors | 18% | 180,000,000 | 4yr vest | Core team + merit-based contribution rewards |

**Team & Contributors Breakdown:**
- 10% (100M TT): Core team fixed allocation (4yr vest)
- 8% (80M TT): Merit-based contribution pool (evaluated quarterly)

## Merit-Based Contribution System

### Overview

The 8% (80M TT) merit-based contribution pool recognizes and rewards team members based on:
- **Effort Dedication**: Time and energy invested in platform development
- **Innovation Quality**: Novel solutions and creative problem-solving
- **Value Creation**: Measurable impact on platform success
- **Decision-Making Fairness**: Equitable and transparent contribution to governance

### Contribution Evaluation Framework

#### Key Performance Indicators (KPIs)

**1. Effort Dedication Metrics (30% weight)**
- Hours committed to project (logged and verified)
- Consistency of participation (attendance, responsiveness)
- Project milestone completion rate
- On-time delivery percentage

**2. Innovation Scoring (35% weight)**
- Novel technical solutions implemented
- Patent-worthy contributions identified
- Process improvements suggested and adopted
- Research and development initiatives led
- Creative problem-solving instances

**3. Value Creation Metrics (25% weight)**
- Code quality and maintainability scores
- User adoption of features developed
- Cost savings achieved through optimization
- Revenue generated from contributions
- Platform stability and performance improvements

**4. Decision-Making Fairness (10% weight)**
- Transparent communication practices
- Collaborative approach in team decisions
- Equitable treatment of all stakeholders
- Ethical considerations in technical choices
- Conflict resolution effectiveness

### Evaluation Process

**Quarterly Assessment:**
1. **Self-reporting**: Team members log contributions with evidence
2. **Peer review**: Anonymous peer evaluation (20% of score)
3. **Technical Council review**: Expert assessment (40% of score)
4. **Strategic Board approval**: Final validation (40% of score)

**Scoring System:**
- Each contributor receives a score: 0-100 points per quarter
- Total pool distributed proportionally to scores
- Minimum threshold: 60 points to qualify for distribution
- Top 10% contributors receive 1.5x multiplier bonus

**Distribution Schedule:**
- Quarterly evaluation: March, June, September, December
- Distribution: Within 30 days of evaluation completion
- Vesting: 25% immediate, 75% over 12 months (quarterly)

### Innovation Bonus Pool

**Additional Incentive:** 10M TT from merit pool reserved for exceptional innovations:

**Criteria for Innovation Bonus:**
- **Game-changing feature**: Significant competitive advantage (5M TT)
- **Patent filed**: Intellectual property creation (2M TT)
- **Major efficiency gain**: >30% cost or time reduction (1M TT)
- **Industry recognition**: Award or publication (1M TT)
- **Security enhancement**: Critical vulnerability prevention (1M TT)

**Payout Structure:**
- 50% immediate upon validation
- 50% vested over 24 months

### Fairness Mechanisms

**Transparency Requirements:**
- All evaluation criteria published in advance
- Scores and rationale shared with contributors
- Appeals process available (15-day window)
- Public dashboard showing aggregate statistics

**Anti-Bias Measures:**
- Anonymous peer review component
- Multiple evaluator perspectives
- Regular audits of evaluation fairness
- Diversity and inclusion metrics tracked

**Conflict Resolution:**
- Dedicated ombudsperson role
- Independent review panel for disputes
- Binding arbitration as final resort

### Fixed Effort Guarantees

**Base Allocation (from 10% core team pool):**
- Full-time contributors: Minimum 2M TT over 4 years (guaranteed)
- Part-time contributors: Prorated based on commitment level
- Contractors: Project-based allocation with clear milestones

**Additional Merit-Based (from 8% merit pool):**
- Variable based on quarterly performance
- No guaranteed minimum from merit pool
- Opportunity to earn 2-5x base allocation for top performers

## Fee Structure

### Trading Fees (Pre-Discount)

| Role | Base Fee | With TT Stake | Discount |
|------|----------|---------------|----------|
| Maker | 0.10% | 0.05% | 50% with ≥X TT |
| Taker | 0.30% | 0.24% | 20% with ≥Y TT |

**Stake Requirements:**
- X = 10,000 TT for maker discount
- Y = 5,000 TT for taker discount

### Service Fees

| Service | Base Fee | Notes |
|---------|----------|-------|
| Lease Origination | 0.5-1.0% | Based on lease term |
| DPP Mint | €0.10 + 0.05 TT | Per passport |
| DPP Attestation | 0.10 TT | Per attestation |
| Repair Escrow | 1.5% | Capped at €500 |

## Staking Models

### Market Maker Staking

**Purpose:** Provide liquidity and earn trading fees

**Parameters:**
- Minimum stake: 50,000 TT
- Lock period: 90 days
- Reward rate: 30% of trading fees proportional to stake
- Unstaking cooldown: 7 days

**Slashing Conditions:**
- Withdrawal of liquidity during high volatility: 5% slash
- Order book manipulation: 25% slash
- Front-running: 50% slash

### Service Provider Staking

**Purpose:** Guarantee service quality and earn service fees

**Parameters:**
- Minimum stake: 25,000 TT
- Lock period: 180 days
- Reward rate: Service fees based on volume
- Reputation boost: Higher stake = better visibility

**Slashing Conditions:**
- SLA breach (minor): 2% slash per incident
- SLA breach (major): 10% slash per incident
- Warranty fraud: 50% slash
- Non-delivery: 30% slash

### Oracle Staking

**Purpose:** Provide attestations and test results

**Parameters:**
- Minimum stake: 100,000 TT
- Lock period: 365 days
- Reward rate: 0.10 TT per attestation
- Appeal period: 30 days

**Slashing Conditions:**
- False attestation: 100% slash
- Data manipulation: 75% slash
- Delayed reporting: 5% slash per occurrence

## Collateral Haircuts

When using TT as collateral for leases:

| TT Amount | EUR Equivalent | Haircut | Effective Value |
|-----------|---------------|---------|-----------------|
| 10,000 TT | €10,000 | 20% | €8,000 |
| 50,000 TT | €50,000 | 15% | €42,500 |
| 100,000+ TT | €100,000+ | 10% | €90,000+ |

**Note:** EUR equivalent based on 7-day moving average price

## Risk Fund Management

### Capitalization
- Initial: 200,000,000 TT + €10,000,000 EUR
- Target: 25% of total market value
- Minimum: 15% of total market value

### Usage Priority
1. Counterparty default coverage
2. Warranty shortfalls
3. Force majeure events
4. System security incidents

### Replenishment
- Fee skim: 10% of all platform fees
- Slashing proceeds: 100% to risk fund
- Emergency assessment: Up to 0.5% of active stakes

## Token Velocity Management

**Target Velocity:** 4-6 transactions per token per quarter

**Mechanisms:**
- Staking incentives (reduce velocity)
- Fee discounts (increase velocity)
- Lock-up periods (reduce velocity)
- Liquidity mining (increase velocity)

## Governance Parameters

### Proposal Thresholds
- **Initiation:** 1,000,000 TT (0.1% of supply)
- **Quorum:** 40,000,000 TT (4% of supply)
- **Approval:** 60% of votes cast

### Voting Power
- 1 TT = 1 vote
- Staked tokens: 1.5x voting power
- Lock-up ≥1 year: 2x voting power

### Timelock
- Standard proposals: 7-day discussion + 3-day vote + 2-day timelock
- Emergency proposals: 24-hour fast track (requires 75% approval)

## Economic Security

### Attack Cost Analysis

| Attack Vector | Required Stake | Expected Loss | ROI for Attacker |
|--------------|----------------|---------------|------------------|
| 51% voting attack | 500M TT | Complete stake | Negative |
| Market manipulation | 150M TT | 50% slash | Negative |
| Oracle collusion | 300M TT | 100% slash | Negative |

### Circuit Breakers
- Trading halt: >20% price movement in 1 hour
- Withdrawal limit: 10% of pool per 24h
- Emergency pause: Governance multi-sig (3/5)

## Integration with Existing Systems

### Finance Module
- Links to `finance/teknia_finance_integration.py`
- EVM metric integration
- Reward calculation alignment

### UTCS Traceability
- Token transactions anchored in UTCS
- Full audit trail
- Provenance tracking

## Files

- [tt_config.json](./tt_config.json) - Main configuration
- [fee_schedule.json](./fee_schedule.json) - Fee schedule details
- [staking_params.json](./staking_params.json) - Staking parameters
- [slashing_rules.json](./slashing_rules.json) - Slashing conditions
- [governance_params.json](./governance_params.json) - Governance settings

## References

- [Teknia Finance Integration](../../../finance/teknia_finance_integration.py)
- [Fee Calculator](../08-TOOLS/fee_calculator.py)
- [Staking Smart Contract Spec](./staking_contract_spec.md)
