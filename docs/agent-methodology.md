# Agent Methodology Notes

These notes summarize the researched baseline behind this template as of May 2026.

## Findings

1. Repository instruction files are prompt context, not hard enforcement. They improve consistency, but anything mandatory must be represented in executable checks.
2. `AGENTS.md` is the best shared root file for multi-agent projects. Cursor documents it as a simple alternative to `.cursor/rules`, and Codex uses it as the repository instruction convention.
3. Claude Code still centers project memory on `CLAUDE.md`, but the official guidance supports importing `AGENTS.md` from `CLAUDE.md` to avoid duplication.
4. Cursor project rules are useful when instructions need scoped loading or stronger Cursor-specific visibility than a single root markdown file.
5. Claude skills are a better home for repeated workflows and larger procedure references than an ever-growing `CLAUDE.md` or `AGENTS.md`.
6. Google Labs DESIGN.md is a visual design-system format, not a general architecture document. Reserve root `DESIGN.md` for UI tokens and visual rationale, and keep concise software structure guidance in `AGENTS.md`.
7. `uv`, `pyproject.toml`, Ruff, Pyright, and pytest form a compact Python baseline that agents can run locally and CI can enforce.
8. Internet access and external issue text should be treated as prompt-injection surfaces. Agents should use trusted sources and avoid exposing secrets.
9. Skills need lifecycle management, not just initial authoring. Useful guidance appears in Anthropic's skill-creator work, the Agent Skills specification, and community skill registries.
10. Skill evaluation should test triggering, task output, and regression against prior behavior. A skill should be changed when it improves repeatable outcomes, not merely because a model suggested a rewrite.
11. Self-evolving skill systems such as Hermes Agent are useful reference designs, but shared project instructions should not be automatically rewritten without review, deterministic checks, and human approval.
12. Refactoring guidance for agents should prefer Kent Beck's structural-versus-behavioral separation and Martin Fowler's behavior-preserving refactoring model over broad "clean code" rewrites.
13. `npx skills` is the strongest current candidate for practical cross-agent skill packaging because it understands Claude Code, Cursor, Codex, and other agent-specific install paths.
14. Minor standalone skill validators are not adopted in this baseline. They may be useful later, but the current template should avoid adding low-signal tooling before the team has real shared skills to validate.
15. Anthropic Skill Creator is the best current reference for skill creation, eval, improve, and benchmark workflows, but it remains Claude Code-centered and should not become a mandatory dependency for every Python project.
16. EvoSkill is promising for benchmark-driven skill evolution, but its API keys, agent harnesses, and benchmark setup make it a research or advanced adoption option rather than a default template component.
17. A root `SPEC.md` convention exists in community workflows, but it is not a stable cross-agent standard comparable to `AGENTS.md`.
18. GitHub Spec Kit is the strongest current open-source candidate for cross-agent spec-driven development. It uses a `specify` CLI, `.specify/` project state, and feature-level `specs/<feature>/spec.md`, `plan.md`, and `tasks.md` artifacts.
19. Kiro has a first-party specs workflow, but its artifacts are tool-specific: `requirements.md` or `bugfix.md`, `design.md`, and `tasks.md`.
20. Root `DESIGN.md` should remain reserved for Google DESIGN.md visual design. Feature-specific `design.md` files belong under the chosen SDD tool's feature spec directory, not at the repository root.
21. Context-grounded development is the practical bridge between ADRs, specs, code intelligence, and agent autonomy. Agents should resolve known decisions from repository evidence before asking users.
22. OpenSpec is a strong brownfield-oriented SDD candidate because it keeps capability specs and change deltas in the repository.
23. Agent OS is relevant for extracting and injecting codebase standards so agents can shape better specs without repeatedly asking for team conventions.
24. Serena is a strong optional MCP layer for semantic code exploration and editing, especially when grep-based discovery is too noisy.
25. AICTX and similar repo-local continuity tools are relevant for active task state, known failures, and handoffs across sessions.

## Template Implications

- Keep `AGENTS.md` short and universal.
- Use `CLAUDE.md` as an adapter, not a duplicate.
- Use `.cursor/rules` for Cursor-specific loading mechanics.
- Use `skills/` as the canonical source for shared Agent Skills only when task-specific workflows become valuable enough to maintain.
- Use `npx skills` as the preferred candidate to install or link shared skills into Claude Code, Cursor, Codex, or other agent-specific directories.
- Use `.claude/skills/` directly only for Claude-specific skills.
- Keep visual design decisions in `DESIGN.md`.
- Keep concise software structure guidance in `AGENTS.md`.
- Do not add a root `SPEC.md` by default. Adopt feature-level spec artifacts only when the team chooses a spec-driven development workflow.
- Prefer GitHub Spec Kit for cross-agent SDD experiments; use Kiro specs only when the project is intentionally using Kiro.
- Use `docs/agent-context-stack.md` to make the context lookup order explicit.
- Ask users only when repository evidence is missing, conflicting, stale, or insufficient for high-impact decisions.
- Keep long-lived decision rationale in ADRs.
- Put deterministic requirements in `pyproject.toml`, tests, CI, and scripts.
- Treat skill changes like code changes: reviewable diffs, clear rationale, realistic validation tasks, and rollback through version control.
- Keep skills optional unless the team has observed repeated value. Drop API-backed tools, security scanners already handled elsewhere, and tools that silently modify shared instructions.
- Drop minor standalone skill validators from the base template for now.
- Capture broad agent behavior in `AGENTS.md`; only move to a skill when the workflow is conditional, long, or needs bundled scripts/references/assets.

## Sources

- Cursor Rules and `AGENTS.md`: https://docs.cursor.com/en/context
- Claude Code memory and `AGENTS.md` import: https://code.claude.com/docs/en/memory
- Claude Code skills: https://code.claude.com/docs/en/skills
- Anthropic skill-creator and skill optimization: https://claude.com/blog/improving-skill-creator-test-measure-and-refine-agent-skills
- Anthropic Skill Creator plugin: https://claude.com/plugins/skill-creator
- Agent Skills specification: https://agentskills.io/specification
- Agent Skills evaluation guidance: https://agentskills.io/skill-creation/evaluating-skills
- Agent Skills CLI, `npx skills`: https://github.com/vercel-labs/skills
- GitHub Spec Kit: https://github.github.io/spec-kit/
- GitHub Spec Kit integrations: https://github.com/github/spec-kit/blob/main/docs/reference/integrations.md
- GitHub Spec Kit repository: https://github.com/github/spec-kit
- OpenSpec: https://openspec.dev/
- Agent OS: https://buildermethods.com/agent-os
- Serena MCP coding toolkit: https://github.com/oraios/serena
- AICTX repo-local continuity: https://aictx.org/
- Codebase-Memory paper: https://arxiv.org/abs/2603.27277
- Spec Kit Agents paper: https://arxiv.org/abs/2604.05278
- ADR violation detection paper: https://arxiv.org/abs/2602.07609
- Kiro specs: https://kiro.dev/docs/specs/
- Spec Coding guide: https://spec-coding.dev/
- specs.md methodology: https://specs.md/
- Spec-driven tool landscape: https://specdriven.com/landscape/
- Claude Code settings: https://code.claude.com/docs/en/settings
- Claude Code hooks: https://code.claude.com/docs/en/hooks
- Hermes Agent self-evolving skills: https://github.com/NousResearch/Hermes-Agent
- Hermes Agent skills system: https://hermes-agent.nousresearch.com/docs/user-guide/features/skills
- EvoSkill: https://github.com/sentient-agi/EvoSkill
- Superpowers Claude plugin: https://github.com/obra/superpowers
- Karpathy-inspired Claude skills: https://github.com/multica-ai/andrej-karpathy-skills
- GitHub awesome-copilot refactor skill: https://skills.sh/github/awesome-copilot/refactor
- Anthropic code-simplifier plugin: https://github.com/anthropics/claude-plugins-official/tree/main/plugins/code-simplifier
- Kent Beck, `Tidy First?`: https://www.oreilly.com/library/view/tidy-first/9781098151232/
- Martin Fowler, `Refactoring`: https://www.martinfowler.com/books/refactoring.html
- OpenAI Codex web: https://developers.openai.com/codex/cloud
- OpenAI Codex internet access risk model: https://developers.openai.com/codex/cloud/internet-access
- Google Labs DESIGN.md specification: https://github.com/google-labs-code/design.md/blob/main/docs/spec.md
- Python Packaging User Guide for `pyproject.toml`: https://packaging.python.org/en/latest/guides/writing-pyproject-toml/
- uv project guide: https://docs.astral.sh/uv/guides/projects/
- Ruff configuration: https://docs.astral.sh/ruff/configuration/
- pytest good integration practices: https://docs.pytest.org/en/latest/goodpractices.html
- Python 3.14 release status: https://docs.python.org/3/whatsnew/3.14.html
