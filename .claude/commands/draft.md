---
description: Draft a RoomIQ asset (landing page, one-pager, article, post, community answer) against the brain
argument-hint: <asset type> for <investors|operators>, stage <n>, <details>
---
Load the control layer named in CLAUDE.md, then the files `python3 tools/brain.py load <task> --paths` lists for this asset type. Draft the asset described here: $ARGUMENTS

Use the matching template in templates/ and match the voice of the matching file in examples/. One audience only. Then run `python3 tools/brain.py lint` on the draft, fix every error, check each warning against rules/, and tick ops/QA-checklist.md. Return the draft, the capability statuses you relied on, and the rule it came closest to breaking.
