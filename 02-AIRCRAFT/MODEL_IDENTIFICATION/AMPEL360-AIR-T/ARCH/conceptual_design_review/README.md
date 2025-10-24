## Summary 

**Design case:** 100-seat blended-wing-body regional transport (Q100) — cruise M0.72 @ 35,000 ft, nominal mission range **1,500 nm (2,780 km)**, primary LH₂/fuel-cell + battery electric drive powering open-fans; SAF turbogenerator for peak/backup.

---

## Primary mission parameters

| Parameter                                        |                                                                 Value (nominal) | Notes / rationale                                                       |
| ------------------------------------------------ | ------------------------------------------------------------------------------: | ----------------------------------------------------------------------- |
| **Design passengers (nominal)**                  |                                                                     **100 pax** | 2-class layout example: 12 Biz + 88 Economy (see payload mixes).        |
| **Passenger mass (incl. carry/checked baggage)** |                                                                  **100 kg/pax** | 80 kg person + 20 kg checked + carry-on/contingency ≈100 kg for sizing. |
| **Nominal payload mass (100 pax)**               |                                                                   **10,000 kg** | 100 × 100 kg.                                                           |
| **Typical mission range (design)**               |                                                         **1,500 nm (2,780 km)** | Range with required regulatory fuel reserves (alternate + holding).     |
| **Short regional mission**                       |                                                           **800 nm (1,480 km)** | Typical 2-hour sectors.                                                 |
| **Ferry / max endurance (empty payload)**        |                                                        **~3,000 nm (5,560 km)** | Ferry with reduced payload and maximum LH₂/SAF ferry fuel.              |
| **Cruise speed**                                 |                                                 **M0.72 ≈ 430 KTAS ≈ 795 km/h** | Open-fan optimized, subsonic, high propulsive efficiency.               |
| **Cruise altitude (nominal)**                    |                                                        **35,000 ft (10,700 m)** | Operating band 30,000–38,000 ft depending on weight and ATC.            |
| **Design mission fuel/reserve policy**           | **Taxi + TO/Climb + Cruise + Alternate (75 nm) + 45 min holding + contingency** | Use this fuel law when sizing LH₂ and SAF turbogenerator capacity.      |

---

## Payload mixes (configurable mission layouts)

1. **Full passenger (standard)**

   * Passengers: **100 pax**
   * Payload mass: **10,000 kg**
   * Belly cargo: **~0–1,000 kg** (small bags / mail)

2. **Combi / mixed**

   * Passengers: **70 pax**
   * Passenger mass: **7,000 kg**
   * Cargo: **4,000 kg** (belly / palletized)
   * Total payload mass: **11,000 kg**

3. **High-density commuter**

   * Passengers: **110 pax** (single-class high density)
   * Payload mass: **11,000 kg**

4. **All-cargo (freighter conversion)**

   * Passengers: **0 pax**
   * Cargo payload: **12,000 kg** (contiguous cargo bay design target)
   * Use for express freight / ferryed cargo legs

> Design the airframe/cargo bay and door geometry to accommodate the “mixed” pallet/container set chosen (e.g., LD3 equivalents or flat pallets). Verify center-of-gravity envelopes for each mix.

---

## Operational notes & constraints

* **Reserves and dispatch:** The 1,500 nm design range assumes dispatch with alternate and 45-min holding reserves. For regulatory compliance, size the LH₂ tanks + SAF turbogenerator/fuel for this profile.
* **Open-fan role:** Electrically driven open-fans give high propulsive efficiency at M0.6–0.78. They are sized for cruise cruise power plus climb margin. Peak/sustained climb power can be supplemented by the SAF turbogenerator and battery.
* **SAF turbogenerator:** SAF is carried for turbogenerator operation (peak power, recharge, diversion). Design for safe dual-fuel operations and mission rules that prioritize LH₂ fuel-cell operation for cruise to minimize SAF consumption. SAF provides operational flexibility where LH₂ refueling is unavailable.
* **Cryogenic LH₂ tanks:** Include dry-mass penalty and boil-off allowance in trade studies. Tank mass reduces useful payload; include in weight & balance early.
* **Ground infrastructure:** Mission planning must consider LH₂ availability. For routes lacking LH₂, design a hybrid mission profile relying more on SAF turbogenerator with reduced LH₂.
* **Environmental goals:** Primary propulsion on LH₂ fuel cell minimizes CO₂. SAF use provides near-term operational capability and supply resilience during rollout of LH₂ infrastructure.

---

## Example sizing checkpoints to derive from these requirements

* LH₂ mass and tank volume to meet 1,500 nm mission + reserves.
* Battery energy for taxi, takeoff assist, reserve climb and brief diversion (sizing dependent on recharge strategy by SAF turbogenerator).
* Open-fan disk area and diameter for cruise thrust at M0.72 and cruise altitude.
* SAF tank mass/volume and turbogenerator power sufficient for peak clustering (takeoff/climb) and alternate scenarios.
* CG and cargo bay layout supporting the 4 payload mixes above.

---

### **Sizing Calculation: LH₂ Mass and Tank Volume for the 1,500 nm Mission**

This analysis derives the required liquid hydrogen (LH₂) fuel mass and the corresponding storage tank volume to meet the 1,500 nm design mission, including all specified reserves.

#### **1. Methodology & Key Assumptions**

The calculation follows an energy-based approach, determining the total energy required for the mission and then deriving the necessary fuel mass based on the energy density of LH₂ and the efficiency of the propulsion system.

| Parameter | Assumed Value | Rationale / Source |
| :--- | :--- | :--- |
| **Aircraft L/D Ratio (Cruise)** | **22** | Aggressive but plausible target for a clean, optimized Blended-Wing-Body configuration. |
| **Average Cruise Weight** | **50,000 kg** | Assumes an MTOW of ~55,000 kg, with the average weight during the cruise segment being lower. |
| **Overall Propulsion Efficiency** | **50%** | "Tank-to-Wake" efficiency. This is a chain of: FC (60%) x Power Dist. (98%) x Motor Controller (97%) x Motor (96%) x Open-Fan Propulsor (92%) ≈ 50%. |
| **LH₂ Energy Density (LHV)** | **120 MJ/kg** | Standard lower heating value for hydrogen. |
| **Mission Fuel Reserve Factor** | **1.30 (30%)** | Represents the energy required for the alternate airport (75 nm), 45-minute holding, and contingency, expressed as a factor on the primary cruise energy. |
| **Liquid Hydrogen (LH₂) Density** | **70.8 kg/m³** | Standard density for LH₂ at its boiling point (20 K). |
| **Cryo-Tank Gravimetric Efficiency** | **55%** | Assumes that the LH₂ fuel mass constitutes 55% of the total tank system mass (including tank structure, insulation, valves, pumps, etc.). |
| **Tank Ullage Requirement** | **15%** | Non-fuel volume required for fuel gauging, thermal expansion, and boil-off gas management. |

#### **2. Calculation Steps**

**Step 1: Calculate Cruise Thrust Required**
The aircraft must generate enough thrust to overcome drag at cruise.
*   `Drag = Weight / (L/D)`
*   Average Weight Force = 50,000 kg × 9.81 m/s² = 490,500 N
*   **Cruise Thrust** = 490,500 N / 22 = **22,300 N (22.3 kN)**

**Step 2: Calculate Propulsive Power Required**
This is the power delivered by the open-fans to the air.
*   `Cruise Speed = M0.72 @ 35,000 ft` ≈ 215 m/s (774 km/h)
*   `Power_propulsive = Thrust × Velocity`
*   **Propulsive Power** = 22,300 N × 215 m/s = 4,794,500 W ≈ **4.80 MW**

**Step 3: Calculate Electrical Power Required from Fuel Cells**
This is the power the fuel cells must generate, accounting for powertrain losses.
*   `Power_electrical = Power_propulsive / Overall Propulsion Efficiency`
*   **Electrical Power** = 4.80 MW / 0.50 = **9.60 MW**

**Step 4: Calculate Total Energy for the Mission (with reserves)**
*   `Mission Duration = Range / Speed` = 2,780 km / 774 km/h ≈ **3.6 hours** (12,960 seconds)
*   `Cruise Energy = Power_electrical × Mission Duration` = 9.6 MJ/s × 12,960 s = 124,416 MJ
*   `Total Energy Required = Cruise Energy × Reserve Factor` = 124,416 MJ × 1.30 = 161,740 MJ
*   **Total Energy Required** ≈ **162,000 MJ**

**Step 5: Calculate Required LH₂ Fuel Mass**
*   `LH₂ Mass = Total Energy Required / LH₂ Energy Density`
*   **LH₂ Mass** = 162,000 MJ / 120 MJ/kg = **1,350 kg**

**Step 6: Calculate Total LH₂ System Mass**
This includes the tankage and systems required to store the fuel.
*   `System Mass = LH₂ Mass / Gravimetric Efficiency`
*   **Total System Mass** = 1,350 kg / 0.55 ≈ **2,455 kg**

**Step 7: Calculate Required LH₂ Tank Volume**
*   `LH₂ Liquid Volume = LH₂ Mass / LH₂ Density` = 1,350 kg / 70.8 kg/m³ = **19.1 m³**
*   `Total Tank Volume (incl. ullage) = Liquid Volume × (1 + Ullage Requirement)`
*   **Total Tank Volume** = 19.1 m³ × 1.15 ≈ **22.0 m³**

#### **3. Summary of Results**

| Sizing Parameter | Calculated Value | Notes |
| :--- | :--- | :--- |
| **Required LH₂ Fuel Mass** | **1,350 kg** | To complete the 1,500 nm mission plus all regulatory reserves. |
| **Total LH₂ Storage System Mass** | **~2,450 kg** | Fuel (1,350 kg) + Tankage/Systems (1,100 kg). A significant weight item. |
| **Required Internal Tank Volume** | **~22 m³** | This is the internal geometric volume needed to house the 1,350 kg of LH₂ plus ullage. |

#### **4. Discussion & Implications**

*   **Volumetric Challenge:** A required tank volume of **22 cubic meters** is substantial. This is equivalent to the interior volume of a 20-foot shipping container. This calculation underscores why a **Blended-Wing-Body is an ideal candidate** for LH₂ storage, as its voluminous center body can accommodate large, non-cylindrical tanks more efficiently than a traditional tube-and-wing aircraft.
*   **Weight Impact:** The total LH₂ system mass of ~2,450 kg represents a major component of the aircraft's Operating Empty Weight (OEW) and must be carefully managed in the weight & balance budget.
*   **Sensitivity:** This result is highly sensitive to the assumed L/D ratio and propulsion efficiency. A 10% decrease in either parameter would increase the required fuel mass by over 100 kg. These assumptions must be validated through CFD, wind tunnel testing, and powertrain rig testing.
*   **System Sizing:** This 1,350 kg LH₂ budget provides the primary input for the detailed design of the cryogenic tanks, fuel lines, pumps, and thermal management system. It also informs the sizing of the SAF tank, which must hold enough fuel for the turbogenerator to cover the energy needs of the 75 nm diversion and 45-minute hold.


### Cabin configurations

Below are two ready-to-use cabin-layout options for **BWB-H2-HY-E Q100**: a **100-seat two-class** and a **110-seat high-density single-class**. Each layout gives seat arrangement, seat pitch, cabin geometry estimates, emergency-exit plan and placement rationale so you can drop them into sizing, weight & balance and evacuation studies.

---

# 1) 100-seat — Two-class (12 Biz + 88 Economy) — **Design intent**

Business class for premium pax and short-haul comfort. Economy optimized for 3-3 abreast (common regional arrangement) to keep aisle counts low and boarding simple.

**Summary**

* Total seats: **100** (Business 12, Economy 88)
* Cabin type: two-aisle effective layout (BWB allows two continuous aisles flanking the center)
* Nominal cabin width (clear usable): **8.0 m** (allows 4-abreast in biz and 6-abreast in economy with service lanes)
* Nominal cabin length (approx): **~22.5 m**

**Business (front section)**

* Seats: **1-2-1** abreast (4 across), **3 rows** → 12 seats.
* Seat pitch: **38 in (965 mm)**.
* Seat width: **20 in (510 mm)** typical for premium.
* Aisles: two aisles, each **≥ 0.50 m** wide for service and egress.
* Galley/service: forward galley directly forward of Row 1 (2.0–3.0 m).

**Economy (main cabin)**

* Seats: **3-3** abreast (6 across).
* Rows: **15 rows** × 6 = 90 seats. To reach 88 economy, two seats can be deleted or used as service/crew seats to achieve exactly 88: practical layout uses 15 rows with two pitch adjustments to meet mass/CG. (You can also set 14 rows + 2 bulkhead/extra seats.)
* Seat pitch: **31 in (787 mm)** standard; can be relaxed to 32 in for higher comfort.
* Seat width: **17.5 in (445 mm)**.
* Economy aisles: two aisles of **0.45–0.50 m** each.

**Doors & emergency exits (evacuation goal: 90 s with half exits blocked)**

* **Total exits proposed: 6 main exits (paired left/right):** Forward pair (L/R) near row 2, Mid pair (L/R) at economy forward-mid (near row 7–8), Aft pair (L/R) near after last economy row.
* Exit spacing: distribute roughly every **~7–8 m** along cabin centerline so no passenger is beyond comfortable walking distance to nearest exit.
* Exit width/type: design to meet regulatory capacity (provisionally Type I/large exits for main pairs). Overwing exits not required with distributed large side exits on BWB.
* Evacuation aisles: aisles width and exit spacing sized to meet evacuation flow. Confirm with evacuation simulation (mass flow rates and 90 s check).

**Lavatories / galleys / service**

* Forward galley and service area ahead of business.
* One or two lavatories aft of economy cluster (2–3 lavs), and crew rest / service area near rear.
* Service carts stored in dedicated stowage adjacent to galley zones.

**Approximate longitudinal layout (forward → aft)**
`Flight deck (cockpit) | Fwd galley | Biz (3 rows 1-2-1) | Divider / service | Economy (15 rows 3-3) | Aft galley / lavs | tail / systems`
Estimated cabin useful length breakdown: forward galley 3 m | biz 4 m | transition/service 1.5 m | economy 11.8 m | aft services 2.2 m = ~22.5 m.

**Rationale / notes**

* 1-2-1 business gives direct aisle access for all premium seats and uses BWB wide floorplate efficiently.
* 3-3 economy minimizes number of aisles to two and keeps boarding/serving operations efficient.
* Six side exits (three pairs) is conservative for 100 pax and intended to meet 90-s evacuation with half exits blocked; confirm with full evacuation analysis per CS-25 / FAR rules.

---

# 2) 110-seat — High-density single-class — **Design intent**

Maximize seat count while keeping comfort tolerable for short-to-medium range. Single class, tighter pitch, more abreast seats using BWB wide planform.

**Summary**

* Total seats: **110** (single class)
* Cabin type: **single-class, 2-aisle (2+4+2 = 8 abreast)** typical wide-but-compact arrangement for high density in a wide interior.
* Nominal cabin width (clear usable): **9.0 m** (enables 8 abreast comfortably)
* Nominal cabin length (approx): **~23.5 m**

**Seating block**

* Configuration: **2-4-2** abreast (8 across) — two side banks of 2, center block of 4. This keeps two aisles and center block dense but serviceable.
* Rows: **14 rows** × 8 = **112 seats**. To reach exactly 110, remove 2 seats as required (e.g., convert 2 seats to service/crew or slightly fewer rows).
* Seat pitch: **29 in (737 mm)** (tight, common in high density single class). Consider 30 in (762 mm) as comfort compromise.
* Seat width: **17 in (430 mm)**.
* Aisles: two aisles each **≥ 0.50 m**, preferable **0.51–0.56 m** for fast circulation on dense flights.

**Doors & emergency exits**

* **Total exits proposed: 8 main exits (four pairs L/R):** Forward pair near row 2, Forward-mid pair near row 6, Aft-mid pair near row 10, Aft pair near row 14. Even longitudinal spacing reduces maximum walking distance.
* This exit count and placement are conservative for 110 pax and intended to satisfy 90-second evacuation with half exits blocked. Validate with evacuation model (placement, slide deployment times, aisle width, seat egress times).
* Consider supplementing with two overwing escape hatches if required by certification route or for additional redundancy.

**Lavatories / galleys / service**

* Forward galley and small rear galley. Two lavatories in aft area plus one or two mid-cabin crew lavs if needed.
* Bulkheads for galley modules designed into forward and aft service zones.

**Approximate longitudinal layout**
`Cockpit | Forward galley | Main cabin rows (14 rows 2-4-2) | Aft galley / lavs | systems`
Estimated useful length: forward galley 3 m | cabin rows (14 × 0.737 m) ≈ 10.3 m | service zones 3.2 m | allowances and spacing ≈ 7 m → total ~23.5 m.

**Rationale / notes**

* 2-4-2 is an efficient balance: two aisles for egress and service, high seat count per row, simpler service logistics than 3-3-3 or 3-4-3.
* Tight pitch 29 in recommended only for short/medium sectors. For longer range missions increase pitch to 30–31 in.
* Eight exits (four pairs) give redundancy and short walking distances — sensible for dense layout. Evacuation proofing mandatory.

---

# Emergency-exit placement guidance (common rules for both layouts)

1. Spread exits so longitudinal distance to nearest usable exit is minimized. Aim for exit nodes every **6–8 m** along cabin centerline for these cabin lengths.
2. Place a **pair of main doors** (left/right) at forward service area (typical L1/R1). Additional pairs mid and aft. BWB planform allows flush exits left and right inboard of the outer wing/fuselage intersections.
3. Design exit widths, steps/slides and clearances to meet evacuation throughput; design aisles and cross-passages to avoid chokepoints near galleys.
4. Provide clear escape path markings, lighting and floor lighting. Validate with evacuation simulation (90 s criterion) with half-exits blocked scenarios per certification.
5. Ensure egress loads consider children/elderly and carry-on interference; in dense configs add aisle width margin.

---

# Additional items to use directly in CAD/PLM/CAE

* **Seat coordinate table**: produce X (fore→aft), Y (left→right) coordinates per row from the layouts above for quick import into CAD. I can generate that CSV if you want.
* **Mass & CG input**: attach seat mass and average passenger mass (100 kg/pax as earlier) to each seat row for CG envelope calculations.
* **Evacuation input**: prepare an evacuation scenario set (90 s, half exits blocked, typical passenger delay distribution) for agent-based evacuation model. I can generate a template.
* **Accessibility & service**: allocate 1–2 dedicated wheelchair / PRM spaces (forward or aft) and stowage with accessible door proximity.

---



* Below are two **row-by-row Markdown tables** ready for CAD import.
Units: **X, Y in millimetres (mm)**. Origin **X = 0** at forward cabin bulkhead (aft face of forward galley). Y = 0 at cabin centerline.
**Mass** column gives *passenger + carry baggage* mass = **100 kg** (use seat mass as separate metadata if needed).

---

## 100-seat layout — Two-class (12 Business + 88 Economy)

**Geometry constants**

* Forward galley length = **3000 mm**
* Business pitch = **965 mm** (3 rows)
* Transition length after business = **1500 mm**
* Economy pitch = **787 mm** (15 rows; last row reduced to 4 seats)
* Business Y columns (4 abreast L→R): **-2000, -600, 600, 2000** (mm)
* Economy Y columns (2-2-2 L→R): **-2100, -1400, -300, 300, 1400, 2100** (mm)

**Business row centers (X, mm)**
Row B1: **3482.5**
Row B2: **4447.5**
Row B3: **5412.5**

**Economy row centers (X, mm)** (rows E4–E18)
E4 7306.0, E5 8093.0, E6 8880.0, E7 9667.0, E8 10454.0,
E9 11241.0, E10 12028.0, E11 12815.0, E12 13602.0, E13 14389.0,
E14 15176.0, E15 15963.0, E16 16750.0, E17 17537.0, E18 18324.0

**Table: 100-seat (each line = 1 seat)**

| Row | SeatID | Class    |  X (mm) | Y (mm) | Passenger_mass (kg) |
| --: | :----- | :------- | ------: | -----: | ------------------: |
|  B1 | 1A     | Business |  3482.5 |  -2000 |                 100 |
|  B1 | 1B     | Business |  3482.5 |   -600 |                 100 |
|  B1 | 1C     | Business |  3482.5 |    600 |                 100 |
|  B1 | 1D     | Business |  3482.5 |   2000 |                 100 |
|  B2 | 2A     | Business |  4447.5 |  -2000 |                 100 |
|  B2 | 2B     | Business |  4447.5 |   -600 |                 100 |
|  B2 | 2C     | Business |  4447.5 |    600 |                 100 |
|  B2 | 2D     | Business |  4447.5 |   2000 |                 100 |
|  B3 | 3A     | Business |  5412.5 |  -2000 |                 100 |
|  B3 | 3B     | Business |  5412.5 |   -600 |                 100 |
|  B3 | 3C     | Business |  5412.5 |    600 |                 100 |
|  B3 | 3D     | Business |  5412.5 |   2000 |                 100 |
|  E4 | 4A     | Economy  |  7306.0 |  -2100 |                 100 |
|  E4 | 4B     | Economy  |  7306.0 |  -1400 |                 100 |
|  E4 | 4C     | Economy  |  7306.0 |   -300 |                 100 |
|  E4 | 4D     | Economy  |  7306.0 |    300 |                 100 |
|  E4 | 4E     | Economy  |  7306.0 |   1400 |                 100 |
|  E4 | 4F     | Economy  |  7306.0 |   2100 |                 100 |
|  E5 | 5A     | Economy  |  8093.0 |  -2100 |                 100 |
|  E5 | 5B     | Economy  |  8093.0 |  -1400 |                 100 |
|  E5 | 5C     | Economy  |  8093.0 |   -300 |                 100 |
|  E5 | 5D     | Economy  |  8093.0 |    300 |                 100 |
|  E5 | 5E     | Economy  |  8093.0 |   1400 |                 100 |
|  E5 | 5F     | Economy  |  8093.0 |   2100 |                 100 |
|  E6 | 6A     | Economy  |  8880.0 |  -2100 |                 100 |
|  E6 | 6B     | Economy  |  8880.0 |  -1400 |                 100 |
|  E6 | 6C     | Economy  |  8880.0 |   -300 |                 100 |
|  E6 | 6D     | Economy  |  8880.0 |    300 |                 100 |
|  E6 | 6E     | Economy  |  8880.0 |   1400 |                 100 |
|  E6 | 6F     | Economy  |  8880.0 |   2100 |                 100 |
|  E7 | 7A     | Economy  |  9667.0 |  -2100 |                 100 |
|  E7 | 7B     | Economy  |  9667.0 |  -1400 |                 100 |
|  E7 | 7C     | Economy  |  9667.0 |   -300 |                 100 |
|  E7 | 7D     | Economy  |  9667.0 |    300 |                 100 |
|  E7 | 7E     | Economy  |  9667.0 |   1400 |                 100 |
|  E7 | 7F     | Economy  |  9667.0 |   2100 |                 100 |
|  E8 | 8A     | Economy  | 10454.0 |  -2100 |                 100 |
|  E8 | 8B     | Economy  | 10454.0 |  -1400 |                 100 |
|  E8 | 8C     | Economy  | 10454.0 |   -300 |                 100 |
|  E8 | 8D     | Economy  | 10454.0 |    300 |                 100 |
|  E8 | 8E     | Economy  | 10454.0 |   1400 |                 100 |
|  E8 | 8F     | Economy  | 10454.0 |   2100 |                 100 |
|  E9 | 9A     | Economy  | 11241.0 |  -2100 |                 100 |
|  E9 | 9B     | Economy  | 11241.0 |  -1400 |                 100 |
|  E9 | 9C     | Economy  | 11241.0 |   -300 |                 100 |
|  E9 | 9D     | Economy  | 11241.0 |    300 |                 100 |
|  E9 | 9E     | Economy  | 11241.0 |   1400 |                 100 |
|  E9 | 9F     | Economy  | 11241.0 |   2100 |                 100 |
| E10 | 10A    | Economy  | 12028.0 |  -2100 |                 100 |
| E10 | 10B    | Economy  | 12028.0 |  -1400 |                 100 |
| E10 | 10C    | Economy  | 12028.0 |   -300 |                 100 |
| E10 | 10D    | Economy  | 12028.0 |    300 |                 100 |
| E10 | 10E    | Economy  | 12028.0 |   1400 |                 100 |
| E10 | 10F    | Economy  | 12028.0 |   2100 |                 100 |
| E11 | 11A    | Economy  | 12815.0 |  -2100 |                 100 |
| E11 | 11B    | Economy  | 12815.0 |  -1400 |                 100 |
| E11 | 11C    | Economy  | 12815.0 |   -300 |                 100 |
| E11 | 11D    | Economy  | 12815.0 |    300 |                 100 |
| E11 | 11E    | Economy  | 12815.0 |   1400 |                 100 |
| E11 | 11F    | Economy  | 12815.0 |   2100 |                 100 |
| E12 | 12A    | Economy  | 13602.0 |  -2100 |                 100 |
| E12 | 12B    | Economy  | 13602.0 |  -1400 |                 100 |
| E12 | 12C    | Economy  | 13602.0 |   -300 |                 100 |
| E12 | 12D    | Economy  | 13602.0 |    300 |                 100 |
| E12 | 12E    | Economy  | 13602.0 |   1400 |                 100 |
| E12 | 12F    | Economy  | 13602.0 |   2100 |                 100 |
| E13 | 13A    | Economy  | 14389.0 |  -2100 |                 100 |
| E13 | 13B    | Economy  | 14389.0 |  -1400 |                 100 |
| E13 | 13C    | Economy  | 14389.0 |   -300 |                 100 |
| E13 | 13D    | Economy  | 14389.0 |    300 |                 100 |
| E13 | 13E    | Economy  | 14389.0 |   1400 |                 100 |
| E13 | 13F    | Economy  | 14389.0 |   2100 |                 100 |
| E14 | 14A    | Economy  | 15176.0 |  -2100 |                 100 |
| E14 | 14B    | Economy  | 15176.0 |  -1400 |                 100 |
| E14 | 14C    | Economy  | 15176.0 |   -300 |                 100 |
| E14 | 14D    | Economy  | 15176.0 |    300 |                 100 |
| E14 | 14E    | Economy  | 15176.0 |   1400 |                 100 |
| E14 | 14F    | Economy  | 15176.0 |   2100 |                 100 |
| E15 | 15A    | Economy  | 15963.0 |  -2100 |                 100 |
| E15 | 15B    | Economy  | 15963.0 |  -1400 |                 100 |
| E15 | 15C    | Economy  | 15963.0 |   -300 |                 100 |
| E15 | 15D    | Economy  | 15963.0 |    300 |                 100 |
| E15 | 15E    | Economy  | 15963.0 |   1400 |                 100 |
| E15 | 15F    | Economy  | 15963.0 |   2100 |                 100 |
| E16 | 16A    | Economy  | 16750.0 |  -2100 |                 100 |
| E16 | 16B    | Economy  | 16750.0 |  -1400 |                 100 |
| E16 | 16C    | Economy  | 16750.0 |   -300 |                 100 |
| E16 | 16D    | Economy  | 16750.0 |    300 |                 100 |
| E16 | 16E    | Economy  | 16750.0 |   1400 |                 100 |
| E16 | 16F    | Economy  | 16750.0 |   2100 |                 100 |
| E17 | 17A    | Economy  | 17537.0 |  -2100 |                 100 |
| E17 | 17B    | Economy  | 17537.0 |  -1400 |                 100 |
| E17 | 17C    | Economy  | 17537.0 |   -300 |                 100 |
| E17 | 17D    | Economy  | 17537.0 |    300 |                 100 |
| E17 | 17E    | Economy  | 17537.0 |   1400 |                 100 |
| E17 | 17F    | Economy  | 17537.0 |   2100 |                 100 |
| E18 | 18A    | Economy  | 18324.0 |  -2100 |                 100 |
| E18 | 18B    | Economy  | 18324.0 |  -1400 |                 100 |
| E18 | 18E    | Economy  | 18324.0 |   1400 |                 100 |
| E18 | 18F    | Economy  | 18324.0 |   2100 |                 100 |

> **Note:** Row E18 has only 4 economy seats (A,B and E,F) to reach the total 88 economy seats.

---

## 110-seat layout — High-density single-class (2-4-2, 14 rows; last row reduced to 6 seats)

**Geometry constants**

* Forward galley length = **3000 mm**
* Seat pitch = **737 mm** (14 rows)
* Columns (2-4-2 L→R) Y positions (mm): **-2600, -2000, -800, -200, 200, 800, 2000, 2600**
  (seat letters A..H left→right).
* First row center X = **3368.5 mm**, subsequent rows +737 mm.

**Row centers X (mm)**
Row1 3368.5, Row2 4105.5, Row3 4842.5, Row4 5579.5, Row5 6316.5, Row6 7053.5,
Row7 7790.5, Row8 8527.5, Row9 9264.5, Row10 10001.5, Row11 10738.5, Row12 11475.5,
Row13 12212.5, Row14 12949.5

**Table: 110-seat**

| Row | SeatID | Class   |  X (mm) | Y (mm) | Passenger_mass (kg) |
| --: | :----- | :------ | ------: | -----: | ------------------: |
|   1 | 1A     | Economy |  3368.5 |  -2600 |                 100 |
|   1 | 1B     | Economy |  3368.5 |  -2000 |                 100 |
|   1 | 1C     | Economy |  3368.5 |   -800 |                 100 |
|   1 | 1D     | Economy |  3368.5 |   -200 |                 100 |
|   1 | 1E     | Economy |  3368.5 |    200 |                 100 |
|   1 | 1F     | Economy |  3368.5 |    800 |                 100 |
|   1 | 1G     | Economy |  3368.5 |   2000 |                 100 |
|   1 | 1H     | Economy |  3368.5 |   2600 |                 100 |
|   2 | 2A     | Economy |  4105.5 |  -2600 |                 100 |
|   2 | 2B     | Economy |  4105.5 |  -2000 |                 100 |
|   2 | 2C     | Economy |  4105.5 |   -800 |                 100 |
|   2 | 2D     | Economy |  4105.5 |   -200 |                 100 |
|   2 | 2E     | Economy |  4105.5 |    200 |                 100 |
|   2 | 2F     | Economy |  4105.5 |    800 |                 100 |
|   2 | 2G     | Economy |  4105.5 |   2000 |                 100 |
|   2 | 2H     | Economy |  4105.5 |   2600 |                 100 |
|   3 | 3A     | Economy |  4842.5 |  -2600 |                 100 |
|   3 | 3B     | Economy |  4842.5 |  -2000 |                 100 |
|   3 | 3C     | Economy |  4842.5 |   -800 |                 100 |
|   3 | 3D     | Economy |  4842.5 |   -200 |                 100 |
|   3 | 3E     | Economy |  4842.5 |    200 |                 100 |
|   3 | 3F     | Economy |  4842.5 |    800 |                 100 |
|   3 | 3G     | Economy |  4842.5 |   2000 |                 100 |
|   3 | 3H     | Economy |  4842.5 |   2600 |                 100 |
|   4 | 4A     | Economy |  5579.5 |  -2600 |                 100 |
|   4 | 4B     | Economy |  5579.5 |  -2000 |                 100 |
|   4 | 4C     | Economy |  5579.5 |   -800 |                 100 |
|   4 | 4D     | Economy |  5579.5 |   -200 |                 100 |
|   4 | 4E     | Economy |  5579.5 |    200 |                 100 |
|   4 | 4F     | Economy |  5579.5 |    800 |                 100 |
|   4 | 4G     | Economy |  5579.5 |   2000 |                 100 |
|   4 | 4H     | Economy |  5579.5 |   2600 |                 100 |
|   5 | 5A     | Economy |  6316.5 |  -2600 |                 100 |
|   5 | 5B     | Economy |  6316.5 |  -2000 |                 100 |
|   5 | 5C     | Economy |  6316.5 |   -800 |                 100 |
|   5 | 5D     | Economy |  6316.5 |   -200 |                 100 |
|   5 | 5E     | Economy |  6316.5 |    200 |                 100 |
|   5 | 5F     | Economy |  6316.5 |    800 |                 100 |
|   5 | 5G     | Economy |  6316.5 |   2000 |                 100 |
|   5 | 5H     | Economy |  6316.5 |   2600 |                 100 |
|   6 | 6A     | Economy |  7053.5 |  -2600 |                 100 |
|   6 | 6B     | Economy |  7053.5 |  -2000 |                 100 |
|   6 | 6C     | Economy |  7053.5 |   -800 |                 100 |
|   6 | 6D     | Economy |  7053.5 |   -200 |                 100 |
|   6 | 6E     | Economy |  7053.5 |    200 |                 100 |
|   6 | 6F     | Economy |  7053.5 |    800 |                 100 |
|   6 | 6G     | Economy |  7053.5 |   2000 |                 100 |
|   6 | 6H     | Economy |  7053.5 |   2600 |                 100 |
|   7 | 7A     | Economy |  7790.5 |  -2600 |                 100 |
|   7 | 7B     | Economy |  7790.5 |  -2000 |                 100 |
|   7 | 7C     | Economy |  7790.5 |   -800 |                 100 |
|   7 | 7D     | Economy |  7790.5 |   -200 |                 100 |
|   7 | 7E     | Economy |  7790.5 |    200 |                 100 |
|   7 | 7F     | Economy |  7790.5 |    800 |                 100 |
|   7 | 7G     | Economy |  7790.5 |   2000 |                 100 |
|   7 | 7H     | Economy |  7790.5 |   2600 |                 100 |
|   8 | 8A     | Economy |  8527.5 |  -2600 |                 100 |
|   8 | 8B     | Economy |  8527.5 |  -2000 |                 100 |
|   8 | 8C     | Economy |  8527.5 |   -800 |                 100 |
|   8 | 8D     | Economy |  8527.5 |   -200 |                 100 |
|   8 | 8E     | Economy |  8527.5 |    200 |                 100 |
|   8 | 8F     | Economy |  8527.5 |    800 |                 100 |
|   8 | 8G     | Economy |  8527.5 |   2000 |                 100 |
|   8 | 8H     | Economy |  8527.5 |   2600 |                 100 |
|   9 | 9A     | Economy |  9264.5 |  -2600 |                 100 |
|   9 | 9B     | Economy |  9264.5 |  -2000 |                 100 |
|   9 | 9C     | Economy |  9264.5 |   -800 |                 100 |
|   9 | 9D     | Economy |  9264.5 |   -200 |                 100 |
|   9 | 9E     | Economy |  9264.5 |    200 |                 100 |
|   9 | 9F     | Economy |  9264.5 |    800 |                 100 |
|   9 | 9G     | Economy |  9264.5 |   2000 |                 100 |
|   9 | 9H     | Economy |  9264.5 |   2600 |                 100 |
|  10 | 10A    | Economy | 10001.5 |  -2600 |                 100 |
|  10 | 10B    | Economy | 10001.5 |  -2000 |                 100 |
|  10 | 10C    | Economy | 10001.5 |   -800 |                 100 |
|  10 | 10D    | Economy | 10001.5 |   -200 |                 100 |
|  10 | 10E    | Economy | 10001.5 |    200 |                 100 |
|  10 | 10F    | Economy | 10001.5 |    800 |                 100 |
|  10 | 10G    | Economy | 10001.5 |   2000 |                 100 |
|  10 | 10H    | Economy | 10001.5 |   2600 |                 100 |
|  11 | 11A    | Economy | 10738.5 |  -2600 |                 100 |
|  11 | 11B    | Economy | 10738.5 |  -2000 |                 100 |
|  11 | 11C    | Economy | 10738.5 |   -800 |                 100 |
|  11 | 11D    | Economy | 10738.5 |   -200 |                 100 |
|  11 | 11E    | Economy | 10738.5 |    200 |                 100 |
|  11 | 11F    | Economy | 10738.5 |    800 |                 100 |
|  11 | 11G    | Economy | 10738.5 |   2000 |                 100 |
|  11 | 11H    | Economy | 10738.5 |   2600 |                 100 |
|  12 | 12A    | Economy | 11475.5 |  -2600 |                 100 |
|  12 | 12B    | Economy | 11475.5 |  -2000 |                 100 |
|  12 | 12C    | Economy | 11475.5 |   -800 |                 100 |
|  12 | 12D    | Economy | 11475.5 |   -200 |                 100 |
|  12 | 12E    | Economy | 11475.5 |    200 |                 100 |
|  12 | 12F    | Economy | 11475.5 |    800 |                 100 |
|  12 | 12G    | Economy | 11475.5 |   2000 |                 100 |
|  12 | 12H    | Economy | 11475.5 |   2600 |                 100 |
|  13 | 13A    | Economy | 12212.5 |  -2600 |                 100 |
|  13 | 13B    | Economy | 12212.5 |  -2000 |                 100 |
|  13 | 13C    | Economy | 12212.5 |   -800 |                 100 |
|  13 | 13D    | Economy | 12212.5 |   -200 |                 100 |
|  13 | 13E    | Economy | 12212.5 |    200 |                 100 |
|  13 | 13F    | Economy | 12212.5 |    800 |                 100 |
|  13 | 13G    | Economy | 12212.5 |   2000 |                 100 |
|  13 | 13H    | Economy | 12212.5 |   2600 |                 100 |
|  14 | 14A    | Economy | 12949.5 |  -2600 |                 100 |
|  14 | 14B    | Economy | 12949.5 |  -2000 |                 100 |
|  14 | 14C    | Economy | 12949.5 |   -800 |                 100 |
|  14 | 14D    | Economy | 12949.5 |   -200 |                 100 |
|  14 | 14E    | Economy | 12949.5 |    200 |                 100 |
|  14 | 14F    | Economy | 12949.5 |    800 |                 100 |

> **Note:** Row 14 omitted seats 14G and 14H (outermost) to make total **110 seats** (14×8 − 2 = 110). Adjust removal position as required by service layout.

---







