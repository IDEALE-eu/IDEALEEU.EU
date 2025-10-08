# 01-REGISTER

Standards register and compliance tracking system.

## Overview

This directory maintains the authoritative register of all standards applicable to the IDEALEEU.EU program, including their status, ownership, and any approved deviations or waivers.

## Contents

- **00-README.md** - This file
- **STANDARDS_REGISTER.csv** - Master register of all applicable standards
- **DEVIATIONS_WAIVERS.csv** - Non-conformances, deviations, and waivers tracking

## STANDARDS_REGISTER.csv

The master register tracks:
- **uid** - Unique identifier (e.g., STD-001, STD-002)
- **title** - Standard title (e.g., "DO-178C", "ARP4754A", "ECSS-E-ST-10C")
- **version** - Specific version/revision being used
- **domain** - Applicability: AIRCRAFT, SPACECRAFT, or CROSS_CUTTING
- **owner** - Responsible engineer/team
- **status** - ACTIVE, PLANNED, SUPERSEDED, RETIRED
- **linked_baseline** - Program baseline(s) where this standard applies
- **license_required** - YES/NO - whether purchase/license needed
- **source_url** - Where to obtain the standard (see 07-LINKS/)
- **effective_date** - When this version became applicable

### Usage
1. All standards MUST be registered before use in design
2. Updates require configuration control board approval
3. Superseded standards must be marked with replacement reference
4. Annual review to ensure currency

## DEVIATIONS_WAIVERS.csv

Tracks approved non-conformances:
- **id** - Unique deviation ID (e.g., DEV-001, WAV-001)
- **standard_id** - References uid in STANDARDS_REGISTER.csv
- **clause** - Specific clause/section not being met
- **type** - DEVIATION, WAIVER, or TAILORING
- **justification** - Technical/business rationale
- **safety_impact** - Assessment of safety implications (NONE, LOW, MEDIUM, HIGH)
- **cert_authority_notified** - YES/NO - whether EASA/FAA/ESA informed
- **approval_ref** - Reference to approval document/meeting
- **expiry_date** - When deviation expires (if applicable)

### Deviation Types
- **DEVIATION** - Temporary non-conformance, plan to comply later
- **WAIVER** - Permanent exception, will not comply
- **TAILORING** - Standard adapted to program needs with authority agreement

### Process
1. Engineering identifies non-conformance
2. Safety impact assessment performed
3. Justification documented
4. Approval sought from appropriate authority
5. If safety-related, certification authority notified
6. Entered into register
7. Tracked until closed or expired

## Reporting

Regular reports generated:
- Standards compliance status by domain
- Deviations/waivers by safety impact
- Standards requiring renewal/license
- Standards needing update due to new revisions

## Audits

This register is audited:
- Quarterly by Quality Assurance
- Before each stage gate (PDR, CDR, PRR)
- By certification authorities during compliance reviews
- During internal/external ISO 9001/AS9100 audits

## Interfaces

- **05-MAPPINGS/** - Standards mapped to requirements and processes
- **00-PROGRAM/CONFIG_MGMT/** - Configuration control of standards baseline
- **00-PROGRAM/QUALITY_QMS/** - Quality management system compliance
- Certification authorities (EASA, FAA, ESA) for approval of deviations

## Responsibilities

- **Standards Manager** - Maintains register, coordinates updates
- **Domain Leads** - Identify applicable standards for their areas
- **Safety Engineer** - Assesses safety impact of deviations
- **Certification Lead** - Interfaces with authorities on waivers
- **Configuration Manager** - Controls baseline changes
- **Quality Assurance** - Audits compliance and completeness

## Access

- Register is read-only except for authorized Standards Manager
- All program members have read access
- Changes require CM approval per 00-PROGRAM/CONFIG_MGMT/

---

**Status**: This register is configuration-controlled. All changes must follow the program's change control process.
