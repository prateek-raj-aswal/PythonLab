import re

def validate_password(password):
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*(),.?":{}|<>])(?=.*\d).{8,}$'
    return bool(re.match(pattern, password))

password = input("Enter a password: ")
print("Valid Password" if validate_password(password) else "Invalid Password")
