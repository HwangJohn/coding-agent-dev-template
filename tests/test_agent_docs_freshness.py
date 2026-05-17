from scripts.check_agent_docs_freshness import needs_context_update


def test_source_change_without_context_update_requires_attention() -> None:
    should_fail, source_changes, context_changes = needs_context_update(
        ["src/coding_agent_dev_template/cli.py"]
    )

    assert should_fail
    assert source_changes == ["src/coding_agent_dev_template/cli.py"]
    assert context_changes == []


def test_source_change_with_adr_update_passes() -> None:
    should_fail, source_changes, context_changes = needs_context_update(
        [
            "src/coding_agent_dev_template/cli.py",
            "docs/adr/0005-cli-version-source.md",
        ]
    )

    assert not should_fail
    assert source_changes == ["src/coding_agent_dev_template/cli.py"]
    assert context_changes == ["docs/adr/0005-cli-version-source.md"]


def test_source_change_with_english_readme_update_passes() -> None:
    should_fail, source_changes, context_changes = needs_context_update(
        [
            "scripts/check_agent_docs_freshness.py",
            "README.en.md",
        ]
    )

    assert not should_fail
    assert source_changes == ["scripts/check_agent_docs_freshness.py"]
    assert context_changes == ["README.en.md"]


def test_spec_only_change_does_not_require_another_context_update() -> None:
    should_fail, source_changes, context_changes = needs_context_update(
        ["specs/cli-json-output/spec.md"]
    )

    assert not should_fail
    assert source_changes == []
    assert context_changes == ["specs/cli-json-output/spec.md"]
