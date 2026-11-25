# Law — Iranian Legal Text Quality & Rule Explorer

Treat legislation as a versioned, structured system. Detect possible drafting, numbering, citation, amendment, and temporal defects; later model selected rules as executable specifications.

**Experimental research tool. Findings are signals for expert review—not legal conclusions or legal advice.**

## Iran-first MVP
- ingest one official/traceable law source with version metadata
- parse hierarchy: law → chapter → article → paragraph → بند → تبصره
- build internal cross-reference graph
- deterministic checks: duplicate numbering, unresolved references, hierarchy anomalies, bracket balance
- evidence-rich report with original text, source/version, anchors, finding status
- AI semantic triage is optional and never confirms a legal defect

Pilot candidate: قانون مالیات‌های مستقیم, pending source/access/version feasibility. Avoid a broad corpus before a reliable small pilot.

## Project branch
`research/legal-linter-mvp` — initial research, architecture, check catalog, source strategy, roadmap.

## International scope
Use common metadata and graph schemas; add countries only when authoritative structured sources, version history, and licensing/access are understood. Candidate sources include US OLRC, UK legislation.gov.uk, and EU EUR-Lex.

See `docs/` for the research and MVP specification.
