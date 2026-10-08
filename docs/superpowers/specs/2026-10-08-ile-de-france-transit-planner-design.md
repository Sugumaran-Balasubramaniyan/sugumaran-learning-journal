# Île-de-France Transit Route Planner — Design

## Purpose and learning goals

Build a portfolio project that helps travelers compare public-transit journeys across Île-de-France. The project should also provide a practical path for learning software engineering: the learner will build and explain the data pipeline, routing algorithm, API, and small interface in stages, applying concepts such as graphs, priority queues, data modeling, testing, and service design.

The intended audience is a general Île-de-France traveler. The learning objective is not only to make the application work: the learner should be able to explain its design, implement its core pieces, and adapt them to a new problem.

## Agreed first-version scope

- Cover bus, tram, metro, and rail services represented in Île-de-France Mobilités schedule data.
- Let a traveler enter an origin, destination, and departure time.
- Rank journeys by scheduled arrival time and return the fastest journey plus at most two alternatives.
- Build a REST API first, then add a small user interface.
- Make the interface available in French and English from its first release.
- Treat live vehicle positions and disruption data as a later enhancement; the first version uses scheduled service data.

## Data source and first-version limits

Use the official Île-de-France Mobilités GTFS schedule dataset as the initial input. Its published coverage and refresh cadence should be rechecked when implementation begins: [Île-de-France Mobilités GTFS schedules](https://data.iledefrance-mobilites.fr/explore/dataset/offre-horaires-tc-gtfs-idfm/).

The planner will describe results as schedule-based estimates. It will not claim to account for current delays, cancellations, platform changes, or accessibility constraints in the first version. A later real-time phase can investigate the official PRIM data perimeter and access requirements: [Île-de-France Mobilités real-time data perimeter](https://data.iledefrance-mobilites.fr/explore/dataset/perimetre-des-donnees-tr-disponibles-plateforme-idfm/).

## User experience and API behavior

The primary request supplies an origin stop, a destination stop, and a local departure date and time. The first version searches GTFS stop names and identifiers; address geocoding is out of scope. If a name matches multiple stops, return candidate stops so the traveler can choose. The response contains zero to three itinerary options ordered by scheduled arrival time. Each option includes its departure and arrival times, total duration, ordered transit legs, service or line labels, and transfer details. If no route is available, the API returns an empty result with a clear explanation rather than fabricating a journey.

The first API should expose a health endpoint and a route-search endpoint. Exact URL and JSON field names are implementation details for the implementation plan. Input validation should report missing or invalid locations and departure times in a useful, stable error format. The later interface will provide the same search flow in French and English; language choice must not change route computation.

## Architecture and data flow

Keep the initial system as a small modular application rather than splitting it into services:

1. **Schedule ingestion:** read the official GTFS files, validate required fields, and produce a normalized local schedule representation. Keep ingestion separate from route search so schedule format changes do not leak into the API.
2. **Transit model:** represent stops, trips, stop times, routes, and service calendars. Preserve identifiers needed to connect the GTFS records and present understandable line names.
3. **Routing service:** find feasible journeys from the requested origin and departure time. Model time-dependent connections and transfers; use an earliest-arrival search with a priority queue as the baseline algorithm. Return the top three distinct journeys when available.
4. **REST API:** validate the request, call the routing service, and serialize the response. It should not contain the routing algorithm itself.
5. **Bilingual interface:** a small client that calls the API and displays the itinerary legs, times, transfers, and no-route/error states in French or English.

The data flow is: GTFS files → validated normalized schedule → routing model → route-search request → ranked itineraries → API response → localized interface.

## Routing behavior

The objective is earliest scheduled arrival after the requested departure time. A connection is usable only if its scheduled departure follows the rider's current reachable time and its transfer assumptions are satisfied. Service calendars and dates must be considered so that trips not running on the requested date are excluded.

The first implementation should prioritize correctness and explainability over advanced optimization. It should support transfers and multiple transport modes, avoid returning the same itinerary repeatedly, and state its transfer-time assumptions. The implementation plan must define a tractable method for producing up to two alternatives and a testable definition of when two itineraries count as distinct before coding begins.

## Errors and operational behavior

- Invalid request fields produce a client error with a clear message.
- Unknown or ambiguous locations are reported explicitly; the API must not silently select an unrelated stop.
- A valid search with no feasible scheduled itinerary returns an empty itinerary list and a user-readable message.
- Malformed or incomplete schedule input fails ingestion with actionable diagnostics; it must not silently create partial or misleading routes.
- The interface distinguishes request errors from a valid search that found no journey.

## Testing and acceptance criteria

Use small hand-built timetable fixtures to test the routing rules independently of the full regional dataset. Cover direct trips, a faster arrival requiring a transfer, an unusable connection due to departure time, inactive service dates, no route, and alternative ranking/distinctness. Test schedule parsing and validation separately, then test API request/response behavior and the interface's French and English text.

The first version is acceptable when a traveler can submit an origin, destination, and departure time; receive up to three distinct schedule-based journeys ordered by arrival; inspect legs and transfers; and understand validation, no-route, and data limitations. The learner should also be able to explain the core graph/search model and demonstrate it on a separate small timetable fixture.

## Out of scope for the first version

- Real-time vehicle locations, delays, and disruption-aware routing.
- Mobile-native applications, accounts, saved journeys, payments, or notifications.
- Accessibility-aware routing, fare optimization, and walking directions beyond explicitly modeled transfer links.
- Deployment and production-scale infrastructure before the local API and interface are working.

## Learning sequence

Build in reviewable stages: (1) inspect a small GTFS sample and explain its relationships, (2) parse and validate schedule records, (3) model stops and time-dependent connections, (4) implement and explain earliest-arrival search, (5) add transfers and ranked alternatives, (6) expose the route search through a REST API, and (7) add the bilingual interface. Each stage should include a tiny runnable example, an explained code fragment, an independent exercise, and a short reflection on what helped learning.
