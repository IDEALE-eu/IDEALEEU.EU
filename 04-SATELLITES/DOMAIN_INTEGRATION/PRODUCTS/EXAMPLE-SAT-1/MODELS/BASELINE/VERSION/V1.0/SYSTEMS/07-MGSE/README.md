# 07-MGSE — Mechanical Ground Support Equipment

**Purpose:**  
Mechanical Ground Support Equipment (MGSE) enables safe handling, integration, transportation, and testing of the EXAMPLE-SAT-1 spacecraft during assembly, integration, and test (AIT) phases. This includes cradles, lift fixtures, alignment tools, and cleanroom handling aids.

**Integration Status:**  
- **Non-flight system** — used exclusively in ground operations  
- **Not part of flight configuration** — excluded from mass/power/thermal budgets  
- **Interface-critical** — defines mechanical and alignment boundaries for flight hardware

**Key Interfaces:**  
- **51-PRIMARY_STRUCTURE**: Load paths, interface plates, alignment pins  
- **50-MECHANISMS_DEPLOYABLES**: Stowage and deployment verification fixtures  
- **16-EGSE**: Coordination with electrical ground support during integrated tests  
- **07-MGSE ↔ 00-PROGRAM/CONFIG_MGMT/09-INTERFACES/**: ICDs managed centrally (e.g., `ICD-MGSE-51-01`)

**Design & Compliance:**  
- Complies with ECSS-E-HB-32-23A (MGSE design handbook)  
- Materials: non-magnetic, low-outgassing (per ECSS-Q-ST-70-02C)  
- Cleanliness: ISO Class 8 (or better) compatible  
- Traceability: All MGSE items tracked in `00-PROGRAM/CONFIG_MGMT/05-CONFIGURATION/`

**Artifacts:**  
MGSE design and verification artifacts are maintained in engineering workspaces.  
**No PLM/CAx content resides in this folder** — per IDEALE rule: *PLM/CAx only in flight SUBSYSTEMS*.

**Verification:**  
- Structural FEM (static, dynamic)  
- Modal survey during AIT  
- Alignment repeatability checks (< 50 µm)  
- Witnessed dry-runs with flight hardware

**Ownership:**  
- AIT Lead Engineering  
- Configuration managed via ECR/ECO in `00-PROGRAM/CONFIG_MGMT/06-CHANGES/`
```

