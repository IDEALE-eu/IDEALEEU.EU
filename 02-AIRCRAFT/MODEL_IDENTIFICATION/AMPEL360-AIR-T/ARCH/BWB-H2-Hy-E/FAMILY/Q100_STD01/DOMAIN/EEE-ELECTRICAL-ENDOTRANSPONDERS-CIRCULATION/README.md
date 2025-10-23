# EEE-ELECTRICAL-ENDOTRANSPONDERS-CIRCULATION

# SYSTEMS — Index

* [24-ELECTRICAL-POWER](./SYSTEMS/24-ELECTRICAL-POWER/README.md)

  * [INTERFACE_MATRIX](./SYSTEMS/24-ELECTRICAL-POWER/INTERFACE_MATRIX.md)
  * [SUBSYSTEMS](./SYSTEMS/24-ELECTRICAL-POWER/SUBSYSTEMS/README.md)

    * [24-00_STANDARDS_GENERAL](./SYSTEMS/24-ELECTRICAL-POWER/SUBSYSTEMS/24-00_STANDARDS_GENERAL/README.md)
    * [24-10_GENERATION_SOURCES_IDG_FC](./SYSTEMS/24-ELECTRICAL-POWER/SUBSYSTEMS/24-10_GENERATION_SOURCES_IDG_FC/README.md)
    * [24-20_CONVERSION_RECTIFIERS_INVERTERS](./SYSTEMS/24-ELECTRICAL-POWER/SUBSYSTEMS/24-20_CONVERSION_RECTIFIERS_INVERTERS/README.md)
    * [24-30_DISTRIBUTION_BUS_TIE_CONTACTORS](./SYSTEMS/24-ELECTRICAL-POWER/SUBSYSTEMS/24-30_DISTRIBUTION_BUS_TIE_CONTACTORS/README.md)
    * [24-40_DISTRIBUTION](./SYSTEMS/24-ELECTRICAL-POWER/SUBSYSTEMS/24-40_DISTRIBUTION/README.md)
    * [24-50_PROTECTION_SSPC_BREAKERS_RRUs](./SYSTEMS/24-ELECTRICAL-POWER/SUBSYSTEMS/24-50_PROTECTION_SSPC_BREAKERS_RRUs/README.md)
    * [24-60_GROUND_POWER_IF_400HZ_28VDC](./SYSTEMS/24-ELECTRICAL-POWER/SUBSYSTEMS/24-60_GROUND_POWER_IF_400HZ_28VDC/README.md)
    * [24-70_POWER_QUALITY_MONITORING_LMS](./SYSTEMS/24-ELECTRICAL-POWER/SUBSYSTEMS/24-70_POWER_QUALITY_MONITORING_LMS/README.md)
    * [24-80_STORAGE_BATTERIES_SUPERCAPS_BMS](./SYSTEMS/24-ELECTRICAL-POWER/SUBSYSTEMS/24-80_STORAGE_BATTERIES_SUPERCAPS_BMS/README.md)
  * [INTEGRATION_VIEW.md](./SYSTEMS/24-ELECTRICAL-POWER/INTEGRATION_VIEW.md)
  * [README.md](./SYSTEMS/24-ELECTRICAL-POWER/README.md)

* [33-LIGHTS](./SYSTEMS/33-LIGHTS/README.md)

  * [SUBSYSTEMS](./SYSTEMS/33-LIGHTS/SUBSYSTEMS/README.md)

    * [33-00_STANDARDS_GENERAL](./SYSTEMS/33-LIGHTS/SUBSYSTEMS/33-00_STANDARDS_GENERAL/README.md)
    * [33-10_EXTERNAL_NAV_STROBE_BEACON](./SYSTEMS/33-LIGHTS/SUBSYSTEMS/33-10_EXTERNAL_NAV_STROBE_BEACON/README.md)
    * [33-20_LANDING_TAXI_TAKEOFF_LIGHTS](./SYSTEMS/33-LIGHTS/SUBSYSTEMS/33-20_LANDING_TAXI_TAKEOFF_LIGHTS/README.md)
    * [33-30_LOGO_WING_INSPECTION_LIGHTS](./SYSTEMS/33-LIGHTS/SUBSYSTEMS/33-30_LOGO_WING_INSPECTION_LIGHTS/README.md)
    * [33-40_EMERGENCY_EXT_MARKINGS_PWR_IF](./SYSTEMS/33-LIGHTS/SUBSYSTEMS/33-40_EMERGENCY_EXT_MARKINGS_PWR_IF/README.md)
  * [INTEGRATION_VIEW.md](./SYSTEMS/33-LIGHTS/INTEGRATION_VIEW.md)
  * [README.md](./SYSTEMS/33-LIGHTS/README.md)

* [39-ELECTRICAL_PANELS](./SYSTEMS/39-ELECTRICAL_PANELS/README.md)

  * [SUBSYSTEMS](./SYSTEMS/39-ELECTRICAL_PANELS/SUBSYSTEMS/README.md)

    * [39-00_STANDARDS_GENERAL](./SYSTEMS/39-ELECTRICAL_PANELS/SUBSYSTEMS/39-00_STANDARDS_GENERAL/README.md)
    * [39-10_PRIMARY_PANELS_PDP_PEB](./SYSTEMS/39-ELECTRICAL_PANELS/SUBSYSTEMS/39-10_PRIMARY_PANELS_PDP_PEB/README.md)
    * [39-20_SECONDARY_PANELS_JUNCTION_BOXES](./SYSTEMS/39-ELECTRICAL_PANELS/SUBSYSTEMS/39-20_SECONDARY_PANELS_JUNCTION_BOXES/README.md)
    * [39-30_REMOTE_POWER_DISTRIBUTION_RPDU](./SYSTEMS/39-ELECTRICAL_PANELS/SUBSYSTEMS/39-30_REMOTE_POWER_DISTRIBUTION_RPDU/README.md)
    * [39-40_PANEL_HEALTH_COOLING_IF_TO_21_94](./SYSTEMS/39-ELECTRICAL_PANELS/SUBSYSTEMS/39-40_PANEL_HEALTH_COOLING_IF_TO_21_94/README.md)
  * [INTEGRATION_VIEW.md](./SYSTEMS/39-ELECTRICAL_PANELS/INTEGRATION_VIEW.md)
  * [README.md](./SYSTEMS/39-ELECTRICAL_PANELS/README.md)

* [80-STARTING](./SYSTEMS/80-STARTING/README.md)

  * [SUBSYSTEMS](./SYSTEMS/80-STARTING/SUBSYSTEMS/README.md)

    * [80-00_STANDARDS_GENERAL](./SYSTEMS/80-STARTING/SUBSYSTEMS/80-00_STANDARDS_GENERAL/README.md)
    * [80-10_STARTER_GENERATORS_SG_PMSM](./SYSTEMS/80-STARTING/SUBSYSTEMS/80-10_STARTER_GENERATORS_SG_PMSM/README.md)
    * [80-20_START_POWER_ELECTRONICS_SPCU](./SYSTEMS/80-STARTING/SUBSYSTEMS/80-20_START_POWER_ELECTRONICS_SPCU/README.md)
    * [80-30_START_SEQUENCE_CONTROL_IF_73_76](./SYSTEMS/80-STARTING/SUBSYSTEMS/80-30_START_SEQUENCE_CONTROL_IF_73_76/README.md)
  * [INTEGRATION_VIEW.md](./SYSTEMS/80-STARTING/INTEGRATION_VIEW.md)
  * [README.md](./SYSTEMS/80-STARTING/README.md)

* [INTERFACE_MATRIX](./INTERFACE_MATRIX.md)

* [NOTES.txt](./NOTES.txt)

* [README.md](./README.md)


## Purpose

Define the scope, rules and governance for the **EEE — Electrical / Endotransponders / Circulation** domain. This file standardizes folder conventions, responsibilities, PLM/CAx rules and traceability requirements for all artifacts in the domain.

## Scope

Covers all electrical systems and subsystems related to endo-transponders and circulation.
Valid folders:

* `/SYSTEMS/...` → system definitions and system README files.
* `/SYSTEMS/<NN>-<NAME>/SUBSYSTEMS/...` → subsystem PLM/CAx, CAE, CAD, tests.
  **Note:** PLM/CAx is allowed **only** inside `SUBSYSTEMS` to preserve EBOM/BOM traceability.

## RASCI (Responsibilities)

* **Responsible:** Domain Owner (Engineering Lead, EEE)
* **Accountable:** Head of Electrical Systems
* **Support:** CAD, CAE, PLM, Safety teams
* **Consulted:** Adjacent system owners (propulsion, structures)
* **Informed:** Certification and Operations teams
  (Replace roles with contact names and emails in the Contacts section.)

## Domain Rules

1. Mandatory folder structure: `SYSTEMS` → `SUBSYSTEMS` → `PLM/CAx` | `CAE` | `CAD` | `TESTS`.
2. PLM/CAx artifacts must reside only under `SUBSYSTEMS/PLM/CAx`. Do not place PLM files at `SYSTEMS` root.
3. Each `CAD/CAE` README must include purpose, required file formats, owner, version and EBOM mapping.
4. Follow the naming conventions and metadata requirements described below.

## Naming and Conventions

* File name pattern: `{PART_ID}-{DESCRIPTION}_R{REV:03d}.{ext}`
  Example: `24-80-001-Battery_Assembly_R001.step`
* Units: SI. Temperatures in °C, pressure in bar, energy in kWh / kJ.
* Primary language: English for README and metadata. Engineering artifacts may contain English keywords required by tools (STEP, scripts).

## PLM / CAx Rules

* Use STEP AP242 with PMI for releaseable parts.
* Every delivery must include a metadata file (`.yaml` or `.json`) with the fields:

  ```yaml
  part_id: string
  description: string
  revision: string
  author: string
  cad_system: string
  cad_version: string
  mass_kg: number
  material: string
  ebom_id: string
  ```
* Revision control: include `Rxxx` in file names and register revisions in PLM.
* Release checklist (mandatory): geometry check, GD&T present, mass/inertia, interference check, STEP AP242 export, thumbnail PNG.

## Traceability and EBOM Mapping

* Each subsystem must publish `EBOM_ID` and a mapping of PART_IDs to PLM items.
* Keep `EBOM_MAPPING.csv` in `SUBSYSTEMS/PLM/` with columns:

  ```
  part_id, plm_id, revision, comment
  ```

## Standards & References

* STEP AP242 / ISO 10303-242
* ASME Y14.5 (GD&T)
* ASME Y14.41 (Digital Product Definition)
* AS9100 / EN 9100 (aerospace quality and traceability)
* ATA chapter mapping where applicable

## Revision Control

* Add `Last Updated` in the README header.
* Maintain `CHANGELOG.md` with entries: date, author, summary, affected files.

## Contacts / Owners

* Domain Owner: *Name* — *email*
* CAD Owner: *Name* — *email*
* CAE Owner: *Name* — *email*
  (Replace placeholders with real names and emails.)

## Templates and Utilities

* `TEMPLATE_METADATA.yaml` — metadata template for deliveries.
* `TEMPLATE_EBOM.csv` — EBOM mapping template.
* Link to `../SYSTEMS/README.md` for system-level structure guidance.

## Additional Notes

* Ensure CAD exports include mass properties and a thumbnail image (PNG).
* Document any deviations from conventions in the subsystem README and obtain approver sign-off.
* Keep metadata and EBOM mappings up to date to support PLM integration.

---

*Last Updated: 2025-10-23*
