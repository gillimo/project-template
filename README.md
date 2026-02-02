# Project Template

Mission Learning Statement
- Mission: Provide a reusable template for fast bootstrapping of local agents and data tools.
- Learning focus: repeatable project scaffolding, consistent run/test workflows, and clean handoffs.
- Project start date: 2026-01-12 (inferred from folder timestamp)

Reusable scaffold with CLI + GUI entry points, docs structure, and data stubs for rapid prototyping.

## Features

- CLI + GUI entry points via `run_app.py`
- Docs scaffolding with reference order
- Data folder with starter JSON stubs
- Bootstrap scripts for placeholder replacement

## Installation

### Requirements

- Python 3.8+

## Quick Start

```bash
python run_app.py status
python run_app.py gui
```

## Usage

- Run `scripts\bootstrap.ps1` to apply placeholders.
- Follow `docs/DOCS_INDEX.md` for the operating order.

## Architecture

```
CLI/GUI Entry (run_app.py)
    |
    v
App Engine (src/)
    |
    v
Data + Docs (data/, docs/)
```

## Project Structure

```
run_app.py     # CLI/GUI entry point
src/           # Core logic
gui/           # GUI assets
data/          # JSON stubs
docs/          # Documentation scaffold
scripts/       # Bootstrap/validation scripts
```

## Building

No build step required. Run directly with Python.

## Contributing

Use this template as a base; customize for your project needs.

## License

MIT License - see [LICENSE](LICENSE) for details.
