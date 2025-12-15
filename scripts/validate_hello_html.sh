#!/usr/bin/env bash
set -euo pipefail

root_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
hello_html="$root_dir/hello.html"

fail() {
  echo "error: $*" >&2
  exit 1
}

[[ -f "$hello_html" ]] || fail "missing file: hello.html"

grep -qiE '^\s*<!doctype\s+html\s*>' "$hello_html" || fail "missing HTML5 doctype"
grep -qiE '<html[^>]*\blang="[^"]+"' "$hello_html" || fail "missing html lang attribute"
grep -qiE '<meta[^>]*\bcharset="utf-8"' "$hello_html" || fail "missing utf-8 charset meta"
grep -qiE '<meta[^>]*\bname="viewport"' "$hello_html" || fail "missing viewport meta"
grep -qiE '<title>[^<]*</title>' "$hello_html" || fail "missing title"
grep -qiE '<h1[^>]*>\s*hello\s*</h1>' "$hello_html" || fail "missing H1 Hello message"

echo "ok: hello.html looks good"

