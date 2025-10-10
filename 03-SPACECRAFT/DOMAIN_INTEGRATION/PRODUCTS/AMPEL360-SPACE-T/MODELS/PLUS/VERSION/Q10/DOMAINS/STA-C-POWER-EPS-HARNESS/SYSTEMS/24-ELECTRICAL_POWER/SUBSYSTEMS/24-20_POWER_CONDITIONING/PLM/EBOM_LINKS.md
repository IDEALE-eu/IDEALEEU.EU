# 24-20 · POWER_CONDITIONING — EBOM LINKS (Q10)

**Scope:** Power conditioning hardware: voltage regulators, buck/boost stages, linear regulators, filters, and conditioning modules for stable power delivery.  
**Rule:** Physical HW lives here (24-20). DC-DC converters in **24-60**. Protection in **24-50**. Algorithms in **24-70**. FSW in **42**. No code stored here.

---

## 1) Assemblies (24-20 EBOM SSOT)
| P/N                    | Description                                  | Level | CAx (design)                          | Status |
|------------------------|----------------------------------------------|-------|---------------------------------------|--------|
| 24-20-ASSY-PCDU        | Power Conditioning & Distribution Unit       | ASSY  | `CAx/CAD/assy_pcdu.step`              | REL    |
| 24-20-ASSY-LDO-RAIL    | Linear Regulator Rail Assembly               | ASSY  | `CAx/CAD/assy_ldo_rail.step`          | REL    |
| 24-20-ASSY-BUCK-5V     | Buck Converter 5V Secondary                  | ASSY  | `CAx/CAD/assy_buck_5v.step`           | RVW    |
| 24-20-ASSY-BOOST-50V   | Boost Converter 50V Battery Charge           | ASSY  | `CAx/CAD/assy_boost_50v.step`         | REL    |
| 24-20-ASSY-FILT-LC     | LC Filter Assembly (EMI suppression)         | ASSY  | `CAx/CAD/assy_filt_lc.step`           | REL    |
| 24-20-ASSY-REG-LIN-3V3 | 3.3V Linear Regulator Module                 | ASSY  | `CAx/CAD/assy_reg_lin_3v3.step`       | REL    |

*EM/QM/FM variants tracked via derived P/N suffixes.*

---

## 2) Key parts by assembly
| P/N                     | Description                           | Belongs to        | CAx / Docs                         | Note |
|-------------------------|---------------------------------------|-------------------|------------------------------------|------|
| 24-20-IC-REG-BUCK       | Buck regulator IC                     | BUCK-5V           | `CAx/CAD/ic_buck.step`             | Efficiency > 90% |
| 24-20-IC-LDO-3V3        | LDO regulator 3.3V 2A                 | REG-LIN-3V3       | `CAx/CAD/ic_ldo_3v3.step`          | Low noise       |
| 24-20-IND-BUCK-10uH     | 10 µH power inductor                  | BUCK-5V           | `CAx/CAD/ind_10uh.step`            | Saturation 5A   |
| 24-20-CAP-BULK-470uF    | 470 µF bulk capacitor                 | PCDU              | `CAx/CAD/cap_bulk.step`            | ESR < 50 mΩ     |
| 24-20-FILT-FERRITE      | Ferrite EMI filter                    | FILT-LC           | `CAx/CAD/filt_ferrite.step`        | 100 MHz atten   |
| 24-20-MOSFET-P-SYNC     | P-channel synchronous MOSFET          | BOOST-50V         | `CAx/CAD/mosfet_p.step`            | Rds(on) < 10mΩ  |

---

## 3) Cross-references
- **Efficiency analysis**: `CAx/CAE/efficiency_analysis_Q10.xlsx`
- **Thermal derating**: `CAx/CAE/thermal_pcdu_Q10.pdf`
- **Voltage regulation spec**: `CAx/CMP/voltage_regulation_spec.pdf`
- **EMI compliance**: See **24-50_PROTECTION_FUSES_BREAKERS** for filtering

---

## 4) Configuration notes
- Primary bus: 28 V nominal (ripple < 100 mV pk-pk)
- Secondary rails: 5 V, 3.3 V, 12 V (tolerance ±5%)
- Efficiency: > 85% across all converters
- Load regulation: < 1% for 0–100% load variation
