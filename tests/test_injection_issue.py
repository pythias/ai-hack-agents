from pathlib import Path


def test_issue_fixture_exists():
    assert Path("issues/002_pr_body_exfil.md").exists()
