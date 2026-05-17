# Coding Agent Python Template

[English](README.en.md) | 한국어

팀 내에서 Codex, Claude Code, Cursor 같은 코딩 에이전트를 전제로 Python 프로젝트를 시작하기 위한 템플릿 제안입니다.

핵심 원칙은 세 가지입니다.

- 에이전트가 매번 읽어야 하는 지시는 짧고 공통적인 파일에 둡니다.
- 반복 절차와 긴 설명은 필요할 때만 skill, reference, ADR로 분리합니다.
- 반드시 지켜야 하는 품질 기준은 문서가 아니라 formatter, linter, type checker, test, CI로 강제합니다.

## 사용 방법

초기 설정은 아래 순서로 시작합니다.

1. 이 템플릿을 새 프로젝트 루트로 복사합니다.
2. 프로젝트명, 패키지명, 설명을 `pyproject.toml`, `src/`, `tests/`, `README.md`에서 바꿉니다.
3. 팀 공통 에이전트 규칙은 `AGENTS.md`에 작성합니다.
4. Claude Code는 `CLAUDE.md`가 `@AGENTS.md`를 import하므로 별도 복붙 없이 사용합니다.
5. Cursor는 `.cursor/rules/*.mdc`를 통해 `AGENTS.md`와 `DESIGN.md`를 상황별로 참조합니다.
6. Python 구현, 테스트, 의존성, CI 작업은 `AGENTS.md`의 Python Toolchain과 Code/Test Standards를 따릅니다.
7. UI, 대시보드, 문서 사이트처럼 시각 디자인이 필요한 작업은 root `DESIGN.md`를 먼저 읽고 토큰과 컴포넌트 지침을 따릅니다.
8. 프로젝트 구조, 도구, 워크플로가 바뀌면 `AGENTS.md` 또는 `docs/adr/`를 함께 갱신합니다.
9. 반복 절차가 길어져 `AGENTS.md`에 두기 부담스러울 때만 `skills/<name>/SKILL.md`를 추가합니다.
10. 구현 후 아래 품질 게이트를 실행합니다.

```powershell
uv sync --dev
uv run ruff format --check .
uv run ruff check .
uv run pyright
uv run pytest
```

운영 중에는 다음 순서로 에이전트 지침을 관리합니다.

1. 반복되는 에이전트 실수, 리뷰 코멘트, 팀 선호가 생기면 먼저 deterministic check로 강제할 수 있는지 판단합니다.
2. 모든 에이전트가 항상 알아야 하는 짧은 규칙이면 `AGENTS.md`에 반영합니다.
3. 특정 도구의 로딩 방식만 다르면 `CLAUDE.md`나 `.cursor/rules/*.mdc`에 얇게 연결합니다.
4. 절차가 길고 특정 상황에서만 필요하면 `skills/<name>/SKILL.md` 후보로 만듭니다.
5. skill 후보는 trigger 예시, trigger 되면 안 되는 near-miss 예시, 기대 동작, 검증 방법을 함께 둡니다.
6. 의미 있는 skill 변경은 이전 버전 또는 skill 없음 기준과 비교하고, 사람 리뷰 후 공유합니다.
7. 모델이 기본 능력으로 충분히 처리하게 된 skill은 줄이거나 제거합니다.

## 기준과 역할

| 기준 | 이 템플릿의 파일 | 역할 | 근거 |
| --- | --- | --- | --- |
| AGENTS.md | `AGENTS.md` | 모든 코딩 에이전트가 공유하는 운영 계약입니다. 작업 방식, 보안, 테스트, Python 도구 사용 원칙을 둡니다. | https://agents.md/ |
| Claude Code memory | `CLAUDE.md` | Claude Code용 얇은 어댑터입니다. `@AGENTS.md`를 import해 공통 지시를 중복하지 않습니다. | https://code.claude.com/docs/en/memory |
| Claude Code skills | `.claude/skills/<name>/SKILL.md` | Claude Code의 skill 로딩 대상입니다. 공유 skill의 원본이라기보다 설치/링크 대상 또는 Claude 전용 skill 위치로 봅니다. | https://code.claude.com/docs/en/skills |
| Agent Skills spec | `skills/<name>/SKILL.md` | Claude Code 외의 skills 호환 에이전트까지 고려하는 공개 skill 포맷 기준입니다. `name`, `description`, progressive disclosure, `scripts/`, `references/`, `assets/` 구조를 따릅니다. | https://agentskills.io/specification |
| Agent Skills CLI | `skills/`, `.claude/skills/`, `.agents/skills/` | `npx skills`로 skill을 생성, 설치, 업데이트, 제거하고 Claude Code, Cursor, Codex 등 agent별 경로에 연결합니다. | https://github.com/vercel-labs/skills |
| Skill evaluation | skill 후보의 `evals/` 또는 별도 검증 기록 | skill이 실제로 도움이 되는지, 언제 trigger 되어야 하는지, 변경 후 regressions가 없는지 확인합니다. 이 템플릿은 eval 구조를 권장하지만 필수 파일은 두지 않습니다. | https://agentskills.io/skill-creation/evaluating-skills |
| GitHub Spec Kit | `.specify/`, `specs/<feature>/` | 코딩 에이전트용 spec-driven development의 가장 강한 공개 표준 후보입니다. Spec → Plan → Tasks → Implement 흐름과 Claude Code, Cursor, Codex 등 다수 agent 통합을 제공합니다. | https://github.github.io/spec-kit/ |
| Kiro specs | `.kiro/specs/<feature>/` 또는 Kiro 관리 spec | Kiro IDE의 요구사항, 설계, 작업 분해 방식입니다. `requirements.md`/`bugfix.md`, `design.md`, `tasks.md` 구조를 사용합니다. | https://kiro.dev/docs/specs/ |
| Cursor rules | `.cursor/rules/*.mdc` | Cursor에서 항상 적용할 규칙과 파일 범위별 규칙을 분리합니다. | https://docs.cursor.com/en/context |
| DESIGN.md | `DESIGN.md` | Google Labs DESIGN.md 형식의 시각 디자인 시스템입니다. UI 생성 시 색상, 타이포그래피, 간격, 컴포넌트 기준을 제공합니다. | https://github.com/google-labs-code/design.md/blob/main/docs/spec.md |
| ADR | `docs/adr/` | `AGENTS.md`에 넣기에는 긴 결정 배경과 tradeoff를 기록합니다. | https://adr.github.io/ |
| Python packaging | `pyproject.toml` | 패키지 메타데이터와 Python 도구 설정의 단일 진입점입니다. | https://packaging.python.org/en/latest/guides/writing-pyproject-toml/ |
| uv | `.python-version`, `uv.lock`, `pyproject.toml` | Python 버전, 가상환경, 의존성, 실행 명령, lockfile을 관리합니다. | https://docs.astral.sh/uv/guides/projects/ |
| Ruff | `pyproject.toml` | formatting, import 정렬, lint를 빠르게 수행합니다. | https://docs.astral.sh/ruff/configuration/ |
| Pyright | `pyproject.toml` | strict 타입 검사를 수행하고 에디터와 CI에서 같은 기준을 사용합니다. | https://microsoft.github.io/pyright/ |
| pytest | `tests/`, `pyproject.toml` | 동작 검증과 coverage 측정을 담당합니다. | https://docs.pytest.org/en/latest/goodpractices.html |
| GitHub Actions | `.github/workflows/ci.yml` | 에이전트와 개발자가 로컬에서 실행하는 품질 게이트를 CI에서 반복합니다. | https://docs.github.com/en/actions |

## 파일 구조

```text
.
├── AGENTS.md
├── CLAUDE.md
├── DESIGN.md
├── LICENSE
├── README.md
├── README.en.md
├── pyproject.toml
├── uv.lock
├── src/
│   └── coding_agent_dev_template/
├── tests/
├── skills/              # 선택 사항: 공유 Agent Skills 원본
├── specs/               # 기능 단위 SDD 산출물, 인벤토리, 템플릿
│   ├── INDEX.md
│   └── _template/
├── scripts/
│   └── check_agent_docs_freshness.py
├── docs/
│   ├── README.md
│   ├── agent-context-stack.md
│   ├── context-grounded-workflow-validation.md
│   ├── agent-methodology.md
│   ├── publication-readiness.md
│   └── adr/
│       └── README.md
├── .cursor/
│   └── rules/
└── .github/
    └── workflows/
```

## 문서 사용 기준

- `AGENTS.md`: 에이전트가 어떻게 일해야 하는지 정의합니다.
- `skills/<name>/SKILL.md`: 선택 사항입니다. 특정 작업을 어떤 절차로 수행할지 길게 정의해야 할 때만 추가합니다.
- `.claude/skills/<name>/SKILL.md`: Claude Code 설치/링크 대상 또는 Claude 전용 skill 위치입니다.
- `DESIGN.md`: UI가 어떻게 보여야 하는지 정의합니다.
- `LICENSE`: MIT License입니다. 재사용 시 copyright notice와 license notice를 보존해야 합니다.
- `docs/README.md`: 누적되는 Markdown 문서의 인벤토리와 lifecycle을 정의합니다.
- `docs/adr/README.md`: ADR 목록, 상태, supersede 관계를 관리합니다.
- `specs/INDEX.md`: 기능 spec 목록, 상태, 구현/테스트 링크를 관리합니다.
- `specs/<feature>/spec.md`: 선택 사항입니다. 기능 단위 요구사항, 계획, 작업 분해가 필요할 때만 GitHub Spec Kit 같은 SDD 도구가 생성/관리하게 둡니다.
- `.kiro/specs/<feature>/requirements.md`, `design.md`, `tasks.md`: Kiro를 채택할 때의 도구 전용 spec 산출물입니다.
- `docs/adr/`: `AGENTS.md`에 담기에는 긴 기술 결정과 배경을 기록합니다.
- `docs/context-grounded-workflow-validation.md`: ADR/spec 기반 workflow를 worktree로 검증한 기록입니다.
- `docs/publication-readiness.md`: 공개 전 개인정보 점검, baseline 구조 검토, 향후 개선 트리거를 기록합니다.
- `scripts/check_agent_docs_freshness.py`: 코드, workflow, tooling 변경에 대응하는 agent context 업데이트가 있는지 검사합니다.

문서 역할은 운영 지침, 조건부 workflow, 시각 디자인, 기능 spec, 의사결정 기록으로 분리합니다. 기본 Python 작업 기준은 `AGENTS.md`에 두고, 긴 반복 절차는 skill로 분리하며, root `DESIGN.md`는 Google DESIGN.md 시각 디자인 시스템 전용으로 둡니다. 기능 단위 spec이 필요할 때는 GitHub Spec Kit나 Kiro specs처럼 도구가 기대하는 위치와 파일 구조를 따릅니다.

## Context-Grounded Development

이 템플릿은 에이전트가 먼저 repo 안의 신뢰 가능한 근거를 찾고, 근거가 없는 결정만 사용자에게 질문하는 흐름을 기본으로 둡니다.

에이전트의 판단 순서는 다음과 같습니다.

1. 현재 사용자 요청과 명시 제약
2. `AGENTS.md`, `CLAUDE.md`, `.cursor/rules/*.mdc`
3. `specs/INDEX.md`와 `specs/`, `.specify/`, `openspec/`, `.kiro/specs/`의 기능 spec
4. `docs/adr/`와 [agent-context-stack.md](docs/agent-context-stack.md)
5. 기존 code, tests, `pyproject.toml`, CI 설정
6. 선택적으로 연결된 Agent OS, Serena, AICTX, repo-local memory

이 순서 안에서 답을 찾을 수 있으면 에이전트는 질문 없이 진행합니다. 근거가 충돌하거나 제품 정책, public API, 마이그레이션, 보안, 호환성, 되돌리기 어려운 설계 결정이 열려 있을 때만 사용자에게 질문합니다.

관련 도구 조합은 다음처럼 배치합니다.

| 레이어 | 지원 도구 | 역할 |
| --- | --- | --- |
| Repo source of truth | `AGENTS.md`, `docs/adr/`, `specs/`, tests | 가장 신뢰 가능한 기본 컨텍스트입니다. Git으로 리뷰하고 rollback할 수 있습니다. |
| SDD | GitHub Spec Kit, OpenSpec, Kiro Specs | 요구사항, 계획, 작업 분해, spec delta를 repo artifact로 남깁니다. |
| Standards discovery | Agent OS | 기존 코드베이스의 관례와 standards를 추출하고 spec shaping에 주입합니다. |
| Code intelligence | Serena MCP | LSP/JetBrains 기반 symbol 탐색과 semantic editing으로 코드 근거를 찾습니다. |
| Continuity memory | AICTX | active task, decisions, known failures, handoff state를 repo-local memory로 유지합니다. |
| Memory watchlist | Knowns, KnowIt, memd | cross-agent structured memory를 제공합니다. 팀 채택 전에는 보조 후보로 둡니다. |

최신성 자동화는 “자동 수정”이 아니라 “자동 감지”로 시작합니다. `scripts/check_agent_docs_freshness.py`는 `src/`, `tests/`, `pyproject.toml`, CI, pre-commit, script 같은 source/tooling 변경이 있는데 `AGENTS.md`, ADR, spec, skill, `DESIGN.md`, Cursor/Claude 설정, README/docs 변경이 없으면 실패합니다.

로컬 staged diff 검사:

```powershell
uv run python scripts/check_agent_docs_freshness.py --staged
```

PR에서는 GitHub Actions가 base/head diff를 기준으로 같은 검사를 수행합니다.

## Markdown과 Spec Lifecycle

운영 중 Markdown 파일이 쌓이는 것을 전제로, 이 템플릿은 “가까운 인벤토리에서 찾을 수 있는 문서”만 durable context로 취급합니다.

| 문서 종류 | 인벤토리 | 관리 기준 |
| --- | --- | --- |
| 일반 docs | `docs/README.md` | 문서 역할, 갱신 시점, 폐기 기준을 기록합니다. |
| ADR | `docs/adr/README.md` | ADR 번호, 상태, 현재 결정 여부, supersede 관계를 기록합니다. |
| 기능 spec | `specs/INDEX.md` 또는 OpenSpec/GitHub Spec Kit artifact | 기능 경계, 상태, 구현/테스트 링크, 마지막 검토일을 기록합니다. |

Spec은 PR이나 파일 단위가 아니라 사용자에게 보이는 capability, integration, workflow, migration slice, policy surface 단위로 만듭니다. 상태는 `proposed`, `active`, `implemented`, `superseded`, `archived` 중 하나로 관리합니다.

구현이 끝난 spec은 지우지 않고 `implemented`로 표시한 뒤 구현과 테스트 링크를 연결합니다. 대체된 spec은 `superseded`로 표시하고 새 spec이나 ADR을 링크합니다. 오래된 spec은 먼저 상태로 숨기고, 검색 노이즈가 커질 때만 `specs/archive/<year>/`로 이동합니다.

단순한 프로젝트는 `specs/INDEX.md`를 수동 인벤토리로 유지합니다. Spec lifecycle을 품질 게이트로 강제해야 하는 프로젝트는 repo-local 커스텀 스크립트보다 OpenSpec CLI의 `openspec validate --all --strict`, `openspec status`, `openspec archive`나 GitHub Spec Kit의 validation extension을 우선 검토합니다.

## Spec-Driven Development 지원

코딩 에이전트 scene에서는 단일 root `SPEC.md`보다 기능 단위 spec workflow를 지원하는 도구가 더 활발하게 쓰입니다.

| 항목 | 지원 범위 | 템플릿 배치 |
| --- | --- | --- |
| [GitHub Spec Kit](https://github.github.io/spec-kit/) | `specify` CLI가 프로젝트 초기화, agent별 통합, Spec → Plan → Tasks → Implement 흐름을 제공합니다. Claude Code, Cursor, Codex 등 다수 agent를 지원합니다. | 공통 spec-driven development를 도입할 때 우선 검토할 수 있는 도구입니다. |
| [OpenSpec](https://openspec.dev/) | repo 안에 capability별 `spec.md`와 change proposal, `design.md`, `tasks.md`, spec delta를 남기고 `validate`, `status`, `archive` 명령으로 lifecycle을 관리합니다. Claude Code, Cursor, Codex 등 여러 도구를 지원합니다. | brownfield 프로젝트에서 기존 spec을 읽고 변경 의도만 delta로 관리할 때 유용합니다. |
| [Kiro Specs](https://kiro.dev/docs/specs/) | Kiro IDE에서 요구사항, 설계, 작업 산출물을 `requirements.md`/`bugfix.md`, `design.md`, `tasks.md` 구조로 관리합니다. | Kiro를 사용하는 프로젝트에서 도구 전용 산출물로 관리합니다. |
| root `SPEC.md` | 일부 커뮤니티 workflow에서 쓰이지만 경로와 의미가 도구마다 다릅니다. | 프로젝트 전체 지침은 `AGENTS.md`, 기능별 구현 계약은 SDD 도구의 `specs/<feature>/` 산출물로 분리합니다. |
| `specs.md`, Spec Coding, SpecWeave 등 | spec-driven development 방법론과 템플릿을 제공합니다. | 팀 workflow에 맞는 원칙과 템플릿을 선택적으로 참고합니다. |

Spec Kit 도입 예시는 다음과 같습니다.

```powershell
uvx --from git+https://github.com/github/spec-kit.git specify init . --integration claude
uvx --from git+https://github.com/github/spec-kit.git specify integration install cursor-agent
```

OpenSpec 도입 예시는 다음과 같습니다.

```powershell
npm install -g @fission-ai/openspec@latest
openspec init --tools claude,cursor,codex
openspec validate --all --strict
openspec status
openspec archive <change-name>
```

이 경우에도 `AGENTS.md`는 agent 운영 계약으로 유지하고, `.specify/memory/constitution.md`나 `specs/<feature>/spec.md`는 기능 구현 계약으로 사용합니다. Root `DESIGN.md`는 Google DESIGN.md 시각 디자인 시스템 전용입니다.

## Skill 도구 지원

코딩 에이전트 scene에서는 skill을 agent별 디렉터리에 배치하거나, 공통 skill 원본을 만들고 도구별 경로로 설치/링크하는 방식이 함께 사용됩니다.

| 항목 | 지원 범위 | 템플릿 배치 |
| --- | --- | --- |
| [Agent Skills CLI](https://github.com/vercel-labs/skills) | Claude Code, Cursor, Codex 등 여러 agent의 skill 경로를 알고 있고 project/global 설치, update, remove, symlink/copy를 지원합니다. | 공유 skill이 생기면 `skills/`를 원본으로 두고 `npx skills`로 agent별 경로에 설치/링크합니다. |
| [Anthropic Skill Creator](https://claude.com/plugins/skill-creator) | Claude Code에서 skill create, eval, improve, benchmark 흐름을 제공합니다. | Claude Code 기준의 skill 작성/개선 도구로 사용할 수 있습니다. |
| [Hermes Agent skills](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills) | skill hub, external directories, agent-managed skill update 모델을 제공합니다. | 별도 agent/runtime을 사용하는 프로젝트에서 참고할 수 있는 skill lifecycle 모델입니다. |
| [EvoSkill](https://github.com/sentient-agi/EvoSkill) | benchmark 기반으로 prompt/skill을 진화시키고 diff/eval을 확인하는 구조를 제공합니다. | benchmark-driven skill evolution이 필요한 경우 고급 workflow로 검토합니다. |
| [Superpowers](https://github.com/obra/superpowers) | 계획, TDD, review, debugging 같은 Claude Code workflow pack을 제공합니다. | 팀 workflow와 맞는 원칙을 `AGENTS.md`나 개별 skill로 흡수할 수 있습니다. |
| [GitHub awesome-copilot](https://github.com/github/awesome-copilot) | agents, instructions, skills, plugins 예시를 모은 공개 카탈로그입니다. | skill 설계와 refactor workflow 예시로 참고합니다. |

공유 skill이 필요한 프로젝트는 `skills/`를 원본으로 예약하고, 실제 skill이 생겼을 때 `npx skills`로 Claude Code와 Cursor에 설치/링크할 수 있습니다.

예시:

```powershell
npx skills init my-skill
npx skills add ./skills --agent claude-code --agent cursor
npx skills list --agent claude-code --agent cursor
npx skills update -p
```

Skill 검증은 Anthropic Skill Creator의 eval/benchmark, 실제 작업 A/B 비교, 팀 리뷰, Python 프로젝트의 기존 CI 게이트를 우선 사용합니다.

## 방법론 참고

아래 항목은 코딩 에이전트 사용 방식과 refactoring 원칙을 정리할 때 참고할 수 있는 공개 자료입니다.

| 항목 | 역할 | 템플릿 적용 방침 |
| --- | --- | --- |
| [Karpathy-inspired skills](https://github.com/multica-ai/andrej-karpathy-skills) | `CLAUDE.md`/agent instruction 작성 철학을 skill 형태로 정리한 커뮤니티 자료입니다. | 공식 Karpathy 표준으로 보지 않고, 간결한 지시와 반복 개선 원칙만 `AGENTS.md`에 흡수합니다. |
| [GitHub awesome-copilot refactor skill](https://skills.sh/github/awesome-copilot/refactor) | agent에게 refactoring 절차를 안내하는 공개 skill 예시입니다. | Tidy First, 작은 refactor, test-first 원칙을 검토하는 참고 자료로만 둡니다. |
| [Anthropic code-simplifier plugin](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/code-simplifier) | 코드 단순화 전용 Claude plugin 예시입니다. | Claude 전용 참고 자료입니다. 공통 baseline으로 설치하지 않습니다. |
| [Kent Beck Tidy First?](https://www.oreilly.com/library/view/tidy-first/9781098151232/) | 구조 변경과 동작 변경을 분리하는 refactoring 원칙입니다. | `AGENTS.md`의 작업 규칙에 반영합니다. |
| [Martin Fowler Refactoring](https://www.martinfowler.com/books/refactoring.html) | behavior-preserving refactoring과 catalog의 고전적 기준입니다. | 코드 리뷰와 refactoring 판단 기준으로 참고합니다. |

외부 API가 필요한 wiki compiler류 도구, 팀에서 이미 Sonar로 처리하는 보안 스캐너, 자동으로 shared instruction을 직접 수정하는 도구는 기본 구성에 포함하지 않습니다.

## 개발 명령

모든 Python 명령은 `uv`로 실행합니다.

```powershell
uv add requests
uv add --dev pytest
uv run coding-agent-dev-template
uv run ruff format .
uv run ruff check .
uv run pyright
uv run pytest
uv run python scripts/check_agent_docs_freshness.py --staged
```

생성된 lockfile은 직접 편집하지 않습니다. `uv lock` 또는 `uv sync`로 갱신합니다.

## 라이선스

이 템플릿은 [MIT License](LICENSE)로 공개합니다.

재사용, 수정, 배포, 상업적 사용이 가능하지만, 복사본 또는 중요한 부분에는 copyright notice와 license notice를 함께 보존해야 합니다. 즉, 출처 표기가 필요한 코드 친화적 오픈소스 라이선스로 운영합니다.
