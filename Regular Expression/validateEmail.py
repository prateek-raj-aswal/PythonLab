import re

def validate_email(email):
    pattern = r'^[\w.-]+@[a-zA-Z]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, email):
        return "Valid email"
    else:
        return "Invalid email"

email = input("Enter an email: ")
print(validate_email(email))
