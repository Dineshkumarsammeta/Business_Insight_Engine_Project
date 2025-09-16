# Progress Log — Business Insight Engine (Modernisation, Sept 2025)

> **Context:** Originally built **14‑Jan‑2024 → 12‑Mar‑2024**. In **September 2025**, this repo was uploaded and refreshed for current tooling. Commit dates now reflect **publication/cleanup**, not the original build window.

This log keeps a transparent record of work sessions, evidence, and releases so reviewers can verify progress quickly.

---

## How to use this log
- Log every meaningful change with **Date**, **Block** (AM/PM), **Task**, **Status**, **Time (h)**, and a **reference** (PR/commit).
- Keep **evidence** in one place: tick the checklist below as artefacts land in the repo.
- Record **benchmark runs** in `data/bench.csv`. Copy a snapshot of the latest results to `data/metrics.csv` if you want a simple single‑file view.
- Release with **CHANGELOG.md** and **tags** (SemVer).

---

## Objectives for v0.1.0 (48‑hour plan)
- [ ] Add `pyproject.toml` (Python 3.11) and pin core deps
- [ ] Add `Dockerfile`, `.env.template`, and `Makefile`
- [ ] Restructure to `src/` where helpful
- [ ] Tiny **Flask API** (`/health`, `/predict`) + **Streamlit** mini‑demo
- [ ] **Smoke tests** + **pytest** in CI (`actions/setup-python`)
- [ ] Create **`data/bench.csv`** and export **`data/metrics.csv`** snapshot
- [ ] **README** Quick Start + **modernisation disclosure**
- [ ] **CHANGELOG.md** and **tag `v0.1.0`**

---

## Evidence checklist (1/0 mirror of A–L report)
- [ ] Data README (DATA_README)
- [ ] Baselines documented (classical vs LLM)
- [ ] Metrics artefact present (`data/metrics.csv`)
- [x] Tests present (`tests/`)
- [x] CI present (GitHub Actions runs visible)
- [ ] Installable package (`pyproject.toml`)
- [ ] Demo runnable (API/UI + instructions)
- [ ] Releases & CHANGELOG (tagged)
- [x] Licence (MIT)
- [ ] Contributing/Code of Conduct

---

## Work sessions (chronological)
| Date       | Block | Task                                                                 | Status    | Time (h) | Ref        | Notes |
|------------|-------|----------------------------------------------------------------------|-----------|----------|------------|-------|
| 2025-09-09 | AM    | Create `docs/progress-log.md` and `data/bench.csv` scaffolds            | Done      | 0.5      | <commit-sha> | Starter artefacts added |
| 2025-09-09 | AM    | Draft `pyproject.toml` and CI workflow snippets                         | Planned   | 1.0      | —          | See Appendix below |
| 2025-09-09 | PM    | Add tiny Flask API + smoke test; wire CI                               | Planned   | 2.5      | —          | Endpoints: `/health`, `/predict` |
| 2025-09-09 | PM    | Prepare `CHANGELOG.md`; tag `v0.1.0`                                    | Planned   | 0.5      | —          | Tag after CI green |

> Tip: Replace `<commit-sha>` with the actual commit SHA (short) and `<PR-#>` with your PR number if using PRs.

---

## Release log
| Version | Date       | Notes                                  |
|---------|------------|----------------------------------------|
| v0.1.0  | 2025-09-09 | First public release; env pins, tiny API, smoke tests, metrics snapshot |

---

## Benchmark runs (recorded in `data/bench.csv`)
This repo tracks benchmarks as **tidy rows** (one row = one run summary). You can append new runs over time.  
Recommended visualisations: accuracy / f1 over time, latency (p50/p95), and cost.

**Update flow:**  
1. Append a new row to `data/bench.csv` after each run.  
2. Copy the latest row(s) into `data/metrics.csv` if you need a one‑file snapshot for the README.  

---

## Appendix — handy commands (copy‑ready)
```bash
# Create and activate venv (example)
python -m venv .venv && source .venv/bin/activate
pip install -e .

# Run tests locally
pytest -q

# Run Flask demo locally
export FLASK_APP=app.py; flask run -p 8000

# Using Docker (if Dockerfile present)
docker build -t bie:dev .
docker run -p 8000:8000 --env-file .env bie:dev

# Minimal curl checks
curl -s http://localhost:8000/health
curl -s -X POST http://localhost:8000/predict -H "Content-Type: application/json" -d '{"text":"Great service"}'
```
