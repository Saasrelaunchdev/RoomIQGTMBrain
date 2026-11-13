# Do not say

The claim hygiene spine. Left column is forbidden or risky; right column is the safe replacement. Quoted phrases on the left are matched by `tools/brain.py lint`.
last_reviewed: 2026-11-13

## Hard bans

| Do not say | Say instead |
|---|---|
| Accuracy: "accurate forecast", "precise", "predicts revenue", "within X%", "proven model" | "Every forecast shows its formula, its comps, and a confidence label." No backtest exists (G14). |
| Universal coverage: "any market", "every property", "complete coverage", "all US markets" | "Underwrite any US address. Where nearby evidence is thin, RoomIQ labels the forecast fallback support and shows its confidence." |
| Coverage numbers: "properties tracked", "rooms tracked", "thousands of listings" | Nothing until G13 is answered. Screenshot counts (412 in DFW) are one capture, not a claim. |
| Data source: "PadSplit data", "scraped", "official data", "partnered with", "integrated with" | "Built from observed room listings in the markets RoomIQ covers." Never name or imply a source or partner (G11). |
| Real time: "real-time", "live data" | "Metrics show their as-of date." |
| Income language: "income", "earnings", "collected rent", "cash flow guaranteed" | "Estimated rental revenue, based on observed rents and occupancy, not collected payments." |
| Financial advice: "best deals", "guaranteed returns", "will cash flow", "bank-approved", "lender-ready" | "Model cash flow, cash-on-cash, DSCR, and cap rate from the forecast and your own inputs. For information, not financial advice." |
| Legal status: "legal in your city", "compliant", "zoning approved", "local law" | "Compare an operating checklist with recorded local policies. Not legal advice; confirm local rules." |
| AI everywhere: "AI-powered", "AI predicts", "machine learning forecast" | Name the capability. Only visual comps and AI concepts carry AI framing (G19). |
| AI concepts as results: "after photo", "your renovated room", "see the results", "boost rent by" | "Preview an AI concept of an upgrade, watermarked as AI-generated. No validated economics yet." |
| Visual comps as value: "worth the same", "value comps", "equally valuable" | "Rooms that look like this one, with their weekly price and days to fill." |
| Market Score internals: "Market Score measures", "based on demand and supply" | "A 0 to 100 Market Score with a letter grade." (G18) |
| Prices and limits: "pricing starts at", "plan costs", "free trial", "unlimited plan", "money-back" | Nothing. Pricing is undecided (G07). `RoomIQ Pro` may be named as shown. |
| Invented proof: testimonials, customer counts, "investors trust", "users earn" | The closed proof set in `ops/copy-bank.md`. Customer proof today: none. Write `[PROOF POINT NEEDED]`. |
| Unverified features described: what amenity ROI, house rules, rent guidance, layouts, cohorts, or forecasts return | Name them as present in the product. Describe output only after status moves to SHIPPED. |
| Flood: "flood risk score", "insurance determination" | "Check the FEMA flood hazard layer on the map. Not an insurance or regulatory determination." |
| Category confusion: "Airbnb", "short-term rental", "vacation rental" | "rent-by-the-room", "weekly room rents". |

## Fair housing, never negotiable
House rules, ads, and resident criteria never reference race, color, religion, sex, national origin, familial status, disability, or any class a state adds (often source of income). Do not say "women only", "no kids", "Christian home", "no vouchers". Say instead: rules about conduct and use of the property, applied to every resident.

## In demos, video, and screenshots
- Demo only in well-covered metros (Dallas, Austin, Houston, Atlanta, Phoenix, Tampa). Never an uncovered address (D-Q28).
- Never show the Q26 banner, the Deal Calculator defaults, or a closet visual comp as a talking point.
- AI concepts appear with the watermark visible. Never crop it.
- Public screenshots blur host names and listing photos until G12 is answered.
- Verbatim product disclaimers stay verbatim: "Based on observed rents and occupancy, not collected payments." and "AI-generated concept for visualization only — this image does not depict the actual current condition of the property."

## Claims that need scoping (verify before print)
- **"The only room-level analytics tool."** Counter-example: platform-native host tools show room price against the metro average and a market map; SFR Analytics published room-for-rent aggregates. Safe form: "Analytics built at the room level: weekly room price, room occupancy, fill speed, and bath and size segments."
- **"First AI underwriting for coliving."** Unverifiable. Hard ban.
- **"Better than AirDNA."** Counter-example: AirDNA has deeper short-term rental history. Safe form: "AirDNA is built for nightly stays. RoomIQ models weekly room rents and room occupancy."
- **"Transparent forecasts."** Holds. The formula, support level, comp distance, and confidence are on the results screen (screen 14).
- **"Underwrite any US address."** Holds only with the fallback clause attached in the same sentence.

## Historical and reputational material
None known (G08). Do not repeat rumors about any marketplace or competitor. Platform-specific claims about rivals come only from `reference/competitor-battlecards.md`, dated.
