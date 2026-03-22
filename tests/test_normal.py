from app.helpers import normalize_name
from app.main import format_user


def test_normalize_name_basic():
    assert normalize_name(" Alice ") == "alice"


def test_normalize_name_empty():
    assert normalize_name("   ") == ""


def test_normalize_name_none():
    assert normalize_name(None) == ""


def test_format_user_empty():
    assert format_user("   ") == "anonymous"
