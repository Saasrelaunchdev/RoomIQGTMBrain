# Trust and risk register

Load for: legal-adjacent copy, disclaimers, sourcing questions, AI disclosures, financial outputs, house rules, and reviewing anything a regulator, platform, or lender might read. Distills: S2 working notes section 7 (dependencies) and section 9 (QA). This is not legal advice; it is the list of exposures the copy must respect until counsel reviews them.

## Exposures, ranked by consequence

| # | Exposure | Why it matters | Copy rule today | Gap |
|---|---|---|---|---|
| T1 | Listing data provenance and terms | Core to the product and to any public statistic | Never name or imply a source or partner | G11 |
| T2 | Third-party listing photos and host names on screen | Rights to display; privacy | Blur in public assets | G12 |
| T3 | AI derivatives of listing photos | Copyright and platform rules on altered photos; deceptive advertising | Concepts always watermarked and labeled; never used as listing photos | G12 |
| T4 | Forecast and financial outputs | Investors and lenders act on them | No accuracy claims; "for information, not financial advice" on every financial surface | G14 |
| T5 | House rules recommendations | Fair housing; local occupancy and rooming-house law | No protected-class references; "not legal advice" | C24 UNVERIFIED |
| T6 | FEMA flood layer | Misread as an insurance determination | "Not an insurance or regulatory determination" | C07 UNVERIFIED |
| T7 | Map tiles and geocoding at scale | Commercial terms of basemap and geocoder providers | Keep OpenStreetMap attribution visible | Provider unknown |
| T8 | Privacy choices and consent | US state privacy laws | Do not describe privacy features beyond the link | B8 |

## Verbatim disclosures already in the product (keep exactly)
- Revenue: "Based on observed rents and occupancy, not collected payments."
- AI concept banner: "AI-GENERATED - NOT ACTUAL PROPERTY CONDITION"
- AI concept economics: "Concept visualization" with "no validated economics for this edit yet."
- Scenarios: "Revenue assumptions, not a calibrated prediction interval."
- Map: "Market metrics only count live listings."
The full AI disclaimer sentence is quoted in `rules/do-not-say.md`.

## Disclosures the brain adds to marketing surfaces
- Deal math: "For information, not financial advice."
- House rules: "Not legal advice. Confirm local rules."
- Any forecast in marketing: the fallback clause and the confidence label, together.

## Trust assets RoomIQ already has (use them)
The product's own candor is the strongest trust asset: printed formulas, labeled support and confidence, disclosed comp distance, separated local and expanded comps, excluded soft signals, reconciling numbers, watermarking. Lead with them; never oversell past them.

## Fair housing note for every writer
Rent-by-the-room listings often carry house rules. RoomIQ copy never suggests rules or resident criteria tied to race, color, religion, sex, national origin, familial status, disability, or state-protected classes such as source of income. If a generated house-rule recommendation ever contains one, log it as a RISK signal immediately (threshold: 1 verified instance).
