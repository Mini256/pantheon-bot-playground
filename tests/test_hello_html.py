import unittest
from pathlib import Path


class TestHelloHtml(unittest.TestCase):
    def test_hello_html_exists_and_has_basic_structure(self) -> None:
        repo_root = Path(__file__).resolve().parents[1]
        hello_path = repo_root / "hello.html"

        self.assertTrue(hello_path.exists(), "hello.html should exist at repo root")

        contents = hello_path.read_text(encoding="utf-8")
        lower = contents.lower()

        self.assertIn("<!doctype html>", lower)
        self.assertIn('<html lang="en">', lower)
        self.assertIn("<head>", lower)
        self.assertIn("<body>", lower)
        self.assertIn("</html>", lower)


if __name__ == "__main__":
    unittest.main()

