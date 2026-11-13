## What changed in the brain

<!-- One or two sentences. Name the signal, experiment, or founder answer that triggered it. -->

## Type
- [ ] PATCH (copy only: copy bank, templates, examples, reference wording)
- [ ] AMEND (a ledger in rules/, positioning, ICP, channels, or pricing)
- [ ] Intake (signal or activity entries only)
- [ ] Tooling (tools/, schemas/, adapters template, CI)

## AMEND checklist, in this order
- [ ] Ledger in `rules/` updated, `last_reviewed` bumped
- [ ] Master context section updated, `version`, `last_updated`, `status_notes` revised
- [ ] Dated entry in `ops/decisions.md`, including "What this does not change"
- [ ] Old phrasing searched and replaced in `ops/copy-bank.md`, templates, examples
- [ ] `adapters/portable-control-layer.md` regenerated and dated
- [ ] `python3 tools/brain.py build` and `python3 tools/brain.py adapters --write` run
- [ ] Affected live surfaces from `ops/asset-index.md` listed with owners

## Checks
- [ ] `python3 tools/brain.py audit` passes
- [ ] Any new customer-facing copy passed `python3 tools/brain.py lint` and `ops/QA-checklist.md`
