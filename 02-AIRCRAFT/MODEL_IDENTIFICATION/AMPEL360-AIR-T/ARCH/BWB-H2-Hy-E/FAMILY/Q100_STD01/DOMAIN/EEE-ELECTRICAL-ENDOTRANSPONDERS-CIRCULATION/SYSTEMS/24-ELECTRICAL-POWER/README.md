# 24-ELECTRICAL-POWER — SYSTEMS

**Ruta:** `IDEALEEU.EU/02-AIRCRAFT/MODEL_IDENTIFICATION/AMPEL360-AIR-T/ARCH/BWB-H2-Hy-E/FAMILY/Q100_STD01/DOMAIN/EEE-ELECTRICAL-ENDOTRANSPONDERS-CIRCULATION/SYSTEMS/24-ELECTRICAL-POWER/`

## Meta
- **Sistema:** 24-ELECTRICAL-POWER
- **ATA Chapter:** 24
- **Descripción:** Electrical Power Generation, Storage, Distribution
- **Norma de organización:** PLM/CAx **solo** bajo `SUBSYSTEMS/`

## Índice de Subsistemas

| Subsistema | Descripción |
|------------|-------------|
| [24-00_STANDARDS_GENERAL/](./SUBSYSTEMS/24-00_STANDARDS_GENERAL/) | General Standards and Documentation |
| [24-10_GENERATION_SOURCES_IDG_FC/](./SUBSYSTEMS/24-10_GENERATION_SOURCES_IDG_FC/) | Power Generation - IDG, Fuel Cells |
| [24-20_CONVERSION_RECTIFIERS_INVERTERS/](./SUBSYSTEMS/24-20_CONVERSION_RECTIFIERS_INVERTERS/) | Power Conversion - Rectifiers, Inverters |
| [24-30_DISTRIBUTION_BUS_TIE_CONTACTORS/](./SUBSYSTEMS/24-30_DISTRIBUTION_BUS_TIE_CONTACTORS/) | Power Distribution - Bus Ties, Contactors |
| [24-40_STORAGE_BATTERIES_SUPERCAPS_BMS/](./SUBSYSTEMS/24-40_STORAGE_BATTERIES_SUPERCAPS_BMS/) | Energy Storage - Batteries, Supercaps, BMS |
| [24-50_PROTECTION_SSPC_BREAKERS_RRUs/](./SUBSYSTEMS/24-50_PROTECTION_SSPC_BREAKERS_RRUs/) | Circuit Protection - SSPC, Breakers, RRUs |
| [24-60_GROUND_POWER_IF_400HZ_28VDC/](./SUBSYSTEMS/24-60_GROUND_POWER_IF_400HZ_28VDC/) | Ground Power Interface - 400Hz, 28VDC |
| [24-70_POWER_QUALITY_MONITORING_LMS/](./SUBSYSTEMS/24-70_POWER_QUALITY_MONITORING_LMS/) | Power Quality Monitoring, Load Management |

## Convenciones clave

- Estructura base: `…/SYSTEMS/24-ELECTRICAL-POWER/{INTEGRATION_VIEW.md, INTERFACE_MATRIX, SUBSYSTEMS}`
- Documentación de sistema en este nivel. Detalle técnico y PLM en `SUBSYSTEMS/…`
- Ver [INTEGRATION_VIEW.md](./INTEGRATION_VIEW.md) para vista de integración
- Ver [INTERFACE_MATRIX/](./INTERFACE_MATRIX/) para interfaces con otros sistemas
- EWIS (cableado) está en ATA 92, no aquí (ver ../NOTES.txt)

## Arquitectura del Sistema

El sistema de potencia eléctrica del BWB-H2-Hy-E incluye:

- **Generación:** Fuel cells, generadores IDG, generadores de emergencia
- **Conversión:** Rectificadores AC/DC, inversores DC/AC
- **Distribución:** Buses primarios, buses de respaldo, contactores, bus ties
- **Almacenamiento:** Baterías principales, baterías de emergencia, supercapacitores
- **Protección:** SSPCs (Solid State Power Controllers), RRUs (Remote Remote Units), breakers
- **Interfaz tierra:** Conexiones de alimentación en tierra 400Hz AC y 28VDC
- **Monitoreo:** Sistema de gestión de carga, monitoreo de calidad de energía
