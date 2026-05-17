# Documentation Inventory

This directory holds durable project context for coding agents and humans.

Use this file as the map for Markdown files under `docs/`. Feature specs are indexed separately in `../specs/INDEX.md`.

## Inventory

| Document | Role | Update When | Retirement Rule |
| --- | --- | --- | --- |
| [agent-context-stack.md](agent-context-stack.md) | Context lookup order and optional tool layers. | Agent context sources or question-reduction workflow changes. | Supersede with an ADR if the workflow changes materially. |
| [agent-methodology.md](agent-methodology.md) | Research notes and methodology references for agent use. | A referenced method is adopted, rejected, or replaced. | Move stale research to an ADR consequence or remove it after replacement. |
| [context-grounded-workflow-validation.md](context-grounded-workflow-validation.md) | Validation record for context-grounded workflow examples. | Test scenarios, worktree validation, or expected workflow changes. | Archive when replaced by automated evals or CI checks. |
| [publication-readiness.md](publication-readiness.md) | Public-release privacy and baseline review. | Publication criteria or release posture changes. | Keep current for public templates. |
| [adr/](adr/) | Durable decisions and tradeoffs. | A decision changes, is superseded, or needs new rationale. | Keep ADRs immutable except status/link updates. |

## Markdown Lifecycle

Classify new Markdown before creating it.

| Need | Location |
| --- | --- |
| Always-loaded agent behavior | `../AGENTS.md` |
| Tool-specific agent loading | `../CLAUDE.md` or `../.cursor/rules/*.mdc` |
| Visual design system | `../DESIGN.md` |
| Feature behavior, acceptance criteria, or implementation plan | `../specs/<feature>/` and `../specs/INDEX.md` |
| Durable technical decision and tradeoff | `adr/NNNN-title.md` and `adr/README.md` |
| Validation record or research note | `docs/` with a row in this file |

Avoid orphan Markdown. A new durable `.md` file should be linked from the nearest inventory: this file, `adr/README.md`, or `../specs/INDEX.md`.

Prefer status updates and cross-links over moving files. Archive only when search noise becomes higher than historical value.
