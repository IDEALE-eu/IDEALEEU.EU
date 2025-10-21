# approvals — Index

Store signed approvals and correspondence supporting Level A plans and SOI milestones.

## Contents
- [SOI1_minutes.pdf](./SOI1_minutes.pdf)
- [SOI2_minutes.pdf](./SOI2_minutes.pdf)
- [SOI3_minutes.pdf](./SOI3_minutes.pdf)
- [SOI4_minutes.pdf](./SOI4_minutes.pdf)
- [authority_correspondence/](./authority_correspondence/) — emails, letters, action items

## Optional
- [plan_signoffs/](./plan_signoffs/) — signed PSAC/SDP/SVP/SQAP/SCMP PDFs
- [deviations/](./deviations/) — approved deviations and justifications
- [agreements/](./agreements/) — MoCs, tool-qualification acceptance

## Filing rules
- Filenames: `<doc>_vX.Y_signed_YYYYMMDD.pdf`
- Include signer, date, and SHA-256 of the source in the footer.

# Approvals — File Naming and Footer Metadata

> **Rule**
> - Filenames: `<doc>_vX.Y_signed_YYYYMMDD.pdf`  
> - Footer on **every page**: **Signer**, **Date**, **SHA-256** of the signed source

---

### File Naming and Footer Metadata

> **Rule**
> - Filenames: `<doc>_vX.Y_signed_YYYYMMDD.pdf`  
> - Footer on **every page**: **Signer**, **Date**, **SHA-256** of the signed source

---

## ✅ Canonical Example

**Filename**
```text
PSAC_v1.2_signed_20251021.pdf
````

**Footer (every page)**

```text
Approved by: J. Alvarez (Certification Authority)
Date: 2025-10-21
Source SHA-256: 3f7a9b5e42e0a7e8c913b6bcb917aa64a2d18ed47b7c1a4f391c9c4b3a2efb8a
```

---

## 🧩 Additional Examples

| Document                        | Version | Filename                        | Footer snippet                                                               |
| ------------------------------- | ------: | ------------------------------- | ---------------------------------------------------------------------------- |
| Software Development Plan       |     1.0 | `SDP_v1.0_signed_20250901.pdf`  | `Approved by: L. Rossi (Dev Lead) • Date: 2025-09-01 • SHA-256: 8bfae43d…`   |
| Software Verification Plan      |     2.1 | `SVP_v2.1_signed_20250715.pdf`  | `Approved by: K. Morgan (IV&V Lead) • Date: 2025-07-15 • SHA-256: e2f54b19…` |
| Software Quality Assurance Plan |     1.3 | `SQAP_v1.3_signed_20250810.pdf` | `Approved by: M. Chen (QA Lead) • Date: 2025-08-10 • SHA-256: 5a12c8e0…`     |

> **Tip:** Keep the **document code** (`PSAC`, `SDP`, `SVP`, `SQAP`, `SCMP`) and **version** in sync with the baselined source.

---

## 🔐 How to Compute SHA-256

**From the baselined source file** (e.g., `PSAC_v1.2.md` or exported PDF before signature):

```bash
# macOS/Linux
shasum -a 256 PSAC_v1.2.md

# OpenSSL alternative
openssl dgst -sha256 PSAC_v1.2.md

# Windows PowerShell
Get-FileHash PSAC_v1.2.md -Algorithm SHA256
```

Paste the 64-hex-char digest into the footer as `Source SHA-256: <hash>`.

---

## ✅ QA Checklist

* [ ] Filename matches `<doc>_vX.Y_signed_YYYYMMDD.pdf`
* [ ] Footer present on **every page**
* [ ] Footer includes **Approver role**, **ISO date**, **SHA-256**
* [ ] Hash computed from the **exact** signed source
* [ ] Entry added to `planning/approvals/index.md` and SOI records

---

## 📁 Location

Store all files under:

```
.../LEVEL_A/planning/approvals/
```

Link them from:

* `planning/README.md` → Approvals section
* `certification/SAS.md` → Evidence index

```
::contentReference[oaicite:0]{index=0}
```

