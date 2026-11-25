# Law — Iran-first Legal Text Engineering

A research and software project for treating legal texts as versioned, structured systems that can be parsed, linted, tested, compared, and eventually formally modeled.

**Not legal advice. Machine findings are review candidates, not confirmed defects.**

## Current MVP: LawLint 0.1

A runnable Python CLI that currently checks:
- `STR-001`: duplicate article labels
- `REF-001`: article citations whose target is absent from the supplied corpus (review-only; external citations and incomplete corpora cause false positives)
- `TXT-001`: unbalanced `()`, `[]`, `{}` delimiters

It parses article headings using Persian and Arabic numerals, preserves source excerpts, heuristically extracts تبصره/بند/جزء markers, and outputs JSON and Markdown reports. Subprovision extraction is experimental and does not yet model legal nesting.

### Run locally

```bash
python -m lawlint examples/synthetic_law.txt --json report.json --markdown report.md
```

### Install CLI

```bash
python -m pip install -e .
lawlint examples/synthetic_law.txt --json report.json
```

### Tests

```bash
python -m unittest discover -s tests -v
```

A synthetic fixture intentionally includes a duplicate article number, missing reference target, and unbalanced parenthesis. It is not a real law and is used to test detection only.

## Project documents
- `docs/PROJECT_BRIEF.md`
- `docs/ARCHITECTURE.md`
- `docs/SOURCES_AND_RESEARCH.md`
- `docs/CHECK_CATALOG.md`
- `docs/ROADMAP.md`

## Next
1. Acquire and provenance-check a legally authoritative corpus and amendments.
2. Extend parsing to تبصره / بند / جزء and cross-law references.
3. Add source anchors, amendment/version models, and regression fixtures.
4. Produce a web UI only after parser/report quality is validated.
5. Model selected computational rules; use Lean when proof properties are well-defined and valuable.

## Jurisdiction design
Start with Iran, but use jurisdiction/source/version metadata that can support US (OLRC), UK (legislation.gov.uk), and EU (EUR-Lex) later. Do not treat legal concepts across jurisdictions as equivalent.
