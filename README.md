# Resumex
A lightweight CV generation engine.

## Setup
1. **Initialize:** `uv venv` && `uv pip install -r pyproject.toml`

## Data Management (Datasette)
Launch the interface to manage data:
`uv run datasette data/resumex.db`
*Access at http://localhost:8001*

## Generation
Run the PDF exporter:
`uv run src/generator.py`

Automation / Orchestration (in progress):
`uv run mage start` (http://localhost:6789)

## SQL Table Schema
Run this in the sqlite-web console:
```sql
CREATE TABLE consultants (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    expertise TEXT,
    bio TEXT
);
```

## Project Structure
```text
resumex/
├── data/
│   └── resumex.db        # SQLite database
├── src/
│   ├── generator.py      # PDF generation script
│   └── template.html     # Jinja2 branding template
├── pyproject.toml        # uv configuration
└── README.md
```

