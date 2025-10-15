# EDI — ELECTRONICS, DIGITAL INSTRUMENTS

## Scope

The EDI (Electronics, Digital Instruments) domain encompasses all electronic, digital, and instrumentation systems for the AMPEL360-AIR-T BWB-H2-Hy-E aircraft. This includes:

- **ATA 31**: Indicating & Recording Systems (displays, recorders, alerting)
- **ATA 34**: Navigation Systems (air data, inertial, GNSS, surveillance, terrain)
- **ATA 40**: Avionics Standards & General (cross-system templates and requirements)
- **ATA 42**: Integrated Modular Avionics (IMA, processors, networks, security)
- **ATA 77**: Engine Indicating Systems (sensors, interfaces, displays)
- **ATA 94**: Electronics & Equipment Compartments (racks, cooling, EMI/EMC)

## Domain Architecture

### Unified Convention
- **Systems Level**: `INTEGRATION_VIEW.md` + `INTERFACE_MATRIX/`
- **Subsystems Level**: `PLM/CAx/` with all 9 subdirectories (CAD, CAE, CAO, CAI, CAM, CAV, CAP, CAS, CMP)
- **PLM/CAx artifacts ONLY in SUBSYSTEMS** (validation enforced)

### Systems
```
EDI-ELECTRONICS-DIGITAL-INSTRUMENTS/
├─ README.md (this file)
├─ INTERFACE_MATRIX/
│  └─ EDI↔24_34_39_42_44_45_71_72_92_93_94.csv
└─ SYSTEMS/
   ├─ README.md
   ├─ 31-INDICATING_RECORDING/
   │  ├─ README.md
   │  ├─ INTEGRATION_VIEW.md
   │  ├─ INTERFACE_MATRIX/
   │  │  └─ 31-INDICATING_RECORDING↔24_34_39_42_44_45_71_72_92_93_94.csv
   │  └─ SUBSYSTEMS/
   │     ├─ 31-00_STANDARDS_GENERAL/PLM/CAx/{CAD,CAE,CAO,CAI,CAM,CAV,CAP,CAS,CMP}/
   │     ├─ 31-10_FLIGHT_DECK_DISPLAYS/PLM/CAx/{CAD,CAE,CAO,CAI,CAM,CAV,CAP,CAS,CMP}/
   │     ├─ 31-20_ALERTING_CAUTION_WARNING/PLM/CAx/{CAD,CAE,CAO,CAI,CAM,CAV,CAP,CAS,CMP}/
   │     ├─ 31-30_RECORDERS_FDR_CVR/PLM/CAx/{CAD,CAE,CAO,CAI,CAM,CAV,CAP,CAS,CMP}/
   │     ├─ 31-40_DATA_ACQUISITION_BUSSING/PLM/CAx/{CAD,CAE,CAO,CAI,CAM,CAV,CAP,CAS,CMP}/
   │     └─ 31-50_ACMS_MAINT_LOGGING_IF/PLM/CAx/{CAD,CAE,CAO,CAI,CAM,CAV,CAP,CAS,CMP}/
   ├─ 34-NAVIGATION/
   │  ├─ README.md
   │  ├─ INTEGRATION_VIEW.md
   │  ├─ INTERFACE_MATRIX/
   │  │  └─ 34-NAVIGATION↔22_24_31_42_45_92.csv
   │  └─ SUBSYSTEMS/
   │     ├─ 34-00_STANDARDS_GENERAL/PLM/CAx/{CAD,CAE,CAO,CAI,CAM,CAV,CAP,CAS,CMP}/
   │     ├─ 34-10_AIR_DATA_ADC_PITOT_STATIC/PLM/CAx/{CAD,CAE,CAO,CAI,CAM,CAV,CAP,CAS,CMP}/
   │     ├─ 34-20_AHRS_IRS_INERTIAL/PLM/CAx/{CAD,CAE,CAO,CAI,CAM,CAV,CAP,CAS,CMP}/
   │     ├─ 34-30_RADIONAV_VOR_ILS_DME/PLM/CAx/{CAD,CAE,CAO,CAI,CAM,CAV,CAP,CAS,CMP}/
   │     ├─ 34-40_GNSS_GPS_GALILEO/PLM/CAx/{CAD,CAE,CAO,CAI,CAM,CAV,CAP,CAS,CMP}/
   │     ├─ 34-50_RADALT_HONEYWELL_ALT/PLM/CAx/{CAD,CAE,CAO,CAI,CAM,CAV,CAP,CAS,CMP}/
   │     ├─ 34-60_SURVEILLANCE_TCAS_ADSB/PLM/CAx/{CAD,CAE,CAO,CAI,CAM,CAV,CAP,CAS,CMP}/
   │     └─ 34-70_TERRAIN_EGPWS_GPWS/PLM/CAx/{CAD,CAE,CAO,CAI,CAM,CAV,CAP,CAS,CMP}/
   ├─ 42-INTEGRATED_MODULAR_AVIONICS/
   │  ├─ README.md
   │  ├─ INTEGRATION_VIEW.md
   │  ├─ INTERFACE_MATRIX/
   │  │  └─ 42-INTEGRATED_MODULAR_AVIONICS↔24_31_34_45_92_93.csv
   │  └─ SUBSYSTEMS/
   │     ├─ 42-00_STANDARDS_GENERAL/PLM/CAx/{CAD,CAE,CAO,CAI,CAM,CAV,CAP,CAS,CMP}/
   │     ├─ 42-10_CORE_PROCESSORS_CMC_CPM/PLM/CAx/{CAD,CAE,CAO,CAI,CAM,CAV,CAP,CAS,CMP}/
   │     ├─ 42-20_NETWORK_AFDX_TSN_SWITCHING/PLM/CAx/{CAD,CAE,CAO,CAI,CAM,CAV,CAP,CAS,CMP}/
   │     ├─ 42-30_TIME_SYNC_PTP_IRIG/PLM/CAx/{CAD,CAE,CAO,CAI,CAM,CAV,CAP,CAS,CMP}/
   │     ├─ 42-40_A653_PARTITIONS_SERVICES/PLM/CAx/{CAD,CAE,CAO,CAI,CAM,CAV,CAP,CAS,CMP}/
   │     ├─ 42-50_SW_LOADERS_CONFIG_MGMT/PLM/CAx/{CAD,CAE,CAO,CAI,CAM,CAV,CAP,CAS,CMP}/
   │     └─ 42-60_SECURITY_CRYPTO_KEYS_HARDENING/PLM/CAx/{CAD,CAE,CAO,CAI,CAM,CAV,CAP,CAS,CMP}/
   ├─ 77-ENGINE_INDICATING/
   │  ├─ README.md
   │  ├─ INTEGRATION_VIEW.md
   │  ├─ INTERFACE_MATRIX/
   │  │  └─ 77-ENGINE_INDICATING↔24_31_42_73_92.csv
   │  └─ SUBSYSTEMS/
   │     ├─ 77-00_STANDARDS_GENERAL/PLM/CAx/{CAD,CAE,CAO,CAI,CAM,CAV,CAP,CAS,CMP}/
   │     ├─ 77-10_EIU_INTERFACES_DATA_GW/PLM/CAx/{CAD,CAE,CAO,CAI,CAM,CAV,CAP,CAS,CMP}/
   │     ├─ 77-20_ENGINE_SENSORS_N1_N2_EGT_FF/PLM/CAx/{CAD,CAE,CAO,CAI,CAM,CAV,CAP,CAS,CMP}/
   │     ├─ 77-30_DISPLAY_INTEGRATION_EICAS/PLM/CAx/{CAD,CAE,CAO,CAI,CAM,CAV,CAP,CAS,CMP}/
   │     └─ 77-40_FADEC_DATA_IF_WITH_73/PLM/CAx/{CAD,CAE,CAO,CAI,CAM,CAV,CAP,CAS,CMP}/
   ├─ 94-EE_COMPARTMENTS/
   │  ├─ README.md
   │  ├─ INTEGRATION_VIEW.md
   │  ├─ INTERFACE_MATRIX/
   │  │  └─ 94-EE_COMPARTMENTS↔21_24_26_31_42_92.csv
   │  └─ SUBSYSTEMS/
   │     ├─ 94-00_STANDARDS_GENERAL/PLM/CAx/{CAD,CAE,CAO,CAI,CAM,CAV,CAP,CAS,CMP}/
   │     ├─ 94-10_RACKS_ARINC600_INSTALL/PLM/CAx/{CAD,CAE,CAO,CAI,CAM,CAV,CAP,CAS,CMP}/
   │     ├─ 94-20_COOLING_AIRFLOW_HEAT_MGMT/PLM/CAx/{CAD,CAE,CAO,CAI,CAM,CAV,CAP,CAS,CMP}/
   │     ├─ 94-30_EMI_EMC_SHIELDING_GASKETS/PLM/CAx/{CAD,CAE,CAO,CAI,CAM,CAV,CAP,CAS,CMP}/
   │     ├─ 94-40_ACCESS_PANELS_HUMS_MON/PLM/CAx/{CAD,CAE,CAO,CAI,CAM,CAV,CAP,CAS,CMP}/
   │     └─ 94-50_FIRE_DETECT_SUPPRESS_IF_26/PLM/CAx/{CAD,CAE,CAO,CAI,CAM,CAV,CAP,CAS,CMP}/
   └─ 40-AVIONICS_STD_GENERAL/            {TEMPLATE}
      ├─ README.md
      ├─ INTEGRATION_VIEW.md
      ├─ INTERFACE_MATRIX/
      │  └─ 40-AVIONICS_STD_GENERAL↔ALL.csv
      └─ SUBSYSTEMS/
         └─ 40-00_STANDARDS_TEMPLATES/PLM/CAx/{CAD,CAE,CAO,CAI,CAM,CAV,CAP,CAS,CMP}/
```

## RASCI Matrix

| Role | Responsible | Accountable | Support | Consult | Inform |
|------|-------------|-------------|---------|---------|--------|
| System Architect | System design, integration views | System requirements flow-down | Subsystem engineers | Chief Engineer, Safety | Program Management |
| Subsystem Engineer | Subsystem design, PLM artifacts | Subsystem requirements | System architect, suppliers | IMA architect, specialists | Configuration Management |
| IMA Architect | Core processing, partitioning | ARINC 653 compliance | Software engineers | System architect, certifying authority | All subsystems |
| Interface Manager | Interface matrix updates | ICD accuracy | System engineers | Configuration Management | Stakeholders |
| PLM Manager | Artifact organization | CAx structure compliance | Engineers | Configuration Management | Program |

## Domain Rules

### PLM Artifacts
- **PLM/CAx directories ONLY at SUBSYSTEM level**
- All 9 CAx subdirectories required: CAD, CAE, CAO, CAI, CAM, CAV, CAP, CAS, CMP
- Engineering BOMs tracked in `PLM/EBOM_LINKS.md`

### Systems Integration
- System-level: `INTEGRATION_VIEW.md` + `INTERFACE_MATRIX/`
- Cross-system interfaces coordinated through ICDs
- All systems must maintain interface matrices

### EWIS (Electrical Wiring Interconnection System)
- Physical connectivity managed in **ATA 92 only**
- Systems reference EWIS via interface matrices
- No duplication of wiring details

### Software Management
- Software versions tracked with **host LRU**
- Examples:
  - FADEC software in ATA 73 (Propulsion)
  - ARINC 653 partitions in ATA 42 (IMA)
  - Navigation software in ATA 34 (host system)

## Integration Notes

### Interface Control Documents (ICDs)
Reference: `../../00-PROGRAM/CONFIG_MGMT/09-INTERFACES/`

Key cross-domain interfaces:
- **EDI ↔ EEE (24)**: Avionics power distribution
- **EDI ↔ LCC (22)**: Auto-flight integration
- **EDI ↔ PPP (73)**: FADEC/engine control data
- **EDI ↔ AAA (92)**: EWIS connectivity
- **EDI ↔ MMM (27)**: Flight control actuation data

### Certification & Safety
- DO-178C for airborne software
- DO-254 for airborne electronic hardware
- ARINC 653 for IMA partitioning
- DO-297 for IMA architecture
- ED-202/DO-326 for cybersecurity

### Standards & References
- ARINC 429, 664p7 (AFDX), 653, 661
- RTCA DO-160 (environmental conditions)
- IEEE 1588 (PTP time synchronization)
- TSN (Time-Sensitive Networking)

## Navigation

- [📋 Systems README](./SYSTEMS/README.md)
- [🔗 Interface Matrix](./INTERFACE_MATRIX/)
- [⬆️ Back to Domains](../)
- [🏠 Q100 Root](../../)

---

**Domain**: EDI — Electronics, Digital Instruments  
**Product**: AMPEL360-AIR-T  
**Model**: BWB-H2-Hy-E  
**Version**: Q100  
**Status**: Structure complete - Ready for artifact population
