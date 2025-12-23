import re
import unittest
from html.parser import HTMLParser
from pathlib import Path


class _HelloHtmlParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.tags_seen: set[str] = set()
        self.doctype_decls: list[str] = []
        self._in_h1 = False
        self.h1_text_parts: list[str] = []

    def handle_decl(self, decl: str) -> None:
        self.doctype_decls.append(decl)

    def handle_starttag(self, tag: str, attrs) -> None:
        self.tags_seen.add(tag)
        if tag == "h1":
            self._in_h1 = True

    def handle_endtag(self, tag: str) -> None:
        if tag == "h1":
            self._in_h1 = False

    def handle_data(self, data: str) -> None:
        if self._in_h1:
            self.h1_text_parts.append(data)


class HelloHtmlTest(unittest.TestCase):
    def test_hello_html_exists_and_has_basic_structure(self) -> None:
        repo_root = Path(__file__).resolve().parents[1]
        hello_path = repo_root / "hello.html"
        self.assertTrue(hello_path.exists(), "Expected hello.html to exist at repo root")

        html = hello_path.read_text(encoding="utf-8")

        self.assertRegex(
            html,
            re.compile(r"(?is)\A\s*<!doctype\s+html\s*>"),
            "Expected an HTML5 doctype declaration at the top of the document",
        )

        parser = _HelloHtmlParser()
        parser.feed(html)

        for required in ("html", "head", "title", "body", "h1"):
            self.assertIn(required, parser.tags_seen, f"Expected <{required}> tag in hello.html")

        doctype_text = " ".join(parser.doctype_decls).lower()
        self.assertIn("doctype html", doctype_text, "Expected doctype declaration to be HTML5")

        h1_text = " ".join(parser.h1_text_parts).strip()
        self.assertRegex(h1_text, re.compile(r"(?i)hello"), "Expected greeting text in <h1>")
