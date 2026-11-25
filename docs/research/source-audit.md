# Source audit and corpus acquisition plan (Iran-first)

**Audit date:** 2026-11-25  
**Project status:** source discovery; no authoritative law corpus imported yet.

## Source hierarchy

1. **Primary/official:** National Laws and Regulations System, [qavanin.ir](https://qavanin.ir/). The portal currently exposes searchable document fields including title/text, law/regulation/opinion categories, approving authority, dates, status, amendment status, notification and Official Gazette fields. Its homepage reports 168,519 records. Official-source access is the target for corpus ingestion.
2. **Official archival corroboration:** Official Gazette (روزنامه رسمی) records/PDFs and official legislative publication records. Use to verify dates, promulgation, and source snapshot.
3. **Secondary structured corpus for parser tests only:** [AdlMind laws index](https://adlmind.ir/laws) and other legal text indexes claim data originates from Qavanin. These may accelerate development but must not be represented as primary evidence; confirm any text/version against the official portal.
4. **Unofficial technical adapter candidate:** [qavanin-mcp](https://github.com/sepehr071/qavanin-mcp), read-only MCP integration for searching and reading Qavanin content. It is not an official API and requires independent validation of behavior, returned metadata, and source links before use.

## Pilot recommendation

Do not begin with the Direct Taxes Act for parser validation: its amendment history and recent changes make versioning and status semantics a difficult first target.

Start with a small, bounded, relatively stable law (e.g., selected chapters/articles of Civil Code or Constitution), with:
- exact official document identifier and source URL;
- retrieval timestamp (UTC and local);
- document title, approval/publication dates if provided;
- source type and publisher;
- extracted text checksum (SHA-256);
- extraction method and software version;
- archived source file if terms and technical access permit;
- article and subordinate-item anchors;
- comparison note against official publication.

Only after the ingestion/provenance pipeline works, select a tax law for temporal/amendment testing.

## Reproducible manifest schema

Each imported snapshot should have fields:
- `jurisdiction`, `document_id`, `title`, `document_type`
- `official_source_url`, `official_source_identifier`, `publisher`
- `approval_date`, `publication_date`, `retrieved_at`
- `version_label`, `status`, `amendment_notes`
- `raw_file_path`, `raw_sha256`, `extracted_text_path`, `text_sha256`
- `extractor`, `extractor_version`, `review_status`

## Safety and legal limitations

- A corpus sourced from a secondary website is a **development fixture**, not authoritative legal evidence.
- A missing citation target is not a defect unless the full citation scope and effective version are known.
- Do not infer legal validity, current applicability, or repeal from text markers alone.
- Human legal review and primary-source confirmation are mandatory for any substantive conclusion.
