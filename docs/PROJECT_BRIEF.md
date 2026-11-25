# Project Brief — Legal Text as a Verifiable System

## Inspiration
A 2026 Lexifina/Alan Yahya report describes formalizing US tax legislation in Lean and running structural/reference checks plus executable tax-rule models. It claims numerous drafting defects and discrepancies surfaced in a large statute. We use the *method* as inspiration, not its findings as independently verified facts.

## Product hypothesis
Iranian legislation is a large, changing corpus whose structure and cross-references can be modeled as data. A transparent, reproducible linter can help lawyers, researchers, journalists, businesses, and citizens detect potential textual/structural defects and understand amendment impact faster.

## Value proposition
- Search and navigate law by structured hierarchy.
- Identify likely broken references, numbering defects, and structural anomalies.
- Track amendments/repeals across versions.
- Explain how a rule's dependencies change over time.
- Eventually model selected formulaic laws as executable rules and test edge cases.
- Compare legal structures and selected rule models across jurisdictions without pretending legal concepts are equivalent.

## Research questions
1. Which official Iranian legal sources provide stable, machine-readable or downloadable text?
2. How can we represent amendments, repeals, effective dates, and consolidated versions?
3. Which mechanical checks have low false-positive rates in Persian legislation?
4. Which domains offer tractable rule-model pilots (tax, social security, licensing, labor, customs)?
5. Can a model produce evidence-backed findings and reproducible test cases without giving legal advice?

## Initial scope
**In:** corpus ingestion, metadata, Persian normalization, hierarchy parsing, deterministic checks, citation graph, evidence reports, version provenance.
**Out:** automatic legal interpretation, court outcome prediction, personalized legal advice, autonomous filing, definitive loophole claims.

## Pilot candidate
Begin with a bounded, high-impact statute such as the Direct Taxes Act. Select the actual source and version only after source-quality assessment. Prefer one law with amendments over a broad low-quality scrape.

## Findings labels
- `machine-detected`: deterministic rule triggered
- `AI-suggested`: language model flagged a semantic concern
- `source-verified`: evidence checked against official publication
- `expert-reviewed`: qualified reviewer confirmed
- `false-positive`: dismissed after review

Never equate machine-detected with confirmed legal defect.
