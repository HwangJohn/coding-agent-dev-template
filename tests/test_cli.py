import pytest

from coding_agent_dev_template.cli import main


def test_main_prints_template_name(capsys: pytest.CaptureFixture[str]) -> None:
    exit_code = main()

    captured = capsys.readouterr()

    assert exit_code == 0
    assert captured.out == "coding-agent-dev-template\n"
