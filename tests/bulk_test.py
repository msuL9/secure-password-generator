# tests/bulk_test.py (run with python tests/bulk_test.py)
from src.generator import generate_password
from src.analyzer import analyze_strength

# Load your actual weak_list (or mock for quick runs)
with open('data/weak_passwords.txt', 'r', encoding='utf-8') as f:
    weak_list = set(line.strip().lower() for line in f)

strong_count = 0
total = 500  # Bulk: Generate/analyze 500 for resume stats
for _ in range(total):
    pw = generate_password()  # Defaults: Strong by design
    result = analyze_strength(pw, weak_list)
    if result["score"] >= 70:
        strong_count += 1
print(f"{strong_count}/{total} ({(strong_count/total)*100:.1f}%) passwords scored strong.")