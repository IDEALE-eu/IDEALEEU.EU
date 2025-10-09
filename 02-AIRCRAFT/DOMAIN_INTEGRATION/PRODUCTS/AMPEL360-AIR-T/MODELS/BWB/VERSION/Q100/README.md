# 02-AIRCRAFT/DOMAIN_INTEGRATION/PRODUCTS/AMPEL360-AIR-T/MODELS/BWB/VERSION/Q100 — Estructura de Dominios (versión unificada con `/SYSTEMS/`, SUBSISTEMAS y PLM/CAx)

## Objetivo

Estandarizar los 15 dominios con **único nivel `/SYSTEMS/`**, **sub-sistemas explícitos** y **PLM integrado dentro de cada sub-sistema (CAx)**.

---

## Convenciones clave

* **Rutas**: `…/<DOMINIO>/SYSTEMS/<ATA-XX_NOMBRE>/SUBSYSTEMS/<ATA-XX-YY_NOMBRE>/…`
* **PLM solo en SUBSYSTEMS** (artefactos reales). A nivel dominio: **políticas/plantillas**, no CAD/CAE reales.
* **SW con su LRU** (capítulos ATA del host). **EWIS solo ATA-92**.
* **Interfaces**: cada *SYSTEM* incluye `INTERFACE_MATRIX/` y `INTEGRATION_VIEW.md`.

---

## Patrón de niveles

### 1) Nivel Dominio (contrato/plantillas)

```
<DOMINIO>/
├─ README.md                      # Alcance, RASCI, reglas
├─ SYSTEMS/                       # Carpeta obligatoria (contenedor de sistemas ATA)
├─ DELs/
│  ├─ TEMPLATES/                  # Plantillas de entregables
│  └─ SCHEMAS/                    # Esquemas de validación
├─ PAx/
│  └─ STANDARDS/                  # Estándares de empaquetado/entrega
├─ QUANTUM_OA/
│  └─ PATTERNS/                   # Workflows de optimización
├─ SUPPLIERS/
│  └─ CRITERIA/                   # Requisitos de homologación
├─ policy/                        # Reglas (incl. política PLM)
├─ tests/                         # Marcos de prueba
├─ META.json                      # {"scope":"domain"}
└─ domain-config.yaml
```

### 2) Nivel Sistema (instancia ATA)

```
<DOMINIO>/SYSTEMS/ATA-XX_NOMBRE/
├─ INTEGRATION_VIEW.md            # Vista de integración del sistema
├─ INTERFACE_MATRIX/
│  └─ XX↔OTROS.csv                # Matriz de interfaces con otros ATA
├─ SUBSYSTEMS/
│  └─ ATA-XX-YY_SUBSYS/
│     ├─ README.md
│     ├─ DELs/
│     │  ├─ EASA-submissions/ MoC/ reports/
│     │  └─ README.md
│     ├─ PAx/
│     │  ├─ ONB/ OUT/
│     │  └─ README.md
│     ├─ PLM/                     # **Artefactos reales SOLO aquí**
│     │  ├─ EBOM_LINKS.md
│     │  └─ CAx/
│     │     ├─ CAD/  ├─ CAE/  ├─ CAO/  ├─ CAM/
│     │     ├─ CAI/  ├─ CAV/  ├─ CAP/  ├─ CAS/  └─ CMP/
│     ├─ PROCUREMENT/VENDORSCOMPONENTS/
│     ├─ QUANTUM_OA/(LP|MILP|QUBO|QAOA…)
│     ├─ SUPPLIERS/(BIDS|SERVICES)/
│     ├─ policy/   ├─ tests/
│     ├─ META.json                # {"scope":"instance"}
│     └─ inherit.json             # Referencia a plantillas de dominio
```

> **CAx** = CAD, CAE, CAO, CAM, CAI, CAV, CAP, CAS, CMP.

---

## Mapeo completo de dominios ↔ ATA

Esta tabla muestra la distribución completa de los capítulos ATA (01-100) entre los 15 dominios de ingeniería. El dominio primario tiene responsabilidad principal; los secundarios son interfaces/coordinación.

> **Referencia completa**: Ver [ATA_MAPPING.csv](./ATA_MAPPING.csv) para la tabla completa en formato CSV procesable.

### Tabla de distribución ATA por dominio

| ATA | Nombre | Primario | Secundarios | Notas |
|-----|--------|----------|-------------|-------|
| 01 | Introduction | LIB | | Program/admin records |
| 04 | Airworthiness Limitations | LIB | | Limits & compliance records |
| 05 | Time Limits | LIB | | Servicing/intervals |
| 06 | Dimensions/Stations | AAA | | Geometry refs |
| 07 | Lifting/Shoring | IIF | | Industrial infra & facilities |
| 08 | Leveling/Weighing | LCC | | Ground control/measure |
| 09 | Surface Protection | DDD | | Drainage/anti-corrosion |
| 10 | Parking/Mooring | AAP | | Airport ops |
| 11 | Placards/Markings | CCC | | Cabin/cockpit labeling |
| 12 | Servicing | LIB | | Ground servicing policies |
| 14 | Hardware (Fasteners) | AAA | | Structural hardware |
| 15 | Noise/Vibration | EER | | Env conditions |
| 16 | Ground Support Equipment | IIS | | EGSE/MGSE specs |
| 21 | Air Conditioning | DDD | CCC, EER | Environmental control |
| 22 | Auto Flight | LCC | EDI | Autopilot/AFCS |
| 23 | Communications | LCC | EDI | Internal/external comms |
| 24 | Electrical Power | EEE | LCC, EDI, MEC | Gen/storage/distribution |
| 25 | Equipment & Furnishings | CCC | DDD, EEE | Cabin & monuments |
| 26 | Fire Protection | EER | EEE, LCC | Sensing/suppression/interlocks |
| 27 | Flight Controls | MEC | LCC | Mechanical primary |
| 28 | Fuel (incl. H₂) | PPP | EEE, DDD, EER | H₂ under 28 per rules |
| 29 | Hydraulic Power | MEC | EEE | Pumps/actuation |
| 30 | Ice & Rain Protection | DDD | EEE, CCC | Anti-ice/de-ice |
| 31 | Indicating/Recording | EDI | LCC, EEE | Displays/recorders |
| 32 | Landing Gear Systems | MEC | EEE, LCC, EER | LG + braking |
| 33 | Lights | EEE | CCC | External/internal lights |
| 34 | Navigation (Avionics) | EDI | LCC, EEE | Nav sensors & processing |
| 35 | Oxygen | CCC | EER, EEE | ECLSS oxygen |
| 36 | Pneumatic | MEC | DDD, EEE | Bleed/pneumatic |
| 37 | Vacuum | MEC | | If applicable |
| 38 | Water & Waste | EER | CCC, EEE | Circular systems (water loop) |
| 39 | Electrical Panels | EEE | | Distribution panels |
| 41 | Water Ballast | DDD | | If applicable |
| 42 | Integrated Modular Avionics | EDI | LCC, EEE | ARINC 653/IMA platform |
| 43 | Cabin Systems | CCC | LCC, EEE | IFE, seats control |
| 44 | Cabin Control | LCC | CCC | Control layer |
| 45 | Central Maintenance | LCC | EDI, EEE | CMS/ACMS/health |
| 46 | Information Systems | IIS | EDI, EEE | IT/ground links |
| 47 | Inert Gas/Cryo (NGS/H₂ aux) | CQH | PPP, EEE | NGS & cryo adjuncts |
| 49 | APU | PPP | EEE, MEC, DDD | Aux power |
| 50 | Cargo & Load Systems | CCC | AAA | Freighter/combi hardware |
| 51 | Structures—General | AAA | | Std practices—structures |
| 52 | Doors | AAA | MEC, EEE | All doors/hatches |
| 53 | Fuselage Structures | AAA | | Primary structure |
| 54 | Nacelles & Pylons | AAA | PPP | AAA for structure; PPP for internals |
| 55 | Stabilizers | AAA | | H/V tails |
| 56 | Windows | AAA | | Cockpit/cabin |
| 57 | Wings | AAA | | Primary structure |
| 60 | Propeller—Practices | PPP | | If applicable |
| 61 | Propellers | PPP | | If applicable |
| 62 | Main Rotor | AAA | MEC | Rotary-wing |
| 63 | Main Rotor Drive | MEC | AAA | Rotary-wing |
| 64 | Tail Rotor | AAA | MEC | Rotary-wing |
| 65 | Tail Rotor Drive | AAA | MEC | Rotary-wing |
| 66 | Folding Blades/Supports | AAA | | Rotary-wing |
| 67 | Rotors Flight Control | MEC | LCC | Rotary-wing |
| 70 | Powerplant Practices | PPP | | General powerplant |
| 71 | Power Plant | PPP | EEE, MEC | Engine installation |
| 72 | Engine | PPP | EEE | Core/fan/EM |
| 73 | Engine Fuel & Control | PPP | EEE, LCC | FADEC software WITH 73 |
| 74 | Ignition | EEE | PPP | Igniters/exciters |
| 75 | Engine Bleed Air | PPP | DDD, MEC | Bleed interfaces |
| 76 | Engine Controls | LCC | PPP | Command/distribution |
| 77 | Engine Indicating | EDI | PPP | EIU/EICAS |
| 78 | Exhaust | PPP | EER | Noise/emissions interface |
| 79 | Oil (Lubrication) | MEC | PPP | Oil systems |
| 80 | Starting | EEE | PPP | Start & SGs |
| 81 | Turbines (Aux) | PPP | | If applicable |
| 82 | Water Injection | PPP | | If applicable |
| 83 | Accessory Gearboxes | MEC | PPP | Accessories drive |
| 84 | Propulsion Augmentation | EDI | PPP | FADEC adj/elec prop (if used) |
| 85 | Emissions/Environmental | EER | PPP | Non-propulsion EMC/EMI here; propulsion EMC with PPP(78) |
| 91 | Charts/Performance | IIS | EDI | Perf data |
| 92 | EWIS (Wiring) | EEE | ALL | **Only wiring here** (authoritative) |
| 93 | Central Control Systems | LCC | EDI | Supervisory/coord |
| 94 | E/E Compartments | EDI | EEE | Racks/bays |

### Capítulos reservados/plantillas (OOO)

Los siguientes capítulos están reservados para uso futuro, templates de plataforma, o aplicaciones spacecraft:

- **02, 03**: Operations, Support (Platform/reserved)
- **13**: General Hardware (Common practices/templates)
- **17-20**: Propeller chapters, Standard Practices (Reserved if N/A, templates)
- **40**: Avionics Std/General (Platform templates)
- **48**: Optical/Video (Templates; spacecraft uses)
- **58-59**: Flight Compartment Equip/Furnishings (Reserved/templates, spacecraft docking/robotics uses)
- **68-69**: Reserved (Rotorcraft)
- **86-87**: Planetary Protection/Env, Radiation Effects (Spacecraft use)
- **88-90**: Reserved, Space Traffic/Conjunction (Spacecraft use)
- **95-99**: Reserved
- **100**: General (Repository/meta templates)

### Resumen por dominio (ATA primarios)

* **AAA — Airframes, Aerodynamics, Airworthiness** → 06, 14, 51-57, 62, 64-66
* **PPP — Propulsion, Fuel Systems** → 28, 49, 60-61, 70-73, 75, 78, 81-82
* **MEC — Mechanical Systems, Modules** → 27, 29, 32, 36-37, 63, 67, 79, 83
* **LCC — Linkages, Control, Communications** → 08, 22-23, 44-45, 76, 93
* **EDI — Electronics, Digital Instruments** → 31, 34, 42, 77, 84, 94
* **EEE — Electrical, Endotransponders, Circulation** → 24, 33, 39, 74, 80, 92
* **EER — Environmental, Emissions, Remediation** → 15, 26, 38, 85
* **DDD — Drainage, Dehumidification, Drying** → 09, 21, 30, 41
* **CCC — Cockpit, Cabin, Cargo** → 11, 25, 35, 43, 50
* **IIS — Information, Intelligence Systems** → 16, 46, 91
* **LIB — Logistics, Inventory, Blockchain** → 01, 04-05, 12
* **AAP — Airport Adaptable Platforms** → 10
* **CQH — Cryogenics, Quantum, H2** → 47
* **IIF — Industrial Infrastructure, Facilities** → 07
* **OOO — OS, Ontologies, Office** → 02-03, 13, 17-20, 40, 48, 58-59, 68-69, 86-90, 95-100

---

## Ejemplos representativos (con SUBSYSTEMS + PLM) — Todos los dominios

Los siguientes sistemas demuestran la estructura para los 15 dominios:

### AAA — 53 FUSELAGE STRUCTURES

```
AAA-.../SYSTEMS/53-FUSELAGE-STRUCTURES/
├─ INTEGRATION_VIEW.md
├─ INTERFACE_MATRIX/53↔OTROS.csv
└─ SUBSYSTEMS/
   └─ 53-10_CENTER-BODY/
      └─ PLM/CAx/(CAD|CAE|CAM|…)
```

### PPP — 71 POWER PLANT

```
PPP-.../SYSTEMS/71-POWER-PLANT/
├─ INTEGRATION_VIEW.md
├─ INTERFACE_MATRIX/71↔OTROS.csv
└─ SUBSYSTEMS/
   └─ 71-00_GENERAL/
      └─ PLM/CAx/…
```

### MEC — 32 LANDING GEAR

```
MEC-.../SYSTEMS/32-LANDING-GEAR-SYSTEMS/
├─ INTEGRATION_VIEW.md
├─ INTERFACE_MATRIX/32↔OTROS.csv
└─ SUBSYSTEMS/
   └─ 32-10_MAIN-GEAR/
      └─ PLM/CAx/…
```

### LCC — 22 AUTO FLIGHT

```
LCC-.../SYSTEMS/22-AUTO-FLIGHT/
├─ INTEGRATION_VIEW.md
├─ INTERFACE_MATRIX/22↔OTROS.csv
└─ SUBSYSTEMS/
   └─ 22-10_AUTOPILOT/
      └─ PLM/CAx/…
```

### EDI — 34 NAVIGATION AVIONICS

```
EDI-.../SYSTEMS/34-NAVIGATION-AVIONICS/
├─ INTEGRATION_VIEW.md
├─ INTERFACE_MATRIX/34↔OTROS.csv
└─ SUBSYSTEMS/
   └─ 34-20_AHRS_IRS_GNSS/
      └─ PLM/CAx/…
```

### EEE — 24 ELECTRICAL POWER

```
EEE-.../SYSTEMS/24-ELECTRICAL-POWER/
├─ INTEGRATION_VIEW.md
├─ INTERFACE_MATRIX/24↔OTROS.csv
└─ SUBSYSTEMS/
   └─ 24-40_DISTRIBUTION/
      └─ PLM/CAx/…
```

### EER — 26 FIRE PROTECTION

```
EER-.../SYSTEMS/26-FIRE-PROTECTION/
├─ INTEGRATION_VIEW.md
├─ INTERFACE_MATRIX/26↔OTROS.csv
└─ SUBSYSTEMS/
   └─ 26-10_DETECTION/
      └─ PLM/CAx/…
```

### DDD — 21 AIR CONDITIONING

```
DDD-.../SYSTEMS/21-AIR-CONDITIONING/
├─ INTEGRATION_VIEW.md
├─ INTERFACE_MATRIX/21↔OTROS.csv
└─ SUBSYSTEMS/
   └─ 21-10_SYSTEM/
      └─ PLM/CAx/…
```

### CCC — 25 EQUIPMENT & FURNISHINGS

```
CCC-.../SYSTEMS/25-EQUIPMENT-FURNISHINGS/
├─ INTEGRATION_VIEW.md
├─ INTERFACE_MATRIX/25↔OTROS.csv
└─ SUBSYSTEMS/
   └─ 25-50_CABIN_INTERIORS/
      └─ PLM/CAx/…
```

### IIS — 46 INFORMATION SYSTEMS

```
IIS-.../SYSTEMS/46-INFORMATION-SYSTEMS/
├─ INTEGRATION_VIEW.md
├─ INTERFACE_MATRIX/46↔OTROS.csv
└─ SUBSYSTEMS/
   └─ 46-10_NETWORK/
      └─ PLM/CAx/…
```

### LIB — 05 TIME LIMITS

```
LIB-.../SYSTEMS/05-TIME-LIMITS/
├─ INTEGRATION_VIEW.md
├─ INTERFACE_MATRIX/05↔OTROS.csv
└─ SUBSYSTEMS/
   └─ 05-00_GENERAL/
      └─ PLM/CAx/…
```

### AAP — 10 PARKING & MOORING

```
AAP-.../SYSTEMS/10-PARKING-MOORING/
├─ INTEGRATION_VIEW.md
├─ INTERFACE_MATRIX/10↔OTROS.csv
└─ SUBSYSTEMS/
   └─ 10-00_GENERAL/
      └─ PLM/CAx/…
```

### CQH — 47 INERT GAS/CRYO

```
CQH-.../SYSTEMS/47-INERT-GAS-CRYO/
├─ INTEGRATION_VIEW.md
├─ INTERFACE_MATRIX/47↔OTROS.csv
└─ SUBSYSTEMS/
   └─ 47-10_NGS/
      └─ PLM/CAx/…
```

### IIF — 07 LIFTING & SHORING

```
IIF-.../SYSTEMS/07-LIFTING-SHORING/
├─ INTEGRATION_VIEW.md
├─ INTERFACE_MATRIX/07↔OTROS.csv
└─ SUBSYSTEMS/
   └─ 07-00_GENERAL/
      └─ PLM/CAx/…
```

### OOO — 13 GENERAL HARDWARE

```
OOO-.../SYSTEMS/13-GENERAL-HARDWARE/
├─ INTEGRATION_VIEW.md
├─ INTERFACE_MATRIX/13↔OTROS.csv
└─ SUBSYSTEMS/
   └─ 13-00_STANDARDS/
      └─ PLM/CAx/…
```

---

## Reglas CI (validación automática)

* `SYSTEMS/` **obligatorio** en todos los dominios.
* Cada `SYSTEMS/ATA-XX_*` debe contener:

  * `INTEGRATION_VIEW.md`
  * `INTERFACE_MATRIX/*.csv`
  * `SUBSYSTEMS/ATA-XX-YY_*/PLM/CAx/*`
* **Prohibido** `PLM/` con CAx en nivel dominio.
* Traza a CM: vínculos a `00-PROGRAM/CONFIG_MGMT` (ECR/ECO, baselines, ICDs).

---

## Notas de integración

* **ICDs**: referenciar `../../00-PROGRAM/CONFIG_MGMT/09-INTERFACES/`.
* **EWIS**: toda conectividad física en **ATA-92** (solo referencias desde matrices).
* **SW**: versiones junto a su **LRU host** (p.ej., FADEC en 73, particiones A653 en 42).

---

## Script de creación

Para generar la estructura inicial de dominios, utilice el script:

```bash
./scripts/create-domains.sh
```

Este script creará:
- Los 15 dominios con sus carpetas obligatorias
- **15 sistemas representativos** (uno por dominio) con subsistemas
- Toda la estructura PLM/CAx necesaria en cada subsistema

## Validación

Para validar que la estructura cumple con las reglas definidas:

```bash
./scripts/validate-structure.sh
```

El script de validación verifica:
- Presencia obligatoria de carpeta `SYSTEMS/` en cada dominio
- Estructura correcta de sistemas (INTEGRATION_VIEW.md, INTERFACE_MATRIX/)
- Estructura correcta de subsistemas (PLM/CAx con todas las carpetas)
- Ausencia de PLM/CAx a nivel dominio
- Formato correcto de archivos META.json y domain-config.yaml
