# Check Catalog

| ID | Check | Method | Caveat |
|---|---|---|---|
| STR-001 | duplicate article labels within parsed heading scope | deterministic | Historical numbering and missing scope headings may cause false positives |
| STR-002 | malformed hierarchy/labels | parser (planned) | Persian formatting variants |
| REF-001 | reference target absent from supplied corpus | parser + registry; review-only | external laws and incomplete corpora are common false-positive sources |
| REF-002 | citation level mismatch | heuristic (planned) | flexible citation wording |
| REF-003 | repealed/renumbered target | temporal graph (planned) | amendment history required |
| TXT-001 | unbalanced parentheses/brackets/braces | deterministic | quoted text and footnotes can trigger |
| TXT-002 | duplicate wording/definition | similarity/AI triage (planned) | repetition may be intentional |
| DATE-001 | missing/unclear effective date | metadata check (planned) | dates can occur in text |
| AMEND-001 | uncertain amendment mapping | diff + review (planned) | similarity is not legal proof |
| LOGIC-001 | threshold boundary anomaly | executable/property tests (planned) | model fidelity must be reviewed |
| LOGIC-002 | possible rule conflict | AI/symbolic triage (planned) | not a legal conclusion |

Severity: Info / Warning / Review. “Confirmed” requires human review and authoritative evidence.
