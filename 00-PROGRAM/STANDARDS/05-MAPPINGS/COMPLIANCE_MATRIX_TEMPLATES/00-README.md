# COMPLIANCE_MATRIX_TEMPLATES

Templates for standards compliance matrices.

## Overview

This directory contains templates for detailed compliance matrices. These are used to demonstrate objective-by-objective or clause-by-clause compliance with standards.

## Contents

- **00-README.md** - This file
- **ARP4754A_CM.csv** - ARP4754A systems engineering compliance matrix
- **DO178C_CM.csv** - DO-178C software compliance matrix
- **ECSS_CM.csv** - ECSS spacecraft engineering compliance matrix

## Usage

1. Copy template for your project
2. Fill in applicability, rationale, compliance method, evidence
3. Update status as work progresses
4. Review at stage gates (PDR, CDR, TRR)
5. Submit to certification authorities as needed

## Template Structure

All templates follow similar structure:
- **Objective/Clause**: Standard requirement identifier
- **Description**: Brief description of requirement
- **Applicability**: FULL, PARTIAL, TAILORED, N/A
- **Rationale**: Why applicable or not applicable
- **Compliance Method**: How requirement is met (DOCUMENT, TEST, REVIEW, ANALYSIS)
- **Compliance Evidence**: Reference to artifact (document ID, test report number, etc.)
- **Status**: COMPLIANT, IN-PROGRESS, NOT-STARTED, N/A
- **Notes**: Additional comments

## Best Practices

- Start filling out during planning phase (Phase A/B)
- Update continuously, not just before audits
- Be specific in evidence references (document IDs, section numbers)
- For N/A items, provide clear rationale
- Have independent reviewer check before submission
- Version control in PLM/PDM system

## Tailoring

For standards that allow tailoring (e.g., ECSS):
- Mark item as TAILORED in Applicability
- Provide detailed rationale for tailoring
- Obtain customer/authority agreement on tailoring

## Submission

- Submit to certification authorities as part of certification data package
- May be subject to audit or review by authorities
- Keep updated through entire lifecycle

---

**Status**: Configuration-controlled per 00-PROGRAM/CONFIG_MGMT/
