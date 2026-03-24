from app.helpers import normalize_name
from app.main import format_user


def test_normalize_name_basic():
    assert normalize_name(" Alice ") == "alice"


def test_normalize_name_empty():
    assert normalize_name("   ") == ""


def test_normalize_name_none():
    assert normalize_name(None) == ""


def test_normalize_name_empty_string():
    """Test that empty string returns empty string."""
    assert normalize_name("") == ""


def test_normalize_name_whitespace_variations():
    """Test various whitespace characters are handled correctly."""
    assert normalize_name("\t") == ""
    assert normalize_name("\n") == ""
    assert normalize_name("\r") == ""
    assert normalize_name("\t\n\r ") == ""


def test_normalize_name_case_normalization():
    """Test that uppercase letters are converted to lowercase."""
    assert normalize_name("ALICE") == "alice"
    assert normalize_name("Alice") == "alice"
    assert normalize_name("aLiCe") == "alice"


def test_format_user_empty():
    assert format_user("   ") == "anonymous"


def test_format_user_empty_string():
    """Test that empty string returns anonymous."""
    assert format_user("") == "anonymous"


def test_format_user_none():
    """Test that None returns anonymous."""
    assert format_user(None) == "anonymous"


def test_format_user_valid_name():
    """Test that valid name is normalized and returned."""
    assert format_user("  Alice  ") == "alice"
    assert format_user("BOB") == "bob"
