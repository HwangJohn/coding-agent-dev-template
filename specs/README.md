# Feature Specs

This directory is reserved for optional feature-level specifications.

Use it when a change needs durable requirements, acceptance criteria, implementation planning, or task breakdown beyond a normal issue or ADR.

Preferred structures:

```text
specs/<feature>/
├── spec.md
├── plan.md
└── tasks.md
```

Tool-specific SDD frameworks may create their own directories instead:

- GitHub Spec Kit: `.specify/` and `specs/<feature>/`
- OpenSpec: `openspec/specs/` and `openspec/changes/`
- Kiro: `.kiro/specs/<feature>/`

Keep root `SPEC.md` out of the baseline. Project-wide agent behavior belongs in `AGENTS.md`; feature behavior belongs in feature-level specs.
