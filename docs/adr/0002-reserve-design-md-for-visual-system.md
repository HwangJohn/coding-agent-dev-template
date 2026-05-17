# ADR 0002: Reserve DESIGN.md for the Visual Design System

## Status

Accepted

## Context

Google Labs publishes `DESIGN.md` as a format for describing visual identity to coding agents. The format combines optional YAML design tokens with ordered Markdown sections for visual rationale. Using `DESIGN.md` as a general software architecture document conflicts with that convention and can mislead agents that expect design tokens, colors, typography, spacing, components, and UI guardrails.

## Decision

Reserve root `DESIGN.md` for the Google DESIGN.md visual design-system format. Keep concise software structure and workflow guidance in `AGENTS.md`. Keep durable technical decisions in `docs/adr/`.

## Consequences

- UI-generating agents get a structured visual source of truth.
- Architecture guidance remains available without colliding with the DESIGN.md spec.
- Agent instructions must refer to `AGENTS.md` for project structure and `DESIGN.md` for UI styling.
