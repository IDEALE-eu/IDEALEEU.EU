# High-Level Requirements (HLR) Index

## Purpose
Central entry point for all **High-Level Requirements** (system → software).  
Each item links directly to its individual requirement file for traceability.

---

## Index

| ID | Title | Status | Verification | Link |
|----|--------|----------|---------------|------|
| HLR-0001 | System Initialization and Mode Control | Draft | Analysis + Test | [HLR-0001.md](./HLR-0001.md) |
| HLR-0002 | Fault Detection and Annunciation | Draft | Test | [HLR-0002.md](./HLR-0002.md) |
| HLR-0003 | Power-Up Built-In Test | Approved | Analysis + Test | [HLR-0003.md](./HLR-0003.md) |
| HLR-0004 | Data Bus Communication Interface | In Review | Review + Test | [HLR-0004.md](./HLR-0004.md) |
| HLR-0005 | Safety Monitoring Function | Draft | Analysis | [HLR-0005.md](./HLR-0005.md) |

---

## Folder Layout
```

high/
HLR-0001.md
HLR-0002.md
HLR-0003.md
...
index.md (this file)

```

---

## Update Procedure
1. Add each new HLR as `HLR-####.md` using the approved template.  
2. Update this table with ID, title, status, verification type, and hyperlink.  
3. Maintain alignment with `requirements/TRACE.md`.  
4. Confirm review signatures before changing any status field.

---

## Review Checklist
- [ ] Requirement is necessary, testable, and unambiguous.  
- [ ] Constraints (timing, bounds, safety) defined.  
- [ ] Verification method stated.  
- [ ] Parent system function identified.  
- [ ] Trace to LLR(s) and test case(s) recorded.  

---

_Last updated: YYYY-MM-DD by [QA or Requirements Lead]_
```
