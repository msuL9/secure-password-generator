# secure-password-generator

secure-password-generator is a Python command-line tool for generating cryptographically secure passwords and analyzing their strength against NIST SP 800-63B guidelines and local breached lists. Built as a preventive cybersecurity project, it emphasizes authentication best practices to mitigate risks like brute-force and dictionary attacks, drawing from Security+ (Sec+) certification knowledge and TryHackMe Cybersecurity 101 modules.

## Installation

1. Clone the repository: `git clone https://github.com/msuL9/secure-password-generator.git`
2. Navigate to the root: `cd secure-password-generator`
3. Create and activate a virtual environment: `python -m venv vulnenv` then `vulnenv\Scripts\activate` (Windows CMD) or `source vulnenv/bin/activate` (Unix/Git Bash).
4. Install dependencies: `pip install -r requirements.txt`

## Usage Examples

- Generate a password: `python src/main.py --length 16` (outputs a strong password with all character types).
- Exclude types: `python src/main.py --length 12 --no-symbols` (letters and digits only).
- Analyze strength: `python src/main.py --analyze 'ComplexUCI2025$!'` (use single quotes for special characters; outputs score and feedback).

## Features

- **Cryptographic Generation**: Uses `secrets` for randomness, guaranteeing at least one of each included type (lowercase, uppercase, digits, symbols) for NIST-compliant entropy.
- **Strength Analysis**: Scores passwords (0-100) based on length, complexity, and breached checks from a local RockYou subset, with tiered feedback (weak/moderate/strong) to educate on Sec+ risks like credential stuffing.
- **Uniqueness**: Local breached detection and mandatory diversity set it apart from basic generators, inspired by TryHackMe password cracking labs for real-world threat simulation.

## Testing

- Unit Tests: 15+ pytest cases with 100% coverage (via `coverage`), verifying guarantees like type inclusion and breached overrides.
- Bulk Metrics: 100% strong scores in 500 simulations, quantifying resistance to common attacks per Sec+ vulnerability management (domain 1.2).
- Run: `python -m pytest tests/` and `python -m coverage report`.

## Reflections

This project was intended to be a refresher on Python skills while also applying some of the knowledge that I gained from the Security+ and my Tryhackme experience.  Special thanks to Grok for helping me with planning and implementing the project.

## License

MIT License. See [LICENSE](LICENSE) for details.
