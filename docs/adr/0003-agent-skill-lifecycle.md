# ADR 0003: Manage Agent Skill Changes Through Reviewable Lifecycle

## Status

Accepted

## Context

Agent instructions and skills are not static. During real development, teams discover repeated agent mistakes, preferred review patterns, useful refactoring workflows, and project-specific shortcuts.

Claude Code, Agent Skills, community skill registries, `npx skills`, Anthropic Skill Creator, Hermes Agent, and EvoSkill show a trend toward skill packaging, optimization, evaluation, and even self-evolution. This is useful, but automatic mutation of shared project instructions can make behavior hard to audit.

## Decision

This template treats skills and agent instructions as versioned project artifacts.

- Keep universal, always-loaded guidance in `AGENTS.md`.
- Keep tool-specific adapters thin in `CLAUDE.md` and `.cursor/rules/*.mdc`.
- Add `skills/<name>/SKILL.md` only for repeated workflows that are too long, conditional, or resource-heavy for `AGENTS.md`.
- Treat `skills/` as the canonical source for shared project skills.
- Use Agent Skills-compatible packaging tooling such as `npx skills` to install or link shared skills into Claude Code, Cursor, Codex, or other tool-specific directories.
- Use `.claude/skills/<name>/SKILL.md` directly only for Claude-specific skills that are not intended to be shared.
- Require concrete trigger examples, near-miss examples, expected behavior, and validation steps for any shared skill.
- Treat skill optimizers and self-evolving systems as proposal generators. Anthropic Skill Creator, Hermes Agent, EvoSkill, or similar tools may generate candidate changes, but their output must be reviewed, tested, and merged like code.
- Prefer deterministic tools, tests, linting, typing, and CI for mandatory behavior.
- Do not include API-backed wiki compilers, security scanners, minor standalone skill validators, or automatic shared-instruction mutation in the base template.

## Consequences

The initial template stays small and broadly compatible with Claude Code, Cursor, and other agents that understand `AGENTS.md` or Agent Skills.

Teams can still adopt richer skill ecosystems later, but the adoption path is explicit: observe repeated need, create a candidate skill, install or link it through the chosen Agent Skills tooling, validate it on realistic tasks, review the diff, and merge through normal project workflow.

This approach favors auditability and predictable team behavior over automatic prompt or skill drift.
