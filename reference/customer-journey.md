# Customer journey funnels

Load for: matching an asset to a stage, choosing KPIs, planning onboarding. Distills: master context Section 13. Status: WORKING. KPI baselines: not measured yet (`innovation/metrics.md`).

## Investor funnel (Audience A)

| Stage | Mindset | Question they ask | Asset | KPI (baseline pending) | Owner |
|---|---|---|---|---|---|
| 1 Unaware | Running deals on gut and spreadsheets | none | none | none | none |
| 2 Problem aware | "My room rent assumptions are guesses" | How do others underwrite rooms? | Education post, community answer | Engaged readers from ICP | Founder |
| 3 Solution aware | "Room-level evidence exists" | What tools do this? | "Underwrite the room" article, walkthrough video | Visits to the product page | Founder |
| 4 Evaluating | "Will it work on my deal?" | Does it cover my market? How sure is it? | Live demo on their address, trial | Demo-to-trial rate | Founder |
| 5 Activated | "This changed how I see the deal" | Can I trust this enough to act? | First forecast in a covered market, then the Deal Calculator | Activation rate, time to first forecast | Product |
| 6 Habit | Running every candidate deal through it | Can I keep these? | My Underwrites, re-run | Forecasts per active user per week | Product |
| 7 Paid | RoomIQ Pro for the Deal Calculator | Is Pro worth it? | Upgrade prompt at the Deal Calculator | Trial-to-paid rate | Founder |
| 8 Advocate | Sends it to a JV partner | Can I share this? | Exported underwrite | Referred signups | Founder |

**Activation definition (hypothesis A1, tested in EXP-001):** a forecast run on an address in a covered metro that returns better than Low confidence, followed by opening the Deal Calculator in the same session.

**Critical success factor:** the first forecast lands in a covered market.
**Primary blocker:** a first run on an uncovered address (D-Q28), or the data-source question going unanswered.
**Accelerator:** the founder running the prospect's own address live.

## Operator funnel (Audience B)

| Stage | Mindset | Question | Asset | KPI (baseline pending) |
|---|---|---|---|---|
| 1 Unaware | Pricing by feel | none | none | none |
| 2 Problem aware | "A room keeps sitting empty" | What are similar rooms charging? | Community answer, pricing article | ICP engagement |
| 3 Solution aware | "Room-level benchmarks exist" | Is my house in there? | Analyzer walkthrough | Product page visits |
| 4 Evaluating | "Show me my property" | How does my house compare? | Analyzer on a comparable property, visual comps | Searches per trial |
| 5 Activated | "That premium explains it" | What should I change? | Segment premium or visual comp that changes a price | Price changes reported |
| 6 Habit | Weekly check | Which way is it trending? | Rolling windows | Weekly active operators |
| 7 Paid | Pro (OPEN) | Is it worth it? | Upgrade prompt | Trial-to-paid |
| 8 Advocate | Tells their operator group | none | Shareable benchmark | Referrals |

## Stage rules for writers
- Stages 2 and 3: no product claims beyond one line. Teach first.
- Stage 4: product only, one audience, covered markets only.
- Stage 5 onward: in-product copy and lifecycle email. Glossary terms exactly as in the UI.
