from __future__ import annotations
import re
from dataclasses import dataclass, asdict

_DIGITS = str.maketrans("۰۱۲۳۴۵۶۷۸۹٠١٢٣٤٥٦٧٨٩", "01234567890123456789")

def normalize_digits(text: str) -> str:
    return text.translate(_DIGITS)

def normalize_text(text: str) -> str:
    text = normalize_digits(text).replace("ي", "ی").replace("ك", "ک")
    text = re.sub(r"[\u200c\u200d]", " ", text)
    return re.sub(r"\s+", " ", text).strip()

@dataclass
class Provision:
    article: str
    start_line: int
    text: str

@dataclass
class Finding:
    rule_id: str
    severity: str
    provision: str | None
    line: int
    excerpt: str
    message: str
    status: str = "machine-detected"
    confidence: str = "high"

_ARTICLE_RE = re.compile(r"^\s*ماده\s*([0-9]+(?:\s*مکرر)?)\s*[-–—:]?\s*(.*)$", re.I)
_REF_RE = re.compile(r"(?<![\w])(?:ماده|مواد)\s*\(?\s*([0-9]+(?:\s*مکرر)?(?:\s*(?:و|,|-)\s*[0-9]+(?:\s*مکرر)?)*)", re.I)

def parse_provisions(text: str) -> list[Provision]:
    provisions: list[Provision] = []
    current = None
    body: list[str] = []
    start = 1
    for line_no, raw in enumerate(text.splitlines(), 1):
        line = normalize_digits(raw).strip()
        match = _ARTICLE_RE.match(line)
        if match:
            if current is not None:
                provisions.append(Provision(current, start, "\n".join(body)))
            current = normalize_text(match.group(1))
            body = [match.group(2)] if match.group(2) else []
            start = line_no
        elif current is not None:
            body.append(raw)
    if current is not None:
        provisions.append(Provision(current, start, "\n".join(body)))
    return provisions

def _balance_errors(text: str) -> list[tuple[str, int]]:
    pairs = {"(": ")", "[": "]", "{": "}"}
    closing = {v: k for k, v in pairs.items()}
    stack: list[tuple[str, int]] = []
    errors: list[tuple[str, int]] = []
    for i, ch in enumerate(text):
        if ch in pairs:
            stack.append((ch, i))
        elif ch in closing:
            if not stack or stack[-1][0] != closing[ch]:
                errors.append((f"unexpected closing delimiter {ch}", i))
            else:
                stack.pop()
    errors.extend((f"unclosed delimiter {ch}", i) for ch, i in stack)
    return errors

def lint_text(text: str) -> dict:
    provisions = parse_provisions(text)
    findings: list[Finding] = []
    line_map = text.splitlines()
    article_ids: dict[str, Provision] = {}
    for p in provisions:
        if p.article in article_ids:
            findings.append(Finding("STR-001", "warning", p.article, p.start_line,
                line_map[p.start_line-1].strip(), f"Duplicate article label: ماده {p.article}. Check scope and source formatting."))
        else:
            article_ids[p.article] = p
        for msg, offset in _balance_errors(p.text):
            findings.append(Finding("TXT-001", "warning", p.article, p.start_line,
                p.text[max(0, offset-30):offset+30].replace("\n", " "), f"Delimiter imbalance candidate: {msg}."))
    known = set(article_ids)
    for p in provisions:
        norm = normalize_digits(p.text)
        for match in _REF_RE.finditer(norm):
            citation = match.group(1)
            targets = re.findall(r"\d+(?:\s*مکرر)?", citation)
            for target in targets:
                target = normalize_text(target)
                if target not in known:
                    findings.append(Finding("REF-001", "review", p.article, p.start_line,
                        match.group(0), f"Reference target ماده {target} was not found in this input corpus. This may be an external-law citation, omitted corpus material, or a real broken reference; verify manually.", confidence="medium"))
    return {
        "tool": "lawlint", "version": "0.1.0",
        "summary": {"provisions_parsed": len(provisions), "findings": len(findings),
            "by_rule": {r: sum(f.rule_id == r for f in findings) for r in sorted({f.rule_id for f in findings})}},
        "provisions": [asdict(p) for p in provisions],
        "findings": [asdict(f) for f in findings],
        "limitations": ["Reference findings are candidates, not confirmed legal defects.",
            "Only article-level structure is parsed in this MVP; تبصره/بند/جزء hierarchy is not yet fully modeled.",
            "The input is treated as a single corpus. References to other laws can be flagged as unresolved.",
            "A clean report does not establish legal validity, completeness, or currentness of the source text."]
    }
