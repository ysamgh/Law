import unittest
from lawlint.core import normalize_digits, parse_provisions, parse_subprovisions, lint_text

FIXTURE = """قانون نمونه
ماده ۱- این قانون به ماده ۲ ارجاع دارد.
ماده ۲- متن صحیح است.
ماده ۳- ارجاع به ماده ۹۹ و متن (ناقص.
ماده ۳- شماره تکراری است.
"""
class ParserTests(unittest.TestCase):
    def test_subprovision_extraction(self):
        text = "ماده ۱- متن ماده.\\nتبصره ۱- متن تبصره\\nالف) بند اول\\n۲) جزء دوم\\nماده ۲- ماده بعد"
        found = parse_subprovisions(text)
        self.assertEqual([(x.parent_article, x.kind, x.label) for x in found], [("1", "تبصره", "1"), ("1", "بند", "الف"), ("1", "جزء", "2")])
        self.assertEqual(lint_text(text)["summary"]["subprovisions_parsed"], 3)

    def test_digits(self):
        self.assertEqual(normalize_digits("۱۲٣"), "123")
    def test_articles_parsed(self):
        self.assertEqual([p.article for p in parse_provisions(FIXTURE)], ["1", "2", "3", "3"])
    def test_lint_detects_expected(self):
        report = lint_text(FIXTURE)
        ids = [f["rule_id"] for f in report["findings"]]
        self.assertIn("STR-001", ids)
        self.assertIn("REF-001", ids)
        self.assertIn("TXT-001", ids)
    def test_duplicate_labels_across_chapters_not_reported(self):
        corpus = "باب اول\nماده ۱- متن اول.\nباب دوم\nماده ۱- متن دوم."
        self.assertNotIn("STR-001", [f["rule_id"] for f in lint_text(corpus)["findings"]])
    def test_valid_text_no_findings(self):
        clean = "ماده ۱- به ماده ۲ ارجاع دارد.\nماده ۲- متن."
        self.assertEqual(lint_text(clean)["summary"]["findings"], 0)
if __name__ == "__main__": unittest.main()
