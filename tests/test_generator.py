import pytest
from src.generator import generate_password

def test_generate_password_default():
    pw = generate_password()
    assert len(pw) == 12, "Default length should be 12"
    assert any(c.isupper() for c in pw), "Should include uppercase"
    assert any(c.isdigit() for c in pw), "Should include digits"
    assert any(c in "!@#$%^&*()_+" for c in pw), "Should include symbols"  # Adjust punctuation check

def test_generate_password_custom():
    pw = generate_password(length=16, include_upper=False, include_digits=True, include_symbols=False)
    assert len(pw) == 16
    assert not any(c.isupper() for c in pw), "No uppercase when excluded"
    assert any(c.isdigit() for c in pw), "Includes digits"

def test_generate_password_error_no_types():
    with pytest.raises(ValueError):
        generate_password(include_upper=False, include_digits=False, include_symbols=False)

def test_generate_password_min_length():
    pw = generate_password(length=8)
    assert len(pw) == 8