# Context-Grounded Workflow Validation

Validation date: 2026-05-17

Baseline commit: `7630851 Add context-grounded agent workflow`

The validation used separate git worktrees so each scenario could change code independently without contaminating the template baseline.

## Worktrees

| Scenario | Branch Type | Worktree |
| --- | --- | --- |
| ADR-grounded change | temporary test branch | temporary ADR worktree |
| Spec-grounded change | temporary test branch | temporary spec worktree |

## Scenario 1: ADR-Grounded Change

Purpose: verify that a simple implementation decision can be resolved from ADR + package metadata without asking the user.

Change:

- Added `docs/adr/0005-cli-version-source.md` in the test branch.
- Implemented `coding-agent-dev-template --version`.
- Read the version from package metadata instead of duplicating a constant.
- Added pytest coverage that compares output with `importlib.metadata.version()`.

Checks:

```powershell
uv run ruff format --check .
uv run ruff check .
uv run pyright
uv run pytest
```

Outcome:

- All checks passed after formatter/import-order feedback was applied.
- No product or architecture question was required because the ADR provided the source-of-truth decision.

## Scenario 2: Spec-Grounded Change

Purpose: verify that a feature-level spec can define behavior clearly enough for implementation without additional user clarification.

Change:

- Added `specs/cli-json-output/spec.md`, `plan.md`, and `tasks.md` in the test branch.
- Implemented `coding-agent-dev-template --json`.
- Preserved default plain-text output.
- Added pytest coverage for compact JSON output.

Checks:

```powershell
uv run ruff format --check .
uv run ruff check .
uv run pyright
uv run pytest
```

Outcome:

- All checks passed after formatter feedback was applied.
- No user question was required because the spec defined the default behavior, new flag, output shape, and non-goals.

## Findings

- The context stack is actionable for small changes: ADRs can own implementation decisions, and feature specs can own behavior contracts.
- Formatter/linter gates remain necessary even when the agent has good context.
- Worktrees are useful for evaluating alternative agent workflows without merging experimental code into the template.
- The template should keep workflow evidence in docs while leaving test branches available for inspection.
