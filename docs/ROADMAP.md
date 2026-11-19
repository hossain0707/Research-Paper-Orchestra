# Roadmap

This is a planning document, **not a claim that the features below exist**.

### Current: ChatGPT plugin v1.0

- Five defined workflow roles with structured handoffs
- Evidence/citation/reviewer safeguard guidance
- Input and deliverable contracts
- Private ChatGPT plugin and public source repository
- Offline integrity checks for plugin packaging

### Proposed later: executable orchestration backend

- Python workflow runner with independent worker execution
- Authenticated document and run management
- Semantic Scholar, Crossref and DOI verification adapters
- Reproducible plotting workers with isolated compute
- Template-aware LaTeX compiler sandbox and PDF inspections
- Durable checkpoint/retry, observability, and cost controls
- Research benchmark/evaluation harness and human review UI

These proposed capabilities require implementation, connected provider credentials and end-to-end testing. The original [Google Research PaperOrchestra](https://github.com/google-research/paper-orchestra) provides a separate reference runtime and can be examined under its own license.
