# File deliverables, gates and completion

Preferred output structure for a full manuscript (only files actually generated should be listed):

```
research-paper/
  research_brief.md
  source_ledger.csv
  outline.md
  figure_manifest.md
  literature_matrix.csv
  paper/main.tex
  paper/references.bib
  paper/figures/<reproducible-assets>
  paper/main.pdf                  # only after successful actual compilation
  review_report.md
  revision_log.md
  remaining_blockers.md
```

QC gates:
- **Evidence**: All numeric outcomes trace to a user measurement or transparent derivation.
- **Literature**: Each public citation resolves to its metadata; claim-level support status recorded. Missing verification must be disclosed.
- **Figures**: Generated from real supplied measurements or explicitly marked conceptual/synthetic.
- **Writing**: Introduction claims align with Methods/Results; limitations and research question stated.
- **Peer review**: At least one adversarial reviewer pass; blockers shown, not concealed.
- **Build**: LaTeX PDF generated and opened/checked if tools support. `pdflatex`/`latexmk` exit code alone does not establish complete correctness; inspect warnings, pages and references if possible.
- **Release**: Do not label `submission-ready` if blockers remain. Say `submission-style draft` or `ready for author verification`.

If a requested full manuscript is impossible with current evidence, create the supported pieces immediately and clearly state what is missing. Use user-provided names only; do not invent titles, authors, affiliations or measured results.
