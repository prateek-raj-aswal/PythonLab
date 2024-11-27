class NegativeValueError(Exception):
    pass

try:
    num = int(input("Enter a positive number: "))
    if num < 0:
        raise NegativeValueError("Negative value entered!")
    print(f"Number: {num}")
except NegativeValueError as e:
    print(e)
