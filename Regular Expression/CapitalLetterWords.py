import re

text = "Alice is a Software Developer at OpenAI."
pattern = r'\b[A-Z][a-zA-Z]*'
print("Capitalized Words:", re.findall(pattern, text))
