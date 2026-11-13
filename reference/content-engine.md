# Content engine, education-led content

Load for: any article, post, video, or newsletter. Every content template points back here. Status: WORKING channel (D-10).

## Thesis
Rent-by-the-room investors learn from each other in public: forums, groups, podcasts, YouTube. They distrust tool marketing and trust worked examples. So RoomIQ content teaches the underwriting method first, shows the product second, and never asks for trust it has not earned with arithmetic.

## How the channels feed each other
1. Community answers surface the questions people actually ask (signal type LANGUAGE).
2. Repeated questions become articles and short videos (Campaign 2).
3. Articles carry one call to action into a demo or a trial (stage 3 to 4).
4. Demos produce objections and proof requests, which return to the signal log and sharpen the next piece.

## Archetypes to rotate
- **The worked example.** One house, one question, the numbers shown. Covered metro only.
- **The method piece.** How to think about one underwriting variable (room mix, shared-bath pressure, fill speed).
- **The myth check.** A common rule of thumb, tested against what the evidence shows. Only with numbers RoomIQ can show on screen.
- **The honest limitation.** What RoomIQ does when evidence is thin, and why the label matters.
- **The operator teardown.** Room segments of a property explained (blurred host and photos).

## Plan, write, edit
**Plan.** One reader (A or B), one stage, one question, one takeaway sentence, one call to action. Name the capability IDs you will mention and confirm their status.
**Write.** Open with the reader's question in their words (pull from `ops/copy-bank.md` customer language once it exists). Teach before you show. Every number carries its unit and window.
**Edit.** Cut the warm-up. Run `python3 tools/brain.py lint`. Check every capability against `rules/feature-status.md`. Read the opening aloud.

## Hook patterns that fit this audience
- A number with its unit: "A shared bath cost this house $72 a week per room."
- A decision: "Garage or two bedrooms? Answer this first."
- A candid limit: "This forecast came back Low confidence. Here is why that is useful."

## Calls to action, one per piece
- "Run your address" (stage 3 to 4).
- "Book a 30-minute underwriting session" (design partners).
- "See how your house compares" (operators).

## Measurement
Per piece: ICP engagement (replies, saves, qualified comments), clicks to the one CTA, demos booked. A piece succeeds on its role, not on views. Log each published piece in `ops/activity-log.md` with the experiment it serves.

## Out of scope
Paid promotion, cold outreach at volume, and any published market statistics until G11 and G12 are answered.
