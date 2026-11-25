# Initial Check Catalog

| ID | Check | Method | Output | Risk / caveat |
|---|---|---|---|---|
| STR-001 | Duplicate article/subsection label | deterministic | duplicate path candidates | intentional duplicates across chapters possible |
| STR-002 | Broken hierarchy | deterministic parser | malformed/unknown nesting | Persian formatting variations |
| REF-001 | Unresolved internal reference | parser + registry | missing target candidate | ambiguous wording / target version |
| REF-002 | Reference level mismatch | rule + parser | paragraph/article mismatch | natural-language citation forms |
| REF-003 | Temporal/dead reference | version graph | target repealed/moved candidate | needs amendment history |
| TXT-001 | Unbalanced parentheses/brackets | deterministic | location of imbalance | citations, quotations, footnotes may create false positives |
| TXT-002 | Suspicious duplicate wording/definition | similarity / AI triage | pair of clauses | repetition may be intentional |
| DATE-001 | Missing/ambiguous effective-date metadata | metadata check | uncertainty warning | effective date may be specified in article text |
| AMEND-001 | Amendment mapping uncertainty | diff + human review | unmatched changed provisions | text similarity alone insufficient |
| LOGIC-001 | Threshold boundary anomaly | executable model/property tests | edge-case test | only for rules faithfully modeled |
| LOGIC-002 | Contradictory rule candidates | AI + symbolic checks | review case | not a legal conclusion |

## Test severity
- **Info:** formatting/coverage issue
- **Warning:** possible structural defect
- **Review:** potential substantive defect requiring legal expert
- **Confirmed:** only human/source review; never automatic
