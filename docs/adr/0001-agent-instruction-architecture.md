# ADR 0001: Agent Instruction Architecture

## Status

Accepted

## Context

The team expects multiple coding agents to work in the same Python repositories, primarily Claude Code and Cursor, with occasional use of Codex-compatible tooling. Agent behavior should be consistent, but prompt-only guidance is not a reliable enforcement mechanism.

## Decision

Use `AGENTS.md` as the universal root instruction file, including concise project structure and workflow guidance. Use `CLAUDE.md` as a Claude Code adapter that imports `AGENTS.md`. Use `.cursor/rules/*.mdc` for Cursor-specific loading and scoped hints. Add `.claude/skills/` only when a repeated procedure is too long or conditional for `AGENTS.md`. Use ADRs for longer architecture rationale. Reserve root `DESIGN.md` for the Google Labs DESIGN.md visual design-system format. Use Python tooling and CI for deterministic enforcement.

## Consequences

- Shared behavior is written once in `AGENTS.md`.
- Claude and Cursor can use the same source of truth without copy-paste drift.
- Long procedures do not consume every agent session's context.
- `DESIGN.md` is available for UI consistency without being overloaded as an architecture document.
- Mandatory rules must be encoded in tests, linting, typing, CI, or scripts.
- Agent configuration changes need synchronized updates across adapters and rationale docs.
