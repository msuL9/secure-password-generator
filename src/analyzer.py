import string

def analyze_strength(password, weak_list):
    score = 0

    # Length check (NIST recommends >=8, bonus for >=12)
    if len(password) >= 12:
        score += 30
    elif len(password) >= 8:
        score += 20
    else:
        feedback.append("Too short: Minimum 8 characters per NIST SP 800-63B. ")

    if any(c.isupper() for c in password):
        score += 20
    else:
        feedback.append("Add uppercase letters for better complexity. ")

    if any(c.isdigit() for c in password):
        score += 15
    else:
        feedback.append("Add digits for better complexity. ")

    if any(c in string.punctuation for c in password):
        score += 15
    else:
        feedback.append("Add symbols for better complexity. ")

    # Breached check (overrides to 0 if matched)
    if password.lower() in weak_list:
        score = 0
        feedback.append("Password is in breached list—change immediately to avoid attacks. ")

    if score < 50 and not feedback:
        feedback.append("Weak: Add more length/complexity per NIST.")
    elif score < 80:
        feedback.append("Moderate: Consider adding more complexity.")
    
    return {"score": score, "feedback": feedback}