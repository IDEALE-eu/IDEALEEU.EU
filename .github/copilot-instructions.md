# Copilot Instructions for IDEALE-EU Codebase

## Orientation
- Evidence-first aerospace platform: QS anchoring + PLUMA automation, organized by TFA domains and CAx lifecycle phases (CAD through CAS).
- Repository structure mirrors program governance: `00-PROGRAM` (CM, governance), `01-10-*` product stacks; paths encode DOMAIN/SYSTEM/SUBSYSTEM context.
- Always maintain the QS→FWD→UE→FE→CB→QB flow when touching evidence, simulations, or automation artifacts.

## Core Code Surfaces
- `aqua-qc/`: Quantum noise mitigation and QML pipelines (Qiskit). Tests live in `tests/`, benchmarks under `benches/`, CI matrices in `ci/`. Run `pip install -r aqua-qc/requirements.txt` then `pytest tests/ -v` from repo root or inside `aqua-qc`.
- `finance/`: Teknia token integration (`FinanceTokenIntegration`) bridges EVM metrics to rewards; see `finance/examples_usage.py` and supporting automation in `10-BUSINESS/FINANCE/08-TOOLS_AUTOMATION/automated_reward_calculator.py`.
- `02-AIRCRAFT/DIGITAL_TWIN_MODEL/12-CODE`: Python runtime skeleton for the aircraft digital twin. `pyproject.toml` defines FastAPI-based services with mypy/pytest tooling and coverage gates.

## Workflows & Commands
- **Python tooling**: prefer Python 3.11; install per package (`pip install -r ...`) then run pytest with coverage (`pytest tests/ --cov=...`). Keep black line length at 100 (per `aqua-qc/ci/config.yaml`) and obey mypy strictness in digital twin code.
- **Finance automation**: run examples via `python finance/examples_usage.py`; automated reward calculator lives under `10-BUSINESS/FINANCE/08-TOOLS_AUTOMATION/`.
- **Docs**: Jekyll site served with `bundle install` then `bundle exec jekyll serve`; docs sources under `docs/`.

## Configuration Management & Validation
- Baselines, CCB, ECR/ECO material under `00-PROGRAM/CONFIG_MGMT`. When modifying manifests (e.g., `04-BASELINES` YAML) keep SHA values and UTCS anchors accurate.
- Structural guards: run `scripts/validate-structure.sh` (global), `validate-aircraft-systems.sh`, `validate-aircraft-subsystems.sh`, and `validate-aircraft-components.sh` after reorganizing aircraft folders.
- Traceability: `00-PROGRAM/CONFIG_MGMT/10-TRACEABILITY/UTCS/validate-utcs.py` enforces UTCS schema; `12-CI/validate-utcs.py` wraps it for CI.
- Federated learning artifacts: use `01-FLEET/FEDERATED_LEARNING/02-ORCHESTRATION/JOB_SPECS/TESTS/validate_job_specs.py --validate-all` before committing YAML specs; diagnostics JSON checked with `03-CLIENTS/.../validate_reports.py`.

## Conventions & Patterns
- Every artifact that leaves configuration control must reference a UTCS URI (see `UTCS/README.md` and schema). Update `INDEX/` CSVs when new subsystems appear.
- Finance artifacts log to `10-BUSINESS/FINANCE/06-REPORTING/rewardIT_LOG.csv`; preserve CSV header order when appending.
- Keep CAx directory naming (SYSTEM/SUBSYSTEM/PLM/CAx) intact; scripts expect hyphenated ATA naming for aircraft and underscored STA naming for spacecraft.
- Digital twin CI requires coverage >95% (Level C) and optional certification gates; coordinate with `12-CODE/CI_CD/` guidance when adding pipelines.

## References
- High-level architecture and navigation: root `README.md`.
- UTCS governance: `00-PROGRAM/CONFIG_MGMT/10-TRACEABILITY/UTCS/README.md` and `SCHEMAS/`.
- Finance domain overview: `10-BUSINESS/FINANCE/README.md`.
- Provide feedback if any critical workflow is missing or unclear.
