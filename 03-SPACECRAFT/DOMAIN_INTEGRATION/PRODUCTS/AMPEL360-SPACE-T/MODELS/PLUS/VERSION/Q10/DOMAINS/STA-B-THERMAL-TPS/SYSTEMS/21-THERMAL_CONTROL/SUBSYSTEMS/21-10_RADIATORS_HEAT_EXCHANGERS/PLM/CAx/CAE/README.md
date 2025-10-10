# CAE · 21-10_RADIATORS_HEAT_EXCHANGERS

Purpose: authoritative analysis artifacts for radiators, embedded heat-pipe radiators, LPHX, coldplates, mounts, TIMs. No source code.

## Deliverables
- Thermal network models (conductive/radiative), view-factor sets
- Orbital hot/cold balance cases, transient profiles
- Coldplate/LPHX hydraulic + pressure-drop models
- Structural FE for flatness/stiffness and mech loads
- Heater sizing and ∆T budgets; uncertainty/margin accounting
- Correlation packages to TVAC/leak/flow tests
- Release reports (PDF) with inputs, results, conclusions

## Layout
```
CAE/
├─ models/
│  ├─ tmm/                 # thermal math models (networks)
│  ├─ fem/                 # structural FE (flatness/stiffness)
│  └─ cfd/                 # flow/pressure (LPHX, channels)
├─ cases/
│  ├─ thermal_balance/     # hot/cold, worst-case, eclipse
│  ├─ transient/           # operational cycles, survival
│  └─ tvac/                # chamber configs (CAV linkage)
├─ loads_bcs/
│  ├─ heatloads/           # dissipation tables (W vs mode)
│  ├─ environments/        # sink, albedo, IR, β-angle sets
│  └─ interfaces/          # TIM k, contact h, clamps, mounts
├─ properties/
│  ├─ materials/           # k(T), c_p(T), ρ, CTE
│  ├─ coatings/            # α/ε vs angle/temp
│  └─ fluids/              # µ(T), ρ(T), k(T) for loops
├─ mesh/                   # meshes and quality reports
├─ runs/
│  ├─ input/               # solver decks
│  └─ output/              # raw results (kept by hash)
├─ post/
│  ├─ plots/               # PNG/PDF
│  ├─ tables/              # CSV/XLSX
│  └─ scripts/             # post-proc utilities
├─ correlation/            # test vs model deltas, factors
├─ reports/                # REL PDFs
└─ templates/              # case sheets, checklists
```

## Naming & revisions
`21-10-CAE_<object|case>__rNN__{WIP|RVW|REL}.*`  
Examples: `21-10-CAE-thermal_balance_hot__r03__RVW.tmm`, `21-10-CAE-coldplate_fem__r02__REL.fem`
