# Configuration Management Plan (CMP)

## 1. Introduction

### 1.1 Purpose
Defines CM processes, procedures, and responsibilities for the IDEALE EU aerospace program lifecycle.

### 1.2 Scope
Applies to:
- Aircraft and spacecraft development/production
- Ground support equipment
- Software and firmware
- Documentation and specifications
- Test equipment and procedures

### 1.3 Applicable Standards
- **AS9100** — QMS: see **[STANDARDS/02-AIRCRAFT/QUALITY/](../STANDARDS/02-AIRCRAFT/QUALITY/)**  
- **ARP4754A** — Systems dev: **[STANDARDS/02-AIRCRAFT/SYSTEMS_ENGINEERING/](../STANDARDS/02-AIRCRAFT/SYSTEMS_ENGINEERING/)**  
- **ECSS-M-ST-40C** — Space CM: **[STANDARDS/04-CROSS_CUTTING/CONFIG_MGMT/](../STANDARDS/04-CROSS_CUTTING/CONFIG_MGMT/)**  
- **ISO 10007** — CM guidelines: **[STANDARDS/04-CROSS_CUTTING/CONFIG_MGMT/](../STANDARDS/04-CROSS_CUTTING/CONFIG_MGMT/)**  
- **DO-178C** — Software: **[STANDARDS/02-AIRCRAFT/SOFTWARE/](../STANDARDS/02-AIRCRAFT/SOFTWARE/)**  
- **DO-254** — Electronic HW: **[STANDARDS/02-AIRCRAFT/HARDWARE/](../STANDARDS/02-AIRCRAFT/HARDWARE/)**

---

## 2. Configuration Management Organization

### 2.1 Configuration Manager
- Maintains CMP, tools, and metrics; coordinates **[CCB](./05-CCB/)**.

### 2.2 Configuration Control Board (CCB)
- Reviews/approves changes; authorizes baselines. Members in **[05-CCB/01-MEMBERS.md](./05-CCB/01-MEMBERS.md)**.

### 2.3 Engineering
- Submits **ECRs**, implements **ECOs**, updates design docs (**[06-CHANGES/](./06-CHANGES/)**).

### 2.4 Quality Assurance
- Runs CM audits (**[11-AUDITS/](./11-AUDITS/)**); verifies implementations.

---

## 3. Configuration Identification

### 3.1 Configuration Items (CIs)
Hardware, software/firmware, documents, tooling/GSE, test procedures.

### 3.2 Part Numbering
See **[02-PART_NUMBERING.md](./02-PART_NUMBERING.md)**. Unique IDs, intelligent codes, revision control, interchangeability.

### 3.3 Serialization
See **[03-SERIALIZATION.md](./03-SERIALIZATION.md)**. Applies to flight-critical hardware, test articles, major assemblies, controlled tooling.

---

## 4. Configuration Control

### 4.1 Baseline Management
Gates and baselines: SRR, PDR, CDR, TRR, PRR, ORR/EIS (aircraft), FRR (spacecraft). Stored in **[04-BASELINES/](./04-BASELINES/)**.

### 4.2 Change Process
All changes to baselined items follow ECR/ECO:
1. **Initiation** — submit **[ECR](./13-TEMPLATES/ECR.yml)**
2. **Classification** — Class I/II/III
3. **Impact Assessment** — engineering
4. **CCB Review** — approve/reject (**[05-CCB/](./05-CCB/)**)
5. **Implementation** — issue ECO
6. **Verification** — QA verifies
7. **Closure** — record in **[06-CHANGES/](./06-CHANGES/)**

### 4.3 Change Classification
- **Class I** — affects form/fit/function or certification; CCB approval
- **Class II** — minor/doc changes; delegated
- **Class III** — administrative; CM approval

### 4.4 Deviations and Waivers
- **Deviation** — temporary departure (one-time) → **[06-CHANGES/DEVIATIONS/](./06-CHANGES/DEVIATIONS/)**  
- **Waiver** — permanent acceptance → **[06-CHANGES/WAIVERS/](./06-CHANGES/WAIVERS/)**

---

## 5. Configuration Status Accounting

### 5.1 Item Master
**[08-ITEM_MASTER/ITEMS.csv](./08-ITEM_MASTER/ITEMS.csv)** with PN, description, revision, status, effectivity, owner.

### 5.2 Traceability
**[10-TRACEABILITY/](./10-TRACEABILITY/)** holds:
- **[REQ_ITEM.csv](./10-TRACEABILITY/REQ_ITEM.csv)**
- **[CHANGE_BASELINE.csv](./10-TRACEABILITY/CHANGE_BASELINE.csv)**
- UTCS threads

### 5.3 Reporting
Monthly metrics: open ECR/ECO, backlog, baseline integrity, audit findings.

---

## 6. Configuration Audits
- **PCA** — as-built vs. design  
- **FCA** — performance vs. requirements  
- CM process audit  
Records in **[11-AUDITS/](./11-AUDITS/)**.

---

## 7. Interface Management

### 7.1 ICDs
All interfaces in **[09-INTERFACES/](./09-INTERFACES/)**.

### 7.2 ICD Process
Identify → draft **ICD** (template **[09-INTERFACES/ICD-XXXX.md](./09-INTERFACES/ICD-XXXX.md)**) → coordinate → sign → place under control.

---

## 8. Release Management

### 8.1 Process
Verify → prepare docs → CCB approval → release to mfg/ops → archive in **[07-RELEASES/AIRCRAFT/](./07-RELEASES/AIRCRAFT/)** or **[07-RELEASES/SPACECRAFT/](./07-RELEASES/SPACECRAFT/)**.

### 8.2 Package Contents
Drawings, BOM, specs, work instructions, test procedures, certification evidence.

---

## 9. CI/CD Integration

### 9.1 Version Control
Git with **[BRANCHING_MODEL.md](./12-CI_CD_RULES/BRANCHING_MODEL.md)**, **[TAGGING.md](./12-CI_CD_RULES/TAGGING.md)**, **[CODEOWNERS](./12-CI_CD_RULES/CODEOWNERS)**.

### 9.2 Automated Gates
Pre-merge checks: **[12-CI_CD_RULES/GATES.md](./12-CI_CD_RULES/GATES.md)**.

---

## 10. Training
Mandatory CM training on processes, tools, change control, and baselines.

---

## 11. CM Tools
Git; PLM/PDM (item master, docs); Issue tracker (ECR/ECO); Traceability tools.

---

## 12. Metrics and Continuous Improvement
Track ECR/ECO cycle time, backlog, baseline integrity, audit closure rate, CI identification coverage. Review and improve periodically.
