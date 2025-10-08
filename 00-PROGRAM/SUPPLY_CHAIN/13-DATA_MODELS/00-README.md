# 13-DATA_MODELS

Data models, schemas, and master data for supply chain systems.

## Overview

Standardized data structures for suppliers, materials, and approved lists to ensure consistency across systems.

## Contents

- **00-README.md** - This file
- **SCHEMAS/** - JSON schemas for data validation
- **INSTANCES/** - Master data instances (CSV format)
- **EDI_MAPPINGS/** - EDI transaction set mappings

## Data Entities

### Vendor Master
- Supplier identification and contact information
- Legal and financial data
- Certifications and approvals
- Performance and risk ratings

### Material Master
- Part number and description
- Technical specifications
- Classification and attributes
- Planning and costing parameters

### Approved Vendor List (AVL)
- Qualified suppliers by part number
- Primary and alternate suppliers
- Lead times and minimums

### Approved Manufacturer List (AML)
- Qualified manufacturers for parts (especially COTS)
- Part cross-references
- Manufacturer part numbers
