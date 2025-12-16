# GitHub Issue #1 — Hello Web Page

## Branch

- Branch name: pantheon/feat-issue-1-b00988c3

## Implementation Approach

- Kept the change intentionally small and dependency-free by adding a single, standalone HTML file.
- Used semantic HTML (header, main, footer) for clarity and accessibility.
- Added lightweight CSS in a style block so the page looks polished without requiring a build step.

## hello.html Content and Structure

- Document setup: HTML5 doctype, lang="en", UTF-8 charset, responsive viewport, and a short description meta tag.
- Layout:
  - header: page title and a short tagline.
  - main: welcoming message and brief context linking back to the repository.
  - footer: small “pill” label and an Issue #1 note.
- Styling:
  - Responsive typography via clamp().
  - Centered “card” container with subtle border, blur, and shadow.
  - Gradient background and an accent link color for a modern, professional look.

## Design Decisions

- Chose system UI fonts for good cross-platform rendering.
- Prioritized readability and contrast, with simple hover/focus styling for links.
- Avoided external assets and frameworks to keep the page fast and easy to maintain.
