# MGSE — 21-10_RADIATORS_HEAT_EXCHANGERS

## Purpose

Mechanical Ground Support Equipment (MGSE) documentation for fixtures, lifts, slings, alignment tools, and handling equipment used during radiator, LPHX, and coldplate integration.

## Content Types

- **Fixture Specifications** — Assembly fixtures, jigs, and tooling
- **Lift/Sling Procedures** — Safe handling and transport
- **Alignment Tools** — Datums, references, measurement setups
- **Tooling Drawings** — MGSE design documentation
- **Calibration Records** — For measurement tooling

## File Formats

- `.pdf` — MGSE specifications, procedures, drawings
- `.step` — 3D models of fixtures and tooling (reference)
- `.xlsx` — Tool inventory and calibration tracking

## Naming Convention

```
MGSE-21-10-{type}__{revision}.pdf
```

**Examples:**
- `MGSE-21-10-fixture__r01.pdf`
- `MGSE-21-10-lift__r02.pdf`
- `MGSE-21-10-alignment_tool__r01.pdf`
- `MGSE-21-10-handling_sling__r00.pdf`

## MGSE Requirements

Each MGSE document must include:
- **Equipment Identification** — MGSE number, description
- **Purpose** — Intended use and hardware compatibility
- **Specifications** — Load capacity, materials, dimensions
- **Operating Procedures** — Setup, use, removal instructions
- **Safety Requirements** — Load limits, PPE, personnel required
- **Maintenance** — Inspection intervals, calibration requirements
- **Traceability** — Calibration records, inspection status
- **Approvals** — Engineering and safety sign-offs

## MGSE Types

### Assembly Fixtures
- **Purpose:** Hold and align radiators, LPHX, coldplates during installation
- **Features:** Datums, clamping provisions, access for fasteners
- **Load Capacity:** Support weight of hardware plus assembly loads
- **Accuracy:** Positioning accuracy per assembly tolerance

### Lifting Equipment
- **Purpose:** Safe handling and transport of heavy components
- **Types:** Hoists, cranes, spreader bars, lifting beams
- **Capacity:** Rated for 5x hardware weight minimum
- **Certification:** Annual inspection and load testing

### Slings and Rigging
- **Purpose:** Attach hardware to lifting equipment
- **Types:** Soft slings, wire rope, shackles, hooks
- **Capacity:** Rated for 5x hardware weight minimum
- **Inspection:** Visual before each use, periodic certification

### Alignment Tools
- **Purpose:** Establish datums and verify alignment
- **Types:** Optical targets, laser trackers, CMM fixtures
- **Accuracy:** ±0.05 mm or per drawing requirement
- **Calibration:** Valid cal cert, typically annual

## Operating Procedures

### Fixture Use
1. **Inspect:** Visual check for damage, cleanliness
2. **Setup:** Position per work instruction, verify datum alignment
3. **Load Hardware:** Carefully place component in fixture
4. **Secure:** Clamp or fasten per procedure
5. **Verify Alignment:** Check position before proceeding
6. **Release:** Remove hardware after operation complete
7. **Clean:** Return fixture to storage clean and ready

### Lifting Operations
1. **Pre-lift Inspection:** Verify rigging, capacity, attachments
2. **Briefing:** Review lift plan with all personnel
3. **Test Lift:** Lift 1-2 inches, verify stability
4. **Move:** Controlled movement, no pendulum swinging
5. **Lower:** Slow, controlled lowering to support
6. **Disconnect:** Remove rigging after hardware secured

## Safety Requirements

- **Load Limits:** Never exceed rated capacity
- **Inspection:** Pre-use visual inspection mandatory
- **Training:** Operators certified for specific MGSE
- **Clearance:** Maintain safe clearances from personnel
- **Communication:** Clear signals during lifting operations
- **Backup:** Safety straps or secondary support for critical operations

## Calibration & Maintenance

- **Measurement Tools:** Annual calibration for dimensional tools
- **Lifting Equipment:** Annual inspection and load test
- **Fixtures:** Periodic dimensional verification
- **Documentation:** Calibration certs and inspection records maintained
- **Out-of-Service:** Tag and segregate non-conforming MGSE

## Cross-References

- [Parent: CAI](../README.md)
- [Work Instructions](../work_instructions/README.md)
- [Assembly Plans](../assembly_plans/README.md)
- [Kitting](../kitting/README.md)

## Standards & Constraints

- **Load Safety Factor:** 5:1 minimum for lifting equipment
- **Accuracy:** Per assembly tolerance requirements
- **Materials:** Compatible with flight hardware (no contamination)
- **Cleanliness:** Clean MGSE before use on flight hardware
- **Calibration:** Valid certs for all measurement tools

## Revision Control

- MGSE documents maintained under configuration control
- Modifications require engineering and safety approval
- Obsolete MGSE tagged and removed from service
- Calibration status tracked in tool inventory
