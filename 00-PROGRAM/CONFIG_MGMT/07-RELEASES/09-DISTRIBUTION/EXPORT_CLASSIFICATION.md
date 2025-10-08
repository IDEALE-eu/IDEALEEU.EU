# Export Control Classification

**Document Number:** CM-EXPORT-CLASS  
**Revision:** 1.0  
**Date:** 2025-01-01

## 1. Purpose

Documents export control classification determinations for releases to ensure compliance with international trade regulations.

## 2. Export Control Regimes

### 2.1 United States
- **ITAR** — International Traffic in Arms Regulations (State Department)
- **EAR** — Export Administration Regulations (Commerce Department)

### 2.2 European Union
- **EU Dual-Use Regulation** — (EC) No 428/2009
- **Common Military List**

### 2.3 International
- **Wassenaar Arrangement** — Multilateral export control

## 3. Classification Process

1. **Technical Review** — Engineering describes technology
2. **Legal Review** — Export compliance attorney determines classification
3. **Justification** — Document rationale
4. **Approval** — Configuration Manager and Legal approve
5. **Documentation** — Record classification
6. **Annual Review** — Re-evaluate classification

## 4. Export Control Classification Number (ECCN)

Format: `XYZ99[.A-E]`

Common ECCNs for aerospace:
- **9A991** — Aircraft and related items
- **9B991** — Manufacturing equipment
- **9D991** — Software
- **9E991** — Technology
- **7A994** — Electronic components

## 5. Classification Template

For each release, document:

```markdown
## Release: [RELEASE-ID]

### Classification
- **ECCN:** [Number or "See USML" or "EAR99"]
- **USML Category:** [Category or "N/A"]
- **Dual-Use:** [Yes/No]
- **Determination Date:** [YYYY-MM-DD]
- **Reviewed By:** [Name, Title]

### Justification
[Detailed technical justification for classification]

### License Requirements
- **License Exception:** [If applicable]
- **License Required:** [Destinations requiring license]

### Authorized Destinations
[List of authorized countries or "Worldwide except..."]

### Restricted Destinations
[List of restricted countries or reference to Country Groups]

### End-User Requirements
- End-user certificate: [Required/Not Required]
- Technology Control Plan: [Required/Not Required]

### Compliance Notes
[Special handling, annual review requirements, etc.]

### Reviewer Signatures
- **Technical Reviewer:** _________________ Date: _______
- **Export Compliance:** _________________ Date: _______
- **Legal:** _________________ Date: _______
```

## 6. Common Classifications

### 6.1 Civil Aircraft (Non-ITAR)
Typically **ECCN 9A991** if:
- Designed for civil use
- Not specifically designed or modified for military use
- Meets civil aviation standards (FAA, EASA)

### 6.2 Spacecraft (Often ITAR)
Many spacecraft items are **USML Category XV**:
- Spacecraft systems and related components
- Ground control systems
- Propulsion systems
- Attitude control systems

Exception: Commercial satellites meeting certain criteria may be **ECCN 9A004**.

### 6.3 Software
- **9D004** — Software for flight control
- **9D991** — Software for civil aircraft (not 9D004)

### 6.4 EAR99
Items not on CCL and not ITAR — minimal controls, still subject to embargo destinations.

## 7. Restricted Destinations

### 7.1 Embargoed Countries
Per U.S. regulations (check current list):
- Cuba
- Iran
- North Korea
- Syria
- Crimea region

### 7.2 Country Groups
- **E:1** — Terrorist supporting countries
- **E:2** — Additional restricted countries

### 7.3 Denied Parties
Check Consolidated Screening List:
- Denied Persons List
- Entity List
- Unverified List
- Specially Designated Nationals (SDN)

## 8. License Exceptions and Exemptions

### 8.1 Common License Exceptions
- **ENC** — Encryption commodities, software, technology
- **TSU** — Technology and software – unrestricted
- **GOV** — Governments and international organizations
- **APR** — Additional permissive reexports

### 8.2 Exemptions
- Public domain information
- Educational information
- Fundamental research

## 9. Compliance Procedures

### 9.1 Before Each External Distribution
1. Verify export classification current
2. Check recipient against denied parties lists
3. Verify destination country restrictions
4. Obtain export license if required
5. Obtain end-user certificate if required
6. Document export in log

### 9.2 Annual Review
- Review all classifications
- Update based on regulatory changes
- Re-classify if technology changed
- Train personnel on updates

## 10. Penalties for Violations

Export control violations can result in:
- Civil fines up to $300,000 per violation
- Criminal fines up to $1,000,000
- Imprisonment up to 20 years
- Debarment from export privileges
- Loss of government contracts

**Report suspected violations immediately to Legal and Export Compliance.**

## 11. Training

All personnel involved in releases must complete:
- Export control awareness training (annual)
- Role-specific training
- Refresher when regulations change

## 12. Related Documents

- [00-README.md](./00-README.md)
- [SECURITY.md](./SECURITY.md)
- Export Control Compliance Plan (Legal)
- International Traffic in Arms Regulations (ITAR)
- Export Administration Regulations (EAR)

## 13. Contact

- **Export Compliance Officer:** [Contact Info]
- **Legal Counsel:** [Contact Info]
- **Configuration Manager:** [Contact Info]

---

**This document is for internal use only. Classification determinations are confidential.**

## 14. Revision History

| Rev | Date | Description | Approved By |
|-----|------|-------------|-------------|
| 1.0 | 2025-01-01 | Initial release | Export Compliance Officer |
