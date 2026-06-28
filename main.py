import re

def check_password_strength(password):
    if len(password) < 8:
        return "Weak: Password is too short"
    elif not re.search("[a-z]", password) or not re.search("[A-Z]", password) or not re.search("[0-9]", password):
        return "Medium: Password needs more variety (Upper, Lower, Numbers)"
    else:
        return "Strong: Great password!"

password = input("Enter password to check: ")
print(check_password_strength(password))
password = input("Enter password to check: ")

if len(password) < 8:
    print("Password is too short!")
else:
    print("Password length is okay.")