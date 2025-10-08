# Configuration Management (CONFIG_MGMT)

Ensures systematic control of product configuration across the lifecycle: consistency, traceability, integrity.

## Purpose
- Unique identification of all configuration items  
- Baseline management across milestones  
- Change control (ECR/ECO)  
- Requirements and change traceability  
- Interface control documentation  
- Versioning and release management

## Contents
- **[00-README.md](./00-README.md)** — This file  
- **[01-CM_PLAN.md](./01-CM_PLAN.md)** — Configuration Management Plan  
- **[02-PART_NUMBERING.md](./02-PART_NUMBERING.md)** — Part numbering scheme  
- **[03-SERIALIZATION.md](./03-SERIALIZATION.md)** — Serialization guidelines  
- **[04-BASELINES/](./04-BASELINES/)** — SRR, PDR, CDR, TRR, PRR, ORR_EIS, FRR  
- **[05-CCB/](./05-CCB/)** — Charter, members, minutes  
- **[06-CHANGES/](./06-CHANGES/)** — ECR, ECO, Deviations, Waivers  
- **[07-RELEASES/](./07-RELEASES/)** — Aircraft and Spacecraft release packages  
- **[08-ITEM_MASTER/](./08-ITEM_MASTER/)** — Master list of CIs with attributes  
- **[09-INTERFACES/](./09-INTERFACES/)** — ICDs and interface management  
- **[10-TRACEABILITY/](./10-TRACEABILITY/)** — Req↔Item, Change↔Baseline, UTCS threads  
- **[11-AUDITS/](./11-AUDITS/)** — Configuration and functional audits  
- **[12-CI_CD_RULES/](./12-CI_CD_RULES/)** — Branching, tagging, gates  
- **[13-TEMPLATES/](./13-TEMPLATES/)** — ECR/ECO and CM templates

## Key Standards
- **AS9100** — QMS: **[STANDARDS/02-AIRCRAFT/QUALITY/](../STANDARDS/02-AIRCRAFT/QUALITY/)**  
- **ARP4754A** — Aircraft systems dev: **[STANDARDS/02-AIRCRAFT/SYSTEMS_ENGINEERING/](../STANDARDS/02-AIRCRAFT/SYSTEMS_ENGINEERING/)**  
- **ECSS-M-ST-40C** — Space CM: **[STANDARDS/04-CROSS_CUTTING/CONFIG_MGMT/](../STANDARDS/04-CROSS_CUTTING/CONFIG_MGMT/)**  
- **ISO 10007** — CM guidelines: **[STANDARDS/04-CROSS_CUTTING/CONFIG_MGMT/](../STANDARDS/04-CROSS_CUTTING/CONFIG_MGMT/)**

## Workflow
1. **Identification** — Assign PNs, maintain **[Item Master](./08-ITEM_MASTER/)**  
2. **Baseline** — Freeze at gates in **[04-BASELINES/](./04-BASELINES/)**  
3. **Change Control** — Submit **[ECR/ECO](./06-CHANGES/)**; approve via **[CCB](./05-CCB/)**  
4. **Traceability** — Maintain links in **[10-TRACEABILITY/](./10-TRACEABILITY/)**  
5. **Audit** — Execute **[configuration/functional audits](./11-AUDITS/)**  
6. **Release** — Package in **[07-RELEASES/](./07-RELEASES/)**

## Roles & Responsibilities
- **Configuration Manager** — CM system owner  
- **CCB Chair** — Leads change control board  
- **CCB Members** — Review and approve changes  
- **Engineering** — Submit ECRs, implement ECOs  
- **Quality** — Audit CM compliance  
- **Manufacturing** — Implement released configurations

## Cross-Links
- Program governance: **[GOVERNANCE.md](../GOVERNANCE.md)**  
- Digital thread hooks: **[DIGITAL_THREAD/](../DIGITAL_THREAD/)**  
- Quality QMS: **[QUALITY_QMS/](../QUALITY_QMS/)**  
- Supply chain impacts: **[SUPPLY_CHAIN/](../SUPPLY_CHAIN/)**
