# Spec Inventory

This file is the entry point for feature-level specs.

Keep it short enough for coding agents to scan before opening individual spec files.

## Status Values

| Status | Meaning |
| --- | --- |
| `proposed` | The problem is real, but implementation has not started. |
| `active` | The feature is being implemented or reviewed. |
| `implemented` | The feature shipped; code and tests are now the primary source of truth. |
| `superseded` | Another spec, ADR, or implementation replaced this spec. |
| `archived` | Kept for history only and no longer loaded by default. |

## Feature Boundary

Create one feature spec for one user-visible capability, integration, workflow, migration slice, or policy surface.

Do not create a feature spec for every PR, file change, minor refactor, daily task, or agent conversation. Use an ADR for durable tradeoffs and use normal issues or PR notes for small implementation tasks.

## Inventory

| Feature | Path | Status | Owner | Last Reviewed | Implementation | Tests | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| No feature specs yet | - | - | - | - | - | - | Add a row when the first feature spec is created. |

## Maintenance Rules

- Every `specs/<feature>/` directory must have one row in this inventory.
- Every inventory row that points to `specs/<feature>/` must point to an existing directory.
- Use stable, lowercase slugs such as `specs/oauth-login/` or `specs/billing-export/`.
- Prefer status changes over moving files. Move old specs to `specs/archive/<year>/` only when the active inventory becomes noisy.
- When a feature ships, mark the spec `implemented` and link the implementation and tests instead of rewriting the spec as retrospective documentation.
- When a spec is replaced, mark it `superseded` and link the replacement.
