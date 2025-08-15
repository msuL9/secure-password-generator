import pytest
from src.analyzer import analyze_strength


@pytest.fixture
def sample_weak_list():
    return {"password", "123456", "qwerty"}  # Mock small set for tests


def test_analyze_strength_strong(sample_weak_list):
    result = analyze_strength("StrongPass123!", sample_weak_list)
    assert result["score"] >= 80, "Strong password should score high"
    assert not result["feedback"], "No feedback for strong passwords"


def test_analyze_strength_weak_length(sample_weak_list):
    result = analyze_strength("short", sample_weak_list)
    assert result["score"] < 50
    assert any("Too short" in fb for fb in result["feedback"])


def test_analyze_strength_breached(sample_weak_list):
    result = analyze_strength("password", sample_weak_list)
    assert result["score"] == 0
    assert any("breached" in fb for fb in result["feedback"])


def test_analyze_strength_missing_types(sample_weak_list):
    result = analyze_strength("alllowercase12", sample_weak_list)
    assert "Add uppercase" in " ".join(result["feedback"])
    assert "Add symbols" in " ".join(result["feedback"])
