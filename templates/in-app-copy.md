# Template, in-app copy

For engineers and designers editing UI strings, empty states, errors, tooltips, banners, and paywall prompts in the RoomIQ product. Also the guardrail spec for any LLM-generated text shown inside the product.

## String review fields
| Field | Value |
|---|---|
| Location | Module, step, component |
| Current string | verbatim |
| Proposed string | verbatim |
| Glossary terms used | from `rules/glossary.md` |
| Ledger check | capability IDs and status |
| Reason | defect ID or rule |

## Rules for product strings
- Use glossary terms exactly: Forecast for the output, baseline profile for the inputs.
- Plurals: "1 result", "2 results"; "1 room", "2 rooms".
- Subject-verb agreement in generated sentences: "Only 1 of 3 bedrooms has".
- Every banner that explains a number must agree with the number on the same screen.
- Empty states say what to do next in one sentence.
- Tooltips define, never sell. Pull definitions from `reference/metrics-methodology.md`, verified rows first.
- Paywall prompts say what Pro adds, never prices until D-11 closes.

## Rules for LLM-generated text inside the product
- House-rule recommendations: never reference a protected class. Conduct and property use only.
- Recommendations never promise rent, occupancy, or returns.
- Every generated recommendation carries its evidence basis or says it has none.
- Run outputs through `python3 tools/brain.py lint` in tests; treat any hit on a hard ban as a failing test.

## Guardrails
`rules/glossary.md`, `rules/do-not-say.md`, `rules/feature-status.md`. Matching example: `examples/in-app-copy-fixes.md`.
