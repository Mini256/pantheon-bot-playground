const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs/promises');
const path = require('node:path');

test('hello.html exists and looks like a valid HTML document', async () => {
  const filePath = path.join(process.cwd(), 'hello.html');
  const contents = await fs.readFile(filePath, 'utf8');

  assert.match(contents, /<!doctype html>/i);
  assert.match(contents, /<html\b[^>]*>/i);
  assert.match(contents, /<head\b[^>]*>/i);
  assert.match(contents, /<body\b[^>]*>/i);
  assert.match(contents, /<\/body>/i);
  assert.match(contents, /<\/html>/i);

  assert.match(contents, /<meta\s+charset=["']utf-8["']\s*\/?\s*>/i);
  assert.match(contents, /<title>\s*hello\s*<\/title>/i);
  assert.match(contents, /<h1\b[^>]*>[\s\S]*hello[\s\S]*<\/h1>/i);
});

