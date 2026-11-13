# Template, release note

Audience: existing users (A and B may share a changelog; individual notes target one). Capability IDs touched: [C..]. Status change: [from X to Y].

## Order of operations (before writing a word)
1. Update `rules/feature-status.md` for every capability this release touches.
2. If a defect in "Known defects that gate claims" is fixed, remove it there and in `reference/demo-playbook.md`.
3. Then write the note.

## Structure
- **Title.** What changed, in the product's own labels.
- **What you can do now.** One to three sentences, present tense, SHIPPED only.
- **Why it matters.** One sentence tied to a job in `reference/icp-personas.md`.
- **Where to find it.** Module and step, exactly as labeled in the UI.
- **Limits.** Anything partial, said plainly.

## Rules
No "coming soon" lists in a release note. No accuracy claims for model changes; describe what changed in the method or the labels. Glossary terms exactly.

## Guardrails
Ledger before copy, always. Lint and QA before publishing. Log the release as an activity (type RELEASE).
