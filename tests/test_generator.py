import pytest
from unittest.mock import patch
from src.generator import generate_password
import string


@patch('secrets.choice')  # Mock for determinism
def test_generate_password_default(mock_choice):
    mock_sequence = list('aB1!cD2@eF3#')  # Includes all types
    mock_choice.side_effect = mock_sequence
    pw = generate_password()
    assert len(pw) == 12
    assert any(c.isupper() for c in pw)
    assert any(c.isdigit() for c in pw)
    assert any(c in string.punctuation for c in pw)


def test_generate_password_custom():
    pw = generate_password(
        length=16, include_upper=False, include_digits=True, include_symbols=False
    )
    assert len(pw) == 16
    assert not any(c.isupper() for c in pw), "No uppercase when excluded"
    assert any(c.isdigit() for c in pw), "Includes digits"


def test_generate_password_error_no_types():
    with pytest.raises(ValueError):
        generate_password(
            include_upper=False, include_digits=False, include_symbols=False
        )


def test_generate_password_min_length():
    pw = generate_password(length=8)
    assert len(pw) == 8


def test_generate_password_guarantees_types():
    pw = generate_password()
    assert any(c.islower() for c in pw)
    assert any(c.isupper() for c in pw)
    assert any(c.isdigit() for c in pw)
    assert any(c in string.punctuation for c in pw)

def test_generate_password_short_length_error():
    with pytest.raises(ValueError):
        generate_password(length=3)  # Hits remaining_length <0

@patch('secrets.choice')
def test_generate_password_custom_no_upper(mock_choice):
    mock_sequence = list('a1b2c3d4e5f6')
    mock_choice.side_effect = mock_sequence
    pw = generate_password(length=12, include_upper=False)
    assert not any(c.isupper() for c in pw)
