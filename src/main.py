# src/main.py (updated for argparse bug workaround)
import argparse
from generator import generate_password
from analyzer import analyze_strength


def main():
    # Load weak passwords list (case-insensitive)
    try:
        with open("data/weak_passwords.txt", "r", encoding="utf-8") as f:
            weak_list = set(line.strip().lower() for line in f)
    except FileNotFoundError:
        print("Error: weak_passwords.txt not found in data/. Please create it.")
        return

    # Set up CLI with mutual exclusive groups for modes
    parser = argparse.ArgumentParser(
        description="SecurePassGen: Generate or analyze strong passwords"
    )
    mode_group = parser.add_mutually_exclusive_group(
        required=False
    )  # Modes: generate (default) or analyze

    # Generation options (default mode) - Set default=None to workaround argparse bug #18943
    mode_group.add_argument(
        "--length",
        type=int,
        default=None,
        help="Password length (minimum 8 for NIST compliance)",
    )
    parser.add_argument(
        "--no-upper",
        action="store_false",
        dest="include_upper",
        help="Exclude uppercase letters",
    )
    parser.add_argument(
        "--no-digits",
        action="store_false",
        dest="include_digits",
        help="Exclude digits",
    )
    parser.add_argument(
        "--no-symbols",
        action="store_false",
        dest="include_symbols",
        help="Exclude special symbols",
    )

    # Analysis mode
    mode_group.add_argument(
        "--analyze",
        type=str,
        help="Analyze the strength of a given password (e.g., --analyze 'myPass123')",
    )

    args = parser.parse_args()

    if args.analyze:
        # Analysis mode
        result = analyze_strength(args.analyze, weak_list)
        print(f"Password: {args.analyze}")
        print(f"Strength Score: {result['score']}/100")
        if result["feedback"]:
            print("Feedback:")
            for fb in result["feedback"]:
                print(f"- {fb}")
        else:
            print("Strong password! Meets NIST complexity.")
    else:
        # Generation mode - Handle default length manually due to argparse bug
        if args.length is None:
            args.length = 12
        if args.length < 8:
            print(
                "Error: Password length must be at least 8 characters per NIST guidelines."
            )
            return
        try:
            password = generate_password(
                length=args.length,
                include_upper=args.include_upper,
                include_digits=args.include_digits,
                include_symbols=args.include_symbols,
            )
            print(f"Generated password: {password}")
        except ValueError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
