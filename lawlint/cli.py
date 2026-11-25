from __future__ import annotations
import argparse, json
from pathlib import Path
from .core import lint_text

def main():
    parser = argparse.ArgumentParser(description="Iranian legal text structural linter (experimental)")
    parser.add_argument("input", help="UTF-8 .txt file")
    parser.add_argument("--json", dest="json_path", help="write JSON report")
    parser.add_argument("--markdown", dest="md_path", help="write Markdown report")
    args = parser.parse_args()
    report = lint_text(Path(args.input).read_text(encoding="utf-8"))
    if args.json_path:
        Path(args.json_path).write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    if args.md_path:
        lines = ["# LawLint Report", "", f"- Provisions parsed: **{report['summary']['provisions_parsed']}**", f"- Findings: **{report['summary']['findings']}**", ""]
        for f in report["findings"]:
            lines += [f"## {f['rule_id']} — {f['severity']} — ماده {f['provision'] or 'N/A'}", f"**Line {f['line']}** · {f['status']}", "", f"> {f['excerpt']}", "", f["message"], ""]
        lines += ["## Limitations", *[f"- {item}" for item in report["limitations"]]]
        Path(args.md_path).write_text("\n".join(lines), encoding="utf-8")
    print(json.dumps(report["summary"], ensure_ascii=False, indent=2))
    if not args.json_path and not args.md_path:
        for f in report["findings"]:
            print(f"[{f['rule_id']}] ماده {f['provision']} line {f['line']}: {f['message']}")
if __name__ == "__main__": main()
