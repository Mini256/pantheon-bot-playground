import re
import unittest
from html.parser import HTMLParser
from pathlib import Path


class _HelloHtmlParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.title_text: list[str] = []
        self.h1_text: list[str] = []
        self._in_title = False
        self._in_h1 = False

    def handle_starttag(self, tag: str, attrs):
        if tag == "title":
            self._in_title = True
        if tag == "h1":
            self._in_h1 = True

    def handle_endtag(self, tag: str):
        if tag == "title":
            self._in_title = False
        if tag == "h1":
            self._in_h1 = False

    def handle_data(self, data: str):
        if self._in_title:
            self.title_text.append(data)
        if self._in_h1:
            self.h1_text.append(data)


class HelloHtmlTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        repo_root = Path(__file__).resolve().parents[1]
        cls.hello_html_path = repo_root / "hello.html"

    def test_hello_html_exists(self):
        self.assertTrue(
            self.hello_html_path.exists(),
            f"Missing {self.hello_html_path.name}; expected at repo root.",
        )

    def test_hello_html_has_basic_structure(self):
        contents = self.hello_html_path.read_text(encoding="utf-8")

        self.assertRegex(
            contents.lstrip(),
            re.compile(r"^<!doctype html>", re.IGNORECASE),
            "Expected a HTML5 doctype at the top of the file.",
        )
        self.assertIn("<html", contents.lower())
        self.assertIn("</html>", contents.lower())

        parser = _HelloHtmlParser()
        parser.feed(contents)

        title = "".join(parser.title_text).strip()
        h1 = "".join(parser.h1_text).strip()

        self.assertTrue(title, "Expected a non-empty <title>.")
        self.assertRegex(title, re.compile(r"hello", re.IGNORECASE))

        self.assertTrue(h1, "Expected a non-empty <h1>.")
        self.assertRegex(h1, re.compile(r"hello", re.IGNORECASE))

