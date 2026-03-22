from pathlib import Path


def test_comment_injection_fixture_exists():
    assert Path("issues/005_comment_chain.md").exists()
