# Agent Context Stack

This project uses context-grounded development: coding agents should resolve known decisions from trusted project artifacts before asking users to restate them.

## Goals

- Reduce repeated clarification questions.
- Keep durable project knowledge in reviewable files.
- Make agent decisions traceable to specs, ADRs, code, or tests.
- Preserve a clear boundary between agent autonomy and human judgment.

## Context Order

Use sources in this order:

1. Current user request and explicit constraints.
2. `AGENTS.md`, `CLAUDE.md`, and `.cursor/rules/*.mdc`.
3. Feature specs in `specs/`, `.specify/`, `openspec/`, or `.kiro/specs/`.
4. ADRs in `docs/adr/`.
5. Existing code, tests, `pyproject.toml`, CI, and local patterns.
6. Optional context tools such as Agent OS, Serena, AICTX, or repo-local memory.

Ask the user only when these sources are missing, conflicting, stale, or insufficient for a product, policy, security, public API, migration, compatibility, or irreversible design decision.

## Artifact Roles

| Artifact | Use |
| --- | --- |
| `AGENTS.md` | Universal working rules and context resolution policy |
| `CLAUDE.md` | Claude Code adapter that imports shared rules |
| `.cursor/rules/*.mdc` | Cursor loading and file-scope hints |
| `specs/<feature>/` | Feature requirements, plan, tasks, and expected behavior |
| `docs/adr/` | Durable architecture decisions and tradeoffs |
| `skills/<name>/SKILL.md` | Conditional workflows too long for always-loaded guidance |
| `DESIGN.md` | Google DESIGN.md visual design system for UI work |

## Optional Tool Layers

| Layer | Tools | Notes |
| --- | --- | --- |
| SDD | GitHub Spec Kit, OpenSpec, Kiro Specs | Use when ambiguity is high or feature behavior should be durable. |
| Standards discovery | Agent OS | Useful when existing codebase conventions need to be extracted and injected into specs. |
| Code intelligence | Serena MCP | Useful for symbol-aware exploration and editing before large refactors. |
| Continuity memory | AICTX | Useful for active task state, known failures, decisions, and handoffs across sessions. |
| Structured memory | Knowns, KnowIt, memd | Watchlist. Adopt only after team policy for memory ownership, review, and retention is clear. |

## Recording New Knowledge

After a change, put new durable knowledge in the smallest artifact that can own it:

- Add an ADR for architecture decisions with tradeoffs.
- Add or update a feature spec for user-visible behavior.
- Add tests or CI checks for mandatory behavior.
- Add a skill only for a repeated conditional workflow.
- Update `AGENTS.md` only for short rules every agent should always know.

Do not store secrets, credentials, or sensitive customer data in agent memory, specs, ADRs, or skills.
