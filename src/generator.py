import secrets
import string

def generate_password(length=12, include_upper=True, include_digits=True, include_symbols=True):
    # Build character set based on user preferences
    chars = string.ascii_lowercase  # Always include lowercase for base entropy
    if include_upper:
        chars += string.ascii_uppercase
    if include_digits:
        chars += string.digits
    if include_symbols:
        chars += string.punctuation
    
    # Ensure at least one additional character type is selected (beyond lowercase)
    if len(chars) == len(string.ascii_lowercase):
        raise ValueError("Must include at least one of: uppercase, digits, or symbols for security.")
    
    # Generate secure password using secrets for cryptographic randomness
    return ''.join(secrets.choice(chars) for _ in range(length))