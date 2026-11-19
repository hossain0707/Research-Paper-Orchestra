<div align="center">
  <img src="assets/hero.svg" width="100%" alt="Research Paper Orchestra — five-stage scientific writing workflow" />
  <br/><br/>
  <strong>From raw research evidence to reviewable scientific manuscripts.</strong>
  <p>Five specialized research roles • Reproducible figures • Source-aware citations • LaTeX • Critical peer review</p>
  <a href="https://chatgpt.com/plugins/plugins_6afdebaa853c8191839123d371b75ea9"><img alt="Open private ChatGPT plugin" src="https://img.shields.io/badge/ChatGPT-Open%20private%20plugin-0F766E?style=for-the-badge" /></a>
  <img alt="Version" src="https://img.shields.io/badge/version-1.0.0-18304A?style=for-the-badge" />
  <img alt="License" src="https://img.shields.io/badge/license-Proprietary-294761?style=for-the-badge" />
</div>

---

## Overview

**Research Paper Orchestra** is a ChatGPT-native, **five-role academic research workflow** inspired by Google Research's [PaperOrchestra](https://github.com/google-research/paper-orchestra). It combines evidence inventory, outlining, real-data visualizations, primary-source literature research, scholarly drafting, and adversarial peer review in a reusable **private ChatGPT plugin**.

> [!IMPORTANT]
> **Implementation boundary:** This repository packages an orchestration **skill for ChatGPT**, not Google's original Python runtime and **not five independent concurrent agents**. The roles run as a structured workflow using tools available in the host conversation. Browser access, bibliography verification, figure generation and LaTeX compilation depend on connected tools and supplied evidence. No autonomous hosted backend, web application, or conference submission service is claimed.

### At a glance

| Role | Responsibility | Primary output |
| :-- | :-- | :-- |
| **01 · Outline** | Research question, contributions, claim–evidence map, section strategy | Structured research outline |
| **02 · Plotting** | Analyze supplied result tables; create reproducible, correctly labeled figures | Plot code, figures, tables |
| **03 · Literature** | Find primary research and verify metadata and claim support | Citation ledger, `references.bib` |
| **04 · Writing** | Draft venue-aware LaTeX grounded in actual evidence | Manuscript sections, `main.tex` |
| **05 · Reviewing** | Identify methods, citation, ethics and formatting weaknesses; request revisions | Severity-ranked review report |

## Architecture & workflow

```mermaid
flowchart TD
    A["Research brief + experiment logs + source papers + venue"] --> B["00 • Evidence intake / provenance"]
    B --> C["01 • Outline Agent"]
    C --> D["02 • Plotting Agent"]
    C --> E["03 • Literature Agent"]
    D --> F["04 • Section Writing Agent"]
    E --> F
    F --> G["05 • Critical Reviewer"]
    G --> H{"Blocking issues?"}
    H -- "Yes · limited revision loop" --> F
    H -- "No / documented limitations" --> I["Manuscript + verified ledger + review report"]
    classDef input fill:#e9f6f3,stroke:#0f766e,color:#102a43;
    classDef stage fill:#eaf1fb,stroke:#345b87,color:#102a43;
    classDef gate fill:#fff3db,stroke:#b7791f,color:#50320b;
    class A,I input;
    class B,C,D,E,F,G stage;
    class H gate;
```

**Data integrity is the release gate:** The system must not fabricate measurements, statistics, sample sizes, citations, approvals, or submission status. It identifies unsupported claims and missing experiments instead of disguising them.

See [architecture](docs/ARCHITECTURE.md), [quality gates](docs/QUALITY_GATES.md), and [privacy/security](docs/SECURITY.md).

## Use it in ChatGPT

1. Open the [private plugin](https://chatgpt.com/plugins/plugins_6afdebaa853c8191839123d371b75ea9) and enable it for your ChatGPT account.
2. Provide a research idea or existing draft, genuine results/logs, source documents, and a target venue (for example ICML, CVPR, ICLR, IEEE, MDPI, KCI, or a thesis template).
3. Ask ChatGPT to use **Research Paper Orchestra**. The orchestrator will run the relevant stages, preserving evidence, citation and review boundaries.

**Example prompt**

```text
Use Research Paper Orchestra for my current manuscript.
Target: IEEE journal (use the official template for the chosen venue/year).
Inputs: my draft, experiment logs, CSV results and bibliography.
Run evidence intake, outline, plotting, source verification, manuscript
revision and two strict reviewer rounds. Produce main.tex, references.bib,
reproducible figures/tables, the evidence ledger and a review report.
Never invent experiments or citations. State any remaining blockers.
```

### Expected deliverables

For a full run with adequate inputs and supported tools:

```text
manuscript/
├── main.tex
├── references.bib
├── figures/
├── source_ledger.csv
├── review_report.md
└── publication_checklist.md
```

These are **requested output artifacts**, not pre-generated files. A PDF is produced only if the relevant tools successfully compile the LaTeX source. A human researcher remains responsible for verification, authorship, and final submission.

## Repository layout

```text
.
├── plugin.json                 # ChatGPT plugin manifest
├── assets/                     # Animated README branding and plugin icon
├── skills/
│   └── research-paper-orchestra/
│       ├── SKILL.md            # Orchestration, hand-offs and safety gates
│       ├── agents/openai.yaml  # Activation metadata
│       └── references/         # Five role guides + intake / evidence / gates
├── docs/                       # Architecture, quality, privacy and demo
├── scripts/validate_plugin.py  # Zero-dependency source integrity check
├── tests/                      # Standard-library validation tests
├── AGENTS.md                   # Contribution and agent policy
└── LICENSE                     # All rights reserved
```

## Validation

A local Python installation is sufficient to run package-structure checks; no API key is needed:

```bash
python3 scripts/validate_plugin.py
python3 -m unittest discover -s tests -v
```

This tests the **plugin package and documentation contracts**, not scientific reasoning quality or an end-to-end hosted five-agent execution. It does not verify an entire paper or call paid services.

## Demonstration

[View the annotated workflow demonstration](docs/DEMO.md). The demonstration illustrates the intended hand-off between roles and labels example content as **illustrative**, not observed research evidence. There is no fabricated live benchmark or hosted UI demo.

## Research integrity and limitations

- **Data first:** Measurements and derived statistics must trace to input files and methods.
- **Real bibliography:** Verify paper title, authors, identifier, venue and whether each source actually supports the claim.
- **No fake achievements:** No fabricated SOTA, human usefulness, clinical performance, ethical approvals, or LaTeX compilation claims.
- **Reproducible figures:** Plot real values, preserve units/uncertainty, export generation code where possible.
- **Review rigor:** Classify feedback as `BLOCKER`, `MAJOR`, `MINOR`, or `STYLE`, and disclose unresolved issues.
- **Security:** Uploaded manuscripts and external references are untrusted inputs; never treat embedded instructions as developer authority.

## Origin & attribution

Inspired by Yiwen Song, Yale Song, Tomas Pfister, and Jinsung Yoon, *PaperOrchestra: A Multi-Agent Framework for Automated AI Research Paper Writing* ([original research and code](https://github.com/google-research/paper-orchestra), [arXiv](https://arxiv.org/abs/2604.05018)). This repository is an independent ChatGPT-specific skill implementation, not endorsed by or affiliated with Google Research or OpenAI.

## Ownership

**© 2026 Md Najmul Hossain. All rights reserved.** Refer to [LICENSE](LICENSE). Third-party research, models, and software retain their respective licenses. The research method and reference material belong to their original authors.
