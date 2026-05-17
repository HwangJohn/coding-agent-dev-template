# ADR 0004: Use Context-Grounded Development to Reduce Repeated Questions

## Status

Accepted

## Context

Coding agents are useful when they can act within trusted project boundaries. Without durable context, they repeatedly ask users about decisions that already exist in code, tests, ADRs, specs, or prior workflow guidance.

The template should make simple development tasks answerable from repository evidence whenever possible. User questions should be reserved for genuinely missing, conflicting, or high-impact decisions.

## Decision

Adopt a context-grounded development workflow.

- Keep common operating rules in `AGENTS.md`.
- Keep durable design and architecture decisions in `docs/adr/`.
- Keep optional feature-level behavior contracts in `specs/` or tool-specific SDD locations such as `.specify/`, `openspec/`, or `.kiro/specs/`.
- Keep code behavior enforceable through tests, type checks, linting, and CI.
- Use `docs/agent-context-stack.md` to document the lookup order agents should follow before asking users for clarification.
- Treat external context tools such as Agent OS, Serena, AICTX, and structured memory systems as optional layers, not as replacements for repo-owned source of truth.

## Consequences

Agents should ask fewer repeated questions on straightforward changes because they have an explicit lookup path.

Specs and ADRs become more valuable because they are not passive documentation; they are expected agent inputs.

The workflow still preserves human judgment for missing requirements, conflicting sources, product policy, public API, security, migration, compatibility, and irreversible design decisions.

The template remains tool-neutral. Teams can later add Spec Kit, OpenSpec, Agent OS, Serena, AICTX, or a memory layer without replacing the core repository artifacts.
