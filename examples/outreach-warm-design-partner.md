# Example, design-partner invitation (warm)

Status: produced 2026-11-13 as the Phase 9 live test, using only the brain. Checked against ledgers; founder approval pending.
Audience: A, acquiring investors. Template: `templates/outreach-warm.md`. Campaign 1, experiment EXP-001.
Relationship: the investor asked a public question about room rents on a house they are evaluating.

---

**Subject:** Your question about the [city] townhouse

Hi [first name],

You asked in [community] how to sanity-check the room rents on the [city] townhouse you're looking at.

I'm building RoomIQ, and I'd like to run that address with you in a 30-minute session. You'd see a room-level forecast, the formula behind it, the comps it used and how far away they are, and a confidence label.

If nearby evidence is thin for that address, it will say fallback support, and we can talk through what that means for your number.

I'm doing this with ten investors who have a live deal. In return, tell me afterwards what you decided and why. Would [day, time] or [day, time] work?

[Founder name]

---

## Why this works
- It opens on their question, in their situation, before RoomIQ appears.
- One offer, one ask, under 120 words, no attachment, no price.
- C27 is SHIPPED and described only as screen 14 shows it: formula, comps, comp distance, confidence.
- The fallback clause is stated before they find it themselves, which is the brand's candor in practice.
- "Tell me what you decided and why" is the EXP-001 learning built into the ask.

## Live test record
- `python3 tools/brain.py lint`: 0 errors, 3 superlative warnings, all reviewed and none a claim ("only" in this record, "first" in the `[first name]` placeholder). C27 reported as SHIPPED.
- Length: the first draft ran 124 words against the template's limit of 120; one sentence was cut.
- `ops/QA-checklist.md`: passed for writing, channel (warm, not cold), claims, naming, audience, and voice.
- Gaps the brain could not fill: the founder's sign-off name and a booking link. Both are founder inputs; the product URL is already an open item in `ops/asset-index.md`. Logged as activity ACT-0005.

Rule this came closest to breaking: "ten investors" is a program size, not a proof point; it stays because it describes the offer, not a result.
