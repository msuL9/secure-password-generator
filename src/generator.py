import secrets
import string

def generate_password(length=12, include_upper=True, include_digits=True, include_symbols=True):
    chars = string.ascii_lowercase
    if include_upper:
        chars += string.ascii_uppercase
    if include_digits:
        chars += string.digits
    if include_symbols:
        chars += string.punctuation

    # Uses secrets.choice instead of random.choice for cryptographically secure randomness
    return ''.join(secrets.choice(chars) for _ in range(length))
