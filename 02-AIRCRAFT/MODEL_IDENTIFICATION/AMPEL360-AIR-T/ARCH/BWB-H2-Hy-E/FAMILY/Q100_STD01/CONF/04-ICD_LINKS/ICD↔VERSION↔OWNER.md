<!-- UTCS: utcs://AMPEL360-AIR-T/BWB-H2-Hy-E/Q100_STD01 -->

# ICD ↔ Version ↔ Owner Quick Reference

## ICD Summary Table

| ICD ID | Version | Domain(s) | Owner | Status | Verification |
|--------|---------|-----------|-------|--------|-------------|
| ICD-CQH-001 | 2.1 | CQH | CQH Domain Lead | ✅ Active | Physical test |
| ICD-EEE-003 | 1.8 | EEE | EEE Domain Lead | ✅ Active | Electrical test |
| ICD-PPP-005 | 2.0 | PPP | PPP Domain Lead | ✅ Active | System test |
| ICD-AAA-007 | 1.5 | AAA | AAA Domain Lead | ✅ Active | FEA + test |
| ICD-IIS-012 | 3.2 | IIS | IIS Domain Lead | ✅ Active | Protocol test |
| ICD-CQH-AAA-002 | 1.3 | CQH, AAA | CQH/AAA Domain Leads | ✅ Active | Design + test |
| ICD-EEE-IIS-004 | 2.5 | EEE, IIS | EEE/IIS Domain Leads | ✅ Active | Integration test |
| ICD-PPP-EEE-006 | 1.9 | PPP, EEE | PPP/EEE Domain Leads | ✅ Active | Functional test |

## Version History

### ICD-CQH-001
- **v2.1** (2025-10-01): Updated leak rate requirements per EASA SC-H2 draft
- **v2.0** (2025-07-15): Major revision - new coupling design
- **v1.5** (2025-05-01): Initial baseline

### ICD-EEE-003
- **v1.8** (2025-09-25): Added arc fault detection requirements
- **v1.7** (2025-08-10): Updated current ratings
- **v1.5** (2025-06-15): Initial baseline

### ICD-PPP-005
- **v2.0** (2025-10-10): Dual power path redundancy added
- **v1.8** (2025-08-20): Cooling system refinements
- **v1.5** (2025-06-01): Initial baseline

### ICD-AAA-007
- **v1.5** (2025-09-15): Fail-safe load path verification complete
- **v1.3** (2025-07-05): Material change to Ti-6Al-4V
- **v1.0** (2025-05-10): Initial baseline

### ICD-IIS-012
- **v3.2** (2025-10-05): AFDX bandwidth optimization
- **v3.0** (2025-08-01): Major protocol revision
- **v2.5** (2025-06-15): Initial baseline

### ICD-CQH-AAA-002
- **v1.3** (2025-08-30): Stress test results incorporated
- **v1.2** (2025-07-10): Thermal expansion analysis
- **v1.0** (2025-05-20): Initial baseline

### ICD-EEE-IIS-004
- **v2.5** (2025-09-20): Power monitoring requirements added
- **v2.3** (2025-07-25): EMI/EMC compliance updates
- **v2.0** (2025-06-01): Initial baseline

### ICD-PPP-EEE-006
- **v1.9** (2025-10-08): Motor controller firmware update
- **v1.7** (2025-08-15): Thermal management improvements
- **v1.5** (2025-06-10): Initial baseline

## Owner Contact Information

| Owner | Email | Domain Role | Phone |
|-------|-------|------------|-------|
| CQH Domain Lead | cqh-steward@idealeeu.eu | CQH Domain Steward | +XX-XX-xxx-xxxx |
| EEE Domain Lead | eee-steward@idealeeu.eu | EEE Domain Steward | +XX-XX-xxx-xxxx |
| PPP Domain Lead | ppp-steward@idealeeu.eu | PPP Domain Steward | +XX-XX-xxx-xxxx |
| AAA Domain Lead | aaa-steward@idealeeu.eu | AAA Domain Steward | +XX-XX-xxx-xxxx |
| IIS Domain Lead | iis-steward@idealeeu.eu | IIS Domain Steward | +XX-XX-xxx-xxxx |

## Change Request Process

1. **File ECR**: Submit to `00-PROGRAM/CONFIG_MGMT/06-CHANGES/05-ECR/INBOX/`
2. **Impact Assessment**: Owner evaluates both interface sides
3. **Coordination**: For joint ICDs, all owners must approve
4. **CCB Review**: Monthly meeting or emergency session
5. **Version Update**: Increment minor (bug fix) or major (breaking change)
6. **Notification**: Email to all stakeholders
7. **Verification**: Re-run verification method after implementation

## Verification Method Legend

- **Physical test**: Hardware integration at test facility
- **Electrical test**: Bench test with real or representative hardware
- **System test**: Full system integration (e.g., iron bird)
- **FEA + test**: Finite element analysis validated by physical test
- **Protocol test**: Network protocol analyzer and load testing
- **Design + test**: Design review followed by validation test
- **Integration test**: Multi-system integration verification
- **Functional test**: End-to-end functional validation

---

**Data Source**: [`ICD_INDEX.md`](./ICD_INDEX.md)  
**Maintained By**: Configuration Management Team  
**Last Updated**: 2025-10-15  
**Next Review**: Monthly at CCB meeting
