from __future__ import annotations

import argparse
import fnmatch
import shutil
import subprocess
import sys
from collections.abc import Sequence

SOURCE_PATTERNS = (
    "src/**",
    "tests/**",
    "pyproject.toml",
    "uv.lock",
    ".python-version",
    ".pre-commit-config.yaml",
    ".github/workflows/**",
    "scripts/**",
)

CONTEXT_PATTERNS = (
    "AGENTS.md",
    "CLAUDE.md",
    "DESIGN.md",
    "README.md",
    ".cursor/rules/**",
    "docs/**",
    "specs/**",
    "skills/**",
)


def normalize_path(path: str) -> str:
    return path.replace("\\", "/").strip()


def matches_any(path: str, patterns: Sequence[str]) -> bool:
    normalized = normalize_path(path)
    return any(fnmatch.fnmatchcase(normalized, pattern) for pattern in patterns)


def run_git(args: Sequence[str]) -> list[str]:
    git_executable = shutil.which("git")
    if git_executable is None:
        raise RuntimeError("git executable was not found on PATH")

    result = subprocess.run(  # noqa: S603
        [git_executable, *args],
        check=True,
        capture_output=True,
        text=True,
    )
    return [line.strip() for line in result.stdout.splitlines() if line.strip()]


def changed_files_from_git(base: str, head: str) -> list[str]:
    try:
        return run_git(["diff", "--name-only", "--diff-filter=ACMR", f"{base}...{head}"])
    except subprocess.CalledProcessError:
        return run_git(["diff", "--name-only", "--diff-filter=ACMR", base, head])


def staged_files_from_git() -> list[str]:
    return run_git(["diff", "--cached", "--name-only", "--diff-filter=ACMR"])


def needs_context_update(changed_files: Sequence[str]) -> tuple[bool, list[str], list[str]]:
    normalized_files = [normalize_path(path) for path in changed_files]
    source_changes = [path for path in normalized_files if matches_any(path, SOURCE_PATTERNS)]
    context_changes = [path for path in normalized_files if matches_any(path, CONTEXT_PATTERNS)]
    return bool(source_changes and not context_changes), source_changes, context_changes


def parse_args(argv: Sequence[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Fail when source/tooling changes lack AGENTS/spec/ADR/docs context updates.",
    )
    parser.add_argument("--base", help="base git ref for comparison")
    parser.add_argument("--head", default="HEAD", help="head git ref for comparison")
    parser.add_argument(
        "--staged",
        action="store_true",
        help="check staged files instead of comparing refs",
    )
    parser.add_argument(
        "--changed-file",
        action="append",
        default=[],
        help="explicit changed file path; may be repeated",
    )
    return parser.parse_args(argv)


def emit(message: str = "") -> None:
    sys.stdout.write(f"{message}\n")


def main(argv: Sequence[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)

    if args.changed_file:
        changed_files = list(args.changed_file)
    elif args.staged:
        changed_files = staged_files_from_git()
    elif args.base:
        changed_files = changed_files_from_git(args.base, args.head)
    else:
        emit(
            "No base ref, staged flag, or explicit changed files provided; "
            "skipping agent docs freshness check."
        )
        return 0

    should_fail, source_changes, context_changes = needs_context_update(changed_files)

    if not changed_files:
        emit("No changed files detected.")
        return 0

    if should_fail:
        emit("Source/tooling changes were detected without agent context updates.")
        emit()
        emit("Source/tooling files:")
        for path in source_changes:
            emit(f"- {path}")
        emit()
        emit("Update one of these if the change affects project behavior or workflow:")
        for pattern in CONTEXT_PATTERNS:
            emit(f"- {pattern}")
        emit()
        emit(
            "If no context update is needed, include that rationale in the PR description "
            "and run this check only after staging the rationale-bearing docs change."
        )
        return 1

    if source_changes:
        emit("Agent docs freshness check passed.")
        emit("Source/tooling changes:")
        for path in source_changes:
            emit(f"- {path}")
        if context_changes:
            emit("Context updates:")
            for path in context_changes:
                emit(f"- {path}")
    else:
        emit("No source/tooling changes requiring context updates detected.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
