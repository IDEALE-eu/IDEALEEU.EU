# 39-ELECTRICAL_PANELS — SYSTEMS

**Ruta:** `IDEALEEU.EU/02-AIRCRAFT/DOMAIN_INTEGRATION/PRODUCTS/AMPEL360-AIR-T/MODELS/BWB-H2-Hy-E/CONF/BASELINE/FAMILY/Q100_STD01/VERSION/Q100/DOMAINS/EEE-ELECTRICAL-ENDOTRANSPONDERS-CIRCULATION/SYSTEMS/39-ELECTRICAL_PANELS/`

## Meta
- **Sistema:** 39-ELECTRICAL_PANELS
- **ATA Chapter:** 39
- **Descripción:** Electrical Panels and Distribution Boxes
- **Norma de organización:** PLM/CAx **solo** bajo `SUBSYSTEMS/`

## Índice de Subsistemas

| Subsistema | Descripción |
|------------|-------------|
| [39-00_STANDARDS_GENERAL/](./SUBSYSTEMS/39-00_STANDARDS_GENERAL/) | General Standards and Documentation |
| [39-10_PRIMARY_PANELS_PDP_PEB/](./SUBSYSTEMS/39-10_PRIMARY_PANELS_PDP_PEB/) | Primary Distribution Panels (PDP), Power Electronics Bays (PEB) |
| [39-20_SECONDARY_PANELS_JUNCTION_BOXES/](./SUBSYSTEMS/39-20_SECONDARY_PANELS_JUNCTION_BOXES/) | Secondary Panels and Junction Boxes |
| [39-30_REMOTE_POWER_DISTRIBUTION_RPDU/](./SUBSYSTEMS/39-30_REMOTE_POWER_DISTRIBUTION_RPDU/) | Remote Power Distribution Units (RPDU) |
| [39-40_PANEL_HEALTH_COOLING_IF_TO_21_94/](./SUBSYSTEMS/39-40_PANEL_HEALTH_COOLING_IF_TO_21_94/) | Panel Health Monitoring, Cooling Interface to ATA 21 & 94 |

## Convenciones clave

- Estructura base: `…/SYSTEMS/39-ELECTRICAL_PANELS/{INTEGRATION_VIEW.md, INTERFACE_MATRIX, SUBSYSTEMS}`
- Documentación de sistema en este nivel. Detalle técnico y PLM en `SUBSYSTEMS/…`
- Ver [INTEGRATION_VIEW.md](./INTEGRATION_VIEW.md) para vista de integración
- Ver [INTERFACE_MATRIX/](./INTERFACE_MATRIX/) para interfaces con otros sistemas
- EWIS (cableado) está en ATA 92, no aquí (ver ../NOTES.txt)

## Arquitectura del Sistema

El sistema de paneles eléctricos del BWB-H2-Hy-E incluye:

- **Paneles primarios (PDP):** Distribución principal de potencia, protección centralizada
- **Bahías de electrónica de potencia (PEB):** Conversores, inversores, controladores de carga
- **Paneles secundarios:** Distribución zonal, cajas de derivación, interfaces de subsistemas
- **RPDUs:** Unidades remotas de distribución con protección integrada SSPC
- **Sistema de salud:** Monitoreo de temperatura, corriente, voltaje, estado de contactores
- **Gestión térmica:** Interfaces con sistemas de refrigeración (ATA 21, 94)
