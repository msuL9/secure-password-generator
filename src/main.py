import argparse
from generator import generate_password

def main():
    parser = argparse.ArgumentParser(description="SecurePassGen: Generate strong passwords")
    # Default length is 15 in in complicane with NIST recommendations
    parser.add_argument("--length", type=int, default=15, help="Password length")
    # Password complexity is optional as per NIST guidelines
    parser.add_argument("--no-upper", action="store_false", dest="include_upper", help="Exclude uppercase letters")
    parser.add_argument("--no-digits", action="store_false", dest="include_digits", help="Exclude digits")
    parser.add_argument("--no-symbols", action="store_false", dest="include_symbols", help="Exclude special symbols")

    args = parser.parse_args()

    # Input Validation
    if args.length < 8:
        print("Error: Password length must be at least 8 characters as recommended per NIST guidelines.")
        return

    if args.length > 64:
        print("Error: Password length cannot be more than 64 characters as recommended per NIST guidelines.")
        return

    try:
        password= generate_password(
                length=args.length,
                include_upper=args.include_upper,
                include_digits=args.include_digits,
                include_symbols=args.include_symbols
                )
        print(f"Generated password: {password}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
