# Example, in-app copy fixes from the discovery QA

Status: proposed string changes, checked against the glossary 2026-11-13, founder and engineering approval pending.
Template: `templates/in-app-copy.md`. Each row cites the QA issue from `sources/extracted/discovery/working-notes.md` section 9.

| QA | Location | Current string | Proposed string | Rule |
|---|---|---|---|---|
| Q27 | Predictor, Results banner | "Only 1 of 3 bedrooms have a room entry" | "Only 1 of 3 bedrooms has a room entry" | Agreement |
| Q26 | Predictor, Results banner | "...so the forecast is based on the full bedroom count with typical rooms." | Copy must match the math. If the forecast uses entered rooms only: "The forecast covers the 1 room entered. Add the other 2 to forecast the whole house." | Banner agrees with the number |
| Q14 | Analyzer, results list | "1 results" | "1 result" | Plurals |
| Q14 | Analyzer, room segments | "1 rooms" | "1 room" | Plurals |
| Q33 | Predictor, locked step 4 | "Run the baseline to [enable] the decision board." | "Run the forecast to open the Decision Board." | Forecast is the output |
| Q33 | Predictor, card title | "Baseline Forecast" | "Forecast" | Forecast is the output |
| Q19 | Media Studio output label | "CONCEPT ·" | "CONCEPT · Add desk" (the preset name) | No empty values |
| Q1 | Dashboard Trends helper | "Index 100 = this country's typical level." | "0% = the national typical level. Higher means stronger." | Units match the axis |
| Q21 | Analyzer, 90-day window | "N/A" | "Needs 180 days of history" | Explain empty states |
| Q23 | Evidence Quality | "MEDIA 9 + 34" | "MEDIA 9 property + 34 room photos" (confirm meaning) | Label every number |

## Why this works
- Each change cites its QA issue, so engineering can trace it.
- Terminology follows `rules/glossary.md`: forecast for the output, Decision Board capitalized as in the UI.
- Q26 is treated as a correctness issue first: the copy follows whatever the math is confirmed to be (G15), not the other way round.
- Bracketed text marks a word the brain does not reproduce; the founder fills in the exact current string.

Rule this came closest to breaking: the Q1 and Q23 proposals assume a meaning that is not yet confirmed; both are flagged for confirmation.
