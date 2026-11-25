# MVP Architecture

## Pipeline
```
Official source / archive
  -> source manifest (URL, authority, retrieval date, version, checksum)
  -> extraction (PDF/XML/HTML/OCR; preserve page/line anchors)
  -> Persian normalization (Arabic/Persian chars, whitespace, punctuation; preserve original)
  -> hierarchy parser
  -> provision registry
  -> reference extractor
  -> graph + deterministic lint
  -> AI triage (optional, grounded in snippets)
  -> findings JSON + HTML/Markdown report
  -> expert review / issue tracker
```

## Proposed minimal stack
- Python 3.12
- Pydantic models for source, law, provision, reference, finding
- PyMuPDF / pdfplumber for PDFs; BeautifulSoup for HTML; OCR only if required
- SQLite initially; JSONL artifacts for reproducibility
- NetworkX for reference graph
- pytest for rule tests
- GitHub Actions CI
- Frontend later: static report first; avoid premature full-stack application

## Data contracts (conceptual)
### SourceManifest
- jurisdiction, authority, source_url, retrieval_timestamp
- document_title, promulgation_date, effective_date, version_label
- checksum_sha256, file_format, extraction_method, license/terms

### Provision
- provision_id (stable internal ID)
- law_id, version_id
- hierarchy_path, article_label, paragraph_labels
- text_original, text_normalized
- source_anchor (page/section/line)
- valid_from, valid_to (nullable; only when verified)
- status (unknown/current/repealed/amended/historical; evidence required)

### Reference
- source_provision_id
- target_citation_text
- parsed_target (nullable)
- target_provision_id (nullable)
- resolution_status (resolved/unresolved/ambiguous/external/temporal)
- evidence

### Finding
- rule_id, severity, status
- provision_id, evidence_excerpt, source_anchor
- explanation, suggested_review
- confidence (for triage only)
- run_id, source_manifest_id

## Checks (first release)
1. duplicate provision labels within same hierarchy
2. article/subarticle label sequence anomalies (non-fatal; legal numbering can intentionally skip)
3. dangling cross-reference (unresolved target)
4. reference level mismatch (e.g., text says بند but target parser finds article only)
5. unmatched parentheses/brackets, with Persian/Arabic punctuation handling
6. references to absent external law/article—report as unresolved, not automatically wrong
7. suspicious repeated amendment markers or broken structural labels

## Versioning and amendments
Never overwrite text. Store each source snapshot as immutable; diff versions and map provisions using exact label + similarity + amendment evidence. A provision can be renumbered; stable IDs are internal, not legal citations.

## Evidence discipline
Every finding links to the original text and source version. Machine-generated explanation is clearly separated from extracted evidence. AI may suggest interpretation but cannot edit evidence or upgrade status.
