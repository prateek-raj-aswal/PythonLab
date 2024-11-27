from utilities.string_utils import to_uppercase, reverse_string
from utilities.list_utils import get_max, get_min

# Test string utilities
print("Uppercase:", to_uppercase("hello"))
print("Reversed string:", reverse_string("world"))

# Test list utilities
numbers = [10, 20, 5, 40, 15]
print("Maximum:", get_max(numbers))
print("Minimum:", get_min(numbers))
