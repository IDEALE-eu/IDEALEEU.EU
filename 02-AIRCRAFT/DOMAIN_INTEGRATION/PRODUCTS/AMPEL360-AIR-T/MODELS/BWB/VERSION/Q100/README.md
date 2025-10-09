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

## Mapeo de dominios ↔ ATA (primarios)

* **AAA — Airframes, Aerodynamics, Airworthiness** → 06, 50, **51**, **52**, **53**, **54**(comp.), **55**, **56**, **57**
* **PPP — Propulsión, Combustible** → **28**, **49**, **54**(comp.), 60–61, 70–73, **75**, 78, 81–82
* **MEC — Mecánicos** → **27**, **29**, **32**, **36**–37, 63, 67, 79, 83
* **LCC — Enlaces/Control/Comms** → 08, **22**, 23, 44, 45, 76, 93
* **EDI — Electrónica/Aviónica/Indicadores** → **31**, **34**, **42**, **77**, 84, 94
* **EEE — Eléctricos/Luces/Arranque** → **24**, **33**, 39, 74, 80, 97
* **EER — Entorno/Emisiones** → 15, **26**, **38**, 85
* **DDD — Drenaje/Deshielo** → 09, **21**, **30**, 41
* **CCC — Cabina/Carga/Tripulación** → 11, **25**, **35**, 43, **50**
* **IIS — Información/IT** → 16, **46**, 91
* **LIB — Logística/Límites** → 01, 04, **05**, **12**
* **AAP — Operación en tierra** → **10**
* **CQH — Criogénicos/H2/NGS** → **47**
* **IIF — Infraestructura industrial** → **07**
* **OOO — OS/Ontologías/Reservas** → 13, 20 y capítulos reservados (plantillas)

---

## Ejemplos mínimos (con SUBSYSTEMS + PLM)

### AAA — 53 FUSELAGE STRUCTURES (ejemplo)

```
AAA-.../SYSTEMS/53-FUSELAGE-STRUCTURES/
├─ INTEGRATION_VIEW.md
├─ INTERFACE_MATRIX/53↔57_25_24_92.csv
└─ SUBSYSTEMS/
   └─ 53-10_CENTER-BODY/
      └─ PLM/CAx/(CAD|CAE|CAM|…)
```

### MEC — 32 LANDING GEAR

```
MEC-.../SYSTEMS/32-LANDING-GEAR-SYSTEMS/
├─ INTEGRATION_VIEW.md
├─ INTERFACE_MATRIX/32↔27_29_24_92.csv
└─ SUBSYSTEMS/
   └─ 32-10_MAIN_GEAR/
      └─ PLM/CAx/…
```

### EEE — 24 ELECTRICAL POWER

```
EEE-.../SYSTEMS/24-ELECTRICAL-POWER/
├─ INTEGRATION_VIEW.md                 # generación↔almacenamiento↔distribución
├─ INTERFACE_MATRIX/24↔28_29_36_42_45_46_92_33.csv
└─ SUBSYSTEMS/
   ├─ 24-20_BATTERIES/
   └─ 24-40_DISTRIBUTION/
      └─ PLM/CAx/…
```

### PPP — 71 POWER PLANT

```
PPP-.../SYSTEMS/71-POWER-PLANT/
├─ INTEGRATION_VIEW.md
├─ INTERFACE_MATRIX/71↔24_28_29_36_75_92.csv
└─ SUBSYSTEMS/
   └─ 71-00_GENERAL/
      └─ PLM/CAx/…
```

### EDI — 34 NAVIGATION

```
EDI-.../SYSTEMS/34-NAVIGATION-AVIONICS/
├─ INTEGRATION_VIEW.md
├─ INTERFACE_MATRIX/34↔22_24_31_42_45_92.csv
└─ SUBSYSTEMS/
   └─ 34-20_AHRS_IRS_GNSS/
      └─ PLM/CAx/…
```

### CCC — 25 EQUIPMENT & FURNISHINGS

```
CCC-.../SYSTEMS/25-EQUIPMENT-FURNISHINGS/
├─ INTEGRATION_VIEW.md
├─ INTERFACE_MATRIX/25↔21_38_24_33_50_92.csv
└─ SUBSYSTEMS/
   └─ 25-50_CABIN_INTERIORS/
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
- 6 sistemas de ejemplo con subsistemas
- Toda la estructura PLM/CAx necesaria

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
