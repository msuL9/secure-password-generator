from src.generator import generate_password
from src.analyzer import analyze_strength

with open('data/weak_passwords.txt', 'r', encoding='utf-8') as f:
    weak_list = set(line.strip().lower() for line in f)

strong_count = 0
total = 500
for _ in range(total):
    pw = generate_password()
    result = analyze_strength(pw, weak_list)
    if result["score"] >= 80:  # Adjust threshold to match strong tier
        strong_count += 1
print(f"{strong_count}/{total} ({(strong_count/total)*100:.1f}%) passwords scored strong.")