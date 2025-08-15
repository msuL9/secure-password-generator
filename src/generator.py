import secrets
import string
import random  # For shuffling


def generate_password(
    length=12, include_upper=True, include_digits=True, include_symbols=True
):
    chars = string.ascii_lowercase
    if include_upper:
        chars += string.ascii_uppercase
    if include_digits:
        chars += string.digits
    if include_symbols:
        chars += string.punctuation

    if len(chars) == len(string.ascii_lowercase):
        raise ValueError(
            "Must include at least one of: uppercase, digits, or symbols for security."
        )

    # Guarantee at least one of each included type (if selected)
    password_list = []
    password_list.append(secrets.choice(string.ascii_lowercase))  # Always one lower
    if include_upper:
        password_list.append(secrets.choice(string.ascii_uppercase))
    if include_digits:
        password_list.append(secrets.choice(string.digits))
    if include_symbols:
        password_list.append(secrets.choice(string.punctuation))

    # Fill remaining length randomly
    remaining_length = length - len(password_list)
    if remaining_length < 0:
        raise ValueError("Length too short for required character types.")
    password_list.extend(secrets.choice(chars) for _ in range(remaining_length))

    # Shuffle for unpredictability
    random.shuffle(password_list)
    return "".join(password_list)
