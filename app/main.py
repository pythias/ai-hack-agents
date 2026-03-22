from app.helpers import normalize_name


def format_user(name: str) -> str:
    normalized = normalize_name(name)
    if not normalized:
        return "anonymous"
    return normalized
