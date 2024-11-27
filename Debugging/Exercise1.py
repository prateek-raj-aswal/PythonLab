import pdb

def calculate_total(price, quantity):
    pdb.set_trace()
    total = price * quantity
    if total > 100:
        return "High"
    else:
        return "Low"

print(calculate_total(10, 5))
print(calculate_total('20', 3))  # This will raise a TypeError
