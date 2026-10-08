# Île-de-France Transit Planner

A learning project that searches scheduled public-transit journeys across Île-de-France. It will be built in small stages: GTFS schedule data, route search, a REST API, then a French/English web interface.

## Local setup

Use Python 3.11 or newer. From this directory:

```bash
python3.13 -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
python -m pytest
```

Keep downloaded schedules and the generated SQLite database in `data/`; those local files are ignored by git.

## Current status

Project scaffold and a tiny hand-authored GTFS fixture. The route planner and API are not implemented yet.
