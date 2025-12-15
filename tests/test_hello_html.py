import unittest
from pathlib import Path


class HelloHtmlTests(unittest.TestCase):
    def test_hello_html_exists(self) -> None:
        repo_root = Path(__file__).resolve().parents[1]
        hello_path = repo_root / "hello.html"
        self.assertTrue(hello_path.is_file(), "Expected hello.html at repository root")

    def test_hello_html_has_expected_structure_and_message(self) -> None:
        repo_root = Path(__file__).resolve().parents[1]
        html = (repo_root / "hello.html").read_text(encoding="utf-8")

        stripped = html.lstrip().lower()
        self.assertTrue(
            stripped.startswith("<!doctype html>"),
            "Expected HTML5 doctype at top of document",
        )

        self.assertIn("<html", html)
        self.assertIn('lang="en"', html)
        self.assertIn("<head>", html)
        self.assertIn("<body>", html)
        self.assertIn('<meta charset="utf-8"', html.lower())
        self.assertIn("<title>Hello</title>", html)
        self.assertIn("Hello from Pantheon Bot Playground", html)

