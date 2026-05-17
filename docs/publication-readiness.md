# Publication Readiness

Publication target: public GitHub repository

Version target: `0.1.0`

## Privacy Check

Tracked files were checked for:

- Local user profile paths
- Personal names or account handles
- Email addresses used for credentials
- API key names and common token prefixes
- Password, secret, credential, and private-key markers
- `.env`, `.env.*`, and `secrets/` content

Result:

- No credential, token, private key, or secret value is present in tracked files.
- No personal user profile path is present in tracked files.
- `.env`, `.env.*`, `secrets/`, caches, virtual environments, coverage output, and Python bytecode are ignored.
- Local test worktree paths are not part of the template documentation.

## Baseline Standard Review

The repository is organized around a small, tool-neutral baseline:

- `AGENTS.md` is the shared agent operating contract.
- `CLAUDE.md` imports `AGENTS.md` for Claude Code.
- `.cursor/rules/` keeps Cursor-specific loading behavior thin.
- `DESIGN.md` is reserved for Google DESIGN.md visual design guidance.
- `docs/adr/` stores durable decisions.
- `docs/agent-context-stack.md` defines how agents should use repo context before asking users.
- `specs/` is reserved for optional feature-level SDD artifacts.
- `skills/` is reserved for optional shared Agent Skills.
- `pyproject.toml`, `uv.lock`, Ruff, Pyright, pytest, and GitHub Actions provide deterministic gates.

This baseline is intentionally conservative. It does not install external memory services, skill validators, self-evolving agents, security scanners, or API-backed wiki tools by default.

## Future Improvement Triggers

| When this happens | Add or evaluate this |
| --- | --- |
| Feature behavior is ambiguous or repeatedly re-explained | Add a feature spec under `specs/<feature>/` or adopt GitHub Spec Kit/OpenSpec. |
| Architecture decisions recur in reviews | Add or update an ADR. |
| Agents repeatedly ask questions that existing docs answer | Update `docs/agent-context-stack.md` or move the durable rule into `AGENTS.md`. |
| A repeated workflow is too long for `AGENTS.md` | Add a shared skill under `skills/<name>/SKILL.md`. |
| Shared skills need installation into multiple agents | Use `npx skills` to link/install from `skills/` into tool-specific directories. |
| Codebase navigation becomes too slow or noisy | Evaluate Serena MCP for symbol-aware exploration. |
| Long-running work loses state across sessions | Evaluate a repo-local continuity layer such as AICTX. |
| Team conventions are implicit in the codebase | Evaluate Agent OS-style standards discovery. |
| UI work becomes recurring | Expand `DESIGN.md` and add UI validation examples. |
| Public reuse increases | Add a license, contributing guide, release notes, and issue templates. |
