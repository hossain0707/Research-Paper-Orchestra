# Quality gates and release criteria

Each research claim should have a traceable evidence source. These checks guide the workflow; they are **not** machine-enforced guarantees of scientific correctness.

| Gate | Requirement | Failure output |
| --- | --- | --- |
| G0: Intake | identify real source files, versions, venue and missing inputs | input gap report |
| G1: Claim mapping | each contribution has an experiment, source, or explicit proposal status | unsupported-claim register |
| G2: Figures | only real measurements; units, baselines and uncertainties where relevant | figure specification rather than false chart |
| G3: Citations | title, authors, publication venue, year, identifier and claim support reviewed | provisional references flagged |
| G4: Draft | LaTeX sections consistent with evidence and target guidelines | unfinished draft and open questions |
| G5: Critical review | classify findings: BLOCKER, MAJOR, MINOR, STYLE | prioritized review report |
| G6: Re-review | targeted fixes checked; no evidence invented to close blockers | outstanding issues |
| G7: Export | output artifacts exist; PDF compilation reported only if run | source-only handoff |

## Labels

- **Draft:** document assembled but evidence checks may be open.
- **Reviewed draft:** reviewer report written and fixes tracked; not proof of publishability.
- **Submission-style manuscript:** formatted to the available template, not an acceptance prediction.
- **Submission-ready:** use only after author verifies all claims, figures, references, ethics, authorship and venue rules; ChatGPT must not certify this automatically.

## Verification and testing

The repository's offline validator checks required manifests, role references and metadata. It does **not** demonstrate citation precision, LLM benchmark performance, LaTeX compilation, journal compliance or five independent agent processes. Those require separate integration tests and human scientific review.
