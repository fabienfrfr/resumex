# Resumex
Lightweight CV engine using Streamlit, LanceDB, and DuckDB. (and FalkorDB for graph ?)

![banner](/banner.jpeg)


## Quick Start
1. **Initialize:** `uv sync`
2. **Launch App:** `uv run streamlit run src/main.py`

## Architecture
- **Interface:** Streamlit + AgGrid (Manual entry)
- **Data:** LanceDB (Local storage)
- **Engine:** DuckDB (SQL analysis)
- **Orchestration:** Mage.ai (Agent workflows)

## Project Structure (TODO)
```text
resumex/
├── app/          # Streamlit UI
├── core/         # DB repository & logic
├── data/         # LanceDB files
├── flow/         # Mage.ai pipelines
└── pyproject.toml
```

