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
    scope: str = ""
    status_marker: str = ""



@dataclass
class SubProvision:
    parent_article: str
    kind: str
    label: str
    start_line: int
    text: str

_SUBPROVISION_PATTERNS = [
    ("تبصره", re.compile(r"^تبصره(?:\s+([0-9]+))?\s*[-–—:]?\s*(.*)$")),
    ("بند", re.compile(r"^(?:بند\s+)?([الف-ی])\s*[)ـ.،:-]\s*(.*)$")),
    ("جزء", re.compile(r"^(?:جزء\s+)?([0-9]+)\s*[)ـ.،:-]\s*(.*)$")),
]

def parse_subprovisions(text: str) -> list[SubProvision]:
    """Extract obvious note/item markers under article headings; heuristic, not legal-semantic parsing."""
    rows: list[SubProvision] = []
    parent = None
    current_kind = None
    current_label = None
    current_start = 0
    body: list[str] = []
    def flush():
        if parent and current_kind:
            rows.append(SubProvision(parent, current_kind, current_label or "", current_start, "\\n".join(body).strip()))
    for line_no, raw in enumerate(text.splitlines(), 1):
        line = normalize_digits(raw).strip()
        article_match = _ARTICLE_RE.match(line)
        if article_match:
            flush()
            parent = normalize_text(article_match.group(1))
            current_kind = current_label = None
            body = []
            continue
        if parent is None:
            continue
        matched = None
        for kind, pattern in _SUBPROVISION_PATTERNS:
            m = pattern.match(line)
            if m:
                matched = (kind, normalize_text(m.group(1) or ""), m.group(2))
                break
        if matched:
            flush()
            current_kind, current_label, first_text = matched
            current_start = line_no
            body = [first_text] if first_text else []
        elif current_kind:
            body.append(raw)
    flush()
    return rows

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
    scope_levels: dict[int, str] = {}
    current_scope = ""
    status_marker = ""
    scope = ""
    for line_no, raw in enumerate(text.splitlines(), 1):
        line = normalize_digits(raw).strip()
        heading = re.match(r"^(باب|فصل|بخش)\s*(.*)$", line)
        if heading:
            level = {"باب": 1, "فصل": 2, "بخش": 3}[heading.group(1)]
            if current is not None:
                provisions.append(Provision(current, start, "\n".join(body), scope, status_marker))
                current, body = None, []
            scope_levels[level] = line
            for deeper in [k for k in scope_levels if k > level]:
                del scope_levels[deeper]
            current_scope = " / ".join(scope_levels[k] for k in sorted(scope_levels))
        match = _ARTICLE_RE.match(line)
        if match:
            if current is not None:
                provisions.append(Provision(current, start, "\n".join(body), scope, status_marker))
            current = normalize_text(match.group(1))
            header = match.group(2)
            status_marker = next((tag for tag in ("منسوخه", "جایگزین", "الحاقی", "اصلاحی") if tag in header), "")
            body = [header] if header else []
            start = line_no
            scope = current_scope
        elif current is not None and not heading:
            body.append(raw)
    if current is not None:
        provisions.append(Provision(current, start, "\n".join(body), scope, status_marker))
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
    scoped_seen: set[tuple[str, str]] = set()
    for p in provisions:
        key = (p.scope, p.article)
        if key in scoped_seen:
            findings.append(Finding("STR-001", "warning", p.article, p.start_line,
                line_map[p.start_line-1].strip(), f"Duplicate article label: ماده {p.article} within scope {p.scope or '(no heading)'}. Check history and numbering."))
        else:
            scoped_seen.add(key)
        article_ids.setdefault(p.article, p)
        for msg, offset in _balance_errors(p.text):
            findings.append(Finding("TXT-001", "warning", p.article, p.start_line,
                p.text[max(0, offset-30):offset+30].replace("\n", " "), f"Delimiter imbalance candidate: {msg}."))
    known = set(article_ids)
    for p in provisions:
        norm = normalize_digits(p.text)
        for match in _REF_RE.finditer(norm):
            targets = re.findall(r"\d+(?:\s*مکرر)?", match.group(1))
            for target in targets:
                target = normalize_text(target)
                if target not in known:
                    findings.append(Finding("REF-001", "review", p.article, p.start_line,
                        match.group(0), f"Reference target ماده {target} was not found in this input corpus. This may be an external-law citation, omitted corpus material, or a real broken reference; verify manually.", confidence="medium"))
    return {
        "tool": "lawlint", "version": "0.1.0",
        "summary": {"provisions_parsed": len(provisions), "subprovisions_parsed": len(parse_subprovisions(text)), "findings": len(findings),
            "by_rule": {r: sum(f.rule_id == r for f in findings) for r in sorted({f.rule_id for f in findings})}},
        "provisions": [asdict(p) for p in provisions],
        "subprovisions": [asdict(s) for s in parse_subprovisions(text)],
        "findings": [asdict(f) for f in findings],
        "limitations": ["Reference findings are candidates, not confirmed legal defects.",
            "Subprovision markers (تبصره/بند/جزء) are heuristically extracted; nesting and semantic relationships are not fully modeled.",
            "The input is treated as a single corpus. References to other laws can be flagged as unresolved.",
            "Duplicate numbering checks are scoped to parsed باب/فصل/بخش headings, but historical numbering may still cause false positives.",
            "A clean report does not establish legal validity, completeness, or currentness of the source text."]
    }
