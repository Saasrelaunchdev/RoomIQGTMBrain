---
description: QA a draft against the RoomIQ brain
argument-hint: <path to the draft>
---
Run `python3 tools/brain.py lint $ARGUMENTS`, fix every error, then tick each item of ops/QA-checklist.md against the draft by reading it. Report each failed item with the fix, every capability mentioned with its status from rules/feature-status.md, and the rule the draft came closest to breaking.
