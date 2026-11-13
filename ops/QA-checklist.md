# QA checklist, run before shipping any output

Every item is answerable yes or no by looking at the draft. Run the mechanical part first: `python3 tools/brain.py lint <draft.md>` catches em dashes, banned words, superlatives, ledger phrases, and mentions of non-shipped capabilities. Then tick the rest by reading.

## Writing
- [ ] No em dashes anywhere.
- [ ] None of the banned words in `rules/writing-rules.md`, including "leverage" in its finance sense.
- [ ] Paragraphs of one to three sentences, point first.
- [ ] Every number carries its unit and window (per room per week, per property per month, last 90 days).
- [ ] No emoji.

## Channel
- [ ] The asset is for an in-scope channel in `rules/writing-rules.md`. Paid ads or cold outreach at volume: stop and redirect.
- [ ] No market statistics published as a dataset or report (data rights open, G11 and G12).

## Claims
- [ ] No accuracy language about forecasts. Transparency language only.
- [ ] "Any US address" always carries the fallback clause in the same sentence.
- [ ] No coverage numbers, no named data source, no partner or affiliation claim.
- [ ] Every capability mentioned is checked in `rules/feature-status.md`. UNVERIFIED ones are named, never described. ROADMAP ones are absent.
- [ ] No price, trial, limit, or tier name other than `RoomIQ Pro`.
- [ ] No proof point outside the closed set in `ops/copy-bank.md`. Gaps marked `[PROOF POINT NEEDED]`.
- [ ] Revenue is "estimated rental revenue", never income or earnings.
- [ ] Every financial output carries "for information, not financial advice" on the same surface.
- [ ] House rules and resident criteria reference no protected class.
- [ ] Every "only", "first", "best", "never", "most", "fastest" checked against `rules/do-not-say.md`.

## Naming and strategy
- [ ] Module and metric names match `rules/glossary.md` exactly ("Property Predictor", "Evidence Quality", "coliving").
- [ ] "Forecast" names the output; "baseline profile" names the inputs.
- [ ] No framing that contradicts `ops/decisions.md`, including WORKING decisions.

## Audience and stage
- [ ] One audience only: investors or operators. Not both.
- [ ] Copy matches one funnel stage in `reference/customer-journey.md`.

## Demos, video, screenshots
- [ ] Demo address is in a well-covered metro, never an uncovered one.
- [ ] No known defect on screen (D-Q26 banner, Deal Calculator defaults, closet visual comps).
- [ ] AI concepts shown with the watermark visible.
- [ ] Host names and listing photos blurred in anything public.
- [ ] Confidence and support labels read out loud, not skipped.
- [ ] Nothing UNVERIFIED is shown as if a customer can do it today.

## Voice
- [ ] Reads like the matching file in `examples/`.
- [ ] One line at the end names the rule the draft came closest to breaking.

## After shipping
- [ ] Asset filed in `pages/` or listed in `ops/asset-index.md`.
- [ ] An entry in `ops/activity-log.md` with the experiment or assumption it tests.
- [ ] Anything the work taught you logged in `ops/signal-log.md`.
