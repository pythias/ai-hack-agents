from pathlib import Path


def test_log_injection_fixture_exists():
    assert Path("issues/007_log_prompt.md").exists()
