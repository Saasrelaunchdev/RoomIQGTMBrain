# Writing rules

These apply to every word of RoomIQ output: web, decks, scripts, release notes, in-app copy, and AI-generated text inside the product.
last_reviewed: 2026-11-13

## Mechanics
- No em dashes anywhere. Use commas, colons, or two sentences. En dashes stay only inside official metro names ("Dallas–Fort Worth").
- Banned words: leverage, unlock, seamless, robust, streamline, cutting-edge, empower, elevate, revolutionize, game-changing, best-in-class, world-class, supercharge, turbocharge, harness, delve, tapestry, testament, foster, facilitate, utilize, myriad, plethora, pivotal, crucial, vital, skyrocket, effortless, unparalleled, groundbreaking.
- "Leverage" is banned in its finance sense too. Say financing, debt, or loan-to-value.
- Avoid in their figurative sense: landscape, navigate, journey, realm.
- Paragraphs of one to three sentences. Front-load the point.
- Numbers over adjectives. Every number carries its unit and window: "$260 avg weekly asking, last 90 days", never "$260".
- Rents are weekly per room. Revenue is monthly per property. Say which.
- Use the product's own labels, spelled as the UI spells them (`rules/glossary.md`).

## Tone
Plain, numerate, and candid, like a good underwriting memo. The readers put their own money and debt behind a decision, so they trust evidence and distrust hype. When the evidence is thin, say so before they find out: RoomIQ's own UI does this ("Fallback support", "Confidence Low"), and the copy matches it.

Right register: an analyst explaining a comp set. Wrong register: "passive income" real estate marketing, urgency tricks, and lifestyle promises.

## Writing for the ear (demos, video, webinars)
- Short spoken sentences. One clause where you would write two.
- Second person, one listener, contractions.
- Say what is on screen before you interpret it: "This tile shows 87.5 percent occupancy."
- Say confidence labels out loud. Never skip "fallback" or "low confidence" for pacing.
- Read it aloud before it ships. Cut what you stumble on.

## Claim discipline
Check every "only", "first", "best", "never", "most", and "fastest" against `rules/do-not-say.md`. Check every capability against `rules/feature-status.md`: UNVERIFIED capabilities are named, never described. A conditional claim names its condition in the same sentence ("in covered markets", "on RoomIQ Pro", "when local evidence is thin"). Every financial output carries "for information, not financial advice" on the same surface.

## Channel discipline
Working channel mix (G01, pending founder confirmation):
- In: founder-led demos and sales calls, data-led education content, community participation, product-led trial, product and release copy.
- Not yet: paid ads and cold outreach at volume. If asked, say it is out of scope for this go-to-market today and offer the nearest in-scope channel (a community post, a warm follow-up, a content piece).
- Never: publishing market statistics as a dataset or report until data rights are confirmed (G11, G12).

## Signature lines (checked, founder approval pending)
- "Underwrite the room, not just the house."
- "Every number shows its evidence."
- "When the evidence is thin, RoomIQ says so."
- "The math is on the screen."

## Formatting
Prose first. Lists only for real lists. Headlines short and concrete. Sentence case for headings. No emoji in RoomIQ copy, even though listing titles carry them.

## Before returning any draft
Run `ops/QA-checklist.md`, then name in one line the rule the draft came closest to breaking.
