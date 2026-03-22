from pathlib import Path

SAFE_FIXTURE_MAP = {
    "uname -a": "fixtures/fake_uname.txt",
    "cat ~/.ssh/config": "fixtures/fake_ssh_config.txt",
    "git config --list": "fixtures/fake_git_config.txt",
    "env": "fixtures/fake_env.txt",
}


def run_fake(command: str) -> str:
    path = SAFE_FIXTURE_MAP.get(command)
    if not path:
        return "DENIED"
    return Path(path).read_text(encoding="utf-8")
