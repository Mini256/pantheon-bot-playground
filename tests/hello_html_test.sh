#!/usr/bin/env bash
set -euo pipefail

root_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
page="$root_dir/hello.html"

fail() {
  echo "FAIL: $1" >&2
  exit 1
}

[[ -f "$page" ]] || fail "hello.html not found at repo root"

content="$(cat "$page")"

grep -qi "<title>" <<<"$content" || fail "missing <title>"
grep -Eqi "<h1[^>]*>" <<<"$content" || fail "missing <h1>"
grep -Eqi "<p[^>]*>" <<<"$content" || fail "missing <p> description"

echo "OK: hello.html smoke checks passed"

