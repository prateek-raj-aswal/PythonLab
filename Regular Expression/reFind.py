import re

# Example 1: Validating an email
email = "example@example.com"
pattern = r'^[\w.-]+@[a-zA-Z]+\.[a-zA-Z]{2,}$'
if re.match(pattern, email):
    print("Valid email")
else:
    print("Invalid email")

# Example 2: Extracting phone numbers
text = "Contact us at 123-456-7890 or 987-654-3210."
phone_pattern = r'\d{3}-\d{3}-\d{4}'
phones = re.findall(phone_pattern, text)
print("Extracted phone numbers:", phones)
