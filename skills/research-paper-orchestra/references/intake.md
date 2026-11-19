# Evidence intake specification

Collect (or infer only where reliably provided):

- Working title, problem, research question, novelty target, domain, hypotheses.
- Venue type, year/version, template source, page limit, anonymity and disclosure policy.
- Source inventory: experiment logs/tables, protocol, code and environment, hardware/dataset provenance, figures, related references and earlier draft.
- Results inventory per metric: dataset and split, n, seeds, unit, method/baseline, variance or confidence interval, run ID, code/experiment provenance.
- Authors and affiliations only if explicitly supplied; else leave anonymized or omit.
- Whether the paper reports studies of human participants, animal data, medical outcomes, or identifiable data; if yes, report required ethics/consent information as *missing* unless evidenced.

A missing target venue should not block a generic paper draft. A missing log should block measured-result claims only, not a structured proposal. A missing verified source should block citation assertions only. For revisions, preserve existing manuscript claims unless contradicted, and report contradictions rather than silently deleting them.

Evidence ledger fields: `id,claim_or_measurement,source_file_or_url,location,confidence_tag,verification_action,limitations,used_in_section`.

Scientific claim gate: measured numeric result needs exact evidence or derived formula and source. Distinguish raw data, derived statistics, prior-work claims, and author's interpretation. Treat citation entries without primary or indexed verification as `UNVERIFIED`.
