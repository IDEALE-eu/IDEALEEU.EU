# CAS · 21-10_RADIATORS_HEAT_EXCHANGERS

Purpose: authoritative **service & sustainment** documentation for radiators, embedded heat-pipe radiators, liquid plate heat exchangers (LPHX), coldplates, mounts, TIM/bondlines, and coating stacks using **S1000D** standard. No source code. No flight SW.

---

## Scope & Standards
- **S1000D Issue 6.0:** XML-based technical publications (Data Modules, Publication Modules, CSDB).
- **ATA iSpec 2200:** chapter/section alignment (21-10 = Thermal Control / Radiators & Heat Exchangers).
- **IETP delivery:** interactive electronic technical publications for ground crews and depot maintenance.

---

## Directory Structure
```
.../STA-B-THERMAL-TPS/SYSTEMS/21-THERMAL_CONTROL/SUBSYSTEMS/21-10_RADIATORS_HEAT_EXCHANGERS/PLM/CAx/CAS/
└── S1000D/                        # CSDB root
    ├── README.md
    ├── brex/
    │   └── BREX-AMPEL360-21-10.xml
    ├── dmrl/
    │   └── DMRL-AMPEL360-21-10.xml
    ├── dm/                        # Data Modules (XML)
    │   ├── 000-general/
    │   ├── 200-fault-isolation/
    │   ├── 400-scheduled-maintenance/
    │   ├── 500-removal-installation/
    │   ├── 600-repair/
    │   ├── 700-overhaul/
    │   ├── 800-ipd/
    │   └── 900-tools-consumables/
    ├── pm/                        # Publication Modules
    │   ├── AMM/PM-AMM-AMPEL360-21-10-Q10.xml
    │   ├── CMM/PM-CMM-AMPEL360-21-10-Q10.xml
    │   └── IPC/PM-IPC-AMPEL360-21-10-Q10.xml
    ├── icn/                       # Illustrations
    │   ├── vector/
    │   └── raster/
    ├── res/                       # CSS/XSL/Schematron
    ├── qc/                        # Validation logs
    └── delivery/                  # IETP/PDF packages
```

---

## Example: BREX Data Module
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- BREX — AMPEL360 — Subsystem 21-10 (Thermal Control: Radiators & Heat Exchangers) -->
<dmodule xmlns="http://www.s1000d.org/S1000D_6-0/xml_schema" xmlns:xlink="http://www.w3.org/1999/xlink">
  <identAndStatusSection>
    <dmAddress>
      <dmIdent>
        <dmCode modelIdentCode="AMPEL360" systemDiffCode="0"
                systemCode="2110" subSystemCode="00" subSubSystemCode="00"
                disassyCode="00" disassyCodeVariant="A"
                infoCode="023" infoCodeVariant="A" itemLocationCode="A"/>
        <language countryIsoCode="US" languageIsoCode="en"/>
        <issueInfo issueNumber="01" inWork="01"/>
        <security securityClassification="01"/>
      </dmIdent>
      <dmAddressItems>
        <issueDate year="2025" month="10" day="11"/>
        <dmTitle>
          <techName>Business Rules Exchange (BREX) for 21-10 Radiators &amp; Heat Exchangers</techName>
        </dmTitle>
      </dmAddressItems>
    </dmAddress>
    <dmStatus>
      <security securityClassification="01"/>
      <responsiblePartnerCompany>
        <enterpriseName>IDEALE Consortium</enterpriseName>
      </responsiblePartnerCompany>
      <originator>
        <enterpriseName>Thermal Control Team</enterpriseName>
      </originator>
      <applic>
        <displayText>
          <simplePara>Applicable to AMPEL360-SPACE-T, Q10 and later.</simplePara>
        </displayText>
      </applic>
      <brexDmRef>
        <dmRef>
          <dmRefIdent>
            <dmCode modelIdentCode="S1000D" systemDiffCode="0"
                    systemCode="0000" subSystemCode="00" subSubSystemCode="00"
                    disassyCode="00" disassyCodeVariant="A"
                    infoCode="022" infoCodeVariant="A" itemLocationCode="D"/>
          </dmRefIdent>
        </dmRef>
      </brexDmRef>
      <qualityAssurance>
        <unverified/>
      </qualityAssurance>
    </dmStatus>
  </identAndStatusSection>
  <content>
    <description>
      <levelledPara>
        <title>BREX Rules for 21-10</title>
        <para>This BREX defines project-specific constraints on S1000D data modules for subsystem 21-10.</para>
      </levelledPara>
    </description>
  </content>
</dmodule>
```

---

## Data Module Types (by Info Code)
- **000:** Descriptions, system overview, operating principles.
- **200:** Fault isolation, troubleshooting trees.
- **400:** Scheduled maintenance intervals, inspection procedures.
- **500:** Removal/installation of radiator panels, LPHX, coldplates.
- **600:** Repair procedures (seal replacement, re-coat).
- **700:** Overhaul (depot-level disassembly/refurb).
- **800:** Illustrated Parts Data (IPD) — parts lists with ICNs.
- **900:** Tools, consumables, special equipment lists.

---

## Publication Modules
- **AMM (Aircraft/Spacecraft Maintenance Manual):** consolidated maintenance tasks.
- **CMM (Component Maintenance Manual):** LPHX/coldplate depot procedures.
- **IPC (Illustrated Parts Catalog):** exploded views, part numbers, NSNs.

---

## Workflow
1. **Author DMs:** write XML per S1000D schema; validate against BREX.
2. **Illustrate:** create ICNs (SVG/CGM); link via `<graphic>` elements.
3. **Assemble PMs:** reference DMs in publication module structure.
4. **Validate:** run Schematron/BREX checks; log results in `qc/`.
5. **Publish:** transform to IETP/PDF via XSL-FO; package in `delivery/`.
6. **Revision Control:** issue/inWork increments; track changes in DMRL.

---

## Tools & Validation
- **XML Editors:** oXygen, Arbortext.
- **BREX Checker:** validate business rules.
- **Schematron:** structural/content validation.
- **XSL-FO:** PDF rendering.
- **IETP Viewer:** S1000D-compliant browser.

---

## References
- S1000D Issue 6.0 Specification (www.s1000d.org)
- ATA iSpec 2200 (Chapter 21 structure)
- AMPEL360 System Breakdown Structure (STA-B domain)
