# Roadmap

## Phase 0 — Research / feasibility
- [x] Create project scope and architecture docs
- [x] Identify initial official/secondary source candidates
- [ ] Verify access, format, terms, and version metadata for candidate pilot law
- [ ] Choose bounded pilot corpus (one law + amendments)

## Phase 1 — Text ingestion
- [ ] Source manifest schema
- [ ] Download/extraction adapter (manual artifact first)
- [ ] Persian normalization with original preservation
- [ ] Hierarchy parser + tests
- [ ] Provision JSON export

## Phase 2 — Deterministic linter
- [ ] Duplicate labels
- [ ] Bracket/parenthesis balance
- [ ] Cross-reference extraction
- [ ] Internal reference resolver
- [ ] Evidence-based findings output
- [ ] CI tests with deliberately faulty synthetic fixtures

## Phase 3 — Version / amendment intelligence
- [ ] Immutable source snapshots
- [ ] Amendment and repeal events
- [ ] Temporal reference resolution
- [ ] Diff and impact graph

## Phase 4 — UI
- [ ] Search law/provision
- [ ] Graph of references
- [ ] Findings dashboard with severity and review states
- [ ] Side-by-side versions
- [ ] Export report

## Phase 5 — Formal modeling
- [ ] Select a small formulaic domain (tax thresholds, benefit eligibility, fee calculation)
- [ ] Translate the rule into executable model (Python first; Lean later)
- [ ] Differential test against official examples/forms and independently implemented calculators
- [ ] Edge-case search / property-based testing
- [ ] Formal proofs only for well-defined model properties; clearly state that proof validity depends on model fidelity to the statute

## Phase 6 — International comparison
- [ ] Common metadata and hierarchy schema
- [ ] Add one jurisdiction from a strong structured source
- [ ] Compare document structure, amendments, citation patterns, and selected rule models
- [ ] Avoid false equivalence; country-specific legal concepts remain jurisdiction-scoped
