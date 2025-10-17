# A360 Entity Relationship Diagram (ERD)

**Version:** 1.0  
**UTCS:** `utcs://BUSINESS/A360-EXCHANGES-TT/DATA-MODELS/ERD`

## Overview

This document describes the entity relationships in the A360exchanges-TT platform data model.

## Core Entities

### Primary Entities
1. **Asset** - Component definition and specifications
2. **Unit** - Individual serialized instances
3. **Listing** - Marketplace offerings
4. **Lease** - Rental contracts
5. **Repair** - Service records
6. **DPP** - Digital Product Passports
7. **Stake** - Token staking positions
8. **FeeEvent** - Transaction fees
9. **Account** - User/organization accounts

## Entity Relationships

```
┌──────────────────────────────────────────────────────────────────────┐
│                       A360 DATA MODEL ERD                             │
└──────────────────────────────────────────────────────────────────────┘

                         ┌───────────────┐
                         │   ACCOUNT     │
                         │───────────────│
                         │ id (PK)       │
                         │ name          │
                         │ type          │
                         │ tt_balance    │
                         │ verified      │
                         └───────┬───────┘
                                 │
                    ┌────────────┼────────────┐
                    │            │            │
           ┌────────▼──────┐ ┌──▼─────────┐ ┌▼────────────┐
           │    LISTING    │ │   LEASE    │ │    STAKE    │
           │───────────────│ │────────────│ │─────────────│
           │ id (PK)       │ │ id (PK)    │ │ id (PK)     │
           │ asset_uuid(FK)│ │ serial(FK) │ │ actor (FK)  │
           │ serial (FK)   │ │ lessor(FK) │ │ amount_TT   │
           │ seller (FK)   │ │ lessee(FK) │ │ role        │
           │ price         │ │ rates      │ │ rewards     │
           │ state         │ │ status     │ │ status      │
           └───────┬───────┘ └──┬─────────┘ └─────────────┘
                   │            │
       ┌───────────┼────────────┤
       │           │            │
┌──────▼───────┐ ┌─▼────────┐  │
│    ASSET     │ │   UNIT   │  │
│──────────────│ │──────────│  │
│ uuid (PK)    │ │serial(PK)│  │
│ partNo       │ │asset_uuid│◄─┘
│ rev          │ │  (FK)    │
│ DPP_id (FK)  │ │hours     │
│ SBOM_uri     │ │kWh       │
│ WEEE_cat     │ │SoH       │
│ specs        │ │status    │
│ limits       │ └──┬───────┘
│ SoH          │    │
│ custody[]    │    │
└──────┬───────┘    │
       │            │
       │         ┌──▼──────────┐
       │         │   REPAIR    │
       │         │─────────────│
       │         │ id (PK)     │
       │         │ serial (FK) │
       │         │ EU_form     │
       │         │ parts[]     │
       │         │ labor       │
       │         │ decision    │
       │         └─────────────┘
       │
┌──────▼───────┐
│     DPP      │
│──────────────│
│ id (PK)      │
│ asset_uuid   │
│   (FK)       │
│ serial       │
│ lifecycle[]  │
│ attestations │
│ compliance   │
└──────────────┘

┌─────────────────┐
│   FEEEVENT      │
│─────────────────│
│ id (PK)         │
│ type            │
│ eur_amount      │
│ tt_amount       │
│ payer (FK)      │
│ tx_ref          │
│ listing_id (FK) │
│ lease_id (FK)   │
│ repair_id (FK)  │
└─────────────────┘
```

## Relationship Details

### Asset → Unit (1:N)
- One Asset definition has many Unit instances
- Each Unit references one Asset via `asset_uuid`
- Cascade delete: Restrict (cannot delete Asset with active Units)

### Unit → Listing (1:N)
- One Unit can have multiple Listings over time
- Only one Listing can be active at a time
- Constraint: `state != 'active'` for historical Listings

### Unit → Lease (1:N)
- One Unit can be leased multiple times (sequentially)
- Active constraint: Only one active Lease per Unit
- Lease references Unit via `serial`

### Asset → DPP (1:1)
- Each Asset has exactly one DPP
- DPP created at Asset registration
- Lifecycle tied to Asset existence

### Unit → Repair (1:N)
- One Unit can have multiple Repair records
- Historical tracking of all repairs
- References Unit via `serial`

### Account → Listing (1:N)
- One Account (seller) can have multiple Listings
- Tracks ownership and transaction history

### Account → Lease (2:N)
- One Account acts as lessor (has N leases as owner)
- One Account acts as lessee (has M leases as renter)
- Dual relationship via `lessor` and `lessee` foreign keys

### Account → Stake (1:N)
- One Account can have multiple Stakes
- Different roles (market_maker, service_provider, oracle)
- Sum of all stakes ≤ account TT balance

### Transaction → FeeEvent (1:N)
- Each transaction (Listing, Lease, Repair, DPP) generates FeeEvents
- Foreign keys to originating transaction
- Aggregated for fee reporting

## Cardinality Summary

| Relationship | Type | Constraint |
|--------------|------|------------|
| Asset → Unit | 1:N | Mandatory |
| Unit → Listing | 1:N | Optional |
| Unit → Lease | 1:N | Optional |
| Unit → Repair | 1:N | Optional |
| Asset → DPP | 1:1 | Mandatory |
| Account → Listing | 1:N | Mandatory |
| Account → Lease (lessor) | 1:N | Mandatory |
| Account → Lease (lessee) | 1:N | Mandatory |
| Account → Stake | 1:N | Optional |
| Transaction → FeeEvent | 1:N | Mandatory |

## Key Constraints

### Business Rules

1. **Unit Availability**
   - A Unit can only be in one active Listing OR Lease at a time
   - Constraint: `CHECK (active_listing_count + active_lease_count ≤ 1)`

2. **Collateral Adequacy**
   - Lease collateral must meet minimum requirements
   - Constraint: `collateral.EUR + (collateral.TT * (1 - haircut)) ≥ required_collateral`

3. **Stake Lock-up**
   - Staked tokens cannot be withdrawn before `lock_until` date
   - Constraint: `CURRENT_DATE < lock_until THEN status = 'locked'`

4. **DPP Completeness**
   - DPP must have minimum required fields for compliance
   - Constraint: `completeness_pct ≥ 80 FOR compliance_status = 'compliant'`

5. **Fee Settlement**
   - All transactions must have corresponding FeeEvent records
   - Constraint: `FOR EACH transaction EXISTS FeeEvent WHERE tx_ref = transaction.id`

## Indexes

### Performance Optimization

```sql
-- Asset lookups
CREATE INDEX idx_asset_partno ON Asset(partNo, rev);
CREATE INDEX idx_asset_dpp ON Asset(DPP_id);
CREATE INDEX idx_asset_weee ON Asset(WEEE_cat);

-- Unit queries
CREATE INDEX idx_unit_asset ON Unit(asset_uuid);
CREATE INDEX idx_unit_status ON Unit(status);
CREATE INDEX idx_unit_owner ON Unit(owner);

-- Listing searches
CREATE INDEX idx_listing_state ON Listing(state);
CREATE INDEX idx_listing_seller ON Listing(seller);
CREATE INDEX idx_listing_asset ON Listing(asset_uuid);

-- Lease tracking
CREATE INDEX idx_lease_serial ON Lease(serial);
CREATE INDEX idx_lease_status ON Lease(status);
CREATE INDEX idx_lease_dates ON Lease(start, end);

-- Repair history
CREATE INDEX idx_repair_serial ON Repair(serial);
CREATE INDEX idx_repair_date ON Repair(created_at);

-- Stake queries
CREATE INDEX idx_stake_actor ON Stake(actor);
CREATE INDEX idx_stake_role ON Stake(role);
CREATE INDEX idx_stake_status ON Stake(status);

-- Fee analytics
CREATE INDEX idx_fee_type ON FeeEvent(type);
CREATE INDEX idx_fee_payer ON FeeEvent(payer);
CREATE INDEX idx_fee_date ON FeeEvent(created_at);
```

## Data Integrity

### Foreign Key Constraints

```sql
-- Asset relationships
ALTER TABLE Unit ADD CONSTRAINT fk_unit_asset
  FOREIGN KEY (asset_uuid) REFERENCES Asset(uuid);

-- Listing relationships
ALTER TABLE Listing ADD CONSTRAINT fk_listing_asset
  FOREIGN KEY (asset_uuid) REFERENCES Asset(uuid);
ALTER TABLE Listing ADD CONSTRAINT fk_listing_unit
  FOREIGN KEY (serial) REFERENCES Unit(serial);
ALTER TABLE Listing ADD CONSTRAINT fk_listing_seller
  FOREIGN KEY (seller) REFERENCES Account(id);

-- Lease relationships
ALTER TABLE Lease ADD CONSTRAINT fk_lease_unit
  FOREIGN KEY (serial) REFERENCES Unit(serial);
ALTER TABLE Lease ADD CONSTRAINT fk_lease_lessor
  FOREIGN KEY (lessor) REFERENCES Account(id);
ALTER TABLE Lease ADD CONSTRAINT fk_lease_lessee
  FOREIGN KEY (lessee) REFERENCES Account(id);

-- Repair relationships
ALTER TABLE Repair ADD CONSTRAINT fk_repair_unit
  FOREIGN KEY (serial) REFERENCES Unit(serial);

-- DPP relationships
ALTER TABLE DPP ADD CONSTRAINT fk_dpp_asset
  FOREIGN KEY (asset_uuid) REFERENCES Asset(uuid);

-- Stake relationships
ALTER TABLE Stake ADD CONSTRAINT fk_stake_actor
  FOREIGN KEY (actor) REFERENCES Account(id);

-- FeeEvent relationships
ALTER TABLE FeeEvent ADD CONSTRAINT fk_fee_payer
  FOREIGN KEY (payer) REFERENCES Account(id);
```

## Normalization

The data model follows 3NF (Third Normal Form):
- **1NF:** All attributes are atomic
- **2NF:** No partial dependencies on composite keys
- **3NF:** No transitive dependencies

### Denormalization Considerations

For performance, certain fields are intentionally denormalized:
- `Listing.DPP_snapshot` - Snapshot at listing time (historical record)
- `Lease.usage_tracking` - Current usage cache (updated frequently)
- `Stake.rewards` - Accumulated rewards (computed field)

## Change Log

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2025-10-17 | Initial ERD |

## Tools

- **Database Schema:** [schema.sql](./schema.sql)
- **Migration Scripts:** [migrations/](./migrations/)
- **Seed Data:** [seeds/](./seeds/)

## References

- [Data Model Schemas](../01-DATA-MODELS/)
- [API Specifications](../02-API-SPECS/)
- [Database Design Best Practices](https://www.postgresql.org/docs/current/ddl.html)
