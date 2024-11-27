import re

# Input text with phone numbers
text = "Contact John at 123-456-7890 or Jane at 987-654-3210 for more details."

# Pattern to match phone numbers
phone_pattern = r'\d{3}-\d{3}-\d{4}'

# Replace phone numbers with a masked version
masked_text = re.sub(phone_pattern, 'XXX-XXX-XXXX', text)

print("Original Text:", text)
print("Masked Text:", masked_text)
