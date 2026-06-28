import re
import math

# Load common weak passwords from file
with open("common_password.txt") as f:
    common_passwords = [line.strip() for line in f]

def check_password_strength(password):
    score = 0
    suggestions = []

    # Length check
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters.")

    # Uppercase check
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("Add uppercase letters.")

    # Lowercase check
    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Add lowercase letters.")

    # Digit check
    if re.search(r"[0-9]", password):
        score += 1
    else:
        suggestions.append("Add numbers.")

    # Special character check
    if re.search(r"[@$!%*?&]", password):
        score += 1
    else:
        suggestions.append("Add special characters (@, $, !, %, *, ?, &).")

    # Dictionary check
    if password.lower() in common_passwords:
        suggestions.append("Avoid common passwords like '123456' or 'password'.")
        score = 0

    # Entropy calculation (approx)
    charset = 0
    if re.search(r"[a-z]", password): charset += 26
    if re.search(r"[A-Z]", password): charset += 26
    if re.search(r"[0-9]", password): charset += 10
    if re.search(r"[@$!%*?&]", password): charset += 8
    entropy = len(password) * math.log2(charset) if charset else 0

    # Final strength
    if score >= 5 and entropy > 50:
        strength = "Strong Password"
    elif score >= 3:
        strength = "Medium Password"
    else:
        strength = "Weak Password"

    return strength, suggestions, round(entropy, 2)

# --- Main Program ---
if __name__ == "__main__":
    pwd = input("Enter your password: ")
    strength, suggestions, entropy = check_password_strength(pwd)

    print("Password Strength:", strength)
    print("Entropy Score:", entropy)
    if suggestions:
        print("Suggestions:")
        for s in suggestions:
            print("-", s)
