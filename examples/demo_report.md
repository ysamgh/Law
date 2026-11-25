# LawLint Demo Report (Synthetic Input Only)

> This report was generated from `examples/synthetic_law.txt`. The fixture is intentionally faulty and is not a real statute.

- Provisions parsed: **4**
- Findings: **3**

## Findings

### TXT-001 — Warning — Article 3
- Line: 4
- Evidence: `عبارت دارای پرانتز ناقص (در اینجا پایان می‌یابد.`
- Finding: Unclosed opening parenthesis candidate.

### STR-001 — Warning — Article 3
- Line: 5
- Evidence: `ماده ۳- شماره تکراری عمدی برای آزمایش.`
- Finding: Duplicate article label within same scope.

### REF-001 — Review — Article 2
- Line: 3
- Evidence: `ماده 40`
- Finding: Reference target is absent from the input corpus. Could be an external law, incomplete corpus, or real reference defect.

## Test evidence
Five unit tests passed locally, including Persian/Arabic numeral normalization, article parsing, expected detection of the three synthetic defects, and duplicate article numbers in separate باب headings not being reported as duplicates.

**No legal defect has been found in any real Iranian law yet.**
