import string


def analyze_strength(password, weak_list):
    """
    Analyzes password strength based on NIST guidelines.
    Score: 0-100 (higher = stronger).
    Checks: length, uppercase, digits, symbols, breached status.
    """
    score = 0
    feedback = []

    # Length check (NIST recommends >=8, bonus for >=12)
    if len(password) >= 12:
        score += 30
    elif len(password) >= 8:
        score += 20
    else:
        feedback.append("Too short: Minimum 8 characters per NIST SP 800-63B.")

    # Character type checks for complexity (balanced at +20 each for max 90 with length bonus)
    if any(c.isupper() for c in password):
        score += 20
    else:
        feedback.append("Add uppercase letters for better complexity.")

    if any(c.isdigit() for c in password):
        score += 20
    else:
        feedback.append("Add digits for better complexity.")

    if any(c in string.punctuation for c in password):
        score += 20
    else:
        feedback.append("Add symbols for better complexity.")

    # Breached check (overrides to 0 if matched)
    if password.lower() in weak_list:
        score = 0
        feedback.append(
            "Password is in breached list—change immediately to avoid attacks."
        )

    # Tiered overall feedback (adjusted thresholds for nuance: moderate 50-79, strong >=80 no extra)
    if score < 80 and score >= 50:
        feedback.append(
            "Moderate: Consider adding more character types for optimal strength."
        )

    return {"score": score, "feedback": feedback}
