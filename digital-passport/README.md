# Aerospace Digital Passport Dashboard

A React-based digital passport platform for aerospace component traceability using UTCS manifests and TFA domains.

## Features

- **Digital Passport Dashboard**: Browse, search, and manage aerospace component digital passports
- **UTCS Manifest Viewer**: Display detailed UTCS manifests with checksum verification
- **TFA Domain Navigator**: Browse components organized by 15 canonical TFA domains
- **Lifecycle Phase Tracking**: Visualize component progression through 9 CAx phases
- **State Progression Monitor**: Track evidence through 6 states (QS → FWD → UE → FE → CB → QB)
- **Advanced Search & Filter**: Multi-faceted filtering by domain, phase, status, and more
- **Templates Library**: (Coming soon) Browsable repository of UTCS manifest templates

## Technology Stack

- **React 19** - Modern React with TypeScript
- **TypeScript** - Type-safe development
- **Tailwind CSS v4** - Utility-first styling with OKLCH colors
- **Vite** - Fast build tool and dev server
- **Spark KV API** - Browser-local persistent storage (mocked)

## Getting Started

### Prerequisites

- Node.js 18+ and npm

### Installation

```bash
npm install
```

### Development

```bash
npm run dev
```

Open [http://localhost:5173/digital-passport/](http://localhost:5173/digital-passport/) in your browser.

### Build

```bash
npm run build
```

The production build will be in the `dist/` directory.

### Preview

```bash
npm run preview
```

## Project Structure

```
digital-passport/
├── src/
│   ├── components/      # React components
│   ├── data/           # Seed data and fixtures
│   ├── hooks/          # Custom React hooks
│   ├── lib/            # Utilities and helpers
│   │   ├── constants.ts    # Domain names, colors, labels
│   │   └── kv.ts          # Spark KV storage mock
│   ├── types/          # TypeScript type definitions
│   ├── App.tsx         # Main application component
│   ├── index.css       # Global styles with Tailwind
│   └── main.tsx        # Application entry point
├── index.html          # HTML template
├── vite.config.ts      # Vite configuration
└── tsconfig.json       # TypeScript configuration
```

## Data Model

### Digital Passport
- Unique ID and UTCS reference
- Component type (hardware/software/firmware/model)
- TFA domain (15 domains: AAA through PPP)
- CAx lifecycle phase (9 phases: CAD through CAS)
- State progression (6 states: QS through QB)
- Verification status and anchoring flags

### TFA Domains
- **AAA**: Airframes-Aerodynamics-Airworthiness
- **AAP**: Airport-Adaptable-Platforms
- **CCC**: Cockpit-Cabin-Cargo
- **CQH**: Cryogenics-Quantum-H2
- **DDD**: Drainage-Dehumidification-Drying
- **EDI**: Electronics-Digital-Instruments
- **EEE**: Electrical-Endocircular-Energization
- **EER**: Environmental-Emissions-Remediation
- **IIF**: Industrial-Infrastructure-Facilities
- **IIS**: Information-Intelligence-Systems
- **LCC**: Linkages-Control-Communications
- **LIB**: Logistics-Inventory-Blockchain
- **MMM**: Mechanical-Material-Modules
- **OOO**: Operations-Optimization-Outcomes
- **PPP**: Propellers-Propellents-Propulsion

### State Flow
QS (Quantum Superposition) → FWD (Future/Waves Dynamics) → UE (Unit Element) → FE (Federation Entanglement) → CB (Classical Bit) → QB (Qubit)

## Design System

### Colors (OKLCH)
- **Primary**: Deep Aerospace Blue - `oklch(0.35 0.12 250)`
- **Secondary**: Titanium Gray - `oklch(0.55 0.01 260)`
- **Accent**: Verification Green - `oklch(0.65 0.15 145)`
- **Special**: Quantum Violet - `oklch(0.45 0.15 300)`

### Typography
- **Sans**: Inter (UI text)
- **Mono**: JetBrains Mono (code, IDs, hashes)

### Spacing
- Card padding: 24px
- Section gaps: 32px
- Content gaps: 16px

## License

Apache-2.0 - See LICENSE file

## Contact

- GitHub: [IDEALE-eu/IDEALEEU.EU](https://github.com/IDEALE-eu/IDEALEEU.EU)
- Website: [https://idealeeu.eu](https://idealeeu.eu)
