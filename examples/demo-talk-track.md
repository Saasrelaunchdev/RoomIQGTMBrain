# Example, demo talk track (investor, Predictor segment)

Status: draft gold standard, checked against ledgers 2026-11-13, founder approval pending.
Audience: A. Template: `templates/demo-script.md`. Written for the ear.

---

**[Predictor, Location step, Dallas address tested this morning]**

So this is the house you sent me. I've typed the address. Before we forecast anything, look at this panel. It counts active coliving properties within about three miles. That's your competition for residents, before we've run a single number.

**[Baseline Profile]**

Now the house itself. Townhouse, four bedrooms, two baths. I'm going to enter every room, because the forecast is only as good as the room mix. This one has a private bath. The other three share.

See this tile? Shared-bath pressure. Three rooms on one shared bath. That number matters more than people think.

**[Run Forecast]**

Model routing is on automatic. This house isn't tracked, so RoomIQ takes the bounded underwriting path. The evidence window is 270 days. Let's run it.

**[Results]**

Here's the monthly revenue. And here's the part I like. Read the line under it. Weekly room price, times rooms, times occupancy, times 4.35 weeks. That's the whole formula. No black box.

Now these two labels. Support level, and confidence. **[Read today's two labels aloud, exactly as shown.]** If this were a thin market, it would say fallback support, and the confidence could read Low. It tells you that up front.

These scenarios on the left? Plus and minus ten percent. It says right there, not a prediction interval. They're assumptions you can edit.

**[Hand-off]**

So that's what each room can earn here, and how much to trust it. Want to take it into the Deal Calculator with your financing?

---

## Why this works
- Every on-screen label is read before it is interpreted.
- The confidence and support labels are spoken, not skipped, and the thin-market case is named.
- Every room is entered first, which avoids D-Q26 on screen.
- The address is pre-tested in a covered metro (D-06). The script never names a confidence level other than Low, because Low is the only level seen in the product so far (`rules/glossary.md`).
- Short spoken sentences, second person, one idea per line.

Rule this came closest to breaking: "No black box" leans toward a superlative; it holds because the formula is literally printed (screen 14).
