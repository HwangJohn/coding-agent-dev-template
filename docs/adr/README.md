# ADR Index

Architecture decision records capture durable decisions and tradeoffs.

Keep ADR files stable after acceptance. If a decision changes, add a new ADR and mark the old one superseded.

## Status Values

| Status | Meaning |
| --- | --- |
| `Proposed` | Under discussion. |
| `Accepted` | Current decision. |
| `Superseded` | Replaced by a newer ADR. |
| `Deprecated` | No longer recommended, but not directly replaced. |

## Records

| ADR | Status | Decision |
| --- | --- | --- |
| [0001](0001-agent-instruction-architecture.md) | Accepted | Use `AGENTS.md` as the shared agent instruction source with thin tool adapters. |
| [0002](0002-reserve-design-md-for-visual-system.md) | Accepted | Reserve root `DESIGN.md` for visual design guidance. |
| [0003](0003-agent-skill-lifecycle.md) | Accepted | Manage agent skills as reviewed, versioned project artifacts. |
| [0004](0004-context-grounded-development.md) | Accepted | Use repo-grounded context lookup to reduce repeated user questions. |
