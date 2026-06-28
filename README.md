 Password Strength Checker

 Aim
To develop a Python-based tool that evaluates the strength of user passwords by analyzing multiple security parameters and providing actionable suggestions for improvement.

---

 Objectives
- Check password length and complexity.
- Verify the presence of uppercase, lowercase, digits, and special characters.
- Detect weak/common passwords using a dictionary file.
- Calculate password entropy to estimate resistance against brute-force attacks.
- Provide clear feedback and suggestions to strengthen weak passwords.

---

Tools & Technologies
- **Programming Language:** Python 3.x
- **Libraries Used:** `re`, `math`
- **Files:**
  - `password_strength.py` → Main program
  - `common_passwords.txt` → List of weak/common passwords
  - `results/` → Screenshots of test outputs

---

 Implementation
1. User enters a password in the terminal.
2. The program checks:
   - Length of the password
   - Character variety (uppercase, lowercase, digits, special characters)
   - Presence in the weak password list (`common_passwords.txt`)
   - Entropy score (mathematical measure of password strength)
3. Based on these checks, the program classifies the password as:
   - **Weak**
   - **Medium**
   - **Strong**
4. Suggestions are displayed to help the user improve their password.

---

 Results

| Password Tested      | Strength | Suggestions                          |
|----------------------|----------|--------------------------------------|
| 123456               | Weak     | Avoid common passwords               |
| Pandey123            | Medium   | Add special characters               |
| Pandey@2026Secure    | Strong   | No suggestions                       |

Screenshots of outputs are available in the `results/` folder.

---
 Conclusion
This project demonstrates how Python can be used to evaluate password strength and raise awareness about secure password practices. By checking length, complexity, dictionary words, and entropy, the tool helps users create stronger passwords and protect themselves against cyber attacks.

---

 How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/<username>/PasswordStrengthChecker
