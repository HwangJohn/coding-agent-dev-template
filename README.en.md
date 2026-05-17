# Coding Agent Python Template

English | [한국어](README.md)

A Python project template for teams that use coding agents such as Codex, Claude Code, and Cursor.

The template has three core principles.

- Keep always-loaded agent instructions short and shared.
- Move repeated procedures and long references into skills, specs, references, or ADRs only when needed.
- Enforce mandatory quality requirements with formatter, linter, type checker, tests, and CI rather than prose alone.

## Usage

Initial setup:

1. Copy this template into a new project root.
2. Rename the project, package, description, `src/`, `tests/`, and README content.
3. Put shared team agent rules in `AGENTS.md`.
4. Claude Code reads `CLAUDE.md`, which imports `@AGENTS.md`.
5. Cursor reads `.cursor/rules/*.mdc`, which point back to `AGENTS.md` and `DESIGN.md`.
6. Python implementation, tests, dependencies, and CI follow the toolchain and standards in `AGENTS.md`.
7. For UI, dashboards, or documentation sites, read root `DESIGN.md` first and follow its tokens and component guidance.
8. When project structure, tools, or workflows change, update `AGENTS.md` or `docs/adr/` in the same change.
9. Add `skills/<name>/SKILL.md` only when a repeated workflow is too long or conditional for `AGENTS.md`.
10. Run the quality gate.

```powershell
uv sync --dev
uv run ruff format --check .
uv run ruff check .
uv run pyright
uv run pytest
```

Ongoing agent-instruction maintenance:

1. When recurring agent mistakes, review comments, or team preferences appear, first decide whether a deterministic check can enforce them.
2. If every agent should always know the rule, put it in `AGENTS.md`.
3. If only tool-specific loading differs, keep it thin in `CLAUDE.md` or `.cursor/rules/*.mdc`.
4. If the workflow is long and conditional, create a candidate `skills/<name>/SKILL.md`.
5. Include trigger examples, near-miss examples, expected behavior, and validation steps for skill candidates.
6. Compare meaningful skill changes against the previous skill or no-skill behavior, then review them before sharing.
7. Retire or simplify skills when the base model handles the workflow reliably without them.

## Standards And Roles

| Standard | Template File | Role | Source |
| --- | --- | --- | --- |
| AGENTS.md | `AGENTS.md` | Shared operating contract for coding agents. | https://agents.md/ |
| Claude Code memory | `CLAUDE.md` | Thin Claude Code adapter that imports `@AGENTS.md`. | https://code.claude.com/docs/en/memory |
| Claude Code skills | `.claude/skills/<name>/SKILL.md` | Claude Code skill loading target or Claude-specific extension point. | https://code.claude.com/docs/en/skills |
| Agent Skills spec | `skills/<name>/SKILL.md` | Public skill format for compatible agents. | https://agentskills.io/specification |
| Agent Skills CLI | `skills/`, `.claude/skills/`, `.agents/skills/` | Install, update, and link skills across agent-specific paths. | https://github.com/vercel-labs/skills |
| Skill evaluation | `evals/` or validation notes | Validate whether a skill triggers correctly and improves repeated outcomes. | https://agentskills.io/skill-creation/evaluating-skills |
| GitHub Spec Kit | `.specify/`, `specs/<feature>/` | Spec-driven development flow for multiple coding agents. | https://github.github.io/spec-kit/ |
| Kiro specs | `.kiro/specs/<feature>/` | Kiro-specific requirements, design, and task artifacts. | https://kiro.dev/docs/specs/ |
| Cursor rules | `.cursor/rules/*.mdc` | Cursor-specific always-on and scoped loading rules. | https://docs.cursor.com/en/context |
| DESIGN.md | `DESIGN.md` | Google Labs DESIGN.md visual design system for UI work. | https://github.com/google-labs-code/design.md/blob/main/docs/spec.md |
| ADR | `docs/adr/` | Durable decisions and tradeoffs too long for `AGENTS.md`. | https://adr.github.io/ |
| Python packaging | `pyproject.toml` | Single entry point for package metadata and tool configuration. | https://packaging.python.org/en/latest/guides/writing-pyproject-toml/ |
| uv | `.python-version`, `uv.lock`, `pyproject.toml` | Python version, environment, dependencies, commands, and lockfile. | https://docs.astral.sh/uv/guides/projects/ |
| Ruff | `pyproject.toml` | Formatting, import sorting, and linting. | https://docs.astral.sh/ruff/configuration/ |
| Pyright | `pyproject.toml` | Strict type checking in editor and CI. | https://microsoft.github.io/pyright/ |
| pytest | `tests/`, `pyproject.toml` | Behavior validation and coverage. | https://docs.pytest.org/en/latest/goodpractices.html |
| GitHub Actions | `.github/workflows/ci.yml` | Repeats the local quality gate in CI. | https://docs.github.com/en/actions |

## File Structure

```text
.
├── AGENTS.md
├── CLAUDE.md
├── DESIGN.md
├── README.md
├── README.en.md
├── pyproject.toml
├── uv.lock
├── src/
│   └── coding_agent_dev_template/
├── tests/
├── skills/              # Optional source for shared Agent Skills
├── specs/               # Feature-level SDD artifacts, inventory, and templates
│   ├── INDEX.md
│   └── _template/
├── scripts/
│   └── check_agent_docs_freshness.py
├── docs/
│   ├── README.md
│   ├── agent-context-stack.md
│   ├── context-grounded-workflow-validation.md
│   ├── agent-methodology.md
│   ├── publication-readiness.md
│   └── adr/
│       └── README.md
├── .cursor/
│   └── rules/
└── .github/
    └── workflows/
```

## Document Roles

- `AGENTS.md`: defines how agents should work in this repository.
- `skills/<name>/SKILL.md`: optional conditional workflows too long for always-loaded instructions.
- `.claude/skills/<name>/SKILL.md`: Claude Code install target or Claude-specific skill location.
- `DESIGN.md`: defines how UI should look.
- `docs/README.md`: inventory and lifecycle rules for accumulating Markdown documents.
- `docs/adr/README.md`: ADR list, status, and supersession map.
- `specs/INDEX.md`: feature spec inventory with status, implementation links, and test links.
- `specs/<feature>/spec.md`: optional feature-level requirements, plan, and task breakdown managed by SDD tooling.
- `.kiro/specs/<feature>/requirements.md`, `design.md`, `tasks.md`: Kiro-specific spec artifacts.
- `docs/adr/`: durable technical decisions and rationale.
- `docs/context-grounded-workflow-validation.md`: validation record for ADR/spec-based workflow tests.
- `docs/publication-readiness.md`: publication privacy check, baseline review, and future improvement triggers.
- `scripts/check_agent_docs_freshness.py`: detects whether code, workflow, or tooling changes have related agent context updates.

Keep operating guidance, conditional workflows, visual design, feature specs, and decision records separate. Put baseline Python workflow in `AGENTS.md`; move long repeated procedures to skills; reserve root `DESIGN.md` for Google DESIGN.md visual design. Use feature-level SDD artifacts when a feature needs a durable spec.

## Context-Grounded Development

This template expects agents to look for trusted repository evidence before asking users to restate decisions.

Context order:

1. Current user request and explicit constraints.
2. `AGENTS.md`, `CLAUDE.md`, `.cursor/rules/*.mdc`.
3. `specs/INDEX.md` and feature specs in `specs/`, `.specify/`, `openspec/`, or `.kiro/specs/`.
4. `docs/adr/` and [agent-context-stack.md](docs/agent-context-stack.md).
5. Existing code, tests, `pyproject.toml`, and CI.
6. Optional Agent OS, Serena, AICTX, or repo-local memory.

If the answer exists in those sources, the agent should proceed without asking. Ask only when trusted context is missing, conflicting, stale, or insufficient for product policy, public API, migration, security, compatibility, or irreversible design decisions.

| Layer | Tools | Role |
| --- | --- | --- |
| Repo source of truth | `AGENTS.md`, ADRs, specs, tests | Highest-trust local context; reviewable and rollbackable in Git. |
| SDD | GitHub Spec Kit, OpenSpec, Kiro Specs | Stores requirements, plans, tasks, and spec deltas in the repo. |
| Standards discovery | Agent OS | Extracts existing standards and injects them into spec shaping. |
| Code intelligence | Serena MCP | Symbol-aware exploration and semantic editing. |
| Continuity memory | AICTX | Repo-local active task state, decisions, failures, and handoffs. |
| Memory watchlist | Knowns, KnowIt, memd | Structured cross-agent memory candidates. |

Freshness automation starts with detection, not automatic rewriting. `scripts/check_agent_docs_freshness.py` fails when source/tooling changes are staged without related context updates in `AGENTS.md`, docs, ADRs, specs, skills, `DESIGN.md`, or tool-specific agent configuration.

```powershell
uv run python scripts/check_agent_docs_freshness.py --staged
```

GitHub Actions runs the same check for pull requests.

## Markdown And Spec Lifecycle

This template assumes Markdown files will accumulate. Durable context should be discoverable from the nearest inventory.

| Document Type | Inventory | Management Rule |
| --- | --- | --- |
| General docs | `docs/README.md` | Track role, update trigger, and retirement rule. |
| ADRs | `docs/adr/README.md` | Track ADR number, status, current decision, and supersession. |
| Feature specs | `specs/INDEX.md` or OpenSpec/GitHub Spec Kit artifacts | Track feature boundary, status, implementation links, test links, and last review date. |

Create specs by user-visible capability, integration, workflow, migration slice, or policy surface. Do not create one spec per PR, file, small refactor, daily task, or agent conversation. Use `proposed`, `active`, `implemented`, `superseded`, or `archived` as the lifecycle status.

When a feature ships, keep the spec and mark it `implemented`, then link the implementation and tests. When a spec is replaced, mark it `superseded` and link the new spec or ADR. Prefer status changes over file moves; move old specs to `specs/archive/<year>/` only when search noise becomes higher than historical value.

Small projects can keep `specs/INDEX.md` as a manual inventory. Projects that need lifecycle enforcement should prefer OpenSpec CLI commands such as `openspec validate --all --strict`, `openspec status`, and `openspec archive`, or GitHub Spec Kit validation extensions, instead of repo-local custom scripts.

## Spec-Driven Development Support

In the coding-agent ecosystem, feature-level spec workflows are more active than a single root `SPEC.md`.

| Item | Support | Template Placement |
| --- | --- | --- |
| GitHub Spec Kit | `specify` CLI, agent integrations, Spec -> Plan -> Tasks -> Implement flow. | Primary candidate for cross-agent SDD. |
| OpenSpec | Capability specs, change proposals, design notes, tasks, spec deltas, and lifecycle commands such as `validate`, `status`, and `archive`. | Useful for brownfield projects and change deltas. |
| Kiro Specs | Kiro-managed requirements, design, and task artifacts. | Use when the project intentionally uses Kiro. |
| root `SPEC.md` | Used by some community workflows, but meaning and paths vary. | Keep project-wide agent behavior in `AGENTS.md`; use feature-level specs for implementation contracts. |
| specs.md, Spec Coding, SpecWeave | Methodologies and templates for SDD. | Optional references for team workflow design. |

Spec Kit example:

```powershell
uvx --from git+https://github.com/github/spec-kit.git specify init . --integration claude
uvx --from git+https://github.com/github/spec-kit.git specify integration install cursor-agent
```

OpenSpec example:

```powershell
npm install -g @fission-ai/openspec@latest
openspec init --tools claude,cursor,codex
openspec validate --all --strict
openspec status
openspec archive <change-name>
```

`AGENTS.md` remains the agent operating contract. `.specify/memory/constitution.md` or `specs/<feature>/spec.md` are feature implementation contracts. Root `DESIGN.md` remains the Google DESIGN.md visual design system.

## Skill Tooling Support

Coding-agent ecosystems commonly either place skills directly in agent-specific directories or keep a shared skill source and link/install it into each agent.

| Item | Support | Template Placement |
| --- | --- | --- |
| Agent Skills CLI | Installs, updates, removes, symlinks, or copies skills for Claude Code, Cursor, Codex, and other agents. | Keep shared skills in `skills/` and install with `npx skills`. |
| Anthropic Skill Creator | Claude Code skill create, eval, improve, and benchmark flow. | Use as a Claude Code reference tool for skill authoring and improvement. |
| Hermes Agent skills | Skill hub, external directories, and agent-managed skill updates. | Reference lifecycle model for Hermes-based projects. |
| EvoSkill | Benchmark-driven prompt/skill evolution with diff/eval inspection. | Advanced workflow for benchmark-driven skill evolution. |
| Superpowers | Claude Code planning, TDD, review, and debugging workflow pack. | Borrow useful principles into `AGENTS.md` or individual skills. |
| GitHub awesome-copilot | Public catalog of agents, instructions, skills, and plugins. | Reference examples for skill design and refactoring workflows. |

Example:

```powershell
npx skills init my-skill
npx skills add ./skills --agent claude-code --agent cursor
npx skills list --agent claude-code --agent cursor
npx skills update -p
```

Skill validation starts with Anthropic Skill Creator eval/benchmark, A/B comparison on real tasks, team review, and the existing Python quality gate.

## Methodology References

| Item | Role | Template Use |
| --- | --- | --- |
| Karpathy-inspired skills | Community skill form of agent instruction-writing principles. | Absorb concise instruction and iterative-improvement principles into `AGENTS.md`. |
| GitHub awesome-copilot refactor skill | Public refactoring workflow example. | Reference for Tidy First, small refactors, and test-first behavior. |
| Anthropic code-simplifier plugin | Claude-only code simplification plugin example. | Claude-specific reference, not a shared baseline. |
| Kent Beck Tidy First? | Separates structural changes from behavior changes. | Reflected in `AGENTS.md` working rules. |
| Martin Fowler Refactoring | Behavior-preserving refactoring model and catalog. | Reference for code review and refactoring judgment. |

API-backed wiki compilers, security scanners already covered elsewhere, and tools that automatically mutate shared instructions are not included in the baseline.

## Development Commands

Run all Python commands through `uv`.

```powershell
uv add requests
uv add --dev pytest
uv run coding-agent-dev-template
uv run ruff format .
uv run ruff check .
uv run pyright
uv run pytest
uv run python scripts/check_agent_docs_freshness.py --staged
```

Do not edit `uv.lock` manually. Regenerate it with `uv lock` or `uv sync`.
