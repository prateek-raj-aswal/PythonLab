# name = input("What is your name? ")
# age = int(input("What is your age? "))
# if age >= 18:
#     print(f"Hi {name}, you’re an adult!")
# else:
#     print(f"Hi {name}, you’re a minor!")

price = 100
quantity = 2
tax_rate = 0.1
discount = 0.2 if quantity > 1 else 0

total_price = (price * quantity) * (1 + tax_rate)
final_price = total_price * (1 - discount)

print("Total Price (after tax):", total_price)
print("Final Price (after discount):", final_price)
