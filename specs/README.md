# Feature Specs

This directory is reserved for optional feature-level specifications.

Use it when a change needs durable requirements, acceptance criteria, implementation planning, or task breakdown beyond a normal issue or ADR.

Start from [INDEX.md](INDEX.md). The index is the lightweight map that prevents accumulated spec files from becoming hard for agents to search.

Preferred native structure:

```text
specs/<feature>/
├── spec.md
├── plan.md
└── tasks.md
```

Use [_template/](./_template/) when creating a spec without an SDD tool.

Tool-specific SDD frameworks may create their own directories instead:

- GitHub Spec Kit: `.specify/` and `specs/<feature>/`
- OpenSpec: `openspec/specs/` and `openspec/changes/`
- Kiro: `.kiro/specs/<feature>/`

## Operating Rules

- Create one spec per user-visible capability, integration, workflow, migration slice, or policy surface.
- Do not create one spec per PR, file, small refactor, daily task, or agent conversation.
- Every `specs/<feature>/` directory must appear in [INDEX.md](INDEX.md).
- Every indexed `specs/<feature>/` path must point to an existing directory.
- Every native feature directory must include `spec.md`.
- Mark shipped specs `implemented` and link implementation/tests instead of rewriting them as retrospective docs.
- Mark replaced specs `superseded` and link the replacement.
- Move specs to `specs/archive/<year>/` only when the active inventory becomes noisy.

Do not add repo-local custom scripts as the default spec management mechanism. If spec lifecycle needs to be enforced, prefer an adopted open-source tool:

- OpenSpec: `openspec validate --all --strict`, `openspec status`, and `openspec archive`
- GitHub Spec Kit: `specify` workflows and validation extensions
- Kiro: Kiro-managed spec artifacts when the project intentionally uses Kiro

Keep root `SPEC.md` out of the baseline. Project-wide agent behavior belongs in `AGENTS.md`; feature behavior belongs in feature-level specs.
