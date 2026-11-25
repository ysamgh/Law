# Roadmap

## Phase 0 — feasibility
- [x] scope and architecture
- [x] initial source candidates/check catalog
- [x] source audit and source hierarchy documented (primary portal access observed; acquisition/reuse still pending)
- [ ] verify official source access, version metadata, extraction, and reuse terms
- [ ] select one bounded pilot law and its amendments (prefer small/stable pilot before tax statute)

## Phase 1 — ingestion and parser
- [x] UTF-8 text input
- [x] Persian/Arabic digit normalization
- [x] article-heading parser
- [x] heading scope extraction for باب/فصل/بخش
- [x] basic provision JSON structure
- [ ] PDF/HTML ingestion with page/line anchors
- [x] heuristic extraction for تبصره / بند / جزء (non-semantic, experimental)
- [ ] nested hierarchy and semantic relationships
- [ ] source manifest + checksums (schema documented; tooling pending)

## Phase 2 — deterministic lint
- [x] duplicate article labels scoped to parsed headings (STR-001)
- [x] delimiter balance (TXT-001)
- [x] basic article reference extraction (REF-001, review-only)
- [x] JSON + Markdown report
- [x] synthetic tests and CI workflow
- [ ] citation type and cross-law handling
- [ ] false-positive reduction and test corpus

## Phase 3 — temporal/amendment analysis
- [ ] immutable source snapshots
- [ ] amendment/repeal events
- [ ] temporal reference resolution
- [ ] provision mapping across versions
- [ ] impact graph and diffs

## Phase 4 — product UI
- [ ] searchable provision view
- [ ] reference graph
- [ ] findings dashboard and review states
- [ ] version comparison and report exports

## Phase 5 — executable rules/formal verification
- [ ] choose formulaic legal domain
- [ ] executable model and differential tests
- [ ] property/edge-case tests
- [ ] Lean proof for carefully scoped model properties
- [ ] explicitly document model-to-law fidelity assumptions

## Phase 6 — global
- [ ] common metadata and jurisdiction adapters
- [ ] add a jurisdiction with authoritative structured source
- [ ] compare structure/versioning and selected rule models
- [ ] avoid false equivalence between legal concepts
