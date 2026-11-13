# Template, landing page

Audience: [A investors / B operators]. Pick one. Never blend.
Funnel stage: [3 solution aware / 4 evaluating]
Voice reference: `examples/landing-hero-investors.md`

1. **Hero.** One promise in the audience's words, from `ops/copy-bank.md`. Subhead names what RoomIQ is and who it is for. One primary call to action.
2. **The problem as they feel it.** Investors: room rents typed into a spreadsheet. Operators: a room that keeps sitting empty. No product yet.
3. **The reframe.** One line from the copy bank reframes section.
4. **What it is.** One paragraph. Room-level, weekly rents, US rent-by-the-room.
5. **Pillar 1.** Headline, then reasons to believe from the audience's value proposition file. SHIPPED capabilities only.
6. **Pillar 2.** Same shape.
7. **Pillar 3.** Same shape. PARTIAL capabilities: describe the visible part only.
8. **How it works.** Three or four steps that match the real flow (Dashboard, Analyzer, Predictor).
9. **Show the evidence.** One screenshot from a covered metro, host names and photos blurred, formula and confidence label visible.
10. **Objections.** The two from `reference/objection-handling.md` that this stage raises, usually data source and accuracy.
11. **Proof.** `[PROOF POINT NEEDED]` until the closed set holds customer proof.
12. **Comparison.** Honest, using `reference/competitor-battlecards.md`, rival strength first.
13. **FAQ.** Real questions, including "not yet" answers. No prices.
14. **Close.** Same call to action as the hero.

## Guardrails
One audience. Every capability checked in `rules/feature-status.md`. "Any US address" carries the fallback clause. No accuracy, coverage, data-source, or price claims (`rules/do-not-say.md`). Run `python3 tools/brain.py lint` and `ops/QA-checklist.md` before shipping.
