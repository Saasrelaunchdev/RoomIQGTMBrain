# Example, investor landing page (hero to first pillar)

Status: draft gold standard, checked against ledgers 2026-11-13, founder approval pending.
Audience: A, acquiring investors. Stage: 3 to 4. Template: `templates/landing-page.md`.

---

**Underwrite the room, not just the house.**

Room-level revenue forecasts with the formula, the comps, and the confidence on screen.

[Run your address]

---

You have a house in diligence and a room rent number in a spreadsheet. Maybe it came from a listing you saw, maybe from a rule of thumb. Either way, the deal rests on it.

RoomIQ starts from observed weekly room rents and room occupancy instead. And it tells you how far to trust the result.

**A forecast that shows its work.** Enter an address and your room mix. RoomIQ forecasts monthly revenue and prints the formula under it: weekly room price, times rooms, times occupancy, times 4.35 weeks. Beside the number you see how many comps it used, how far away they are, and a confidence label. Where nearby evidence is thin, it says fallback support, so you know before you make an offer.

**Rooms earn differently. RoomIQ shows how.** In a tracked house, a private-bath room and a shared-bath room rarely rent for the same. RoomIQ breaks properties into room segments by bathroom and size, with each segment's weekly price and 90-day occupancy.

**Start where rooms fill.** Rank US markets by a 0 to 100 Market Score, check seasonality of occupancy and fill speed, and see which submarkets have strong evidence and which are thin.

---

*Estimates are based on observed rents and occupancy, not collected payments. Deal math is for information, not financial advice.*

---

## Why this works
- The problem is stated in the investor's own situation (a house in diligence, a spreadsheet number) before the product appears.
- The flagship claim (C27) appears once, in the body, with the fallback clause in the same paragraph. An earlier draft put "any US address" in the subhead without the clause; `tools/brain.py lint` flagged it and the subhead was rewritten.
- It sells transparency, which is SHIPPED, instead of accuracy, which is banned.
- Every capability named is SHIPPED (C27, C14, C02 as PARTIAL named only by its visible parts, C03, C05).
- No numbers appear that a reader could mistake for proof; the 4.35 weeks factor is product behavior.
- One call to action, repeated nowhere else in the block.

Rule this came closest to breaking: "Rooms earn differently" edges toward a general claim; it stays safe because it describes what the segment view shows rather than a market-wide statistic.
