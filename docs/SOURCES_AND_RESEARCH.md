# Source Research & Data Strategy (Iran-first)

## Source hierarchy
1. Official promulgation/publication: Official Gazette (روزنامه رسمی) and the issuing authority.
2. National legislation/regulation portals and official agency repositories.
3. Parliament / legislative research portals for bills, explanatory material, and legislative history.
4. Secondary databases: discovery and convenience only; cross-check against official text.

Potential starting points surfaced in research:
- روزنامه رسمی کشور: https://www.rrk.ir/
- سامانه ملی قوانین و مقررات کشور (Dotic): https://www.dotic.ir/
- مرکز پژوهش‌های مجلس: https://rc.majlis.ir/
- IranCodify (secondary): https://irancodify.com/
- LawLex (secondary): https://lawlex.ir/

Source access, completeness, machine readability, legal status, and terms of use must be investigated per collection. Do not assume any site offers a reliable API or bulk download.

## Corpus strategy
- Begin with one law and its amendments.
- Preserve original downloaded artifact.
- Record SHA-256, retrieval date, publisher, document identifier, and edition.
- Extract article-level text while retaining source page anchors.
- Maintain amendment acts separately, then build consolidated snapshots only when amendment mapping is reliable.
- Track publication date, promulgation date, effective date, repeal date, and transition rules separately.

## Candidate pilot
قانون مالیات‌های مستقیم is a plausible pilot due to its rule-heavy structure and economic impact. Alternatives: قانون کار, قانون تأمین اجتماعی, قانون تجارت. Choose after source accessibility and scope review.

## International comparison
Build a jurisdiction-agnostic schema first. Do not compare laws based only on translated text. Possible later sources:
- United States: structured US Code from OLRC; good model for XML and versioning.
- United Kingdom: legislation.gov.uk provides structured legislation and temporal metadata.
- EU: EUR-Lex provides multilingual legal acts and metadata.
- Other jurisdictions: only add after evaluating authoritative source, licensing, version history, and machine-readable availability.

## Legal and ethical guardrails
- Use lawful access and respect website terms, copyright, and robots restrictions.
- Do not mass-scrape or bypass access controls.
- Public access does not necessarily imply unrestricted redistribution.
- Always display source and version, and state when consolidation/status is uncertain.
