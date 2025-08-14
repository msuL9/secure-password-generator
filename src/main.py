import argparse
from generator import generate_password

parser = argparse.ArgumentParser(description="SecurePassGen: Generate strong passwords")
parser.add_argument("--length", type=int, default=12, help="Password length")
parser.add_argument("--no-upper", action="store_false", help="Exclude uppercase")
# Add similar for digits/symbols
args = parser.parse_args()

pw = generate_password(args.length, args.no_upper)  # Adjust args
print(f"Generated: {pw}")
