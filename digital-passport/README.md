# Aerospace Digital Passport Dashboard

[![Demo](https://img.shields.io/badge/demo-live-0A7)](https://aerospace-digital-pa--Robbbo-T.github.app)
[![TypeScript](https://img.shields.io/badge/TypeScript-5.x-blue)](#technology-stack)
[![React](https://img.shields.io/badge/React-19-61dafb)](#technology-stack)
[![License](https://img.shields.io/badge/License-Apache--2.0-green)](#license)

> A React-based digital-passport platform for aerospace component traceability using **UTCS** manifests and **TFA** domains.

---

## Contents
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Getting Started](#getting-started)
- [Project Structure](#project-structure)
- [Data Model](#data-model)
  - [Digital Passport](#digital-passport)
  - [TFA Domains](#tfa-domains)
  - [State Flow](#state-flow)
- [Design System](#design-system)
- [Contributing](#contributing)
- [Security](#security)
- [License](#license)
- [Contact](#contact)

---

## Features
- **Digital Passport Dashboard**: Browse, search, and manage component passports
- **UTCS Manifest Viewer**: Render UTCS with checksum verification
- **TFA Domain Navigator**: 15 canonical domains
- **Lifecycle Phase Tracking**: 9 CAx phases
- **State Progression Monitor**: QS → FWD → UE → FE → CB → QB
- **Advanced Search & Filter**: Domain, phase, status, more
- **Templates Library**: *(Coming soon)* UTCS template browser

## Technology Stack
- **React 19** + **TypeScript**
- **Tailwind CSS v4** (OKLCH)
- **Vite**
- **Spark KV API** (browser-local mock)

---

## Getting Started

### Prerequisites
- Node.js **18+** and npm

### Install
```bash
npm install
````

### Dev

```bash
npm run dev
# open http://localhost:5173/digital-passport/
```

### Build

```bash
npm run build
# outputs to dist/
```

### Preview

```bash
npm run preview
```

> Tip: Serve under `/digital-passport/` base path in production (see `vite.config.ts`).

---

## Project Structure

```
digital-passport/
├─ src/
│  ├─ components/        # UI components
│  ├─ data/              # Seed data and fixtures
│  ├─ hooks/             # Custom hooks
│  ├─ lib/
│  │  ├─ constants.ts    # Domain names, colors, labels
│  │  └─ kv.ts           # Spark KV storage mock
│  ├─ types/             # Type definitions
│  ├─ App.tsx            # App shell
│  ├─ index.css          # Tailwind globals
│  └─ main.tsx           # Entry point
├─ index.html
├─ vite.config.ts
└─ tsconfig.json
```

---

## Data Model

### Digital Passport

* ID and UTCS reference
* Component type *(hardware/software/firmware/model)*
* **TFA domain** *(AAA…PPP)*
* **CAx phase** *(9 phases: CAD … CAS)*
* **State** *(QS → … → QB)*
* Verification status and anchoring flags

### TFA Domains

* **AAA** Airframes-Aerodynamics-Airworthiness
* **AAP** Airport-Adaptable-Platforms
* **CCC** Cockpit-Cabin-Cargo
* **CQH** Cryogenics-Quantum-H₂
* **DDD** Drainage-Dehumidification-Drying
* **EDI** Electronics-Digital-Instruments
* **EEE** Electrical-Endocircular-Energization
* **EER** Environmental-Emissions-Remediation
* **IIF** Industrial-Infrastructure-Facilities
* **IIS** Information-Intelligence-Systems
* **LCC** Linkages-Control-Communications
* **LIB** Logistics-Inventory-Blockchain
* **MMM** Mechanical-Material-Modules
* **OOO** Operations-Optimization-Outcomes *(OS, Ontologies, Office UIs)*
* **PPP** Propellers-Propellents-Propulsion

### State Flow

```
QS → FWD → UE → FE → CB → QB
```

---

## Design System

### Colors (OKLCH)

* **Primary**: Deep Aerospace Blue `oklch(0.35 0.12 250)`
* **Secondary**: Titanium Gray `oklch(0.55 0.01 260)`
* **Accent**: Verification Green `oklch(0.65 0.15 145)`
* **Special**: Quantum Violet `oklch(0.45 0.15 300)`

### Typography

* **Sans**: Inter
* **Mono**: JetBrains Mono

### Spacing

* Card padding **24px**
* Section gaps **32px**
* Content gaps **16px**

---

## Contributing

Issues and PRs welcome. Propose schema or UI changes via RFC in `/.github/ISSUE_TEMPLATE/` if present.

## Security

Report vulnerabilities to **[security@ideale-eu.org](mailto:security@ideale-eu.org)**. Do not open public issues.

## License

**Apache-2.0** — see `LICENSE`.

## Contact

* GitHub: [IDEALE-eu/IDEALEEU.EU](https://github.com/IDEALE-eu/IDEALEEU.EU)
* Website: [https://idealeeu.eu](https://idealeeu.eu)
* Demo: [https://aerospace-digital-pa--Robbbo-T.github.app](https://aerospace-digital-pa--Robbbo-T.github.app)

```
::contentReference[oaicite:0]{index=0}
```
