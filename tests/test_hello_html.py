import re
import unittest
from pathlib import Path


class HelloHtmlTests(unittest.TestCase):
    def test_hello_html_exists_and_has_basic_structure(self) -> None:
        repo_root = Path(__file__).resolve().parents[1]
        hello_path = repo_root / "hello.html"
        self.assertTrue(hello_path.exists(), "Expected hello.html to exist at repo root")

        content = hello_path.read_text(encoding="utf-8")
        normalized = content.lower()

        self.assertIn("<!doctype html>", normalized)
        self.assertIn("<head", normalized)
        self.assertIn("</head>", normalized)
        self.assertIn("<body", normalized)
        self.assertIn("</body>", normalized)
        self.assertIn("</html>", normalized)

        self.assertRegex(content, re.compile(r"\bhello\b", re.IGNORECASE))

