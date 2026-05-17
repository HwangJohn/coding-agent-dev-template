import tomllib
from pathlib import Path
from typing import Any, cast

import pytest

from coding_agent_dev_template.cli import main


def test_main_prints_template_name(capsys: pytest.CaptureFixture[str]) -> None:
    exit_code = main()

    captured = capsys.readouterr()

    assert exit_code == 0
    assert captured.out == "coding-agent-dev-template\n"


def test_pyproject_exposes_console_script() -> None:
    pyproject = tomllib.loads(Path("pyproject.toml").read_text(encoding="utf-8"))
    project = cast(dict[str, Any], pyproject["project"])
    scripts = cast(dict[str, str], project["scripts"])

    assert scripts["coding-agent-dev-template"] == "coding_agent_dev_template.cli:main"
