# Île-de-France Transit Route Planner Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a bilingual schedule-based Île-de-France route planner with a Python REST API and a small browser interface, while guiding the learner through each component.

**Architecture:** Keep the project as one modular Python application in `transit_planner/`. Import GTFS CSV files into a local SQLite database, expose schedule lookup and time-dependent routing behind Python service interfaces, serve the REST API with FastAPI, and serve a small HTML/CSS/JavaScript interface from the same application.

**Tech Stack:** Python 3.11+, FastAPI, Uvicorn, SQLite via the Python standard library, HTML, CSS, JavaScript, pytest.

**Spec:** `docs/superpowers/specs/2026-10-08-ile-de-france-transit-planner-design.md`

## Global Constraints

- Cover bus, tram, metro, and rail services represented in Île-de-France Mobilités schedule data.
- Let a traveler enter an origin, destination, and local departure date and time.
- Rank journeys by scheduled arrival time and return the fastest journey plus at most two alternatives.
- Build a REST API first, then add a small user interface.
- Make the interface available in French and English from its first release.
- The first version uses scheduled service data and presents results as schedule-based estimates.
- Use GTFS service calendars to exclude trips not running on the requested date.
- Keep routing logic out of API handlers and keep schedule ingestion separate from route search.
- Keep downloaded full GTFS feeds and generated local databases out of version control.
- Preserve the learning workflow: each stage includes a tiny runnable example, an explained code fragment, an independent exercise, and a reflection prompt; do not provide a complete answer to the learner's exercise.

## Review Focus

- GTFS times after midnight can exceed `24:00:00`; parse and compare these correctly in the schedule parser tests.
- Local dates and daylight-saving transitions affect service activation and departure-time interpretation; test a service-date boundary and document the application timezone as `Europe/Paris`.
- A stop name can identify multiple stops; test that location lookup returns candidates and never silently chooses one.
- A transfer is only feasible when the next trip departs after arrival plus the configured minimum transfer time; test both an exactly feasible and an infeasible transfer.
- Large or malformed feeds can fail during import; test missing required columns and bad stop-time values and ensure failures identify the file and row without marking the database ready.

---

## File Map

- Create `transit_planner/pyproject.toml` — package metadata and runtime/development dependencies.
- Create `transit_planner/README.md` — setup, feed import, local run commands, API examples, data limits, and learning-stage links.
- Create `transit_planner/.gitignore` — local feed files, generated SQLite database, caches, and secrets.
- Create `transit_planner/app/__init__.py` — package marker.
- Create `transit_planner/app/models.py` — typed domain records for stops, trips, services, legs, and itineraries.
- Create `transit_planner/app/gtfs_import.py` — GTFS parsing, validation, and database import.
- Create `transit_planner/app/repository.py` — SQLite persistence and schedule/location lookup.
- Create `transit_planner/app/routing.py` — earliest-arrival and top-three distinct-itinerary search.
- Create `transit_planner/app/api.py` — FastAPI health, location-search, and route-search endpoints.
- Create `transit_planner/app/main.py` — application construction and static interface mounting.
- Create `transit_planner/app/static/index.html` — semantic bilingual search and results page.
- Create `transit_planner/app/static/app.js` — API calls, locale selection, and rendering.
- Create `transit_planner/app/static/styles.css` — responsive layout and readable itinerary presentation.
- Create `transit_planner/tests/fixtures/` — tiny hand-authored GTFS tables, including agency metadata, and timetable cases.
- Create `transit_planner/tests/test_gtfs_import.py` — parsing, validation, and import tests.
- Create `transit_planner/tests/test_repository.py` — location and schedule persistence tests.
- Create `transit_planner/tests/test_routing.py` — timetable, transfer, service-date, and ranking tests.
- Create `transit_planner/tests/test_api.py` — request validation and response contract tests.
- Create `transit_planner/tests/test_static_ui.py` — static interface delivery and locale text checks.
- Create `transit_planner/tests/test_end_to_end.py` — fixture-based full route-search flow.

All product code and project tests live under the new `transit_planner/` directory. Do not edit learner-owned files in `sandbox/` or `projects/`.

## Interfaces

The following interfaces are shared across tasks:

```python
# app/models.py
@dataclass(frozen=True)
class Stop:
    stop_id: str
    name: str
    latitude: float | None
    longitude: float | None

@dataclass(frozen=True)
class JourneyLeg:
    trip_id: str
    route_id: str
    route_name: str
    mode: str
    from_stop: Stop
    to_stop: Stop
    departure: datetime
    arrival: datetime

@dataclass(frozen=True)
class Itinerary:
    legs: tuple[JourneyLeg, ...]
    departure: datetime
    arrival: datetime
    duration_seconds: int
```

```python
# app/gtfs_import.py
def parse_gtfs_time(value: str) -> int: ...
def import_gtfs(feed_path: Path, database_path: Path) -> ImportSummary: ...

# app/repository.py
class TransitRepository:
    def find_stops(self, query: str, limit: int = 10) -> list[Stop]: ...
    def get_active_connections(self, service_date: date) -> Iterable[Connection]: ...

# app/routing.py
class RoutePlanner:
    def find_itineraries(
        self, origin_id: str, destination_id: str, departure: datetime,
        max_results: int = 3,
    ) -> list[Itinerary]: ...
```

`Connection` contains its from/to stop IDs, trip and route IDs, mode/route label, scheduled departure and arrival datetimes, and the applicable service ID. The planner uses a configurable minimum transfer time, initially five minutes. It returns up to three distinct itineraries, where distinctness means the ordered sequence of `(trip_id, from_stop_id, to_stop_id)` legs differs. Itinerary ranking is by arrival time, then departure time, then stable leg identifiers.

The API contract is:

- `GET /health` → `{"status": "ok"}` once the application has a usable imported database.
- `GET /api/stops?q=<text>` → matching stop candidates, each with an ID and display name.
- `POST /api/routes` with `{"origin_id": "...", "destination_id": "...", "departure": "ISO-8601 datetime"}` → `{"itineraries": [...], "message": null}`; no route returns an empty array and a localized-neutral message.
- Invalid fields return HTTP 422 with a stable JSON error structure. Unknown IDs return HTTP 404. API messages remain language-neutral; the browser localizes user-facing labels and errors.

The first route-search implementation uses a time-dependent multi-label search. At each `(stop_id, incoming_trip_id)` state, retain up to three best labels with distinct leg signatures, ordered by arrival time and transfer count; this preserves whether continuing on the current trip avoids a transfer. Expand only connections whose departure is at least the label's reachable time, including the minimum transfer time after changing trips. The implementation must prevent repeated use of a trip/stop segment in one itinerary. This bounded policy directly supports the requested top-three behavior and remains explainable with small timetable traces.

---

### Task 1: Project skeleton and tiny GTFS fixture

**Files:**
- Create: `transit_planner/pyproject.toml`
- Create: `transit_planner/README.md`
- Create: `transit_planner/.gitignore`
- Create: `transit_planner/app/__init__.py`
- Create: `transit_planner/tests/fixtures/basic/`
- Create: `transit_planner/tests/fixtures/basic/agency.txt`
- Create: `transit_planner/tests/test_gtfs_import.py`

**Interfaces:**
- Consumes: global constraints above.
- Produces: installable project; fixture containing `agency.txt`, `stops.txt`, `routes.txt`, `trips.txt`, `stop_times.txt`, `calendar.txt`, and `calendar_dates.txt`; test command `pytest`.

- [ ] **Step 1: Write a failing project smoke test**

Create `test_project_imports` to import `app` and assert it resolves from this project directory.

- [ ] **Step 2: Run the smoke test and confirm it fails before package setup**

Run from `transit_planner/`: `python -m pytest tests/test_gtfs_import.py::test_project_imports -q`
Expected: FAIL because the package is not yet installed/importable.

- [ ] **Step 3: Add minimal package configuration and fixture files**

Declare FastAPI and Uvicorn as runtime dependencies and pytest as a development dependency. Ignore `.venv/`, `.pytest_cache/`, Python caches, `data/`, and generated `.sqlite3` files. Document creation of a local virtual environment and editable install. Hand-author a compact feed where one traveler can take a direct trip or transfer.

- [ ] **Step 4: Run the smoke test**

Run: `python -m pytest tests/test_gtfs_import.py::test_project_imports -q`
Expected: PASS.

- [ ] **Step 5: Learning checkpoint**

Have the learner explain how Python finds a package and identify how the fixture files link stops, trips, routes, and service dates. Give one small practice prompt without asking them to build the whole app.

### Task 2: Validate and import GTFS schedules

**Files:**
- Create: `transit_planner/app/models.py`
- Create: `transit_planner/app/gtfs_import.py`
- Modify: `transit_planner/tests/test_gtfs_import.py`
- Test: `transit_planner/tests/fixtures/basic/`

**Interfaces:**
- Consumes: project package and fixture from Task 1.
- Produces: `ImportSummary` with counts and `import_gtfs(feed_path: Path, database_path: Path) -> ImportSummary`; schema tables for agencies, stops, routes, trips, stop times, calendars, and exceptions.

- [ ] **Step 1: Add failing tests**

Add tests for a valid fixture import; missing required `stop_times.txt` columns; a route that references an absent agency; malformed time with the file and row identified; a GTFS time such as `25:10:00`; and service-date exceptions overriding the weekly calendar.

- [ ] **Step 2: Run those tests and confirm they fail**

Run: `python -m pytest tests/test_gtfs_import.py -q`
Expected: FAIL because `import_gtfs` and the record types do not exist.

- [ ] **Step 3: Implement parsing, validation, and transactional SQLite import**

Parse CSV using `csv.DictReader`; validate required files, columns, agency/route/trip/stop references, and time formats; preserve GTFS times beyond midnight as seconds from the service-day start; import agencies and all other records in a transaction; raise a typed error that includes the file and row; add `ImportSummary` and the initial domain dataclasses.

- [ ] **Step 4: Run importer tests**

Run: `python -m pytest tests/test_gtfs_import.py -q`
Expected: PASS, including rollback/no-ready-state behavior after malformed input.

- [ ] **Step 5: Learning checkpoint**

Show a tiny fragment that converts a `HH:MM:SS` GTFS value to seconds and explain the boundary case after midnight. Ask the learner to parse a different time by hand and add an independent validation case.

### Task 3: Schedule repository and stop lookup

**Files:**
- Create: `transit_planner/app/repository.py`
- Create: `transit_planner/tests/test_repository.py`
- Modify: `transit_planner/tests/test_gtfs_import.py`

**Interfaces:**
- Consumes: imported SQLite schema and `Stop` model from Task 2.
- Produces: `TransitRepository(database_path)` with `find_stops(query, limit=10)` and `get_active_connections(service_date)`; location results never silently choose among duplicate names.

- [ ] **Step 1: Add failing repository tests**

Test case-insensitive partial stop-name search, ID lookup, duplicate-name candidates, result limit, connection creation from consecutive stop times, weekly service activation, and added/removed service exceptions.

- [ ] **Step 2: Run repository tests to confirm they fail**

Run: `python -m pytest tests/test_repository.py -q`
Expected: FAIL because the repository is not implemented.

- [ ] **Step 3: Implement indexed SQLite lookups and service-date filtering**

Add indexes for stop names, trip IDs, and service IDs. Return all matching candidates up to `limit`; derive adjacent stop connections from trip stop times and include only service IDs active for the requested Europe/Paris date after calendar exceptions.

- [ ] **Step 4: Run repository tests**

Run: `python -m pytest tests/test_repository.py tests/test_gtfs_import.py -q`
Expected: PASS.

- [ ] **Step 5: Learning checkpoint**

Explain why an index helps name lookup and trace a trip's ordered stop times into connections. Ask the learner to predict which services remain active after one exception is applied.

### Task 4: Earliest-arrival routing

**Files:**
- Create: `transit_planner/app/routing.py`
- Create: `transit_planner/tests/test_routing.py`
- Modify: `transit_planner/app/models.py`

**Interfaces:**
- Consumes: `TransitRepository.get_active_connections(service_date)` from Task 3.
- Produces: `RoutePlanner(repository, minimum_transfer_seconds=300)` and `find_itineraries(origin_id, destination_id, departure, max_results=3) -> list[Itinerary]`.

- [ ] **Step 1: Add failing single-route tests**

Test a direct journey, a faster journey requiring a transfer, a missed connection, no route, inactive service date, and an origin equal to destination.

- [ ] **Step 2: Run the routing tests to confirm they fail**

Run: `python -m pytest tests/test_routing.py -q`
Expected: FAIL because `RoutePlanner` is not implemented.

- [ ] **Step 3: Implement the time-dependent earliest-arrival search**

Use a priority queue ordered by reachable arrival time and represent a search state with stop ID plus incoming trip ID. A connection can be boarded at the requested departure instant; after changing trips, require the configured minimum transfer time. Track legs so the returned itinerary contains complete stop and route details. Interpret a timezone-naive API/local UI departure as `Europe/Paris`; preserve explicit offsets supplied by API clients.

- [ ] **Step 4: Run the routing tests**

Run: `python -m pytest tests/test_routing.py -q`
Expected: PASS for direct, transfer, missed connection, inactive date, no-route, and same-stop cases.

- [ ] **Step 5: Learning checkpoint**

Trace a three-stop timetable using a small queue table. Ask the learner to explain why the next connection is feasible or missed, then solve a separate hand-built timetable.

### Task 5: Up to three distinct ranked itineraries

**Files:**
- Modify: `transit_planner/app/routing.py`
- Modify: `transit_planner/tests/test_routing.py`

**Interfaces:**
- Consumes: single-route `RoutePlanner` from Task 4.
- Produces: up to `max_results` itineraries ordered by scheduled arrival; distinctness is the ordered `(trip_id, from_stop_id, to_stop_id)` signature; deterministic tie-break by departure time, transfer count, then signature.

- [ ] **Step 1: Add failing top-three tests**

Create a fixture with four candidate journeys: three distinct feasible journeys with different arrivals and one duplicate signature; assert only the best three distinct journeys are returned in deterministic order. Also test fewer than three candidates and `max_results=1`.

- [ ] **Step 2: Run top-three tests to confirm they fail**

Run: `python -m pytest tests/test_routing.py -q`
Expected: FAIL because the planner currently returns only one journey or does not apply distinct ranking.

- [ ] **Step 3: Retain bounded labels per stop and reconstruct distinct journeys**

Extend the priority-queue search to retain at most three non-dominated labels for each `(stop_id, incoming_trip_id)` state with distinct leg signatures. Reject repeated trip/stop segments within an itinerary. Apply the documented deterministic ranking and requested `max_results` cap.

- [ ] **Step 4: Run all routing tests**

Run: `python -m pytest tests/test_routing.py -q`
Expected: PASS; results are distinct, sorted, and capped.

- [ ] **Step 5: Learning checkpoint**

Use a short example to explain why keeping more than one candidate path is necessary for alternatives. Ask the learner to describe the signature that makes two itineraries distinct and test it on another example.

### Task 6: REST API and local feed import command

**Files:**
- Create: `transit_planner/app/api.py`
- Create: `transit_planner/app/main.py`
- Create: `transit_planner/tests/test_api.py`
- Modify: `transit_planner/README.md`

**Interfaces:**
- Consumes: repository and planner from Tasks 3–5.
- Produces: `GET /health`, `GET /api/stops?q=...`, and `POST /api/routes`; a command `python -m app.gtfs_import <feed-directory> <database-path>` for local import; stable JSON errors.

- [ ] **Step 1: Add failing API tests**

Test health after database readiness; stop lookup candidates; valid route response fields and ordering; 422 for missing/invalid request fields; 404 for unknown stop IDs; and a valid no-route response with an empty itinerary list.

- [ ] **Step 2: Run API tests to confirm they fail**

Run: `python -m pytest tests/test_api.py -q`
Expected: FAIL because the FastAPI app and endpoints do not exist.

- [ ] **Step 3: Add API handlers, serialization, and import command**

Construct repository/planner dependencies outside handler logic. Validate ISO-8601 local datetimes and normalize to `Europe/Paris`. Keep API messages language-neutral; serialize each leg with line, mode, stops, and scheduled times. Fail health clearly when the database is absent or not imported.

- [ ] **Step 4: Run API tests and a local server smoke check**

Run: `python -m pytest tests/test_api.py -q`, then `uvicorn app.main:app --app-dir . --host 127.0.0.1 --port 8000` from `transit_planner/` and request `/health` and `/docs`.
Expected: tests pass; health returns `{"status":"ok"}` after fixture import; OpenAPI docs load locally.

- [ ] **Step 5: Document API use and learning checkpoint**

Add setup/import/run commands and request/response examples to the README. Ask the learner to explain the path from HTTP request to routing service and identify which layer owns each responsibility.

### Task 7: Bilingual browser interface

**Files:**
- Create: `transit_planner/app/static/index.html`
- Create: `transit_planner/app/static/app.js`
- Create: `transit_planner/app/static/styles.css`
- Create: `transit_planner/tests/test_static_ui.py`
- Modify: `transit_planner/app/main.py`

**Interfaces:**
- Consumes: API endpoints from Task 6.
- Produces: responsive local search page with French/English selector; stop candidate selection; departure date/time inputs; ranked journey cards; loading, validation, empty, and request-error states.

- [ ] **Step 1: Add failing static/UI behavior checks**

Test that the app serves the page and static assets; check the source includes translated labels and messages for both locales and that itinerary rendering uses API fields rather than hard-coded journey data.

- [ ] **Step 2: Run UI checks to confirm they fail**

Run: `python -m pytest tests/test_static_ui.py -q`
Expected: FAIL because static assets are not mounted or created.

- [ ] **Step 3: Build the small bilingual UI**

Use a visible language selector and translation dictionary in `app.js`. Fetch stop candidates from `/api/stops`, require explicit selection, submit the selected stop IDs and local departure date/time to `/api/routes`, and render up to three itinerary cards. Localize labels and errors while preserving language-neutral API data.

- [ ] **Step 4: Run UI checks and manual local walkthrough**

Run: `python -m pytest tests/test_static_ui.py -q`, then open the local app and perform one valid route search in French and English, one ambiguous-stop selection, and one no-route search.
Expected: assets load and all states are understandable in both languages.

- [ ] **Step 5: Learning checkpoint and reflection**

Ask the learner to explain the request/response flow, identify one issue they debugged independently, and answer which activity helped most and what should change in the next learning stage. Record only the learner's own reflection in `log/learning-reflections.md`.

### Task 8: End-to-end acceptance with a small fixture

**Files:**
- Modify: `transit_planner/README.md`
- Create: `transit_planner/tests/test_end_to_end.py`
- Test: all project modules and fixture feed.

**Interfaces:**
- Consumes: complete local app from Tasks 1–7.
- Produces: documented reproducible local demonstration that starts from fixture import and ends with three ranked bilingual UI results.

- [ ] **Step 1: Add one end-to-end test**

Import the tiny GTFS fixture into a temporary SQLite database, start the app with that database, call the route API through FastAPI's test client, and assert three distinct ranked itineraries and expected leg details.

- [ ] **Step 2: Run the full test suite**

Run from `transit_planner/`: `python -m pytest -q`
Expected: PASS with no external network access or real GTFS feed required.

- [ ] **Step 3: Verify the documented local demonstration**

Follow the README from environment setup through fixture import and local UI search. Confirm generated full feeds/database are ignored by git.

- [ ] **Step 4: Review the learning outcome**

Have the learner explain the data model, earliest-arrival search, transfer condition, API boundary, and one limitation using a new small timetable. Update the learning journal only with demonstrated progress and learner-provided reflections.
